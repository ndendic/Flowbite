from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The sidebar component can be used as a complementary element relative to the navbar shown on either the left or right side of the page used for the navigation on your web application, including menu items, multi-level menu items, call to actions elements, and more.'),
    H2(
        'Default sidebar',
        Span(id='default-sidebar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default sidebar', href='#default-sidebar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a responsive list of menu items inside the sidebar with icons and labels.'),
    component_showcase(Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='default-sidebar',
        data_drawer_toggle='default-sidebar',
        aria_controls='default-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='default-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='default-sidebar',
        data_drawer_toggle='default-sidebar',
        aria_controls='default-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='default-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    Div(
        A(
            Span(
                Svg(
                    Path(d='M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z', stroke_linecap='round', stroke_linejoin='round', stroke_width='2'),
                    fill='none',
                    stroke='currentColor',
                    viewbox='0 0 24 24',
                    xmlns='http://www.w3.org/2000/svg',
                    cls='w-4 h-4'
                ),
                aria_hidden='true',
                cls='text-xs bg-primary-600 rounded-full text-white px-3 py-1.5 mr-3'
            ),
            Span('Requires Fastbite JS', cls='text-sm font-medium'),
            Svg(
                Path(d='m1 9 4-4-4-4', stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2'),
                aria_hidden='true',
                fill='none',
                viewbox='0 0 6 10',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-2.5 h-2.5 ml-2.5'
            ),
            aria_label='Component requires Fastbite JavaScript',
            href='/docs/getting-started/quickstart/',
            cls='inline-flex items-center justify-between px-1 py-1 pr-4 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700'
        ),
        cls='mt-8 -mb-5'
    ),
    H2(
        'Multi-level menu',
        Span(id='multi-level-menu', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Multi-level menu', href='#multi-level-menu', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this sidebar example to create multi-level menu items by applying the',
        Code('data-collapse-toggle="id"'),
        'data attribute from Fastbite and toggle the second-level menu item.'
    ),
    component_showcase(Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='sidebar-multi-level-sidebar',
        data_drawer_toggle='sidebar-multi-level-sidebar',
        aria_controls='sidebar-multi-level-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    Button(
                        Svg(
                            Path(d='M15 12a1 1 0 0 0 .962-.726l2-7A1 1 0 0 0 17 3H3.77L3.175.745A1 1 0 0 0 2.208 0H1a1 1 0 0 0 0 2h.438l.6 2.255v.019l2 7 .746 2.986A3 3 0 1 0 9 17a2.966 2.966 0 0 0-.184-1h2.368c-.118.32-.18.659-.184 1a3 3 0 1 0 3-3H6.78l-.5-2H15Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 21',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white'
                        ),
                        Span('E-commerce', cls='flex-1 ms-3 text-left rtl:text-right whitespace-nowrap'),
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-3 h-3'
                        ),
                        type='button',
                        aria_controls='dropdown-example',
                        data_collapse_toggle='dropdown-example',
                        cls='flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700'
                    ),
                    Ul(
                        Li(
                            A('Products', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        Li(
                            A('Billing', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        Li(
                            A('Invoice', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        id='dropdown-example',
                        cls='hidden py-2 space-y-2'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='sidebar-multi-level-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='sidebar-multi-level-sidebar',
        data_drawer_toggle='sidebar-multi-level-sidebar',
        aria_controls='sidebar-multi-level-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    Button(
                        Svg(
                            Path(d='M15 12a1 1 0 0 0 .962-.726l2-7A1 1 0 0 0 17 3H3.77L3.175.745A1 1 0 0 0 2.208 0H1a1 1 0 0 0 0 2h.438l.6 2.255v.019l2 7 .746 2.986A3 3 0 1 0 9 17a2.966 2.966 0 0 0-.184-1h2.368c-.118.32-.18.659-.184 1a3 3 0 1 0 3-3H6.78l-.5-2H15Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 21',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white'
                        ),
                        Span('E-commerce', cls='flex-1 ms-3 text-left rtl:text-right whitespace-nowrap'),
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-3 h-3'
                        ),
                        type='button',
                        aria_controls='dropdown-example',
                        data_collapse_toggle='dropdown-example',
                        cls='flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700'
                    ),
                    Ul(
                        Li(
                            A('Products', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        Li(
                            A('Billing', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        Li(
                            A('Invoice', href='#', cls='flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700')
                        ),
                        id='dropdown-example',
                        cls='hidden py-2 space-y-2'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='sidebar-multi-level-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Content separator',
        Span(id='content-separator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Content separator', href='#content-separator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Separate the content inside the sidebar component by applying a border separator between the two menus.'),
    component_showcase(Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='separator-sidebar',
        data_drawer_toggle='separator-sidebar',
        aria_controls='separator-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M7.958 19.393a7.7 7.7 0 0 1-6.715-3.439c-2.868-4.832 0-9.376.944-10.654l.091-.122a3.286 3.286 0 0 0 .765-3.288A1 1 0 0 1 4.6.8c.133.1.313.212.525.347A10.451 10.451 0 0 1 10.6 9.3c.5-1.06.772-2.213.8-3.385a1 1 0 0 1 1.592-.758c1.636 1.205 4.638 6.081 2.019 10.441a8.177 8.177 0 0 1-7.053 3.795Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 17 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Upgrade to Pro', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Documentation', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M18 0H6a2 2 0 0 0-2 2h14v12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            Path(d='M14 4H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM2 16v-6h12v6H2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Components', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 21',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Help', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                cls='pt-4 mt-4 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='separator-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='separator-sidebar',
        data_drawer_toggle='separator-sidebar',
        aria_controls='separator-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M7.958 19.393a7.7 7.7 0 0 1-6.715-3.439c-2.868-4.832 0-9.376.944-10.654l.091-.122a3.286 3.286 0 0 0 .765-3.288A1 1 0 0 1 4.6.8c.133.1.313.212.525.347A10.451 10.451 0 0 1 10.6 9.3c.5-1.06.772-2.213.8-3.385a1 1 0 0 1 1.592-.758c1.636 1.205 4.638 6.081 2.019 10.441a8.177 8.177 0 0 1-7.053 3.795Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 17 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Upgrade to Pro', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Documentation', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M18 0H6a2 2 0 0 0-2 2h14v12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            Path(d='M14 4H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2ZM2 16v-6h12v6H2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Components', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 21',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Help', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 transition duration-75 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 dark:text-white group'
                    )
                ),
                cls='pt-4 mt-4 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='separator-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'CTA button',
        Span(id='cta-button', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: CTA button', href='#cta-button', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to add a CTA button inside the sidebar component and encourage your users to visit the dedicated page.'),
    component_showcase(Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='cta-button-sidebar',
        data_drawer_toggle='cta-button-sidebar',
        aria_controls='cta-button-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            Div(
                Div(
                    Span('Beta', cls='bg-orange-100 text-orange-800 text-sm font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-orange-200 dark:text-orange-900'),
                    Button(
                        Span('Close', cls='sr-only'),
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-2.5 h-2.5'
                        ),
                        type='button',
                        data_dismiss_target='#dropdown-cta',
                        aria_label='Close',
                        cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 inline-flex justify-center items-center w-6 h-6 text-primary-900 rounded-lg focus:ring-2 focus:ring-primary-400 p-1 hover:bg-primary-200 dark:bg-primary-900 dark:text-primary-400 dark:hover:bg-primary-800'
                    ),
                    cls='flex items-center mb-3'
                ),
                P('Preview the new Fastbite dashboard navigation! You can turn the new navigation off for a limited time in your profile.', cls='mb-3 text-sm text-primary-800 dark:text-primary-400'),
                A('Turn new navigation off', href='#', cls='text-sm text-primary-800 underline font-medium hover:text-primary-900 dark:text-primary-400 dark:hover:text-primary-300'),
                id='dropdown-cta',
                role='alert',
                cls='p-4 mt-6 rounded-lg bg-primary-50 dark:bg-primary-900'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='cta-button-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='cta-button-sidebar',
        data_drawer_toggle='cta-button-sidebar',
        aria_controls='cta-button-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            Div(
                Div(
                    Span('Beta', cls='bg-orange-100 text-orange-800 text-sm font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-orange-200 dark:text-orange-900'),
                    Button(
                        Span('Close', cls='sr-only'),
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-2.5 h-2.5'
                        ),
                        type='button',
                        data_dismiss_target='#dropdown-cta',
                        aria_label='Close',
                        cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 inline-flex justify-center items-center w-6 h-6 text-primary-900 rounded-lg focus:ring-2 focus:ring-primary-400 p-1 hover:bg-primary-200 dark:bg-primary-900 dark:text-primary-400 dark:hover:bg-primary-800'
                    ),
                    cls='flex items-center mb-3'
                ),
                P('Preview the new Fastbite dashboard navigation! You can turn the new navigation off for a limited time in your profile.', cls='mb-3 text-sm text-primary-800 dark:text-primary-400'),
                A('Turn new navigation off', href='#', cls='text-sm text-primary-800 underline font-medium hover:text-primary-900 dark:text-primary-400 dark:hover:text-primary-300'),
                id='dropdown-cta',
                role='alert',
                cls='p-4 mt-6 rounded-lg bg-primary-50 dark:bg-primary-900'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='cta-button-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Logo branding',
        Span(id='logo-branding', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Logo branding', href='#logo-branding', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Show the logo of your brand and link back to the homepage from the top part of the sidebar.'),
    component_showcase(Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='logo-sidebar',
        data_drawer_toggle='logo-sidebar',
        aria_controls='logo-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            A(
                Img(src='images/logo.png', alt='Fastbite Logo', cls='h-6 me-3 sm:h-7'),
                Span('Fastbite', cls='self-center text-xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center ps-2.5 mb-5'
            ),
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Button(
        Span('Open sidebar', cls='sr-only'),
        Svg(
            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
            aria_hidden='true',
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-6 h-6'
        ),
        data_drawer_target='logo-sidebar',
        data_drawer_toggle='logo-sidebar',
        aria_controls='logo-sidebar',
        type='button',
        cls='inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
    ),
    Aside(
        Div(
            A(
                Img(src='images/logo.png', alt='Fastbite Logo', cls='h-6 me-3 sm:h-7'),
                Span('Fastbite', cls='self-center text-xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center ps-2.5 mb-5'
            ),
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Sidebar with navbar',
        Span(id='sidebar-with-navbar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sidebar with navbar', href='#sidebar-with-navbar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a navbar together with a sidebar layout for your web application.'),
    component_showcase(Div(
    Nav(
        Div(
            Div(
                Div(
                    Button(
                        Span('Open sidebar', cls='sr-only'),
                        Svg(
                            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
                            aria_hidden='true',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-6 h-6'
                        ),
                        data_drawer_target='logo-sidebar',
                        data_drawer_toggle='logo-sidebar',
                        aria_controls='logo-sidebar',
                        type='button',
                        cls='inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                    ),
                    A(
                        Img(src='images/logo.png', alt='FlowBite Logo', cls='h-8 me-3'),
                        Span('Fastbite', cls='self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white'),
                        href='https://flowbite.com',
                        cls='flex ms-2 md:me-24'
                    ),
                    cls='flex items-center justify-start rtl:justify-end'
                ),
                Div(
                    Div(
                        Div(
                            Button(
                                Span('Open user menu', cls='sr-only'),
                                Img(src='https://flowbite.com/docs/images/people/profile-picture-5.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
                                type='button',
                                aria_expanded='false',
                                data_dropdown_toggle='dropdown-user',
                                cls='flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
                            )
                        ),
                        Div(
                            Div(
                                P('Neil Sims', role='none', cls='text-sm text-gray-900 dark:text-white'),
                                P('neil.sims@fastbite.com', role='none', cls='text-sm font-medium text-gray-900 truncate dark:text-gray-300'),
                                role='none',
                                cls='px-4 py-3'
                            ),
                            Ul(
                                Li(
                                    A('Dashboard', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Settings', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Earnings', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Sign out', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                role='none',
                                cls='py-1'
                            ),
                            id='dropdown-user',
                            cls='z-50 hidden my-4 text-base list-none bg-gray-50 divide-y divide-gray-100 rounded-sm shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                        ),
                        cls='flex items-center ms-3'
                    ),
                    cls='flex items-center'
                ),
                cls='flex items-center justify-between'
            ),
            cls='px-3 py-3 lg:px-5 lg:pl-3'
        ),
        cls='fixed top-0 z-50 w-full bg-gray-50 border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 pb-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-gray-50 border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14'
        ),
        cls='p-4 sm:ml-64'
    )
), code="""Div(
    Nav(
        Div(
            Div(
                Div(
                    Button(
                        Span('Open sidebar', cls='sr-only'),
                        Svg(
                            Path(clip_rule='evenodd', fill_rule='evenodd', d='M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z'),
                            aria_hidden='true',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-6 h-6'
                        ),
                        data_drawer_target='logo-sidebar',
                        data_drawer_toggle='logo-sidebar',
                        aria_controls='logo-sidebar',
                        type='button',
                        cls='inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                    ),
                    A(
                        Img(src='images/logo.png', alt='FlowBite Logo', cls='h-8 me-3'),
                        Span('Fastbite', cls='self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white'),
                        href='https://flowbite.com',
                        cls='flex ms-2 md:me-24'
                    ),
                    cls='flex items-center justify-start rtl:justify-end'
                ),
                Div(
                    Div(
                        Div(
                            Button(
                                Span('Open user menu', cls='sr-only'),
                                Img(src='https://flowbite.com/docs/images/people/profile-picture-5.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
                                type='button',
                                aria_expanded='false',
                                data_dropdown_toggle='dropdown-user',
                                cls='flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
                            )
                        ),
                        Div(
                            Div(
                                P('Neil Sims', role='none', cls='text-sm text-gray-900 dark:text-white'),
                                P('neil.sims@fastbite.com', role='none', cls='text-sm font-medium text-gray-900 truncate dark:text-gray-300'),
                                role='none',
                                cls='px-4 py-3'
                            ),
                            Ul(
                                Li(
                                    A('Dashboard', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Settings', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Earnings', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Sign out', href='#', role='menuitem', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                role='none',
                                cls='py-1'
                            ),
                            id='dropdown-user',
                            cls='z-50 hidden my-4 text-base list-none bg-gray-50 divide-y divide-gray-100 rounded-sm shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                        ),
                        cls='flex items-center ms-3'
                    ),
                    cls='flex items-center'
                ),
                cls='flex items-center justify-between'
            ),
            cls='px-3 py-3 lg:px-5 lg:pl-3'
        ),
        cls='fixed top-0 z-50 w-full bg-gray-50 border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700'
    ),
    Aside(
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 pb-4 overflow-y-auto bg-gray-50 dark:bg-gray-800'
        ),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-gray-50 border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center h-24 rounded-sm bg-gray-50 dark:bg-gray-800'
                ),
                cls='grid grid-cols-3 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4 mb-4'
            ),
            Div(
                P(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5'
                    ),
                    cls='text-2xl text-gray-400 dark:text-gray-500'
                ),
                cls='flex items-center justify-center h-48 mb-4 rounded-sm bg-gray-50 dark:bg-gray-800'
            ),
            Div(
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                Div(
                    P(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 18',
                            cls='w-3.5 h-3.5'
                        ),
                        cls='text-2xl text-gray-400 dark:text-gray-500'
                    ),
                    cls='flex items-center justify-center rounded-sm bg-gray-50 h-28 dark:bg-gray-800'
                ),
                cls='grid grid-cols-2 gap-4'
            ),
            cls='p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14'
        ),
        cls='p-4 sm:ml-64'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Off-canvas sidebar',
        Span(id='off-canvas-sidebar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Off-canvas sidebar', href='#off-canvas-sidebar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show the navigation as an off-canvas drawer component when clicking on an element.'),
    component_showcase(Div(
    Div(
        Button('Show navigation', type='button', data_drawer_target='drawer-navigation', data_drawer_show='drawer-navigation', aria_controls='drawer-navigation', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='text-center'
    ),
    Div(
        H5('Menu', id='drawer-navigation-label', cls='text-base font-semibold text-gray-500 uppercase dark:text-gray-400'),
        Button(
            Svg(
                Path(fill_rule='evenodd', d='M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z', clip_rule='evenodd'),
                aria_hidden='true',
                fill='currentColor',
                viewbox='0 0 20 20',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-5 h-5'
            ),
            Span('Close menu', cls='sr-only'),
            type='button',
            data_drawer_hide='drawer-navigation',
            aria_controls='drawer-navigation',
            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 absolute top-2.5 end-2.5 inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white'
        ),
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='py-4 overflow-y-auto'
        ),
        id='drawer-navigation',
        tabindex='-1',
        aria_labelledby='drawer-navigation-label',
        cls='fixed top-0 left-0 z-40 w-64 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-gray-50 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Button('Show navigation', type='button', data_drawer_target='drawer-navigation', data_drawer_show='drawer-navigation', aria_controls='drawer-navigation', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='text-center'
    ),
    Div(
        H5('Menu', id='drawer-navigation-label', cls='text-base font-semibold text-gray-500 uppercase dark:text-gray-400'),
        Button(
            Svg(
                Path(fill_rule='evenodd', d='M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z', clip_rule='evenodd'),
                aria_hidden='true',
                fill='currentColor',
                viewbox='0 0 20 20',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-5 h-5'
            ),
            Span('Close menu', cls='sr-only'),
            type='button',
            data_drawer_hide='drawer-navigation',
            aria_controls='drawer-navigation',
            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 absolute top-2.5 end-2.5 inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white'
        ),
        Div(
            Ul(
                Li(
                    A(
                        Svg(
                            Path(d='M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z'),
                            Path(d='M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 22 21',
                            cls='w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Dashboard', cls='ms-3'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Kanban', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('Pro', cls='inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Inbox', cls='flex-1 ms-3 whitespace-nowrap'),
                        Span('3', cls='inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-primary-800 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Users', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Products', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 18 16',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign In', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                Li(
                    A(
                        Svg(
                            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                            Path(d='M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z'),
                            Path(d='M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
                        ),
                        Span('Sign Up', cls='flex-1 ms-3 whitespace-nowrap'),
                        href='#',
                        cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
                    )
                ),
                cls='space-y-2 font-medium'
            ),
            cls='py-4 overflow-y-auto'
        ),
        id='drawer-navigation',
        tabindex='-1',
        aria_labelledby='drawer-navigation-label',
        cls='fixed top-0 left-0 z-40 w-64 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-gray-50 dark:bg-gray-800'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can check out more',
        A('sidenav component', href='https://flowbite.com/blocks/application/sidenav/'),
        'examples and',
        A('application shell layouts', href='https://flowbite.com/blocks/application/shells/'),
        'from Fastbite Blocks.'
    ),
    H2(
        'Dashboard Layout',
        Span(id='dashboard-layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dashboard Layout', href='#dashboard-layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'These sidebar examples can be viewed in action and used by checking out the',
        A('Fastbite Admin Dashboard', href='https://github.com/themesberg/flowbite-admin-dashboard'),
        'template and use it as a solid starting point for you web application.'
    ),
    id='mainContent'
)
