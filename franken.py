
# %% ../nbs/02_franken.ipynb
import fasthtml.common as fh

from fastbite.all import TabContainer
from .foundations import *
from fasthtml.common import Div, P, Span, FT
from enum import Enum, auto
from fasthtml.components import Uk_select,Uk_input_tag,Uk_icon
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional, Sequence
from fastcore.all import *
import copy, re, httpx, os
from pathlib import Path
from mistletoe.html_renderer import HTMLRenderer
from mistletoe.span_token import Image
from pathlib import Path
import mistletoe
from lxml import html, etree
from fasthtml.components import Uk_input_range
import fasthtml.components as fh_comp

# %% ../nbs/02_franken.ipynb
# def UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6):
#     "A form section with a title, description and optional button"
#     return Div(cls=f'space-y-{inner_margin} py-{outer_margin}')(
#         Div(H3(title), P(description, cls=TextPresets.muted_sm)),
#         DividerSplit(), *c,
#         Div(Button(button_txt, cls=ButtonT.primary)) if button_txt else None)

# %% ../nbs/02_franken.ipynb
# class ScrollspyT(VEnum):
#     underline = 'navbar-underline'
#     bold = 'navbar-bold'

# %% ../nbs/02_franken.ipynb
def TableFromLists(header_data:Sequence, # List of header data
                   body_data:Sequence[Sequence], # List of lists of body data
                   footer_data=None, # List of footer data
                   header_cell_render=Th, # Function(content) -> FT that renders header cells
                   body_cell_render=Td, # Function(key, content) -> FT that renders body cells
                   footer_cell_render=Td, #  Function(key, content) -> FT that renders footer cells
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), # Additional classes on the table
                   sortable=False, # Whether to use sortable table
                   **kwargs # Additional args for the table
                  )->FT: # Table from lists
    "Creates a Table from a list of header data and a list of lists of body data"
    return Table(
                Thead(Tr(*map(header_cell_render, header_data))),
                Tbody(*[Tr(*map(body_cell_render, r)) for r in body_data], sortable=sortable),
                Tfoot(Tr(*map(footer_cell_render, footer_data))) if footer_data else '',
                cls=stringify(cls),    
                **kwargs)

# %% ../nbs/02_franken.ipynb
def TableFromDicts(header_data:Sequence, # List of header data
                   body_data:Sequence[dict], # List of dicts of body data
                   footer_data=None, # List of footer data
                   header_cell_render=Th, # Function(content) -> FT that renders header cells
                   body_cell_render=lambda k,v : Td(v), # Function(key, content) -> FT that renders body cells
                   footer_cell_render=lambda k,v : Td(v), #  Function(key, content) -> FT that renders footer cells
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), # Additional classes on the table
                   sortable=False, # Whether to use sortable table
                   **kwargs # Additional args for the table
                  )->FT: # Styled Table
    "Creates a Table from a list of header data and a list of dicts of body data"
    return Table(
        Thead(Tr(*[header_cell_render(h) for h in header_data])),
        Tbody(*[Tr(*[body_cell_render(k, r.get(k, '')) for k in header_data]) for r in body_data], sortable=sortable),
        Tfoot(Tr(*[footer_cell_render(k, footer_data.get(k.lower(), '')) for k in header_data])) if footer_data else '',
        cls=stringify(cls),    
        **kwargs
    )

# %% ../nbs/02_franken.ipynb
franken_class_map = {
    'h1': 'uk-h1 text-4xl font-bold mt-12 mb-6',
    'h2': 'uk-h2 text-3xl font-bold mt-10 mb-5', 
    'h3': 'uk-h3 text-2xl font-semibold mt-8 mb-4',
    'h4': 'uk-h4 text-xl font-semibold mt-6 mb-3',
    
    # Body text and links
    'p': 'text-lg leading-relaxed mb-6',
    'a': 'uk-link text-primary hover:text-primary-focus underline',
    
    # Lists with proper spacing
    'ul': 'uk-list uk-list-bullet space-y-2 mb-6 ml-6 text-lg',
    'ol': 'uk-list uk-list-decimal space-y-2 mb-6 ml-6 text-lg',
    'li': 'leading-relaxed',
    
    # Code and quotes
    'pre': 'bg-base-200 rounded-lg p-4 mb-6',
    'code': 'uk-codespan px-1',
    'pre code': 'uk-codespan px-1 block overflow-x-auto',
    'blockquote': 'uk-blockquote pl-4 border-l-4 border-primary italic mb-6',
    
    # Tables
    'table': 'uk-table uk-table-divider uk-table-hover uk-table-small w-full mb-6',
    'th': '!text-left p-2 font-semibold',
    'td': 'p-2',
    
    # Other elements
    'hr': 'uk-divider-icon my-8',
    'img': 'max-w-full h-auto rounded-lg mb-6'
}

# %% ../nbs/02_franken.ipynb


# %% ../nbs/02_franken.ipynb
def get_franken_renderer(img_dir):
    "Create a renderer class with the specified img_dir"
    class FrankenRenderer(HTMLRenderer):
        "Custom renderer for Franken UI that handles image paths"
        def render_image(self, token):
            "Modify image paths if they're relative and img_dir is specified"
            template = '<img src="{}" alt="{}"{} class="max-w-full h-auto rounded-lg mb-6">'
            title = f' title="{token.title}"' if hasattr(token, 'title') else ''
            src = token.src
            if img_dir and not src.startswith(('http://', 'https://', '/')):
                src = f'{Path(img_dir)}/{src}'
            return template.format(src, token.children[0].content if token.children else '', title)
    return FrankenRenderer

# %% ../nbs/02_franken.ipynb
def render_md(md_content:str, # Markdown content
             class_map=None, # Class map
             class_map_mods=None, # Additional class map
             img_dir:str=None # Directory containing images
             )->FT: # Rendered markdown
    "Renders markdown using mistletoe and lxml with custom image handling"
    if md_content=='': return md_content
    renderer = get_franken_renderer(img_dir)
    html_content = mistletoe.markdown(md_content, renderer)
    return NotStr(apply_classes(html_content, class_map, class_map_mods))

# %% ../nbs/02_franken.ipynb
def LightboxContainer(*lightboxitem, # `LightBoxItem`s that will be inside lightbox
                      data_uk_lightbox='counter: true', # See https://franken-ui.dev/docs/2.0/lightbox for advanced options
                      **kwargs # Additional options for outer container
                     )->FT: # Lightbox
    "Lightbox container that will hold `LightboxItems`"
    return fh.Div(*lightboxitem, data_uk_lightbox=data_uk_lightbox, **kwargs)

# %% ../nbs/02_franken.ipynb
def LightboxItem(*c, # Component that when clicked will open the lightbox (often a button)
                 href, # Href to image, youtube video, vimeo, google maps, etc.
                 data_alt=None, # Alt text for the lightbox item/image
                 data_caption=None, # Caption for the item that shows below it
                 cls='', # Class for the A tag (often nothing or `uk-btn`)
                 **kwargs # Additional args for the `A` tag
                )->FT: # A(... href, data_alt, cls., ...)
    "Anchor tag with appropriate structure to go inside a `LightBoxContainer`"
    return fh.A(*c, href=href, data_alt=data_alt, cls=stringify(cls), **kwargs)

