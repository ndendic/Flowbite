from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The timeline component can be used to show series of data in a chronological order for use cases such as activity feeds, user actions, application updates, and more. Get started with multiple vertical timeline styles built with the utility classes from Tailwind CSS and Flowbite.'),
    H2(
        'Default timeline',
        Span(id='default-timeline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default timeline', href='#default-timeline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this responsive Tailwind CSS timeline component to show a series of data entries with a date, title, and description with a vertical line with dots on the left or right side of the wrapper element.'),
    P('Optionally, you can also add a CTA button to any of the timeline elements.'),
    component_showcase(Div(
    Ol(
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('February 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('Application UI code in Tailwind CSS', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce & Marketing pages.', cls='mb-4 text-base font-normal text-gray-500 dark:text-gray-400'),
            A(
                'Learn more',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3 h-3 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-100 focus:text-primary-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700'
            ),
            cls='mb-10 ms-4'
        ),
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('March 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('Marketing UI design in Figma', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('All of the pages and components are first designed in Figma and we keep a parity between the two versions even as we update the project.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-10 ms-4'
        ),
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('April 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('E-Commerce UI code in Tailwind CSS', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('Get started with dozens of web components and interactive elements built on top of Tailwind CSS.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='ms-4'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
), code="""Div(
    Ol(
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('February 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('Application UI code in Tailwind CSS', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce & Marketing pages.', cls='mb-4 text-base font-normal text-gray-500 dark:text-gray-400'),
            A(
                'Learn more',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3 h-3 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-100 focus:text-primary-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700'
            ),
            cls='mb-10 ms-4'
        ),
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('March 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('Marketing UI design in Figma', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('All of the pages and components are first designed in Figma and we keep a parity between the two versions even as we update the project.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-10 ms-4'
        ),
        Li(
            Div(cls='absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700'),
            Time('April 2022', cls='mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            H3('E-Commerce UI code in Tailwind CSS', cls='text-lg font-semibold text-gray-900 dark:text-white'),
            P('Get started with dozens of web components and interactive elements built on top of Tailwind CSS.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='ms-4'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Vertical timeline',
        Span(id='vertical-timeline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Vertical timeline', href='#vertical-timeline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this vertical timeline component with icons and badges to show a more advanced set of data.'),
    component_showcase(Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3(
                'Flowbite Application UI v2.0.0',
                Span('Latest', cls='bg-primary-100 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300 ms-3'),
                cls='flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white'
            ),
            Time('Released on January 13th, 2022', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce & Marketing pages.', cls='mb-4 text-base font-normal text-gray-500 dark:text-gray-400'),
            A(
                Svg(
                    Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                    Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-3.5 h-3.5 me-2.5'
                ),
                'Download ZIP',
                href='#',
                cls='inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-100 focus:text-primary-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3('Flowbite Figma v1.3.0', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
            Time('Released on December 7th, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('All of the pages and components are first designed in Figma and we keep a parity between the two versions even as we update the project.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3('Flowbite Library v1.2.2', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
            Time('Released on December 2nd, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('Get started with dozens of web components and interactive elements built on top of Tailwind CSS.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='ms-6'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
), code="""Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3(
                'Flowbite Application UI v2.0.0',
                Span('Latest', cls='bg-primary-100 text-primary-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300 ms-3'),
                cls='flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white'
            ),
            Time('Released on January 13th, 2022', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce & Marketing pages.', cls='mb-4 text-base font-normal text-gray-500 dark:text-gray-400'),
            A(
                Svg(
                    Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                    Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-3.5 h-3.5 me-2.5'
                ),
                'Download ZIP',
                href='#',
                cls='inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-100 focus:text-primary-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3('Flowbite Figma v1.3.0', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
            Time('Released on December 7th, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('All of the pages and components are first designed in Figma and we keep a parity between the two versions even as we update the project.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                ),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            H3('Flowbite Library v1.2.2', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
            Time('Released on December 2nd, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
            P('Get started with dozens of web components and interactive elements built on top of Tailwind CSS.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
            cls='ms-6'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Stepper timeline',
        Span(id='stepper-timeline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Stepper timeline', href='#stepper-timeline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this horizontally aligned timeline component to show a series of data in a chronological order.'),
    component_showcase(Div(
    Ol(
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.0.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on December 2, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.2.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on December 23, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.3.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on January 5, 2022', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        cls='items-center sm:flex'
    )
), code="""Div(
    Ol(
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.0.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on December 2, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.2.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on December 23, 2021', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        Li(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-2.5 h-2.5 text-primary-800 dark:text-primary-300'
                    ),
                    cls='z-10 flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full ring-0 ring-white dark:bg-primary-900 sm:ring-8 dark:ring-gray-900 shrink-0'
                ),
                Div(cls='hidden sm:flex w-full bg-gray-200 h-0.5 dark:bg-gray-700'),
                cls='flex items-center'
            ),
            Div(
                H3('Flowbite Library v1.3.0', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                Time('Released on January 5, 2022', cls='block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500'),
                P('Get started with dozens of web components and interactive elements.', cls='text-base font-normal text-gray-500 dark:text-gray-400'),
                cls='mt-3 sm:pe-8'
            ),
            cls='relative mb-6 sm:mb-0'
        ),
        cls='items-center sm:flex'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Activity log',
        Span(id='activity-log', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Activity log', href='#activity-log', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to show the timline of a user’s activity history inside your application by using an avatar, datetime, description, and links to specific pages.'),
    component_showcase(Div(
    Ol(
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Time('just now', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                Div(
                    'Bonnie moved',
                    A('Jese Leos', href='#', cls='font-semibold text-primary-600 dark:text-primary-500 hover:underline'),
                    'to',
                    Span('Funny Group', cls='bg-gray-100 text-gray-800 text-xs font-normal me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-600 dark:text-gray-300'),
                    cls='text-sm font-normal text-gray-500 dark:text-gray-300'
                ),
                cls='items-center justify-between p-4 bg-white border border-gray-200 rounded-lg shadow-xs sm:flex dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt='Thomas Lean image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Div(
                    Time('2 hours ago', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                    Div(
                        'Thomas Lean commented on',
                        A('Flowbite Pro', href='#', cls='font-semibold text-gray-900 dark:text-white hover:underline'),
                        cls='text-sm font-normal text-gray-500 lex dark:text-gray-300'
                    ),
                    cls='items-center justify-between mb-3 sm:flex'
                ),
                Div("Hi ya'll! I wanted to share a webinar zeroheight is having regarding how to best measure your design system! This is the second session of our new webinar series on #DesignSystems discussions where we'll be speaking about Measurement.", cls='p-3 text-xs italic font-normal text-gray-500 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-600 dark:border-gray-500 dark:text-gray-300'),
                cls='p-4 bg-white border border-gray-200 rounded-lg shadow-xs dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Time('1 day ago', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                Div(
                    'Jese Leos has changed',
                    A('Pricing page', href='#', cls='font-semibold text-primary-600 dark:text-primary-500 hover:underline'),
                    'task status to',
                    Span('Finished', cls='font-semibold text-gray-900 dark:text-white'),
                    cls='text-sm font-normal text-gray-500 lex dark:text-gray-300'
                ),
                cls='items-center justify-between p-4 bg-white border border-gray-200 rounded-lg shadow-xs sm:flex dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='ms-6'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
), code="""Div(
    Ol(
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Time('just now', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                Div(
                    'Bonnie moved',
                    A('Jese Leos', href='#', cls='font-semibold text-primary-600 dark:text-primary-500 hover:underline'),
                    'to',
                    Span('Funny Group', cls='bg-gray-100 text-gray-800 text-xs font-normal me-2 px-2.5 py-0.5 rounded-sm dark:bg-gray-600 dark:text-gray-300'),
                    cls='text-sm font-normal text-gray-500 dark:text-gray-300'
                ),
                cls='items-center justify-between p-4 bg-white border border-gray-200 rounded-lg shadow-xs sm:flex dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt='Thomas Lean image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Div(
                    Time('2 hours ago', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                    Div(
                        'Thomas Lean commented on',
                        A('Flowbite Pro', href='#', cls='font-semibold text-gray-900 dark:text-white hover:underline'),
                        cls='text-sm font-normal text-gray-500 lex dark:text-gray-300'
                    ),
                    cls='items-center justify-between mb-3 sm:flex'
                ),
                Div("Hi ya'll! I wanted to share a webinar zeroheight is having regarding how to best measure your design system! This is the second session of our new webinar series on #DesignSystems discussions where we'll be speaking about Measurement.", cls='p-3 text-xs italic font-normal text-gray-500 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-600 dark:border-gray-500 dark:text-gray-300'),
                cls='p-4 bg-white border border-gray-200 rounded-lg shadow-xs dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='rounded-full shadow-lg'),
                cls='absolute flex items-center justify-center w-6 h-6 bg-primary-100 rounded-full -start-3 ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900'
            ),
            Div(
                Time('1 day ago', cls='mb-1 text-xs font-normal text-gray-400 sm:order-last sm:mb-0'),
                Div(
                    'Jese Leos has changed',
                    A('Pricing page', href='#', cls='font-semibold text-primary-600 dark:text-primary-500 hover:underline'),
                    'task status to',
                    Span('Finished', cls='font-semibold text-gray-900 dark:text-white'),
                    cls='text-sm font-normal text-gray-500 lex dark:text-gray-300'
                ),
                cls='items-center justify-between p-4 bg-white border border-gray-200 rounded-lg shadow-xs sm:flex dark:bg-gray-700 dark:border-gray-600'
            ),
            cls='ms-6'
        ),
        cls='relative border-s border-gray-200 dark:border-gray-700'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Grouped timeline',
        Span(id='grouped-timeline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Grouped timeline', href='#grouped-timeline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to group multiple data entries inside a single date and show elements like the avatar, title, description, tag and link to a relevant page.'),
    component_showcase(Div(
    Div(
        Time('January 13th, 2022', cls='text-lg font-semibold text-gray-900 dark:text-white'),
        Ol(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Jese Leos', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Bonnie Green', cls='font-medium text-gray-900 dark:text-white'),
                            'react to',
                            Span("Thomas Lean's", cls='font-medium text-gray-900 dark:text-white'),
                            'comment',
                            cls='text-base font-normal text-gray-600 dark:text-gray-400'
                        ),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        )
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            cls='mt-3 divide-y divide-gray-200 dark:divide-gray-700'
        ),
        cls='p-5 mb-4 border border-gray-100 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    ),
    Div(
        Time('January 12th, 2022', cls='text-lg font-semibold text-gray-900 dark:text-white'),
        Ol(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Laura Romeros image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Laura Romeros', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Mike Willi image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Mike Willi', cls='font-medium text-gray-900 dark:text-white'),
                            'react to',
                            Span("Thomas Lean's", cls='font-medium text-gray-900 dark:text-white'),
                            'comment',
                            cls='text-base font-normal text-gray-600 dark:text-gray-400'
                        ),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        )
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese Leos image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Jese Leos', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Bonnie Green', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('Top figma designs', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            cls='mt-3 divide-y divide-gray-200 dark:divide-gray-700'
        ),
        cls='p-5 border border-gray-100 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Time('January 13th, 2022', cls='text-lg font-semibold text-gray-900 dark:text-white'),
        Ol(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Jese Leos', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Bonnie Green', cls='font-medium text-gray-900 dark:text-white'),
                            'react to',
                            Span("Thomas Lean's", cls='font-medium text-gray-900 dark:text-white'),
                            'comment',
                            cls='text-base font-normal text-gray-600 dark:text-gray-400'
                        ),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        )
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            cls='mt-3 divide-y divide-gray-200 dark:divide-gray-700'
        ),
        cls='p-5 mb-4 border border-gray-100 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    ),
    Div(
        Time('January 12th, 2022', cls='text-lg font-semibold text-gray-900 dark:text-white'),
        Ol(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Laura Romeros image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Laura Romeros', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Mike Willi image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Mike Willi', cls='font-medium text-gray-900 dark:text-white'),
                            'react to',
                            Span("Thomas Lean's", cls='font-medium text-gray-900 dark:text-white'),
                            'comment',
                            cls='text-base font-normal text-gray-600 dark:text-gray-400'
                        ),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        )
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese Leos image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Jese Leos', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('How to start with Flowbite library', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 0 19 9.5 9.5 0 0 0 0-19ZM8.374 17.4a7.6 7.6 0 0 1-5.9-7.4c0-.83.137-1.655.406-2.441l.239.019a3.887 3.887 0 0 1 2.082 2.5 4.1 4.1 0 0 0 2.441 2.8c1.148.522 1.389 2.007.732 4.522Zm3.6-8.829a.997.997 0 0 0-.027-.225 5.456 5.456 0 0 0-2.811-3.662c-.832-.527-1.347-.854-1.486-1.89a7.584 7.584 0 0 1 8.364 2.47c-1.387.208-2.14 2.237-2.14 3.307a1.187 1.187 0 0 1-1.9 0Zm1.626 8.053-.671-2.013a1.9 1.9 0 0 1 1.771-1.757l2.032.619a7.553 7.553 0 0 1-3.132 3.151Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Public',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-12 h-12 mb-3 me-3 rounded-full sm:mb-0'),
                    Div(
                        Div(
                            Span('Bonnie Green', cls='font-medium text-gray-900 dark:text-white'),
                            'likes',
                            Span("Bonnie Green's", cls='font-medium text-gray-900 dark:text-white'),
                            'post in',
                            Span('Top figma designs', cls='font-medium text-gray-900 dark:text-white'),
                            cls='text-base font-normal'
                        ),
                        Div('"I wanted to share a webinar zeroheight."', cls='text-sm font-normal'),
                        Span(
                            Svg(
                                Path(d='m2 13.587 3.055-3.055A4.913 4.913 0 0 1 5 10a5.006 5.006 0 0 1 5-5c.178.008.356.026.532.054l1.744-1.744A8.973 8.973 0 0 0 10 3C4.612 3 0 8.336 0 10a6.49 6.49 0 0 0 2 3.587Z'),
                                Path(d='m12.7 8.714 6.007-6.007a1 1 0 1 0-1.414-1.414L11.286 7.3a2.98 2.98 0 0 0-.588-.21l-.035-.01a2.981 2.981 0 0 0-3.584 3.583c0 .012.008.022.01.033.05.204.12.401.211.59l-6.007 6.007a1 1 0 1 0 1.414 1.414L8.714 12.7c.189.091.386.162.59.211.011 0 .021.007.033.01a2.981 2.981 0 0 0 3.584-3.584c0-.012-.008-.023-.011-.035a3.05 3.05 0 0 0-.21-.588Z'),
                                Path(d='M17.821 6.593 14.964 9.45a4.952 4.952 0 0 1-5.514 5.514L7.665 16.75c.767.165 1.55.25 2.335.251 6.453 0 10-5.258 10-7 0-1.166-1.637-2.874-2.179-3.407Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-2.5 h-2.5 me-1'
                            ),
                            'Private',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 dark:text-gray-400'
                        ),
                        cls='text-gray-600 dark:text-gray-400'
                    ),
                    href='#',
                    cls='items-center block p-3 sm:flex hover:bg-gray-100 dark:hover:bg-gray-700'
                )
            ),
            cls='mt-3 divide-y divide-gray-200 dark:divide-gray-700'
        ),
        cls='p-5 border border-gray-100 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
