from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from utils import component_showcase
from theme_switcher import ThemeSwitcher
from extracted.input_field import component as input_field_component
from extracted.file_input import component as file_input_component

from ft_datastar import *

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

form_component = Form(
        H3("Form Inputs", cls="mb-4"),
        Input(id="first_name",placeholder="No label input",required=True),
        Input(id="disabled",placeholder="Disabled input",disabled=True),
        Input(label="First Name",id="first_name",placeholder="John",required=True,cls=InputT.default),
        Input(label="Last Name",id="last_name",placeholder="Doe",required=True,cls=InputT.default),
        Input(label="Email",icon="mail",id="email",placeholder="john.doe@example.com",type="email",required=True,cls=InputT.default),
        Input(label="Password",id="password",placeholder="********",type="password",required=True,help_text="Password must be at least 8 characters long",cls=InputT.default),
        Input(label="Phone",id="phone",placeholder="123-456-7890",type="tel",required=True,cls=InputT.default),
        Input(label="Success",help_text="This is a success message",id="success",placeholder="Success",type="text",required=True,cls=InputT.success,lbl_cls=LabelInputT.success,help_cls=TextT.success+TextT.sm),
        Input(label="Error",help_text="This is an error message",id="error",placeholder="Error",type="text",required=True,cls=InputT.error,lbl_cls=LabelInputT.error,help_cls=TextT.error+TextT.sm),
        TextArea(label="Text Area",id="text_area",placeholder="Text Area",required=True,cls=InputT.default),
        Select(Option("Option 1"),Option("Option 2"),label="Select",id="select",placeholder="Select",required=True,cls=InputT.default),
        # Button("Submit",cls=ButtonT.primary),
    )

playground = Section(cls=(SectionT.default))(
    # input_field_component,
    P("This is your playground for developing Flowbite components.\n Go to and modify ",
Code("app/pages/playground.py")," to see the components in action.",cls=ParagrafT.lead+TextT.center),

    # component,

    form_component,

    component_showcase(Div(
        DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-full'),
        DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-sm')
    ), code="""Div(
        DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-full'),
        DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-sm')
    )""", id="example_0",cls='mt-2 mb-6'),

    # DivCentered(
    #     NotStr("""        
        
    #     """)
    # )
) 