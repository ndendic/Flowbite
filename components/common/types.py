"""Type definitions for Flowbite components"""

from enum import auto
from .foundations import VEnum, stringify, str2cls

class TextT(VEnum):
    """Text utility types for Flowbite components"""
    def _generate_next_value_(name, start, count, last_values): 
        return str2cls('text', name)
    
    # Text sizes
    xs = auto()  # Will generate "text-xs"
    sm = auto()  # Will generate "text-sm"
    base = auto()  # Will generate "text-base"
    lg = auto()  # Will generate "text-lg"
    xl = auto()  # Will generate "text-xl"
    
    # Font weights
    thin = "font-thin"
    light = "font-light"
    normal = "font-normal"
    medium = "font-medium"
    semibold = "font-semibold"
    bold = "font-bold"
    
    # Text colors
    white = "text-white"
    gray = "text-gray-500 dark:text-gray-400"
    black = "text-black dark:text-white"
    primary = "text-blue-700 dark:text-blue-500"
    success = "text-green-700 dark:text-green-500"
    warning = "text-yellow-700 dark:text-yellow-500"
    danger = "text-red-700 dark:text-red-500"
    
    # Text alignment
    left = auto()  # Will generate "text-left"
    center = auto()  # Will generate "text-center"
    right = auto()  # Will generate "text-right"
    justify = auto()  # Will generate "text-justify"
    
    # Text decoration
    underline = auto()  # Will generate "text-underline"
    line_through = "line-through"
    no_underline = "no-underline"
    
    # Text transform
    uppercase = auto()  # Will generate "text-uppercase"
    lowercase = auto()  # Will generate "text-lowercase"
    capitalize = auto()  # Will generate "text-capitalize"
    normal_case = auto()  # Will generate "text-normal-case"

class ButtonT(VEnum):
    """Button utility types for Flowbite components"""
    def _generate_next_value_(name, start, count, last_values): 
        return str2cls('button', name)
    
    # Base styles
    default = "text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    alternative = "py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
    dark = "text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
    light = "text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
    green = "focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
    red = "focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900"
    yellow = "focus:outline-none text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:focus:ring-yellow-900"
    purple = "focus:outline-none text-white bg-purple-700 hover:bg-purple-800 focus:ring-4 focus:ring-purple-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-900"

    # Sizes
    xs = auto()  # Will generate "button-xs"
    sm = auto()  # Will generate "button-sm"
    base = auto()  # Will generate "button-base"
    lg = auto()  # Will generate "button-lg"
    xl = auto()  # Will generate "button-xl"

class CardT(VEnum):
    """Card utility types for Flowbite components"""
    default = "block p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700"
    hover = "block p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700"
    
class FlexT(VEnum):
    """Flexbox utility types"""
    def _generate_next_value_(name, start, count, last_values): 
        return str2cls('flex', name)
    
    # Display
    flex = "flex"
    inline = "inline-flex"
    
    # Direction
    row = auto()  # Will generate "flex-row"
    row_reverse = auto()  # Will generate "flex-row-reverse"
    col = auto()  # Will generate "flex-col"
    col_reverse = auto()  # Will generate "flex-col-reverse"
    
    # Justify content
    justify_start = "justify-start"
    justify_end = "justify-end"
    justify_center = "justify-center"
    justify_between = "justify-between"
    justify_around = "justify-around"
    justify_evenly = "justify-evenly"
    
    # Align items
    items_start = "items-start"
    items_end = "items-end"
    items_center = "items-center"
    items_baseline = "items-baseline"
    items_stretch = "items-stretch"
    
    # Wrap
    wrap = auto()  # Will generate "flex-wrap"
    wrap_reverse = auto()  # Will generate "flex-wrap-reverse"
    nowrap = auto()  # Will generate "flex-nowrap" 