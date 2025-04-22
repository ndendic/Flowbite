from fasthtml.common import Div, P, Html, Head, Body, Br, Code
from fastbite.all import *
from utils import component_showcase

def badge_showcase():
    """Page showcasing Badge components"""
    
    return Container(
        H1("Badge Components", link=True, cls="mb-8 mt-6"),
        
        P("This showcase provides examples of badge components available in the Fastbite library. Badges are used for labeling, categorization, and highlighting small pieces of information.", cls="mb-6 text-lg"),
        
        # Badge Components section
        H2("Badge Components", link=True, cls="mb-4 mt-10"),
        badge_section(),
    )

def badge_section():
    """Create the badge components showcase section"""
    
    return Div(
        # Default Badges
        H3("Default Badges", link=True, cls="mb-3"),
        P("The ", Code("Badge"), " component creates small text labels with background colors. Use the ", Code("BadgeT"), " enum to apply different styles:"),
        
        component_showcase(
            Div(
                Badge("Default", cls=BadgeT.default),
                Badge("Dark", cls=BadgeT.dark),
                Badge("Red", cls=BadgeT.red),
                Badge("Yellow", cls=BadgeT.yellow),
                Badge("Green", cls=BadgeT.green),
                Badge("Blue", cls=BadgeT.blue),
                Badge("Indigo", cls=BadgeT.indigo),
                Badge("Purple", cls=BadgeT.purple),
                Badge("Pink", cls=BadgeT.pink),
                cls="space-x-2"
            ),
            code="""# Import at the top of your file
from fastbite.all import Badge, BadgeT

# Default badges
Badge("Default", cls=BadgeT.default)
Badge("Dark", cls=BadgeT.dark)
Badge("Red", cls=BadgeT.red)
Badge("Yellow", cls=BadgeT.yellow)
Badge("Green", cls=BadgeT.green)
Badge("Blue", cls=BadgeT.blue)
Badge("Indigo", cls=BadgeT.indigo)
Badge("Purple", cls=BadgeT.purple)
Badge("Pink", cls=BadgeT.pink)""",
            id="default-badges"
        ),
        
        Br(),
        
        # Large Badges
        H3("Large Badges", link=True, cls="mb-3"),
        P("For larger badges, use the ", Code("BadgeT"), " enum with ", Code("_lg"), " suffix:"),
        
        component_showcase(
            Div(
                Badge("Default", cls=BadgeT.default_lg),
                Badge("Dark", cls=BadgeT.dark_lg),
                Badge("Red", cls=BadgeT.red_lg),
                Badge("Yellow", cls=BadgeT.yellow_lg),
                Badge("Green", cls=BadgeT.green_lg),
                Badge("Blue", cls=BadgeT.blue_lg),
                Badge("Indigo", cls=BadgeT.indigo_lg),
                Badge("Purple", cls=BadgeT.purple_lg),
                Badge("Pink", cls=BadgeT.pink_lg),
                cls="space-x-2"
            ),
            code="""# Large badges
Badge("Default", cls=BadgeT.default_lg)
Badge("Dark", cls=BadgeT.dark_lg)
Badge("Red", cls=BadgeT.red_lg)
Badge("Yellow", cls=BadgeT.yellow_lg)
Badge("Green", cls=BadgeT.green_lg)
Badge("Blue", cls=BadgeT.blue_lg)
Badge("Indigo", cls=BadgeT.indigo_lg)
Badge("Purple", cls=BadgeT.purple_lg)
Badge("Pink", cls=BadgeT.pink_lg)""",
            id="large-badges"
        ),
        
        Br(),
        
        # Pill Badges
        H3("Pill Badges", link=True, cls="mb-3"),
        P("For rounded pill-shaped badges, use the ", Code("BadgeT"), " enum with ", Code("_pill"), " suffix:"),
        
        component_showcase(
            Div(
                Badge("Default", cls=BadgeT.default_pill),
                Badge("Dark", cls=BadgeT.dark_pill),
                Badge("Red", cls=BadgeT.red_pill),
                Badge("Yellow", cls=BadgeT.yellow_pill),
                Badge("Green", cls=BadgeT.green_pill),
                Badge("Blue", cls=BadgeT.blue_pill),
                Badge("Indigo", cls=BadgeT.indigo_pill),
                Badge("Purple", cls=BadgeT.purple_pill),
                Badge("Pink", cls=BadgeT.pink_pill),
                cls="space-x-2"
            ),
            code="""# Pill-shaped badges
Badge("Default", cls=BadgeT.default_pill)
Badge("Dark", cls=BadgeT.dark_pill)
Badge("Red", cls=BadgeT.red_pill)
Badge("Yellow", cls=BadgeT.yellow_pill)
Badge("Green", cls=BadgeT.green_pill)
Badge("Blue", cls=BadgeT.blue_pill)
Badge("Indigo", cls=BadgeT.indigo_pill)
Badge("Purple", cls=BadgeT.purple_pill)
Badge("Pink", cls=BadgeT.pink_pill)""",
            id="pill-badges"
        ),
        
        Br(),
        
        # Outline Badges
        H3("Outline Badges", link=True, cls="mb-3"),
        P("For badges with outlines, use the ", Code("BadgeT"), " enum with ", Code("_outline"), " suffix:"),
        
        component_showcase(
            Div(
                Badge("Default", cls=BadgeT.default_outline),
                Badge("Dark", cls=BadgeT.dark_outline),
                Badge("Red", cls=BadgeT.red_outline),
                Badge("Yellow", cls=BadgeT.yellow_outline),
                Badge("Green", cls=BadgeT.green_outline),
                Badge("Blue", cls=BadgeT.blue_outline),
                Badge("Indigo", cls=BadgeT.indigo_outline),
                Badge("Purple", cls=BadgeT.purple_outline),
                Badge("Pink", cls=BadgeT.pink_outline),
                cls="space-x-2"
            ),
            code="""# Outline badges
Badge("Default", cls=BadgeT.default_outline)
Badge("Dark", cls=BadgeT.dark_outline)
Badge("Red", cls=BadgeT.red_outline)
Badge("Yellow", cls=BadgeT.yellow_outline)
Badge("Green", cls=BadgeT.green_outline)
Badge("Blue", cls=BadgeT.blue_outline)
Badge("Indigo", cls=BadgeT.indigo_outline)
Badge("Purple", cls=BadgeT.purple_outline)
Badge("Pink", cls=BadgeT.pink_outline)""",
            id="outline-badges"
        ),
        
        Br(),
        
        # Badges with Icons
        H3("Badges with Icons", link=True, cls="mb-3"),
        P("You can add icons to badges using the ", Code("icon"), " parameter:"),
        
        component_showcase(
            Div(
                Badge("Default",icon="lucide:home", cls=BadgeT.default),
                Badge("Dark",icon="lucide:home", cls=BadgeT.dark),
                Badge("Red",icon="lucide:home", cls=BadgeT.red),
                Badge("Yellow",icon="lucide:home", cls=BadgeT.yellow),
                Badge("Green",icon="lucide:home", cls=BadgeT.green),
                Badge("Blue",icon="lucide:home", cls=BadgeT.blue),
                Badge("Indigo",icon="lucide:home", cls=BadgeT.indigo),
                Badge("Purple",icon="lucide:home", cls=BadgeT.purple),
                Badge("Pink",icon="lucide:home", cls=BadgeT.pink),
                cls="space-x-2"
            ),
            code="""# Badges with icons
Badge("Default",icon="lucide:home", cls=BadgeT.default)
Badge("Dark",icon="lucide:home", cls=BadgeT.dark)
Badge("Red",icon="lucide:home", cls=BadgeT.red)
Badge("Yellow",icon="lucide:home", cls=BadgeT.yellow)
Badge("Green",icon="lucide:home", cls=BadgeT.green)
Badge("Blue",icon="lucide:home", cls=BadgeT.blue)
Badge("Indigo",icon="lucide:home", cls=BadgeT.indigo)
Badge("Purple",icon="lucide:home", cls=BadgeT.purple)
Badge("Pink",icon="lucide:home", cls=BadgeT.pink)""",
            id="icon-badges"
        ),
        
        Br(),
        
        # Icon-Only Badges
        H3("Icon-Only Badges", link=True, cls="mb-3"),
        P("For badges with only icons, use the ", Code("IconBadge"), " component:"),
        
        component_showcase(
            Div(
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
                cls="space-x-2"
            ),
            code="""# Icon-only badges with various background colors
IconBadge(icon="home", cls=BackgroundT.primary)
IconBadge(icon="home", cls=BackgroundT.secondary)
IconBadge(icon="home", cls=BackgroundT.success)
IconBadge(icon="home", cls=BackgroundT.warning)
IconBadge(icon="home", cls=BackgroundT.error)
IconBadge(icon="home", cls=BackgroundT.info)

# Icon-only badges with gradient backgrounds
IconBadge(icon="home", cls=BackgroundT.grad_primary)
IconBadge(icon="home", cls=BackgroundT.grad_secondary)
IconBadge(icon="home", cls=BackgroundT.grad_success)
IconBadge(icon="home", cls=BackgroundT.grad_warning)
IconBadge(icon="home", cls=BackgroundT.grad_error)
IconBadge(icon="home", cls=BackgroundT.grad_info)""",
            id="icon-only-badges"
        ),
        
        Br(),
        
        # Usage Examples
        H3("Usage Examples", link=True, cls="mb-3"),
        P("Badges can be used in different contexts such as labels, counters, or status indicators:"),
        
        component_showcase(
            Div(
                Div(
                    H5("Product Status", cls="mb-2"),
                    Div(
                        P("Laptop", cls="mr-2"),
                        Badge("In Stock", cls=BadgeT.green_pill),
                        cls="flex items-center"
                    ),
                    Div(
                        P("Phone", cls="mr-2"),
                        Badge("Low Stock", cls=BadgeT.yellow_pill),
                        cls="flex items-center mt-2"
                    ),
                    Div(
                        P("Headphones", cls="mr-2"),
                        Badge("Out of Stock", cls=BadgeT.red_pill),
                        cls="flex items-center mt-2"
                    ),
                    cls="p-4 border rounded-md mb-4"
                ),
                
                Div(
                    H5("Feature Status", cls="mb-2"),
                    Div(
                        P("Notifications", cls="mr-2"),
                        IconBadge(icon="bell", cls=BackgroundT.primary),
                        Badge("3", cls=BadgeT.red_pill),
                        cls="flex items-center"
                    ),
                    Div(
                        P("Messages", cls="mr-2"),
                        IconBadge(icon="mail", cls=BackgroundT.secondary),
                        Badge("New", cls=BadgeT.blue_pill),
                        cls="flex items-center mt-2"
                    ),
                    cls="p-4 border rounded-md"
                )
            ),
            code="""# Product status example
Div(
    H5("Product Status", cls="mb-2"),
    Div(
        P("Laptop", cls="mr-2"),
        Badge("In Stock", cls=BadgeT.green_pill),
        cls="flex items-center"
    ),
    Div(
        P("Phone", cls="mr-2"),
        Badge("Low Stock", cls=BadgeT.yellow_pill),
        cls="flex items-center mt-2"
    ),
    Div(
        P("Headphones", cls="mr-2"),
        Badge("Out of Stock", cls=BadgeT.red_pill),
        cls="flex items-center mt-2"
    ),
    cls="p-4 border rounded-md mb-4"
)

# Feature status example with notification counters
Div(
    H5("Feature Status", cls="mb-2"),
    Div(
        P("Notifications", cls="mr-2"),
        IconBadge(icon="bell", cls=BackgroundT.primary),
        Badge("3", cls=BadgeT.red_pill),
        cls="flex items-center"
    ),
    Div(
        P("Messages", cls="mr-2"),
        IconBadge(icon="mail", cls=BackgroundT.secondary),
        Badge("New", cls=BadgeT.blue_pill),
        cls="flex items-center mt-2"
    ),
    cls="p-4 border rounded-md"
)""",
            id="usage-examples"
        ),
        
        Br(),
        
        # API Reference
        H3("Badge API", link=True, cls="mb-3"),
        P("Here's a reference for the Badge component API:"),
        
        component_showcase(
            Div(
                P(Strong("Badge Component"), " - Creates a styled text label"),
                P(Code("*c"), " - Badge content (text or other elements)"),
                P(Code("icon"), " - Optional icon name to include before text"),
                P(Code("cls"), " - Style classes, usually from BadgeT enum"),
                P(Code("**kwargs"), " - Additional HTML attributes"),
                
                P(Strong("IconBadge Component"), " - Creates an icon-only badge", cls="mt-4"),
                P(Code("icon"), " - Icon name to display"),
                P(Code("h"), " - Height of the icon (default: '2.5')"),
                P(Code("w"), " - Width of the icon (default: '2.5')"),
                P(Code("cls"), " - Style classes for the badge"),
                P(Code("icon_cls"), " - Style classes for the icon"),
                P(Code("**kwargs"), " - Additional HTML attributes"),
                
                P(Strong("BadgeT Enum"), " - Style classes for badges", cls="mt-4"),
                P("Default styles: ", Code("default"), ", ", Code("dark"), ", ", Code("red"), ", etc."),
                P("Large styles: ", Code("default_lg"), ", ", Code("dark_lg"), ", ", Code("red_lg"), ", etc."),
                P("Outline styles: ", Code("default_outline"), ", ", Code("dark_outline"), ", ", Code("red_outline"), ", etc."),
                P("Pill styles: ", Code("default_pill"), ", ", Code("dark_pill"), ", ", Code("red_pill"), ", etc."),
            ),
            code="""# Badge component syntax
Badge("Text",icon="lucide:icon-name", cls=BadgeT.variant)

# IconBadge component syntax
IconBadge(icon="icon-name", h="2.5", w="2.5", cls=BackgroundT.variant, icon_cls="additional-icon-classes")

# Available BadgeT variants
BadgeT.default           # Default badge style
BadgeT.dark              # Dark badge style
BadgeT.red               # Red badge style
BadgeT.green             # Green badge style
BadgeT.blue              # Blue badge style
BadgeT.yellow            # Yellow badge style
BadgeT.indigo            # Indigo badge style
BadgeT.purple            # Purple badge style
BadgeT.pink              # Pink badge style

# Size variants
BadgeT.default_lg        # Large badge
BadgeT.default_outline   # Outlined badge
BadgeT.default_pill      # Pill-shaped badge

# These can be combined with colors
# e.g., BadgeT.red_lg, BadgeT.blue_pill, BadgeT.green_outline""",
            id="api-reference"
        )
    )

# Make the showcase available to the app
badge_components = badge_showcase() 