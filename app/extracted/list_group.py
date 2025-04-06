from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The list group component can be used to display a series of elements, buttons or links inside a single card component similar to a sidebar.'),
    H2(
        'Default list group',
        Span(id='default-list-group', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default list group', href='#default-list-group', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Here’s an example of a list group that you can use right away.'),
    component_showcase(Div(
    Ul(
        Li('Profile', cls='w-full px-4 py-2 border-b border-gray-200 rounded-t-lg dark:border-gray-600'),
        Li('Settings', cls='w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600'),
        Li('Messages', cls='w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600'),
        Li('Download', cls='w-full px-4 py-2 rounded-b-lg'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    Ul(
        Li('Profile', cls='w-full px-4 py-2 border-b border-gray-200 rounded-t-lg dark:border-gray-600'),
        Li('Settings', cls='w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600'),
        Li('Messages', cls='w-full px-4 py-2 border-b border-gray-200 dark:border-gray-600'),
        Li('Download', cls='w-full px-4 py-2 rounded-b-lg'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'List group with links',
        Span(id='list-group-with-links', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: List group with links', href='#list-group-with-links', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can also display a series of links inside the list group element.'),
    component_showcase(Div(
    Div(
        A('Profile', href='#', aria_current='true', cls='block w-full px-4 py-2 text-white bg-primary-700 border-b border-gray-200 rounded-t-lg cursor-pointer dark:bg-gray-800 dark:border-gray-600'),
        A('Settings', href='#', cls='block w-full px-4 py-2 border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        A('Messages', href='#', cls='block w-full px-4 py-2 border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        A('Download', href='#', cls='block w-full px-4 py-2 rounded-b-lg cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    Div(
        A('Profile', href='#', aria_current='true', cls='block w-full px-4 py-2 text-white bg-primary-700 border-b border-gray-200 rounded-t-lg cursor-pointer dark:bg-gray-800 dark:border-gray-600'),
        A('Settings', href='#', cls='block w-full px-4 py-2 border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        A('Messages', href='#', cls='block w-full px-4 py-2 border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        A('Download', href='#', cls='block w-full px-4 py-2 rounded-b-lg cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'List group with buttons',
        Span(id='list-group-with-buttons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: List group with buttons', href='#list-group-with-buttons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('It is also possible to display a list of button element inside the list group component. The following example includes an active and disabled item as well.'),
    component_showcase(Div(
    Div(
        Button('Profile', aria_current='true', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right text-white bg-primary-700 border-b border-gray-200 rounded-t-lg cursor-pointer focus:outline-none dark:bg-gray-800 dark:border-gray-600'),
        Button('Settings', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        Button('Messages', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        Button('Download', disabled=True, type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right bg-gray-100 rounded-b-lg cursor-not-allowed dark:bg-gray-600 dark:text-gray-400'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    Div(
        Button('Profile', aria_current='true', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right text-white bg-primary-700 border-b border-gray-200 rounded-t-lg cursor-pointer focus:outline-none dark:bg-gray-800 dark:border-gray-600'),
        Button('Settings', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        Button('Messages', type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right border-b border-gray-200 cursor-pointer hover:bg-gray-100 hover:text-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'),
        Button('Download', disabled=True, type='button', cls='w-full px-4 py-2 font-medium text-left rtl:text-right bg-gray-100 rounded-b-lg cursor-not-allowed dark:bg-gray-600 dark:text-gray-400'),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'List group with icons',
        Span(id='list-group-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: List group with icons', href='#list-group-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the following example to create a list of buttons as a menu together with',
        A('SVG icons', href='https://flowbite.com/icons/'),
        '.'
    ),
    component_showcase(Div(
    Div(
        Button(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Profile',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 rounded-t-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.75 4H19M7.75 4a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 4h2.25m13.5 6H19m-2.25 0a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 10h11.25m-4.5 6H19M7.75 16a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 16h2.25'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Settings',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(d='M18 4H16V9C16 10.0609 15.5786 11.0783 14.8284 11.8284C14.0783 12.5786 13.0609 13 12 13H9L6.846 14.615C7.17993 14.8628 7.58418 14.9977 8 15H11.667L15.4 17.8C15.5731 17.9298 15.7836 18 16 18C16.2652 18 16.5196 17.8946 16.7071 17.7071C16.8946 17.5196 17 17.2652 17 17V15H18C18.5304 15 19.0391 14.7893 19.4142 14.4142C19.7893 14.0391 20 13.5304 20 13V6C20 5.46957 19.7893 4.96086 19.4142 4.58579C19.0391 4.21071 18.5304 4 18 4Z', fill='currentColor'),
                Path(d='M12 0H2C1.46957 0 0.960859 0.210714 0.585786 0.585786C0.210714 0.960859 0 1.46957 0 2V9C0 9.53043 0.210714 10.0391 0.585786 10.4142C0.960859 10.7893 1.46957 11 2 11H3V13C3 13.1857 3.05171 13.3678 3.14935 13.5257C3.24698 13.6837 3.38668 13.8114 3.55279 13.8944C3.71889 13.9775 3.90484 14.0126 4.08981 13.996C4.27477 13.9793 4.45143 13.9114 4.6 13.8L8.333 11H12C12.5304 11 13.0391 10.7893 13.4142 10.4142C13.7893 10.0391 14 9.53043 14 9V2C14 1.46957 13.7893 0.960859 13.4142 0.585786C13.0391 0.210714 12.5304 0 12 0Z', fill='currentColor'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                viewbox='0 0 20 18',
                fill='currentColor',
                cls='w-3 h-3 me-2.5'
            ),
            'Messages',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Download',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium rounded-b-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        cls='w-48 text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    Div(
        Button(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Profile',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 rounded-t-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.75 4H19M7.75 4a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 4h2.25m13.5 6H19m-2.25 0a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 10h11.25m-4.5 6H19M7.75 16a2.25 2.25 0 0 1-4.5 0m4.5 0a2.25 2.25 0 0 0-4.5 0M1 16h2.25'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Settings',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(d='M18 4H16V9C16 10.0609 15.5786 11.0783 14.8284 11.8284C14.0783 12.5786 13.0609 13 12 13H9L6.846 14.615C7.17993 14.8628 7.58418 14.9977 8 15H11.667L15.4 17.8C15.5731 17.9298 15.7836 18 16 18C16.2652 18 16.5196 17.8946 16.7071 17.7071C16.8946 17.5196 17 17.2652 17 17V15H18C18.5304 15 19.0391 14.7893 19.4142 14.4142C19.7893 14.0391 20 13.5304 20 13V6C20 5.46957 19.7893 4.96086 19.4142 4.58579C19.0391 4.21071 18.5304 4 18 4Z', fill='currentColor'),
                Path(d='M12 0H2C1.46957 0 0.960859 0.210714 0.585786 0.585786C0.210714 0.960859 0 1.46957 0 2V9C0 9.53043 0.210714 10.0391 0.585786 10.4142C0.960859 10.7893 1.46957 11 2 11H3V13C3 13.1857 3.05171 13.3678 3.14935 13.5257C3.24698 13.6837 3.38668 13.8114 3.55279 13.8944C3.71889 13.9775 3.90484 14.0126 4.08981 13.996C4.27477 13.9793 4.45143 13.9114 4.6 13.8L8.333 11H12C12.5304 11 13.0391 10.7893 13.4142 10.4142C13.7893 10.0391 14 9.53043 14 9V2C14 1.46957 13.7893 0.960859 13.4142 0.585786C13.0391 0.210714 12.5304 0 12 0Z', fill='currentColor'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                viewbox='0 0 20 18',
                fill='currentColor',
                cls='w-3 h-3 me-2.5'
            ),
            'Messages',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        Button(
            Svg(
                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3 h-3 me-2.5'
            ),
            'Download',
            type='button',
            cls='relative inline-flex items-center w-full px-4 py-2 text-sm font-medium rounded-b-lg hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-2 focus:ring-primary-700 focus:text-primary-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white'
        ),
        cls='w-48 text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    id='mainContent'
)
