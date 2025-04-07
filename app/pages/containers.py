from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase
containers = Div(
    H1("Container Examples", cls=TextHeading.h1),
    P("Containers are layout elements that organize content within defined boundaries. They provide structure to your application and control how components are positioned and sized."),
    P("Fastbite offers a variety of container components with different sizing options, responsive behaviors, and layout patterns to help you structure your application efficiently."),
    
    H2("Basic Container", link=True),
    P("The ", Code("Container"), " component provides a responsive wrapper that centers content with appropriate padding. By default, it adapts to different screen sizes."),
    component_showcase(
        Container(
            Div("Default Container", cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
        ),
        code="""Container(
    Div("Default Container", cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold")
)""",
        id="basic-container"
    ),
    Br(),

    H2("Container Sizes", link=True),
    P("Control the maximum width of containers using the ", Code("size"), " parameter with ", Code("ContainerSize"), " enum values. This allows for consistent layouts across different sections of your application."),
    component_showcase(
        Div(
            P("Extra Small Container (20rem):"),
            Container(
                Div("XS Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
                size=ContainerSize.xs
            ),
            Br(),
            P("Small Container (24rem):"),
            Container(
                Div("SM Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
                size=ContainerSize.sm
            ),
            Br(),
            P("Medium Container (28rem):"),
            Container(
                Div("MD Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
                size=ContainerSize.md
            ),
            Br(),
            P("Large Container (32rem):"),
            Container(
                Div("LG Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
                size=ContainerSize.lg
            ),
        ),
        code="""# Extra Small Container (20rem)
Container(
    Div("XS Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.xs
)

# Small Container (24rem)
Container(
    Div("SM Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.sm
)

# Medium Container (28rem)
Container(
    Div("MD Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.md
)

# Large Container (32rem)
Container(
    Div("LG Container", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.lg
)""",
        id="container-sizes"
    ),
    Br(),
    # Fixed-width containers
    H2("Special Containers", link=True),
    P("Fastbite provides special container variants for specific layout needs."),
    
    H3("Fluid Container"),
    P("The fluid container (", Code("ContainerSize.fluid"), ") spans the full width of its parent element with padding on the sides."),
    component_showcase(
        Container(
            Div("Fluid Container (Full Width)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.fluid
        ),
        code="""Container(
    Div("Fluid Container (Full Width)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.fluid
)""",
        id="fluid-container"
    ),
    Br(),
    H3("Responsive Container"),
    P("The responsive container (", Code("ContainerSize.responsive"), ") automatically adjusts its width at different breakpoints for optimal viewing."),
    component_showcase(
        Container(
            Div("Responsive Container (Adapts to screen size)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.responsive
        ),
        code="""Container(
    Div("Responsive Container (Adapts to screen size)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
    size=ContainerSize.responsive
)""",
        id="responsive-container"
    ),
    Br(),
    
    # Container with FlexT layouts
    H2("Flexbox Container Layouts", link=True),
    P("Combine containers with Flexbox utilities using the ", Code("FlexT"), " enum for powerful layout control."),
    
    H3("Row Layout"),
    P("Create horizontal layouts with the ", Code("FlexT.row"), " class. Use the ", Code("gap"), " utility to control spacing between items."),
    component_showcase(
        Container(
            Container("Item 1", size=ContainerSize.fluid, cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
            Container("Item 2", size=ContainerSize.fluid, cls="bg-blue-200 dark:bg-blue-800 p-4 rounded-lg text-center font-bold"),
            Container("Item 3", size=ContainerSize.fluid, cls="bg-blue-300 dark:bg-blue-700 p-4 rounded-lg text-center font-bold"),
            cls=(FlexT.block, FlexT.row, "gap-4")
        ),
        code="""Container(
    Container("Item 1", size=ContainerSize.fluid, cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
    Container("Item 2", size=ContainerSize.fluid, cls="bg-blue-200 dark:bg-blue-800 p-4 rounded-lg text-center font-bold"),
    Container("Item 3", size=ContainerSize.fluid, cls="bg-blue-300 dark:bg-blue-700 p-4 rounded-lg text-center font-bold"),
    cls=(FlexT.block, FlexT.row, "gap-4")
)""",
        id="row-layout"
    ),
    Br(),
    
    H3("Column Layout"),
    P("Create vertical layouts with the ", Code("FlexT.column"), " class. Control spacing with the ", Code("gap"), " utility."),
    component_showcase(
        Container(
            Container("Item 1", size=ContainerSize.fluid, cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
            Container("Item 2", size=ContainerSize.fluid, cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
            Container("Item 3", size=ContainerSize.fluid, cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),
            cls=(FlexT.block, FlexT.column, "gap-4")
        ),
        code="""Container(
    Container("Item 1", size=ContainerSize.fluid, cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
    Container("Item 2", size=ContainerSize.fluid, cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
    Container("Item 3", size=ContainerSize.fluid, cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),
    cls=(FlexT.block, FlexT.column, "gap-4")
)""",
        id="column-layout"
    ),
    Br(),
    
    H3("Centered Content"),
    P("Center content both horizontally and vertically using ", Code("FlexT.center"), " and ", Code("FlexT.middle"), " classes."),
    component_showcase(
        Container(
            Div("Centered Content", cls="bg-purple-200 dark:bg-purple-800 p-8 rounded-lg text-center font-bold"),
            cls=(FlexT.block, FlexT.center, FlexT.middle, "h-48 bg-gray-100 dark:bg-gray-700 rounded-lg p-4")
        ),
        code="""Container(
    Div("Centered Content", cls="bg-purple-200 dark:bg-purple-800 p-8 rounded-lg text-center font-bold"),
    cls=(FlexT.block, FlexT.center, FlexT.middle, "h-48 bg-gray-100 dark:bg-gray-700 rounded-lg p-4")
)""",
        id="centered-content"
    ),
    Br(),
    
    H3("Content Justification"),
    P("Control how items are positioned along the main axis with various justification classes."),
    component_showcase(
        Div(
            P("Space Between (", Code("FlexT.between"), "):"),
            Container(
                Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
                Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
                Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
                cls=(FlexT.block, FlexT.between, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg")
            ),
            Br(),
            P("Left Aligned (", Code("FlexT.left"), "):"),
            Container(
                Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
                Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
                Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
                cls=(FlexT.block, FlexT.left, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
            ),
            Br(),
            P("Center Aligned (", Code("FlexT.center"), "):"),
            Container(
                Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
                Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
                Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
                cls=(FlexT.block, FlexT.center, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
            )
        ),
        code="""# Space Between
Container(
    Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
    Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
    Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
    cls=(FlexT.block, FlexT.between, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg")
)

# Left Aligned
Container(
    Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
    Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
    Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
    cls=(FlexT.block, FlexT.left, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
)

# Center Aligned
Container(
    Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
    Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
    Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
    cls=(FlexT.block, FlexT.center, "p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
)""",
        id="content-justification"
    ),
    Br(),
    
    H2("Predefined Layout Components", link=True),
    P("Fastbite provides several predefined layout components that combine containers with common flexbox patterns for quick implementation."),
    
    H3("DivHStacked"),
    P("The ", Code("DivHStacked"), " component creates a horizontal stack of elements with proper spacing."),
    component_showcase(
        DivHStacked(
            Div("Left Item", cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
            Div("Middle Item", cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
            Div("Right Item", cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),
            cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4"
        ),
        code="""DivHStacked(
    Div("Left Item", cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
    Div("Middle Item", cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
    Div("Right Item", cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),
    cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4"
)""",
        id="div-h-stacked"
    ),
    Br(),
    
    H3("DivVStacked"),
    P("The ", Code("DivVStacked"), " component creates a vertical stack of elements with proper spacing."),
    component_showcase(
        DivVStacked(
            Div("Top Item", cls="bg-yellow-100 dark:bg-yellow-900 p-4 rounded-lg text-center font-bold w-full"),
            Div("Middle Item", cls="bg-yellow-200 dark:bg-yellow-800 p-4 rounded-lg text-center font-bold w-full"),
            Div("Bottom Item", cls="bg-yellow-300 dark:bg-yellow-700 p-4 rounded-lg text-center font-bold w-full"),
            cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4"
        ),
        code="""DivVStacked(
    Div("Top Item", cls="bg-yellow-100 dark:bg-yellow-900 p-4 rounded-lg text-center font-bold w-full"),
    Div("Middle Item", cls="bg-yellow-200 dark:bg-yellow-800 p-4 rounded-lg text-center font-bold w-full"),
    Div("Bottom Item", cls="bg-yellow-300 dark:bg-yellow-700 p-4 rounded-lg text-center font-bold w-full"),
    cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4"
)""",
        id="div-v-stacked"
    ),
    Br(),
    
    H3("DivCentered"),
    P("The ", Code("DivCentered"), " component centers its contents both horizontally and vertically. Use the ", Code("vstack"), " parameter to control direction."),
    component_showcase(
        Div(
            P("Vertical Stack (vstack=True):"),
            DivCentered(
                Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold w-32"),
                Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold w-32"),
                Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold w-32"),
                cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-64 gap-4"
            ),
            Br(),
            P("Horizontal Stack (vstack=False):"),
            DivCentered(
                Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
                Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold"),
                Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold"),
                vstack=False,
                cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-32 gap-4"
            )
        ),
        code="""# Vertical Stack (Default)
DivCentered(
    Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold w-32"),
    Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold w-32"),
    Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold w-32"),
    cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-64 gap-4"
)

# Horizontal Stack
DivCentered(
    Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
    Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold"),
    Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold"),
    vstack=False,
    cls="p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-32 gap-4"
)""",
        id="div-centered"
    ),
    Br(),
    
    H2("Grid Layout", link=True),
    P("The ", Code("Grid"), " component creates responsive grid layouts that automatically adjust based on screen size."),
    component_showcase(
        Grid(
            Div("Item 1", cls="bg-blue-100 dark:bg-blue-900 p-6 rounded-lg text-center font-bold"),
            Div("Item 2", cls="bg-blue-200 dark:bg-blue-800 p-6 rounded-lg text-center font-bold"),
            Div("Item 3", cls="bg-blue-300 dark:bg-blue-700 p-6 rounded-lg text-center font-bold"),
            Div("Item 4", cls="bg-blue-400 dark:bg-blue-600 p-6 rounded-lg text-center font-bold"),
            Div("Item 5", cls="bg-blue-500 dark:bg-blue-500 p-6 rounded-lg text-center font-bold"),
            Div("Item 6", cls="bg-blue-600 dark:bg-blue-400 p-6 rounded-lg text-center font-bold"),
            cls="gap-4"
        ),
        code="""Grid(
    Div("Item 1", cls="bg-blue-100 dark:bg-blue-900 p-6 rounded-lg text-center font-bold"),
    Div("Item 2", cls="bg-blue-200 dark:bg-blue-800 p-6 rounded-lg text-center font-bold"),
    Div("Item 3", cls="bg-blue-300 dark:bg-blue-700 p-6 rounded-lg text-center font-bold"),
    Div("Item 4", cls="bg-blue-400 dark:bg-blue-600 p-6 rounded-lg text-center font-bold"),
    Div("Item 5", cls="bg-blue-500 dark:bg-blue-500 p-6 rounded-lg text-center font-bold"),
    Div("Item 6", cls="bg-blue-600 dark:bg-blue-400 p-6 rounded-lg text-center font-bold"),
    cls="gap-4"
)""",
        id="basic-grid"
    ),
    Br(),
    
    H3("Fixed Column Grid"),
    P("Specify a fixed number of columns with the ", Code("cols"), " parameter."),
    component_showcase(
        Grid(
            Div("Column 1", cls="bg-green-100 dark:bg-green-900 p-6 rounded-lg text-center font-bold"),
            Div("Column 2", cls="bg-green-200 dark:bg-green-800 p-6 rounded-lg text-center font-bold"),
            Div("Column 3", cls="bg-green-300 dark:bg-green-700 p-6 rounded-lg text-center font-bold"),
            cols=3,  # Always display 3 columns
            cls="gap-4"
        ),
        code="""Grid(
    Div("Column 1", cls="bg-green-100 dark:bg-green-900 p-6 rounded-lg text-center font-bold"),
    Div("Column 2", cls="bg-green-200 dark:bg-green-800 p-6 rounded-lg text-center font-bold"),
    Div("Column 3", cls="bg-green-300 dark:bg-green-700 p-6 rounded-lg text-center font-bold"),
    cols=3,  # Always display 3 columns
    cls="gap-4"
)""",
        id="fixed-column-grid"
    ),
    Br(),
    
    H3("Responsive Grid"),
    P("Control the number of columns at different breakpoints for fully responsive layouts."),
    component_showcase(
        Grid(
            Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-6 rounded-lg text-center font-bold"),
            Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-6 rounded-lg text-center font-bold"),
            Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-6 rounded-lg text-center font-bold"),
            Div("Item 4", cls="bg-purple-400 dark:bg-purple-600 p-6 rounded-lg text-center font-bold"),
            cols_min=1,  # 1 column on extra small screens
            cols_sm=2,   # 2 columns on small screens
            cols_md=2,   # 2 columns on medium screens
            cols_lg=4,   # 4 columns on large screens
            cls="gap-4"
        ),
        code="""Grid(
    Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-6 rounded-lg text-center font-bold"),
    Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-6 rounded-lg text-center font-bold"),
    Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-6 rounded-lg text-center font-bold"),
    Div("Item 4", cls="bg-purple-400 dark:bg-purple-600 p-6 rounded-lg text-center font-bold"),
    cols_min=1,  # 1 column on extra small screens
    cols_sm=2,   # 2 columns on small screens
    cols_md=2,   # 2 columns on medium screens
    cols_lg=4,   # 4 columns on large screens
    cls="gap-4"
)""",
        id="responsive-grid"
    ),
    Br(),

    # TODO Grid Layout Components
    # Section(        # Product Card Grid Example
    #     H3("Product Card Grid", cls=TextHeading.h3 + " mt-8 mb-2"),
    #     P("A practical example using Grid to display product cards.", cls=TextT.muted + " mb-4"),
        
    #     Container(
    #         Grid(
    #             # Product Card 1
    #             Div(
    #                 Div(cls="relative h-48 rounded-t-lg overflow-hidden",
    #                     style="background-image: url('https://flowbite.com/docs/images/blog/image-1.jpg'); background-size: cover; background-position: center;"),
    #                 Div(
    #                     H5("Product Title 1", cls=TextHeading.h5),
    #                     P("This is a product description. It showcases how to use Grid for product listings.", cls=TextT.muted + " mb-4"),
    #                     DivFullySpaced(
    #                         P("$29.99", cls=TextT.bold + TextT.lg),
    #                         Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
    #                     ),
    #                     cls="p-4"
    #                 ),
    #                 cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
    #             ),
                
    #             # Product Card 2
    #             Div(
    #                 Div(cls="relative h-48 rounded-t-lg overflow-hidden",
    #                     style="background-image: url('https://flowbite.com/docs/images/blog/image-2.jpg'); background-size: cover; background-position: center;"),
    #                 Div(
    #                     H5("Product Title 2", cls=TextHeading.h5),
    #                     P("Another product with a different image and price point.", cls=TextT.muted + " mb-4"),
    #                     DivFullySpaced(
    #                         P("$49.99", cls=TextT.bold + TextT.lg),
    #                         Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
    #                     ),
    #                     cls="p-4"
    #                 ),
    #                 cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
    #             ),
                
    #             # Product Card 3
    #             Div(
    #                 Div(cls="relative h-48 rounded-t-lg overflow-hidden",
    #                     style="background-image: url('https://flowbite.com/docs/images/blog/image-3.jpg'); background-size: cover; background-position: center;"),
    #                 Div(
    #                     H5("Product Title 3", cls=TextHeading.h5),
    #                     P("A third product showcasing the responsive grid layout.", cls=TextT.muted + " mb-4"),
    #                     DivFullySpaced(
    #                         P("$39.99", cls=TextT.bold + TextT.lg),
    #                         Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
    #                     ),
    #                     cls="p-4"
    #                 ),
    #                 cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
    #             ),
                
    #             # Product Card 4
    #             Div(
    #                 Div(cls="relative h-48 rounded-t-lg overflow-hidden",
    #                     style="background-image: url('https://flowbite.com/docs/images/blog/image-4.jpg'); background-size: cover; background-position: center;"),
    #                 Div(
    #                     H5("Product Title 4", cls=TextHeading.h5),
    #                     P("A fourth product to fill out the grid on larger screens.", cls=TextT.muted + " mb-4"),
    #                     DivFullySpaced(
    #                         P("$59.99", cls=TextT.bold + TextT.lg),
    #                         Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
    #                     ),
    #                     cls="p-4"
    #                 ),
    #                 cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
    #             ),
                
    #             cols_min=1,  # 1 column on mobile
    #             cols_sm=2,   # 2 columns on small screens
    #             cols_lg=4,   # 4 columns on large screens
    #             cls="gap-6"  # Larger gap for product cards
    #         ),
    #         # size=ContainerSize.lg,
    #         cls="mb-8"
    #     ),
    #     cls="mb-12"
    # ),
) 