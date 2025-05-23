# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/21_markdown.ipynb.

# %% auto 0
__all__ = ['DEFAULT_CLASS_MAP', 'apply_classes', 'render_md', 'render_md_article']

# %% ../../nbs/21_markdown.ipynb 1
from fasthtml.common import FT
from fastcore.all import *
from ..core import *
from .base import *
from .base_styles import *
from enum import Enum

import mistletoe
from lxml import html, etree

# %% ../../nbs/21_markdown.ipynb 2
DEFAULT_CLASS_MAP = {
    # Headings with proper hierarchy and spacing
    'h1': 'text-4xl font-bold text-gray-900 dark:text-white mb-6 mt-12',
    'h2': 'text-3xl font-bold text-gray-900 dark:text-white mb-5 mt-10', 
    'h3': 'text-2xl font-semibold text-gray-900 dark:text-white mb-4 mt-8',
    'h4': 'text-xl font-semibold text-gray-900 dark:text-white mb-3 mt-6',
    
    # Body text and links
    'p': 'text-base text-gray-700 dark:text-gray-300 leading-relaxed mb-6',
    'a': 'text-primary-600 dark:text-primary-500 hover:underline font-medium',
    
    # Lists with proper spacing
    'ul': 'list-disc space-y-2 pl-5 mb-6 text-base text-gray-700 dark:text-gray-300',
    'ol': 'list-decimal space-y-2 pl-5 mb-6 text-base text-gray-700 dark:text-gray-300',
    'li': 'leading-relaxed',
    
    # Code and quotes
    'pre': 'bg-gray-50 dark:bg-gray-800 rounded-lg p-4 mb-6 overflow-x-auto',
    'code': 'font-mono text-sm bg-gray-100 dark:bg-gray-800 px-1 py-0.5 rounded text-gray-800 dark:text-gray-200',
    'pre code': 'font-mono text-sm block overflow-x-auto text-gray-800 dark:text-gray-200',
    'blockquote': 'pl-4 border-l-4 border-primary-500 italic mb-6 text-gray-700 dark:text-gray-300',
    
    # Tables
    'table': 'w-full border-collapse mb-6',
    'th': 'text-left p-2 font-semibold border-b border-gray-200 dark:border-gray-700',
    'td': 'p-2 border-b border-gray-200 dark:border-gray-700',
    
    # Other elements
    'hr': 'my-8 border-t border-gray-200 dark:border-gray-700',
    'img': 'max-w-full h-auto rounded-lg mb-6'
}

def apply_classes(html_str:str, # Html string
                  class_map=None, # Class map
                  class_map_mods=None # Class map that will modify the class map map (useful for small changes to a base class map)
                 )->str: # Html string with classes applied
    "Apply classes to html string"
    if not html_str: return html_str
    try:
        class_map = ifnone(class_map, DEFAULT_CLASS_MAP)
        if class_map_mods: class_map = {**class_map, **class_map_mods}
        html_str = html.fromstring(html_str)
        for selector, classes in class_map.items():
            # Handle descendant selectors (e.g., 'pre code')
            xpath = '//' + '/descendant::'.join(selector.split())
            for element in html_str.xpath(xpath):
                existing_class = element.get('class', '')
                new_class = f"{existing_class} {classes}".strip()
                element.set('class', new_class)
        return etree.tostring(html_str, encoding='unicode', method='html')
    except etree.ParserError:
        return html_str

def render_md(md_content:str, # Markdown content
               class_map=None, # Class map
               class_map_mods=None # Additional class map
              )->FT: # Rendered markdown
    "Renders markdown using mistletoe and lxml"
    if md_content=='': return md_content
    # Check for required dependencies        
    html_content = mistletoe.markdown(md_content) #, mcp.PygmentsRenderer)
    return NotStr(apply_classes(html_content, class_map, class_map_mods))

def render_md_article(md_content:str, # Markdown content
                      class_map=None, # Class map
                      class_map_mods=None, # Additional class map
                      cls:Enum|str|tuple=TextT.article # Added cls parameter
                     )->FT: # Rendered markdown
    "Renders markdown using mistletoe and lxml"
    return Div(render_md(md_content, class_map, class_map_mods),cls=stringify(cls)) # Use stringify

