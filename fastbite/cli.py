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

def create_input_css(path: Path) -> None:
    """Create an optimized input.css file for Tailwind v4"""
    content = """@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom dark mode variant - more targeted approach */
@custom-variant dark (&:where(.dark, .dark *));

/* Theme configuration using CSS variables */
@theme {
    /* Primary colors - Rose theme by default */
    --color-primary-50: #fff1f2;
    --color-primary-100: #ffe4e6;
    --color-primary-200: #fecdd3;
    --color-primary-300: #fda4af;
    --color-primary-400: #fb7185;
    --color-primary-500: #f43f5e;
    --color-primary-600: #e11d48;
    --color-primary-700: #be123c;
    --color-primary-800: #9f1239;
    --color-primary-900: #881337;
    --color-primary-950: #4c0519;

    /* Gray scale */
    --color-gray-50: #fafafa;
    --color-gray-100: #f4f4f5;
    --color-gray-200: #e4e4e7;
    --color-gray-300: #d4d4d8;
    --color-gray-400: #a1a1aa;
    --color-gray-500: #71717a;
    --color-gray-600: #52525b;
    --color-gray-700: #3f3f46;
    --color-gray-800: #27272a;
    --color-gray-900: #18181b;
    --color-gray-950: #09090b;

    /* Font stacks */
    --font-sans: 'Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', sans-serif;
    --font-mono: 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', monospace;
}

/* Dark mode overrides */
html.dark {
    color-scheme: dark;
}

/* Ensure proper inheritance */
.bg-inherit {
    background-color: inherit;
}

/* Optional theme variations - can be activated with data-theme attribute */
@layer base {
    [data-theme='emerald'] {
        --color-primary-50: #ecfdf5;
        --color-primary-100: #d1fae5;
        --color-primary-200: #a7f3d0;
        --color-primary-300: #6ee7b7;
        --color-primary-400: #34d399;
        --color-primary-500: #10b981;
        --color-primary-600: #059669;
        --color-primary-700: #047857;
        --color-primary-800: #065f46;
        --color-primary-900: #064e3b;
        --color-primary-950: #022c22;
    }

    [data-theme='amber'] {
        --color-primary-50: #fffbeb;
        --color-primary-100: #fef3c7;
        --color-primary-200: #fde68a;
        --color-primary-300: #fcd34d;
        --color-primary-400: #fbbf24;
        --color-primary-500: #f59e0b;
        --color-primary-600: #d97706;
        --color-primary-700: #b45309;
        --color-primary-800: #92400e;
        --color-primary-900: #78350f;
        --color-primary-950: #451a03;
    }
}
"""
    with open(path, "w") as f:
        f.write(content)

@app.command()
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
                # Default to scripts directory in the package
                install_dir = Path(__file__).parent.parent / "scripts"
            
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

@app.command()
def init(
    force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing configuration"),
    install_path: Optional[str] = typer.Option(None, "--path", "-p", help="Custom installation path for Tailwind binary")
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
        
        with console.status("[bold green]Initializing project...") as status:
            # Create assets directory structure
            config.assets_path.mkdir(parents=True, exist_ok=True)
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
        console.print(f"[dim]CSS file created at: {config.css_input_path}[/dim]")
        console.print("\nNext steps:")
        console.print("1. Run [bold]fastbite build[/] to generate your CSS")
        console.print("2. Or run [bold]fastbite watch[/] to start development mode")
        
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
def watch(
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

if __name__ == "__main__":
    app()
