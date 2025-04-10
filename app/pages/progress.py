from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import *
from utils import component_showcase

progress_components = Div(
    H1("Progress Components", link=True),
    
    P("Fastbite provides customizable progress bars to visualize completion status, loading states, and data metrics."),
    
    H2("Basic Progress Bars", link=True),
    
    H3("Default Progress Bar", link=True),
    P("The ", Code("Progress"), " component creates a simple progress bar with a percentage value:"),

    component_showcase(
        Div(
            Progress(label="Default Progress", value="45"),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress

# Basic progress bar with label
Progress(
    label="Default Progress", 
    value="45"  # Value as percentage (0-100)
)""",
        id="basic-progress"
    ),
    
    Br(),
    
    H3("Progress Sizes", link=True),
    P("Progress bars come in different sizes using the ", Code("size"), " parameter:"),

    component_showcase(
        Div(
            Div(
                P("Small Size (sm)", cls="mb-1"),
                Progress(value="45", size="sm"),
                cls="mb-4"
            ),
            Div(
                P("Medium Size (md) - Default", cls="mb-1"),
                Progress(value="65", size="md"),
                cls="mb-4"
            ),
            Div(
                P("Large Size (lg)", cls="mb-1"),
                Progress(value="85", size="lg"),
                cls="mb-4"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress

# Small progress bar
Progress(
    label="", 
    value="45",
    size="sm"  # Small size
)

# Medium progress bar (default)
Progress(
    label="", 
    value="65",
    size="md"  # Medium size
)

# Large progress bar
Progress(
    label="", 
    value="85",
    size="lg"  # Large size
)""",
        id="progress-sizes"
    ),
    
    Br(),
    
    H2("Progress Bar Colors", link=True),
    
    H3("Color Variants", link=True),
    P("Change the progress bar color using the ", Code("progress_cls"), " parameter with ", Code("ProgressT"), " enum values:"),

    component_showcase(
        Div(
            Div(
                P("Primary", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_primary),
                cls="mb-3"
            ),
            Div(
                P("Dark", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_dark),
                cls="mb-3"
            ),
            Div(
                P("Blue", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_blue),
                cls="mb-3"
            ),
            Div(
                P("Red", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_red),
                cls="mb-3"
            ),
            Div(
                P("Green", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_green),
                cls="mb-3"
            ),
            Div(
                P("Yellow", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_yellow),
                cls="mb-3"
            ),
            Div(
                P("Purple", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_purple),
                cls="mb-3"
            ),
            Div(
                P("Pink", cls="mb-1"),
                Progress(value="75", progress_cls=ProgressT.progress_pink),
                cls="mb-3"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress, ProgressT

# Primary color (default)
Progress(value="75", progress_cls=ProgressT.progress_primary)

# Dark color
Progress(value="75", progress_cls=ProgressT.progress_dark)

# Blue color
Progress(value="75", progress_cls=ProgressT.progress_blue)

# Red color
Progress(value="75", progress_cls=ProgressT.progress_red)

# Green color
Progress(value="75", progress_cls=ProgressT.progress_green)

# Yellow color
Progress(value="75", progress_cls=ProgressT.progress_yellow)

# Purple color
Progress(value="75", progress_cls=ProgressT.progress_purple)

# Pink color
Progress(value="75", progress_cls=ProgressT.progress_pink)""",
        id="progress-colors"
    ),
    
    Br(),
    
    H3("Background Colors", link=True),
    P("Change the background color of the progress track using the ", Code("bg_cls"), " parameter:"),

    component_showcase(
        Div(
            Div(
                P("Default Background", cls="mb-1"),
                Progress(value="60", bg_cls=ProgressT.bg_default),
                cls="mb-3"
            ),
            Div(
                P("Primary Background", cls="mb-1"),
                Progress(value="60", progress_cls=ProgressT.progress_dark, bg_cls=ProgressT.bg_primary),
                cls="mb-3"
            ),
            Div(
                P("Dark Background", cls="mb-1"),
                Progress(value="60", progress_cls=ProgressT.progress_primary, bg_cls=ProgressT.bg_dark),
                cls="mb-3"
            ),
            Div(
                P("Blue Background", cls="mb-1"),
                Progress(value="60", progress_cls=ProgressT.progress_yellow, bg_cls=ProgressT.bg_blue),
                cls="mb-3"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress, ProgressT

# Default background
Progress(
    value="60", 
    bg_cls=ProgressT.bg_default  # Gray background
)

# Primary background with dark progress
Progress(
    value="60", 
    progress_cls=ProgressT.progress_dark,
    bg_cls=ProgressT.bg_primary  # Primary color background
)

# Dark background with primary progress
Progress(
    value="60", 
    progress_cls=ProgressT.progress_primary,
    bg_cls=ProgressT.bg_dark  # Dark background
)

# Blue background with yellow progress for contrast
Progress(
    value="60", 
    progress_cls=ProgressT.progress_yellow,
    bg_cls=ProgressT.bg_blue  # Blue background
)""",
        id="progress-backgrounds"
    ),
    
    Br(),
    
    H2("Label Customization", link=True),
    
    H3("Basic Labels", link=True),
    P("Customize the label for progress bars with the ", Code("label"), " and ", Code("label_cls"), " parameters:"),

    component_showcase(
        Div(
            Div(
                Progress(
                    label="Downloading... 45%", 
                    value="45"
                ),
                cls="mb-3"
            ),
            Div(
                Progress(
                    label="Loading profile", 
                    value="75",
                    label_cls=TextT.lg
                ),
                cls="mb-3"
            ),
            Div(
                Progress(
                    label=Span("Processing ", Strong("critical"), " task"),
                    value="30",
                    progress_cls=ProgressT.progress_red
                ),
                cls="mb-3"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress, ProgressT, TextT
from fasthtml.common import Span, Strong

# Simple text label
Progress(
    label="Downloading... 45%", 
    value="45"
)

# Large text label
Progress(
    label="Loading profile", 
    value="75",
    label_cls=TextT.lg  # Larger text
)

# Component as label
Progress(
    label=Span("Processing ", Strong("critical"), " task"),
    value="30",
    progress_cls=ProgressT.progress_red
)""",
        id="progress-labels"
    ),
    
    Br(),
    
    H3("Label with Percentage Display", link=True),
    P("Add dynamic information to show both a label and the current percentage:"),

    component_showcase(
        Div(
            Div(
                Progress(
                    label=DivFullySpaced(
                        Span("Uploading files"),
                        Span("67%")
                    ),
                    value="67"
                ),
                cls="mb-3"
            ),
            Div(
                Progress(
                    label=DivFullySpaced(
                        Span("Storage usage"),
                        Span("85%", cls="float-right text-red-500")
                    ),
                    value="85",
                    progress_cls=ProgressT.progress_red
                ),
                cls="mb-3"
            ),
            Div(
                Progress("85%",
                    value="85",
                    size="lg",
                    label="Making some progress..",
                    progress_cls=ProgressT.progress_red
                ),
                cls="mb-3"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress, ProgressT
from fasthtml.common import Div, Span

# Label with percentage display
Progress(
    label=DivFullySpaced(
        Span("Uploading files"),
        Span("67%", cls="float-right")
    ),
    value="67"
)

# Storage usage with warning color
Progress(
    label=DivFullySpaced(
        Span("Storage usage"),
        Span("85%", cls="float-right text-red-500")
    ),
    value="85",
    progress_cls=ProgressT.progress_red
)""",
        id="progress-percentage-labels"
    ),
    
    Br(),
    
    H2("Complex Usage Examples", link=True),
    
    H3("Progress with Multiple Steps", link=True),
    P("Create a multi-step process indicator using multiple progress bars:"),

    component_showcase(
        Div(
            Div(
                H4("Form Completion", cls="mb-2"),
                Div(
                    Div(
                        P("Step 1: Account Details", cls="mb-1"),
                        Progress(value="100", size="sm"),
                        cls="mb-2"
                    ),
                    Div(
                        P("Step 2: Personal Information", cls="mb-1"),
                        Progress(value="100", size="sm"),
                        cls="mb-2"
                    ),
                    Div(
                        P("Step 3: Preferences", cls="mb-1"),
                        Progress(value="65", size="sm"),
                        cls="mb-2"
                    ),
                    Div(
                        P("Step 4: Confirmation", cls="mb-1"),
                        Progress(value="0", size="sm"),
                        cls="mb-2"
                    ),
                ),
                P("Overall Progress:", cls="mt-4 mb-1"),
                Progress(value="66", progress_cls=ProgressT.progress_green),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Progress, ProgressT
from fasthtml.common import Div, H4, P

Div(
    H4("Form Completion", cls="mb-2"),
    Div(
        # Step 1 - Completed
        Div(
            P("Step 1: Account Details", cls="mb-1"),
            Progress(value="100", size="sm"),
            cls="mb-2"
        ),
        # Step 2 - Completed
        Div(
            P("Step 2: Personal Information", cls="mb-1"),
            Progress(value="100", size="sm"),
            cls="mb-2"
        ),
        # Step 3 - In progress
        Div(
            P("Step 3: Preferences", cls="mb-1"),
            Progress(value="65", size="sm"),
            cls="mb-2"
        ),
        # Step 4 - Not started
        Div(
            P("Step 4: Confirmation", cls="mb-1"),
            Progress(value="0", size="sm"),
            cls="mb-2"
        ),
    ),
    # Overall progress
    P("Overall Progress:", cls="mt-4 mb-1"),
    Progress(value="66", progress_cls=ProgressT.progress_green),
    cls="p-4 border rounded-lg"
)""",
        id="multi-step-progress"
    ),
    
    Br(),
    
    H3("Dashboard Usage Example", link=True),
    P("Use progress bars in dashboard contexts to display metrics:"),

    component_showcase(
        Div(
            Div(
                H4("System Resources", cls="mb-4"),
                Div(
                    Div(
                        Div(
                            P("CPU Usage", cls="mb-1"),
                            Progress(
                                label=Span("78%", cls="float-right"),
                                value="78",
                                progress_cls=ProgressT.progress_blue,
                                size="sm"
                            ),
                            cls="mb-3"
                        ),
                        Div(
                            P("Memory Usage", cls="mb-1"),
                            Progress(
                                label=Span("45%", cls="float-right"),
                                value="45",
                                progress_cls=ProgressT.progress_green,
                                size="sm"
                            ),
                            cls="mb-3"
                        ),
                        cls="w-full md:w-1/2 px-2"
                    ),
                    Div(
                        Div(
                            P("Disk Usage", cls="mb-1"),
                            Progress(
                                label=Span("92%", cls="float-right"),
                                value="92",
                                progress_cls=ProgressT.progress_red,
                                size="sm"
                            ),
                            cls="mb-3"
                        ),
                        Div(
                            P("Network", cls="mb-1"),
                            Progress(
                                label=Span("33%", cls="float-right"),
                                value="33",
                                progress_cls=ProgressT.progress_purple,
                                size="sm"
                            ),
                            cls="mb-3"
                        ),
                        cls="w-full md:w-1/2 px-2"
                    ),
                    cls="flex flex-wrap -mx-2"
                ),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-2xl"
        ),
        code="""from fastbite.all import Progress, ProgressT
from fasthtml.common import Div, H4, P, Span

Div(
    H4("System Resources", cls="mb-4"),
    Div(
        # Left column
        Div(
            # CPU Usage
            Div(
                P("CPU Usage", cls="mb-1"),
                Progress(
                    label=Span("78%", cls="float-right"),
                    value="78",
                    progress_cls=ProgressT.progress_blue,
                    size="sm"
                ),
                cls="mb-3"
            ),
            # Memory Usage
            Div(
                P("Memory Usage", cls="mb-1"),
                Progress(
                    label=Span("45%", cls="float-right"),
                    value="45",
                    progress_cls=ProgressT.progress_green,
                    size="sm"
                ),
                cls="mb-3"
            ),
            cls="w-full md:w-1/2 px-2"
        ),
        # Right column
        Div(
            # Disk Usage
            Div(
                P("Disk Usage", cls="mb-1"),
                Progress(
                    label=Span("92%", cls="float-right"),
                    value="92",
                    progress_cls=ProgressT.progress_red,
                    size="sm"
                ),
                cls="mb-3"
            ),
            # Network
            Div(
                P("Network", cls="mb-1"),
                Progress(
                    label=Span("33%", cls="float-right"),
                    value="33",
                    progress_cls=ProgressT.progress_purple,
                    size="sm"
                ),
                cls="mb-3"
            ),
            cls="w-full md:w-1/2 px-2"
        ),
        cls="flex flex-wrap -mx-2"
    ),
    cls="p-4 border rounded-lg"
)""",
        id="dashboard-progress"
    ),
    
    Br(),
    
    H2("API Reference", link=True),
    
    H3("Progress Component", link=True),
    P("The complete API reference for the Progress component:"),
    
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
                Td("Components to put in the progress bar (often nothing)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("label", cls="px-4 py-2 border"),
                Td("str|FT", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Label of the progress bar (string or component)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("label_cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("TextT.sm", cls="px-4 py-2 border"),
                Td("Additional classes on the label", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("ProgressT.progress_primary", cls="px-4 py-2 border"),
                Td("Additional classes on the progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("ProgressT.bg_default", cls="px-4 py-2 border"),
                Td("Additional classes on the background", cls="px-4 py-2 border")
            ),
            Tr(
                Td("value", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Value of the progress bar (0-100)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("size", cls="px-4 py-2 border"),
                Td("'sm'|'md'|'lg'", cls="px-4 py-2 border"),
                Td("'md'", cls="px-4 py-2 border"),
                Td("Height of the progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("()", cls="px-4 py-2 border"),
                Td("Additional classes on the container", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("ProgressT Enum", link=True),
    P("Available theme options for progress bars:"),
    
    Table(
        Thead(
            Tr(
                Th("Value", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("progress_primary", cls="px-4 py-2 border"),
                Td("Primary color progress bar (default)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_dark", cls="px-4 py-2 border"),
                Td("Dark gray color with light mode/dark mode support", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_blue", cls="px-4 py-2 border"),
                Td("Blue color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_red", cls="px-4 py-2 border"),
                Td("Red color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_green", cls="px-4 py-2 border"),
                Td("Green color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_yellow", cls="px-4 py-2 border"),
                Td("Yellow color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_purple", cls="px-4 py-2 border"),
                Td("Purple color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("progress_pink", cls="px-4 py-2 border"),
                Td("Pink color progress bar", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_default", cls="px-4 py-2 border"),
                Td("Default gray background with dark mode support", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_primary", cls="px-4 py-2 border"),
                Td("Primary color background", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_dark", cls="px-4 py-2 border"),
                Td("Dark gray background with dark mode support", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_blue", cls="px-4 py-2 border"),
                Td("Blue background", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_red", cls="px-4 py-2 border"),
                Td("Red background", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_green", cls="px-4 py-2 border"),
                Td("Green background", cls="px-4 py-2 border")
            ),
            Tr(
                Td("bg_yellow", cls="px-4 py-2 border"),
                Td("Yellow background", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    H2("Best Practices", link=True),
    
    P("Follow these guidelines when using progress components:"),
    
    Ul(
        Li("Use appropriate colors to indicate status (green for success, red for warnings)"),
        Li("Keep labels concise and clear"),
        Li("Consider providing context with percentages when useful"),
        Li("Use smaller progress bars for dashboard displays with multiple metrics"),
        Li("Ensure sufficient contrast between the progress bar and its background"),
        Li("Choose size based on the importance and visibility needs"),
        Li("Group related progress indicators together"),
        cls="list-disc pl-5 space-y-2 mb-6"
    )
) 