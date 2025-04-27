from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import Svg, Path
from utils import component_showcase

accordion_components = Div(
    H1("Accordion Components", link=True),

    P("The Accordion component allows you to organize content into expandable sections. Use it to build FAQ sections or to condense long content blocks."),

    H2("Accordion Behaviour Types", link=True),

    H3("Collapse (Single open)", link=True),
    P(
        "When ", Code("type='collapse'"), " (default) is used, only one item can be open at a time. Opening a new item will automatically close the previously opened one."
    ),

    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "What is Fastbite?",
                    P("Fastbite is an open-source UI component library built with Tailwind CSS."),
                    open=True,
                    trigger_add_cls = 'rounded-t-xl'

                ),
                AccordionItem(
                    "Is the Accordion collapsible?",
                    P("Yes – clicking on the header will toggle the visibility of the body content.")
                ),
                AccordionItem(
                    "Can I have multiple items open?",
                    P("Not in collapse mode; only one item will remain open at a time."),
                ),
                id="accordion-collapse-example",
                type="collapse"
            ),
            cls="max-w-xl"
        ),
        code="""from fastbite.all import Accordion, AccordionItem

Accordion(
    AccordionItem(
        "What is Fastbite?",
        P("Fastbite is an open-source UI component library built with Tailwind CSS."),
        open=True
    ),
    AccordionItem(
        "Is the Accordion collapsible?",
        P("Yes – clicking on the header will toggle the visibility of the body content.")
    ),
    AccordionItem(
        "Can I have multiple items open?",
        P("Not in collapse mode; only one item will remain open at a time.")
    ),
    id="accordion-collapse-example",
    type="collapse"
)""",
        id="accordion-collapse"
    ),

    Br(),

    H3("Open (Multiple open)", link=True),
    P(
        "Set ", Code("type='open'"), " to allow multiple accordion items to stay open simultaneously."
    ),

    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "First question",
                    P("Answer for the first question."),
                    open=True,
                    trigger_add_cls = 'rounded-t-xl'
                ),
                AccordionItem(
                    "Second question",
                    P("Answer for the second question."),
                    open=True
                ),
                AccordionItem(
                    "Third question",
                    P("Answer for the third question.")
                ),
                id="accordion-open-example",
                type="open"
            ),
            cls="max-w-xl"
        ),
        code="""from fastbite.all import Accordion, AccordionItem

Accordion(
    AccordionItem("First question", P("Answer for the first question."), open=True),
    AccordionItem("Second question", P("Answer for the second question."), open=True),
    AccordionItem("Third question", P("Answer for the third question.")),
    id="accordion-open-example",
    type="open"
)""",
        id="accordion-open"
    ),

    Br(),

    H2("Flush Style", link=True),
    P(
        "Enable the flush style by passing ", Code("flush=True"), " to the parent ", Code("Accordion"), ". The child ", Code("AccordionItem"), " components automatically inherit the flush styling context unless explicitly overridden with custom style classes like ", Code("trigger_style_cls"), " or ", Code("body_inner_style_cls"), "."
    ),

    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "Flush item #1",
                    P("This is the body content for the first item."),
                    trigger_add_cls = 'rounded-t-xl'
                ),
                AccordionItem(
                    "Flush item #2",
                    P("This is the body content for the second item.")
                ),
                AccordionItem(
                    "Flush item #3",
                    P("This is the body content for the third item.")
                ),
                id="accordion-flush-example",
                flush=True
            ),
            cls="max-w-xl"
        ),
        code="""from fastbite.all import Accordion, AccordionItem

Accordion(
    AccordionItem("Flush item #1", P("This is the body content for the first item.")),
    AccordionItem("Flush item #2", P("This is the body content for the second item.")),
    AccordionItem("Flush item #3", P("This is the body content for the third item.")),
    id="accordion-flush-example",
    flush=True
)""",
        id="accordion-flush"
    ),

    Br(),

    H2("Color Customization", link=True),
    P(
        "Customize the appearance of active and inactive item headers using the ", Code("active_classes"), " and ", Code("inactive_classes"), " parameters on the parent ", Code("Accordion"), ". These correspond to the ", Code("data-active-classes"), " and ", Code("data-inactive-classes"), " attributes used by Flowbite's JavaScript."
    ),

    component_showcase(
        Div(
            Accordion(
                AccordionItem("What is Fastbite?", P("..."), open=True, trigger_add_cls = 'rounded-t-xl'),
                AccordionItem("Is there a Figma file?", P("...")),
                AccordionItem("Differences vs Tailwind UI?", P("...")),
                id="accordion-color-example",
                type="collapse",
                active_classes='bg-primary-100 dark:bg-gray-800 text-primary-600 dark:text-white',
                inactive_classes='text-gray-500 dark:text-gray-400'
            ),
            cls="max-w-xl"
        ),
        code="""from fastbite.all import Accordion, AccordionItem

Accordion(
    AccordionItem("What is Fastbite?", P("..."), open=True, trigger_add_cls = 'rounded-t-xl'),
    AccordionItem("Is there a Figma file?", P("...")),
    AccordionItem("Differences vs Tailwind UI?", P("...")),
    id="accordion-color-example",
    type="collapse",
    active_classes='bg-primary-100 dark:bg-gray-800 text-primary-600 dark:text-white',
    inactive_classes='text-gray-500 dark:text-gray-400'
)""",
        id="accordion-color"
    ),

    Br(),

    H2("Icon Customization", link=True),
    P(
        "Control the icon displayed in the ", Code("AccordionItem"), " header using the ", Code("icon"), " parameter. You can disable it, provide a custom FastHTML element, or customize the default icon's classes."
    ),

    H3("No Icon", link=True),
    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "Item without an icon",
                    P("The default chevron icon is removed."),
                    icon=False,
                ),
                id="accordion-no-icon-example"
            ),
            cls="max-w-xl"
        ),
        code="""Accordion(
    AccordionItem(
        "Item without an icon",
        P("The default chevron icon is removed."),
        icon=False
    ),
    id="accordion-no-icon-example"
)""",
        id="accordion-no-icon"
    ),

    H3("Custom Icon", link=True),
    P("Provide any FastHTML element (like an ", Code("Svg"), ") to the ", Code("icon"), " parameter."),
    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "Item with a custom icon",
                    P("Using a custom question mark SVG."),
                    icon=Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 shrink-0 text-blue-500'
                    )
                ),
                id="accordion-custom-icon-example"
            ),
            cls="max-w-xl"
        ),
        code="""from fasthtml.svg import Svg, Path

Accordion(
    AccordionItem(
        "Item with a custom icon",
        P("Using a custom question mark SVG."),
        icon=Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 20 20',
            cls='w-4 h-4 shrink-0 text-blue-500'
        )
    ),
    id="accordion-custom-icon-example"
)""",
        id="accordion-custom-icon"
    ),

    H3("Customizing Default Icon", link=True),
    P(
        "Modify the default icon's appearance using ", Code("icon_base_cls"), ", ", Code("icon_open_cls"), ", and ", Code("icon_add_cls"), " parameters on the ", Code("AccordionItem"), "."
    ),
    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "Item with a larger, red icon",
                    P("The default icon is modified."),
                    open=True,
                    icon_base_cls='w-5 h-5 shrink-0',
                    icon_add_cls='text-red-600 dark:text-red-500',
                    icon_open_cls='rotate-90'
                ),
                id="accordion-custom-default-icon-example"
            ),
            cls="max-w-xl"
        ),
        code="""Accordion(
    AccordionItem(
        "Item with a larger, red icon",
        P("The default icon is modified."),
        open=True,
        icon_base_cls='w-5 h-5 shrink-0',
        icon_add_cls='text-red-600 dark:text-red-500',
        icon_open_cls='rotate-90'
    ),
    id="accordion-custom-default-icon-example"
)""",
        id="accordion-custom-default-icon"
    ),

    Br(),
) 