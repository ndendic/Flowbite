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
datastar_script = Script(src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.8/bundles/datastar.js", type="module")
  

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
        datastar_script,
        Link(rel="stylesheet", href="/css/output.css"),
        HighlightJS(langs=["python", "javascript", "html", "css"]),
    ),
    # ftrs=fastbite_ftrs,
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
