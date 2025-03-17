from fasthtml.common import *
from fh_flowbite.components import *

containers = Div(
    H1("Container Examples", cls=TextHeading.h1),
    P("This page demonstrates the various container types available in Flowbite.", cls=TextT.muted + TextT.lg + " mb-4"),
    
    # Default container
    Section(
        H2("Default Container", cls=TextHeading.h2),
        P("The default container is responsive and centers content with padding on the sides.", cls=TextT.muted + " mb-4"),
        Container(
            Div("Default Container", cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
            cls="mb-4"
        ),
        cls="mb-12"
    ),
    
    # Fixed-width containers
    Section(
        H2("Fixed-Width Containers", cls=TextHeading.h2),
        P("These containers have fixed widths based on Flowbite's container size variables.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div("XXS Container (16rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._3xs,
            cls="mb-4"
        ),
        Container(
            Div("XXS Container (18rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._2xs,
            cls="mb-4"
        ),
        
        Container(
            Div("XS Container (20rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.xs,
            cls="mb-4"
        ),
        
        Container(
            Div("SM Container (24rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.sm,
            cls="mb-4"
        ),
        
        Container(
            Div("MD Container (28rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.md,
            cls="mb-4"
        ),
        
        Container(
            Div("LG Container (32rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.lg,
            cls="mb-4"
        ),
        
        Container(
            Div("XL Container (36rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.xl,
            cls="mb-4"
        ),
        
        Container(
            Div("2XL Container (42rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._2xl,
            cls="mb-4"
        ),
        
        Container(
            Div("3XL Container (48rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._3xl,
            cls="mb-4"
        ),
        
        Container(
            Div("4XL Container (56rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._4xl,
            cls="mb-4"
        ),

        Container(
            Div("5XL Container (64rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._5xl,
            cls="mb-4"
        ),

        Container(
            Div("6XL Container (72rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._6xl,
            cls="mb-4"
        ),

        Container(
            Div("7XL Container (80rem)", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize._7xl,
            cls="mb-4"
        ),
        
        cls="mb-12"
    ),
    
    # Special containers
    Section(
        H2("Special Containers", cls=TextHeading.h2),
        P("Special container types for different use cases.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div("Fluid Container (Full Width)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.fluid,
            cls="mb-4"
        ),
        
        Container(
            Div("Responsive Container (Adapts to screen size)", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold"),
            size=ContainerSize.responsive,
            cls="mb-4"
        ),
        
        cls="mb-12"
    ),
    
    # Container with FlexT layouts
    Section(
        H2("Flexbox Container Layouts", cls=TextHeading.h2),
        P("Containers combined with flexbox layouts for various use cases.", cls=TextT.muted + " mb-4"),
        
        # Row containers
        H3("Row Layout Containers", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Containers that arrange children in a row (horizontal layout).", cls=TextT.muted + " mb-4"),
        
        Container(
            Container("Item 1", size=ContainerSize.fluid, cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
            Container("Item 2", size=ContainerSize.fluid, cls="bg-blue-200 dark:bg-blue-800 p-4 rounded-lg text-center font-bold"),
            Container("Item 3", size=ContainerSize.fluid, cls="bg-blue-300 dark:bg-blue-700 p-4 rounded-lg text-center font-bold"),
            cls=(FlexT.block,FlexT.row,"mb-6 gap-4")
        ),
        
        H3("Column Layout Containers", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Containers that arrange children in a column (vertical layout).", cls=TextT.muted + " mb-4"),
        
        Container(
            Container("Item 1", size=ContainerSize.fluid, cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
            Container("Item 2", size=ContainerSize.fluid, cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
            Container("Item 3", size=ContainerSize.fluid, cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),            
            cls=(FlexT.block,FlexT.column,"mb-6 gap-4")
        ),
        
        H3("Centered Content Container", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Container that centers its content both horizontally and vertically.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div("Centered Content", cls="bg-purple-200 dark:bg-purple-800 p-8 rounded-lg text-center font-bold"),
            cls=(FlexT.block,FlexT.center,FlexT.middle,"mb-6 h-48 bg-gray-100 dark:bg-gray-700 rounded-lg p-4")
        ),
        
        H3("Content Justification", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Containers with different horizontal content alignment.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
            Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
            Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
            cls=(FlexT.block,FlexT.between,"mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
        ),
        Container(
            Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
            Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
            Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
            cls=(FlexT.block,FlexT.left,"mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
        ),
        Container(
            Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
            Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
            Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
            cls=(FlexT.block,FlexT.right,"mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
        ),
        Container(
            Div("Start", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold w-24"),
            Div("Middle", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold w-24"),
            Div("End", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold w-24"),
            cls=(FlexT.block,FlexT.center,"mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg gap-4")
        ),

        cls="mb-12"
    ),
    
    # Predefined Div Components
    Section(
        H2("Predefined Div Components", cls=TextHeading.h2),
        P("Ready-to-use div components with predefined layouts and alignments.", cls=TextT.muted + " mb-4"),
        
        # DivFullySpaced
        H3("DivFullySpaced", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A flex div with components having maximum space between them.", cls=TextT.muted + " mb-4"),
        
        DivFullySpaced(
            Div("Left Item", cls="bg-blue-100 dark:bg-blue-900 p-4 rounded-lg text-center font-bold"),
            Div("Center Item", cls="bg-blue-200 dark:bg-blue-800 p-4 rounded-lg text-center font-bold"),
            Div("Right Item", cls="bg-blue-300 dark:bg-blue-700 p-4 rounded-lg text-center font-bold"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg"
        ),
        
        # DivCentered
        H3("DivCentered", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A flex div with components centered both horizontally and vertically.", cls=TextT.muted + " mb-4"),
        
        P("Vertical Stack (Default):", cls=TextT.muted + " mb-2"),
        DivCentered(
            Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold w-32"),
            Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold w-32"),
            Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold w-32"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-64 space-y-4"
        ),
        
        P("Horizontal Stack:", cls=TextT.muted + " mb-2"),
        DivCentered(
            Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-4 rounded-lg text-center font-bold"),
            Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-4 rounded-lg text-center font-bold"),
            Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-4 rounded-lg text-center font-bold"),
            vstack=False,
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg h-32 space-x-4"
        ),
        
        # DivLAligned
        H3("DivLAligned", cls=TextHeading.h3 + "mt-8 mb-2"),
        P("A flex div with components aligned to the left.", cls=TextT.muted + " mb-4"),
        
        DivLAligned(
            Div("Left", cls="bg-green-100 dark:bg-green-900 p-4 rounded-lg text-center font-bold w-20"),
            Div("Aligned", cls="bg-green-200 dark:bg-green-800 p-4 rounded-lg text-center font-bold w-20"),
            Div("Items", cls="bg-green-300 dark:bg-green-700 p-4 rounded-lg text-center font-bold w-20"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg space-x-4"
        ),
        
        # DivRAligned
        H3("DivRAligned", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A flex div with components aligned to the right.", cls=TextT.muted + " mb-4"),
        
        DivRAligned(
            Div("Right", cls="bg-red-100 dark:bg-red-900 p-4 rounded-lg text-center font-bold w-20"),
            Div("Aligned", cls="bg-red-200 dark:bg-red-800 p-4 rounded-lg text-center font-bold w-20"),
            Div("Items", cls="bg-red-300 dark:bg-red-700 p-4 rounded-lg text-center font-bold w-20"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg space-x-4"
        ),
        
        # DivVStacked
        H3("DivVStacked", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A flex div with components stacked vertically.", cls=TextT.muted + " mb-4"),
        
        DivVStacked(
            Div("Top Item", cls="bg-yellow-100 dark:bg-yellow-900 p-4 rounded-lg text-center font-bold w-full"),
            Div("Middle Item", cls="bg-yellow-200 dark:bg-yellow-800 p-4 rounded-lg text-center font-bold w-full"),
            Div("Bottom Item", cls="bg-yellow-300 dark:bg-yellow-700 p-4 rounded-lg text-center font-bold w-full"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg space-y-4"
        ),
        
        # DivHStacked
        H3("DivHStacked", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A flex div with components stacked horizontally.", cls=TextT.muted + " mb-4"),
        
        DivHStacked(
            Div("Left Item", cls="bg-indigo-100 dark:bg-indigo-900 p-4 rounded-lg text-center font-bold"),
            Div("Middle Item", cls="bg-indigo-200 dark:bg-indigo-800 p-4 rounded-lg text-center font-bold"),
            Div("Right Item", cls="bg-indigo-300 dark:bg-indigo-700 p-4 rounded-lg text-center font-bold"),
            cls="mb-6 p-4 bg-gray-100 dark:bg-gray-700 rounded-lg space-x-4"
        ),
        
        # Comparison Section
        H3("Comparison Example", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A practical example comparing different layout components.", cls=TextT.muted + " mb-4"),                
        
        cls="mb-12"
    ),

    # Grid Layout Components
    Section(
        H2("Grid Layout Components"),
        P("Responsive CSS Grid layouts with automatic column sizing and breakpoints.", cls=TextT.muted + " mb-4"),
        
        # Basic Grid Example
        H3("Basic Responsive Grid", cls=" mt-8 mb-2"),
        P("A grid that automatically adjusts the number of columns based on screen size and content.", cls=TextT.muted + " mb-4"),
        
        Container(
            Grid(
                Div("Item 1", cls="bg-blue-100 dark:bg-blue-900 p-6 rounded-lg text-center font-bold"),
                Div("Item 2", cls="bg-blue-200 dark:bg-blue-800 p-6 rounded-lg text-center font-bold"),
                Div("Item 3", cls="bg-blue-300 dark:bg-blue-700 p-6 rounded-lg text-center font-bold"),
                Div("Item 4", cls="bg-blue-400 dark:bg-blue-600 p-6 rounded-lg text-center font-bold"),
                Div("Item 5", cls="bg-blue-500 dark:bg-blue-500 p-6 rounded-lg text-center font-bold"),
                Div("Item 6", cls="bg-blue-600 dark:bg-blue-400 p-6 rounded-lg text-center font-bold"),
                cls="mb-6 gap-4"
            ),
            size=ContainerSize.fluid,
            cls="mb-8"
        ),
        
        # Fixed Column Grid
        H3("Fixed Column Grid", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A grid with a fixed number of columns across all screen sizes.", cls=TextT.muted + " mb-4"),
        
        Container(
            Grid(
                Div("Column 1", cls="bg-green-100 dark:bg-green-900 p-6 rounded-lg text-center font-bold"),
                Div("Column 2", cls="bg-green-200 dark:bg-green-800 p-6 rounded-lg text-center font-bold"),
                Div("Column 3", cls="bg-green-300 dark:bg-green-700 p-6 rounded-lg text-center font-bold"),
                cols=3,  # Always display 3 columns regardless of screen size
                cls="mb-6 gap-4"
            ),
            size=ContainerSize.fluid,
            cls="mb-8"
        ),
        
        # Custom Responsive Grid
        H3("Custom Responsive Grid", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A grid with custom column configurations for different screen sizes.", cls=TextT.muted + " mb-4"),
        
        Container(
            Grid(
                Div("Item 1", cls="bg-purple-100 dark:bg-purple-900 p-6 rounded-lg text-center font-bold"),
                Div("Item 2", cls="bg-purple-200 dark:bg-purple-800 p-6 rounded-lg text-center font-bold"),
                Div("Item 3", cls="bg-purple-300 dark:bg-purple-700 p-6 rounded-lg text-center font-bold"),
                Div("Item 4", cls="bg-purple-400 dark:bg-purple-600 p-6 rounded-lg text-center font-bold"),
                Div("Item 5", cls="bg-purple-500 dark:bg-purple-500 p-6 rounded-lg text-center font-bold"),
                Div("Item 6", cls="bg-purple-600 dark:bg-purple-400 p-6 rounded-lg text-center font-bold"),
                cols_min=1,  # 1 column on extra small screens
                cols_sm=2,   # 2 columns on small screens
                cols_md=3,   # 3 columns on medium screens
                cols_lg=3,   # 3 columns on large screens
                cols_xl=6,   # 6 columns on extra large screens
                cls="mb-6 gap-4"
            ),
            size=ContainerSize.fluid,
            cls="mb-8"
        ),
        
        # Grid with Custom Gap
        H3("Grid with Custom Spacing", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Grids with different gap sizes between items.", cls=TextT.muted + " mb-4"),
        
        Container(
            DivVStacked(
                P("Small Gap (gap-2):", cls=TextT.muted + " mb-2"),
                Grid(
                    Div("1", cls="bg-red-100 dark:bg-red-900 p-4 rounded-lg text-center font-bold"),
                    Div("2", cls="bg-red-200 dark:bg-red-800 p-4 rounded-lg text-center font-bold"),
                    Div("3", cls="bg-red-300 dark:bg-red-700 p-4 rounded-lg text-center font-bold"),
                    Div("4", cls="bg-red-400 dark:bg-red-600 p-4 rounded-lg text-center font-bold"),
                    cols=4,
                    cls="gap-2 mb-6"  # Small gap
                ),
                
                P("Medium Gap (gap-4, default):", cls=TextT.muted + " mb-2"),
                Grid(
                    Div("1", cls="bg-amber-100 dark:bg-amber-900 p-4 rounded-lg text-center font-bold"),
                    Div("2", cls="bg-amber-200 dark:bg-amber-800 p-4 rounded-lg text-center font-bold"),
                    Div("3", cls="bg-amber-300 dark:bg-amber-700 p-4 rounded-lg text-center font-bold"),
                    Div("4", cls="bg-amber-400 dark:bg-amber-600 p-4 rounded-lg text-center font-bold"),
                    cols=4,
                    cls="gap-4 mb-6"  # Medium gap (default)
                ),
                
                P("Large Gap (gap-8):", cls=TextT.muted + " mb-2"),
                Grid(
                    Div("1", cls="bg-teal-100 dark:bg-teal-900 p-4 rounded-lg text-center font-bold"),
                    Div("2", cls="bg-teal-200 dark:bg-teal-800 p-4 rounded-lg text-center font-bold"),
                    Div("3", cls="bg-teal-300 dark:bg-teal-700 p-4 rounded-lg text-center font-bold"),
                    Div("4", cls="bg-teal-400 dark:bg-teal-600 p-4 rounded-lg text-center font-bold"),
                    cols=4,
                    cls="gap-8 mb-6"  # Large gap
                ),
                
                P("Row and Column Gap (gap-x-8 gap-y-4):", cls=TextT.muted + " mb-2"),
                Grid(
                    Div("1", cls="bg-cyan-100 dark:bg-cyan-900 p-4 rounded-lg text-center font-bold"),
                    Div("2", cls="bg-cyan-200 dark:bg-cyan-800 p-4 rounded-lg text-center font-bold"),
                    Div("3", cls="bg-cyan-300 dark:bg-cyan-700 p-4 rounded-lg text-center font-bold"),
                    Div("4", cls="bg-cyan-400 dark:bg-cyan-600 p-4 rounded-lg text-center font-bold"),
                    Div("5", cls="bg-cyan-500 dark:bg-cyan-500 p-4 rounded-lg text-center font-bold"),
                    Div("6", cls="bg-cyan-600 dark:bg-cyan-400 p-4 rounded-lg text-center font-bold"),
                    Div("7", cls="bg-cyan-700 dark:bg-cyan-300 p-4 rounded-lg text-center font-bold"),
                    Div("8", cls="bg-cyan-800 dark:bg-cyan-200 p-4 rounded-lg text-center font-bold"),
                    cols=4,
                    cls="gap-x-8 gap-y-4 mb-6"  # Different horizontal and vertical gaps
                ),
            ),
            size=ContainerSize.fluid,
            cls="mb-8"
        ),
        
        # Product Card Grid Example
        H3("Product Card Grid", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("A practical example using Grid to display product cards.", cls=TextT.muted + " mb-4"),
        
        Container(
            Grid(
                # Product Card 1
                Div(
                    Div(cls="relative h-48 rounded-t-lg overflow-hidden",
                        style="background-image: url('https://flowbite.com/docs/images/blog/image-1.jpg'); background-size: cover; background-position: center;"),
                    Div(
                        H5("Product Title 1", cls=TextHeading.h5),
                        P("This is a product description. It showcases how to use Grid for product listings.", cls=TextT.muted + " mb-4"),
                        DivFullySpaced(
                            P("$29.99", cls=TextT.bold + TextT.lg),
                            Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
                        ),
                        cls="p-4"
                    ),
                    cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
                ),
                
                # Product Card 2
                Div(
                    Div(cls="relative h-48 rounded-t-lg overflow-hidden",
                        style="background-image: url('https://flowbite.com/docs/images/blog/image-2.jpg'); background-size: cover; background-position: center;"),
                    Div(
                        H5("Product Title 2", cls=TextHeading.h5),
                        P("Another product with a different image and price point.", cls=TextT.muted + " mb-4"),
                        DivFullySpaced(
                            P("$49.99", cls=TextT.bold + TextT.lg),
                            Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
                        ),
                        cls="p-4"
                    ),
                    cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
                ),
                
                # Product Card 3
                Div(
                    Div(cls="relative h-48 rounded-t-lg overflow-hidden",
                        style="background-image: url('https://flowbite.com/docs/images/blog/image-3.jpg'); background-size: cover; background-position: center;"),
                    Div(
                        H5("Product Title 3", cls=TextHeading.h5),
                        P("A third product showcasing the responsive grid layout.", cls=TextT.muted + " mb-4"),
                        DivFullySpaced(
                            P("$39.99", cls=TextT.bold + TextT.lg),
                            Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
                        ),
                        cls="p-4"
                    ),
                    cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
                ),
                
                # Product Card 4
                Div(
                    Div(cls="relative h-48 rounded-t-lg overflow-hidden",
                        style="background-image: url('https://flowbite.com/docs/images/blog/image-4.jpg'); background-size: cover; background-position: center;"),
                    Div(
                        H5("Product Title 4", cls=TextHeading.h5),
                        P("A fourth product to fill out the grid on larger screens.", cls=TextT.muted + " mb-4"),
                        DivFullySpaced(
                            P("$59.99", cls=TextT.bold + TextT.lg),
                            Button("Add to Cart", size=ButtonSize.sm, cls=ButtonT.primary),
                        ),
                        cls="p-4"
                    ),
                    cls="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden"
                ),
                
                cols_min=1,  # 1 column on mobile
                cols_sm=2,   # 2 columns on small screens
                cols_lg=4,   # 4 columns on large screens
                cls="gap-6"  # Larger gap for product cards
            ),
            # size=ContainerSize.lg,
            cls="mb-8"
        ),
        cls="mb-12"
    ),
) 