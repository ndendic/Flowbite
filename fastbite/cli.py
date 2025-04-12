import typer
from rich import print
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import subprocess
from pathlib import Path
import platform
import sys
from typing import Optional
from urllib.request import urlretrieve
import os
from .config import load_config, Config

app = typer.Typer(help="FastBite CLI tool for project management")
console = Console()

def get_tailwind_binary_name() -> str:
    """Get the appropriate Tailwind binary name for the current platform"""
    return "tailwindcss.exe" if platform.system().lower() == "windows" else "tailwindcss"

def is_wsl() -> bool:
    """Check if running under Windows Subsystem for Linux"""
    try:
        with open('/proc/version', 'r') as f:
            return 'microsoft' in f.read().lower()
    except:
        return False

def get_system_info():
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    is_arm = 'arm' in machine or 'aarch64' in machine
    is_64bit = '64' in machine or 'amd64' in machine
    
    # Handle WSL case
    if system == 'linux' and is_wsl():
        system = 'wsl'
        
    console.print(f"[dim]Debug: Detected system={system}, machine={machine}, is_arm={is_arm}, is_64bit={is_64bit}[/dim]")
    return system, is_arm, is_64bit

def get_tailwind_url(system: str, is_arm: bool, is_64bit: bool) -> tuple[str, str]:
    base_url = "https://github.com/tailwindlabs/tailwindcss/releases/latest/download/"
    binary_name = get_tailwind_binary_name()
    
    if system == "windows":
        return f"{base_url}tailwindcss-windows-x64.exe", binary_name
    
    if system == "darwin":  # macOS
        if is_arm:
            return f"{base_url}tailwindcss-macos-arm64", binary_name
        return f"{base_url}tailwindcss-macos-x64", binary_name
    
    # Linux or WSL
    if system in ('linux', 'wsl'):
        if is_arm and is_64bit:
            return f"{base_url}tailwindcss-linux-arm64", binary_name
        return f"{base_url}tailwindcss-linux-x64", binary_name
    
    raise ValueError(f"Unsupported system: {system} (machine: {platform.machine()})")

def get_binary_path() -> Path:
    """Get the path to the Tailwind binary"""
    return Path(__file__).parent.parent / "scripts" / get_tailwind_binary_name()

def run_tailwind_command(config: Config, binary_path: Path, watch: bool = False) -> None:
    """Run Tailwind CLI with the specified configuration"""
    cmd = [
        str(binary_path),
        "-i", str(config.css_input_path),
        "-o", str(config.css_output_path),
    ]
    
    if config.should_minify:
        cmd.append("--minify")
    
    if watch:
        cmd.append("--watch")
    
    try:
        if watch:
            console.print("[bold green]Starting Tailwind CSS in watch mode...[/]")
            subprocess.run(cmd)
        else:
            with console.status("[bold green]Building CSS...[/]"):
                subprocess.run(cmd, check=True, capture_output=True)
            console.print("[bold green]✓[/] CSS built successfully!")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error:[/] Failed to run Tailwind: {e.stderr.decode()}")
        raise typer.Exit(1)

@app.command()
def install_tailwind(
    force: bool = typer.Option(False, "--force", "-f", help="Force reinstall even if Tailwind CLI exists"),
    path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed debug information")
):
    """
    Install Tailwind CSS standalone CLI for your system.
    """
    try:
        system, is_arm, is_64bit = get_system_info()
        
        with console.status("[bold green]Detecting system architecture...") as status:
            tailwind_url, tailwind_filename = get_tailwind_url(system, is_arm, is_64bit)
            status.update(f"[bold green]Detected: {system} {'ARM64' if is_arm else 'x64'}")
            
            if verbose:
                console.print(f"[dim]Debug: Downloading from {tailwind_url}[/dim]")
            
            # Determine installation path
            if path:
                install_dir = Path(path)
            else:
                install_dir = Path(__file__).parent.parent / "scripts"
            
            full_path = install_dir / tailwind_filename
            
            if full_path.exists() and not force:
                console.print(f"[yellow]Tailwind CLI already exists at: {full_path}")
                console.print("[yellow]Use --force to reinstall")
                return
            
            # Ensure directory exists
            install_dir.mkdir(parents=True, exist_ok=True)
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description=f"Downloading Tailwind CLI from {tailwind_url}...", total=None)
                urlretrieve(tailwind_url, full_path)
            
            # Make executable on Unix-based systems
            if system != "windows":
                os.chmod(full_path, 0o755)
            
            console.print(f"[bold green]✓[/] Tailwind CLI installed successfully at: {full_path}")
            
            if verbose:
                console.print(f"[dim]Debug: File permissions set to: {oct(os.stat(full_path).st_mode)[-3:]}[/dim]")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to install Tailwind CLI: {str(e)}")
        if verbose:
            import traceback
            console.print("[dim]" + traceback.format_exc() + "[/dim]")
        raise typer.Exit(1)

@app.command()
def init(
    force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing configuration"),
):
    """Initialize FastBite project configuration."""
    try:
        config = load_config()
        if config.config_path.exists() and not force:
            console.print("[yellow]Configuration file already exists. Use --force to overwrite.")
            return
        
        # Create assets directory structure
        config.assets_path.mkdir(parents=True, exist_ok=True)
        config.css_input_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create initial CSS file if it doesn't exist
        if not config.css_input_path.exists():
            with open(config.css_input_path, "w") as f:
                f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")
        
        # Save configuration
        config.save()
        console.print("[bold green]✓[/] Project initialized successfully!")
        console.print(f"[dim]Configuration saved to: {config.config_path}[/dim]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to initialize project: {str(e)}")
        raise typer.Exit(1)

@app.command()
def build(
    minify: bool = typer.Option(False, "--minify", "-m", help="Minify the output CSS"),
):
    """Build Tailwind CSS once."""
    try:
        config = load_config()
        binary_path = get_binary_path()
        
        if not binary_path.exists():
            console.print("[yellow]Tailwind CLI not found. Installing...")
            install_tailwind()
            binary_path = get_binary_path()  # Get the path again after installation
        
        run_tailwind_command(config, binary_path, watch=False)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to build CSS: {str(e)}")
        raise typer.Exit(1)

@app.command()
def watch():
    """Start Tailwind CSS in watch mode for development."""
    try:
        config = load_config()
        binary_path = get_binary_path()
        
        if not binary_path.exists():
            console.print("[yellow]Tailwind CLI not found. Installing...")
            install_tailwind()
            binary_path = get_binary_path()  # Get the path again after installation
        
        run_tailwind_command(config, binary_path, watch=True)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to start watch mode: {str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
