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

        H3("Responsive Grid Layout", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Container with a responsive grid that changes columns based on screen size.", cls=TextT.muted + " mb-4"),
        
        # TODO: Add responsive grid layout
        Container(
            Div("Card 1", cls="bg-pink-100 dark:bg-pink-900 p-8 rounded-lg text-center font-bold"),
            Div("Card 2", cls="bg-pink-200 dark:bg-pink-800 p-8 rounded-lg text-center font-bold"),
            Div("Card 3", cls="bg-pink-300 dark:bg-pink-700 p-8 rounded-lg text-center font-bold"),
            Div("Card 4", cls="bg-pink-400 dark:bg-pink-600 p-8 rounded-lg text-center font-bold"),
            Div("Card 5", cls="bg-pink-500 dark:bg-pink-500 p-8 rounded-lg text-center font-bold"),
            Div("Card 6", cls="bg-pink-600 dark:bg-pink-400 p-8 rounded-lg text-center font-bold"),
            cls="mb-6"
        ),
        
        H3("Card Container", cls=TextHeading.h3 + " mt-8 mb-2"),
        P("Flexible container for displaying card-like elements.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div(
                H4("Card Title 1", cls=TextHeading.h4), 
                P("Card content with some descriptive text.", cls="mb-4"),
                Button("Action", size=ButtonSize.sm, cls=ButtonT.primary),
                cls="bg-white dark:bg-gray-800 p-4 border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm"
            ),
            Div(
                H4("Card Title 2", cls=TextHeading.h4), 
                P("Another card with different content.", cls="mb-4"),
                Button("Action", size=ButtonSize.sm, cls=ButtonT.secondary),
                cls="bg-white dark:bg-gray-800 p-4 border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm"
            ),
            Div(
                H4("Card Title 3", cls=TextHeading.h4), 
                P("Third card with more example content.", cls="mb-4"),
                Button("Action", size=ButtonSize.sm, cls=ButtonT.success),
                cls="bg-white dark:bg-gray-800 p-4 border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm"
            ),
            cls=FlexT.wrap+"mb-12"
        ),
        
        cls="mb-12"
    ),
    
    # Custom container examples
    Section(
        H2("Custom Container Combinations", cls=TextHeading.h2),
        P("Examples of custom containers combining size and layout.", cls=TextT.muted + " mb-4"),
        
        Container(
            Div("Custom MD Container with Column Layout", cls="bg-orange-100 dark:bg-orange-900 p-4 rounded-lg text-center font-bold w-full"),
            Div("Second Item", cls="bg-orange-200 dark:bg-orange-800 p-4 rounded-lg text-center font-bold w-full"),
            Div("Third Item", cls="bg-orange-300 dark:bg-orange-700 p-4 rounded-lg text-center font-bold w-full"),
            cls=FlexT.block+"mb-6 gap-4"
        ),
        
        Container(
            Div("Custom XL Centered Content", cls="bg-cyan-200 dark:bg-cyan-800 p-8 rounded-lg text-center font-bold"),
            cls=FlexT.center+"mb-6 h-48 bg-gray-100 dark:bg-gray-700 rounded-lg"
        ),
        
        cls="mb-12"
    ),
) 