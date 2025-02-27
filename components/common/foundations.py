"""Data Structures and Utilities for Flowbite Components"""

from enum import Enum, auto
from typing import Union, Tuple, Sequence
from fastcore.foundation import L, Generator

def stringify(o: Union[str, Tuple, Enum, Sequence]) -> str:
    """Converts input types into strings that can be passed to FT components"""
    if isinstance(o, (tuple,list,L,slice,Generator)): 
        return ' '.join(map(str, o)) if o else ""
    return str(o)

def str2cls(base: str, txt: str) -> str:
    """Convert base and text into a class name"""
    return f"{base}-{txt.replace('_', '-')}".strip('-')

class VEnum(str, Enum):
    """Base class for value enums with string operations"""
    def __str__(self) -> str:
        return self.value
    
    def __add__(self, other) -> str:
        return stringify((self, other))
    
    def __radd__(self, other) -> str:
        return stringify((other, self)) 