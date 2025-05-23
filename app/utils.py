from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from fastbite.core import *

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
            data_tabs_toggle=f'#{id}-tab-content',
            cls=TabContainerT.rounded
        ),
        Ul(id=f'{id}-tab-content', cls='relative')(
            Li(id=f'{id}-preview', role='tabpanel', aria_labelledby=f'{id}-preview-tab', cls='p-4 border border-t-0 rounded-b-lg border-gray-300 dark:border-gray-600')(
                *c
            ),
            Li(id=f'{id}-code', role='tabpanel', aria_labelledby=f'{id}-code-tab', cls='hidden border border-t-0 rounded-b-lg border-gray-300 dark:border-gray-600')(
                CodeBlock(code)
            ),   
        ),
        cls=(cls,"max-w-4xl"),
        **kwargs
    )