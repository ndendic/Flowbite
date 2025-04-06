from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('Get started with the responsive navbar component from Flowbite to quickly set up a navigation menu for your website and set up the logo, list of pages, CTA button, search input, user profile options with a dropdown, and more.'),
    H2(
        'Default navbar',
        Span(id='default-navbar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default navbar', href='#default-navbar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a navigation bar built with the utility classes from Tailwind CSS to enable users to navigate across the pages of your website.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-default',
                type='button',
                aria_controls='navbar-default',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 dark:text-white md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-default',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-default',
                type='button',
                aria_controls='navbar-default',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 dark:text-white md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-default',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Navbar with dropdown',
        Span(id='navbar-with-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Navbar with dropdown', href='#navbar-with-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a secondary dropdown menu when clicking on one of the navigation links.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-dropdown',
                type='button',
                aria_controls='navbar-dropdown',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        Button(
                            'Dropdown',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-white md:dark:hover:text-primary-500 dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
                        ),
                        Div(
                            Ul(
                                Li(
                                    A('Dashboard', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Settings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                aria_labelledby='dropdownLargeButton',
                                cls='py-2 text-sm text-gray-700 dark:text-gray-400'
                            ),
                            Div(
                                A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                                cls='py-1'
                            ),
                            id='dropdownNavbar',
                            cls='z-10 hidden font-normal bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                        )
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-dropdown',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-dropdown',
                type='button',
                aria_controls='navbar-dropdown',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        Button(
                            'Dropdown',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-white md:dark:hover:text-primary-500 dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
                        ),
                        Div(
                            Ul(
                                Li(
                                    A('Dashboard', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Settings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                aria_labelledby='dropdownLargeButton',
                                cls='py-2 text-sm text-gray-700 dark:text-gray-400'
                            ),
                            Div(
                                A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                                cls='py-1'
                            ),
                            id='dropdownNavbar',
                            cls='z-10 hidden font-normal bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                        )
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-dropdown',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Multi-level dropdown',
        Span(id='multi-level-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Multi-level dropdown', href='#multi-level-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show multiple layers of dropdown menu by stacking them inside of each other.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-multi-level',
                type='button',
                aria_controls='navbar-multi-level',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        Button(
                            'Dropdown',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-white md:dark:hover:text-primary-500 dark:focus:text-white dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
                        ),
                        Div(
                            Ul(
                                Li(
                                    A('Dashboard', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    Button(
                                        'Dropdown',
                                        Svg(
                                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                            aria_hidden='true',
                                            xmlns='http://www.w3.org/2000/svg',
                                            fill='none',
                                            viewbox='0 0 10 6',
                                            cls='w-2.5 h-2.5 ms-2.5'
                                        ),
                                        id='doubleDropdownButton',
                                        data_dropdown_toggle='doubleDropdown',
                                        data_dropdown_placement='right-start',
                                        type='button',
                                        cls='flex items-center justify-between w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                                    ),
                                    Div(
                                        Ul(
                                            Li(
                                                A('Overview', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('My downloads', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('Billing', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('Rewards', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            aria_labelledby='doubleDropdownButton',
                                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                                        ),
                                        id='doubleDropdown',
                                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                                    ),
                                    aria_labelledby='dropdownNavbarLink'
                                ),
                                Li(
                                    A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                aria_labelledby='dropdownLargeButton',
                                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                            ),
                            Div(
                                A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                                cls='py-1'
                            ),
                            id='dropdownNavbar',
                            cls='z-10 hidden font-normal bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                        )
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-multi-level',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-multi-level',
                type='button',
                aria_controls='navbar-multi-level',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        Button(
                            'Dropdown',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-white md:dark:hover:text-primary-500 dark:focus:text-white dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
                        ),
                        Div(
                            Ul(
                                Li(
                                    A('Dashboard', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                Li(
                                    Button(
                                        'Dropdown',
                                        Svg(
                                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                            aria_hidden='true',
                                            xmlns='http://www.w3.org/2000/svg',
                                            fill='none',
                                            viewbox='0 0 10 6',
                                            cls='w-2.5 h-2.5 ms-2.5'
                                        ),
                                        id='doubleDropdownButton',
                                        data_dropdown_toggle='doubleDropdown',
                                        data_dropdown_placement='right-start',
                                        type='button',
                                        cls='flex items-center justify-between w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                                    ),
                                    Div(
                                        Ul(
                                            Li(
                                                A('Overview', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('My downloads', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('Billing', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            Li(
                                                A('Rewards', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                                            ),
                                            aria_labelledby='doubleDropdownButton',
                                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                                        ),
                                        id='doubleDropdown',
                                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                                    ),
                                    aria_labelledby='dropdownNavbarLink'
                                ),
                                Li(
                                    A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                ),
                                aria_labelledby='dropdownLargeButton',
                                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                            ),
                            Div(
                                A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                                cls='py-1'
                            ),
                            id='dropdownNavbar',
                            cls='z-10 hidden font-normal bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                        )
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-multi-level',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Sticky navbar',
        Span(id='sticky-navbar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sticky navbar', href='#sticky-navbar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to keep the navbar positioned fixed to the top side as you scroll down the document page.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button('Get started', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-sticky',
                    type='button',
                    aria_controls='navbar-sticky',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-sticky',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white dark:bg-gray-900 fixed w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button('Get started', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-sticky',
                    type='button',
                    aria_controls='navbar-sticky',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-sticky',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white dark:bg-gray-900 fixed w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Navbar with submenu',
        Span(id='navbar-with-submenu', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Navbar with submenu', href='#navbar-with-submenu', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show another subnav below the main navbar element.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                A('(555) 412-1234', href='tel:5541251234', cls='text-sm text-gray-500 dark:text-white hover:underline'),
                A('Login', href='#', cls='text-sm text-primary-600 dark:text-primary-500 hover:underline'),
                cls='flex items-center space-x-6 rtl:space-x-reverse'
            ),
            cls='flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    ),
    Nav(
        Div(
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Company', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Team', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Features', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    cls='flex flex-row font-medium mt-0 space-x-8 rtl:space-x-reverse text-sm'
                ),
                cls='flex items-center'
            ),
            cls='max-w-screen-xl px-4 py-3 mx-auto'
        ),
        cls='bg-gray-50 dark:bg-gray-700'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                A('(555) 412-1234', href='tel:5541251234', cls='text-sm text-gray-500 dark:text-white hover:underline'),
                A('Login', href='#', cls='text-sm text-primary-600 dark:text-primary-500 hover:underline'),
                cls='flex items-center space-x-6 rtl:space-x-reverse'
            ),
            cls='flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    ),
    Nav(
        Div(
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Company', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Team', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    Li(
                        A('Features', href='#', cls='text-gray-900 dark:text-white hover:underline')
                    ),
                    cls='flex flex-row font-medium mt-0 space-x-8 rtl:space-x-reverse text-sm'
                ),
                cls='flex items-center'
            ),
            cls='max-w-screen-xl px-4 py-3 mx-auto'
        ),
        cls='bg-gray-50 dark:bg-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Navbar with search',
        Span(id='navbar-with-search', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Navbar with search', href='#navbar-with-search', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a navbar element to also show a search input element that you can integrate for a site-wide search.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-5 h-5'
                    ),
                    Span('Search', cls='sr-only'),
                    type='button',
                    data_collapse_toggle='navbar-search',
                    aria_controls='navbar-search',
                    aria_expanded='false',
                    cls='md:hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 me-1'
                ),
                Div(
                    Div(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        Span('Search icon', cls='sr-only'),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(type='text', id='search-navbar', placeholder='Search...', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative hidden md:block'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-search',
                    type='button',
                    aria_controls='navbar-search',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2'
            ),
            Div(
                Div(
                    Div(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(type='text', id='search-navbar', placeholder='Search...', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative mt-3 md:hidden'
                ),
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-search',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-5 h-5'
                    ),
                    Span('Search', cls='sr-only'),
                    type='button',
                    data_collapse_toggle='navbar-search',
                    aria_controls='navbar-search',
                    aria_expanded='false',
                    cls='md:hidden text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 me-1'
                ),
                Div(
                    Div(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        Span('Search icon', cls='sr-only'),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(type='text', id='search-navbar', placeholder='Search...', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative hidden md:block'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-search',
                    type='button',
                    aria_controls='navbar-search',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2'
            ),
            Div(
                Div(
                    Div(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(type='text', id='search-navbar', placeholder='Search...', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative mt-3 md:hidden'
                ),
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-search',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Navbar with CTA button',
        Span(id='navbar-with-cta-button', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Navbar with CTA button', href='#navbar-with-cta-button', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following navbar element to show a call to action button alongside the logo and page links.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button('Get started', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-cta',
                    type='button',
                    aria_controls='navbar-cta',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 md:p-0 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-cta',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button('Get started', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-cta',
                    type='button',
                    aria_controls='navbar-cta',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 md:p-0 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-cta',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Language dropdown',
        Span(id='language-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Language dropdown', href='#language-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example to show a language dropdown selector in the navbar component.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(fill='#b22234', d='M0 0h7410v3900H0z'),
                        Path(d='M0 450h7410m0 600H0m0 600h7410m0 600H0m0 600h7410m0 600H0', stroke='#fff', stroke_width='300'),
                        Path(fill='#3c3b6e', d='M0 0h2964v2100H0z'),
                        G(
                            G(
                                G(
                                    G(
                                        G(
                                            Path(id='a', d='M247 90l70.534 217.082-184.66-134.164h228.253L176.466 307.082z'),
                                            Use(y='420', **{'xlink:href': '#a'}),
                                            Use(y='840', **{'xlink:href': '#a'}),
                                            Use(y='1260', **{'xlink:href': '#a'}),
                                            id='b'
                                        ),
                                        Use(y='1680', **{'xlink:href': '#a'}),
                                        id='e'
                                    ),
                                    Use(x='247', y='210', **{'xlink:href': '#b'}),
                                    id='c'
                                ),
                                Use(x='494', **{'xlink:href': '#c'}),
                                id='d'
                            ),
                            Use(x='988', **{'xlink:href': '#d'}),
                            Use(x='1976', **{'xlink:href': '#c'}),
                            Use(x='2470', **{'xlink:href': '#e'}),
                            fill='#fff'
                        ),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 3900 3900',
                        cls='w-5 h-5 rounded-full me-3',
                        **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                    ),
                    'English (US)',
                    type='button',
                    data_dropdown_toggle='language-dropdown-menu',
                    cls='inline-flex items-center font-medium justify-center px-4 py-2 text-sm text-gray-900 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white'
                ),
                Div(
                    Ul(
                        Li(
                            A(
                                Div(
                                    Svg(
                                        G(
                                            G(
                                                Path(fill='#bd3d44', d='M0 0h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                                Path(fill='#fff', d='M0 10h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                                stroke_width='1pt'
                                            ),
                                            Path(fill='#192f5d', d='M0 0h98.8v70H0z', transform='scale(3.9385)'),
                                            Path(fill='#fff', d='M8.2 3l1 2.8H12L9.7 7.5l.9 2.7-2.4-1.7L6 10.2l.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7L74 8.5l-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 7.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 24.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 21.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 38.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 35.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 52.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 49.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 66.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 63.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9z', transform='scale(3.9385)'),
                                            fill_rule='evenodd'
                                        ),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-us',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'English (US)',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        Path(fill='#ffce00', d='M0 341.3h512V512H0z'),
                                        Path(d='M0 0h512v170.7H0z'),
                                        Path(fill='#d00', d='M0 170.7h512v170.6H0z'),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-de',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'Deutsch',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        G(
                                            Path(fill='#fff', d='M0 0h512v512H0z'),
                                            Path(fill='#009246', d='M0 0h170.7v512H0z'),
                                            Path(fill='#ce2b37', d='M341.3 0H512v512H341.3z'),
                                            fill_rule='evenodd',
                                            stroke_width='1pt'
                                        ),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-it',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'Italiano',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        Defs(
                                            Path(id='a', fill='#ffde00', d='M1-.3L-.7.8 0-1 .6.8-1-.3z')
                                        ),
                                        Path(fill='#de2910', d='M0 0h512v512H0z'),
                                        Use(width='30', height='20', transform='matrix(76.8 0 0 76.8 128 128)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-121 142.6 -47) scale(25.5827)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-98.1 198 -82) scale(25.6)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-74 272.4 -114) scale(25.6137)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='matrix(16 -19.968 19.968 16 256 230.4)', **{'xlink:href': '#a'}),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-cn',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2',
                                        **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                                    ),
                                    'ä¸\xadæ\x96\x87 (ç¹\x81é«\x94)',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        role='none',
                        cls='py-2 font-medium'
                    ),
                    id='language-dropdown-menu',
                    cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-language',
                    type='button',
                    aria_controls='navbar-language',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex items-center md:order-2 space-x-1 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-language',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(fill='#b22234', d='M0 0h7410v3900H0z'),
                        Path(d='M0 450h7410m0 600H0m0 600h7410m0 600H0m0 600h7410m0 600H0', stroke='#fff', stroke_width='300'),
                        Path(fill='#3c3b6e', d='M0 0h2964v2100H0z'),
                        G(
                            G(
                                G(
                                    G(
                                        G(
                                            Path(id='a', d='M247 90l70.534 217.082-184.66-134.164h228.253L176.466 307.082z'),
                                            Use(y='420', **{'xlink:href': '#a'}),
                                            Use(y='840', **{'xlink:href': '#a'}),
                                            Use(y='1260', **{'xlink:href': '#a'}),
                                            id='b'
                                        ),
                                        Use(y='1680', **{'xlink:href': '#a'}),
                                        id='e'
                                    ),
                                    Use(x='247', y='210', **{'xlink:href': '#b'}),
                                    id='c'
                                ),
                                Use(x='494', **{'xlink:href': '#c'}),
                                id='d'
                            ),
                            Use(x='988', **{'xlink:href': '#d'}),
                            Use(x='1976', **{'xlink:href': '#c'}),
                            Use(x='2470', **{'xlink:href': '#e'}),
                            fill='#fff'
                        ),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 3900 3900',
                        cls='w-5 h-5 rounded-full me-3',
                        **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                    ),
                    'English (US)',
                    type='button',
                    data_dropdown_toggle='language-dropdown-menu',
                    cls='inline-flex items-center font-medium justify-center px-4 py-2 text-sm text-gray-900 dark:text-white rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white'
                ),
                Div(
                    Ul(
                        Li(
                            A(
                                Div(
                                    Svg(
                                        G(
                                            G(
                                                Path(fill='#bd3d44', d='M0 0h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                                Path(fill='#fff', d='M0 10h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                                stroke_width='1pt'
                                            ),
                                            Path(fill='#192f5d', d='M0 0h98.8v70H0z', transform='scale(3.9385)'),
                                            Path(fill='#fff', d='M8.2 3l1 2.8H12L9.7 7.5l.9 2.7-2.4-1.7L6 10.2l.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7L74 8.5l-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 7.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 24.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 21.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 38.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 35.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 52.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 49.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 66.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 63.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9z', transform='scale(3.9385)'),
                                            fill_rule='evenodd'
                                        ),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-us',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'English (US)',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        Path(fill='#ffce00', d='M0 341.3h512V512H0z'),
                                        Path(d='M0 0h512v170.7H0z'),
                                        Path(fill='#d00', d='M0 170.7h512v170.6H0z'),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-de',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'Deutsch',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        G(
                                            Path(fill='#fff', d='M0 0h512v512H0z'),
                                            Path(fill='#009246', d='M0 0h170.7v512H0z'),
                                            Path(fill='#ce2b37', d='M341.3 0H512v512H341.3z'),
                                            fill_rule='evenodd',
                                            stroke_width='1pt'
                                        ),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-it',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2'
                                    ),
                                    'Italiano',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Svg(
                                        Defs(
                                            Path(id='a', fill='#ffde00', d='M1-.3L-.7.8 0-1 .6.8-1-.3z')
                                        ),
                                        Path(fill='#de2910', d='M0 0h512v512H0z'),
                                        Use(width='30', height='20', transform='matrix(76.8 0 0 76.8 128 128)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-121 142.6 -47) scale(25.5827)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-98.1 198 -82) scale(25.6)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='rotate(-74 272.4 -114) scale(25.6137)', **{'xlink:href': '#a'}),
                                        Use(width='30', height='20', transform='matrix(16 -19.968 19.968 16 256 230.4)', **{'xlink:href': '#a'}),
                                        aria_hidden='true',
                                        xmlns='http://www.w3.org/2000/svg',
                                        id='flag-icon-css-cn',
                                        viewbox='0 0 512 512',
                                        cls='h-3.5 w-3.5 rounded-full me-2',
                                        **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                                    ),
                                    'ä¸\xadæ\x96\x87 (ç¹\x81é«\x94)',
                                    cls='inline-flex items-center'
                                ),
                                href='#',
                                role='menuitem',
                                cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        role='none',
                        cls='py-2 font-medium'
                    ),
                    id='language-dropdown-menu',
                    cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-language',
                    type='button',
                    aria_controls='navbar-language',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex items-center md:order-2 space-x-1 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-language',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'User menu dropdown',
        Span(id='user-menu-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User menu dropdown', href='#user-menu-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to create a navigation bar with a user profile or button to toggle a dropdown menu.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Span('Open user menu', cls='sr-only'),
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
                    type='button',
                    id='user-menu-button',
                    aria_expanded='false',
                    data_dropdown_toggle='user-dropdown',
                    data_dropdown_placement='bottom',
                    cls='flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
                ),
                Div(
                    Div(
                        Span('Bonnie Green', cls='block text-sm text-gray-900 dark:text-white'),
                        Span('name@flowbite.com', cls='block text-sm text-gray-500 truncate dark:text-gray-400'),
                        cls='px-4 py-3'
                    ),
                    Ul(
                        Li(
                            A('Dashboard', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Settings', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Earnings', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        aria_labelledby='user-menu-button',
                        cls='py-2'
                    ),
                    id='user-dropdown',
                    cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-user',
                    type='button',
                    aria_controls='navbar-user',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-user',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Span('Open user menu', cls='sr-only'),
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
                    type='button',
                    id='user-menu-button',
                    aria_expanded='false',
                    data_dropdown_toggle='user-dropdown',
                    data_dropdown_placement='bottom',
                    cls='flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
                ),
                Div(
                    Div(
                        Span('Bonnie Green', cls='block text-sm text-gray-900 dark:text-white'),
                        Span('name@flowbite.com', cls='block text-sm text-gray-500 truncate dark:text-gray-400'),
                        cls='px-4 py-3'
                    ),
                    Ul(
                        Li(
                            A('Dashboard', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Settings', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Earnings', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        Li(
                            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white')
                        ),
                        aria_labelledby='user-menu-button',
                        cls='py-2'
                    ),
                    id='user-dropdown',
                    cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                ),
                Button(
                    Span('Open main menu', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 17 14',
                        cls='w-5 h-5'
                    ),
                    data_collapse_toggle='navbar-user',
                    type='button',
                    aria_controls='navbar-user',
                    aria_expanded='false',
                    cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                ),
                cls='flex items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-primary-500')
                    ),
                    Li(
                        A('About', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='navbar-user',
                cls='items-center justify-between hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Mega menu navbar',
        Span(id='mega-menu-navbar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Mega menu navbar', href='#mega-menu-navbar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also use the dropdown element inside a navigation bar and add a second level of navigation hierarchy, but make sure to use a',
        Code('button'),
        'element.'
    ),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='mega-menu-full',
                type='button',
                aria_controls='mega-menu-full',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        Button(
                            'Company',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='mega-menu-full-dropdown-button',
                            data_collapse_toggle='mega-menu-full-dropdown',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 rounded-sm md:w-auto hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700'
                        )
                    ),
                    Li(
                        A('Marketplace', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Resources', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='mega-menu-full',
                cls='items-center justify-between font-medium hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4'
        ),
        Div(
            Div(
                Ul(
                    Li(
                        A(
                            Div('Online Stores', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Segmentation', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Marketing CRM', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    )
                ),
                Ul(
                    Li(
                        A(
                            Div('Online Stores', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Segmentation', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Marketing CRM', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    )
                ),
                cls='grid max-w-screen-xl px-4 py-5 mx-auto text-gray-900 dark:text-white sm:grid-cols-2 md:px-6'
            ),
            id='mega-menu-full-dropdown',
            cls='mt-1 border-gray-200 shadow-xs bg-gray-50 md:bg-white border-y dark:bg-gray-800 dark:border-gray-600'
        ),
        cls='bg-white border-gray-200 dark:border-gray-600 dark:bg-gray-900'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='mega-menu-full',
                type='button',
                aria_controls='mega-menu-full',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        Button(
                            'Company',
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-2.5 h-2.5 ms-2.5'
                            ),
                            id='mega-menu-full-dropdown-button',
                            data_collapse_toggle='mega-menu-full-dropdown',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-900 rounded-sm md:w-auto hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700'
                        )
                    ),
                    Li(
                        A('Marketplace', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Resources', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:hover:text-primary-700 md:p-0 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-primary-500 md:dark:hover:bg-transparent dark:border-gray-700')
                    ),
                    cls='flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
                ),
                id='mega-menu-full',
                cls='items-center justify-between font-medium hidden w-full md:flex md:w-auto md:order-1'
            ),
            cls='flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4'
        ),
        Div(
            Div(
                Ul(
                    Li(
                        A(
                            Div('Online Stores', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Segmentation', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Marketing CRM', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    )
                ),
                Ul(
                    Li(
                        A(
                            Div('Online Stores', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Segmentation', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    ),
                    Li(
                        A(
                            Div('Marketing CRM', cls='font-semibold'),
                            Span("Connect with third-party tools that you're already using.", cls='text-sm text-gray-500 dark:text-gray-400'),
                            href='#',
                            cls='block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700'
                        )
                    )
                ),
                cls='grid max-w-screen-xl px-4 py-5 mx-auto text-gray-900 dark:text-white sm:grid-cols-2 md:px-6'
            ),
            id='mega-menu-full-dropdown',
            cls='mt-1 border-gray-200 shadow-xs bg-gray-50 md:bg-white border-y dark:bg-gray-800 dark:border-gray-600'
        ),
        cls='bg-white border-gray-200 dark:border-gray-600 dark:bg-gray-900'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Solid background',
        Span(id='solid-background', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Solid background', href='#solid-background', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a solid background for the navbar component instead of being transparent.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-solid-bg',
                type='button',
                aria_controls='navbar-solid-bg',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 md:p-0 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700'
                ),
                id='navbar-solid-bg',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-solid-bg',
                type='button',
                aria_controls='navbar-solid-bg',
                aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 md:p-0 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:dark:text-primary-500 dark:bg-primary-600 md:dark:bg-transparent')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 md:p-0 text-gray-900 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 dark:text-white md:dark:hover:text-primary-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700'
                ),
                id='navbar-solid-bg',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H2(
        'Hamburger menu',
        Span(id='hamburger-menu', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Hamburger menu', href='#hamburger-menu', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'All of the navbar components from this page have a responsive hamburger menu included which by default appears when the screen goes below 768px in width based on the',
        Code('md'),
        'utility class from Tailwind CSS.'
    ),
    P('Here’s an example where you can show the hamburger icon and the menu on all screen sizes.'),
    component_showcase(Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-hamburger',
                type='button',
                aria_controls='navbar-hamburger',
                aria_expanded='false',
                cls='inline-flex items-center justify-center p-2 w-10 h-10 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm dark:bg-primary-600')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    cls='flex flex-col font-medium mt-4 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
                ),
                id='navbar-hamburger',
                cls='hidden w-full'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Nav(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                href='#',
                cls='flex items-center space-x-3 rtl:space-x-reverse'
            ),
            Button(
                Span('Open main menu', cls='sr-only'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 17 14',
                    cls='w-5 h-5'
                ),
                data_collapse_toggle='navbar-hamburger',
                type='button',
                aria_controls='navbar-hamburger',
                aria_expanded='false',
                cls='inline-flex items-center justify-center p-2 w-10 h-10 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm dark:bg-primary-600')
                    ),
                    Li(
                        A('Services', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
                    ),
                    cls='flex flex-col font-medium mt-4 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
                ),
                id='navbar-hamburger',
                cls='hidden w-full'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ),
        cls='border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can check out more navbar component examples from the following resources from Flowbite Blocks:'),
    Ul(
        Li(
            A('Headers for marketing', href='https://flowbite.com/blocks/marketing/header/')
        ),
        Li(
            A('Navbars for dashboard', href='https://flowbite.com/blocks/application/navbar/')
        ),
        Li(
            A('Application shell layouts', href='https://flowbite.com/blocks/application/shells/')
        )
    ),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('Collapse'),
        'class to create an object with a trigger and target element, where the target element will be collapsed or expanded based on the events dispatched on the trigger element. This can be used to toggle another element such as a dropdown menu or a hamburger navbar.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the object parameters from the Collapse object to set the trigger element, target element, and the options including callback functions.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Parameter', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Required', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass the target element object that will be expanded or collapsed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('triggerEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass the trigger element that will expand or collapse the target element based on click event.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Set these options to override the default transition, duration, and timing function of the collapse animation.', cls='px-6 py-4'),
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
    P('Use these optional options for the Collapse object to set the transition, duration, and timing function types based on the utility classes from Tailwind CSS.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Option', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('onCollapse', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the item has been collapsed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onExpand', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the item has been expanded.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onToggle', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the item has either been expanded or collapsed.', cls='px-6 py-4'),
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
    P('Use the following methods on the Dismiss object to programmatically manipulate the behaviour.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Method', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('collapse()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method on the Collapse object to hide the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('expand()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method on the Collapse object to show the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('toggle()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method on the Collapse object toggle the current visibility of the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnCollapse(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function when the item has been collapsed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnExpand(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function when the item has been expanded.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnToggle(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function when the item has been toggled.', cls='px-6 py-4'),
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
    P(
        'Check out the following example to learn how to initialize and use the methods of the',
        Strong('Collapse'),
        'object to manually expand and collapse elements on the page.'
    ),
    P('First of all, you need to set the object parameters where the target element is required and the other two are optional.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the target element that will be collapsed or expanded (eg. navbar menu)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$targetEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'targetEl'", cls='s1'),
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
                        Span('// optionally set a trigger element (eg. a button, hamburger icon)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$triggerEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'triggerEl'", cls='s1'),
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
                        Span('// optional options with default values and callback functions', cls='c1'),
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
                        Span('onCollapse', cls='nx'),
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
                        Span("'element has been collapsed'", cls='s1'),
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
                        Span('onExpand', cls='nx'),
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
                        Span("'element has been expanded'", cls='s1'),
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
                        Span('onToggle', cls='nx'),
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
                        Span("'element has been toggled'", cls='s1'),
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
                        Span("'targetEl'", cls='s1'),
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
    P('Next step is to create a new instance of a Collapse object using the parameters we have set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Collapse', cls='nx'),
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
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $triggerEl: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options: optional', cls='cm'),
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
                        Span('collapse', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Collapse', cls='nx'),
                        Span('(', cls='p'),
                        Span('$targetEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('$triggerEl', cls='nx'),
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
    P('Now you can programmatically expand or collapse the target element using the methods of the Collapse object.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// show the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('collapse', cls='nx'),
                        Span('.', cls='p'),
                        Span('expand', cls='nx'),
                        Span('();', cls='p'),
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
                        Span('// hide the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('collapse', cls='nx'),
                        Span('.', cls='p'),
                        Span('collapse', cls='nx'),
                        Span('();', cls='p'),
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
                        Span('// toggle the visibility of the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('collapse', cls='nx'),
                        Span('.', cls='p'),
                        Span('toggle', cls='nx'),
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
    P(
        'Here is an example of the HTML markup that you can use for the JavaScript example above. Please note that you should use the',
        Code('hidden'),
        'class from Tailwind CSS to hide the target element by default.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"triggerEl"', cls='s'),
                        Span('aria-expanded', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800"', cls='s'),
                        Span('>', cls='p'),
                        'Trigger collapse',
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
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
                        Span('<!-- Target element -->', cls='c'),
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
                        Span('"targetEl"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('ul', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-48 rounded-lg  border border-gray-200 bg-white text-sm text-gray-900 dark:border-gray-600 dark:bg-gray-700 dark:text-white"', cls='s'),
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
                        Span('li', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-full rounded-t-lg border-b border-gray-200 px-4 py-2 dark:border-gray-600"', cls='s'),
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
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-full border-b border-gray-200 px-4 py-2 dark:border-gray-600"', cls='s'),
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
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-full border-b border-gray-200 px-4 py-2 dark:border-gray-600"', cls='s'),
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
                    Span('Messages', cls='cl'),
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
                        Span('"w-full rounded-b-lg px-4 py-2"', cls='s'),
                        Span('>', cls='p'),
                        'Download',
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
        'from Flowbite then you can import the types for the Collapse object, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Collapse', cls='nx'),
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
                        Span('CollapseOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('CollapseInterface', cls='nx'),
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
                        Span('// set the target element that will be collapsed or expanded (eg. navbar menu)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'targetEl'", cls='s1'),
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
                        Span('// optionally set a trigger element (eg. a button, hamburger icon)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'triggerEl'", cls='s1'),
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
                        Span('// optional options with default values and callback functions', cls='c1'),
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
                        Span('CollapseOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onCollapse', cls='nx'),
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
                        Span("'element has been collapsed'", cls='s1'),
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
                        Span('onExpand', cls='nx'),
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
                        Span("'element has been expanded'", cls='s1'),
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
                        Span('onToggle', cls='nx'),
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
                        Span("'element has been toggled'", cls='s1'),
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
                        Span('// instance options object', cls='c1'),
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
                        Span("'targetEl'", cls='s1'),
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
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $triggerEl: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions: optional', cls='cm'),
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
                        Span('collapse', cls='nx'),
                        Span(':', cls='o'),
                        Span('CollapseInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Collapse', cls='nx'),
                        Span('(', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$targetEl', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$triggerEl', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('instanceOptions', cls='nx'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
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
                        Span('// show the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('collapse', cls='nx'),
                        Span('.', cls='p'),
                        Span('expand', cls='nx'),
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
    id='mainContent'
)
