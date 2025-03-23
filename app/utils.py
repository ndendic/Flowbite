from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *

def component_showcase(*c:FT|str, # Components
              code:str, # Code
              id:str, # ID
              cls:str|tuple=(), # Additional classes
              **kwargs # Additional args
              )->FT: # Playground
    return Div(
        TabContainer(
            TabItem('Preview', controls=f'{id}-preview'),
            TabItem('Code', controls=f'{id}-code'),
            data_tabs_toggle=f'#{id}-tab-content'
        ),
        Ul(id=f'{id}-tab-content')(
            Li(id=f'{id}-preview', role='tabpanel', aria_labelledby=f'{id}-preview-tab', cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800')(
                *c
            ),
            Li(id=f'{id}-code', role='tabpanel', aria_labelledby=f'{id}-code-tab', cls='hidden rounded-lg bg-gray-50 dark:bg-gray-800')(
                CodeBlock(code)
            ),   
        ),
        cls=(cls,"max-w-5xl"),
        **kwargs
    )