from fasthtml.common import *
from fasthtml.svg import *

def Navbar():
    return Nav(
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
                        cls='inline-flex items-center p-2 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                    ),  
                    A(
                        Img(src='https://flowbite.com/docs/images/logo.svg', alt='Logo', cls='h-8 me-3'),
                        Span('Flowbite', cls='self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white'),
                        href='https://flowbite.com',
                        cls='flex ms-2 md:me-24'
                    ),
                    cls='flex items-center justify-start rtl:justify-end'
                ),
                Div(
                    Button(
                        Svg(
                            Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z'),
                            id='theme-toggle-dark-icon',
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='w-4 h-4 hidden'
                        ),
                        Svg(
                            Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z'),
                            id='theme-toggle-light-icon',
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 hidden'
                        ),
                        Span('Toggle dark mode', cls='sr-only'),
                        id='theme-toggle',
                        # data_tooltip_target='tooltip-toggle',
                        type='button',
                        cls='text-gray-500 inline-flex items-center justify-center dark:text-gray-400 hover:bg-gray-100 w-10 h-10 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5'
                    ),
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
                                P('neil.sims@flowbite.com', role='none', cls='text-sm font-medium text-gray-900 truncate dark:text-gray-300'),
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
                            cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-sm shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                        ),
                        cls='flex items-center ms-3'
                    ),
                    cls='flex items-center'
                ),
                cls='flex items-center justify-between'
            ),
            cls='px-3 py-3 lg:px-5 lg:pl-3'
        ),
        cls='fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700'
) 

def SidebarItem(name, href = "#", icon=None):
    return Li(
        A(
            icon,
            Span(name, cls='ms-3'),
            href=href + "#",
            hx_boost="true",
            hx_target="#content",
            hx_swap_oob=True,
            cls='flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group'
        )
    )

sidebar_items = [
    SidebarItem("Home", href="/"),
    SidebarItem("Typography", href="/typography"),
    SidebarItem("Buttons", href="/buttons"),
    SidebarItem("Containers", href="/containers"),
]

def Sidebar():
    return Aside(
        Div(
            Ul(
                *sidebar_items,
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800'
        ),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 dark:bg-gray-800 dark:border-gray-700'
    )

def Main(content):
    return Div(
        Div(content,
            cls='p-4 mt-14',
            id='content',
        ),
        cls='p-4'
    )