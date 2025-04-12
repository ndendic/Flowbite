from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from fastbite.core import *
from app.navigation import Sidebar, Main, Navbar
from pages.typography import typography
from pages.templates import page_template
from route_collector import add_routes

from component_registry import component_registry
datastar_script = Script(src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.8/bundles/datastar.js", type="module")
  

favicons = Favicon(
    light_icon="/images/favicon-light.svg", dark_icon="/images/favicon-dark.svg"
)

flowbite_ftrs = [
    Script(src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"), 
    Script("""
    document.addEventListener('DOMContentLoaded', function() {
        // Theme toggle functionality
        var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
        var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
        var themeToggleBtn = document.getElementById('theme-toggle');
        
        // Function to update icon visibility
        function updateThemeToggleIcons() {
            if (document.documentElement.classList.contains('dark')) {
                themeToggleLightIcon.classList.remove('hidden');
                themeToggleDarkIcon.classList.add('hidden');
            } else {
                themeToggleLightIcon.classList.add('hidden');
                themeToggleDarkIcon.classList.remove('hidden');
            }
        }

        // Set initial state based on localStorage or system preference
        if (localStorage.getItem('color-theme') === 'dark' || 
            (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        
        // Update icons based on initial state
        updateThemeToggleIcons();
        
        // Handle theme toggle button click
        if (themeToggleBtn) {
            themeToggleBtn.addEventListener('click', function() {
                // Toggle dark class on the html element
                document.documentElement.classList.toggle('dark');
                
                // Update localStorage based on current state
                if (document.documentElement.classList.contains('dark')) {
                    localStorage.setItem('color-theme', 'dark');
                } else {
                    localStorage.setItem('color-theme', 'light');
                }
                
                // Update icon visibility
                updateThemeToggleIcons();
            });
        }
        
        // Listen for system preference changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
            if (!localStorage.getItem('color-theme')) {
                if (e.matches) {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                }
                updateThemeToggleIcons();
            }
        });
    });
    """),
    Script("""
        function setTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
        }

        // On page load, set the theme based on localStorage
        const savedTheme = localStorage.getItem('theme') || 'none';
        document.documentElement.setAttribute('data-theme', savedTheme);
        """
    ),
    ]

app, rt = fast_app(
    live=True,
    pico=False,
    static_path="assets",
    hdrs=(
        favicons,
        fastbite_hdrs,
        datastar_script,
        Link(rel="stylesheet", href="/css/output.css"),
        HighlightJS(langs=["python", "javascript", "html", "css"]),
    ),
    ftrs=flowbite_ftrs,
    htmlkw=dict(data_theme="retro",cls="bg-white dark:bg-gray-950 text-gray-900 dark:text-white font-sans antialiased"),
    # exception_handlers={404: custom_404_handler},
)

@rt("/")
@page_template("Home")
def home(req):
    return Ul(
        Li(A("Typography", href="/typography")), 
        Li(A("Buttons", href="/buttons")),
        Li(A("Containers", href="/containers")),
        Li(A("Themes", href="/themes")),
    )

component_registry.register_routes(rt, page_template)
app = add_routes(app)

if __name__ == "__main__":
    serve(reload=True, port=8008)
