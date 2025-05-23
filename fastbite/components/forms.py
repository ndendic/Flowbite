# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/07_forms.ipynb.

# %% auto 0
__all__ = ['FormT', 'Form', 'LabelInputT', 'FormLabel', 'InputT', 'Input', 'TextArea', 'Options', 'Select', 'RadioT', 'Radio',
           'CheckboxT', 'Checkbox', 'SwitchT', 'Switch']

# %% ../../nbs/07_forms.ipynb 1
import fasthtml.common as fh
from fasthtml.common import FT
from fastcore.all import *
from ..core import *
from .base import *
from .base_styles import *
from .media import *
from .buttons import *
from enum import Enum


# %% ../../nbs/07_forms.ipynb 2

def Form(*c, # contents of Form tag (often Buttons, FormLabels, and LabelInputs)
          cls:Enum|str|tuple=FormT.default, # Classes in addition to Form styling (default is 'space-y-3' to prevent scrunched up form elements)
          **kwargs # Additional args for Form tag
          )->FT: # Form(..., cls='space-y-3')
    "A Form with default spacing between form elements"
    return fh.Form(*c, cls=stringify(cls), **kwargs)

def FormLabel(*c, # contents of FormLabel tag (often text)
               cls:Enum|str|tuple=LabelInputT.default, # Classes in addition to FormLabel styling
               **kwargs # Additional args for FormLabel tag
               )->FT: # Label(..., cls='uk-form-label')
    "A Label with default styling"
    return fh.Label(*c, cls=stringify(cls), **kwargs)

def Input(label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=LabelInputT.default, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=InputT.default, # Additional classes for `Input`
          help_cls:Enum|str|tuple=TextT.sm, # Additional classes for `P` (help text)
          div_cls:Enum|str|tuple='mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          placeholder='', # Placeholder text for the input
          required=False, # Whether the input is required
          help_text:str|FT = None, # Help text for the input
         icon='lucide:', # Icon for the input
          disabled=False, # Whether the input is disabled
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(
                FormLabel(label, fr=id, cls=lbl_cls) if label else None,
                Div(cls="relative")(
                    Div(
                        Icon(icon,cls=IconT.default),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
                    ),
                    fh.Input(id=id, 
                             placeholder=placeholder, 
                             required=required, 
                             cls=(cls,'ps-10' if icon else '','cursor-not-allowed' if disabled else ''), 
                             disabled=disabled, 
                             **kwargs
                        )
                ),
                P(help_text, cls=(help_cls,"mt-2")),
                cls=(div_cls),                
            )

def TextArea(label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=LabelInputT.default, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=InputT.default, # Additional classes for `Input`
          help_cls:Enum|str|tuple=TextT.sm, # Additional classes for `P` (help text)
          div_cls:Enum|str|tuple='mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          placeholder='', # Placeholder text for the input
          required=False, # Whether the input is required
          help_text:str|FT = None, # Help text for the input
         icon='lucide:', # Icon for the input
          disabled=False, # Whether the input is disabled
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(
                FormLabel(label, fr=id, cls=lbl_cls) if label else None,
                Div(cls="relative")(
                    Div(
                        Icon(icon,cls=IconT.default),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
                    ),
                    fh.Textarea(id=id, placeholder=placeholder, required=required, cls=(cls,'ps-10' if icon else '','cursor-not-allowed' if disabled else ''), disabled=disabled, **kwargs)
                ),
                P(help_text, cls=(help_cls,"mt-2")),
                cls=(div_cls),                
            )

def Options(*c,                    # Content for an `Option`
            selected_idx:int=None, # Index location of selected `Option`
            disabled_idxs:set=None # Idex locations of disabled `Options`
           ):
    "Helper function to wrap things into `Option`s for use in `Select`"
    return [fh.Option(o) for i,o in enumerate(c)]

def Select(*options, # Options for the select dropdown (can use `Options` helper function to create)
          label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=LabelInputT.default, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=InputT.default, # Additional classes for `Input`
          help_cls:Enum|str|tuple=TextT.sm, # Additional classes for `P` (help text)
          div_cls:Enum|str|tuple='mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          placeholder='', # Placeholder text for the input
          required=False, # Whether the input is required
          help_text:str|FT = None, # Help text for the input
         icon='lucide:', # Icon for the input
          disabled=False, # Whether the input is disabled
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(
                FormLabel(label, fr=id, cls=lbl_cls) if label else None,
                Div(cls="relative")(
                    Div(
                        Icon(icon,cls=IconT.default),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
                    ),
                    fh.Select(*options,id=id, placeholder=placeholder, required=required, cls=(cls,'ps-10' if icon else '','cursor-not-allowed' if disabled else ''), disabled=disabled, **kwargs)
                ),
                P(help_text, cls=(help_cls,"mt-2")),
                cls=(div_cls),                
            )

def Radio(value:str='', # Value for the radio button
          label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=TextT.medium, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=RadioT.default, # Additional classes for `Input`
          help_cls:Enum|str|tuple=TextT.xs+TextT.gray, # Additional classes for `P` (help text)
          div_cls:Enum|str|tuple='flex mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          help_text:str|FT = None, # Help text for the input
          disabled=False, # Whether the input is disabled
          checked=False, # Whether the input is selected
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(cls=div_cls)(
                Div(cls='flex items-center h-5')(
                    fh.Input(id=id, aria_describedby=f'{id}-text', type='radio', value=value, cls=(cls,'cursor-not-allowed' if disabled else ''), disabled=disabled, checked=checked, **kwargs)
                ),
                Div(cls='ms-2 text-sm')(
                    FormLabel(label, fr=id, cls=lbl_cls),
                    P(help_text, id=f'{id}-text', cls=help_cls)
                ),                         
            )

def Checkbox(label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=TextT.medium, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=CheckboxT.default, # Additional classes for `Input`
          help_cls:Enum|str|tuple=TextT.xs+TextT.gray, # Additional classes for `P` (help text)
          div_cls:Enum|str|tuple='flex mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          help_text:str|FT = None, # Help text for the input
          disabled=False, # Whether the input is disabled
          checked=False, # Whether the input is selected
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(cls=div_cls)(
                Div(cls='flex items-center h-5')(
                    fh.Input(id=id, aria_describedby=f'{id}-text', type='checkbox', value='', cls=(cls,'cursor-not-allowed' if disabled else ''), disabled=disabled, checked=checked, **kwargs)
                ),
                Div(cls='ms-2 text-sm')(
                    FormLabel(label, fr=id, cls=lbl_cls),
                    P(help_text, id=f'{id}-text', cls=help_cls)
                ),                         
            )

def Switch(label:str|FT = None, # FormLabel content (often text)
          lbl_cls:Enum|str|tuple=TextT.medium, # Additional classes for `FormLabel`
          cls:Enum|str|tuple=SwitchT.default, # Additional classes for `Input`
          div_cls:Enum|str|tuple='flex mb-5', # Classes on container (default is `'space-y-2'` to prevent scrunched up form elements)
          id='', # id for `FormLabel` and `Input` (`id`, `name` and `for` attributes are set to this value)
          disabled=False, # Whether the input is disabled
          checked=False, # Whether the input is selected
          **kwargs # Additional args for `Input`
          )->FT:    
    return Div(cls=div_cls)(FormLabel(cls='inline-flex items-center cursor-pointer')(
            fh.Input(type='checkbox',id=id, value='', cls='sr-only peer',disabled=disabled,checked=checked,**kwargs),
            Div(cls=cls,disabled=disabled),
            Span(label, cls=(lbl_cls,"ms-3"))
        )
    )
# Label(cls='inline-flex items-center mb-5 cursor-pointer')(
#             Input(type='checkbox', cls='sr-only peer',disabled=disabled,checked=checked),
#             Div(cls="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-gray-50 after:border-gray-300 after:border after:rounded-full after:w-5 after:h-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600 dark:peer-checked:bg-blue-600"),
#             Span(label, cls=(lbl_cls,"ms-3"))
#         )


