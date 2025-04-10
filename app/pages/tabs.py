from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

def _basic_tabs_section():
    return Section(
        H2("Basic Tabs", link=True, cls="mb-4 mt-10"),
        P("Tabs provide a way to organize content into separate views that users can navigate between."),
        
        H3("Simple Tabs", link=True, cls="mb-3"),
        P("Create a basic tab interface with ", Code("TabContainer"), " and ", Code("TabItem"), " components:"),
        
        component_showcase(
            Div(
                # Tab navigation
                TabContainer(
                    TabItem("Profile", controls="profile"),
                    TabItem("Settings", controls="settings"),
                    TabItem("Messages", controls="messages"),
                ),
                # Tab content
                Div(
                    Div(P("Profile content goes here..."), id="profile", cls="p-4"),
                    Div(P("Settings content goes here..."), id="settings", cls="hidden p-4"),
                    Div(P("Messages content goes here..."), id="messages", cls="hidden p-4")
                )
            ),
            code="""from fastbite.all import TabContainer, TabItem

# Create tab navigation
tabs = TabContainer(
    TabItem("Profile", controls="profile"),
    TabItem("Settings", controls="settings"),
    TabItem("Messages", controls="messages"),
)

# Create tab content panels
content = Div(
    Div(P("Profile content goes here..."), id="profile", cls="p-4"),
    Div(P("Settings content goes here..."), id="settings", cls="hidden p-4"),
    Div(P("Messages content goes here..."), id="messages", cls="hidden p-4")
)

# Combine tabs and content
Div(tabs, content)""",
            id="basic-tabs"
        ),
        
        Br(),
        
        H3("Tabs with Rich Content", link=True, cls="mb-3"),
        P("Tabs can contain more complex content in each panel:"),
        
        component_showcase(
            Div(
                TabContainer(
                    TabItem("Products", controls="products-panel"),
                    TabItem("Services", controls="services-panel"),
                    TabItem("Support", controls="support-panel"),
                ),
                Div(
                    Div(
                        H3("Featured Products", cls="mb-3"),
                        Ul(cls="list-disc pl-5")(
                            Li("Product A"),
                            Li("Product B"),
                            Li("Product C")
                        ),
                        id="products-panel", 
                        cls="p-4"
                    ),
                    Div(
                        H3("Our Services", cls="mb-3"),
                        Ul(cls="list-disc pl-5")(
                            Li("Consulting"),
                            Li("Development"),
                            Li("Support")
                        ),
                        id="services-panel", 
                        cls="hidden p-4"
                    ),
                    Div(
                        H3("Support Options", cls="mb-3"),
                        P("Contact us via:"),
                        Ul(cls="list-disc pl-5")(
                            Li("Email: support@example.com"),
                            Li("Phone: +1 234 567 890"),
                            Li("Chat: Available 24/7")
                        ),
                        id="support-panel", 
                        cls="hidden p-4"
                    )
                )
            ),
            code="""from fastbite.all import TabContainer, TabItem

# Create tab navigation
tabs = TabContainer(
    TabItem("Products", controls="products-panel"),
    TabItem("Services", controls="services-panel"),
    TabItem("Support", controls="support-panel"),
)

# Create content panels with rich content
content = Div(
    Div(
        H3("Featured Products", cls="mb-3"),
        Ul(cls="list-disc pl-5")(
            Li("Product A"),
            Li("Product B"),
            Li("Product C")
        ),
        id="products-panel", 
        cls="p-4"
    ),
    Div(
        H3("Our Services", cls="mb-3"),
        Ul(cls="list-disc pl-5")(
            Li("Consulting"),
            Li("Development"),
            Li("Support")
        ),
        id="services-panel", 
        cls="hidden p-4"
    ),
    Div(
        H3("Support Options", cls="mb-3"),
        P("Contact us via:"),
        Ul(cls="list-disc pl-5")(
            Li("Email: support@example.com"),
            Li("Phone: +1 234 567 890"),
            Li("Chat: Available 24/7")
        ),
        id="support-panel", 
        cls="hidden p-4"
    )
)

# Combine tabs and content
Div(tabs, content)""",
            id="rich-content-tabs"
        ),
        
        Br(),
    )

def _customized_tabs_section():
    return Section(
        H2("Customized Tabs", link=True, cls="mb-4 mt-10"),
        P("Tabs can be customized using the provided parameters."),
        
        H3("Custom Active and Inactive Styles", link=True, cls="mb-3"),
        P("Customize the appearance of active and inactive tabs using the ", Code("active_items_cls"), " and ", Code("inactive_items_cls"), " parameters:"),
        
        component_showcase(
            Div(
                # Custom styled tabs
                TabContainer(
                    TabItem("Tab 1", controls="tab-1-custom"),
                    TabItem("Tab 2", controls="tab-2-custom"),
                    TabItem("Tab 3", controls="tab-3-custom"),
                    active_items_cls="text-blue-600 hover:text-blue-800 dark:text-blue-500 dark:hover:text-blue-400 border-blue-600 dark:border-blue-500",
                    inactive_items_cls="text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-300 border-transparent hover:border-gray-300 dark:border-transparent"
                ),
                # Tab content
                Div(
                    Div(P("Content for Tab 1"), id="tab-1-custom", cls="p-4 bg-blue-50 dark:bg-gray-800 rounded-lg"),
                    Div(P("Content for Tab 2"), id="tab-2-custom", cls="hidden p-4 bg-blue-50 dark:bg-gray-800 rounded-lg"),
                    Div(P("Content for Tab 3"), id="tab-3-custom", cls="hidden p-4 bg-blue-50 dark:bg-gray-800 rounded-lg")
                )
            ),
            code="""from fastbite.all import TabContainer, TabItem

# Custom color styling for tabs
custom_tabs = TabContainer(
    TabItem("Tab 1", controls="tab-1-custom"),
    TabItem("Tab 2", controls="tab-2-custom"),
    TabItem("Tab 3", controls="tab-3-custom"),
    # Custom styling for active tabs
    active_items_cls="text-blue-600 hover:text-blue-800 dark:text-blue-500 dark:hover:text-blue-400 border-blue-600 dark:border-blue-500",
    # Custom styling for inactive tabs
    inactive_items_cls="text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-300 border-transparent hover:border-gray-300 dark:border-transparent"
)

# Content panels with custom background
content = Div(
    Div(P("Content for Tab 1"), id="tab-1-custom", cls="p-4 bg-blue-50 dark:bg-gray-800 rounded-lg"),
    Div(P("Content for Tab 2"), id="tab-2-custom", cls="hidden p-4 bg-blue-50 dark:bg-gray-800 rounded-lg"),
    Div(P("Content for Tab 3"), id="tab-3-custom", cls="hidden p-4 bg-blue-50 dark:bg-gray-800 rounded-lg")
)

Div(custom_tabs, content)""",
            id="custom-styled-tabs"
        ),
        
        Br(),
        
        H3("Adding Additional Classes", link=True, cls="mb-3"),
        P("Add additional classes to the tab container using the ", Code("cls"), " parameter:"),
        
        component_showcase(
            Div(
                TabContainer(
                    TabItem("Files", controls="files-tab"),
                    TabItem("Images", controls="images-tab"),
                    TabItem("Videos", controls="videos-tab"),
                    cls="border rounded-t-lg p-2 bg-gray-50 dark:bg-gray-700"
                ),
                Div(
                    Div(P("Files content here..."), id="files-tab", cls="p-4 border border-t-0 rounded-b-lg"),
                    Div(P("Images content here..."), id="images-tab", cls="hidden p-4 border border-t-0 rounded-b-lg"),
                    Div(P("Videos content here..."), id="videos-tab", cls="hidden p-4 border border-t-0 rounded-b-lg")
                )
            ),
            code="""from fastbite.all import TabContainer, TabItem

# Tabs with additional styling classes
styled_tabs = TabContainer(
    TabItem("Files", controls="files-tab"),
    TabItem("Images", controls="images-tab"),
    TabItem("Videos", controls="videos-tab"),
    # Additional styling for the tab container
    cls="border rounded-t-lg p-2 bg-gray-50 dark:bg-gray-700"
)

# Content panels with border styling
content = Div(
    Div(P("Files content here..."), id="files-tab", cls="p-4 border border-t-0 rounded-b-lg"),
    Div(P("Images content here..."), id="images-tab", cls="hidden p-4 border border-t-0 rounded-b-lg"),
    Div(P("Videos content here..."), id="videos-tab", cls="hidden p-4 border border-t-0 rounded-b-lg")
)

Div(styled_tabs, content)""",
            id="tabs-with-additional-classes"
        ),
        
        Br(),
    )

def _integration_section():
    return Section(
        H2("Integrating Tabs", link=True, cls="mb-4 mt-10"),
        P("Tabs can be integrated with other components to create more complex interfaces."),
        
        H3("Tabs with Cards", link=True, cls="mb-3"),
        P("Combine tabs with card components for a cleaner interface:"),
        
        component_showcase(
            Card(
                Title("Product Information"),
                TabContainer(
                    TabItem("Details", controls="details-tab"),
                    TabItem("Specifications", controls="specs-tab"),
                    TabItem("Reviews", controls="reviews-tab")
                ),
                Div(
                    Div(
                        P("This product is designed for professional use with high-quality materials."),
                        P("Features include durability, ease of use, and premium components."),
                        id="details-tab", 
                        cls="p-4"
                    ),
                    Div(
                        P("Technical Specifications:"),
                        Ul(cls="list-disc pl-5 mt-2")(
                            Li("Dimensions: 10 x 5 x 2 inches"),
                            Li("Weight: 1.5 lbs"),
                            Li("Material: Aircraft-grade aluminum"),
                            Li("Power: 100-240V AC"),
                            Li("Battery life: 10 hours")
                        ),
                        id="specs-tab", 
                        cls="hidden p-4"
                    ),
                    Div(
                        P("Customer Reviews:"),
                        Div(
                            P("\"Excellent product, highly recommended!\" - John D."),
                            P("\"Works as advertised, very satisfied.\" - Sarah M."),
                            P("\"Great value for the price.\" - Mike K."),
                            cls="mt-2"
                        ),
                        id="reviews-tab", 
                        cls="hidden p-4"
                    )
                )
            ),
            code="""from fastbite.all import Card, Title, TabContainer, TabItem

Card(
    Title("Product Information"),
    # Tab navigation
    TabContainer(
        TabItem("Details", controls="details-tab"),
        TabItem("Specifications", controls="specs-tab"),
        TabItem("Reviews", controls="reviews-tab")
    ),
    # Tab content panels
    Div(
        Div(
            P("This product is designed for professional use with high-quality materials."),
            P("Features include durability, ease of use, and premium components."),
            id="details-tab", 
            cls="p-4"
        ),
        Div(
            P("Technical Specifications:"),
            Ul(cls="list-disc pl-5 mt-2")(
                Li("Dimensions: 10 x 5 x 2 inches"),
                Li("Weight: 1.5 lbs"),
                Li("Material: Aircraft-grade aluminum"),
                Li("Power: 100-240V AC"),
                Li("Battery life: 10 hours")
            ),
            id="specs-tab", 
            cls="hidden p-4"
        ),
        Div(
            P("Customer Reviews:"),
            Div(
                P("\"Excellent product, highly recommended!\" - John D."),
                P("\"Works as advertised, very satisfied.\" - Sarah M."),
                P("\"Great value for the price.\" - Mike K."),
                cls="mt-2"
            ),
            id="reviews-tab", 
            cls="hidden p-4"
        )
    )
)""",
            id="tabs-with-cards"
        ),
        
        Br(),
        
        H3("Tabs for Form Organization", link=True, cls="mb-3"),
        P("Use tabs to organize different sections of a form:"),
        
        component_showcase(
            Div(cls="max-w-2xl mx-auto")(
                H3("Registration Form", cls="text-xl font-bold mb-4"),
                TabContainer(
                    TabItem("Personal", controls="personal-info"),
                    TabItem("Contact", controls="contact-info"),
                    TabItem("Preferences", controls="preferences")
                ),
                Div(
                    Div(id="personal-info", cls="p-4 border border-t-0 rounded-b-lg")(
                        Div(cls="mb-3")(
                            Label("First Name", for_="first-name"),
                            Input(id="first-name", placeholder="Enter your first name", required=True)
                        ),
                        Div(cls="mb-3")(
                            Label("Last Name", for_="last-name"),
                            Input(id="last-name", placeholder="Enter your last name", required=True)
                        ),
                        Div(cls="mb-3")(
                            Label("Date of Birth", for_="dob"),
                            Input(id="dob", type="date")
                        )
                    ),
                    Div(id="contact-info", cls="hidden p-4 border border-t-0 rounded-b-lg")(
                        Div(cls="mb-3")(
                            Label("Email", for_="email"),
                            Input(id="email", type="email", placeholder="Enter your email", required=True)
                        ),
                        Div(cls="mb-3")(
                            Label("Phone", for_="phone"),
                            Input(id="phone", type="tel", placeholder="Enter your phone number")
                        ),
                        Div(cls="mb-3")(
                            Label("Address", for_="address"),
                            Textarea(id="address", placeholder="Enter your address", rows=3)
                        )
                    ),
                    Div(id="preferences", cls="hidden p-4 border border-t-0 rounded-b-lg")(
                        Div(cls="mb-3")(
                            Label("Language"),
                            Select()(
                                Option("English"),
                                Option("Spanish"),
                                Option("French"),
                                Option("German")
                            )
                        ),
                        Div(cls="mb-3")(
                            Checkbox(id="newsletter", cls="mr-2"),
                            Label("Subscribe to newsletter", for_="newsletter")
                        ),
                        Div(cls="mb-3")(
                            P("Theme Preference", cls="mb-2"),
                            Radio(id="light-theme", name="theme", value="light", cls="mr-2", checked=True),
                            Label("Light", for_="light-theme", cls="mr-4"),
                            Radio(id="dark-theme", name="theme", value="dark", cls="mr-2"),
                            Label("Dark", for_="dark-theme")
                        )
                    )
                ),
                Div(cls="mt-4")(
                    Button("Submit", variant="primary")
                )
            ),
            code="""from fastbite.all import TabContainer, TabItem, Label, Input, Textarea, Select, Option, Checkbox, Radio, Button

Div(cls="max-w-2xl mx-auto")(
    H3("Registration Form", cls="text-xl font-bold mb-4"),
    # Form tabs
    TabContainer(
        TabItem("Personal", controls="personal-info"),
        TabItem("Contact", controls="contact-info"),
        TabItem("Preferences", controls="preferences")
    ),
    # Form sections in tabs
    Div(
        # Personal information tab
        Div(id="personal-info", cls="p-4 border border-t-0 rounded-b-lg")(
            Div(cls="mb-3")(
                Label("First Name", for_="first-name"),
                Input(id="first-name", placeholder="Enter your first name", required=True)
            ),
            Div(cls="mb-3")(
                Label("Last Name", for_="last-name"),
                Input(id="last-name", placeholder="Enter your last name", required=True)
            ),
            Div(cls="mb-3")(
                Label("Date of Birth", for_="dob"),
                Input(id="dob", type="date")
            )
        ),
        # Contact information tab
        Div(id="contact-info", cls="hidden p-4 border border-t-0 rounded-b-lg")(
            Div(cls="mb-3")(
                Label("Email", for_="email"),
                Input(id="email", type="email", placeholder="Enter your email", required=True)
            ),
            Div(cls="mb-3")(
                Label("Phone", for_="phone"),
                Input(id="phone", type="tel", placeholder="Enter your phone number")
            ),
            Div(cls="mb-3")(
                Label("Address", for_="address"),
                Textarea(id="address", placeholder="Enter your address", rows=3)
            )
        ),
        # Preferences tab
        Div(id="preferences", cls="hidden p-4 border border-t-0 rounded-b-lg")(
            Div(cls="mb-3")(
                Label("Language"),
                Select()(
                    Option("English"),
                    Option("Spanish"),
                    Option("French"),
                    Option("German")
                )
            ),
            Div(cls="mb-3")(
                Checkbox(id="newsletter", cls="mr-2"),
                Label("Subscribe to newsletter", for_="newsletter")
            ),
            Div(cls="mb-3")(
                P("Theme Preference", cls="mb-2"),
                Radio(id="light-theme", name="theme", value="light", cls="mr-2", checked=True),
                Label("Light", for_="light-theme", cls="mr-4"),
                Radio(id="dark-theme", name="theme", value="dark", cls="mr-2"),
                Label("Dark", for_="dark-theme")
            )
        )
    ),
    # Submit button
    Div(cls="mt-4")(
        Button("Submit", variant="primary")
    )
)""",
            id="tabs-for-forms"
        ),
        
        Br()
    )

def tabs_showcase():
    """Page showcasing tabs components"""
    return Container(
        H1("Tabs Components", link=True, cls="mb-8 mt-6"),
        P(
            "Fastbite provides tab components to create tabbed interfaces for organizing content and improving user experience.",
            cls="mb-6 text-lg"
        ),
        
        # Call section functions
        _basic_tabs_section(),
        _customized_tabs_section(),
        _integration_section(),
    )

# Make the showcase available to the app
tabs_components = tabs_showcase() 