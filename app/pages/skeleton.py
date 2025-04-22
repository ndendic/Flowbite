from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import *
from utils import component_showcase

skeleton_components = Div(
    H1("Placeholder Components", link=True),
    
    P("Fastbite provides placeholder components to create loading skeletons, content placeholders, and visual indicators for content that is still loading or unavailable."),
    
    H2("Basic Placeholders", link=True),
    
    H3("Default Dashed Placeholder", link=True),
    P("The ", Code("Placeholder"), " component creates a basic container with dashed borders to indicate loading or empty states:"),

    component_showcase(
        Div(
            Placeholder(
                P("This is a placeholder with dashed border", cls="text-center text-gray-400")
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder

# Basic placeholder with default dashed border style
Placeholder(
    P("This is a placeholder with dashed border", cls="text-center text-gray-400")
)""",
        id="basic-placeholder"
    ),
    
    Br(),
    
    H3("Gray Background Placeholder", link=True),
    P("Use the gray background variant with the ", Code("PlaceholderT.gray"), " enum value:"),

    component_showcase(
        Div(
            Placeholder(
                P("Gray Background Placeholder", cls="text-center text-gray-400"),
                cls=PlaceholderT.gray
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder, PlaceholderT

# Placeholder with gray background
Placeholder(
    P("Gray Background Placeholder", cls="text-center text-gray-400"),
    cls=PlaceholderT.gray
)""",
        id="gray-placeholder"
    ),
    
    Br(),
    
    H2("Empty State Placeholders", link=True),
    
    H3("Simple Empty State", link=True),
    P("Create placeholders for empty states with informative messages and icons:"),

    component_showcase(
        Div(
            Placeholder(
                Div(
                    Icon("lucide:inbox", cls="w-10 h-10 mb-2 text-gray-400"),
                    H3("No items found", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
                    P("Your search didn't return any results", cls="text-gray-500 dark:text-gray-400"),
                    cls="flex flex-col items-center justify-center py-5"
                )
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder, Icon
from fasthtml.common import Div, H3, P

Placeholder(
    Div(
        Icon("lucide:inbox", cls="w-10 h-10 mb-2 text-gray-400"),
        H3("No items found", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
        P("Your search didn't return any results", cls="text-gray-500 dark:text-gray-400"),
        cls="flex flex-col items-center justify-center py-5"
    )
)""",
        id="empty-state"
    ),
    
    Br(),
    
    H3("Actionable Empty State", link=True),
    P("Add actions to empty state placeholders to guide users:"),

    component_showcase(
        Div(
            Placeholder(
                Div(
                    Icon("lucide:file-plus", cls="w-10 h-10 mb-3 text-gray-400"),
                    H3("No documents yet", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
                    P("Get started by creating your first document", cls="mb-4 text-gray-500 dark:text-gray-400"),
                    Button("Create Document", cls=ButtonT.primary),
                    cls="flex flex-col items-center justify-center py-5"
                )
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder, Icon, Button, ButtonT
from fasthtml.common import Div, H3, P

Placeholder(
    Div(
        Icon("lucide:file-plus", cls="w-10 h-10 mb-3 text-gray-400"),
        H3("No documents yet", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
        P("Get started by creating your first document", cls="mb-4 text-gray-500 dark:text-gray-400"),
        Button("Create Document", cls=ButtonT.primary),
        cls="flex flex-col items-center justify-center py-5"
    )
)""",
        id="actionable-empty-state"
    ),
    
    Br(),
    
    H2("Loading State Placeholders", link=True),
    
    H3("Skeleton Loading Cards", link=True),
    P("Create loading skeleton placeholders to indicate content is being loaded:"),

    component_showcase(
        Div(
            Div(
                Placeholder(
                    Div(
                        Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]"),
                        cls="flex flex-col space-y-2.5 animate-pulse"
                    ),
                    cls="p-4 border border-gray-200 rounded shadow"
                ),
                cls="mb-4"
            ),
            Div(
                Placeholder(
                    Div(
                        Div(cls="w-12 h-12 rounded-full bg-gray-200 dark:bg-gray-700"),
                        Div(cls="flex-1 space-y-2 py-1"),
                        Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32"),
                        Div(cls="w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
                        cls="flex items-center space-x-4 animate-pulse"
                    ),
                    cls="p-4 border border-gray-200 rounded shadow"
                )
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder
from fasthtml.common import Div

# Text content skeleton loader
Placeholder(
    Div(
        Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]"),
        cls="flex flex-col space-y-2.5 animate-pulse"  # Animation adds subtle loading effect
    ),
    cls="p-4 border border-gray-200 rounded shadow"
)

# User profile skeleton loader
Placeholder(
    Div(
        Div(cls="w-12 h-12 rounded-full bg-gray-200 dark:bg-gray-700"),
        Div(cls="flex-1 space-y-2 py-1"),
        Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32"),
        Div(cls="w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
        cls="flex items-center space-x-4 animate-pulse"  # Animation adds subtle loading effect
    ),
    cls="p-4 border border-gray-200 rounded shadow"
)""",
        id="skeleton-loading"
    ),
    
    Br(),
    
    H3("Grid Layout Skeleton", link=True),
    P("Create grid layouts with skeleton loading placeholders:"),

    component_showcase(
        Div(
            Placeholder(
                Div(
                    Div(
                        Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
                        cls="col-span-1 animate-pulse"
                    ),
                    Div(
                        Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
                        cls="col-span-1 animate-pulse"
                    ),
                    Div(
                        Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),
                        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
                        cls="col-span-1 animate-pulse"
                    ),
                    cls="grid grid-cols-1 md:grid-cols-3 gap-4"
                ),
                cls="p-4"
            ),
            cls="max-w-4xl"
        ),
        code="""from fastbite.all import Placeholder
from fasthtml.common import Div

Placeholder(
    Div(
        # Item 1
        Div(
            Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),  # Image placeholder
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),  # Title placeholder
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),  # Description placeholder
            cls="col-span-1 animate-pulse"
        ),
        # Item 2
        Div(
            Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
            cls="col-span-1 animate-pulse"
        ),
        # Item 3
        Div(
            Div(cls="h-48 rounded bg-gray-200 dark:bg-gray-700"),
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mt-4 mb-2.5"),
            Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
            cls="col-span-1 animate-pulse"
        ),
        cls="grid grid-cols-1 md:grid-cols-3 gap-4"  # Responsive grid layout
    ),
    cls="p-4"
)""",
        id="grid-skeleton"
    ),
    
    Br(),
    
    H2("Custom Placeholders", link=True),
    
    H3("Custom Styled Placeholders", link=True),
    P("Customize placeholder appearances with different styles:"),

    component_showcase(
        Div(
            Div(
                Placeholder(
                    P("Default dashed border placeholder", cls="text-center text-gray-400"),
                    cls=PlaceholderT.dashed
                ),
                cls="mb-4"
            ),
            Div(
                Placeholder(
                    P("Custom styled placeholder", cls="text-center text-blue-500"),
                    cls="p-4 border-2 border-blue-300 border-dashed rounded-lg dark:border-blue-700 bg-blue-50 dark:bg-blue-950"
                ),
                cls="mb-4"
            ),
            Div(
                Placeholder(
                    P("Solid border placeholder", cls="text-center text-gray-600"),
                    cls="p-4 border-2 border-gray-300 rounded-lg shadow-sm dark:border-gray-600"
                ),
                cls="mb-4"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder, PlaceholderT
from fasthtml.common import P

# Default dashed border placeholder
Placeholder(
    P("Default dashed border placeholder", cls="text-center text-gray-400"),
    cls=PlaceholderT.dashed
)

# Custom styled placeholder with blue theme
Placeholder(
    P("Custom styled placeholder", cls="text-center text-blue-500"),
    cls="p-4 border-2 border-blue-300 border-dashed rounded-lg dark:border-blue-700 bg-blue-50 dark:bg-blue-950"
)

# Solid border placeholder
Placeholder(
    P("Solid border placeholder", cls="text-center text-gray-600"),
    cls="p-4 border-2 border-gray-300 rounded-lg shadow-sm dark:border-gray-600"
)""",
        id="custom-styled-placeholders"
    ),
    
    Br(),
    
    H2("Practical Examples", link=True),
    
    H3("Content Unavailable Placeholder", link=True),
    P("Use placeholders to handle cases where content is unavailable:"),

    component_showcase(
        Div(
            Placeholder(
                Div(
                    Icon("lucide:wifi-off", cls="w-12 h-12 mb-3 text-gray-400"),
                    H3("Content Unavailable", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
                    P("Sorry, we couldn't load this content. Please check your connection and try again.", 
                     cls="mb-4 text-gray-500 dark:text-gray-400 text-center max-w-xs"),
                    Button("Retry", cls=ButtonT.primary + "px-5"),
                    cls="flex flex-col items-center justify-center py-6"
                )
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder, Icon, Button, ButtonT
from fasthtml.common import Div, H3, P

Placeholder(
    Div(
        Icon("lucide:wifi-off", cls="w-12 h-12 mb-3 text-gray-400"),
        H3("Content Unavailable", cls="mb-1 text-lg font-semibold text-gray-900 dark:text-white"),
        P("Sorry, we couldn't load this content. Please check your connection and try again.", 
           cls="mb-4 text-gray-500 dark:text-gray-400 text-center max-w-xs"),
        Button("Retry", cls=ButtonT.primary + "px-5"),
        cls="flex flex-col items-center justify-center py-6"
    )
)""",
        id="unavailable-content"
    ),
    
    Br(),
    
    H3("Comment Section Skeleton", link=True),
    P("Create a skeleton placeholder for a comment section while loading:"),

    component_showcase(
        Div(
            Placeholder(
                Div(
                    Div(
                        Div(cls="flex items-center mt-4 space-x-3"),
                        Div(cls="w-10 h-10 rounded-full bg-gray-200 dark:bg-gray-700"),
                        Div(
                            Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2"),
                            Div(cls="w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700"),
                            cls="flex-1"
                        ),
                        cls="flex items-center space-x-4 animate-pulse",
                    ),
                    Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5 mt-4"),
                    Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[440px] mb-2.5"),
                    Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[460px]"),
                    cls="animate-pulse"
                ),
                cls="p-4 border border-gray-200 rounded shadow"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Placeholder
from fasthtml.common import Div

Placeholder(
    Div(
        # User avatar and name skeleton
        Div(
            Div(cls="flex items-center mt-4 space-x-3"),
            Div(cls="w-10 h-10 rounded-full bg-gray-200 dark:bg-gray-700"),  # Avatar
            Div(
                Div(cls="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2"),  # Username
                Div(cls="w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700"),  # Date
                cls="flex-1"
            ),
            cls="flex items-center space-x-4 animate-pulse",
        ),
        # Comment text skeleton
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5 mt-4"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[440px] mb-2.5"),
        Div(cls="h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[460px]"),
        cls="animate-pulse"
    ),
    cls="p-4 border border-gray-200 rounded shadow"
)""",
        id="comment-skeleton"
    ),
    
    Br(),
    
    H2("API Reference", link=True),
    
    H3("Placeholder Component", link=True),
    P("The complete API reference for the Placeholder component:"),
    
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
                Td("Components", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("Components to put in the placeholder", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("PlaceholderT.dashed", cls="px-4 py-2 border"),
                Td("Classes for the placeholder", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("PlaceholderT Enum", link=True),
    P("Available theme options for placeholders:"),
    
    Table(
        Thead(
            Tr(
                Th("Value", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("dashed", cls="px-4 py-2 border"),
                Td("Dashed border with padding and rounded corners, with dark mode support", cls="px-4 py-2 border")
            ),
            Tr(
                Td("gray", cls="px-4 py-2 border"),
                Td("Gray background with padding, centered content, and rounded corners with dark mode support", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H2("Best Practices", link=True),
    
    P("Follow these guidelines when using placeholder components:"),
    
    Ul(
        Li("Use placeholders to indicate loading states, empty states, or unavailable content"),
        Li("Keep placeholder designs simple and representative of the expected content"),
        Li("Use subtle animations (like pulse) to indicate loading states without being distracting"),
        Li("Ensure placeholders have proper contrast in both light and dark modes"),
        Li("Include helpful messaging to explain why content is missing or what users can do"),
        Li("Match the size and shape of placeholders to the expected content dimensions"),
        Li("For loading states, try to match the layout of the content that will eventually appear"),
        Li("Add appropriate actions when possible to help users resolve empty states"),
        cls="list-disc pl-5 space-y-2 mb-6"
    )
) 