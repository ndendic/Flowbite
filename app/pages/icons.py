from fasthtml.common import Div, P, Html, Head, Body
from fastbite import *

def visual_components_showcase():
    """Page showcasing visual components including Icons, Avatars and Images"""
    
    return Container(
        H1("Visual Components Showcase", cls="mb-8 mt-6"),
        
        # Icons section
        H2("Icon Component", cls="mb-4 mt-10"),
        icons_section(),
        
        # Avatars section
        H2("DiceBear Avatars", cls="mb-4 mt-10"),
        avatars_section(),
        
        # Images section
        H2("PicSum Image Gallery", cls="mb-4 mt-10"),
        images_section(),
        
        # # Practical examples section
        # H2("Practical Examples", cls="mb-4 mt-10"),
        # practical_examples_section(),
    )

def icons_section():
    """Create the icons showcase section"""
    
    icon_names = ["house", "settings", "user", "mail", "heart", "star", 
                  "bell", "calendar", "check", "x", "alert-circle", "search"]
    
    return Div(
        P("A collection of Lucide icons in various sizes and styles:", cls=TextT.lg),
        
        # Basic icons in a grid
        H3("Basic Icon Examples", cls="mt-6 mb-3"),
        Grid(*[Icon(icon) for icon in icon_names[:12]], cols=4),
        
        # Different sizes
        H3("Different Sizes", cls="mt-6 mb-3"),
        DivHStacked(
            Icon("house", height=16, width=16),
            Icon("house", height=24, width=24),
            Icon("house", height=32, width=32),
            Icon("house", height=48, width=48),
            Icon("house", height=64, width=64),
        ),
        
        # Different stroke-widths
        H3("Different Stroke Widths", cls="mt-6 mb-3"),
        DivHStacked(
            Icon("circle", stroke_width=1),
            Icon("circle", stroke_width=1.5),
            Icon("circle", stroke_width=2),
            Icon("circle", stroke_width=2.5),
            Icon("circle", stroke_width=3),
        ),
        
        # Common icon use cases
        H3("Icons in Buttons", cls="mt-6 mb-3"),
        DivHStacked(
            Button(Icon("plus", height=16, width=16, cls="mr-2"), " Add New"),
            Button(Icon("trash", height=16, width=16, cls="mr-2"), " Delete", cls=ButtonT.error),
            Button(Icon("save", height=16, width=16, cls="mr-2"), " Save", cls=ButtonT.success),
            Button(Icon("download", height=16, width=16, cls="mr-2"), " Download", cls=ButtonT.info),
        ),
    )

def avatars_section():
    """Create the avatars showcase section"""
    
    names = ["Alex Smith", "Jamie Brown", "Taylor Jones", "Morgan Lee", 
             "Riley Kim", "Sam Wilson", "Jordan Davis", "Casey Miller"]
    
    return Div(
        P("DiceBear generates consistent avatars from seed names:", cls=TextT.lg),
        
        # Size comparison
        H3("Avatar Sizes", cls="mt-6 mb-3"),
        DivHStacked(
            DiceBearAvatar("User", h=10, w=10),
            DiceBearAvatar("User", h=12, w=12),
            DiceBearAvatar("User", h=16, w=16),
            DiceBearAvatar("User", h=20, w=20),
            DiceBearAvatar("User", h=24, w=24)
        ),
        
        # Different seeds
        H3("Different Avatar Seeds", cls="mt-6 mb-3"),
        Grid(*[
            DivVStacked(
                DiceBearAvatar(name, h=16, w=16),
                P(name, cls=TextT.center)
            ) 
            for name in names
        ], cols=4),
    )

def images_section():
    """Create the PicSum images showcase section"""
    
    return Div(
        P("PicSum provides beautiful placeholder images with various options:", cls=TextT.lg),
        
        # Basic random images
        H3("Random Images", cls="mt-6 mb-3"),
        Grid(
            PicSumImg(h=200, w=300),
            PicSumImg(h=200, w=300),
            PicSumImg(h=200, w=300),
            PicSumImg(h=200, w=300),
            cls="gap-6"
        ),
        
        # Specific image IDs
        H3("Specific Image IDs", cls="mt-6 mb-3"),
        Grid(
            PicSumImg(h=200, w=300, id=237),
            PicSumImg(h=200, w=300, id=42),
            PicSumImg(h=200, w=300, id=1084),
            cls="gap-6"
        ),
        
        # Image effects
        H3("Image Effects", cls="mt-6 mb-3"),
        Grid(
            Div(
                PicSumImg(h=200, w=300, id=1005),
                P("Original", cls=TextT.center)
            ),
            Div(
                PicSumImg(h=200, w=300, id=1005, grayscale=True),
                P("Grayscale", cls=TextT.center)
            ),
            Div(
                PicSumImg(h=200, w=300, id=1005, blur=5),
                P("Blur = 5", cls=TextT.center)
            ),
            Div(
                PicSumImg(h=200, w=300, id=1005, grayscale=True, blur=5),
                P("Grayscale + Blur", cls=TextT.center)
            ),
            cls="gap-6"
        ),
        
        # Different sizes
        H3("Different Sizes", cls="mt-6 mb-3"),
        DivHStacked(
            PicSumImg(h=100, w=100, id=1),
            PicSumImg(h=150, w=150, id=1),
            PicSumImg(h=200, w=200, id=1),
            cls="gap-4"
        ),
    )

# TODO: enhance this section
def practical_examples_section():
    """Create practical examples of combining the components"""
    
    return Div(
        P("Here are some practical examples of how these components can be used together:", cls=TextT.lg),
        
        # User profile card
        H3("User Profile Card", cls="mt-6 mb-3"),
        Div(
            DivHStacked(
                DiceBearAvatar("John Doe", h=16, w=16),
                Div(
                    P("John Doe", cls=TextT.bold),
                    P("Software Developer", cls=TextT.muted+TextT.sm),
                ),
                cls="gap-3"
            ),
            P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
              cls="mt-3"),
            DivHStacked(
                Icon("mail", height=16, width=16),
                P("john.doe@example.com"),
                cls="mt-3 gap-2"
            ),
            DivHStacked(
                Icon("phone", height=16, width=16),
                P("(123) 456-7890"),
                cls="mt-1 gap-2"
            ),
            cls="p-4 border border-gray-200 rounded-lg dark:border-gray-700 w-full max-w-md"
        ),
        
        # Image gallery with controls
        H3("Image Gallery with Controls", cls="mt-6 mb-3"),
        Div(
            PicSumImg(h=300, w=500, id=1084, cls="rounded-lg"),
            DivHStacked(
                Button(Icon("arrow-left", height=16, width=16), cls=ButtonT.primary + " mt-2"),
                Button(Icon("heart", height=16, width=16), cls=ButtonT.secondary + " mt-2"),
                Button(Icon("download", height=16, width=16), cls=ButtonT.secondary + " mt-2"),
                Button(Icon("share", height=16, width=16), cls=ButtonT.secondary + " mt-2"),
                Button(Icon("arrow-right", height=16, width=16), cls=ButtonT.primary + " mt-2"),
                cls="justify-between w-full"
            ),
            cls="max-w-xl"
        ),
        
        # Dashboard card example
        H3("Dashboard Card", cls="mt-6 mb-3"),
        Div(
            DivHStacked(
                Icon("trending-up", height=24, width=24, cls="text-green-500"),
                P("Sales Statistics", cls=TextT.xl + " " + TextT.bold),
                cls="justify-between w-full"
            ),
            Div(
                P("Monthly Revenue", cls=TextPresets.muted_sm),
                P("$12,350", cls=TextT.bold + " " + TextT.xl),
                P(Icon("arrow-up", height=16, width=16, cls="inline text-green-500"), " 12% increase from last month", 
                  cls=TextT.success + " " + TextT.sm),
                cls="mt-4"
            ),
            Grid(
                PicSumImg(h=100, w=150, id=1005, grayscale=True),
                PicSumImg(h=100, w=150, id=1005, grayscale=True),
                cols=2,
                cls="mt-4 gap-2"
            ),
            cls="p-4 border border-gray-200 rounded-lg dark:border-gray-700 max-w-xl"
        ),
    )

icons_images = visual_components_showcase()