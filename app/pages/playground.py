from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.components import Radio
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
        Select(*Options("Option 1","Option 2","Option 3"),label="Select",id="select",placeholder="Select",required=True,cls=InputT.default),
        Radio("Option 1",help_text="For orders shipped from $25 in books or $29 in other categories",id="radio",required=True),
        Radio("Option Checked",help_text="For orders shipped from $30 in books or $39 in other categories",id="radio",checked=True),
        Radio("Option disabled",help_text="For orders shipped from $30 in books or $39 in other categories",id="radio",disabled=True),
        Checkbox("Option 1",id="checkbox"),
        Checkbox("Option disabled",id="checkbox",disabled=True),
        Checkbox("Option checked",id="checkbox",checked=True),
        Checkbox("Option help",help_text="For orders shipped from $30 in books or $39 in other categories",id="checkbox"),
        
        Switch("Option 1",id="switch"),
        Switch("Option disabled",id="switch",disabled=True),
        Switch("Option checked",id="switch",checked=True),
        Switch("Option error",id="switch",cls=SwitchT.error,checked=True),
        Switch("Option success",id="switch",cls=SwitchT.success,checked=True),

        Upload("Upload file",id="file_input"),
        Upload("Upload help",help_text="This is a help text",id="file_input"),
        Upload("Upload multiple",multiple=True,id="file_input"),
        H3("Range",cls="mb-4"),
        Range(label="Default range",id="default-range"),
        Range(label="Range with help labels",id="default-range",help_labels=["0%","20%","40%","60%","80%","100%"]),
        Range(label="Disabled range",id="default-range",disabled=True),
        Range(label="Min Max",id="default-range",min=0,max=100, help_labels=["0%","50%","100%"]),
        Range(label="Steps",id="default-range",min=0,max=100, step=10, help_labels=["0%","50%","100%"]),

        H3("Range size",cls="mb-4"),
        Range(label="Small",id="default-range",cls=RangeT.sm),
        Range(label="Default",id="default-range"),
        Range(label="Large",id="default-range",cls=RangeT.lg),
        # Button("Submit",cls=ButtonT.primary),

        H3("Link",cls="mb-4"),
        Div(
            A("Default",cls=AT.default),
            A("Muted",cls=AT.muted),
            A("Text",cls=AT.text),
            A("Primary",cls=AT.primary),
            A("Classic",cls=AT.classic),
            cls="space-x-2 mb-4"
        ),
        H3("List",cls="mb-4"),
        Div(
            Ul("Unordered list",Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.ul+"mb-4"),
            Ol("Ordered list",Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.ol+"mb-4"),
            Ul("Unstyled",Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.unstyled+"mb-4"),

            Ul("Nested",
                Ul("Nested ordered list",Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.nested_ol+"mb-4"),
                Ul("Nested unordered list",Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.nested_ul+"mb-4"),
            ),
            H4("Horizontal",cls="mb-4"),
            Ul(Li("Item 1"),Li("Item 2"),Li("Item 3"),cls=ListT.horizontal+"mb-4"),
            Ul("Definition list",
                Div(Dt("Item 1", cls=ListT.dt),Dd("Item 1", cls=ListT.dd)),
                Div(Dt("Item 2", cls=ListT.dt),Dd("Item 2", cls=ListT.dd)),
                Div(Dt("Item 3", cls=ListT.dt),Dd("Item 3", cls=ListT.dd)),
                cls=ListT.dl+"mb-4"
            ),

        ),
        
    )
badges_component = Div(
            H3("Badges",cls="mb-4"),
            H4("Default",cls="mb-4"),
            Div(
                Badge("Default",cls=BadgeT.default),
                Badge("Dark",cls=BadgeT.dark),
                Badge("Red",cls=BadgeT.red),
                Badge("Yellow",cls=BadgeT.yellow),
                Badge("Green",cls=BadgeT.green),
                Badge("Blue",cls=BadgeT.blue),
                Badge("Indigo",cls=BadgeT.indigo),
                Badge("Purple",cls=BadgeT.purple),
                Badge("Pink",cls=BadgeT.pink),
                cls="space-x-2 mb-4"
            ),
            H4("Large",cls="mb-4"),
            Div(
                Badge("Default",cls=BadgeT.default_lg),
                Badge("Dark",cls=BadgeT.dark_lg),
                Badge("Red",cls=BadgeT.red_lg),
                Badge("Yellow",cls=BadgeT.yellow_lg),
                Badge("Green",cls=BadgeT.green_lg),
                Badge("Blue",cls=BadgeT.blue_lg),
                Badge("Indigo",cls=BadgeT.indigo_lg),
                Badge("Purple",cls=BadgeT.purple_lg),
                Badge("Pink",cls=BadgeT.pink_lg),
                cls="space-x-2 mb-4"
            ),
            H4("Pill",cls="mb-4"),
            Div(
                Badge("Default",cls=BadgeT.default_pill),
                Badge("Dark",cls=BadgeT.dark_pill),
                Badge("Red",cls=BadgeT.red_pill),
                Badge("Yellow",cls=BadgeT.yellow_pill),
                Badge("Green",cls=BadgeT.green_pill),
                Badge("Blue",cls=BadgeT.blue_pill),
                Badge("Indigo",cls=BadgeT.indigo_pill),
                Badge("Purple",cls=BadgeT.purple_pill),
                Badge("Pink",cls=BadgeT.pink_pill),
                cls="space-x-2 mb-4"
            ),

            H4("Outline",cls="mb-4"),
            Div(
                Badge("Default",cls=BadgeT.default_outline),
                Badge("Dark",cls=BadgeT.dark_outline),
                Badge("Red",cls=BadgeT.red_outline),
                Badge("Yellow",cls=BadgeT.yellow_outline),
                Badge("Green",cls=BadgeT.green_outline),
                Badge("Blue",cls=BadgeT.blue_outline),
                Badge("Indigo",cls=BadgeT.indigo_outline),
                Badge("Purple",cls=BadgeT.purple_outline),
                Badge("Pink",cls=BadgeT.pink_outline),
                cls="space-x-2 mb-4"
            ),
            H4("Icon",cls="mb-4"),
            Div(
                Badge("Default", icon="home",cls=BadgeT.default),
                Badge("Dark", icon="home",cls=BadgeT.dark),
                Badge("Red", icon="home",cls=BadgeT.red),
                Badge("Yellow", icon="home",cls=BadgeT.yellow),
                Badge("Green", icon="home",cls=BadgeT.green),
                Badge("Blue", icon="home",cls=BadgeT.blue),
                Badge("Indigo", icon="home",cls=BadgeT.indigo),
                Badge("Purple", icon="home",cls=BadgeT.purple),
                Badge("Pink", icon="home",cls=BadgeT.pink),
                cls="space-x-2 mb-4"
            ),
            H4("Icon only",cls="mb-4"),
            Div(
                IconBadge(icon="home", cls=BackgroundT.primary+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.secondary+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.success+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.warning+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.error+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.info+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_primary+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_secondary+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_success+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_warning+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_error+"p-1"),
                IconBadge(icon="home", cls=BackgroundT.grad_info+"p-1"),
                cls="space-x-2 mb-4"
            )
        )

playground = Section(cls=(SectionT.default))(
    # input_field_component,
    P("This is your playground for developing Flowbite components.\n Go to and modify ",
Code("app/pages/playground.py")," to see the components in action.",cls=ParagrafT.lead+TextT.center),

    # component,

    form_component,
    badges_component,
    # component_showcase(Div(
    #         DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-full'),
    #         DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-sm')
    #     ), code="""Div(
    #         DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-full'),
    #         DiceBearAvatar("Nikola", cls='w-10 h-10 rounded-sm')
    #     )""", id="example_0",cls='mt-2 mb-6'),

    DivCentered(
        UploadZone(label="Click to upload or drag and drop file",help_text="SVG, PNG, JPG or GIF (MAX. 800x400px)",id="file_input"),

        NotStr("""        


        """)
    )
) 