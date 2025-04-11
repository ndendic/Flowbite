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
                    data_tabs_toggle="#basic-tabs",
                ),
                # Tab content
                Ul(
                    Li(P("Profile content goes here..."), id="profile", cls="p-4"),
                    Li(P("Settings content goes here..."), id="settings", cls="hidden p-4"),
                    Li(P("Messages content goes here..."), id="messages", cls="hidden p-4"),
                    id="basic-tabs"
                )
            ),
            code="""from fastbite.all import *

# Create tab navigation
Div(
    TabContainer(
        TabItem("Profile", controls="profile"),
        TabItem("Settings", controls="settings"),
        TabItem("Messages", controls="messages"),
        data_tabs_toggle="#basic-tabs"
    ),
    # Tab content
    Ul(
        Li(P("Profile content goes here..."), id="profile", cls="p-4"),
        Li(P("Settings content goes here..."), id="settings", cls="hidden p-4"),
        Li(P("Messages content goes here..."), id="messages", cls="hidden p-4"),
        id="basic-tabs"
    )
)""",
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
                    data_tabs_toggle="#rich-content-tabs"
                ),
                Ul(
                    Li(
                        H3("Featured Products", cls="mb-3"),
                        Ul(cls="list-disc pl-5")(
                            Li("Product A"),
                            Li("Product B"),
                            Li("Product C")
                        ),
                        id="products-panel", 
                        cls="p-4"
                    ),
                    Li(
                        H3("Our Services", cls="mb-3"),
                        Ul(cls="list-disc pl-5")(
                            Li("Consulting"),
                            Li("Development"),
                            Li("Support")
                        ),
                        id="services-panel", 
                        cls="hidden p-4"
                    ),
                    Li(
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
                ),
                id="rich-content-tabs"
            ),
            code="""from fastbite.all import *

# Create tab navigation
Div(
    TabContainer(
        TabItem("Products", controls="products-panel"),
        TabItem("Services", controls="services-panel"),
        TabItem("Support", controls="support-panel"),
        data_tabs_toggle="#rich-content-tabs"
    ),
    Ul(
        Li(
            H3("Featured Products", cls="mb-3"),
            Ul(cls="list-disc pl-5")(
                Li("Product A"),
                Li("Product B"),
                Li("Product C")
            ),
            id="products-panel", 
            cls="p-4"
        ),
        Li(
            H3("Our Services", cls="mb-3"),
            Ul(cls="list-disc pl-5")(
                Li("Consulting"),
                Li("Development"),
                Li("Support")
            ),
            id="services-panel", 
            cls="hidden p-4"
        ),
        Li(
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
    ),
    id="rich-content-tabs"
)""",
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
                    data_tabs_toggle="#custom-styled-tabs",
                    active_items_cls="text-lime-600 hover:text-lime-800 dark:text-lime-500 dark:hover:text-lime-400 border-lime-600 dark:border-lime-500",
                    inactive_items_cls="text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-300 border-transparent hover:border-gray-300 dark:border-transparent"
                ),
                # Tab content
                Ul(
                    Li(P("Content for Tab 1", cls=TextT.text_3xl+"text-white"), id="tab-1-custom", cls="p-4"),
                    Li(P("Content for Tab 2", cls=TextT.text_3xl+"text-white"), id="tab-2-custom", cls="p-4 hidden"),
                    Li(P("Content for Tab 3", cls=TextT.text_3xl+"text-white"), id="tab-3-custom", cls="p-4 hidden"),
                    id="custom-styled-tabs",
                    cls="mt-2 rounded-lg"+BgColor.grad_lime
                ),
            ),
            code="""from fastbite.all import *

# Custom color styling for tabs
Div(
    # Custom styled tabs
    TabContainer(
        TabItem("Tab 1", controls="tab-1-custom"),
        TabItem("Tab 2", controls="tab-2-custom"),
        TabItem("Tab 3", controls="tab-3-custom"),
        data_tabs_toggle="#custom-styled-tabs",
        active_items_cls="text-green-600 hover:text-green-800 dark:text-green-500 dark:hover:text-green-400 border-green-600 dark:border-green-500",
        inactive_items_cls="text-gray-500 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-300 border-transparent hover:border-gray-300 dark:border-transparent"
    ),
    # Tab content
    Ul(
        Li(P("Content for Tab 1", cls=TextT.text_3xl+"text-white"), id="tab-1-custom", cls="p-4"),
        Li(P("Content for Tab 2", cls=TextT.text_3xl+"text-white"), id="tab-2-custom", cls="p-4 hidden"),
        Li(P("Content for Tab 3", cls=TextT.text_3xl+"text-white"), id="tab-3-custom", cls="p-4 hidden"),
        id="custom-styled-tabs",
        cls="mt-2 bg-primary-500 dark:bg-primary-500 rounded-lg"
    ),
)""",
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
                    data_tabs_toggle="#tabs-with-additional-classes",
                    cls=TabContainerT.rounded
                ),
                Ul(
                    Li(P("Files content here..."), id="files-tab", cls="p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
                    Li(P("Images content here..."), id="images-tab", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
                    Li(P("Videos content here..."), id="videos-tab", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
                    id="tabs-with-additional-classes"
                )
            ),
            code="""from fastbite.all import *

# Tabs with additional styling classes
Div(
    TabContainer(
        TabItem("Files", controls="files-tab"),
        TabItem("Images", controls="images-tab"),
        TabItem("Videos", controls="videos-tab"),
        data_tabs_toggle="#tabs-with-additional-classes",
        cls=TabContainerT.rounded
    ),
    Ul(
        Li(P("Files content here..."), id="files-tab", cls="p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
        Li(P("Images content here..."), id="images-tab", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
        Li(P("Videos content here..."), id="videos-tab", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-700"),
        id="tabs-with-additional-classes"
    )
)""",
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
                    TabItem("Reviews", controls="reviews-tab"),
                    data_tabs_toggle="#tabs-with-cards"
                ),
                Ul(
                    Li(
                        P("This product is designed for professional use with high-quality materials."),
                        P("Features include durability, ease of use, and premium components."),
                        id="details-tab", 
                        cls="p-4"
                    ),
                    Li(
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
                    Li(
                        P("Customer Reviews:"),
                        Div(
                            P("\"Excellent product, highly recommended!\" - John D."),
                            P("\"Works as advertised, very satisfied.\" - Sarah M."),
                            P("\"Great value for the price.\" - Mike K."),
                            cls="mt-2"
                        ),
                        id="reviews-tab", 
                        cls="hidden p-4"
                    ),
                    id="tabs-with-cards"
                ),
                cls=CardT.hover
            ),
            code="""from fastbite.all import *

Card(
    Title("Product Information"),
    TabContainer(
        TabItem("Details", controls="details-tab"),
        TabItem("Specifications", controls="specs-tab"),
        TabItem("Reviews", controls="reviews-tab"),
        data_tabs_toggle="#tabs-with-cards"
    ),
    Ul(
        Li(
            P("This product is designed for professional use with high-quality materials."),
            P("Features include durability, ease of use, and premium components."),
            id="details-tab", 
            cls="p-4"
        ),
        Li(
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
        Li(
            P("Customer Reviews:"),
            Div(
                P("\"Excellent product, highly recommended!\" - John D."),
                P("\"Works as advertised, very satisfied.\" - Sarah M."),
                P("\"Great value for the price.\" - Mike K."),
                cls="mt-2"
            ),
            id="reviews-tab", 
            cls="hidden p-4"
        ),
        id="tabs-with-cards"
    ),
    cls=CardT.hover
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
                    TabItem("Preferences", controls="preferences"),
                    data_tabs_toggle="#tabs-for-forms",
                    cls=TabContainerT.rounded
                ),
                Ul(
                    Li(id="personal-info", cls="p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
                        Div(cls="mb-3")(
                            Input(label="First Name", id="first-name", placeholder="Enter your first name", required=True)
                        ),
                        Div(cls="mb-3")(
                            Input(label="Last Name", id="last-name", placeholder="Enter your last name", required=True)
                        ),
                        Div(cls="mb-3")(
                            Input(label="Date of Birth", id="dob", type="date")
                        )
                    ),
                    Li(id="contact-info", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
                        Div(cls="mb-3")(
                            Input(label="Email", id="email", type="email", placeholder="Enter your email", required=True)
                        ),
                        Div(cls="mb-3")(
                            Input(label="Phone", id="phone", type="tel", placeholder="Enter your phone number")
                        ),
                        Div(cls="mb-3")(
                            TextArea(label="Address", id="address", placeholder="Enter your address", rows=3)
                        )
                    ),
                    Li(id="preferences", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
                        Div(cls="mb-3")(
                            Select(*Options("English","Spanish","French","German"),label="Language",id="language",placeholder="Select",required=True)
                        ),                        
                        Div(cls="mb-3")(FormLabel("Theme Preference"),
                            Radio(label="Light", id="light-theme", name="theme", value="light", cls="mr-2", checked=True),
                            Radio(label="Dark", id="dark-theme", name="theme", value="dark", cls="mr-2"),
                        ),
                        Div(cls="mb-3")(
                            Checkbox(label="Subscribe to newsletter", id="newsletter", cls="mr-2"),
                        )
                    ),
                    id="tabs-for-forms"
                ),
                Div(cls="mt-4")(
                    Button("Submit", variant="primary")
                )
            ),
            code="""from fastbite.all import *

Div(cls="max-w-2xl mx-auto")(
    H3("Registration Form", cls="text-xl font-bold mb-4"),
    TabContainer(
        TabItem("Personal", controls="personal-info"),
        TabItem("Contact", controls="contact-info"),
        TabItem("Preferences", controls="preferences"),
        data_tabs_toggle="#tabs-for-forms",
        cls=TabContainerT.rounded
    ),
    Ul(
        Li(id="personal-info", cls="p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
            Div(cls="mb-3")(
                Input(label="First Name", id="first-name", placeholder="Enter your first name", required=True)
            ),
            Div(cls="mb-3")(
                Input(label="Last Name", id="last-name", placeholder="Enter your last name", required=True)
            ),
            Div(cls="mb-3")(
                Input(label="Date of Birth", id="dob", type="date")
            )
        ),
        Li(id="contact-info", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
            Div(cls="mb-3")(
                Input(label="Email", id="email", type="email", placeholder="Enter your email", required=True)
            ),
            Div(cls="mb-3")(
                Input(label="Phone", id="phone", type="tel", placeholder="Enter your phone number")
            ),
            Div(cls="mb-3")(
                TextArea(label="Address", id="address", placeholder="Enter your address", rows=3)
            )
        ),
        Li(id="preferences", cls="hidden p-4 border border-t-0 rounded-b-lg border-gray-50 dark:border-gray-600")(
            Div(cls="mb-3")(
                Select(*Options("English","Spanish","French","German"),label="Language",id="language",placeholder="Select",required=True)
            ),                        
            Div(cls="mb-3")(FormLabel("Theme Preference"),
                Radio(label="Light", id="light-theme", name="theme", value="light", cls="mr-2", checked=True),
                Radio(label="Dark", id="dark-theme", name="theme", value="dark", cls="mr-2"),
            ),
            Div(cls="mb-3")(
                Checkbox(label="Subscribe to newsletter", id="newsletter", cls="mr-2"),
            )
        ),
        id="tabs-for-forms"
    ),
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