from fasthtml.common import Div, P, Html, Head, Body, Br, Code
from fastbite.all import *
from utils import component_showcase


def visual_components_showcase():
    """Page showcasing visual components including Icons, Avatars and Images"""
    
    return Container(
        H1("Visual Components Showcase",link=True, cls="mb-8 mt-6"),
        
        P("This showcase provides examples of visual components available in the Fastbite library. You'll find reusable UI elements including icons, avatars, and image placeholders that can be customized to fit your application needs. Each component is demonstrated with different configurations and includes code examples for implementation.", cls="mb-6"),
        
        # Icons section
        H2("Icon Component", link=True, cls="mb-4 mt-10"),
        icons_section(),
        
        # Avatars section
        H2("DiceBear Avatars", link=True, cls="mb-4 mt-10"),
        avatars_section(),
        
        # Images section
        H2("PicSum Image Gallery", link=True, cls="mb-4 mt-10"),
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
        H3("Basic Icon Examples", link=True, cls="mb-3"),
        P("The ", Code("Icon"), " component renders Lucide icons with various customization options:"),
        
        # Basic icons
        component_showcase(
            Div(
                Grid(*[Icon(icon) for icon in icon_names[:12]], cols=4)
            ),
            code="""# Import at the top of your file
from fastbite.all import Icon, Grid

# Basic icons in a 4-column grid
icon_names = ["house", "settings", "user", "mail", 
              "heart", "star", "bell", "calendar", 
              "check", "x", "alert-circle", "search"]

Grid(*[Icon(icon) for icon in icon_names], cols=4)""",
            id="basic-icons"
        ),
        
        Br(),
        
        # Different sizes
        H3("Different Sizes", link=True, cls="mb-3"),
        P("The ", Code("Icon"), " component supports different sizes via ", Code("height"), " and ", Code("width"), " parameters:"),
        component_showcase(
            Div(
                DivHStacked(
                    Icon("house", height=16, width=16),
                    Icon("house", height=24, width=24),
                    Icon("house", height=32, width=32),
                    Icon("house", height=48, width=48),
                    Icon("house", height=64, width=64),
                )
            ),
            code="""# Icons with different sizes
DivHStacked(
    Icon("house", height=16, width=16),
    Icon("house", height=24, width=24),
    Icon("house", height=32, width=32),
    Icon("house", height=48, width=48),
    Icon("house", height=64, width=64),
)""",
            id="icon-sizes"
        ),
        
        Br(),
        
        # Different stroke-widths
        H3("Different Stroke Widths", link=True, cls="mb-3"),
        P("Control the stroke width of icons using the ", Code("stroke_width"), " parameter:"),
        component_showcase(
            Div(
                DivHStacked(
                    Icon("circle", stroke_width=1),
                    Icon("circle", stroke_width=1.5),
                    Icon("circle", stroke_width=2),
                    Icon("circle", stroke_width=2.5),
                    Icon("circle", stroke_width=3),
                )
            ),
            code="""# Icons with different stroke widths
DivHStacked(
    Icon("circle", stroke_width=1),
    Icon("circle", stroke_width=1.5),
    Icon("circle", stroke_width=2),
    Icon("circle", stroke_width=2.5),
    Icon("circle", stroke_width=3),
)""",
            id="icon-stroke-widths"
        ),
        
        Br(),
        
        # Icons in buttons
        H3("Icons in Buttons", link=True, cls="mb-3"),
        P("Icons can be combined with other components like ", Code("Button"), ":"),
        component_showcase(
            Div(
                DivHStacked(
                    Button(Icon("plus", height=16, width=16, cls="mr-2"), " Add New"),
                    Button(Icon("trash", height=16, width=16, cls="mr-2"), " Delete", cls=ButtonT.error),
                    Button(Icon("save", height=16, width=16, cls="mr-2"), " Save", cls=ButtonT.success),
                    Button(Icon("download", height=16, width=16, cls="mr-2"), " Download", cls=ButtonT.info),
                )
            ),
            code="""# Icons in buttons with different styles
DivHStacked(
    Button(Icon("plus", height=16, width=16, cls="mr-2"), " Add New"),
    Button(Icon("trash", height=16, width=16, cls="mr-2"), " Delete", cls=ButtonT.error),
    Button(Icon("save", height=16, width=16, cls="mr-2"), " Save", cls=ButtonT.success),
    Button(Icon("download", height=16, width=16, cls="mr-2"), " Download", cls=ButtonT.info),
)""",
            id="icon-buttons"
        ),
    )

def avatars_section():
    """Create the avatars showcase section"""
    
    names = ["Alex Smith", "Jamie Brown", "Taylor Jones", "Morgan Lee", 
             "Riley Kim", "Sam Wilson", "Jordan Davis", "Casey Miller"]
    
    return Div(
        H3("Avatar Sizes", link=True, cls="mb-3"),
        P("The ", Code("DiceBearAvatar"), " component generates consistent avatars from seed names:"),
        
        # Size comparison
        component_showcase(
            Div(
                DivHStacked(
                    DiceBearAvatar("User", h=10, w=10),
                    DiceBearAvatar("User", h=12, w=12),
                    DiceBearAvatar("User", h=16, w=16),
                    DiceBearAvatar("User", h=20, w=20),
                    DiceBearAvatar("User", h=24, w=24)
                )
            ),
            code="""# Import at the top of your file
from fastbite.all import DiceBearAvatar, DivHStacked

# Avatars in different sizes
DivHStacked(
    DiceBearAvatar("User", h=10, w=10),
    DiceBearAvatar("User", h=12, w=12),
    DiceBearAvatar("User", h=16, w=16),
    DiceBearAvatar("User", h=20, w=20),
    DiceBearAvatar("User", h=24, w=24)
)""",
            id="avatar-sizes"
        ),
        
        Br(),
        
        # Different seeds
        H3("Different Avatar Seeds", link=True, cls="mb-3"),
        P("Using different name seeds generates unique but consistent avatars:"),
        component_showcase(
            Div(
                Grid(*[
                    DivVStacked(
                        DiceBearAvatar(name, h=16, w=16),
                        P(name, cls=TextT.center)
                    ) 
                    for name in names
                ], cols=4)
            ),
            code="""# Avatars with different name seeds
names = ["Alex Smith", "Jamie Brown", "Taylor Jones", "Morgan Lee", 
         "Riley Kim", "Sam Wilson", "Jordan Davis", "Casey Miller"]

Grid(*[
    DivVStacked(
        DiceBearAvatar(name, h=16, w=16),
        P(name, cls=TextT.center)
    ) 
    for name in names
], cols=4)""",
            id="avatar-seeds"
        ),
    )

def images_section():
    """Create the PicSum images showcase section"""
    
    return Div(
        H3("Random Images", link=True, cls="mb-3"),
        P("The ", Code("PicSumImg"), " component provides beautiful placeholder images with various options:"),
        
        # Basic random images
        component_showcase(
            Div(
                Grid(
                    PicSumImg(h=200, w=300),
                    PicSumImg(h=200, w=300),
                    PicSumImg(h=200, w=300),
                    PicSumImg(h=200, w=300),
                    cls="gap-6"
                )
            ),
            code="""# Import at the top of your file
from fastbite.all import PicSumImg, Grid

# Random placeholder images
Grid(
    PicSumImg(h=200, w=300),
    PicSumImg(h=200, w=300),
    PicSumImg(h=200, w=300),
    PicSumImg(h=200, w=300),
    cls="gap-6"
)""",
            id="random-images"
        ),
        
        Br(),
        
        # Specific image IDs
        H3("Specific Image IDs", link=True, cls="mb-3"),
        P("Use the ", Code("id"), " parameter to consistently get the same image:"),
        component_showcase(
            Div(
                Grid(
                    PicSumImg(h=200, w=300, id=237),
                    PicSumImg(h=200, w=300, id=42),
                    PicSumImg(h=200, w=300, id=1084),
                    cls="gap-6"
                )
            ),
            code="""# Images with specific IDs
Grid(
    PicSumImg(h=200, w=300, id=237),  # Dog image
    PicSumImg(h=200, w=300, id=42),   # Forest image
    PicSumImg(h=200, w=300, id=1084), # Walrus image
    cls="gap-6"
)""",
            id="specific-images"
        ),
        
        Br(),
        
        # Image effects
        H3("Image Effects", link=True, cls="mb-3"),
        P("Apply effects with ", Code("grayscale"), " and ", Code("blur"), " parameters:"),
        component_showcase(
            Div(
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
                )
            ),
            code="""# Image effects: grayscale and blur
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
)""",
            id="image-effects"
        ),
        
        Br(),
        
        # Different sizes
        H3("Different Sizes", link=True, cls="mb-3"),
        P("Control image dimensions with ", Code("h"), " and ", Code("w"), " parameters:"),
        component_showcase(
            Div(
                DivHStacked(
                    PicSumImg(h=100, w=100, id=1),
                    PicSumImg(h=150, w=150, id=1),
                    PicSumImg(h=200, w=200, id=1),
                    cls="gap-4"
                )
            ),
            code="""# Images with different sizes
DivHStacked(
    PicSumImg(h=100, w=100, id=1),
    PicSumImg(h=150, w=150, id=1),
    PicSumImg(h=200, w=200, id=1),
    cls="gap-4"
)""",
            id="image-sizes"
        ),
    )

# Uncomment and enhance when needed
# def practical_examples_section():
#     """Create practical examples of combining the components"""
#     
#     return Div(
#         P("Here are some practical examples of how these components can be used together:"),
#         
#         # Examples would go here following component_showcase pattern
#     )

icons_images = visual_components_showcase()