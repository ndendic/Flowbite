from fasthtml.common import *
from fasthtml.svg import *
from components.navigation.navbar import Navbar
from fh_flowbite.components import *
from fh_flowbite.core import *

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
                # cls="max-w-7xl mx-auto px-4 mt-12 sm:px-6 lg:px-8 py-12"  # dark:bg-gray-900 dark:text-white
                cls="max-w-7xl mx-auto px-4 mt-12 sm:px-6 lg:px-8 py-12 lg:format-lg format dark:format-invert"  # dark:bg-gray-900 dark:text-white
            )(
                
                Div(cls="grid grid-cols-1 md:grid-cols-3 gap-8")(
                    content,
                    cls="min-h-screen",
                ),
            ),
        ),
    )

typography = Div(
    H1("Typography", cls=TextT.center),

    H1("Heading 1"),
    H2("Heading 2"),
    H3("Heading 3"),
    H4("Heading 4"),
    H5("Heading 5"),
    H6("Heading 6"),
    Br(),

    H2("Text size", cls=TextT.center),
    P("Text Styling xs", cls=TextT.xs),
    P("Text Styling sm", cls=TextT.sm),
    P("Text Styling base", cls=TextT.base),
    P("Text Styling lg", cls=TextT.lg),
    P("Text Styling xl", cls=TextT.xl),
    P("Text Styling 2xl", cls=TextT.text_2xl),
    P("Text Styling 3xl", cls=TextT.text_3xl),
    P("Text Styling 4xl", cls=TextT.text_4xl),
    P("Text Styling 5xl", cls=TextT.text_5xl),
    P("Text Styling 6xl", cls=TextT.text_6xl),
    P("Text Styling 7xl", cls=TextT.text_7xl),
    P("Text Styling 8xl", cls=TextT.text_8xl),
    P("Text Styling 9xl", cls=TextT.text_9xl),

    H2("Tracking Styling", cls=TextT.center),
    P("Tracking Styling", cls=TextT.tracking_tighter),
    P("Tracking Styling", cls=TextT.tracking_tight),
    P("Tracking Styling", cls=TextT.tracking_normal),
    P("Tracking Styling", cls=TextT.tracking_wide),
    P("Tracking Styling", cls=TextT.tracking_wider),
    P("Tracking Styling", cls=TextT.tracking_widest),

    H2("Highlight and color", cls=TextT.center),
    P("Highlight Styling", cls=TextT.highlight),
    P("Highlight muted", cls=TextT.muted),
    P("Highlight primary", cls=TextT.primary),
    P("Highlight secondary", cls=TextT.secondary),
    P("Highlight success", cls=TextT.success),
    P("Highlight warning", cls=TextT.warning),
    P("Highlight error", cls=TextT.error),

    H2("Text weight", cls=TextT.center),
    P("Text weight thin", cls=TextT.thin),
    P("Text weight extralight", cls=TextT.extralight),
    P("Text weight light", cls=TextT.light),
    P("Text weight normal", cls=TextT.normal),
    P("Text weight medium", cls=TextT.medium),
    P("Text weight semibold", cls=TextT.semibold),
    P("Text weight bold", cls=TextT.bold),
    P("Text weight extrabold", cls=TextT.extrabold),
    P("Text weight black", cls=TextT.black),

    H2("Text style", cls=TextT.center),
    P("Text style italic", cls=TextT.italic),
    P("Text style normal", cls=TextT.normal),
    P("Text style underline", cls=TextT.underline),
    P("Text style line-through", cls=TextT.line_through),
    P("Text style uppercase", cls=TextT.uppercase),
    P("Text style lowercase", cls=TextT.lowercase),
    P("Text style capitalize", cls=TextT.capitalize),
    P("Text style normal-case", cls=TextT.normal_case),
    
    H2("Text alignment", cls=TextT.center),
    P("Text alignment left", cls=TextT.left),
    P("Text alignment right", cls=TextT.right),
    P("Text alignment center", cls=TextT.center),
    P("Text alignment justify", cls=TextT.justify),
    P("Text alignment start", cls=TextT.start),
    P("Text alignment end", cls=TextT.end),
    
    H2("Code", cls=TextT.center),
    Code(
        """
        Button("Default", cls=ButtonT.default),
        Button("Alternative", cls=ButtonT.alternative),
        Button("Dark", cls=ButtonT.dark),
        Button("Light", cls=ButtonT.light),
        """
    ),
    Pre(Code(
        """
        Button("Default", cls=ButtonT.default),
        Button("Alternative", cls=ButtonT.alternative),
        Button("Dark", cls=ButtonT.dark),
        Button("Light", cls=ButtonT.light),
        """
    )),

    H2("Special tags", cls=TextT.center),
    Br(),
    H3("Blockquote"),
    Blockquote(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    H3("Del"),
    Del(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Ins"),
    Ins(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Mark"),
    Mark(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Sub"),
    Sub(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Sup"),
    Sup(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("S"),
    S(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Small"),
    Small(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Span"),
    Span(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Strong"),
    Strong(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Cite"),
    Cite(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Dfn"),
    Dfn(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Address"),
    Address(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Time"),
    Time(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Abbr"),
    Abbr(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    # TODO: Add to list data list
    H3("Summary"),
    Summary("SSS"),
    Br(),
    H3("Details"),
    Details(Summary("Summary of details"),
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """,cls="cursor-pointer"
    ),
    Br(),
    H3("Dl"),
    Dl(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Kbd"),
    Kbd(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    ),
    Br(),
    H3("Meter"),
    Meter(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """"",value=50,min=0,max=100
    ),

    
    # Div(cls="relative max-w-sm")(
    #     Div(
    #         cls="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none"
    #     )(
    #         Svg(
    #             aria_hidden="true",
    #             xmlns="http://www.w3.org/2000/svg",
    #             fill="currentColor",
    #             viewbox="0 0 20 20",
    #             cls="w-4 h-4 text-gray-500 dark:text-gray-400",
    #         )(
    #             Path(
    #                 d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
    #             )
    #         )
    #     ),
    #     Input(
    #         id="datepicker",
    #         type="text",
    #         placeholder="Select date",
    #         cls="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
    #     ),
    #     Script("""
    #             document.addEventListener('DOMContentLoaded', function() {
    #                 const datepickerEl = document.getElementById('datepicker');
    #                 new Datepicker(datepickerEl, {
    #                     // options
    #                 }); 
    #             });
    #         """),
    # ),
)

def ButtonGroup():
    """Example of different button styles"""
    return Div(
        cls=stringify((FlexT.flex, FlexT.items_center, "gap-2 py-4")),
    )(
        Button("Default", cls=ButtonT.default),
        Button("Alternative", cls=ButtonT.alternative),
        Button("Dark", cls=ButtonT.dark),
        Button("Light", cls=ButtonT.light),
        Button("Green", cls=ButtonT.green),
        Button("Red", cls=ButtonT.red),
        Button("Yellow", cls=ButtonT.yellow),
        Button("Purple", cls=ButtonT.purple),
    )
buttons = Div(
    H1("Buttons"),
    ButtonGroup(),
    
    # Button("Button", cls=ButtonT.primary),
    # Button("Button", cls=ButtonT.secondary),
    # Button("Button", cls=ButtonT.success),
)

@rt("/")
def home(req):
    return site_page("Flowbite CSS", 
    Ul(
        Li(A("Typography", href="/typography")), 
        Li(A("Buttons", href="/buttons"))
    )
    )

@rt("/typography")
def get(req):
    return site_page("Typography", typography)

@rt("/buttons")
def get(req):
    return site_page("Buttons", buttons)


if __name__ == "__main__":
    serve(reload=True, port=8008)
