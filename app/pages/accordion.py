from fasthtml.common import *
from fastbite.all import *
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
                    open=True
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
        "Enable the flush style by passing ", Code("flush=True"), " to both the parent ", Code("Accordion"), " and the ", Code("AccordionItem"), " components to remove outer borders and background."
    ),

    component_showcase(
        Div(
            Accordion(
                AccordionItem(
                    "Flush item #1",
                    P("This is the body content for the first item."),
                    flush=True
                ),
                AccordionItem(
                    "Flush item #2",
                    P("This is the body content for the second item."),
                    flush=True
                ),
                AccordionItem(
                    "Flush item #3",
                    P("This is the body content for the third item."),
                    flush=True
                ),
                id="accordion-flush-example",
                flush=True
            ),
            cls="max-w-xl"
        ),
        code="""from fastbite.all import Accordion, AccordionItem

Accordion(
    AccordionItem("Flush item #1", P("This is the body content for the first item."), flush=True),
    AccordionItem("Flush item #2", P("This is the body content for the second item."), flush=True),
    AccordionItem("Flush item #3", P("This is the body content for the third item."), flush=True),
    id="accordion-flush-example",
    flush=True
)""",
        id="accordion-flush"
    ),

    Br(),
) 