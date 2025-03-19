from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from utils import component_showcase
from theme_switcher import ThemeSwitcher

playground = Container(
    component_showcase(
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
        code ="""Div(cls=stringify((FlexT.block, FlexT.middle, "gap-2 py-4")))(
    Button("Primary", cls=ButtonT.primary),
    Button("Secondary", cls=ButtonT.secondary),
    Button("Ghost", cls=ButtonT.ghost),
    Button("Link", cls=ButtonT.link),
    Button("Success", cls=ButtonT.success),
    Button("Warning", cls=ButtonT.warning),
    Button("Error", cls=ButtonT.error), 
    Button("Info", cls=ButtonT.info),
)""",
        id="button-group",
    ),       
    DivCentered(
        NotStr("""        
        
        """)
    )
) 