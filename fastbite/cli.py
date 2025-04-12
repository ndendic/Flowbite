import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
import subprocess
from pathlib import Path
import platform
import sys
from typing import Optional
from urllib.request import urlretrieve
import os
import pkg_resources
from .config import load_config, Config, DEFAULT_CONFIG

app = typer.Typer(help="FastBite CLI tool for project management")
console = Console()

def get_template_content(template_name: str) -> str:
    """Get the content of a template file from the templates directory"""
    template_path = Path(__file__).parent / "templates" / template_name
    if not template_path.exists():
        raise FileNotFoundError(f"Template {template_name} not found at {template_path}")
    return template_path.read_text()

def get_project_root() -> Path:
    """Get the project root directory (where the command is being run)"""
    return Path.cwd()

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
    """Get the path to the Tailwind binary in the project root"""
    return get_project_root() / get_tailwind_binary_name()

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

def create_input_css(path: Path) -> None:
    """Create an optimized input.css file for Tailwind v4"""
    try:
        content = get_template_content("base_theme.css")
        with open(path, "w") as f:
            f.write(content)
    except Exception as e:
        console.print(f"[red]Error:[/] Failed to create input.css: {str(e)}")
        raise typer.Exit(1)

def install_tailwind(
    force: bool = typer.Option(False, "--force", "-f", help="Force reinstall even if Tailwind CLI exists"),
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed debug information")
):
    """Install Tailwind CSS standalone CLI for your system."""
    try:
        system, is_arm, is_64bit = get_system_info()
        
        with console.status("[bold green]Detecting system architecture...") as status:
            tailwind_url, tailwind_filename = get_tailwind_url(system, is_arm, is_64bit)
            status.update(f"[bold green]Detected: {system} {'ARM64' if is_arm else 'x64'}")
            
            if verbose:
                console.print(f"[dim]Debug: Downloading from {tailwind_url}[/dim]")
            
            # Determine installation path
            if install_path:
                install_dir = Path(install_path)
            else:
                # Default to project root
                install_dir = get_project_root()
            
            full_path = install_dir / tailwind_filename
            
            if full_path.exists() and not force:
                console.print(f"[yellow]Tailwind CLI already exists at: {full_path}")
                console.print("[yellow]Use --force to reinstall")
                return full_path
            
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
            
            return full_path
            
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to install Tailwind CLI: {str(e)}")
        if verbose:
            import traceback
            console.print("[dim]" + traceback.format_exc() + "[/dim]")
        raise typer.Exit(1)

def update_package():
    """Update the fastbite package using pip"""
    try:
        with console.status("[bold green]Checking for FastBite updates...") as status:
            # Check if package is installed via pip
            try:
                from importlib.metadata import version, PackageNotFoundError
                try:
                    current_version = version("fastbite")
                except PackageNotFoundError:
                    console.print("[yellow]FastBite package not installed via pip, skipping update")
                    return

                # Create pip cache directory if it doesn't exist
                pip_cache_dir = Path.home() / ".cache" / "pip"
                pip_cache_dir.mkdir(parents=True, exist_ok=True)

                # Use python -m pip to ensure we're using the right pip
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", "--upgrade", "fastbite"],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    try:
                        new_version = version("fastbite")
                        if new_version != current_version:
                            console.print(f"[bold green]✓[/] FastBite updated from version {current_version} to {new_version}")
                        else:
                            console.print(f"[bold green]✓[/] FastBite is already at the latest version ({current_version})")
                    except Exception:
                        console.print("[bold green]✓[/] FastBite updated successfully")
                else:
                    if "No matching distribution found" in result.stderr:
                        console.print("[yellow]No updates available for FastBite")
                    else:
                        console.print(f"[red]Error during update:[/] {result.stderr}")
            except ImportError:
                console.print("[red]Error:[/] Could not import required modules for version checking")
                    
    except Exception as e:
        console.print(f"[red]Error:[/] Could not update package: {str(e)}")

@app.command()
def init(
    force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing configuration"),
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path for Tailwind binary"),
    default_paths: bool = typer.Option(False, "--default", "-d", help="Use default paths without prompting")
):
    """Initialize FastBite project configuration and install Tailwind CLI."""
    try:
        # First, check if we need to install Tailwind
        binary_path = get_binary_path()
        if not binary_path.exists():
            console.print("[yellow]Tailwind CLI not found. Installing...[/]")
            binary_path = install_tailwind(force=force, install_path=install_path)
        
        config = load_config()
        if config.config_path.exists() and not force:
            console.print("[yellow]Configuration file already exists. Use --force to overwrite.")
            return

        # Interactive path configuration if not using defaults
        if not default_paths:
            console.print("\n[bold]CSS Path Configuration[/]")
            console.print(f"Default input path: [dim]{DEFAULT_CONFIG['paths']['css']['input']}[/dim]")
            console.print(f"Default output path: [dim]{DEFAULT_CONFIG['paths']['css']['output']}[/dim]")
            
            if Confirm.ask("Would you like to customize the CSS paths?", default=False):
                input_path = Prompt.ask(
                    "Enter the path for your input CSS file",
                    default=DEFAULT_CONFIG['paths']['css']['input']
                )
                output_path = Prompt.ask(
                    "Enter the path for your output CSS file",
                    default=DEFAULT_CONFIG['paths']['css']['output']
                )
                
                # Update config with custom paths
                config._config['paths']['css']['input'] = input_path
                config._config['paths']['css']['output'] = output_path
            else:
                console.print("[dim]Using default paths...[/dim]")
        
        with console.status("[bold green]Initializing project...") as status:
            # Create assets directory structure
            config.css_input_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create initial CSS file if it doesn't exist or force is True
            if not config.css_input_path.exists() or force:
                status.update("Creating optimized input.css for Tailwind v4...")
                create_input_css(config.css_input_path)
            
            # Save configuration
            status.update("Saving configuration...")
            config.save()
        
        console.print("\n[bold green]✓[/] Project initialized successfully!")
        console.print(f"[dim]Configuration saved to: {config.config_path}[/dim]")
        console.print(f"[dim]Input CSS file: {config.css_input_path}[/dim]")
        console.print(f"[dim]Output CSS file: {config.css_output_path}[/dim]")
        console.print(f"[dim]Tailwind binary installed at: {binary_path}[/dim]")
        
        # Show the watch command hint based on the paths
        console.print("\nNext steps:")
        console.print("1. Run [bold]`fastbite build`[/] to generate your CSS")
        console.print("2. Or run [bold]`fastbite dev`[/] to start development mode")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to initialize project: {str(e)}")
        raise typer.Exit(1)

@app.command()
def build(
    minify: bool = typer.Option(False, "--minify", "-m", help="Minify the output CSS"),
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path for Tailwind binary")
):
    """Build Tailwind CSS once."""
    try:
        config = load_config()
        binary_path = get_binary_path()
        
        if not binary_path.exists():
            console.print("[yellow]Tailwind CLI not found. Installing...")
            binary_path = install_tailwind(force=False, install_path=install_path)
        
        run_tailwind_command(config, binary_path, watch=False)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to build CSS: {str(e)}")
        raise typer.Exit(1)

@app.command()
def dev(
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path for Tailwind binary")
):
    """Start Tailwind CSS in watch mode for development."""
    try:
        config = load_config()
        binary_path = get_binary_path()
        
        if not binary_path.exists():
            console.print("[yellow]Tailwind CLI not found. Installing...")
            binary_path = install_tailwind(force=False, install_path=install_path)
        
        run_tailwind_command(config, binary_path, watch=True)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to start watch mode: {str(e)}")
        raise typer.Exit(1)

@app.command()
def update(
    skip_package: bool = typer.Option(False, "--skip-package", help="Skip updating the FastBite package"),
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path for Tailwind binary"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed debug information")
):
    """Update Tailwind binary and FastBite package to their latest versions."""
    try:
        console.print("[bold]Starting update process...[/]")
        
        # Update FastBite package first
        if not skip_package:
            update_package()
        
        # Get current binary path
        binary_path = get_binary_path() if not install_path else Path(install_path) / get_tailwind_binary_name()
        
        # Create directory if it doesn't exist
        binary_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if binary exists
        if binary_path.exists():
            console.print(f"\n[dim]Removing existing Tailwind binary at: {binary_path}[/dim]")
            try:
                binary_path.unlink()
            except Exception as e:
                console.print(f"[yellow]Warning: Could not remove existing binary: {str(e)}")
                console.print("[yellow]You may need to remove it manually or run with elevated privileges")
                return
        
        # Install new binary
        console.print("\n[bold]Installing latest Tailwind version...[/]")
        new_binary_path = install_tailwind(force=True, install_path=install_path)
        
        if new_binary_path and new_binary_path.exists():
            # Try to get Tailwind version without outputting CSS
            try:
                version_result = subprocess.run(
                    [str(new_binary_path), "--help"],
                    capture_output=True,
                    text=True
                )
                if version_result.returncode == 0:
                    # Extract version from help output - it's usually in the first line
                    version_line = version_result.stdout.splitlines()[0]
                    if "tailwindcss" in version_line.lower():
                        console.print(f"[bold green]✓[/] {version_line.strip()}")
                    else:
                        console.print("[bold green]✓[/] Tailwind CLI updated to latest version")
                else:
                    console.print("[bold green]✓[/] Tailwind CLI updated to latest version")
            except Exception as e:
                if verbose:
                    console.print(f"[dim]Could not get version info: {str(e)}[/dim]")
                console.print("[bold green]✓[/] Tailwind CLI updated to latest version")
        
        console.print("\n[bold green]Update completed successfully![/]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/] Update failed: {str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
