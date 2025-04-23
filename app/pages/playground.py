from pydoc import render_doc
import fasthtml.common as fh
from fasthtml.jupyter import HTMX
from fasthtml.svg import *
from fastbite.all import *
from fastbite.core import *
from utils import component_showcase
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
                Badge("Default",icon="lucide:home",cls=BadgeT.default),
                Badge("Dark",icon="lucide:home",cls=BadgeT.dark),
                Badge("Red",icon="lucide:home",cls=BadgeT.red),
                Badge("Yellow",icon="lucide:home",cls=BadgeT.yellow),
                Badge("Green",icon="lucide:home",cls=BadgeT.green),
                Badge("Blue",icon="lucide:home",cls=BadgeT.blue),
                Badge("Indigo",icon="lucide:home",cls=BadgeT.indigo),
                Badge("Purple",icon="lucide:home",cls=BadgeT.purple),
                Badge("Pink",icon="lucide:home",cls=BadgeT.pink),
                cls="space-x-2 mb-4"
            ),
            H4("Icon only",cls="mb-4"),
            fh.Div(
                IconBadge(icon="home", cls=BackgroundT.primary),
                IconBadge(icon="home", cls=BackgroundT.secondary),
                IconBadge(icon="home", cls=BackgroundT.success),
                IconBadge(icon="home", cls=BackgroundT.warning),
                IconBadge(icon="home", cls=BackgroundT.error),
                IconBadge(icon="home", cls=BackgroundT.info),
                IconBadge(icon="home", cls=BackgroundT.grad_primary),
                IconBadge(icon="home", cls=BackgroundT.grad_secondary),
                IconBadge(icon="home", cls=BackgroundT.grad_success),
                IconBadge(icon="home", cls=BackgroundT.grad_warning),
                IconBadge(icon="home", cls=BackgroundT.grad_error),
                IconBadge(icon="home", cls=BackgroundT.grad_info),
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
        Placeholder(Icon("lucide:plus"),cls=PlaceholderT.gray),
        Placeholder(Placeholder(Icon("lucide:plus"),cls=PlaceholderT.gray),cls=PlaceholderT.dashed+ContainerSize.sm),
        Placeholder(Placeholder(Icon("lucide:plus"),cls=(PlaceholderT.gray,"h-48")),cls=(PlaceholderT.dashed,ContainerSize.lg)),
        Placeholder(Placeholder(Icon("lucide:plus"),cls=PlaceholderT.gray),cls=PlaceholderT.dashed+ContainerSize.xl),
        cls="space-y-2"
    )
navs = NavContainer(
        NavHeaderLi(label="Fastbite"),
        NavSubtitle("Subtitle"),
        NavParentLi(
            NavContainer(
                NavChildLi('Products', href='#'),
                NavChildLi('Billing', href='#'),
                NavChildLi('Invoice', href='#'),
                parent=False,
            ),
            label="Home",
           icon="lucide:home"
        ),
        NavDividerLi(),
        NavLi(label='About', href='#'),
        NavParentLi(label="Contact"),
    )
navbars = fh.Div(
        NavBar(
            NavBarItem("Home", href="#"),
            NavBarItem("About", href="#"),
            NavBarItem("Services", href="#"),
            NavBarItem("Pricing", href="#"),
            NavBarItem("Contact", href="#"),
            brand=DivLAligned(Icon("lucide:home"),H4("Flowpy UI", cls=(TextT.tracking_wide,TextT.primary))),
        ),
        SubNavBar(
            SubNavBarItem("Home", href="#"),
            SubNavBarItem("About", href="#"),
            SubNavBarItem("Services", href="#"),
            SubNavBarItem("Pricing", href="#"),
            SubNavBarItem("Contact", href="#"),
        ),
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
dropdowns = fh.Div(
        DropdownButton("Dropdown button", cls=ButtonT.link, controls="dropdown-example"),
        Dropdown(        
            DropdownItem("Dropdown item"),
            DropdownItem("Dropdown item"),
            DropdownItem("Dropdown item"),
            id="dropdown-example"
        ),
        cls="space-y-2"
    ),
def iframe_str(content):
    return f"""
    <!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-gray-50 dark:bg-gray-900 antialiased \'>
    {content}
    {fh.Script(src='https://flowbite.com/docs/flowbite.min.js').__html__()}
    {fh.Script("window.onload = function () { const anchorTags = document.querySelectorAll('a'); anchorTags.forEach(function(a){a.addEventListener('click', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector('[data-dropdown-toggle]'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector('[data-modal-toggle]'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector('[data-rangepicker] input'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector('[data-drawer-show]'); if (drawerEl) { drawerEl.click(); }  }").__html__()}
    </body></html>
    """

header_controls = fh.Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
    fh.Div(cls='grid grid-cols-3')(
        fh.Div(cls='col-span-2 sm:col-span-1')(
            fh.A(href='https://github.com/themesberg/flowbite/blob/main/content/components/tables.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-gray-50 border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                    Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                ),
                'Edit on GitHub'
            )
        ),
        fh.Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
            fh.Button(data_tooltip_target='table-striped-rows-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                fh.Span('Toggle full view', cls='sr-only'),
                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                )
            ),
            fh.Div(id='table-striped-rows-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(745px, 529px);', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                'Toggle full screen',
                fh.Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
            ),  
            fh.Button(data_tooltip_target='table-striped-rows-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                fh.Span('Toggle tablet view', cls='sr-only'),
                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                )
            ),
            fh.Div(id='table-striped-rows-example-tablet-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 544px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                'Toggle tablet view',
                fh.Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
            ),
            fh.Button(data_tooltip_target='table-striped-rows-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                fh.Span('Toggle mobile view', cls='sr-only'),
                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                )
            ),
            fh.Div(id='table-striped-rows-example-mobile-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 544px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                'Toggle mobile view',
                fh.Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
            )
        ),
        fh.Div(cls='flex justify-end col-span-1')(
            fh.Button('RTL', data_tooltip_target='table-striped-rows-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
            fh.Div(id='table-striped-rows-example-toggle-rtl', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 544px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                fh.Span('Toggle RTL mode', cls='tooltip-text'),
                fh.Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
            ),
            fh.Button(data_tooltip_target='table-striped-rows-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-gray-50 border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                    Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                ),
                Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                    Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                ),
                fh.Span('Toggle dark/light mode', cls='sr-only')
            ),
            fh.Div(id='table-striped-rows-example-toggle-dark-mode-tooltip', role='tooltip', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 544px);', data_popper_placement='top', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                fh.Span('Toggle light mode', cls='tooltip-text'),
                fh.Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
            )
        )
    )
)

headers = ['Product name', 'Color', 'Category', 'Price']
rows = [
    ['Apple MacBook Pro 17"', 'Silver', 'Laptop', '$2999'],
    ['Microsoft Surface Pro', 'White', 'Laptop PC', '$1999'],
    ['Magic Mouse 2', 'Black', 'Accessories', '$99'],
    ['Dell XPS 13', 'Silver', 'Laptop', '$1499'],
    ['HP Spectre x360', 'Black', 'Laptop', '$1599'],
    ['Logitech MX Master 3', 'Gray', 'Accessories', '$99'],
    ['Samsung Galaxy S21', 'Phantom Gray', 'Smartphone', '$799'],
    ['Sony WH-1000XM4', 'Black', 'Headphones', '$349'],
    ['Google Pixel 5', 'Just Black', 'Smartphone', '$699'],
    ['Amazon Echo Dot', 'Charcoal', 'Smart Home', '$49'],
    ['Apple iPad Pro', 'Space Gray', 'Tablet', '$999'],
    ['Asus ROG Strix', 'Black', 'Gaming Laptop', '$1999'],
    ['Bose QuietComfort 35', 'Silver', 'Headphones', '$299'],
    ['Apple iPhone 12', 'Black', 'Smartphone', '$799'],
    ['Sony A7 III', 'Black', 'Mirrorless Camera', '$1499'],
    ['Canon EOS R6', 'White', 'Mirrorless Camera', '$1999'],
    ['DJI Mavic Air 2', 'Silver', 'Drone', '$799'],
    ['DJI Mavic 3', 'Black', 'Drone', '$1299'],
    ['Panasonic Lumix G9', 'Black', 'Mirrorless Camera', '$1499'],
    ['DJI Osmo Action', 'Black', 'Action Camera', '$299'],
    ['DJI Osmo Pocket', 'White', 'Action Camera', '$399'],
    ['DJI Osmo Mobile 3', 'Black', 'Gimbal', '$199'],
]
footer = ["Total", "3", "3", "$6000"]
tables = fh.Div(
        H4("Default Simple Table"),
        SimpleTable(headers, rows),

        H4("DataTable"),
        DataTable(id="datatable-default",
            headers=headers,
            rows=rows,
            sortable=True,
            searchable=True,
            # expand_column=0,
            # row_cls="dark:bg-gray-950",  # Custom row background
            container_cls="mt-4 rounded-lg"
        ),

        H4("Striped Table"),
        DataTable(
            headers=headers,
            rows=rows,
            footer=footer,
            expand_column=0,
            with_shadow=True,
            cls=TableT.table_default,
            container_cls="mt-4 rounded-lg",
            id="datatable-striped",
            sortable=True,
            searchable=True,
            striped=True,  # Will apply row_striped to tbody
            hover=True,    # Will apply row_hover to tbody
        ),

        H4("Hover Table"),
        DataTable(
            headers=headers,
            rows=rows,
            expand_column=0,
            with_shadow=True,
            row_cls=TableT.row_hover,  # Custom row background
            cls=TableT.table_default,
            container_cls="mt-4 rounded-lg",
        ),

        H4("Custom Table"),
        Table(
            Thead(
                Tr(
                    Th('Product name', expand=True),  # This column will expand
                    Th('Color', expand=True),         # This column will shrink to content
                    Th('Category'),
                    Th('Price', shrink=True),         # This column will shrink to content
                    header=True
                ),
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
                    Td('MacBook Pro 17"', expand=True),
                    Td('Silver'),
                    Td('Laptop'),
                    Td('$100'),
                    cls=TableT.row_hover,
                ),
                Tr(
                    Td('MacBook Pro 19"', expand=True),
                    Td('Silver'),
                    Td('Laptop'),
                    Td('$300'),
                    cls=TableT.row_hover,
                ),
                # ... more rows
            ),
            fh.Script("""
            if (document.getElementById('my_table') && typeof simpleDatatables.DataTable !== 'undefined') {
                const dataTable = new simpleDatatables.DataTable('#my_table', {
                    searchable: false,
                    perPageSelect: false
                });
            }
            """),
            cls=TableT.table_default,
            container_cls="mt-4 rounded-lg",
            id="my_table",
            with_shadow=True
        ),

    )

markdown_example = """
# Hello World

This is a test of the markdown component.

## Subheading

This is a subheading.

![Fastbite Logo](images/logo.png)

[Fastbite](https://flowbite.com) is a library of pre-built components for Tailwind CSS.

> This is a block quote.
> It can span multiple paragraphs,
> if you like.


"""

playground = Section(cls=(SectionT.default))(
    # input_field_component,
    P("This is your playground for developing Fastbite components.\n Go to and modify ",
    Code("app/pages/playground.py")," to see the components in action.",cls=PT.lead+TextT.center),
    # datastar_example,
    # form_component,
    # badges_component,
    # cards,
    # modals,
    # icon_links,
    # progress,
    # placeholders,
    # tables,
    # navbars,
    # navs,
    # sliders,
    # dropdowns,
    Modal(
        P("This is the default modal body content.", cls=TextT.gray), 
        P("You can put any content here."),        
    header=[
        ModalTitle("Default Modal Header"),
        ModalCloseButton(modal_id='ModalBasic') # Use the specific close button
    ],
    footer=fh.Div(
        Button("Accept", cls=ButtonT.primary, data_on_click=f'$show{"ModalBasic"} = !$show{"ModalBasic"}'), # Use toggle to close
        Button("Decline", cls=ButtonT.secondary, data_on_click=f'$show{"ModalBasic"} = !$show{"ModalBasic"}'),
        cls="space-x-2"
    ),
    id='ModalBasic',
    ),
    Button("Click me",
        data_on_click='$showModalBasic = !$showModalBasic'
    ),
    # Accordion(
    #     AccordionItem(
    #         "Accordion Item 1",
    #         "Accordion Item 2",
    #         "Accordion Item 3"
    #     )
    # ),
    # tables,

    # render_md(markdown_example),
    # render_md_article(markdown_example),
    DivCentered(
        # UploadZone(label="Click to upload or drag and drop file",help_text="SVG, PNG, JPG or GIF (MAX. 800x400px)",id="file_input"),

        fh.NotStr("""        

        """)
    )
) 