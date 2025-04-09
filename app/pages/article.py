from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

def article_showcase():
    """Page showcasing Article components"""
    
    return Container(
        H1("Article Components", link=True, cls="mb-8 mt-6"),
        
        P("This showcase provides examples of article components available in the Fastbite library. These components are designed for creating blog posts, news articles, and other text-heavy content with proper styling and organization.", cls="mb-6"),
        
        # Article Components section
        H2("Article Components", link=True, cls="mb-4 mt-10"),
        article_section(),
    )

def article_section():
    """Create the article components showcase section"""
    
    basic_article = Article(
        ArticleTitle("Getting Started with Fastbite", link=True),
        ArticleMeta("Posted on February 8, 2023 by John Doe"),
        P("Fastbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It provides a consistent and accessible set of components for building modern web applications."),
        P("This guide will help you get started with using Fastbite in your projects and explore its capabilities.")
    )
    
    article_with_figure = Article(
        ArticleTitle("Visual Design with Fastbite", link=True),
        ArticleMeta("Posted on March 15, 2023 by Jane Smith"),
        P("Fastbite provides a comprehensive set of visual design components that follow modern design principles and accessibility standards."),
        Figure(
            Img(src="https://picsum.photos/id/1005/800/400", alt="Person working on a laptop"),
            Figcaption("Designing with Fastbite components")
        ),
        P("The visual design system in Fastbite is built on a foundation of consistency, usability, and customization, making it easy to create beautiful interfaces.")
    )
    
    full_article = Article(
        ArticleTitle("Building Responsive Interfaces with Fastbite", link=True),
        ArticleMeta("Posted on April 22, 2023 by Alex Johnson • 5 min read"),
        P("Fastbite provides a comprehensive set of components designed to work across all device sizes and screen types, enabling you to build truly responsive interfaces with minimal effort.", cls="lead"),
        
        H2("Core Principles", link=True),
        P("The responsive design system in Fastbite is built on these core principles:"),
        Ul(
            Li(Strong("Mobile-first approach"), " - Design for smaller screens first, then enhance for larger ones"),
            Li(Strong("Flexible layouts"), " - Use flexible grid systems and containers"),
            Li(Strong("Responsive typography"), " - Text that scales appropriately across devices")
        ),
        
        H2("Responsive Components", link=True),
        P("All Fastbite components are designed to be responsive by default. For example:"),
        
        H3("Flexible Grids", link=True),
        P("The Grid component automatically adjusts based on screen size:"),
        P(Code("Grid(*items, cols=3)"), " - Creates a 3-column grid on desktop that stacks on mobile"),
        
        H3("Adaptive Navigation", link=True),
        P("Navigation components transform based on available space:"),
        P("Desktop: Full horizontal menu with dropdowns"),
        P("Mobile: Collapsed menu with hamburger icon"),
        
        H2("Best Practices", link=True),
        P("When building responsive interfaces with Fastbite:"),
        Ol(
            Li("Test on multiple device sizes throughout development"),
            Li("Use the built-in responsive utilities rather than custom CSS"),
            Li("Consider touch interactions for mobile users")
        ),
        
        P("By following these principles and leveraging Fastbite's responsive components, you can create interfaces that work beautifully across all devices and screen sizes.")
    )
    
    return Div(
        # Basic Article
        H3("Basic Article", link=True, cls="mb-3"),
        P("The ", Code("Article"), " component provides a semantic container for article content with appropriate styling. Use ", Code("ArticleTitle"), " for the article heading and ", Code("ArticleMeta"), " for publication details:"),
        
        component_showcase(
            Div(basic_article),
            code="""# Import at the top of your file
from fastbite.all import Article, ArticleTitle, ArticleMeta

# Basic article example
Article(
    ArticleTitle("Getting Started with Fastbite", link=True),
    ArticleMeta("Posted on February 8, 2023 by John Doe"),
    P("Fastbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It provides a consistent and accessible set of components for building modern web applications."),
    P("This guide will help you get started with using Fastbite in your projects and explore its capabilities.")
)""",
            id="basic-article"
        ),
        
        Br(),
        
        # Article with Figure
        H3("Article with Figure", link=True, cls="mb-3"),
        P("Articles can contain various elements including figures with images:"),
        
        component_showcase(
            Div(article_with_figure),
            code="""Article(
    ArticleTitle("Visual Design with Fastbite", link=True),
    ArticleMeta("Posted on March 15, 2023 by Jane Smith"),
    P("Fastbite provides a comprehensive set of visual design components that follow modern design principles and accessibility standards."),
    Figure(
        Img(src="https://picsum.photos/id/1005/800/400", alt="Person working on a laptop"),
        Figcaption("Designing with Fastbite components")
    ),
    P("The visual design system in Fastbite is built on a foundation of consistency, usability, and customization, making it easy to create beautiful interfaces.")
)""",
            id="article-with-figure"
        ),
        
        Br(),
        
        # Full Article Example
        H3("Complete Article", link=True, cls="mb-3"),
        P("A more complete article example with headings, lists, and formatted text:"),
        
        component_showcase(
            Div(full_article),
            code="""Article(
    ArticleTitle("Building Responsive Interfaces with Fastbite", link=True),
    ArticleMeta("Posted on April 22, 2023 by Alex Johnson • 5 min read"),
    P("Fastbite provides a comprehensive set of components designed to work across all device sizes and screen types, enabling you to build truly responsive interfaces with minimal effort.", cls="lead"),
    
    H2("Core Principles", link=True),
    P("The responsive design system in Fastbite is built on these core principles:"),
    Ul(
        Li(Strong("Mobile-first approach"), " - Design for smaller screens first, then enhance for larger ones"),
        Li(Strong("Flexible layouts"), " - Use flexible grid systems and containers"),
        Li(Strong("Responsive typography"), " - Text that scales appropriately across devices")
    ),
    
    H2("Responsive Components", link=True),
    P("All Fastbite components are designed to be responsive by default. For example:"),
    
    H3("Flexible Grids", link=True),
    P("The Grid component automatically adjusts based on screen size:"),
    P(Code("Grid(*items, cols=3)"), " - Creates a 3-column grid on desktop that stacks on mobile"),
    
    H3("Adaptive Navigation", link=True),
    P("Navigation components transform based on available space:"),
    P("Desktop: Full horizontal menu with dropdowns"),
    P("Mobile: Collapsed menu with hamburger icon"),
    
    H2("Best Practices", link=True),
    P("When building responsive interfaces with Fastbite:"),
    Ol(
        Li("Test on multiple device sizes throughout development"),
        Li("Use the built-in responsive utilities rather than custom CSS"),
        Li("Consider touch interactions for mobile users")
    ),
    
    P("By following these principles and leveraging Fastbite's responsive components, you can create interfaces that work beautifully across all devices and screen sizes.")
)""",
            id="complete-article"
        ),
        
        Br(),
        
        # Individual Components Section
        H3("Article Components", link=True, cls="mb-3"),
        P("The article system consists of three main components:"),
        
        # Article Component
        H4("Article", link=True, cls="mb-2"),
        P("The ", Code("Article"), " component is a semantic container for article content with appropriate styling:"),
        component_showcase(
            Div(
                Article(
                    P("This is content inside an Article component. It provides proper styling and semantic structure for article content.")
                )
            ),
            code="""# Main container for article content
Article(
    # Content elements go here
    P("This is content inside an Article component. It provides proper styling and semantic structure for article content.")
)""",
            id="article-component"
        ),
        
        Br(),
        
        # ArticleTitle Component
        H4("ArticleTitle", link=True, cls="mb-2"),
        P("The ", Code("ArticleTitle"), " component provides properly styled titles for articles:"),
        component_showcase(
            Div(
                ArticleTitle("This is an Article Title")
            ),
            code="""# Article title component
ArticleTitle("This is an Article Title")

# You can also add link=True for navigation purposes
ArticleTitle("This is an Article Title with Link", link=True)""",
            id="article-title-component"
        ),
        
        Br(),
        
        # ArticleMeta Component
        H4("ArticleMeta", link=True, cls="mb-2"),
        P("The ", Code("ArticleMeta"), " component displays metadata about the article such as publication date and author:"),
        component_showcase(
            Div(
                ArticleMeta("Posted on June 12, 2023 by Sam Wilson")
            ),
            code="""# Article metadata component
ArticleMeta("Posted on June 12, 2023 by Sam Wilson")

# Can include other elements
ArticleMeta(
    "Posted on June 12, 2023 by ",
    A("Sam Wilson", href="#author-profile")
)""",
            id="article-meta-component"
        )
    )

# Make the showcase available to the app
article_components = article_showcase() 