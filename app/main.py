from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from navigation import Sidebar, Main, Navbar
from pages.typography import typography

favicons = Favicon(
    light_icon="/images/favicon-light.svg", dark_icon="/images/favicon-dark.svg"
)
flowbite_hdrs = (
    Script(src="https://unpkg.com/@tailwindcss/browser@4"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    ),
    Link(rel="stylesheet", href="/css/output.css"),
    Script(
        "if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {\r\n        document.documentElement.classList.add('dark');\r\n    } else {\r\n        document.documentElement.classList.remove('dark')\r\n    }"
    ),
    # Script(src="/tailwind.config.js"),
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


def ButtonGroup():
    """Example of different button styles"""
    return Div(
        H2("Button Types"),
        Div(cls=stringify((FlexT.flex, FlexT.items_center, "gap-2 py-4")))(
            Button("Primary", cls=ButtonT.primary),
            Button("Secondary", cls=ButtonT.secondary),
            Button("Ghost", cls=ButtonT.ghost),
            Button("Link", cls=ButtonT.link),
            Button("Success", cls=ButtonT.success),
            Button("Warning", cls=ButtonT.warning),
            Button("Error", cls=ButtonT.error), 
            Button("Info", cls=ButtonT.info),
        ),
        H2("Button Shape"),
        Div(cls=stringify((FlexT.flex, FlexT.items_center, "gap-2 py-4")))(
            Button("Default", cls=  ButtonT.primary,shape=Round.default),
            Button("Full", cls=ButtonT.primary, shape=Round.full),
            Button("None", cls=ButtonT.primary, shape=Round.none),
            Button("Small", cls=ButtonT.primary, shape=Round.sm),
            Button("Medium", cls=ButtonT.primary, shape=Round.md),
            Button("Large", cls=ButtonT.primary, shape=Round.lg),
            Button("XLarge", cls=ButtonT.primary, shape=Round.xl),

        ),
        H2("Button Size"),
        Div(cls=stringify((FlexT.flex, FlexT.items_center, "gap-2 py-4")))(
            Button("Button xs", cls=ButtonT.primary+ButtonSize.xs),
            Button("Button sm", cls=ButtonT.primary+ButtonSize.sm),
            Button("Button base", cls=ButtonT.primary+ButtonSize.base),
            Button("Button lg", cls=ButtonT.primary+ButtonSize.lg),
            Button("Button xl", cls=ButtonT.primary+ButtonSize.xl),

        ),
    )
buttons = Div(
    H1("Buttons"),
    ButtonGroup(),
)

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
