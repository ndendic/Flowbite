from enum import Enum, auto
import fasthtml.common as fh
from fastcore.all import *
from ..common.types import ButtonT, TextT, FlexT
from ..common.foundations import stringify

def Button(*c: Union[str, FT],
           cls: Union[str, Enum]=ButtonT.default, 
           submit=True, 
           **kwargs 
           ) -> FT: 
    """
    Create a Flowbite button component
    
    Args:
        text (str): Button text
        style (str): Style from ButtonT (default, alternative, dark, light, etc.)
        type (str): Button type attribute
        cls (str): Custom classes (will override style if provided)
        size (str): Size from ButtonT (xs, sm, base, lg, xl)
        **kwargs: Additional HTML attributes
    """
    if 'type' not in kwargs: kwargs['type'] = 'submit' if submit else 'button'
    return fh.Button(*c, cls=('uk-btn', stringify(cls)), **kwargs)

def ButtonGroup():
    """Example of different button styles"""
    return fh.Div(
        cls=stringify((FlexT.flex, FlexT.items_center, "gap-2 py-4")),
    )(
        Button("Default"),
        Button("Alternative", cls=ButtonT.alternative),
        Button("Dark", cls=ButtonT.dark),
        Button("Light", cls=ButtonT.light),
        Button("Green", cls=ButtonT.green),
        Button("Red", cls=ButtonT.red),
        Button("Yellow", cls=ButtonT.yellow),
        Button("Purple", cls=ButtonT.purple),
    )
