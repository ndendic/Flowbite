from fasthtml.common import *
from fasthtml.svg import *
from components.buttons import Buttons
from components.navbar import Navbar

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


def site_page(title, content):
    return (
        Title(title),
        Body(
            Navbar(),
            Main(
                cls="max-w-7xl mx-auto px-4 mt-12 sm:px-6 lg:px-8 py-12 format lg:format-lg dark:format-invert"  # dark:bg-gray-900 dark:text-white
            )(
                
                Div(cls="grid grid-cols-1 md:grid-cols-3 gap-8")(
                    content,
                    cls="min-h-screen",
                ),
            ),
        ),
    )


content = Div(
    H1(
        "Hello, Flowbite!",
        # cls="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white",
    ),
    Buttons(),
    Div(cls="relative max-w-sm")(
        Div(
            cls="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none"
        )(
            Svg(
                aria_hidden="true",
                xmlns="http://www.w3.org/2000/svg",
                fill="currentColor",
                viewbox="0 0 20 20",
                cls="w-4 h-4 text-gray-500 dark:text-gray-400",
            )(
                Path(
                    d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
                )
            )
        ),
        Input(
            id="datepicker",
            type="text",
            placeholder="Select date",
            cls="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
        ),
        Script("""
                document.addEventListener('DOMContentLoaded', function() {
                    const datepickerEl = document.getElementById('datepicker');
                    new Datepicker(datepickerEl, {
                        // options
                    }); 
                });
            """),
    ),
)


@rt("/")
def home(req):
    return site_page("Flowbite CSS", content)


if __name__ == "__main__":
    serve(reload=True, port=8008)
