from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('The tabs component can be used either as an extra navigational hierarchy complementing the main navbar or you can also use it to change content inside a container just below the tabs using the data attributes from Flowbite.'),
    H2(
        'Default tabs',
        Span(id='default-tabs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default tabs', href='#default-tabs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following default tabs component example to show a list of links that the user can navigate from on your website.'),
    component_showcase(Div(
    Ul(
        Li(
            A('Profile', href='#', aria_current='page', cls='inline-block p-4 text-primary-600 bg-gray-100 rounded-t-lg active dark:bg-gray-800 dark:text-primary-500'),
            cls='me-2'
        ),
        Li(
            A('Dashboard', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Settings', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Contacts', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
        ),
        cls='flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400'
    )
), code="""Div(
    Ul(
        Li(
            A('Profile', href='#', aria_current='page', cls='inline-block p-4 text-primary-600 bg-gray-100 rounded-t-lg active dark:bg-gray-800 dark:text-primary-500'),
            cls='me-2'
        ),
        Li(
            A('Dashboard', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Settings', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Contacts', href='#', cls='inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300'),
            cls='me-2'
        ),
        Li(
            A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
        ),
        cls='flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Tabs with underline',
        Span(id='tabs-with-underline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Tabs with underline', href='#tabs-with-underline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this alternative tabs component style with an underline instead of a background when hovering and being active on a certain page.'),
    component_showcase(Div(
    Div(
        Ul(
            Li(
                A('Profile', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Dashboard', href='#', aria_current='page', cls='inline-block p-4 text-primary-600 border-b-2 border-primary-600 rounded-t-lg active dark:text-primary-500 dark:border-primary-500'),
                cls='me-2'
            ),
            Li(
                A('Settings', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Contacts', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
            ),
            cls='flex flex-wrap -mb-px'
        ),
        cls='text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Ul(
            Li(
                A('Profile', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Dashboard', href='#', aria_current='page', cls='inline-block p-4 text-primary-600 border-b-2 border-primary-600 rounded-t-lg active dark:text-primary-500 dark:border-primary-500'),
                cls='me-2'
            ),
            Li(
                A('Settings', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Contacts', href='#', cls='inline-block p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                cls='me-2'
            ),
            Li(
                A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
            ),
            cls='flex flex-wrap -mb-px'
        ),
        cls='text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Tabs with icons',
        Span(id='tabs-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Tabs with icons', href='#tabs-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This is an example of the tabs component where you can also use a SVG powered icon to complement the text within the navigational tabs.'),
    component_showcase(Div(
    Div(
        Ul(
            Li(
                A(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Profile',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-4 h-4 me-2 text-primary-600 dark:text-primary-500'
                    ),
                    'Dashboard',
                    href='#',
                    aria_current='page',
                    cls='inline-flex items-center justify-center p-4 text-primary-600 border-b-2 border-primary-600 rounded-t-lg active dark:text-primary-500 dark:border-primary-500 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M5 11.424V1a1 1 0 1 0-2 0v10.424a3.228 3.228 0 0 0 0 6.152V19a1 1 0 1 0 2 0v-1.424a3.228 3.228 0 0 0 0-6.152ZM19.25 14.5A3.243 3.243 0 0 0 17 11.424V1a1 1 0 0 0-2 0v10.424a3.227 3.227 0 0 0 0 6.152V19a1 1 0 1 0 2 0v-1.424a3.243 3.243 0 0 0 2.25-3.076Zm-6-9A3.243 3.243 0 0 0 11 2.424V1a1 1 0 0 0-2 0v1.424a3.228 3.228 0 0 0 0 6.152V19a1 1 0 1 0 2 0V8.576A3.243 3.243 0 0 0 13.25 5.5Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Settings',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Contacts',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
            ),
            cls='flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400'
        ),
        cls='border-b border-gray-200 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Ul(
            Li(
                A(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Profile',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-4 h-4 me-2 text-primary-600 dark:text-primary-500'
                    ),
                    'Dashboard',
                    href='#',
                    aria_current='page',
                    cls='inline-flex items-center justify-center p-4 text-primary-600 border-b-2 border-primary-600 rounded-t-lg active dark:text-primary-500 dark:border-primary-500 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M5 11.424V1a1 1 0 1 0-2 0v10.424a3.228 3.228 0 0 0 0 6.152V19a1 1 0 1 0 2 0v-1.424a3.228 3.228 0 0 0 0-6.152ZM19.25 14.5A3.243 3.243 0 0 0 17 11.424V1a1 1 0 0 0-2 0v10.424a3.227 3.227 0 0 0 0 6.152V19a1 1 0 1 0 2 0v-1.424a3.243 3.243 0 0 0 2.25-3.076Zm-6-9A3.243 3.243 0 0 0 11 2.424V1a1 1 0 0 0-2 0v1.424a3.228 3.228 0 0 0 0 6.152V19a1 1 0 1 0 2 0V8.576A3.243 3.243 0 0 0 13.25 5.5Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Settings',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4 me-2 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-300'
                    ),
                    'Contacts',
                    href='#',
                    cls='inline-flex items-center justify-center p-4 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300 group'
                ),
                cls='me-2'
            ),
            Li(
                A('Disabled', cls='inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500')
            ),
            cls='flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400'
        ),
        cls='border-b border-gray-200 dark:border-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Pills tabs',
        Span(id='pills-tabs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pills tabs', href='#pills-tabs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you want to use pills as a style for the tabs component you can do so by using this example.'),
    component_showcase(Div(
    Ul(
        Li(
            A('Tab 1', href='#', aria_current='page', cls='inline-block px-4 py-3 text-white bg-primary-600 rounded-lg active'),
            cls='me-2'
        ),
        Li(
            A('Tab 2', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 3', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 4', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 5', cls='inline-block px-4 py-3 text-gray-400 cursor-not-allowed dark:text-gray-500')
        ),
        cls='flex flex-wrap text-sm font-medium text-center text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    Ul(
        Li(
            A('Tab 1', href='#', aria_current='page', cls='inline-block px-4 py-3 text-white bg-primary-600 rounded-lg active'),
            cls='me-2'
        ),
        Li(
            A('Tab 2', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 3', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 4', href='#', cls='inline-block px-4 py-3 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white'),
            cls='me-2'
        ),
        Li(
            A('Tab 5', cls='inline-block px-4 py-3 text-gray-400 cursor-not-allowed dark:text-gray-500')
        ),
        cls='flex flex-wrap text-sm font-medium text-center text-gray-500 dark:text-gray-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Vertical tabs',
        Span(id='vertical-tabs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Vertical tabs', href='#vertical-tabs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a vertically aligned set of tabs on the left side of the page.'),
    component_showcase(Div(
    Div(
        Ul(
            Li(
                A(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-white'
                    ),
                    'Profile',
                    href='#',
                    aria_current='page',
                    cls='inline-flex items-center px-4 py-3 text-white bg-primary-700 rounded-lg active w-full dark:bg-primary-600'
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
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Dashboard',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Settings',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M7.824 5.937a1 1 0 0 0 .726-.312 2.042 2.042 0 0 1 2.835-.065 1 1 0 0 0 1.388-1.441 3.994 3.994 0 0 0-5.674.13 1 1 0 0 0 .725 1.688Z'),
                        Path(d='M17 7A7 7 0 1 0 3 7a3 3 0 0 0-3 3v2a3 3 0 0 0 3 3h1a1 1 0 0 0 1-1V7a5 5 0 1 1 10 0v7.083A2.92 2.92 0 0 1 12.083 17H12a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v1a2 2 0 0 0 2 2h1a1.993 1.993 0 0 0 1.722-1h.361a4.92 4.92 0 0 0 4.824-4H17a3 3 0 0 0 3-3v-2a3 3 0 0 0-3-3Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Contact',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 dark:text-gray-500'
                    ),
                    'Disabled',
                    cls='inline-flex items-center px-4 py-3 text-gray-400 rounded-lg cursor-not-allowed bg-gray-50 w-full dark:bg-gray-800 dark:text-gray-500'
                )
            ),
            cls='flex-column space-y space-y-4 text-sm font-medium text-gray-500 dark:text-gray-400 md:me-4 mb-4 md:mb-0'
        ),
        Div(
            H3('Profile Tab', cls='text-lg font-bold text-gray-900 dark:text-white mb-2'),
            P("This is some placeholder content the Profile tab's associated content, clicking another tab will toggle the visibility of this one for the next.", cls='mb-2'),
            P('The tab JavaScript swaps classes to control the content visibility and styling.'),
            cls='p-6 bg-gray-50 text-medium text-gray-500 dark:text-gray-400 dark:bg-gray-800 rounded-lg w-full'
        ),
        cls='md:flex'
    )
), code="""Div(
    Div(
        Ul(
            Li(
                A(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-white'
                    ),
                    'Profile',
                    href='#',
                    aria_current='page',
                    cls='inline-flex items-center px-4 py-3 text-white bg-primary-700 rounded-lg active w-full dark:bg-primary-600'
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
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Dashboard',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Settings',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M7.824 5.937a1 1 0 0 0 .726-.312 2.042 2.042 0 0 1 2.835-.065 1 1 0 0 0 1.388-1.441 3.994 3.994 0 0 0-5.674.13 1 1 0 0 0 .725 1.688Z'),
                        Path(d='M17 7A7 7 0 1 0 3 7a3 3 0 0 0-3 3v2a3 3 0 0 0 3 3h1a1 1 0 0 0 1-1V7a5 5 0 1 1 10 0v7.083A2.92 2.92 0 0 1 12.083 17H12a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v1a2 2 0 0 0 2 2h1a1.993 1.993 0 0 0 1.722-1h.361a4.92 4.92 0 0 0 4.824-4H17a3 3 0 0 0 3-3v-2a3 3 0 0 0-3-3Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                    ),
                    'Contact',
                    href='#',
                    cls='inline-flex items-center px-4 py-3 rounded-lg hover:text-gray-900 bg-gray-50 hover:bg-gray-100 w-full dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Svg(
                        Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 me-2 text-gray-400 dark:text-gray-500'
                    ),
                    'Disabled',
                    cls='inline-flex items-center px-4 py-3 text-gray-400 rounded-lg cursor-not-allowed bg-gray-50 w-full dark:bg-gray-800 dark:text-gray-500'
                )
            ),
            cls='flex-column space-y space-y-4 text-sm font-medium text-gray-500 dark:text-gray-400 md:me-4 mb-4 md:mb-0'
        ),
        Div(
            H3('Profile Tab', cls='text-lg font-bold text-gray-900 dark:text-white mb-2'),
            P("This is some placeholder content the Profile tab's associated content, clicking another tab will toggle the visibility of this one for the next.", cls='mb-2'),
            P('The tab JavaScript swaps classes to control the content visibility and styling.'),
            cls='p-6 bg-gray-50 text-medium text-gray-500 dark:text-gray-400 dark:bg-gray-800 rounded-lg w-full'
        ),
        cls='md:flex'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Full width tabs',
        Span(id='full-width-tabs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Full width tabs', href='#full-width-tabs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you want to show the tabs on the full width relative to the parent element you can do so by using the full width tabs component example.'),
    component_showcase(Div(
    Div(
        Label('Select your country', fr='tabs', cls='sr-only'),
        Select(
            Option('Profile'),
            Option('Dashboard'),
            Option('setting'),
            Option('Invoioce'),
            id='tabs',
            cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        ),
        cls='sm:hidden'
    ),
    Ul(
        Li(
            A('Profile', href='#', aria_current='page', cls='inline-block w-full p-4 text-gray-900 bg-gray-100 border-r border-gray-200 dark:border-gray-700 rounded-s-lg focus:ring-4 focus:ring-primary-300 active focus:outline-none dark:bg-gray-700 dark:text-white'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Dashboard', href='#', cls='inline-block w-full p-4 bg-white border-r border-gray-200 dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-primary-300 focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Settings', href='#', cls='inline-block w-full p-4 bg-white border-r border-gray-200 dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-primary-300 focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Invoice', href='#', cls='inline-block w-full p-4 bg-white border-s-0 border-gray-200 dark:border-gray-700 rounded-e-lg hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        cls='hidden text-sm font-medium text-center text-gray-500 rounded-lg shadow-sm sm:flex dark:divide-gray-700 dark:text-gray-400'
    )
), code="""Div(
    Div(
        Label('Select your country', fr='tabs', cls='sr-only'),
        Select(
            Option('Profile'),
            Option('Dashboard'),
            Option('setting'),
            Option('Invoioce'),
            id='tabs',
            cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        ),
        cls='sm:hidden'
    ),
    Ul(
        Li(
            A('Profile', href='#', aria_current='page', cls='inline-block w-full p-4 text-gray-900 bg-gray-100 border-r border-gray-200 dark:border-gray-700 rounded-s-lg focus:ring-4 focus:ring-primary-300 active focus:outline-none dark:bg-gray-700 dark:text-white'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Dashboard', href='#', cls='inline-block w-full p-4 bg-white border-r border-gray-200 dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-primary-300 focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Settings', href='#', cls='inline-block w-full p-4 bg-white border-r border-gray-200 dark:border-gray-700 hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:ring-primary-300 focus:outline-none dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        Li(
            A('Invoice', href='#', cls='inline-block w-full p-4 bg-white border-s-0 border-gray-200 dark:border-gray-700 rounded-e-lg hover:text-gray-700 hover:bg-gray-50 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'),
            cls='w-full focus-within:z-10'
        ),
        cls='hidden text-sm font-medium text-center text-gray-500 rounded-lg shadow-sm sm:flex dark:divide-gray-700 dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
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
            Span('Requires Flowbite JS', cls='text-sm font-medium'),
            Svg(
                Path(d='m1 9 4-4-4-4', stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2'),
                aria_hidden='true',
                fill='none',
                viewbox='0 0 6 10',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-2.5 h-2.5 ml-2.5'
            ),
            aria_label='Component requires Flowbite JavaScript',
            href='/docs/getting-started/quickstart/',
            cls='inline-flex items-center justify-between px-1 py-1 pr-4 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700'
        ),
        cls='mt-8 -mb-5'
    ),
    H2(
        'Interactive tabs',
        Span(id='interactive-tabs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Interactive tabs', href='#interactive-tabs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the dynamic tabs component to interactively show and hide the content below the tabs based on the currently active tab item. Make sure that you initialize the component by using the',
        Code('data-tabs-toggle="{parentTabContentSelector}"'),
        'and also apply an',
        Code('id'),
        'attribute to the same element.'
    ),
    P(
        'Each tab toggle button requires a',
        Code('role="tab"'),
        'attribute and a',
        Code('data-tabs-target="{tabContentSelector}"'),
        'to target the tab content element that will be shown when clicked.'
    ),
    P(
        'Use the',
        Code('aria-selected="true"'),
        'data attribute so that Flowbite can target the currently active tab component and hide it when another is shown. If not set, it will show the first tab as active.'
    ),
    P(
        'Apply the',
        Code('role="tabpanel"'),
        'data attribute to every tab content element and set the',
        Code('id'),
        'attribute which will be equal to the',
        Code('data-tabs-target={tabContentSelector}'),
        'from the tabs toggles.'
    ),
    P('You can use multiple tab components on a single page but make sure that the id’s are different.'),
    component_showcase(Div(
    Div(
        Ul(
            Li(
                Button('Profile', id='profile-tab', data_tabs_target='#profile', type='button', role='tab', aria_controls='profile', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Dashboard', id='dashboard-tab', data_tabs_target='#dashboard', type='button', role='tab', aria_controls='dashboard', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Settings', id='settings-tab', data_tabs_target='#settings', type='button', role='tab', aria_controls='settings', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Contacts', id='contacts-tab', data_tabs_target='#contacts', type='button', role='tab', aria_controls='contacts', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation'
            ),
            id='default-tab',
            data_tabs_toggle='#default-tab-content',
            role='tablist',
            cls='flex flex-wrap -mb-px text-sm font-medium text-center'
        ),
        cls='mb-4 border-b border-gray-200 dark:border-gray-700'
    ),
    Div(
        Div(
            P(
                'This is some placeholder content the',
                Strong("Profile tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='profile',
            role='tabpanel',
            aria_labelledby='profile-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Dashboard tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='dashboard',
            role='tabpanel',
            aria_labelledby='dashboard-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Settings tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='settings',
            role='tabpanel',
            aria_labelledby='settings-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Contacts tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='contacts',
            role='tabpanel',
            aria_labelledby='contacts-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        id='default-tab-content'
    )
), code="""Div(
    Div(
        Ul(
            Li(
                Button('Profile', id='profile-tab', data_tabs_target='#profile', type='button', role='tab', aria_controls='profile', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Dashboard', id='dashboard-tab', data_tabs_target='#dashboard', type='button', role='tab', aria_controls='dashboard', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Settings', id='settings-tab', data_tabs_target='#settings', type='button', role='tab', aria_controls='settings', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Contacts', id='contacts-tab', data_tabs_target='#contacts', type='button', role='tab', aria_controls='contacts', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation'
            ),
            id='default-tab',
            data_tabs_toggle='#default-tab-content',
            role='tablist',
            cls='flex flex-wrap -mb-px text-sm font-medium text-center'
        ),
        cls='mb-4 border-b border-gray-200 dark:border-gray-700'
    ),
    Div(
        Div(
            P(
                'This is some placeholder content the',
                Strong("Profile tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='profile',
            role='tabpanel',
            aria_labelledby='profile-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Dashboard tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='dashboard',
            role='tabpanel',
            aria_labelledby='dashboard-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Settings tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='settings',
            role='tabpanel',
            aria_labelledby='settings-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Contacts tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='contacts',
            role='tabpanel',
            aria_labelledby='contacts-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        id='default-tab-content'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Active tab style',
        Span(id='active-tab-style', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Active tab style', href='#active-tab-style', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-tabs-active-classes'),
        'and the',
        Code('data-tabs-inactive-classes'),
        'to set the active and inactive tab Tailwind CSS classes. In this example we set the active classes to the purple color instead of primary.'
    ),
    component_showcase(Div(
    Div(
        Ul(
            Li(
                Button('Profile', id='profile-styled-tab', data_tabs_target='#styled-profile', type='button', role='tab', aria_controls='profile', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Dashboard', id='dashboard-styled-tab', data_tabs_target='#styled-dashboard', type='button', role='tab', aria_controls='dashboard', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Settings', id='settings-styled-tab', data_tabs_target='#styled-settings', type='button', role='tab', aria_controls='settings', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Contacts', id='contacts-styled-tab', data_tabs_target='#styled-contacts', type='button', role='tab', aria_controls='contacts', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation'
            ),
            id='default-styled-tab',
            data_tabs_toggle='#default-styled-tab-content',
            data_tabs_active_classes='text-purple-600 hover:text-purple-600 dark:text-purple-500 dark:hover:text-purple-500 border-purple-600 dark:border-purple-500',
            data_tabs_inactive_classes='dark:border-transparent text-gray-500 hover:text-gray-600 dark:text-gray-400 border-gray-100 hover:border-gray-300 dark:border-gray-700 dark:hover:text-gray-300',
            role='tablist',
            cls='flex flex-wrap -mb-px text-sm font-medium text-center'
        ),
        cls='mb-4 border-b border-gray-200 dark:border-gray-700'
    ),
    Div(
        Div(
            P(
                'This is some placeholder content the',
                Strong("Profile tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-profile',
            role='tabpanel',
            aria_labelledby='profile-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Dashboard tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-dashboard',
            role='tabpanel',
            aria_labelledby='dashboard-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Settings tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-settings',
            role='tabpanel',
            aria_labelledby='settings-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Contacts tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-contacts',
            role='tabpanel',
            aria_labelledby='contacts-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        id='default-styled-tab-content'
    )
), code="""Div(
    Div(
        Ul(
            Li(
                Button('Profile', id='profile-styled-tab', data_tabs_target='#styled-profile', type='button', role='tab', aria_controls='profile', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Dashboard', id='dashboard-styled-tab', data_tabs_target='#styled-dashboard', type='button', role='tab', aria_controls='dashboard', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Settings', id='settings-styled-tab', data_tabs_target='#styled-settings', type='button', role='tab', aria_controls='settings', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation',
                cls='me-2'
            ),
            Li(
                Button('Contacts', id='contacts-styled-tab', data_tabs_target='#styled-contacts', type='button', role='tab', aria_controls='contacts', aria_selected='false', cls='inline-block p-4 border-b-2 rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300'),
                role='presentation'
            ),
            id='default-styled-tab',
            data_tabs_toggle='#default-styled-tab-content',
            data_tabs_active_classes='text-purple-600 hover:text-purple-600 dark:text-purple-500 dark:hover:text-purple-500 border-purple-600 dark:border-purple-500',
            data_tabs_inactive_classes='dark:border-transparent text-gray-500 hover:text-gray-600 dark:text-gray-400 border-gray-100 hover:border-gray-300 dark:border-gray-700 dark:hover:text-gray-300',
            role='tablist',
            cls='flex flex-wrap -mb-px text-sm font-medium text-center'
        ),
        cls='mb-4 border-b border-gray-200 dark:border-gray-700'
    ),
    Div(
        Div(
            P(
                'This is some placeholder content the',
                Strong("Profile tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-profile',
            role='tabpanel',
            aria_labelledby='profile-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Dashboard tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-dashboard',
            role='tabpanel',
            aria_labelledby='dashboard-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Settings tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-settings',
            role='tabpanel',
            aria_labelledby='settings-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        Div(
            P(
                'This is some placeholder content the',
                Strong("Contacts tab's associated content", cls='font-medium text-gray-800 dark:text-white'),
                '. Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to control the content visibility and styling.',
                cls='text-sm text-gray-500 dark:text-gray-400'
            ),
            id='styled-contacts',
            role='tabpanel',
            aria_labelledby='contacts-tab',
            cls='hidden p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
        ),
        id='default-styled-tab-content'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Strong('Tabs'),
        'class from Flowbite can be used to create an object that will enable the interactive navigation between tabs and its content based on the parameters, options, methods, and callback functions that you apply.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Create a new Tabs object with parameters such as an array of the tab and content elements.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Parameter', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Required', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('tabsElement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Parent HTML element of the tabs component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('items', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Array of the tab objects including the id, trigger element, and the content element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('An object of options for the appearances of the tabs and to use callback functions.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('instanceOptions', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td(
                        'Object of options that allows you to set a custom ID for the instance that is being added to the',
                        A('Instance Manager', href='https://flowbite.com/docs/getting-started/javascript/#instance-options', cls='underline hover:no-underline'),
                        'and whether to override or not an existing instance.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following options as the second parameter for the Tabs object to set the appearance of the active tab elements and use callback functions.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Option', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('defaultTabId', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Set the currently active tab element based on the ID.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('activeClasses', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Set a string of Tailwind CSS class names to apply to the active tab element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('inactiveClasses', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Set a string of Tailwind CSS class names to apply to the inactive tab elements.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onShow', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the a new tab has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Methods',
        Span(id='methods', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Methods', href='#methods', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the methods from the Tabs object to programmatically change the current active tab using JavaScript.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Method', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('show(id)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use the show function on the Tab object to change the current active tab element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('getTab(id)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Return the tab element based on the ID.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnShow(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function whenever a tab has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Example',
        Span(id='example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Example', href='#example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Check out the following example to learn how to initialize and manipulate a Tabs object in JavaScript.'),
    P('First of all, create an array of objects that contains the id, trigger element, and content element of each tab, set the active tab based on the id, and optionally set a callback function after a new tab has been shown.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('tabsElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'tabs-example'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// create an array of objects with the id, trigger element (eg. button), and the content element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('tabElements', cls='nx'),
                        Span('=', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'profile'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#profile-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#profile-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'dashboard'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#dashboard-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#dashboard-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'settings'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#settings-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#settings-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'contacts'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#contacts-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#contacts-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('];', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('options', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('defaultTabId', cls='nx'),
                        Span(':', cls='o'),
                        Span("'settings'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'text-primary-600 hover:text-primary-600 dark:text-primary-500 dark:hover:text-primary-400 border-primary-600 dark:border-primary-500'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'text-gray-500 hover:text-gray-600 dark:text-gray-400 border-gray-100 hover:border-gray-300 dark:border-gray-700 dark:hover:text-gray-300'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onShow', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'tab is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// instance options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('instanceOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'tabs-example'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('override', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P('Create a new Tabs object based on the parameters we’ve previously set.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Tabs', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/*', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* tabsElement: parent element of the tabs component (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* tabElements: array of tab objects (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('*/', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('tabs', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Tabs', cls='nx'),
                        Span('(', cls='p'),
                        Span('tabsElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('tabElements', cls='nx'),
                        Span(',', cls='p'),
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        Span('instanceOptions', cls='nx'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P('Lastly, you can now use the methods on the Tabs object to show another tab element, get a tab element based on the id, or get the current active tab element.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// shows another tab element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tabs', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
                        Span('(', cls='p'),
                        Span("'dashboard'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// get the tab object based on ID', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tabs', cls='nx'),
                        Span('.', cls='p'),
                        Span('getTab', cls='nx'),
                        Span('(', cls='p'),
                        Span("'contacts'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// get the current active tab object', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tabs', cls='nx'),
                        Span('.', cls='p'),
                        Span('getActiveTab', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H3(
        'HTML Markup',
        Span(id='html-markup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: HTML Markup', href='#html-markup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can use this HTML code as an example for the JavaScript code from above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-4 border-b border-gray-200 dark:border-gray-700"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('ul', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex flex-wrap -mb-px text-sm font-medium text-center text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabs-example"', cls='s'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tablist"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"me-2"', cls='s'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"presentation"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-block rounded-t-lg border-b-2 border-transparent p-4 hover:border-gray-300 hover:text-gray-600 dark:hover:text-gray-300"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"profile-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tab"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"profile-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-selected', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Profile', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"me-2"', cls='s'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"presentation"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-block rounded-t-lg border-b-2 border-transparent p-4 hover:border-gray-300 hover:text-gray-600 dark:hover:text-gray-300"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"dashboard-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tab"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"dashboard-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-selected', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Dashboard', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"me-2"', cls='s'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"presentation"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-block rounded-t-lg border-b-2 border-transparent p-4 hover:border-gray-300 hover:text-gray-600 dark:hover:text-gray-300"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"settings-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tab"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"settings-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-selected', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Settings', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"presentation"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-block rounded-t-lg border-b-2 border-transparent p-4 hover:border-gray-300 hover:text-gray-600 dark:hover:text-gray-300"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"contacts-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tab"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"contacts-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-selected', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Contacts', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('ul', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabContentExample"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden rounded-lg bg-gray-50 p-4 dark:bg-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"profile-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabpanel"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"profile-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-sm text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('This is some placeholder content the', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('strong', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-medium text-gray-800 dark:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        "Profile tab's associated content",
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        '. Clicking another tab will toggle the visibility of this one for',
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('the next. The tab JavaScript swaps classes to control the content', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('visibility and styling.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden rounded-lg bg-gray-50 p-4 dark:bg-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"dashboard-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabpanel"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"dashboard-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-sm text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('This is some placeholder content the', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('strong', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-medium text-gray-800 dark:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        "Dashboard tab's associated content",
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        '. Clicking another tab will toggle the visibility of this one for',
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('the next. The tab JavaScript swaps classes to control the content', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('visibility and styling.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden rounded-lg bg-gray-50 p-4 dark:bg-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"settings-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabpanel"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"settings-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-sm text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('This is some placeholder content the', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('strong', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-medium text-gray-800 dark:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        "Settings tab's associated content",
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        '. Clicking another tab will toggle the visibility of this one for',
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('the next. The tab JavaScript swaps classes to control the content', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('visibility and styling.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden rounded-lg bg-gray-50 p-4 dark:bg-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"contacts-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tabpanel"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"contacts-tab-example"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-sm text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('This is some placeholder content the', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('strong', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-medium text-gray-800 dark:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        "Contacts tab's associated content",
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        '. Clicking another tab will toggle the visibility of this one for',
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('the next. The tab JavaScript swaps classes to control the content', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('visibility and styling.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='html',
                cls='language-html'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H3(
        'TypeScript',
        Span(id='typescript', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: TypeScript', href='#typescript', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you’re using the',
        A('TypeScript configuration', href='https://flowbite.com/docs/getting-started/typescript/'),
        'from Flowbite then you can import the types for the Tabs class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Tabs', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('type', cls='nx'),
                        Span('{', cls='p'),
                        Span('TabsOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('TabsInterface', cls='nx'),
                        Span(',', cls='p'),
                        Span('TabItem', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('type', cls='nx'),
                        Span('{', cls='p'),
                        Span('InstanceOptions', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('tabsElement', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'tabs-example'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// create an array of objects with the id, trigger element (eg. button), and the content element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('tabElements', cls='nx'),
                        Span(':', cls='o'),
                        Span('TabItem', cls='nx'),
                        Span('[]', cls='p'),
                        Span('=', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'profile'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#profile-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#profile-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'dashboard'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#dashboard-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#dashboard-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'settings'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#settings-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#settings-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'contacts'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#contacts-tab-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#contacts-example'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('];', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('options', cls='nx'),
                        Span(':', cls='o'),
                        Span('TabsOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('defaultTabId', cls='nx'),
                        Span(':', cls='o'),
                        Span("'settings'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'text-primary-600 hover:text-primary-600 dark:text-primary-500 dark:hover:text-primary-400 border-primary-600 dark:border-primary-500'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'text-gray-500 hover:text-gray-600 dark:text-gray-400 border-gray-100 hover:border-gray-300 dark:border-gray-700 dark:hover:text-gray-300'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onShow', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'tab is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// instance options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('instanceOptions', cls='nx'),
                        Span(':', cls='o'),
                        Span('InstanceOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'tabs-example'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('override', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/*', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* tabsElement: parent element of the tabs component (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* tabElements: array of tab elements (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('*/', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('tabs', cls='nx'),
                        Span(':', cls='o'),
                        Span('TabsInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Tabs', cls='nx'),
                        Span('(', cls='p'),
                        Span('tabsElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('tabElements', cls='nx'),
                        Span(',', cls='p'),
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        Span('instanceOptions', cls='nx'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// open tab item based on id', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tabs', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
                        Span('(', cls='p'),
                        Span("'contacts'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    id='mainContent'
)
