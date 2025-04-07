from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The range component can be used as an input field to get a number from the user based on your custom selection (ie. from 1 to 100) by using a sliding animation.'),
    P('The examples on this page are all coded with Tailwind CSS and requires you to install Fastbite as a plugin inside your project to obtain all the necessary stylings.'),
    H2(
        'Range slider example',
        Span(id='range-slider-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Range slider example', href='#range-slider-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this default example with values from 1 to 100 and the default value of 50.'),
    component_showcase(Div(
    Label('Default range', fr='default-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='default-range', type='range', value='50', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
), code="""Div(
    Label('Default range', fr='default-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='default-range', type='range', value='50', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Disabled state',
        Span(id='disabled-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disabled state', href='#disabled-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('disabled'),
        'class to disallow the users from further selecting values.'
    ),
    component_showcase(Div(
    Label('Default range', fr='disabled-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='disabled-range', type='range', value='50', disabled=True, cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
), code="""Div(
    Label('Default range', fr='disabled-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='disabled-range', type='range', value='50', disabled=True, cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Min and max',
        Span(id='min-and-max', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Min and max', href='#min-and-max', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the min and max attributes on the range component to set the limits of the range values.'),
    component_showcase(Div(
    Label('Min-max range', fr='minmax-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='minmax-range', type='range', min='0', max='10', value='5', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
), code="""Div(
    Label('Min-max range', fr='minmax-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='minmax-range', type='range', min='0', max='10', value='5', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Steps',
        Span(id='steps', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Steps', href='#steps', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the step attribute on the range component to set the increment with which the values will change.'),
    component_showcase(Div(
    Label('Range steps', fr='steps-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='steps-range', type='range', min='0', max='5', value='2.5', step='0.5', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
), code="""Div(
    Label('Range steps', fr='steps-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='steps-range', type='range', min='0', max='5', value='2.5', step='0.5', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the small, default, and large sizes for the range component by applying the',
        Code('range-sm'),
        'and',
        Code('range-lg'),
        'utility classes from Fastbite and Tailwind CSS.'
    ),
    component_showcase(Div(
    Label('Small range', fr='small-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='small-range', type='range', value='50', cls='w-full h-1 mb-6 bg-gray-200 rounded-lg appearance-none cursor-pointer range-sm dark:bg-gray-700'),
    Label('Default range', fr='medium-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='medium-range', type='range', value='50', cls='w-full h-2 mb-6 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
    Label('Large range', fr='large-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='large-range', type='range', value='50', cls='w-full h-3 bg-gray-200 rounded-lg appearance-none cursor-pointer range-lg dark:bg-gray-700')
), code="""Div(
    Label('Small range', fr='small-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='small-range', type='range', value='50', cls='w-full h-1 mb-6 bg-gray-200 rounded-lg appearance-none cursor-pointer range-sm dark:bg-gray-700'),
    Label('Default range', fr='medium-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='medium-range', type='range', value='50', cls='w-full h-2 mb-6 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
    Label('Large range', fr='large-range', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='large-range', type='range', value='50', cls='w-full h-3 bg-gray-200 rounded-lg appearance-none cursor-pointer range-lg dark:bg-gray-700')
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Labels',
        Span(id='labels', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Labels', href='#labels', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example to add labels to each value milestone of the range slider component.'),
    component_showcase(Div(
    Div(
        Label('Labels range', fr='labels-range-input', cls='sr-only'),
        Input(id='labels-range-input', type='range', value='1000', min='100', max='1500', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
        Span('Min ($100)', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6'),
        Span('$500', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
        Span('$1000', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
        Span('Max ($1500)', cls='text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6'),
        cls='relative mb-6'
    )
), code="""Div(
    Div(
        Label('Labels range', fr='labels-range-input', cls='sr-only'),
        Input(id='labels-range-input', type='range', value='1000', min='100', max='1500', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
        Span('Min ($100)', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6'),
        Span('$500', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
        Span('$1000', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
        Span('Max ($1500)', cls='text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6'),
        cls='relative mb-6'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    id='mainContent'
)
