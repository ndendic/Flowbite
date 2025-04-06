from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The progress bar component can be used as an indicator to show the completion rate of data sets or it can be used as an animated loader component. There are multiple sizes, colors, and styles available.'),
    H2(
        'Default progress bar',
        Span(id='default-progress-bar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default progress bar', href='#default-progress-bar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example of a progress bar element to show a completion rate of 45% by using an inline style and the utility classes from Tailwind CSS.'),
    component_showcase(Div(
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
), code="""Div(
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can also use different sizes by using various sizing utility classes from Flowbite and Tailwind CSS.'),
    component_showcase(Div(
    Div('Small', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-1.5 rounded-full dark:bg-primary-500'),
        cls='w-full bg-gray-200 rounded-full h-1.5 mb-4 dark:bg-gray-700'
    ),
    Div('Default', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full dark:bg-primary-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Large', cls='mb-1 text-lg font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='h-4 bg-primary-600 rounded-full dark:bg-primary-500'),
        cls='w-full h-4 mb-4 bg-gray-200 rounded-full dark:bg-gray-700'
    ),
    Div('Extra Large', cls='mb-1 text-lg font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='h-6 bg-primary-600 rounded-full dark:bg-primary-500'),
        cls='w-full h-6 bg-gray-200 rounded-full dark:bg-gray-700'
    )
), code="""Div(
    Div('Small', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-1.5 rounded-full dark:bg-primary-500'),
        cls='w-full bg-gray-200 rounded-full h-1.5 mb-4 dark:bg-gray-700'
    ),
    Div('Default', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full dark:bg-primary-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Large', cls='mb-1 text-lg font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='h-4 bg-primary-600 rounded-full dark:bg-primary-500'),
        cls='w-full h-4 mb-4 bg-gray-200 rounded-full dark:bg-gray-700'
    ),
    Div('Extra Large', cls='mb-1 text-lg font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='h-6 bg-primary-600 rounded-full dark:bg-primary-500'),
        cls='w-full h-6 bg-gray-200 rounded-full dark:bg-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'With label inside',
        Span(id='with-label-inside', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: With label inside', href='#with-label-inside', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Here is an example of using a progress bar with the label inside the bar.'),
    component_showcase(Div(
    Div(
        Div('45%', style='width: 45%', cls='bg-primary-600 text-xs font-medium text-primary-100 text-center p-0.5 leading-none rounded-full'),
        cls='w-full bg-gray-200 rounded-full dark:bg-gray-700'
    )
), code="""Div(
    Div(
        Div('45%', style='width: 45%', cls='bg-primary-600 text-xs font-medium text-primary-100 text-center p-0.5 leading-none rounded-full'),
        cls='w-full bg-gray-200 rounded-full dark:bg-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'With label outside',
        Span(id='with-label-outside', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: With label outside', href='#with-label-outside', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('And this is an example of using a progress bar outside the bar.'),
    component_showcase(Div(
    Div(
        Span('Flowbite', cls='text-base font-medium text-primary-700 dark:text-white'),
        Span('45%', cls='text-sm font-medium text-primary-700 dark:text-white'),
        cls='flex justify-between mb-1'
    ),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
), code="""Div(
    Div(
        Span('Flowbite', cls='text-base font-medium text-primary-700 dark:text-white'),
        Span('45%', cls='text-sm font-medium text-primary-700 dark:text-white'),
        cls='flex justify-between mb-1'
    ),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Colors',
        Span(id='colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Colors', href='#colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also apply any color using the',
        Code('bg-{color}'),
        'utility classes from Tailwind CSS and Flowbite.'
    ),
    component_showcase(Div(
    Div('Dark', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-gray-600 h-2.5 rounded-full dark:bg-gray-300'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Blue', cls='mb-1 text-base font-medium text-primary-700 dark:text-primary-500'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Red', cls='mb-1 text-base font-medium text-red-700 dark:text-red-500'),
    Div(
        Div(style='width: 45%', cls='bg-red-600 h-2.5 rounded-full dark:bg-red-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Green', cls='mb-1 text-base font-medium text-green-700 dark:text-green-500'),
    Div(
        Div(style='width: 45%', cls='bg-green-600 h-2.5 rounded-full dark:bg-green-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Yellow', cls='mb-1 text-base font-medium text-yellow-700 dark:text-yellow-500'),
    Div(
        Div(style='width: 45%', cls='bg-yellow-400 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Indigo', cls='mb-1 text-base font-medium text-indigo-700 dark:text-indigo-500'),
    Div(
        Div(style='width: 45%', cls='bg-indigo-600 h-2.5 rounded-full dark:bg-indigo-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Purple', cls='mb-1 text-base font-medium text-purple-700 dark:text-purple-500'),
    Div(
        Div(style='width: 45%', cls='bg-purple-600 h-2.5 rounded-full dark:bg-purple-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
), code="""Div(
    Div('Dark', cls='mb-1 text-base font-medium dark:text-white'),
    Div(
        Div(style='width: 45%', cls='bg-gray-600 h-2.5 rounded-full dark:bg-gray-300'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Blue', cls='mb-1 text-base font-medium text-primary-700 dark:text-primary-500'),
    Div(
        Div(style='width: 45%', cls='bg-primary-600 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Red', cls='mb-1 text-base font-medium text-red-700 dark:text-red-500'),
    Div(
        Div(style='width: 45%', cls='bg-red-600 h-2.5 rounded-full dark:bg-red-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Green', cls='mb-1 text-base font-medium text-green-700 dark:text-green-500'),
    Div(
        Div(style='width: 45%', cls='bg-green-600 h-2.5 rounded-full dark:bg-green-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Yellow', cls='mb-1 text-base font-medium text-yellow-700 dark:text-yellow-500'),
    Div(
        Div(style='width: 45%', cls='bg-yellow-400 h-2.5 rounded-full'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Indigo', cls='mb-1 text-base font-medium text-indigo-700 dark:text-indigo-500'),
    Div(
        Div(style='width: 45%', cls='bg-indigo-600 h-2.5 rounded-full dark:bg-indigo-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
    ),
    Div('Purple', cls='mb-1 text-base font-medium text-purple-700 dark:text-purple-500'),
    Div(
        Div(style='width: 45%', cls='bg-purple-600 h-2.5 rounded-full dark:bg-purple-500'),
        cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
