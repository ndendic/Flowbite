from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from theme_switcher import ThemeSwitcher

def component_showcase(*c:FT|str, # Components
              code:str, # Code
              cls:str|tuple=(), # Additional classes
              **kwargs # Additional args
              )->FT: # Playground
    return Container(
        TabContainer(
            TabItem('Preview', controls='preview'),
            TabItem('Code', controls='code'),
            data_tabs_toggle='#default-tab-content'
        ),
        Ul(id='default-tab-content')(
            Li(id='preview', role='tabpanel', aria_labelledby='preview-tab', cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800')(
                *c
            ),
            Li(id='code', role='tabpanel', aria_labelledby='code-tab', cls='hidden rounded-lg bg-gray-50 dark:bg-gray-800')(
                Pre(cls='text-sm text-gray-500 dark:text-gray-400'+Round.lg)(
                    Code(cls='language-python')(code)
                )
            ),   
        ),
    )