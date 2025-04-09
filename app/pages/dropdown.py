from fasthtml.common import Div, P, Html, Head, Body, Br, Code, A, H1, H2, H3, Span
from fastbite.all import *
from utils import component_showcase
from fasthtml.common import Script

def dropdown_showcase():
    """Page showcasing Dropdown components"""
    
    return Container(
        H1("Dropdown Components", link=True, cls="mb-8 mt-6"),
        
        P("The dropdown component can be used to show a list of menu items when clicking on an element such as a button and hiding it when focusing outside of the triggering element.", cls="mb-6 text-lg"),
        
        P(
            "Make sure to include ",
            A("Fastbite's JavaScript file", href="/docs/getting-started/quickstart/"),
            " inside your project to enable dropdowns.",
            cls="mb-6"
        ),
        
        # Dropdown Examples section
        H2("Dropdown Examples", link=True, cls="mb-4 mt-10"),
        dropdown_examples(),
    )

def dropdown_examples():
    """Create the dropdown components showcase section"""
    
    return Div(
        # Basic Dropdown
        H3("Basic Dropdown", link=True, cls="mb-3"),
        P(
            "If you want to show a dropdown menu when clicking on an element make sure that you add the data attribute ",
            Code("data-dropdown-toggle=\"dropdownId\""),
            " to the element (ie. a button) that will trigger the dropdown menu. The ",
            Code("dropdownId"),
            " is the id of the dropdown menu element."
        ),
        
        component_showcase(
            Div(
                DropdownButton("Dropdown button", controls="dropdown-example-1"),
                Dropdown(
                    DropdownItem("Dashboard"),
                    DropdownItem("Settings"),
                    DropdownItem("Earnings"),
                    DropdownItem("Sign out"),
                    id="dropdown-example-1"
                ),
                cls="relative"
            ),
            code="""# Import at the top of your file
from fastbite.all import DropdownButton, Dropdown, DropdownItem

# Basic dropdown
DropdownButton("Dropdown button", controls="dropdown-example-1")
Dropdown(
    DropdownItem("Dashboard"),
    DropdownItem("Settings"),
    DropdownItem("Earnings"),
    DropdownItem("Sign out"),
    id="dropdown-example-1"
)""",
            id="basic-dropdown"
        ),
        
        Br(),
        
        # Dropdown with Hover
        H3("Dropdown Hover", link=True, cls="mb-3"),
        P(
            "Use the ",
            Code("data_dropdown_trigger=\"hover\""),
            " parameter to make the dropdown appear on hover instead of click. There's a 300ms default delay when showing or hiding the dropdown due to UI/UX reasons."
        ),
        
        component_showcase(
            Div(
                DropdownButton("Dropdown hover",controls="dropdownHover",data_dropdown_trigger="hover"),
                DropdownContainer(
                    DropdownList(
                        DropdownItem("Dashboard"),
                        DropdownItem("Settings"),
                        DropdownItem("Earnings"),
                        DropdownItem("Sign out")
                    ),
                    id="dropdownHover"
                ),
                cls="relative"
            ),
            code="""DropdownButton("Dropdown hover",controls="dropdownHover",data_dropdown_trigger="hover"),
    DropdownContainer(
        DropdownList(
            DropdownItem("Dashboard"),
            DropdownItem("Settings"),
            DropdownItem("Earnings"),
            DropdownItem("Sign out")
        ),
        id="dropdownHover"    
)""",
            id="hover-dropdown"
        ),
        
        Br(),
        
        # Dropdown with Header
        H3("Dropdown with Header", link=True, cls="mb-3"),
        P("Use this example to show extra information outside of the list of menu items inside the dropdown."),
        
        component_showcase(
            Div(
                DropdownButton("Dropdown with header", controls="dropdown-header-example"),
                Dropdown(
                    DropdownItem("Dashboard"),
                    DropdownItem("Settings"),
                    DropdownItem("Earnings"),
                    id="dropdown-header-example",
                    header=DropdownHeader(
                        Div("Bonnie Green"),
                        Div("name@fastbite.com", cls="font-medium truncate")
                    ),
                    devider=True
                ),
                cls="relative"
            ),
            code="""# Dropdown with header
DropdownButton("Dropdown with header", controls="dropdown-header-example")
Dropdown(
    DropdownItem("Dashboard"),
    DropdownItem("Settings"),
    DropdownItem("Earnings"),
    id="dropdown-header-example",
    header=DropdownHeader(
        Div("Bonnie Green"),
        Div("name@fastbite.com", cls="font-medium truncate")
    ),
    devider=True
)""",
            id="header-dropdown"
        ),
        
        Br(),
        
        # Dropdown with Divider
        H3("Dropdown with Divider", link=True, cls="mb-3"),
        P(
            "You can use the ",
            Code("devider=True"),
            " parameter to add separators inside the dropdown menu."
        ),
        
        component_showcase(
            Div(
                DropdownButton("Dropdown with divider", controls="dropdown-divider-example"),
                DropdownContainer(
                    DropdownList(
                        DropdownItem("Dashboard"),
                        DropdownItem("Settings"),
                        DropdownItem("Earnings")
                    ),
                    Div(
                        A("Separated link", href="#", cls="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"),
                        cls="py-2"
                    ),
                    id="dropdown-divider-example",
                    devider=True
                ),
                cls="relative"
            ),
            code="""# Dropdown with divider
DropdownButton("Dropdown with divider", controls="dropdown-divider-example")
DropdownContainer(
    DropdownList(
        DropdownItem("Dashboard"),
        DropdownItem("Settings"),
        DropdownItem("Earnings")
    ),
    Div(
        A("Separated link", href="#", cls="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white"),
        cls="py-2"
    ),
    id="dropdown-divider-example",
    devider=True
)""",
            id="divider-dropdown"
        ),
        
        Br(),
        
        # Custom Dropdown Button
        H3("Custom Dropdown Button", link=True, cls="mb-3"),
        P("You can customize the appearance of the dropdown button by passing additional classes."),
        
        component_showcase(
            Div(
                DropdownButton(
                    "Custom dropdown", 
                    controls="dropdown-custom-example",
                    cls="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center",
                ),
                Dropdown(
                    DropdownItem("Dashboard"),
                    DropdownItem("Settings"),
                    DropdownItem("Earnings"),
                    DropdownItem("Sign out"),
                    id="dropdown-custom-example"
                ),
                cls="relative"
            ),
            code="""# Custom dropdown button
DropdownButton(
    "Custom dropdown", 
    controls="dropdown-custom-example",
    cls="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center",
)
Dropdown(
    DropdownItem("Dashboard"),
    DropdownItem("Settings"),
    DropdownItem("Earnings"),
    DropdownItem("Sign out"),
    id="dropdown-custom-example"
)""",
            id="custom-button-dropdown"
        ),
        
        # Add javascript to initialize dropdowns
        Script("window.addEventListener('load', function() { initDropdowns(); });"),
    )

# Export the dropdown_showcase function
dropdown_components = dropdown_showcase() 