from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The badge component can be used to complement other elements such as buttons or text elements as a label or to show the count of a given data, such as the number of comments for an article or how much time has passed by since a comment has been made.'),
    P(
        'Alternatively, badges can also be used as standalone elements that link to a certain page by using the anchor tag instead of a',
        Code('span'),
        'element.'
    ),
    H2(
        'Default badge',
        Span(id='default-badge', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default badge', href='#default-badge', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following badge elements to indicate counts or labels inside or outside components.'),
    component_showcase(Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-pink-900 dark:text-pink-300')
), code="""Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-pink-900 dark:text-pink-300')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Large badges',
        Span(id='large-badges', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Large badges', href='#large-badges', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-sm'),
        'utility class and increase the paddings to create a larger variant of the badges.'
    ),
    component_showcase(Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-pink-900 dark:text-pink-300')
), code="""Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-pink-900 dark:text-pink-300')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Bordered badge',
        Span(id='bordered-badge', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Bordered badge', href='#bordered-badge', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add a border accent to the badge component.'),
    component_showcase(Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-400 border border-gray-500'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-red-400 border border-red-400'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-green-400 border border-green-400'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-yellow-300 border border-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-indigo-400 border border-indigo-400'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-purple-400 border border-purple-400'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-pink-400 border border-pink-400')
), code="""Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-gray-400 border border-gray-500'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-red-400 border border-red-400'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-green-400 border border-green-400'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-yellow-300 border border-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-indigo-400 border border-indigo-400'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-purple-400 border border-purple-400'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-pink-400 border border-pink-400')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Pills badge',
        Span(id='pills-badge', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pills badge', href='#pills-badge', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to make the corners even more rounded-sm like pills for the badge component.'),
    component_showcase(Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-pink-900 dark:text-pink-300')
), code="""Div(
    Span('Default', cls='bg-primary-100 text-primary-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-primary-900 dark:text-primary-300'),
    Span('Dark', cls='bg-gray-100 text-gray-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-gray-700 dark:text-gray-300'),
    Span('Red', cls='bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300'),
    Span('Green', cls='bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-green-900 dark:text-green-300'),
    Span('Yellow', cls='bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-yellow-900 dark:text-yellow-300'),
    Span('Indigo', cls='bg-indigo-100 text-indigo-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-indigo-900 dark:text-indigo-300'),
    Span('Purple', cls='bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-purple-900 dark:text-purple-300'),
    Span('Pink', cls='bg-pink-100 text-pink-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full dark:bg-pink-900 dark:text-pink-300')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Badges as links',
        Span(id='badges-as-links', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Badges as links', href='#badges-as-links', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can also use badges as anchor elements to link to another page.'),
    component_showcase(Div(
    A('Badge link', href='#', cls='bg-primary-100 hover:bg-primary-200 text-primary-800 text-xs font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400 inline-flex items-center justify-center'),
    A('Badge link', href='#', cls='bg-primary-100 hover:bg-primary-200 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400 inline-flex items-center justify-center')
), code="""Div(
    A('Badge link', href='#', cls='bg-primary-100 hover:bg-primary-200 text-primary-800 text-xs font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400 inline-flex items-center justify-center'),
    A('Badge link', href='#', cls='bg-primary-100 hover:bg-primary-200 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400 inline-flex items-center justify-center')
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Badges with icon',
        Span(id='badges-with-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Badges with icon', href='#badges-with-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also use',
        A('SVG icons', href='https://flowbite.com/icons/'),
        'inside the badge elements.'
    ),
    component_showcase(Div(
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-2.5 h-2.5 me-1.5'
        ),
        '3 days ago',
        cls='bg-gray-100 text-gray-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-sm me-2 dark:bg-gray-700 dark:text-gray-400 border border-gray-500'
    ),
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-2.5 h-2.5 me-1.5'
        ),
        '2 minutes ago',
        cls='bg-primary-100 text-primary-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400'
    )
), code="""Div(
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-2.5 h-2.5 me-1.5'
        ),
        '3 days ago',
        cls='bg-gray-100 text-gray-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-sm me-2 dark:bg-gray-700 dark:text-gray-400 border border-gray-500'
    ),
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-2.5 h-2.5 me-1.5'
        ),
        '2 minutes ago',
        cls='bg-primary-100 text-primary-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-sm dark:bg-gray-700 dark:text-primary-400 border border-primary-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Notification badge',
        Span(id='notification-badge', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Notification badge', href='#notification-badge', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example to show a badge inside of a button component.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
            Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 16',
            cls='w-5 h-5'
        ),
        Span('Notifications', cls='sr-only'),
        Div('20', cls='absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900'),
        type='button',
        cls='relative inline-flex items-center p-3 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    )
), code="""Div(
    Button(
        Svg(
            Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
            Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 16',
            cls='w-5 h-5'
        ),
        Span('Notifications', cls='sr-only'),
        Div('20', cls='absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900'),
        type='button',
        cls='relative inline-flex items-center p-3 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Button with badge',
        Span(id='button-with-badge', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Button with badge', href='#button-with-badge', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to add a badge inside a button component for a count indicator.'),
    component_showcase(Div(
    Button(
        'Messages',
        Span('2', cls='inline-flex items-center justify-center w-4 h-4 ms-2 text-xs font-semibold text-primary-800 bg-primary-200 rounded-full'),
        type='button',
        cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    )
), code="""Div(
    Button(
        'Messages',
        Span('2', cls='inline-flex items-center justify-center w-4 h-4 ms-2 text-xs font-semibold text-primary-800 bg-primary-200 rounded-full'),
        type='button',
        cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Badge with icon only',
        Span(id='badge-with-icon-only', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Badge with icon only', href='#badge-with-icon-only', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Alternatively you can also use badges which indicate only a SVG icon.'),
    component_showcase(Div(
    Span(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 16 12',
            cls='w-2.5 h-2.5'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        Svg(
            Path(fill='currentColor', d='m18.774 8.245-.892-.893a1.5 1.5 0 0 1-.437-1.052V5.036a2.484 2.484 0 0 0-2.48-2.48H13.7a1.5 1.5 0 0 1-1.052-.438l-.893-.892a2.484 2.484 0 0 0-3.51 0l-.893.892a1.5 1.5 0 0 1-1.052.437H5.036a2.484 2.484 0 0 0-2.48 2.481V6.3a1.5 1.5 0 0 1-.438 1.052l-.892.893a2.484 2.484 0 0 0 0 3.51l.892.893a1.5 1.5 0 0 1 .437 1.052v1.264a2.484 2.484 0 0 0 2.481 2.481H6.3a1.5 1.5 0 0 1 1.052.437l.893.892a2.484 2.484 0 0 0 3.51 0l.893-.892a1.5 1.5 0 0 1 1.052-.437h1.264a2.484 2.484 0 0 0 2.481-2.48V13.7a1.5 1.5 0 0 1 .437-1.052l.892-.893a2.484 2.484 0 0 0 0-3.51Z'),
            Path(fill='#fff', d='M8 13a1 1 0 0 1-.707-.293l-2-2a1 1 0 1 1 1.414-1.414l1.42 1.42 5.318-3.545a1 1 0 0 1 1.11 1.664l-6 4A1 1 0 0 1 8 13Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-primary-800 bg-primary-100 rounded-full dark:bg-gray-700 dark:text-primary-400'
    ),
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-primary-800 bg-primary-100 rounded-full dark:bg-gray-700 dark:text-primary-400'
    )
), code="""Div(
    Span(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 16 12',
            cls='w-2.5 h-2.5'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        Svg(
            Path(fill='currentColor', d='m18.774 8.245-.892-.893a1.5 1.5 0 0 1-.437-1.052V5.036a2.484 2.484 0 0 0-2.48-2.48H13.7a1.5 1.5 0 0 1-1.052-.438l-.893-.892a2.484 2.484 0 0 0-3.51 0l-.893.892a1.5 1.5 0 0 1-1.052.437H5.036a2.484 2.484 0 0 0-2.48 2.481V6.3a1.5 1.5 0 0 1-.438 1.052l-.892.893a2.484 2.484 0 0 0 0 3.51l.892.893a1.5 1.5 0 0 1 .437 1.052v1.264a2.484 2.484 0 0 0 2.481 2.481H6.3a1.5 1.5 0 0 1 1.052.437l.893.892a2.484 2.484 0 0 0 3.51 0l.893-.892a1.5 1.5 0 0 1 1.052-.437h1.264a2.484 2.484 0 0 0 2.481-2.48V13.7a1.5 1.5 0 0 1 .437-1.052l.892-.893a2.484 2.484 0 0 0 0-3.51Z'),
            Path(fill='#fff', d='M8 13a1 1 0 0 1-.707-.293l-2-2a1 1 0 1 1 1.414-1.414l1.42 1.42 5.318-3.545a1 1 0 0 1 1.11 1.664l-6 4A1 1 0 0 1 8 13Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-primary-800 bg-primary-100 rounded-full dark:bg-gray-700 dark:text-primary-400'
    ),
    Span(
        Svg(
            Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='w-3 h-3'
        ),
        Span('Icon description', cls='sr-only'),
        cls='inline-flex items-center justify-center w-6 h-6 me-2 text-sm font-semibold text-primary-800 bg-primary-100 rounded-full dark:bg-gray-700 dark:text-primary-400'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Chips (dismissible badges)',
        Span(id='chips-dismissible-badges', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Chips (dismissible badges)', href='#chips-dismissible-badges', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-dismiss-target'),
        'data attribute to dismiss the current badge where the value is the id of the target element using a transition animation.'
    ),
    component_showcase(Div(
    Span(
        'Default',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-default',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-primary-400 bg-transparent rounded-xs hover:bg-primary-200 hover:text-primary-900 dark:hover:bg-primary-800 dark:hover:text-primary-300'
        ),
        id='badge-dismiss-default',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-primary-800 bg-primary-100 rounded-sm dark:bg-primary-900 dark:text-primary-300'
    ),
    Span(
        'Dark',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-dark',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-gray-400 bg-transparent rounded-xs hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-gray-300'
        ),
        id='badge-dismiss-dark',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-gray-800 bg-gray-100 rounded-sm dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        'Red',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-red',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-red-400 bg-transparent rounded-xs hover:bg-red-200 hover:text-red-900 dark:hover:bg-red-800 dark:hover:text-red-300'
        ),
        id='badge-dismiss-red',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-red-800 bg-red-100 rounded-sm dark:bg-red-900 dark:text-red-300'
    ),
    Span(
        'Green',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-green',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-green-400 bg-transparent rounded-xs hover:bg-green-200 hover:text-green-900 dark:hover:bg-green-800 dark:hover:text-green-300'
        ),
        id='badge-dismiss-green',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-green-800 bg-green-100 rounded-sm dark:bg-green-900 dark:text-green-300'
    ),
    Span(
        'Yellow',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-yellow',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-yellow-400 bg-transparent rounded-xs hover:bg-yellow-200 hover:text-yellow-900 dark:hover:bg-yellow-800 dark:hover:text-yellow-300'
        ),
        id='badge-dismiss-yellow',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-yellow-800 bg-yellow-100 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'
    ),
    Span(
        'Indigo',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-indigo',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-indigo-400 bg-transparent rounded-xs hover:bg-indigo-200 hover:text-indigo-900 dark:hover:bg-indigo-800 dark:hover:text-indigo-300'
        ),
        id='badge-dismiss-indigo',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-indigo-800 bg-indigo-100 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'
    ),
    Span(
        'Purple',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-purple',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-purple-400 bg-transparent rounded-xs hover:bg-purple-200 hover:text-purple-900 dark:hover:bg-purple-800 dark:hover:text-purple-300'
        ),
        id='badge-dismiss-purple',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-purple-800 bg-purple-100 rounded-sm dark:bg-purple-900 dark:text-purple-300'
    ),
    Span(
        'Pink',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-pink',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-pink-400 bg-transparent rounded-xs hover:bg-pink-200 hover:text-pink-900 dark:hover:bg-pink-800 dark:hover:text-pink-300'
        ),
        id='badge-dismiss-pink',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-pink-800 bg-pink-100 rounded-sm dark:bg-pink-900 dark:text-pink-300'
    )
), code="""Div(
    Span(
        'Default',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-default',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-primary-400 bg-transparent rounded-xs hover:bg-primary-200 hover:text-primary-900 dark:hover:bg-primary-800 dark:hover:text-primary-300'
        ),
        id='badge-dismiss-default',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-primary-800 bg-primary-100 rounded-sm dark:bg-primary-900 dark:text-primary-300'
    ),
    Span(
        'Dark',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-dark',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-gray-400 bg-transparent rounded-xs hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-gray-300'
        ),
        id='badge-dismiss-dark',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-gray-800 bg-gray-100 rounded-sm dark:bg-gray-700 dark:text-gray-300'
    ),
    Span(
        'Red',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-red',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-red-400 bg-transparent rounded-xs hover:bg-red-200 hover:text-red-900 dark:hover:bg-red-800 dark:hover:text-red-300'
        ),
        id='badge-dismiss-red',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-red-800 bg-red-100 rounded-sm dark:bg-red-900 dark:text-red-300'
    ),
    Span(
        'Green',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-green',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-green-400 bg-transparent rounded-xs hover:bg-green-200 hover:text-green-900 dark:hover:bg-green-800 dark:hover:text-green-300'
        ),
        id='badge-dismiss-green',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-green-800 bg-green-100 rounded-sm dark:bg-green-900 dark:text-green-300'
    ),
    Span(
        'Yellow',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-yellow',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-yellow-400 bg-transparent rounded-xs hover:bg-yellow-200 hover:text-yellow-900 dark:hover:bg-yellow-800 dark:hover:text-yellow-300'
        ),
        id='badge-dismiss-yellow',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-yellow-800 bg-yellow-100 rounded-sm dark:bg-yellow-900 dark:text-yellow-300'
    ),
    Span(
        'Indigo',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-indigo',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-indigo-400 bg-transparent rounded-xs hover:bg-indigo-200 hover:text-indigo-900 dark:hover:bg-indigo-800 dark:hover:text-indigo-300'
        ),
        id='badge-dismiss-indigo',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-indigo-800 bg-indigo-100 rounded-sm dark:bg-indigo-900 dark:text-indigo-300'
    ),
    Span(
        'Purple',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-purple',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-purple-400 bg-transparent rounded-xs hover:bg-purple-200 hover:text-purple-900 dark:hover:bg-purple-800 dark:hover:text-purple-300'
        ),
        id='badge-dismiss-purple',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-purple-800 bg-purple-100 rounded-sm dark:bg-purple-900 dark:text-purple-300'
    ),
    Span(
        'Pink',
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-2 h-2'
            ),
            Span('Remove badge', cls='sr-only'),
            type='button',
            data_dismiss_target='#badge-dismiss-pink',
            aria_label='Remove',
            cls='inline-flex items-center p-1 ms-2 text-sm text-pink-400 bg-transparent rounded-xs hover:bg-pink-200 hover:text-pink-900 dark:hover:bg-pink-800 dark:hover:text-pink-300'
        ),
        id='badge-dismiss-pink',
        cls='inline-flex items-center px-2 py-1 me-2 text-sm font-medium text-pink-800 bg-pink-100 rounded-sm dark:bg-pink-900 dark:text-pink-300'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    id='mainContent'
)
