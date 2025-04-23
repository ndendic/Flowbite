from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import *
from utils import component_showcase

navigation_components = Div(
    H1("Navigation Components", link=True),
    
    P("Fastbite provides a comprehensive set of navigation components for creating sidebars, navigation bars, and other navigational elements in your applications."),
    
    H2("NavContainer and NavLi Components", link=True),
    
    P("The basic building blocks for creating navigation menus."),
    
    H3("Basic Navigation", link=True),
    P("The ", Code("NavContainer"), " component creates a sidebar navigation with list items using ", Code("NavLi"), " components:"),

    component_showcase(
        Div(
            NavContainer(
                NavLi("Dashboard",icon="lucide:home", href="#"),
                NavLi("Projects",icon="lucide:folder", href="#"),
                NavLi("Messages",icon="lucide:mail", href="#"),
                NavLi("Settings",icon="lucide:settings", href="#")
            ),
            cls="w-64"
        ),
        code="""from fastbite.all import NavContainer, NavLi

# Create a basic navigation menu
NavContainer(
    NavLi("Dashboard",icon="lucide:home", href="#"),
    NavLi("Projects",icon="lucide:folder", href="#"),
    NavLi("Messages",icon="lucide:mail", href="#"),
    NavLi("Settings",icon="lucide:settings", href="#")
)""",
        id="basic-navigation"
    ),
    
    Br(),
    
    H3("Navigation Themes", link=True),
    P("The ", Code("NavContainer"), " supports different themes through the ", Code("cls"), " parameter with ", Code("NavT"), " enum values:"),

    component_showcase(
        Div(
            Grid(
                Div(
                    P("Default Theme", cls="font-bold mb-2"),
                    NavContainer(
                        NavLi("Item 1", href="#"),
                        NavLi("Item 2", href="#"),
                        cls=NavT.default
                    ),
                ),
                Div(
                    P("Primary Theme", cls="font-bold mb-2"),
                    NavContainer(
                        NavLi("Item 1", href="#"),
                        NavLi("Item 2", href="#"),
                        cls=NavT.primary
                    ),
                ),
                cols=2,
                gap=4,
            )
        ),
        code="""from fastbite.all import NavContainer, NavLi, NavT

# Default theme
NavContainer(
    NavLi("Item 1", href="#"),
    NavLi("Item 2", href="#"),
    cls=NavT.default  # Default blue/white theme
)

# Dark theme
NavContainer(
    NavLi("Item 1", href="#"),
    NavLi("Item 2", href="#"),
    cls=NavT.primary  # Primary theme
)""",
        id="navigation-themes"
    ),
    
    Br(),
    
    H2("Nested Navigation Components", link=True),
    
    H3("Dropdown Navigation", link=True),
    P("Use ", Code("NavParentLi"), " to create expandable navigation sections with child items using ", Code("NavChildLi"), ":"),

    component_showcase(
        Div(
            NavContainer(
                NavLi("Dashboard",icon="lucide:home", href="#"),
                NavParentLi(
                    NavChildLi("All projects", href="#"),
                    NavChildLi("Active projects", href="#"),
                    NavChildLi("Archived projects", href="#"),
                    label="Projects",
                   icon="lucide:folder",
                    id="projectsNav"
                ),
                NavLi("Messages",icon="lucide:mail", href="#")
            ),
            cls="w-64"
        ),
        code="""Div(
    NavContainer(
        NavLi("Dashboard",icon="lucide:home", href="#"),
        NavParentLi(
            NavChildLi("All projects", href="#"),
            NavChildLi("Active projects", href="#"),
            NavChildLi("Archived projects", href="#"),
            label="Projects",
            icon="lucide:folder",
            id="projectsNav"
        ),
        NavLi("Messages",icon="lucide:mail", href="#")
    ),
    cls="w-64"
)""",
        id="dropdown-navigation"
    ),
    
    Br(),
    
    H3("Structured Navigation", link=True),
    P("Add structure to your navigation with ", Code("NavHeaderLi"), ", ", Code("NavSubtitle"), ", and ", Code("NavDividerLi"), " components:"),

    component_showcase(
        Div(
            NavContainer(
                NavHeaderLi(label="Admin Panel", href="#"),
                NavSubtitle("Main navigation"),
                NavLi("Dashboard",icon="lucide:home", href="#"),
                NavLi("Users",icon="lucide:users", href="#"),
                NavDividerLi(),
                NavSubtitle("Settings"),
                NavLi("Profile",icon="lucide:user", href="#"),
                NavLi("Security",icon="lucide:shield", href="#")
            ),
            cls="w-64"
        ),
        code="""from fastbite.all import NavContainer, NavLi, NavHeaderLi, NavSubtitle, NavDividerLi

NavContainer(
    # Header with large text and link
    NavHeaderLi(label="Admin Panel", href="#"),
    
    # Subtitle for categorizing items
    NavSubtitle("Main navigation"),
    NavLi("Dashboard",icon="lucide:home", href="#"),
    NavLi("Users",icon="lucide:users", href="#"),
    
    # Divider for visual separation
    NavDividerLi(),
    
    NavSubtitle("Settings"),
    NavLi("Profile",icon="lucide:user", href="#"),
    NavLi("Security",icon="lucide:shield", href="#")
)""",
        id="structured-navigation"
    ),
    
    Br(),
    
    H2("Navigation Bars", link=True),
    
    H3("Main Navigation Bar", link=True),
    P("Create responsive navigation bars with the ", Code("NavBar"), " and ", Code("NavBarItem"), " components:"),

    component_showcase(
        Div(
            NavBar(
                NavBarItem("Home", href="#"),
                NavBarItem("Features", href="#"),
                NavBarItem("Pricing", href="#"),
                NavBarItem("Contact", href="#"),
                brand=H4("Fastbite", cls="text-xl font-semibold")
            )
        ),
        code="""from fastbite.all import NavBar, NavBarItem
from fasthtml.common import H4

NavBar(
    NavBarItem("Home", href="#"),
    NavBarItem("Features", href="#"),
    NavBarItem("Pricing", href="#"),
    NavBarItem("Contact", href="#"),
    # Logo/brand on the left side
    brand=H4("Fastbite", cls="text-xl font-semibold")
)""",
        id="main-navbar"
    ),
    
    Br(),
    
    H3("Secondary Navigation Bar", link=True),
    P("Add secondary navigation with the ", Code("SubNavBar"), " and ", Code("SubNavBarItem"), " components:"),

    component_showcase(
        Div(
            SubNavBar(
                SubNavBarItem("Overview", href="#"),
                SubNavBarItem("Features", href="#"),
                SubNavBarItem("Documentation", href="#"),
                SubNavBarItem("Resources", href="#")
            )
        ),
        code="""from fastbite.all import SubNavBar, SubNavBarItem

SubNavBar(
    SubNavBarItem("Overview", href="#"),
    SubNavBarItem("Features", href="#"),
    SubNavBarItem("Documentation", href="#"),
    SubNavBarItem("Resources", href="#")
)""",
        id="secondary-navbar"
    ),
    
    Br(),
    
    H3("Combined Navigation Example", link=True),
    P("Combine multiple navigation components to create complex navigation systems:"),

    component_showcase(
        Div(
            Div(
                NavBar(
                    NavBarItem("Home", href="#"),
                    NavBarItem("Products", href="#"),
                    NavBarItem("Services", href="#"),
                    NavBarItem("About", href="#"),
                    brand=H4("Company Name", cls="text-xl font-semibold")
                ),
                SubNavBar(
                    SubNavBarItem("Overview", href="#"),
                    SubNavBarItem("Features", href="#"),
                    SubNavBarItem("Pricing", href="#"),
                    SubNavBarItem("FAQ", href="#")
                )
            )
        ),
        code="""from fastbite.all import NavBar, NavBarItem, SubNavBar, SubNavBarItem
from fasthtml.common import Div, H4

Div(
    # Main navigation bar
    NavBar(
        NavBarItem("Home", href="#"),
        NavBarItem("Products", href="#"),
        NavBarItem("Services", href="#"),
        NavBarItem("About", href="#"),
        brand=H4("Company Name", cls="text-xl font-semibold")
    ),
    # Secondary navigation bar
    SubNavBar(
        SubNavBarItem("Overview", href="#"),
        SubNavBarItem("Features", href="#"),
        SubNavBarItem("Pricing", href="#"),
        SubNavBarItem("FAQ", href="#")
    )
)""",
        id="combined-navbar"
    ),
    
    Br(),
    
    H2("Navigation Best Practices", link=True),
    
    P("Here are some best practices for using navigation components in your applications:"),
    
    Ul(
        Li("Keep navigation labels short and clear"),
        Li("Use icons to enhance visual recognition"),
        Li("Group related items together"),
        Li("Use dividers to separate different sections"),
        Li("Limit the number of main navigation items to 7 ± 2"),
        Li("Ensure proper contrast between navigation text and background"),
        Li("Make active/current page clearly identifiable"),
        cls="list-disc pl-5 space-y-2 mb-6"
    ),
    
    Br(),
    
    H2("API Reference", link=True),
    
    H3("NavContainer", link=True),
    P("Creates a navigation container for sidebar navigation:"),
    
    Table(
        Thead(
            Tr(
                Th("Parameter", cls="px-4 py-2"),
                Th("Type", cls="px-4 py-2"),
                Th("Default", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("*li", cls="px-4 py-2 border"),
                Td("FT", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("Navigation list items", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("NavT.default", cls="px-4 py-2 border"),
                Td("Additional classes for styling", cls="px-4 py-2 border")
            ),
            Tr(
                Td("parent", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("True", cls="px-4 py-2 border"),
                Td("Whether this nav is a parent or sub nav", cls="px-4 py-2 border")
            ),
            Tr(
                Td("uk_nav", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("False", cls="px-4 py-2 border"),
                Td("Enable collapsible behavior", cls="px-4 py-2 border")
            ),
            Tr(
                Td("sticky", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("False", cls="px-4 py-2 border"),
                Td("Whether to stick to top of page while scrolling", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("NavLi", link=True),
    P("Creates a navigation list item:"),
    
    Table(
        Thead(
            Tr(
                Th("Parameter", cls="px-4 py-2"),
                Th("Type", cls="px-4 py-2"),
                Th("Default", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("*c", cls="px-4 py-2 border"),
                Td("FT", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("Child components", cls="px-4 py-2 border")
            ),
            Tr(
                Td("label", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Label text for the navigation item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("icon", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Icon name for the navigation item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("href", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("'#'", cls="px-4 py-2 border"),
                Td("URL for the navigation item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("()", cls="px-4 py-2 border"),
                Td("Additional classes for styling", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("NavParentLi", link=True),
    P("Creates a navigation list item with a dropdown:"),
    
    Table(
        Thead(
            Tr(
                Th("Parameter", cls="px-4 py-2"),
                Th("Type", cls="px-4 py-2"),
                Th("Default", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("*nav_items", cls="px-4 py-2 border"),
                Td("FT", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("Child navigation items", cls="px-4 py-2 border")
            ),
            Tr(
                Td("label", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Label text for the parent item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("icon", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Icon name for the parent item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("id", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("random", cls="px-4 py-2 border"),
                Td("Unique ID for the dropdown", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("()", cls="px-4 py-2 border"),
                Td("Additional classes for styling", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("NavBar Component", link=True),
    P("Creates a responsive navigation bar:"),
    
    Table(
        Thead(
            Tr(
                Th("Parameter", cls="px-4 py-2"),
                Th("Type", cls="px-4 py-2"),
                Th("Default", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("*c", cls="px-4 py-2 border"),
                Td("FT", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("NavBarItem components", cls="px-4 py-2 border")
            ),
            Tr(
                Td("brand", cls="px-4 py-2 border"),
                Td("FT", cls="px-4 py-2 border"),
                Td("H4('Title')", cls="px-4 py-2 border"),
                Td("Brand/logo component for left side", cls="px-4 py-2 border")
            ),
            Tr(
                Td("right_cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("'items-center space-x-4'", cls="px-4 py-2 border"),
                Td("Spacing for desktop links", cls="px-4 py-2 border")
            ),
            Tr(
                Td("mobile_cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("'space-y-4'", cls="px-4 py-2 border"),
                Td("Spacing for mobile links", cls="px-4 py-2 border")
            ),
            Tr(
                Td("sticky", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("False", cls="px-4 py-2 border"),
                Td("Whether to stick to top while scrolling", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("'bg-gray-50...'", cls="px-4 py-2 border"),
                Td("Classes for navbar styling", cls="px-4 py-2 border")
            ),
            Tr(
                Td("menu_id", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("None (random)", cls="px-4 py-2 border"),
                Td("ID for mobile menu toggle", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    )
) 