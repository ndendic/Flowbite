import fasthtml.common as fh
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from utils import component_showcase
from theme_switcher import ThemeSwitcher
from extracted.input_field import component as input_field_component
from extracted.file_input import component as file_input_component

from ft_datastar import *

datastar_example = fh.Div(
        H2("Datastar + FastHTML Example", cls="text-xl font-bold mb-4"),
        fh.Div(
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
        fh.Div(
            "Count: ",
            fh.Span(ds_text("$count"), cls="font-mono"),
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
        fh.Div(
            fh.A("Default",cls=AT.default),
            fh.A("Muted",cls=AT.muted),
            fh.A("Text",cls=AT.text),
            fh.A("Primary",cls=AT.primary),
            fh.A("Classic",cls=AT.classic),
            cls="space-x-2 mb-4"
        ),
        H3("List",cls="mb-4"),
        fh.Div(
            fh.Ul("Unordered list",fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.ul+"mb-4"),
            fh.Ol("Ordered list",fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.ol+"mb-4"),
            fh.Ul("Unstyled",fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.unstyled+"mb-4"),

            fh.Ul("Nested",
                fh.Ul("Nested ordered list",fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.nested_ol+"mb-4"),
                fh.Ul("Nested unordered list",fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.nested_ul+"mb-4"),
            ),
            H4("Horizontal",cls="mb-4"),
            fh.Ul(fh.Li("Item 1"),fh.Li("Item 2"),fh.Li("Item 3"),cls=ListT.horizontal+"mb-4"),
            fh.Ul("Definition list",
                fh.Div(fh.Dt("Item 1", cls=ListT.dt),fh.Dd("Item 1", cls=ListT.dd)),
                fh.Div(fh.Dt("Item 2", cls=ListT.dt),fh.Dd("Item 2", cls=ListT.dd)),
                fh.Div(fh.Dt("Item 3", cls=ListT.dt),fh.Dd("Item 3", cls=ListT.dd)),
                cls=ListT.dl+"mb-4"
            ),

        ),
        
    )
badges_component = fh.Div(
            H3("Badges",cls="mb-4"),
            H4("Default",cls="mb-4"),
            fh.Div(
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
            fh.Div(
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
            fh.Div(
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
            fh.Div(
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
            fh.Div(
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
            fh.Div(
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
cards = Grid(
        Card(
            CardHeader(
                CardTitle("Noteworthy technology acquisitions 2021"),
        ),
            CardBody("Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.")
        ),
        Card(
            CardHeader(
                CardTitle("Noteworthy technology acquisitions 2021"),
            ),
            CardBody("Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."),
            cls=CardT.default+CardT.hover
        ),
        Card(
            CardHeader(
                CardTitle("Noteworthy technology acquisitions 2021"),
            ),
            CardBody("Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."),
            cls=CardT.primary+CardT.hover
        ),
        Card(
            CardHeader(
                CardTitle("Noteworthy technology acquisitions 2021"),
            ),
            CardBody("Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."),
            cls=CardT.secondary+CardT.hover
        ),
        Card(
            CardHeader(
                CardTitle("Noteworthy technology acquisitions 2021"),
            ),
            CardBody("Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."),
            cls=CardT.destructive+CardT.hover
        ),
        Card(
            CardHeader(
                CardTitle("Plain Card with footer Button"),
            ),
            CardBody("Here is a plain card with a footer button. It is a good way to add a button to the card, and it is also a good way to add a footer to the card.",
            ),
            footer=fh.Div(Button("Read more", cls=ButtonT.primary), Button("Subscribe", cls=ButtonT.secondary), cls="flex space-x-2"),
            cls=CardT.hover+CardT.plain
        ),

        Card(
            CardHeader(
                CardTitle("Plain Card with footer Button"),
            ),
            CardBody("Here is a plain card with a footer button. It is a good way to add a button to the card, and it is also a good way to add a footer to the card.",
            ),
            footer=fh.Div(Button("Read more", cls=ButtonT.primary), Button("Subscribe", cls=ButtonT.secondary), cls="flex space-x-2"),
            cls=CardT.hover+CardT.plain
        ),
        cols=2,
        cls="space-y-2 space-x-2 mt-2"
    )
modals= fh.Div(
    Button("Default Modal", data_modal_target="modal-id", data_modal_toggle="modal-id"),
    Modal(
        P("""With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
The European Unionâs General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. 
It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them."""
            ,cls=TextT.gray
        ),
        header=[
            ModalTitle("Modal Title"),
            ModalCloseButton(modal_id="modal-id")
        ],
        footer=Button("Close", data_modal_toggle="modal-id", cls=ButtonT.primary),
        id="modal-id"
    ),
    Button("Modal 2XL", data_modal_target="modal-id2", data_modal_toggle="modal-id2"),
    Modal(
        P("""With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
The European Unionâs General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. 
It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them."""
            ,cls=TextT.gray
        ),
        header=[
            ModalTitle("Modal Title"),
            ModalCloseButton(modal_id="modal-id2")
        ],
        footer=[Button("Close", data_modal_toggle="modal-id2", cls=ButtonT.primary+"mr-2"),
                Button("Save", data_modal_toggle="modal-id2", cls=ButtonT.secondary)],
        id="modal-id2",
        dialog_cls=ModalT._2xl,
        placement=ModalT.top_left
    ),

    )
icon_links = fh.Div(
        H3("Icon Links"),
        fh.Div(cls="space-x-2")(
        IconLink("home", cls=AT.default),
        IconLink("home", cls=AT.primary),
        IconLink("home", cls=AT.muted),
        IconLink("home", cls=AT.classic),
        ),
        H3("Icon Links with button"),
        fh.Div(cls="space-x-2")(
        IconLink("home", button=True),
        IconLink("home", cls=ButtonT.ghost, button=True),
        IconLink("home", cls=ButtonT.primary, button=True),
        IconLink("home", cls=ButtonT.secondary, button=True),
        IconLink("home", cls=ButtonT.success, button=True),
        IconLink("home", cls=ButtonT.warning, button=True),
        IconLink("home", cls=ButtonT.error, button=True),
        ),
        cls="space-y-2"
    )
progress = fh.Div(
        H3("Progress",cls="mb-2"),
    Progress(value="50", cls="mb-2"),
    Progress(value="50", label="Progress Label" ,cls="mb-2"),
    Progress(value="20",size='sm', label="Small",cls="mb-2"),
    Progress(value="40",label="Default Medium",cls="mb-2"),
    Progress(value="60",size='lg', label="Large",cls="mb-2"),
    Progress(value="80",size='xl', label="XLarge",cls="mb-2"),
    Progress("80%",value="80",size="lg", label="Label Inside",cls="mb-2"),
    H3("Progress Colors",cls="mb-2"),
    Progress(value="50",label="Primary", progress_cls=ProgressT.progress_primary+"animate-pulse"),
    Progress(value="50",label="Dark", progress_cls=ProgressT.progress_dark),
    Progress(value="50",label="Green", progress_cls=ProgressT.progress_green),
    Progress(value="50",label="Blue", progress_cls=ProgressT.progress_blue),
    Progress(value="50",label="Red", progress_cls=ProgressT.progress_red),
    Progress(value="50",label="Yellow", progress_cls=ProgressT.progress_yellow),
    Progress(value="50",label="Purple", progress_cls=ProgressT.progress_purple),
    Progress(value="50",label="Pink", progress_cls=ProgressT.progress_pink),
    cls="space-y-2"
)
placeholders = fh.Div(
        Placeholder(cls=PlaceholderT.dashed),
        Placeholder(Icon("plus"),cls=PlaceholderT.gray),
        Placeholder(Placeholder(Icon("plus"),cls=PlaceholderT.gray),cls=PlaceholderT.dashed+ContainerSize.sm),
        Placeholder(Placeholder(Icon("plus"),cls=(PlaceholderT.gray,"h-48")),cls=(PlaceholderT.dashed,ContainerSize.lg)),
        Placeholder(Placeholder(Icon("plus"),cls=PlaceholderT.gray),cls=PlaceholderT.dashed+ContainerSize.xl),
        cls="space-y-2"
    )
navs = NavContainer(
        NavHeaderLi(label="Flowbite"),
        NavSubtitle("Subtitle"),
        NavParentLi(
            NavContainer(
                NavChildLi('Products', href='#'),
                NavChildLi('Billing', href='#'),
                NavChildLi('Invoice', href='#'),
                parent=False,
            ),
            label="Home",
            icon="home"
        ),
        NavDividerLi(),
        NavLi(label='About', href='#'),
        NavParentLi(label="Contact"),
    )
sliders = fh.Div(
        Slider([PicSumImg(id=i, alt='...', cls=SliderItemT.ease_out_in, h=400, w=800) for i in range(100, 600, 100)],
                cls="h-64 overflow-hidden rounded-lg"
        ),
        Slider(
            [
                fh.Div(
                    H2("Slide 1 Title", cls="px-4"),
                    P("Some content", cls="px-4"),
                    cls=SliderItemT.default+BackgroundT.primary+Round.lg
                ),
                fh.Div(
                    H2("Slide 2 Title", cls="px-4"),
                    P("Other content", cls="px-4"),
                    cls=SliderItemT.default+BackgroundT.secondary+Round.lg
                ),
            ],
            wrapper_cls='relative h-64 overflow-hidden rounded-lg',
            show_indicators=True,
            show_controls=False
        )
    ),


headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99']
]

table = SimpleTable(headers, rows)
playground = Section(cls=(SectionT.default))(
    # input_field_component,
    P("This is your playground for developing Flowbite components.\n Go to and modify ",
    Code("app/pages/playground.py")," to see the components in action.",cls=ParagrafT.lead+TextT.center),
    # datastar_example,
    # form_component,
    # badges_component,
    # cards,
    # modals,
    # icon_links,
    # progress,
    # placeholders,
    NavBar(
        NavBarItem("Home", href="#"),
        NavBarItem("About", href="#"),
        NavBarItem("Services", href="#"),
        NavBarItem("Pricing", href="#"),
        NavBarItem("Contact", href="#"),
        brand=DivLAligned(Icon("home"),H4("Flowpy UI", cls=(TextT.tracking_wide,TextT.primary))),
    ),
    SubNavBar(
        SubNavBarItem("Home", href="#"),
        SubNavBarItem("About", href="#"),
        SubNavBarItem("Services", href="#"),
        SubNavBarItem("Pricing", href="#"),
        SubNavBarItem("Contact", href="#"),
    ),

    # navs,
    # sliders,

    DropdownButton("Dropdown button", cls=ButtonT.link, controls="dropdown-example"),
    Dropdown(        
        DropdownItem("Dropdown item"),
        DropdownItem("Dropdown item"),
        DropdownItem("Dropdown item"),
        id="dropdown-example"
    ),

    Table(
        Thead(
            Tr(
                Th('Product name', expand=True),  # This column will expand
                Th('Color', expand=True),         # This column will shrink to content
                Th('Category'),
                Th('Price', shrink=True)          # This column will shrink to content
            )
        ),
        Tbody(
            Tr(
                Td('Apple MacBook Pro 17"', expand=True),
                Td('Silver'),
                Td('Laptop'),
                Td('$2999'),
                cls=TableT.row_hover,
            ),
            Tr(
                Td('Apple MacBook Pro 17"', expand=True),
                Td('Silver'),
                Td('Laptop'),
                Td('$2999'),
                cls=TableT.row_hover,
            ),
            Tr(
                Td('Apple MacBook Pro 17"', expand=True),
                Td('Silver'),
                Td('Laptop'),
                Td('$2999'),
                cls=TableT.row_hover,
            ),
            # ... more rows
        ),
        cls=TableT.table_default,
        container_cls="mt-4 rounded-lg",
        with_shadow=True
    ),

    DataTable(
        headers=headers,
        rows=rows,
        # expand_column=0,
        row_cls="dark:bg-gray-950",  # Custom row background
        container_cls="mt-4 rounded-lg"
    ),

    DataTable(
        headers=headers,
        rows=rows,
        expand_column=0,
        with_shadow=True,
        row_cls=TableT.row_striped,  # Custom row background
        # Table specific classes
        cls=TableT.table_default,
        # Container specific classes
        container_cls="mt-4 rounded-lg",
        striped=True,  # Will apply row_striped to tbody
        hover=True,    # Will apply row_hover to tbody
    ),
    DivCentered(
        # UploadZone(label="Click to upload or drag and drop file",help_text="SVG, PNG, JPG or GIF (MAX. 800x400px)",id="file_input"),

        fh.NotStr("""        

        """)
    )
) 