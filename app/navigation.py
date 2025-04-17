from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from app.component_registry import component_registry

# Define themes in the new format required by the Fastbite ThemeSwitcher
default_themes_with_colors = {
    "none": {"label": "Default", "colors": ["bg-gray-300", "bg-gray-400", "bg-gray-500"]},
    "retro": {"label": "Retro Blue", "colors": ["bg-[#3c79f5]", "bg-[#265aea]", "bg-[#1e45d7]"]},
    "emerald": {"label": "Emerald Green", "colors": ["bg-emerald-400", "bg-emerald-500", "bg-emerald-600"]},
    "shadcn-like": {"label": "Shadcn Style", "colors": ["bg-zinc-300", "bg-zinc-500", "bg-zinc-700"]},
    "ocean-deep": {"label": "Ocean Deep", "colors": ["bg-blue-400", "bg-blue-500", "bg-blue-600"]},
    "sunset-glow": {"label": "Sunset Glow", "colors": ["bg-orange-400", "bg-orange-500", "bg-orange-600"]}
}

def Navbar():
    return Nav(
        Div(
            Div(
                Div(
                    Button(
                        Span('Open sidebar', cls='sr-only'),
                        Icon('menu', cls='w-6 h-6'),
                        data_drawer_target='logo-sidebar',
                        data_drawer_toggle='logo-sidebar',
                        aria_controls='logo-sidebar',
                        type='button',
                        cls='inline-flex items-center p-2 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
                    ),  
                    A(
                        Img(src='images/logo.png', alt='Logo', cls='h-8 me-3'),
                        Span('Fastbite', cls='self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white'),
                        href='/',
                        cls='flex ms-2 md:me-24'
                    ),
                    cls='flex items-center justify-start rtl:justify-end'
                ),
                Div(
                    ThemeSwitcher(themes=default_themes_with_colors),
                    ThemeToggle(),
                    Div(
                        Div(
                            Div(
                                Span('Open user menu', cls='sr-only'),
                                DiceBearAvatar(seed_name='Neil Sims',h=9,w=9),
                                type='button',
                                aria_expanded='false',
                                data_dropdown_toggle='dropdown-user',
                                cls='flex text-sm rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
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
                            cls='z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-sm shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                        ),
                        cls='flex items-center'
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

standard_sidebar_items = [
    NavLi("Home", href="/#", icon="home",hx_boost="true",hx_target="#content",hx_swap_oob=True),
    NavLi("Typography", href="/typography#", icon="type",hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Buttons", href="/buttons#", icon="stretch-horizontal",hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Containers", href="/containers#", icon="layout-dashboard",hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Playground", href="/playground#", icon="brush",hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Icons and images", href="/icons#", icon="image",hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Themes", href="/themes#", icon='palette',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Article", href="/article#", icon='file-text',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Badge", href="/badge#", icon='badge',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Dropdown", href="/dropdown#", icon='chevron-down',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Forms", href="/forms#", icon='book-text',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Markdown", href="/markdown#", icon='text-select',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Modals", href="/modals#", icon='picture-in-picture',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Navigation", href="/navigation#", icon='menu',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Progress", href="/progress#", icon='activity',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Ranges", href="/ranges#", icon='sliders',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Placeholders", href="/skeleton#", icon='square-dashed',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Slider", href="/slider#", icon='panel-right-open',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Tables", href="/tables#", icon='table',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
    NavLi("Tabs", href="/tabs#", icon='app-window',hx_boost="true",hx_target="#content",hx_swap_oob=True,),
]

component_sidebar_items = component_registry.get_sidebar_items(NavChildLi)
sidebar_items = standard_sidebar_items + component_sidebar_items

def Sidebar():
    return Aside(
        NavContainer(
            NavParentLi(
                *standard_sidebar_items,
                label="Components",
                icon='layout-dashboard',
                cls='space-y-2 font-medium'
            ),
            NavParentLi(
                *component_sidebar_items,
                label="Extracted",
                icon='layout-template',
                cls='space-y-2 font-medium'
            ),
            cls='h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800'
        ),
        Script('htmx.onLoad(function(content) {initSidebars();})'),
        id='logo-sidebar',
        aria_label='Sidebar',
        cls='fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 dark:bg-gray-800 dark:border-gray-700'
    )

def Main(content,cls=()):
    return DivCentered(
        Div(content,
            # Script('htmx.onLoad(function(content) {initSidebars();})'),
            cls='p-4 mt-18 max-w-4xl',
            id='content',

        ),
        cls=cls
    )