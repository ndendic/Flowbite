from fasthtml.common import *
from fasthtml.svg import *
from monsterui.all import *
from fastbite.all import *
from fastbite.core import *
from app.navigation import Sidebar, Main, Navbar
from pages.typography import typography
from pages.templates import page_template
from route_collector import add_routes

from component_registry import component_registry
  

favicons = Favicon(
    light_icon="/images/favicon-light.svg", dark_icon="/images/favicon-dark.svg"
)

monsterui_headers = Theme.rose.headers()
app, rt = fast_app(
    live=True,
    pico=False,
    static_path="assets",
    hdrs=(
        favicons,
        fastbite_hdrs,
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(href='https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap', rel='stylesheet'),
        Link(rel="stylesheet", href="/css/output.css"),
        Link(rel="stylesheet", href="/css/fonts.css"),
        HighlightJS(langs=["python"]),
    ),
    ftrs=fastbite_ftrs,
    htmlkw=dict(data_theme="retro",cls="bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-white font-sans antialiased"),
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

@rt("/about")
def about(req):
    return Div(
        H1("About"),
        P("This is the about page."),
    )

component_registry.register_routes(rt, page_template)
app = add_routes(app)

if __name__ == "__main__":
    serve(reload=True, port=8008)
