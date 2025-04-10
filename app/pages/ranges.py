from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import *
from utils import component_showcase

ranges_components = Div(
    H1("Range Input Components", link=True),
    
    P("Fastbite provides customizable range input components for selecting numeric values within a specified range."),
    
    H2("Basic Range Inputs", link=True),
    
    H3("Default Range Input", link=True),
    P("The ", Code("Range"), " component creates a styled range slider with a label:"),

    component_showcase(
        Div(
            Range(
                label="Default Range",
                value="50",
                min="0",
                max="100"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range

# Basic range slider with label
Range(
    label="Default Range",  # Label text
    value="50",            # Initial value
    min="0",               # Minimum value
    max="100"              # Maximum value
)""",
        id="basic-range"
    ),
    
    Br(),
    
    H3("Range Sizes", link=True),
    P("Range inputs come in different sizes using the ", Code("cls"), " parameter with the ", Code("RangeT"), " enum:"),

    component_showcase(
        Div(
            Div(
                P("Small Range", cls="mb-2"),
                Range(
                    label="Small Range",
                    value="50",
                    cls=RangeT.sm
                ),
                cls="mb-6"
            ),
            Div(
                P("Default Range", cls="mb-2"),
                Range(
                    label="Default Range",
                    value="50",
                    cls=RangeT.default
                ),
                cls="mb-6"
            ),
            Div(
                P("Large Range", cls="mb-2"),
                Range(
                    label="Large Range",
                    value="50",
                    cls=RangeT.lg
                ),
                cls="mb-6"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range, RangeT

# Small range slider
Range(
    label="Small Range",
    value="50",
    cls=RangeT.sm  # Small size
)

# Default range slider
Range(
    label="Default Range",
    value="50",
    cls=RangeT.default  # Default size
)

# Large range slider
Range(
    label="Large Range",
    value="50",
    cls=RangeT.lg  # Large size
)""",
        id="range-sizes"
    ),
    
    Br(),
    
    H2("Range Configuration", link=True),
    
    H3("Min, Max and Step Values", link=True),
    P("Configure the range slider behavior with ", Code("min"), ", ", Code("max"), ", and ", Code("step"), " parameters:"),

    component_showcase(
        Div(
            Div(
                P("Default Range (0-100, step=1)", cls="mb-2"),
                Range(
                    label="Default Range",
                    value="50",
                    min="0",
                    max="100",
                    step="1"
                ),
                cls="mb-6"
            ),
            Div(
                P("Custom Range (-50 to 50, step=5)", cls="mb-2"),
                Range(
                    label="Custom Range",
                    value="0",
                    min="-50",
                    max="50",
                    step="5"
                ),
                cls="mb-6"
            ),
            Div(
                P("Decimal Range (0-1, step=0.1)", cls="mb-2"),
                Range(
                    label="Decimal Range",
                    value="0.5",
                    min="0",
                    max="1",
                    step="0.1"
                ),
                cls="mb-6"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range

# Default range (0-100, step=1)
Range(
    label="Default Range",
    value="50",
    min="0",
    max="100",
    step="1"  # Default step is 1
)

# Custom range (-50 to 50, step=5)
Range(
    label="Custom Range",
    value="0",
    min="-50",   # Minimum value can be negative
    max="50",    # Maximum value
    step="5"     # Increment by 5
)

# Decimal range (0-1, step=0.1)
Range(
    label="Decimal Range",
    value="0.5",
    min="0",
    max="1",
    step="0.1"   # Increment by 0.1
)""",
        id="range-configuration"
    ),
    
    Br(),
    
    H3("Help Labels", link=True),
    P("Add context to range sliders with help labels to show minimum and maximum values:"),

    component_showcase(
        Div(
            Range(
                label="Volume Control",
                value="60",
                min="0",
                max="100",
                help_labels=["Mute", "Max"]
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range

# Range with min/max context labels
Range(
    label="Volume Control",
    value="60",
    min="0",
    max="100",
    help_labels=["Mute", "Max"]  # Labels for min/max values
)""",
        id="range-help-labels"
    ),
    
    Br(),
    
    H3("Custom Styling", link=True),
    P("Customize the appearance of range inputs with different container and range styles:"),

    component_showcase(
        Div(
            Div(
                Range(
                    label="Default Styling",
                    value="50",
                    div_cls="mb-5"  # Default container class
                ),
                cls="mb-6"
            ),
            Div(
                Range(
                    label="Custom Container Spacing",
                    value="50",
                    div_cls="mb-8 p-4 border rounded-lg"  # Custom container class
                ),
                cls="mb-6"
            ),
            Div(
                Range(
                    label="Custom Range Color",
                    value="50",
                    cls="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer dark:bg-blue-700"  # Custom range class
                ),
                cls="mb-6"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range

# Default styling
Range(
    label="Default Styling",
    value="50",
    div_cls="mb-5"  # Default container spacing
)

# Custom container styling
Range(
    label="Custom Container Spacing",
    value="50",
    div_cls="mb-8 p-4 border rounded-lg"  # Custom container with border
)

# Custom range color styling
Range(
    label="Custom Range Color",
    value="50",
    # Custom color for the range track
    cls="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer dark:bg-blue-700"
)""",
        id="range-custom-styling"
    ),
    
    Br(),
    
    H2("Practical Examples", link=True),
    
    H3("Filter Controls", link=True),
    P("Use range inputs to create filter controls for applications:"),

    component_showcase(
        Div(
            Div(
                H4("Filter Options", cls="text-lg font-semibold mb-4"),
                Range(
                    label="Price Range",
                    value="50",
                    min="0",
                    max="100",
                    help_labels=["$0", "$100"]
                ),
                Range(
                    label="Distance",
                    value="10",
                    min="0",
                    max="50",
                    help_labels=["Nearby", "50 miles"]
                ),
                Range(
                    label="Rating",
                    value="4",
                    min="1",
                    max="5",
                    step="1",
                    help_labels=["1 star", "5 stars"]
                ),
                Button("Apply Filters", cls=ButtonT.primary+"mt-4"),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range, ButtonPrimary
from fasthtml.common import Div, H4

Div(
    H4("Filter Options", cls="text-lg font-semibold mb-4"),
    
    # Price range filter
    Range(
        label="Price Range",
        value="50",
        min="0",
        max="100",
        help_labels=["$0", "$100"]
    ),
    
    # Distance filter
    Range(
        label="Distance",
        value="10",
        min="0",
        max="50",
        help_labels=["Nearby", "50 miles"]
    ),
    
    # Rating filter
    Range(
        label="Rating",
        value="4",
        min="1",
        max="5",
        step="1",
        help_labels=["1 star", "5 stars"]
    ),
    
    ButtonPrimary("Apply Filters", cls="mt-4"),
    cls="p-4 border rounded-lg"
)""",
        id="filter-controls"
    ),
    
    Br(),
    
    H3("Media Controls", link=True),
    P("Create media player controls using range inputs:"),

    component_showcase(
        Div(
            Div(
                H4("Audio Player", cls="text-lg font-semibold mb-4"),
                P("Now Playing: Sample Audio Track", cls="mb-2"),
                Range(
                    label="",
                    value="35",
                    min="0",
                    max="100",
                    help_labels=["0:00", "3:45"],
                    div_cls="mb-3"
                ),
                DivFullySpaced(
                    DivHStacked(
                        Button(
                            Icon("skip-back", cls="w-4 h-4"),
                            cls="p-2 rounded-full bg-gray-100 dark:bg-gray-700"
                        ),
                        Button(
                            Icon("play", cls="w-5 h-5"),
                            cls="p-2 rounded-full bg-primary-600 text-white mx-2"
                        ),
                        Button(
                            Icon("skip-forward", cls="w-4 h-4"),
                            cls="p-2 rounded-full bg-gray-100 dark:bg-gray-700"
                        ),
                        cls="flex"
                    ),
                    Div(
                        Range(
                            label="",
                            value="70",
                            min="0",
                            max="100",
                            cls=RangeT.sm,
                            div_cls="mb-0 w-32"
                        ),
                        Icon("volume-2", cls="w-5 h-5 ml-2"),
                        cls="flex items-center"
                    ),
                    cls="mt-4"
                ),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range, RangeT, Button, Icon, DivFullySpaced, DivCentered
from fasthtml.common import Div, H4, P

Div(
    H4("Audio Player", cls="text-lg font-semibold mb-4"),
    P("Now Playing: Sample Audio Track", cls="mb-2"),
    
    # Progress/timeline range
    Range(
        label="",
        value="35",
        min="0",
        max="100",
        help_labels=["0:00", "3:45"],
        div_cls="mb-3"
    ),
    
    DivFullySpaced(
        # Playback controls
        DivCentered(
            Button(
                Icon("skip-back", cls="w-4 h-4"),
                cls="p-2 rounded-full bg-gray-100 dark:bg-gray-700"
            ),
            Button(
                Icon("play", cls="w-5 h-5"),
                cls="p-2 rounded-full bg-primary-600 text-white mx-2"
            ),
            Button(
                Icon("skip-forward", cls="w-4 h-4"),
                cls="p-2 rounded-full bg-gray-100 dark:bg-gray-700"
            ),
            cls="flex"
        ),
        
        # Volume control
        Div(
            Range(
                label="",
                value="70",
                min="0",
                max="100",
                cls=RangeT.sm,
                div_cls="mb-0 w-32"
            ),
            Icon("volume-2", cls="w-5 h-5 ml-2"),
            cls="flex items-center"
        ),
        cls="mt-4"
    ),
    cls="p-4 border rounded-lg"
)""",
        id="media-controls"
    ),
    
    Br(),
    
    H2("Interactive Form Examples", link=True),
    
    H3("Range with Live Preview", link=True),
    P("Combine range inputs with interactive elements to create responsive UIs:"),

    component_showcase(
        Div(
            Div(
                H4("Slider with Preview", cls="text-lg font-semibold mb-4"),
                DivFullySpaced(
                    H5("Opacity Control", cls="text-base font-medium"),
                    Badge("75%", cls="bg-primary-100 text-primary-800 dark:bg-primary-900 dark:text-primary-300"),
                    cls="mb-2"
                ),
                Range(
                    label="",
                    value="75",
                    min="0",
                    max="100",
                    id="opacity-range",
                    div_cls="mb-4"
                ),
                DivCentered(
                    Div(
                        cls="w-32 h-32 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600"
                    ),
                    cls="p-4 border rounded-lg opacity-75"
                ),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range, Badge, DivFullySpaced, DivCentered
from fasthtml.common import Div, H4, H5

Div(
    H4("Slider with Preview", cls="text-lg font-semibold mb-4"),
    
    # Header with value display
    DivFullySpaced(
        H5("Opacity Control", cls="text-base font-medium"),
        Badge("75%", cls="bg-primary-100 text-primary-800 dark:bg-primary-900 dark:text-primary-300"),
        cls="mb-2"
    ),
    
    # Range slider
    Range(
        label="",
        value="75",
        min="0",
        max="100",
        id="opacity-range",
        div_cls="mb-4"
    ),
    
    # Preview element with opacity applied
    DivCentered(
        Div(
            cls="w-32 h-32 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600"
        ),
        cls="p-4 border rounded-lg opacity-75"  # Opacity value matches range
    ),
    cls="p-4 border rounded-lg"
)

# Note: In a real implementation, you would use JavaScript to update 
# the opacity value and badge text based on the range input value.""",
        id="range-live-preview"
    ),
    
    Br(),
    
    H2("API Reference", link=True),
    
    H3("Range Component", link=True),
    P("The complete API reference for the Range component:"),
    
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
                Td("Components to put in the range (often nothing)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("value", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Initial value of the range input", cls="px-4 py-2 border")
            ),
            Tr(
                Td("label", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Label text for the range input", cls="px-4 py-2 border")
            ),
            Tr(
                Td("help_labels", cls="px-4 py-2 border"),
                Td("list", cls="px-4 py-2 border"),
                Td("None", cls="px-4 py-2 border"),
                Td("Min/max context labels (list of 2 items)", cls="px-4 py-2 border")
            ),
            Tr(
                Td("id", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("'default-range'", cls="px-4 py-2 border"),
                Td("ID attribute for the range input", cls="px-4 py-2 border")
            ),
            Tr(
                Td("min", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("None", cls="px-4 py-2 border"),
                Td("Minimum value of the range", cls="px-4 py-2 border")
            ),
            Tr(
                Td("max", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("None", cls="px-4 py-2 border"),
                Td("Maximum value of the range", cls="px-4 py-2 border")
            ),
            Tr(
                Td("step", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("None", cls="px-4 py-2 border"),
                Td("Step increment value", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("Enum|str|tuple", cls="px-4 py-2 border"),
                Td("RangeT.default", cls="px-4 py-2 border"),
                Td("Classes for the range input", cls="px-4 py-2 border")
            ),
            Tr(
                Td("div_cls", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("'mb-5'", cls="px-4 py-2 border"),
                Td("Classes for the container div", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("RangeT Enum", link=True),
    P("Available theme options for range inputs:"),
    
    Table(
        Thead(
            Tr(
                Th("Value", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("default", cls="px-4 py-2 border"),
                Td("Standard range input style with medium height and dark mode support", cls="px-4 py-2 border")
            ),
            Tr(
                Td("sm", cls="px-4 py-2 border"),
                Td("Small range input with reduced height", cls="px-4 py-2 border")
            ),
            Tr(
                Td("lg", cls="px-4 py-2 border"),
                Td("Large range input with increased height", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H2("Best Practices", link=True),
    
    P("Follow these guidelines when using range components:"),
    
    Ul(
        Li("Always include min and max values to define the valid range"),
        Li("Add descriptive labels to help users understand what the range controls"),
        Li("Consider using help_labels to provide context for the minimum and maximum values"),
        Li("Choose an appropriate step value based on the precision needed"),
        Li("Use a suitable size (sm, default, lg) based on the importance and precision required"),
        Li("Set a sensible default value within the valid range"),
        Li("Consider adding visual feedback (like previews) for range adjustments"),
        Li("Ensure sufficient spacing around range inputs for easy interaction"),
        cls="list-disc pl-5 space-y-2 mb-6"
    )
) 