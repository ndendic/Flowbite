from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The indicator component can be used as a small element positioned absolutely relative to another component such as a button or card and show a number count, account status (red for offline, green for online) and other useful information.'),
    P('Check out the following examples for multiple sizes, colors, positionings, styles, and more all coded with Tailwind CSS and Flowbite.'),
    H2(
        'Default indicator',
        Span(id='default-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default indicator', href='#default-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to create a simple indicator with multiple colors and position it anywhere on the website.'),
    component_showcase(Div(
    Span(cls='flex w-3 h-3 me-3 bg-gray-200 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-gray-900 rounded-full dark:bg-gray-700'),
    Span(cls='flex w-3 h-3 me-3 bg-primary-600 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-green-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-red-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-purple-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-indigo-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-yellow-300 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-teal-500 rounded-full')
), code="""Div(
    Span(cls='flex w-3 h-3 me-3 bg-gray-200 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-gray-900 rounded-full dark:bg-gray-700'),
    Span(cls='flex w-3 h-3 me-3 bg-primary-600 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-green-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-red-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-purple-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-indigo-500 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-yellow-300 rounded-full'),
    Span(cls='flex w-3 h-3 me-3 bg-teal-500 rounded-full')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Legend indicator',
        Span(id='legend-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Legend indicator', href='#legend-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used as a legend indicator for charts to also add a text next to the bullet point.'),
    component_showcase(Div(
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-primary-600 rounded-full me-1.5 shrink-0'),
        'Visitors',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-purple-500 rounded-full me-1.5 shrink-0'),
        'Sessions',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-indigo-500 rounded-full me-1.5 shrink-0'),
        'Customers',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-teal-500 rounded-full me-1.5 shrink-0'),
        'Revenue',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    )
), code="""Div(
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-primary-600 rounded-full me-1.5 shrink-0'),
        'Visitors',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-purple-500 rounded-full me-1.5 shrink-0'),
        'Sessions',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-indigo-500 rounded-full me-1.5 shrink-0'),
        'Customers',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    ),
    Span(
        Span(cls='flex w-2.5 h-2.5 bg-teal-500 rounded-full me-1.5 shrink-0'),
        'Revenue',
        cls='flex items-center text-sm font-medium text-gray-900 dark:text-white me-3'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Indicator count',
        Span(id='indicator-count', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Indicator count', href='#indicator-count', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a number count inside the indicator and position it relative to a button component.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
            Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 16',
            cls='w-4 h-4 me-2'
        ),
        Span('Notifications', cls='sr-only'),
        'Messages',
        Div('8', cls='absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900'),
        type='button',
        cls='relative inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            cls='w-4 h-4 me-2'
        ),
        Span('Notifications', cls='sr-only'),
        'Messages',
        Div('8', cls='absolute inline-flex items-center justify-center w-6 h-6 text-xs font-bold text-white bg-red-500 border-2 border-white rounded-full -top-2 -end-2 dark:border-gray-900'),
        type='button',
        cls='relative inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Status indicator',
        Span(id='status-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Status indicator', href='#status-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a status indicator for the currently logged in user by showing red for offline and green for online.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='profile image', cls='w-10 h-10 rounded-full'),
        Span(cls='top-0 start-7 absolute w-3.5 h-3.5 bg-green-500 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative me-4'
    ),
    Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='profile image', cls='w-10 h-10 rounded-full'),
        Span(cls='top-0 start-7 absolute w-3.5 h-3.5 bg-red-500 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='profile image', cls='w-10 h-10 rounded-full'),
        Span(cls='top-0 start-7 absolute w-3.5 h-3.5 bg-green-500 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative me-4'
    ),
    Div(
        Img(src='/docs/images/people/profile-picture-5.jpg', alt='profile image', cls='w-10 h-10 rounded-full'),
        Span(cls='top-0 start-7 absolute w-3.5 h-3.5 bg-red-500 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Badge indicator',
        Span(id='badge-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Badge indicator', href='#badge-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add an indicator inside of a badge component.'),
    component_showcase(Div(
    Ul(
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Neil Sims', cls='text-sm font-semibold text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Span(
                    Span(cls='w-2 h-2 me-1 bg-green-500 rounded-full'),
                    'Available',
                    cls='inline-flex items-center bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-green-900 dark:text-green-300'
                ),
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Bonnie Green', cls='text-sm font-semibold text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Span(
                    Span(cls='w-2 h-2 me-1 bg-red-500 rounded-full'),
                    'Unavailable',
                    cls='inline-flex items-center bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300'
                ),
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        role='list',
        cls='max-w-sm divide-y divide-gray-200 dark:divide-gray-700'
    )
), code="""Div(
    Ul(
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Neil Sims', cls='text-sm font-semibold text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Span(
                    Span(cls='w-2 h-2 me-1 bg-green-500 rounded-full'),
                    'Available',
                    cls='inline-flex items-center bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-green-900 dark:text-green-300'
                ),
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Bonnie Green', cls='text-sm font-semibold text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Span(
                    Span(cls='w-2 h-2 me-1 bg-red-500 rounded-full'),
                    'Unavailable',
                    cls='inline-flex items-center bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300'
                ),
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        role='list',
        cls='max-w-sm divide-y divide-gray-200 dark:divide-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Stepper indicator',
        Span(id='stepper-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Stepper indicator', href='#stepper-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can also use the indicators inside of a stepper component when completing a form element.'),
    component_showcase(Div(
    Ol(
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 1', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-gray-200 rounded-full ring-0 ring-white dark:bg-gray-700 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                cls='flex items-center'
            ),
            Div(
                H3('Step 3', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        cls='flex items-center'
    ),
    Ol(
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 1', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-gray-900 rounded-full dark:bg-gray-300'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-gray-200 rounded-full ring-0 ring-white dark:bg-gray-700 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                cls='flex items-center'
            ),
            Div(
                H3('Step 3', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        cls='flex items-center'
    )
), code="""Div(
    Ol(
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 1', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-primary-100 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-gray-200 rounded-full ring-0 ring-white dark:bg-gray-700 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                cls='flex items-center'
            ),
            Div(
                H3('Step 3', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        cls='flex items-center'
    ),
    Ol(
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 1', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-primary-600 rounded-full'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-200 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Step 2', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        Li(
            Div(
                Div(
                    Span(cls='flex w-3 h-3 bg-gray-900 rounded-full dark:bg-gray-300'),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-gray-200 rounded-full ring-0 ring-white dark:bg-gray-700 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                cls='flex items-center'
            ),
            Div(
                H3('Step 3', cls='font-medium text-gray-900 dark:text-white'),
                cls='mt-3'
            ),
            cls='relative w-full mb-6'
        ),
        cls='flex items-center'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Loading indicator',
        Span(id='loading-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Loading indicator', href='#loading-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this animated loading indicator when content inside of a card is still loading.'),
    component_showcase(Div(
    Div(
        Div('loading...', cls='px-3 py-1 text-xs font-medium leading-none text-center text-primary-800 bg-primary-200 rounded-full animate-pulse dark:bg-primary-900 dark:text-primary-200'),
        cls='flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Div('loading...', cls='px-3 py-1 text-xs font-medium leading-none text-center text-primary-800 bg-primary-200 rounded-full animate-pulse dark:bg-primary-900 dark:text-primary-200'),
        cls='flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Spinner indicator',
        Span(id='spinner-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Spinner indicator', href='#spinner-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this animated spinner component inside of a card component that hasn’t loaded yet.'),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill'),
                aria_hidden='true',
                viewbox='0 0 100 101',
                fill='none',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-primary-600'
            ),
            Span('Loading...', cls='sr-only'),
            role='status'
        ),
        cls='flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill'),
                aria_hidden='true',
                viewbox='0 0 100 101',
                fill='none',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-primary-600'
            ),
            Span('Loading...', cls='sr-only'),
            role='status'
        ),
        cls='flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Indicator position',
        Span(id='indicator-position', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Indicator position', href='#indicator-position', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use these examples to position the indicator component anywhere relative to the parent element.'),
    component_showcase(Div(
    Div(
        Span('top-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 right-1/2'),
        Span('top-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 right-auto top-0 left-0'),
        Span('top-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 left-auto top-0 right-0'),
        Span('middle-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 top-2/4 left-1/2'),
        Span('middle-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 right-auto left-0 top-2/4'),
        Span('middle-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 left-auto right-0 top-2/4'),
        Span('bottom-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 translate-x-1/2 bottom-0 right-1/2'),
        Span('bottom-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 -translate-x-1/2 right-auto bottom-0 left-0'),
        Span('bottom-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 translate-x-1/2 left-auto bottom-0 right-0'),
        cls='relative w-56 h-56 bg-gray-100 border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Span('top-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 right-1/2'),
        Span('top-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 right-auto top-0 left-0'),
        Span('top-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 left-auto top-0 right-0'),
        Span('middle-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 top-2/4 left-1/2'),
        Span('middle-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 -translate-x-1/2 right-auto left-0 top-2/4'),
        Span('middle-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute -translate-y-1/2 translate-x-1/2 left-auto right-0 top-2/4'),
        Span('bottom-center', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 translate-x-1/2 bottom-0 right-1/2'),
        Span('bottom-left', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 -translate-x-1/2 right-auto bottom-0 left-0'),
        Span('bottom-right', cls='bg-primary-200 text-xs font-medium text-primary-800 text-center p-0.5 leading-none rounded-full px-2 dark:bg-primary-900 dark:text-primary-200 absolute translate-y-1/2 translate-x-1/2 left-auto bottom-0 right-0'),
        cls='relative w-56 h-56 bg-gray-100 border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    id='mainContent'
)
