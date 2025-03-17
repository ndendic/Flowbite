from fasthtml.components import *
from fasthtml.svg import *
from fh_flowbite.core import *
from fh_flowbite.components import *

def Buttons():
    """Example of different button styles"""
    return Div(
        H2("Button Types"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Primary", cls=ButtonT.primary),
            Button("Secondary", cls=ButtonT.secondary),
            Button("Ghost", cls=ButtonT.ghost),
            Button("Link", cls=ButtonT.link),
            Button("Success", cls=ButtonT.success),
            Button("Warning", cls=ButtonT.warning),
            Button("Error", cls=ButtonT.error), 
            Button("Info", cls=ButtonT.info),
        ),
        H2("Button Colors"),
        H4("Flat"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Primary", cls=ButtonColor.primary),
            Button("Blue", cls=ButtonColor.blue),
            Button("Green", cls=ButtonColor.green),
            Button("Cyan", cls=ButtonColor.cyan),
            Button("Teal", cls=ButtonColor.teal),
            Button("Lime", cls=ButtonColor.lime),
            Button("Red", cls=ButtonColor.red),
            Button("Yellow", cls=ButtonColor.yellow),
            Button("Pink", cls=ButtonColor.pink),
            Button("Purple", cls=ButtonColor.purple),            

        ),
        H4("Monotone gradient"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Primary", cls=ButtonColor.grad_primary),
            Button("Blue", cls=ButtonColor.grad_blue),
            Button("Green", cls=ButtonColor.grad_green),
            Button("Cyan", cls=ButtonColor.grad_cyan),
            Button("Teal", cls=ButtonColor.grad_teal),
            Button("Lime", cls=ButtonColor.grad_lime),
            Button("Red", cls=ButtonColor.grad_red),
            Button("Yellow", cls=ButtonColor.grad_yellow),
            Button("Pink", cls=ButtonColor.grad_pink),
            Button("Purple", cls=ButtonColor.grad_purple),
        ),
        H4("Duotone gradient"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Cyan Blue", cls=ButtonColor.cyan_blue),
            Button("Green Blue", cls=ButtonColor.green_blue),
            Button("Pink Orange", cls=ButtonColor.pink_orange),
            Button("Purple Blue", cls=ButtonColor.purple_blue),
            Button("Purple Pink", cls=ButtonColor.purple_pink),
            Button("Red Yellow", cls=ButtonColor.red_yellow),
            Button("Teal Lime", cls=ButtonColor.teal_lime),

        ),
        H2("Button Outline"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Default", cls=ButtonOutline.default),
            Button("Dark", cls=ButtonOutline.dark),
            Button("Green", cls=ButtonOutline.green),
            Button("Red", cls=ButtonOutline.red),
            Button("Yellow", cls=ButtonOutline.yellow),
            Button("Purple", cls=ButtonOutline.purple),

        ),
        H2("Button Shape"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Default", cls=  ButtonT.secondary,shape=Round.default),
            Button("Full", cls=ButtonT.secondary, shape=Round.full),
            Button("None", cls=ButtonT.secondary, shape=Round.none),
            Button("Small", cls=ButtonT.secondary, shape=Round.sm),
            Button("Medium", cls=ButtonT.secondary, shape=Round.md),
            Button("Large", cls=ButtonT.secondary, shape=Round.lg),
            Button("XLarge", cls=ButtonT.secondary, shape=Round.xl),

        ),
        H2("Button Size"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Extra small", cls=ButtonT.primary, size=ButtonSize.xs),
            Button("Small", cls=ButtonT.primary, size=ButtonSize.sm),
            Button("Base", cls=ButtonT.primary, size=ButtonSize.base),
            Button("Large", cls=ButtonT.primary, size=ButtonSize.lg),
            Button("Extra large", cls=ButtonT.primary, size=ButtonSize.xl),

        ),
        

    )
buttons = Div(
    H1("Buttons"),
    Buttons(),
)
