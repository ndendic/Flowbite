import os
import importlib
from pathlib import Path
import inspect
from fasthtml.components import *
from fh_flowbite.components import *
import traceback

class ComponentRegistry:
    def __init__(self):
        self.components = {}
        self.extracted_dir = Path("app/extracted")
        self._scan_components()
    
    def _scan_components(self):
        """Scan the extracted directory for component files and import them"""
        if not self.extracted_dir.exists():
            print(f"Warning: {self.extracted_dir} directory not found")
            return
        
        for file_path in self.extracted_dir.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
                
            component_name = file_path.stem  # filename without extension
            route_path = f"/{component_name.lower()}"
            display_name = " ".join(word.capitalize() for word in component_name.split("_"))
            
            try:
                # Import the module
                module = importlib.import_module(f"extracted.{component_name}")
                
                # Find the component in the module - first check for a 'component' attribute
                component = getattr(module, "component", None)
                
                # If not found, look for any exportable function/class
                if component is None:
                    for name, obj in inspect.getmembers(module):
                        if not name.startswith('_') and callable(obj):
                            component = obj
                            break
                
                if component:
                    self.components[component_name] = {
                        "component": component,
                        "route_path": route_path,
                        "display_name": display_name
                    }
                    print(f"Registered component: {component_name}")
                else:
                    print(f"Warning: No component found in {file_path}")
                    
            except Exception as e:
                print(f"Error registering component {component_name}: {str(e)}")
                print("Stack trace:")
                traceback.print_exc()
    
    def register_routes(self, router, page_template):
        """Register all components with the router"""
        for name, info in self.components.items():
            title = name.replace("_", " ").capitalize()
            @router(info["route_path"])
            @page_template(title)
            def component_view(req, title=title, component=info["component"]):
                return Div(H1(title),component)
            
            print(f"Route registered: {info['route_path']} -> {name}")
    
    def get_sidebar_items(self, SidebarItem):
        """Generate sidebar items for all components"""
        # Sort the components by display_name alphabetically
        sorted_components = sorted(
            self.components.items(),
            key=lambda item: item[1]["display_name"]
        )
        
        return [
            SidebarItem(info["display_name"], href=info["route_path"])
            for name, info in sorted_components
        ]

# Create a singleton instance
component_registry = ComponentRegistry()
