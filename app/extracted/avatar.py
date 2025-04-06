from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The avatar component can be used as a visual identifier for a user profile on your website and you can use the examples from Flowbite to modify the styles and sizes of these components using the utility classes from Tailwind CSS.'),
    H2(
        'Default avatar',
        Span(id='default-avatar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default avatar', href='#default-avatar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to create a circle and rounded avatar on an image element.'),
    component_showcase(Div(
        DiceBearAvatar('Nikola Dendic',h=10,w=10),
        DiceBearAvatar('Nikola Dendic',h=10,w=10,cls=Round.sm),
        cls='flex gap-2'
), code="""Div(
    DiceBearAvatar('Nikola Dendic',h=10,w=10),
    DiceBearAvatar('Nikola Dendic',h=10,w=10,cls=Round.sm),
    cls='flex gap-2'
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Bordered',
        Span(id='bordered', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Bordered', href='#bordered', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply a border around the avatar component you can use the',
        Code('ring-{color}'),
        'class from Tailwind CSS.'
    ),
    component_showcase(Div(
    DiceBearAvatar('Nikola Dendic',h=10,w=10, cls='rounded-full ring-2 ring-gray-300 dark:ring-gray-500')
), code="""Div(
    DiceBearAvatar('Nikola Dendic',h=10,w=10, cls='p-1 rounded-full ring-2 ring-gray-300 dark:ring-gray-500')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Placeholder icon',
        Span(id='placeholder-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Placeholder icon', href='#placeholder-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example as a placeholder icon for the user profile when there is no custom image available.'),
    component_showcase(Div(
    Div(
        Icon("user",cls='w-10 h-10'),
        cls='relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600'
    )
), code="""Div(
    Icon("user",cls='w-10 h-10'),
    cls='relative w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600'
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Placeholder initials',
        Span(id='placeholder-initials', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Placeholder initials', href='#placeholder-initials', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the initials of the user’s first and last name as a placeholder when no profile picture is available.'),
    component_showcase(Div(
    Div(
        Span('JL', cls='font-medium text-gray-600 dark:text-gray-300'),
        cls='relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600'
    )
), code="""Div(
    Div(
        Span('JL', cls='font-medium text-gray-600 dark:text-gray-300'),
        cls='relative inline-flex items-center justify-center w-10 h-10 overflow-hidden bg-gray-100 rounded-full dark:bg-gray-600'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Dot indicator',
        Span(id='dot-indicator', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dot indicator', href='#dot-indicator', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use a dot element relative to the avatar component as an indicator for the user (eg. online or offline status).'),
    component_showcase(Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Span(cls='top-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
        Span(cls='absolute top-0 left-8 transform -translate-y-1/2 w-3.5 h-3.5 bg-red-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Span(cls='bottom-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
        Span(cls='absolute bottom-0 left-8 transform translate-y-1/4 w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    cls='flex gap-2'
), code="""Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Span(cls='top-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
        Span(cls='absolute top-0 left-8 transform -translate-y-1/2 w-3.5 h-3.5 bg-red-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Span(cls='bottom-0 left-7 absolute w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
        Span(cls='absolute bottom-0 left-8 transform translate-y-1/4 w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full'),
        cls='relative'
    ),
    cls='flex gap-2'
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Stacked',
        Span(id='stacked', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Stacked', href='#stacked', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example if you want to stack a group of users by overlapping the avatar components.'),
    component_showcase(Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Roberta Casas',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Bonnie Green',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        cls='flex -space-x-4 rtl:space-x-reverse'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Roberta Casas',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Bonnie Green',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        A('+99', href='#', cls='flex items-center justify-center w-10 h-10 text-xs font-medium text-white bg-gray-700 border-2 border-white rounded-full hover:bg-gray-600 dark:border-gray-800'),
        cls='flex -space-x-4 rtl:space-x-reverse'
    )
), code="""Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Roberta Casas',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Bonnie Green',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        cls='flex -space-x-4 rtl:space-x-reverse'
    ),
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Roberta Casas',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        DiceBearAvatar('Bonnie Green',h=10,w=10, cls='border-2 border-white rounded-full dark:border-gray-800'),
        A('+99', href='#', cls='flex items-center justify-center w-10 h-10 text-xs font-medium text-white bg-gray-700 border-2 border-white rounded-full hover:bg-gray-600 dark:border-gray-800'),
        cls='flex -space-x-4 rtl:space-x-reverse'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Avatar text',
        Span(id='avatar-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Avatar text', href='#avatar-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used if you want to show additional information in the form of text elements such as the user’s name and join date.'),
    component_showcase(Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Div(
            Div('Jese Leos'),
            Div('Joined in August 2014', cls='text-sm text-gray-500 dark:text-gray-400'),
            cls='font-medium dark:text-white'
        ),
        cls='flex items-center gap-4'
    )
), code="""Div(
    Div(
        DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-full'),
        Div(
            Div('Jese Leos'),
            Div('Joined in August 2014', cls='text-sm text-gray-500 dark:text-gray-400'),
            cls='font-medium dark:text-white'
        ),
        cls='flex items-center gap-4'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'User dropdown',
        Span(id='user-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User dropdown', href='#user-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example if you want to show a dropdown menu when clicking on the avatar component.'),
    component_showcase(Div(
    DiceBearAvatar('Bonnie Green',h=10,w=10, cls='cursor-pointer',data_dropdown_toggle='userDropdown', data_dropdown_placement='bottom-start'),
    Div(
        Div(
            Div('Bonnie Green'),
            Div('name@flowbite.com', cls='font-medium truncate'),
            cls='px-4 py-3 text-sm text-gray-900 dark:text-white'
        ),
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
            aria_labelledby='avatarButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-1'
        ),
        id='userDropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    DiceBearAvatar('Bonnie Green',h=10,w=10, cls='cursor-pointer',data_dropdown_toggle='userDropdown', data_dropdown_placement='bottom-start'),
    Div(
        Div(
            Div('Bonnie Green'),
            Div('name@flowbite.com', cls='font-medium truncate'),
            cls='px-4 py-3 text-sm text-gray-900 dark:text-white'
        ),
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
            aria_labelledby='avatarButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-1'
        ),
        id='userDropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Choose from multiple sizing options for the avatar component from this example.'),
    component_showcase(Div(
    DiceBearAvatar('Jese Leos',h=6,w=6, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=8,w=8, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=20,w=20, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=36,w=36, cls='rounded-sm'),
    cls='flex gap-2'
), code="""Div(
    DiceBearAvatar('Jese Leos',h=6,w=6, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=8,w=8, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=10,w=10, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=20,w=20, cls='rounded-sm'),
    DiceBearAvatar('Jese Leos',h=36,w=36, cls='rounded-sm'),
    cls='flex gap-2'
)""", id="example_9",cls='mt-2 mb-6'),
    id='mainContent'
)
