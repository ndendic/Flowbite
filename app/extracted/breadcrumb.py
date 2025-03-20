from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The breadcrumb component is an important part of any website or application that can be used to show the current location of a page in a hierarchical structure of pages.'),
    P('Flowbite includes two styles of breadcrumb elements, one that has a transparent background and a few more that come with a background in different colors.'),
    H2(
        'Default breadcrumb',
        Span(id='default-breadcrumb', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default breadcrumb', href='#default-breadcrumb', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following breadcrumb example to show the hierarchical structure of pages.'),
    component_showcase(Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 text-gray-400 mx-1'
                    ),
                    A('Projects', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 text-gray-400 mx-1'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex'
    )
), code="""Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 text-gray-400 mx-1'
                    ),
                    A('Projects', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 text-gray-400 mx-1'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Solid background',
        Span(id='solid-background', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Solid background', href='#solid-background', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can alternatively also use the breadcrumb components with a solid background.'),
    component_showcase(Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 block w-3 h-3 mx-1 text-gray-400'
                    ),
                    A('Templates', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex px-5 py-3 text-gray-700 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 block w-3 h-3 mx-1 text-gray-400'
                    ),
                    A('Templates', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex px-5 py-3 text-gray-700 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Header breadcrumb',
        Span(id='header-breadcrumb', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Header breadcrumb', href='#header-breadcrumb', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a list of items such as the branches from GitHub and a dropdown component.'),
    component_showcase(Div(
    Nav(
        Ol(
            Li(
                Div(
                    A('flowbite.com', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    A('develop', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    Span('Issue #312', cls='mx-1 text-sm font-medium text-gray-500 md:mx-2 dark:text-gray-400'),
                    Span('docs', cls='bg-primary-100 text-primary-800 text-xs font-semibold me-2 px-2 py-0.5 rounded-sm dark:bg-primary-200 dark:text-primary-800 hidden sm:flex'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center mb-3 space-x-1 md:space-x-2 rtl:space-x-reverse sm:mb-0'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm9-10v.4A3.6 3.6 0 0 1 8.4 9H6.61A3.6 3.6 0 0 0 3 12.605M14.458 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 20',
                    cls='w-3 h-3 me-2'
                ),
                'Fix #6597',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdownDefault',
                data_dropdown_toggle='dropdown',
                cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-600 bg-gray-200 rounded-lg hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-gray-300 dark:focus:ring-gray-700'
            ),
            Div(
                Ul(
                    Li(
                        A('New branch', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Rename', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdownDefault',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            )
        ),
        aria_label='Breadcrumb',
        cls='justify-between px-4 py-3 text-gray-700 border border-gray-200 rounded-lg sm:flex sm:px-5 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Ol(
            Li(
                Div(
                    A('flowbite.com', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    A('develop', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='rtl:rotate-180 w-3 h-3 mx-1 text-gray-400'
                    ),
                    Span('Issue #312', cls='mx-1 text-sm font-medium text-gray-500 md:mx-2 dark:text-gray-400'),
                    Span('docs', cls='bg-primary-100 text-primary-800 text-xs font-semibold me-2 px-2 py-0.5 rounded-sm dark:bg-primary-200 dark:text-primary-800 hidden sm:flex'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center mb-3 space-x-1 md:space-x-2 rtl:space-x-reverse sm:mb-0'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm9-10v.4A3.6 3.6 0 0 1 8.4 9H6.61A3.6 3.6 0 0 0 3 12.605M14.458 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 20',
                    cls='w-3 h-3 me-2'
                ),
                'Fix #6597',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdownDefault',
                data_dropdown_toggle='dropdown',
                cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-600 bg-gray-200 rounded-lg hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-gray-300 dark:focus:ring-gray-700'
            ),
            Div(
                Ul(
                    Li(
                        A('New branch', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Rename', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdownDefault',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            )
        ),
        aria_label='Breadcrumb',
        cls='justify-between px-4 py-3 text-gray-700 border border-gray-200 rounded-lg sm:flex sm:px-5 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Breadcrumb with dropdown',
        Span(id='breadcrumb-with-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Breadcrumb with dropdown', href='#breadcrumb-with-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show dropdown components inside the breadcrumbs.'),
    component_showcase(Div(
    Nav(
        Ol(
            Li(
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm9-10v.4A3.6 3.6 0 0 1 8.4 9H6.61A3.6 3.6 0 0 0 3 12.605M14.458 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 20',
                            cls='w-3 h-3 me-2'
                        ),
                        'flowbite.com',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-2.5 h-2.5 ms-2.5'
                        ),
                        id='dropdownProject',
                        data_dropdown_toggle='dropdown-project',
                        cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-900 dark:hover:bg-gray-800 dark:text-white dark:focus:ring-gray-700'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('themesberg.com', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('ui.glass', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('iconscale', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdownDefault',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-project',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    ),
                    cls='flex items-center'
                )
            ),
            Span('/', cls='mx-2 text-gray-400'),
            Li(
                Div(
                    Button(
                        Svg(
                            Path(d='M8 5.625c4.418 0 8-1.063 8-2.375S12.418.875 8 .875 0 1.938 0 3.25s3.582 2.375 8 2.375Zm0 13.5c4.963 0 8-1.538 8-2.375v-4.019c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353c-.193.081-.394.158-.6.231l-.189.067c-2.04.628-4.165.936-6.3.911a20.601 20.601 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244c-.053-.028-.113-.053-.165-.082v4.019C0 17.587 3.037 19.125 8 19.125Zm7.09-12.709c-.193.081-.394.158-.6.231l-.189.067a20.6 20.6 0 0 1-6.3.911 20.6 20.6 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244C.112 6.035.052 6.01 0 5.981V10c0 .837 3.037 2.375 8 2.375s8-1.538 8-2.375V5.981c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='w-3 h-3 me-2'
                        ),
                        'databaseName',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-2.5 h-2.5 ms-2.5'
                        ),
                        id='dropdownDatabase',
                        data_dropdown_toggle='dropdown-database',
                        cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-900 dark:hover:bg-gray-800 dark:text-white dark:focus:ring-gray-700'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('databaseProd', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('databaseStaging', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('flowbiteProd', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdownDefault',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-database',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    ),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center mb-3 sm:mb-0'
        ),
        aria_label='Breadcrumb',
        cls='flex justify-between'
    )
), code="""Div(
    Nav(
        Ol(
            Li(
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm9-10v.4A3.6 3.6 0 0 1 8.4 9H6.61A3.6 3.6 0 0 0 3 12.605M14.458 3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 20',
                            cls='w-3 h-3 me-2'
                        ),
                        'flowbite.com',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-2.5 h-2.5 ms-2.5'
                        ),
                        id='dropdownProject',
                        data_dropdown_toggle='dropdown-project',
                        cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-900 dark:hover:bg-gray-800 dark:text-white dark:focus:ring-gray-700'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('themesberg.com', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('ui.glass', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('iconscale', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdownDefault',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-project',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    ),
                    cls='flex items-center'
                )
            ),
            Span('/', cls='mx-2 text-gray-400'),
            Li(
                Div(
                    Button(
                        Svg(
                            Path(d='M8 5.625c4.418 0 8-1.063 8-2.375S12.418.875 8 .875 0 1.938 0 3.25s3.582 2.375 8 2.375Zm0 13.5c4.963 0 8-1.538 8-2.375v-4.019c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353c-.193.081-.394.158-.6.231l-.189.067c-2.04.628-4.165.936-6.3.911a20.601 20.601 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244c-.053-.028-.113-.053-.165-.082v4.019C0 17.587 3.037 19.125 8 19.125Zm7.09-12.709c-.193.081-.394.158-.6.231l-.189.067a20.6 20.6 0 0 1-6.3.911 20.6 20.6 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244C.112 6.035.052 6.01 0 5.981V10c0 .837 3.037 2.375 8 2.375s8-1.538 8-2.375V5.981c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='w-3 h-3 me-2'
                        ),
                        'databaseName',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 10 6',
                            cls='w-2.5 h-2.5 ms-2.5'
                        ),
                        id='dropdownDatabase',
                        data_dropdown_toggle='dropdown-database',
                        cls='inline-flex items-center px-3 py-2 text-sm font-normal text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-900 dark:hover:bg-gray-800 dark:text-white dark:focus:ring-gray-700'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('databaseProd', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('databaseStaging', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('flowbiteProd', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdownDefault',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-database',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    ),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center mb-3 sm:mb-0'
        ),
        aria_label='Breadcrumb',
        cls='flex justify-between'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    id='mainContent'
)
