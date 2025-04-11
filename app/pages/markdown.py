from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase
from fastbite.all import render_md, render_md_article # Import specific functions

# --- Sample Markdown Content ---
SAMPLE_MD = """# Heading 1

This is a paragraph with **bold text**, *italic text*, and `inline code`.

## Heading 2

Here's a list:

*   Item 1
*   Item 2
    *   Sub-item 2.1

> Blockquote example.

### Heading 3

A code block:

```python
def hello():
    print("Hello, Fastbite!")
```

An ordered list:

1.  First item
2.  Second item

[This is a link](https://example.com)
"""

# --- render_md Section ---
def _render_md_section():
    return Section(
        H2("`render_md`", link=True, cls="mb-4 mt-10"),
        P("Renders Markdown content to HTML using Mistletoe and applies Tailwind classes based on a class map. By default, it uses ", Code("DEFAULT_CLASS_MAP"), "."),

        H3("Default Rendering", link=True, cls="mb-3"),
        P("Rendering the sample Markdown with default classes:"),
        component_showcase(
            render_md(SAMPLE_MD),
            code='''from fastbite.all import render_md

SAMPLE_MD = """# Heading 1\n... (rest of markdown) ..."""

render_md(SAMPLE_MD)''',
            id="render-md-default",
            show_code_only=True # Just show the code, render the actual output below
        ),
        Br(),

        H3("Custom `class_map`", link=True, cls="mb-3"),
        P("Providing a completely custom ", Code("class_map"), " to override all default styles."),
        component_showcase(
            render_md(SAMPLE_MD, class_map={
                'h1': 'text-purple-600 text-2xl font-serif',
                'p': 'text-gray-500 italic'
                # Other tags will not have classes applied unless specified
            }),
            code='''from fastbite.all import render_md

SAMPLE_MD = """..."""

custom_map = {
    'h1': 'text-purple-600 text-2xl font-serif',
    'p': 'text-gray-500 italic'
    # ... add other mappings as needed
}

render_md(SAMPLE_MD, class_map=custom_map)''',
            id="render-md-custom-map",
            show_code_only=True
        ),

        Br(),

        H3("Modifying Classes with `class_map_mods`", link=True, cls="mb-3"),
        P("Using ", Code("class_map_mods"), " to tweak specific classes from the default map (or a provided custom map)."),
        component_showcase(
            render_md(SAMPLE_MD, class_map_mods={
                'h1': 'underline decoration-wavy', # Adds underline to default H1 styles
                'p': 'text-sm' # Overrides default paragraph size
            }),
            code='''from fastbite.all import render_md

SAMPLE_MD = """..."""

mods = {
    'h1': 'underline decoration-wavy', # Add classes to default H1
    'p': 'text-sm' # Override default P size
}

# This uses DEFAULT_CLASS_MAP and applies mods on top
render_md(SAMPLE_MD, class_map_mods=mods)''',
            id="render-md-mods",
            show_code_only=True
        ),

        Br(),
    )

# --- render_md_article Section ---
def _render_md_article_section():
    return Section(
        H2("`render_md_article`", link=True, cls="mb-4 mt-10"),
        P("A convenience function that calls ", Code("render_md"), " and wraps the result in a ", Code("Div"), " with Tailwind's typography plugin classes (", Code("format lg:format-lg dark:format-invert"), ") for article-style rendering."),

        H3("Default Article Rendering", link=True, cls="mb-3"),
        P("Rendering the sample Markdown using ", Code("render_md_article"), ". Notice the prose styling applied."),
        component_showcase(
            render_md_article(SAMPLE_MD),
            code='''from fastbite.all import render_md_article

SAMPLE_MD = """# Heading 1\n... (rest of markdown) ..."""

render_md_article(SAMPLE_MD)''',
            id="render-md-article-default",
            show_code_only=True
        ),
        Br(),

        H3("Article Rendering with Mods", link=True, cls="mb-3"),
        P("You can still pass ", Code("class_map_mods"), " to ", Code("render_md_article"), " to customize specific elements within the article format."),
        component_showcase(
            render_md_article(SAMPLE_MD, class_map_mods={
                'blockquote': 'border-green-500' # Change blockquote border color
            }),
            code='''from fastbite.all import render_md_article

SAMPLE_MD = """..."""

mods = {
    'blockquote': 'border-green-500' # Customize blockquote
}

render_md_article(SAMPLE_MD, class_map_mods=mods)''',
            id="render-md-article-mods",
            show_code_only=True
        ),
        Br(),
    )


# --- Main Showcase Function ---
def markdown_showcase():
    """Page showcasing Markdown rendering components"""
    return Container(
        H1("Markdown Rendering", link=True, cls="mb-8 mt-6"),
        P("Fastbite provides utilities to render Markdown content into styled HTML using the ", Code("fastbite.markdown"), " module, which leverages Mistletoe and applies Tailwind classes.", cls="mb-6 text-lg"),

        # Call section functions
        _render_md_section(),
        _render_md_article_section(),
    )

# Make the showcase available to the app
markdown_components = markdown_showcase() 