from fasthtml.components import *
from fasthtml.svg import *
from fastbite.core import *
from fastbite.components import *

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
            Button("Primary", cls=BgColor.primary),
            Button("Blue", cls=BgColor.blue),
            Button("Green", cls=BgColor.green),
            Button("Cyan", cls=BgColor.cyan),
            Button("Teal", cls=BgColor.teal),
            Button("Lime", cls=BgColor.lime),
            Button("Red", cls=BgColor.red),
            Button("Yellow", cls=BgColor.yellow),
            Button("Pink", cls=BgColor.pink),
            Button("Purple", cls=BgColor.purple),            

        ),
        H4("Monotone gradient"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Primary", cls=BgColor.grad_primary),
            Button("Blue", cls=BgColor.grad_blue),
            Button("Green", cls=BgColor.grad_green),
            Button("Cyan", cls=BgColor.grad_cyan),
            Button("Teal", cls=BgColor.grad_teal),
            Button("Lime", cls=BgColor.grad_lime),
            Button("Red", cls=BgColor.grad_red),
            Button("Yellow", cls=BgColor.grad_yellow),
            Button("Pink", cls=BgColor.grad_pink),
            Button("Purple", cls=BgColor.grad_purple),
        ),
        H4("Duotone gradient"),
        Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
            Button("Cyan Blue", cls=BgColor.cyan_blue),
            Button("Green Blue", cls=BgColor.green_blue),
            Button("Pink Orange", cls=BgColor.pink_orange),
            Button("Purple Blue", cls=BgColor.purple_blue),
            Button("Purple Pink", cls=BgColor.purple_pink),
            Button("Red Yellow", cls=BgColor.red_yellow),
            Button("Teal Lime", cls=BgColor.teal_lime),

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
