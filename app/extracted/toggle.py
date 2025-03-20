from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The toggle component can be used to receive a simple “yes” or “no” type of answer from the user by choosing a single option from two options available in multiple sizes, styles, and colors coded with the utility classes from Tailwind CSS and with dark mode support.'),
    H2(
        'Toggle example',
        Span(id='toggle-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Toggle example', href='#toggle-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with the default toggle component example as a checkbox element to receive a true or false selection from the user.'),
    component_showcase(Div(
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Toggle me', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
), code="""Div(
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Toggle me', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Checked state',
        Span(id='checked-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Checked state', href='#checked-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('checked'),
        'attribute to the toggle component to activate the selection by default.'
    ),
    component_showcase(Div(
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Checked toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
), code="""Div(
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Checked toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Disabled state',
        Span(id='disabled-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disabled state', href='#disabled-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('disabled'),
        'attribute to disallow the users from making any further selections.'
    ),
    component_showcase(Div(
    Label(
        Input(type='checkbox', value=True, disabled=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Disabled toggle', cls='ms-3 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, disabled=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Disabled checked', cls='ms-3 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='inline-flex items-center cursor-pointer'
    )
), code="""Div(
    Label(
        Input(type='checkbox', value=True, disabled=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Disabled toggle', cls='ms-3 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, disabled=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Disabled checked', cls='ms-3 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='inline-flex items-center cursor-pointer'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Colors',
        Span(id='colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Colors', href='#colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Change the color of the toggle component by updating the color classes of',
        Code('peer-focus'),
        'and',
        Code('peer-checked'),
        '.'
    ),
    component_showcase(Div(
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-red-300 dark:peer-focus:ring-red-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-red-600 dark:peer-checked:bg-red-600"),
        Span('Red', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-green-300 dark:peer-focus:ring-green-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-green-600 dark:peer-checked:bg-green-600"),
        Span('Green', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-purple-300 dark:peer-focus:ring-purple-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-purple-600 dark:peer-checked:bg-purple-600"),
        Span('Purple', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-yellow-300 dark:peer-focus:ring-yellow-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-yellow-400 dark:peer-checked:bg-yellow-400"),
        Span('Yellow', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-teal-300 dark:peer-focus:ring-teal-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-teal-600 dark:peer-checked:bg-teal-600"),
        Span('Teal', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-orange-300 dark:peer-focus:ring-orange-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-orange-500 dark:peer-checked:bg-orange-500"),
        Span('Orange', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    )
), code="""Div(
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-red-300 dark:peer-focus:ring-red-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-red-600 dark:peer-checked:bg-red-600"),
        Span('Red', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-green-300 dark:peer-focus:ring-green-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-green-600 dark:peer-checked:bg-green-600"),
        Span('Green', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-purple-300 dark:peer-focus:ring-purple-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-purple-600 dark:peer-checked:bg-purple-600"),
        Span('Purple', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-yellow-300 dark:peer-focus:ring-yellow-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-yellow-400 dark:peer-checked:bg-yellow-400"),
        Span('Yellow', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-teal-300 dark:peer-focus:ring-teal-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-teal-600 dark:peer-checked:bg-teal-600"),
        Span('Teal', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, checked=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-focus:ring-4 peer-focus:ring-orange-300 dark:peer-focus:ring-orange-800 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-orange-500 dark:peer-checked:bg-orange-500"),
        Span('Orange', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center me-5 cursor-pointer'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with small, default, or large sizes of the toggle component based on your needs.'),
    component_showcase(Div(
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Small toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Default toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-14 h-7 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[4px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Large toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
), code="""Div(
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Small toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Default toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center mb-5 cursor-pointer'
    ),
    Label(
        Input(type='checkbox', value=True, cls='sr-only peer'),
        Div(cls="relative w-14 h-7 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[4px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
        Span('Large toggle', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='inline-flex items-center cursor-pointer'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
