from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from utils import component_showcase
from theme_switcher import ThemeSwitcher
from extracted.input_field import component as input_field_component
from extracted.file_input import component as file_input_component

from ft_datastar import *

def TabItem(text: str, controls: str, tab_signal: str) -> FT:
    return Li(role='presentation', cls='me-2')(
        Button(
            text,
            id=f'{text}-tab',
            type='button',
            role='tab',
            aria_controls=controls,
            data_on_click=f"${tab_signal} = '{controls}'",
            data_aria_selected=f"${tab_signal} === '{controls}'",
            data_class=(
                f"{'text-primary-600 hover:text-primary-600 dark:text-primary-500 dark:hover:text-primary-500 border-primary-600 dark:border-primary-500'}"
                f" if {tab_signal} === '{controls}' else "
                f"'dark:border-transparent text-gray-500 hover:text-gray-600 dark:text-gray-400 border-gray-100 hover:border-gray-300 dark:border-gray-700 dark:hover:text-gray-300'"
            ),
            cls='inline-block p-4 border-b-2' + Round.none,
        )
    )


def TabContainer(*li: FT, **kwargs) -> FT:
    return Div(cls="flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400")(
        Ul(cls="flex -mb-px text-sm font-medium text-center", **kwargs)(*li)
    )


def component_showcase(*c: FT | str, code: str, id: str, cls: str | tuple = (), **kwargs) -> FT:
    tab_signal = f"{id}_tab"
    return Div(
        Div(data_signals={tab_signal: f"{id}-preview"}),  # Set default active tab

        TabContainer(
            TabItem("Preview", f"{id}-preview", tab_signal),
            TabItem("Code", f"{id}-code", tab_signal),
        ),

        Ul(id=f'{id}-tab-content')(
            Li(
                id=f'{id}-preview',
                role='tabpanel',
                aria_labelledby='Preview-tab',
                data_class_hidden=f"${tab_signal} !== '{id}-preview'",
                cls='p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
            )(*c),

            Li(
                id=f'{id}-code',
                role='tabpanel',
                aria_labelledby='Code-tab',
                data_class_hidden=f"${tab_signal} !== '{id}-code'",
                cls='rounded-lg bg-gray-50 dark:bg-gray-800'
            )(
                Pre(cls='text-sm text-gray-500 dark:text-gray-400' + Round.lg)(
                    Code(cls='language-python')(code)
                )
            ),
        ),

        cls=(cls, "max-w-5xl"),
        **kwargs
    )

component =Div(
        H2("Datastar + FastHTML Example", cls="text-xl font-bold mb-4"),
        Div(
            "Using signals we default the starting count to 5",
            ds_signals(count="5")
        ),
        Button(
            "Increment",
            ds_on(click="$count++"),
            cls=ButtonT.primary
        ),
        Button(
            "Reset",
            ds_on(click="$count = 0"),
            cls=ButtonT.warning
        ),
        Div(
            "Count: ",
            Span(ds_text("$count"), cls="font-mono"),
            cls="mt-2"
        ),
        cls="p-4 space-x-2"
    )

playground = Container(
    # input_field_component,
    component,
    component_showcase(Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Rounded avatar', cls='w-10 h-10 rounded-full'),
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Default avatar', cls='w-10 h-10 rounded-sm')
    ), code="""Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Rounded avatar', cls='w-10 h-10 rounded-full'),
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Default avatar', cls='w-10 h-10 rounded-sm')
    )""", id="example_0",cls='mt-2 mb-6'),

    DivCentered(
        NotStr("""        
        
        """)
    )
) 