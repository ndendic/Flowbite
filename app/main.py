from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from navigation import Sidebar, Main, Navbar
from pages.typography import typography
from pages.buttons import buttons

favicons = Favicon(
    light_icon="/images/favicon-light.svg", dark_icon="/images/favicon-dark.svg"
)
flowbite_hdrs = (
    # Script(src="https://unpkg.com/@tailwindcss/browser@4"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    ),    
    Script(
        "if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {\r\n        document.documentElement.classList.add('dark');\r\n    } else {\r\n        document.documentElement.classList.remove('dark')\r\n    }"
    ),
)

flowbite_ftrs = [
    Script(src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"),
    Script("""
    document.addEventListener('DOMContentLoaded', function() {
        // Get references to elements
        const drawerButton = document.querySelector('[data-drawer-target="logo-sidebar"]');
        const sidebar = document.getElementById('logo-sidebar');
        const mainContent = document.querySelector('.p-4:not(.mt-14)');
        
        // Function to toggle main content margin
        function toggleMainMargin() {
            // Check if sidebar is visible (doesn't have -translate-x-full class)
            if (!sidebar.classList.contains('-translate-x-full')) {
                // Sidebar is visible, add margin to main content
                mainContent.classList.add('ml-64');
            } else {
                // Sidebar is hidden, remove margin from main content
                mainContent.classList.remove('ml-64');
            }
        }
        
        // Initial check
        toggleMainMargin();
        
        // Listen for sidebar visibility changes
        if (drawerButton) {
            drawerButton.addEventListener('click', function() {
                // Wait for the drawer animation to complete
                setTimeout(toggleMainMargin, 300);
            });
        }
        
        // Create a MutationObserver to watch for class changes on the sidebar
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    toggleMainMargin();
                }
            });
        });
        
        // Start observing the sidebar for class changes
        if (sidebar) {
            observer.observe(sidebar, { attributes: true });
        }
    });
    """)
]

app, rt = fast_app(
    live=True,
    pico=False,
    static_path="assets",
    hdrs=(
        favicons,
        flowbite_hdrs,
        Link(rel="stylesheet", href="/css/output.css"),
        HighlightJS(langs=["python", "javascript", "html", "css"]),
    ),
    ftrs=flowbite_ftrs,
    htmlkw=dict(cls="bg-white dark:bg-gray-950 text-white font-sans antialiased"),
    # exception_handlers={404: custom_404_handler},
)

def is_htmx(request=None):
    "Check if the request is an HTMX request"
    return request and "hx-request" in request.headers

def site_page(title, content):
    return (
        Title(title),
        Body(
            Navbar(),
            Sidebar(),
            Main(content),
        ),
    )
def page_template(title):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            content = func(request)
            if is_htmx(request):
                return content
            return site_page(title, content)
        return wrapper
    return decorator

@rt("/")
@page_template("Home")
def home(req):
    return Ul(
        Li(A("Typography", href="/typography")), 
        Li(A("Buttons", href="/buttons"))
    )

@rt("/typography")
@page_template("Typography")
def get(req):
    return typography

@rt("/buttons")
@page_template("Buttons")
def get(req):
    return buttons


if __name__ == "__main__":
    serve(reload=True, port=8008)
