from pathlib import Path
import tomli
import tomli_w
from typing import Dict, Any, Optional

DEFAULT_CONFIG = {
    "paths": {
        "assets": "assets",
        "css": {
            "input": "assets/css/input.css",
            "output": "assets/css/output.css"
        }
    },
    "tailwind": {
        "config": "tailwind.config.js",
        "minify": False
    }
}

class Config:
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path("fastbite.toml")
        self._config = self.load_or_create()
    
    def load_or_create(self) -> Dict[str, Any]:
        """Load existing config or create with defaults"""
        if self.config_path.exists():
            with open(self.config_path, "rb") as f:
                return tomli.load(f)
        return DEFAULT_CONFIG.copy()
    
    def save(self) -> None:
        """Save current configuration to file"""
        with open(self.config_path, "wb") as f:
            tomli_w.dump(self._config, f)
    
    @property
    def css_input_path(self) -> Path:
        return Path(self._config["paths"]["css"]["input"])
    
    @property
    def css_output_path(self) -> Path:
        return Path(self._config["paths"]["css"]["output"])
    
    @property
    def assets_path(self) -> Path:
        return Path(self._config["paths"]["assets"])
    
    @property
    def tailwind_config_path(self) -> Path:
        return Path(self._config["tailwind"]["config"])
    
    @property
    def should_minify(self) -> bool:
        return self._config["tailwind"]["minify"]

def load_config(config_path: Optional[Path] = None) -> Config:
    """Load configuration from file or create with defaults"""
    return Config(config_path) 