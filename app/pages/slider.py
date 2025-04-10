from fasthtml.common import *
from fastbite.all import *
from fasthtml.svg import *
from utils import component_showcase

slider_components = Div(
    H1("Slider Components", link=True),
    
    P("Fastbite provides carousel/slider components for creating interactive image galleries, product showcases, and content carousels."),
    
    H2("Basic Slider", link=True),
    
    H3("Default Slider", link=True),
    P("The ", Code("Slider"), " component creates a basic image carousel with navigation controls and indicators:"),

    component_showcase(
        Div(
            Slider(
                [
                    PicSumImg(h=600, w=800, alt="Slide 1", cls="d-block w-full"),
                    PicSumImg(h=600, w=800, id=237, alt="Slide 2", cls="d-block w-full"),
                    PicSumImg(h=600, w=800, id=42, alt="Slide 3", cls="d-block w-full")
                ],
                id="default-slider"
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import Slider, PicSumImg

# Basic slider with images
Slider(
    [
        PicSumImg(h=400, w=800, alt="Slide 1", cls="d-block w-full"),
        PicSumImg(h=400, w=800, id=237, alt="Slide 2", cls="d-block w-full"),
        PicSumImg(h=400, w=800, id=42, alt="Slide 3", cls="d-block w-full")
    ],
    id="default-slider"  # Unique ID for the slider
)""",
        id="basic-slider"
    ),
    
    Br(),
    
    H3("Slider with Custom Content", link=True),
    P("Create sliders with custom content instead of just images:"),

    component_showcase(
        Div(
            Slider(
                [
                    Div(
                        H3("First Slide", cls="text-2xl font-bold mb-2 text-white"),
                        P("This is the first slide content", cls="text-white"),
                        cls="flex flex-col items-center justify-center h-full p-4 bg-blue-600"
                    ),
                    Div(
                        H3("Second Slide", cls="text-2xl font-bold mb-2 text-white"),
                        P("This is the second slide content", cls="text-white"),
                        cls="flex flex-col items-center justify-center h-full p-4 bg-green-600"
                    ),
                    Div(
                        H3("Third Slide", cls="text-2xl font-bold mb-2 text-white"),
                        P("This is the third slide content", cls="text-white"),
                        cls="flex flex-col items-center justify-center h-full p-4 bg-purple-600"
                    )
                ],
                id="content-slider"
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import Slider
from fasthtml.common import Div, H3, P

# Slider with custom content
Slider(
    [
        Div(
            H3("First Slide", cls="text-2xl font-bold mb-2 text-white"),
            P("This is the first slide content", cls="text-white"),
            cls="flex flex-col items-center justify-center h-full p-4 bg-blue-600"
        ),
        Div(
            H3("Second Slide", cls="text-2xl font-bold mb-2 text-white"),
            P("This is the second slide content", cls="text-white"),
            cls="flex flex-col items-center justify-center h-full p-4 bg-green-600"
        ),
        Div(
            H3("Third Slide", cls="text-2xl font-bold mb-2 text-white"),
            P("This is the third slide content", cls="text-white"),
            cls="flex flex-col items-center justify-center h-full p-4 bg-purple-600"
        )
    ],
    id="content-slider"
)""",
        id="content-slider"
    ),
    
    Br(),
    
    H2("Slider Options", link=True),
    
    H3("Controls and Indicators", link=True),
    P("Customize the slider by showing or hiding controls and indicators:"),

    component_showcase(
        Div(
            Div(
                H4("Slider without Controls", cls="mb-2"),
                Slider(
                    [
                        PicSumImg(h=300, w=800, alt="Slide 1", cls="d-block w-full"),
                        PicSumImg(h=300, w=800, id=240, alt="Slide 2", cls="d-block w-full")
                    ],
                    show_controls=False,
                    id="no-controls-slider"
                ),
                cls="mb-8"
            ),
            Div(
                H4("Slider without Indicators", cls="mb-2"),
                Slider(
                    [
                        PicSumImg(h=300, w=800, id=244, alt="Slide 1", cls="d-block w-full"),
                        PicSumImg(h=300, w=800, id=243, alt="Slide 2", cls="d-block w-full")
                    ],
                    show_indicators=False,
                    id="no-indicators-slider"
                ),
                cls="mb-8"
            ),
            Div(
                H4("Slider without Controls or Indicators", cls="mb-2"),
                Slider(
                    [
                        PicSumImg(h=300, w=800, id=239, alt="Slide 1", cls="d-block w-full"),
                        PicSumImg(h=300, w=800, id=248, alt="Slide 2", cls="d-block w-full")
                    ],
                    show_controls=False,
                    show_indicators=False,
                    id="minimal-slider"
                )
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import Slider, PicSumImg
from fasthtml.common import Div, H4

# Slider without control arrows
Slider(
    [
        PicSumImg(h=300, w=800, alt="Slide 1", cls="d-block w-full"),
        PicSumImg(h=300, w=800, id=240, alt="Slide 2", cls="d-block w-full")
    ],
    show_controls=False,  # Hide the next/previous arrows
    id="no-controls-slider"
)

# Slider without indicator dots
Slider(
    [
        PicSumImg(h=300, w=800, id=244, alt="Slide 1", cls="d-block w-full"),
        PicSumImg(h=300, w=800, id=243, alt="Slide 2", cls="d-block w-full")
    ],
    show_indicators=False,  # Hide the indicator dots
    id="no-indicators-slider"
)

# Minimal slider without controls or indicators
Slider(
    [
        PicSumImg(h=300, w=800, id=239, alt="Slide 1", cls="d-block w-full"),
        PicSumImg(h=300, w=800, id=248, alt="Slide 2", cls="d-block w-full")
    ],
    show_controls=False,
    show_indicators=False,
    id="minimal-slider"
)""",
        id="slider-options"
    ),
    
    Br(),
    
    H3("Slider Transitions", link=True),
    P("Different transition effects can be applied using the ", Code("SliderItemT"), " enum:"),

    component_showcase(
        Div(
            H4("Default Transition", cls="mb-2"),
            SliderContainer(
                Div(
                    SliderItem(
                        PicSumImg(h=300, w=800, id=250, alt="Slide 1", cls="d-block w-full"),
                        cls=SliderItemT.default
                    ),
                    SliderItem(
                        PicSumImg(h=300, w=800, id=251, alt="Slide 2", cls="d-block w-full"),
                        cls=SliderItemT.default
                    ),
                    cls="relative h-56 overflow-hidden rounded-lg md:h-72"
                ),
                *SliderControls(),
                SliderNav(num_slides=2),
                id="default-transition"
            ),
            cls="max-w-2xl mb-8"
        ),
        code="""from fastbite.all import SliderContainer, SliderItem, SliderItemT, SliderControls, SliderNav, PicSumImg
from fasthtml.common import Div

# Slider with default transition (ease-in-out)
SliderContainer(
    Div(
        SliderItem(
            PicSumImg(h=300, w=800, id=250, alt="Slide 1", cls="d-block w-full"),
            cls=SliderItemT.default  # Default transition (ease-in-out)
        ),
        SliderItem(
            PicSumImg(h=300, w=800, id=251, alt="Slide 2", cls="d-block w-full"),
            cls=SliderItemT.default
        ),
        cls="relative h-56 overflow-hidden rounded-lg md:h-72"
    ),
    *SliderControls(),  # Unpack previous and next buttons
    SliderNav(num_slides=2),  # Navigation indicators
    id="default-transition"
)""",
        id="default-transition"
    ),
    
    Br(),
    
    component_showcase(
        Div(
            H4("Linear Transition", cls="mb-2"),
            SliderContainer(
                Div(
                    SliderItem(
                        PicSumImg(h=300, w=800, id=252, alt="Slide 1", cls="d-block w-full"),
                        cls=SliderItemT.linear
                    ),
                    SliderItem(
                        PicSumImg(h=300, w=800, id=253, alt="Slide 2", cls="d-block w-full"),
                        cls=SliderItemT.linear
                    ),
                    cls="relative h-56 overflow-hidden rounded-lg md:h-72"
                ),
                *SliderControls(),
                SliderNav(num_slides=2),
                id="linear-transition"
            ),
            cls="max-w-2xl"
        ),
        code="""from fastbite.all import SliderContainer, SliderItem, SliderItemT, SliderControls, SliderNav, PicSumImg
from fasthtml.common import Div

# Slider with linear transition
SliderContainer(
    Div(
        SliderItem(
            PicSumImg(h=300, w=800, id=252, alt="Slide 1", cls="d-block w-full"),
            cls=SliderItemT.linear  # Linear transition
        ),
        SliderItem(
            PicSumImg(h=300, w=800, id=253, alt="Slide 2", cls="d-block w-full"),
            cls=SliderItemT.linear
        ),
        cls="relative h-56 overflow-hidden rounded-lg md:h-72"
    ),
    *SliderControls(),
    SliderNav(num_slides=2),
    id="linear-transition"
)""",
        id="linear-transition"
    ),
    
    Br(),
    
    H2("Using Individual Components", link=True),
    
    H3("Custom Slider Assembly", link=True),
    P("Build custom sliders by composing the individual components:"),

    component_showcase(
        Div(
            SliderContainer(
                Div(
                    SliderItem(
                        Div(
                            H3("First Custom Slide", cls="text-2xl font-bold mb-2 text-white"),
                            P("This is a custom-built slider", cls="text-white"),
                            cls="flex flex-col items-center justify-center h-full p-4 bg-red-600"
                        )
                    ),
                    SliderItem(
                        Div(
                            H3("Second Custom Slide", cls="text-2xl font-bold mb-2 text-white"),
                            P("Built using individual components", cls="text-white"),
                            cls="flex flex-col items-center justify-center h-full p-4 bg-indigo-600"
                        )
                    ),
                    cls="relative h-56 overflow-hidden rounded-lg md:h-72"
                ),
                SliderNav(num_slides=2, cls="absolute z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse bottom-5 left-1/2"),
                *SliderControls(),
                id="custom-assembled-slider"
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import SliderContainer, SliderItem, SliderNav, SliderControls
from fasthtml.common import Div, H3, P

# Building a slider with individual components
SliderContainer(
    # Wrapper div containing slides
    Div(
        # First slide
        SliderItem(
            Div(
                H3("First Custom Slide", cls="text-2xl font-bold mb-2 text-white"),
                P("This is a custom-built slider", cls="text-white"),
                cls="flex flex-col items-center justify-center h-full p-4 bg-red-600"
            )
        ),
        # Second slide
        SliderItem(
            Div(
                H3("Second Custom Slide", cls="text-2xl font-bold mb-2 text-white"),
                P("Built using individual components", cls="text-white"),
                cls="flex flex-col items-center justify-center h-full p-4 bg-indigo-600"
            )
        ),
        cls="relative h-56 overflow-hidden rounded-lg md:h-72"
    ),
    # Navigation indicators
    SliderNav(
        num_slides=2, 
        cls="absolute z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse bottom-5 left-1/2"
    ),
    # Control buttons (unpacked from tuple)
    *SliderControls(),
    id="custom-assembled-slider"
)""",
        id="custom-slider"
    ),
    
    Br(),
    
    H2("Practical Examples", link=True),
    
    H3("Product Showcase", link=True),
    P("Use sliders to create product galleries with thumbnails:"),

    component_showcase(
        Div(
            Div(
                H4("Product Gallery", cls="text-xl font-bold mb-4"),
                Slider(
                    [
                        Div(
                            PicSumImg(h=500, w=800, id=26, alt="Product 1", cls="mx-auto"),
                            H5("Premium Camera", cls="text-lg font-medium mt-2"),
                            P("$199.99", cls="text-primary-600 font-bold"),
                            P("High-quality premium camera with enhanced features", cls="text-gray-600 text-sm"),
                            cls="p-4"
                        ),
                        Div(
                            PicSumImg(h=500, w=800, id=28, alt="Product 2", cls="mx-auto"),
                            H5("Deluxe Camera Plus", cls="text-lg font-medium mt-2"),
                            P("$249.99", cls="text-primary-600 font-bold"),
                            P("Our deluxe model with advanced shooting capabilities", cls="text-gray-600 text-sm"),
                            cls="p-4"
                        ),
                        Div(
                            PicSumImg(h=500, w=800, id=27, alt="Product 3", cls="mx-auto"),
                            H5("Ultimate Camera Pro", cls="text-lg font-medium mt-2"),
                            P("$299.99", cls="text-primary-600 font-bold"),
                            P("Professional-grade camera for serious photography enthusiasts", cls="text-gray-600 text-sm"),
                            cls="p-4"
                        )
                    ],
                    id="product-slider",
                    wrapper_cls="relative h-96 overflow-hidden rounded-lg md:h-[450px]"
                ),
                cls="border rounded-lg shadow-sm"
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import Slider, PicSumImg
from fasthtml.common import Div, H4, H5, P

# Product showcase slider
Div(
    H4("Product Gallery", cls="text-xl font-bold mb-4"),
    Slider(
        [
            Div(
                PicSumImg(h=500, w=800, id=26, alt="Product 1", cls="mx-auto"),
                H5("Premium Camera", cls="text-lg font-medium mt-2"),
                P("$199.99", cls="text-primary-600 font-bold"),
                P("High-quality premium camera with enhanced features", cls="text-gray-600 text-sm"),
                cls="p-4"
            ),
            Div(
                PicSumImg(h=500, w=800, id=28, alt="Product 2", cls="mx-auto"),
                H5("Deluxe Camera Plus", cls="text-lg font-medium mt-2"),
                P("$249.99", cls="text-primary-600 font-bold"),
                P("Our deluxe model with advanced shooting capabilities", cls="text-gray-600 text-sm"),
                cls="p-4"
            ),
            Div(
                PicSumImg(h=500, w=800, id=27, alt="Product 3", cls="mx-auto"),
                H5("Ultimate Camera Pro", cls="text-lg font-medium mt-2"),
                P("$299.99", cls="text-primary-600 font-bold"),
                P("Professional-grade camera for serious photography enthusiasts", cls="text-gray-600 text-sm"),
                cls="p-4"
            )
        ],
        id="product-slider",
        wrapper_cls="relative h-96 overflow-hidden rounded-lg md:h-[450px]"
    ),
    cls="border rounded-lg shadow-sm"
)""",
        id="product-showcase"
    ),
    
    Br(),
    
    H3("Testimonial Carousel", link=True),
    P("Create a testimonial carousel to showcase customer feedback:"),

    component_showcase(
        Div(
            Slider(
                [
                    Div(
                        P("\"This is the best product I've ever used! It completely changed my life.\"", cls="text-lg italic mb-4"),
                        Div(
                            DiceBearAvatar("John Doe", h=10, w=10, cls="rounded-full"),
                            Div(
                                H5("John Doe", cls="font-medium"),
                                P("CEO at TechCorp", cls="text-sm text-gray-600"),
                                cls=""
                            ),
                            cls="flex items-center"
                        ),
                        cls="bg-white p-6 rounded-lg shadow-md mx-4"
                    ),
                    Div(
                        P("\"I was skeptical at first, but this product exceeded all my expectations!\"", cls="text-lg italic mb-4"),
                        Div(
                            DiceBearAvatar("Jane Smith", h=10, w=10, cls="rounded-full"),
                            Div(
                                H5("Jane Smith", cls="font-medium"),
                                P("Designer at CreativeCo", cls="text-sm text-gray-600"),
                                cls=""
                            ),
                            cls="flex items-center"
                        ),
                        cls="bg-white p-6 rounded-lg shadow-md mx-4"
                    ),
                    Div(
                        P("\"Our team's productivity increased by 200% after implementing this solution.\"", cls="text-lg italic mb-4"),
                        Div(
                            DiceBearAvatar("Mike Johnson", h=10, w=10, cls="rounded-full"),
                            Div(
                                H5("Mike Johnson", cls="font-medium"),
                                P("Project Manager at BuildInc", cls="text-sm text-gray-600"),
                                cls=""
                            ),
                            cls="flex items-center"
                        ),
                        cls="bg-white p-6 rounded-lg shadow-md mx-4"
                    )
                ],
                id="testimonial-slider",
                wrapper_cls="relative h-64 overflow-hidden rounded-lg md:h-72 bg-gray-100"
            ),
            cls="max-w-3xl"
        ),
        code="""from fastbite.all import Slider, DiceBearAvatar
from fasthtml.common import Div, H5, P

# Testimonial carousel
Slider(
    [
        Div(
            P("\"This is the best product I've ever used! It completely changed my life.\"", cls="text-lg italic mb-4"),
            Div(
                DiceBearAvatar("John Doe", h=10, w=10, cls="rounded-full"),  # Avatar with DiceBearAvatar
                Div(
                    H5("John Doe", cls="font-medium"),
                    P("CEO at TechCorp", cls="text-sm text-gray-600"),
                ),
                cls="flex items-center"
            ),
            cls="bg-white p-6 rounded-lg shadow-md mx-4"
        ),
        Div(
            P("\"I was skeptical at first, but this product exceeded all my expectations!\"", cls="text-lg italic mb-4"),
            Div(
                DiceBearAvatar("Jane Smith", h=10, w=10, cls="rounded-full"),  # Avatar with DiceBearAvatar
                Div(
                    H5("Jane Smith", cls="font-medium"),
                    P("Designer at CreativeCo", cls="text-sm text-gray-600"),
                ),
                cls="flex items-center"
            ),
            cls="bg-white p-6 rounded-lg shadow-md mx-4"
        ),
        Div(
            P("\"Our team's productivity increased by 200% after implementing this solution.\"", cls="text-lg italic mb-4"),
            Div(
                DiceBearAvatar("Mike Johnson", h=10, w=10, cls="rounded-full"),  # Avatar with DiceBearAvatar
                Div(
                    H5("Mike Johnson", cls="font-medium"),
                    P("Project Manager at BuildInc", cls="text-sm text-gray-600"),
                ),
                cls="flex items-center"
            ),
            cls="bg-white p-6 rounded-lg shadow-md mx-4"
        )
    ],
    id="testimonial-slider",
    wrapper_cls="relative h-64 overflow-hidden rounded-lg md:h-72 bg-gray-100"
)""",
        id="testimonial-carousel"
    ),
    
    Br(),
    
    H2("API Reference", link=True),
    
    H3("Slider Component", link=True),
    P("The complete API reference for the Slider component:"),
    
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
                Td("items", cls="px-4 py-2 border"),
                Td("list", cls="px-4 py-2 border"),
                Td("-", cls="px-4 py-2 border"),
                Td("List of items to show in the slider", cls="px-4 py-2 border")
            ),
            Tr(
                Td("wrapper_cls", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("'relative h-56...'", cls="px-4 py-2 border"),
                Td("Classes for the wrapper div", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cls", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("''", cls="px-4 py-2 border"),
                Td("Classes for slider container", cls="px-4 py-2 border")
            ),
            Tr(
                Td("show_controls", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("True", cls="px-4 py-2 border"),
                Td("Whether to show navigation controls", cls="px-4 py-2 border")
            ),
            Tr(
                Td("show_indicators", cls="px-4 py-2 border"),
                Td("bool", cls="px-4 py-2 border"),
                Td("True", cls="px-4 py-2 border"),
                Td("Whether to show slide indicators", cls="px-4 py-2 border")
            ),
            Tr(
                Td("type", cls="px-4 py-2 border"),
                Td("'slide'|'static'", cls="px-4 py-2 border"),
                Td("'slide'", cls="px-4 py-2 border"),
                Td("Type of slider", cls="px-4 py-2 border")
            ),
            Tr(
                Td("id", cls="px-4 py-2 border"),
                Td("str", cls="px-4 py-2 border"),
                Td("None", cls="px-4 py-2 border"),
                Td("Optional ID for the carousel", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("SliderItemT Enum", link=True),
    P("Available transition options for slider items:"),
    
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
                Td("Standard ease-in-out transition", cls="px-4 py-2 border")
            ),
            Tr(
                Td("linear", cls="px-4 py-2 border"),
                Td("Linear transition with constant speed", cls="px-4 py-2 border")
            ),
            Tr(
                Td("ease_out_in", cls="px-4 py-2 border"),
                Td("Ease-out-in transition effect", cls="px-4 py-2 border")
            ),
            Tr(
                Td("cubic_bezier", cls="px-4 py-2 border"),
                Td("Cubic bezier transition for smoother motion", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H3("Component Functions", link=True),
    P("Individual components for building custom sliders:"),
    
    Table(
        Thead(
            Tr(
                Th("Component", cls="px-4 py-2"),
                Th("Description", cls="px-4 py-2")
            )
        ),
        Tbody(
            Tr(
                Td("SliderContainer", cls="px-4 py-2 border"),
                Td("Main container for the slider", cls="px-4 py-2 border")
            ),
            Tr(
                Td("SliderItem", cls="px-4 py-2 border"),
                Td("Individual slide item", cls="px-4 py-2 border")
            ),
            Tr(
                Td("SliderItems", cls="px-4 py-2 border"),
                Td("Container for slide items", cls="px-4 py-2 border")
            ),
            Tr(
                Td("SliderControls", cls="px-4 py-2 border"),
                Td("Previous and next control buttons", cls="px-4 py-2 border")
            ),
            Tr(
                Td("SliderNav", cls="px-4 py-2 border"),
                Td("Navigation indicators", cls="px-4 py-2 border")
            )
        ),
        cls="w-full table-auto mb-6 border"
    ),
    
    Br(),
    
    H2("Best Practices", link=True),
    
    P("Follow these guidelines when using slider components:"),
    
    Ul(
        Li("Keep the number of slides reasonable (3-5 is usually optimal)"),
        Li("Use appropriate sizing for slides to avoid content overflow"),
        Li("Ensure text on slides has sufficient contrast with the background"),
        Li("Consider using the static type for better accessibility"),
        Li("Add descriptive alt text to slide images"),
        Li("Test slider responsiveness across different screen sizes"),
        Li("Use consistent slide dimensions for a smoother experience"),
        Li("Consider adding keyboard navigation for accessibility"),
        Li("Keep slide content concise and focused"),
        cls="list-disc pl-5 space-y-2 mb-6"
    ),
    
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
                    PicSumImg(h=128, w=128, id=1005, cls="rounded-lg"),
                    cls="p-4 border rounded-lg opacity-75"
                ),
                cls="p-4 border rounded-lg"
            ),
            cls="max-w-md"
        ),
        code="""from fastbite.all import Range, Badge, DivFullySpaced, DivCentered, PicSumImg
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
    
    # Preview with adjustable opacity
    DivCentered(
        PicSumImg(h=128, w=128, id=1005, cls="rounded-lg"),
        cls="p-4 border rounded-lg opacity-75"
    ),
    cls="p-4 border rounded-lg"
)""",
        id="opacity-preview"
    )
) 