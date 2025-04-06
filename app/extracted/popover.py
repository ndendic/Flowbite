from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('Get started with the popover component to show any type of content inside a pop-up box when hovering or clicking over a trigger element. There are multiple examples that you can choose from, such as showing more information about a user profile, company profile, password strength, and more.'),
    P(
        'Make sure that you have the Flowbite JavaScript included in your project to enable the popover interactivity by following the',
        A('quickstart guide', href='https://flowbite.com/docs/getting-started/quickstart/'),
        '.'
    ),
    H2(
        'Default popover',
        Span(id='default-popover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default popover', href='#default-popover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Initialize a new popover by adding the',
        Code('data-popover-target="{elementId}"'),
        'data attribute to the trigger element where',
        Code('elementId'),
        'is the id of the popover component.'
    ),
    component_showcase(Div(
    Button('Default popover', data_popover_target='popover-default', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover title', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-default',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Default popover', data_popover_target='popover-default', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover title', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-default',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'User profile',
        Span(id='user-profile', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User profile', href='#user-profile', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show more information about a user profile when hovering over the trigger component.'),
    component_showcase(Div(
    Button('User profile', data_popover_target='popover-user-profile', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos', cls='w-10 h-10 rounded-full'),
                    href='#'
                ),
                Div(
                    Button('Follow', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-1.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800')
                ),
                cls='flex items-center justify-between mb-2'
            ),
            P(
                A('Jese Leos', href='#'),
                cls='text-base font-semibold leading-none text-gray-900 dark:text-white'
            ),
            P(
                A('@jeseleos', href='#', cls='hover:underline'),
                cls='mb-3 text-sm font-normal'
            ),
            P(
                'Open-source contributor. Building',
                A('flowbite.com', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                '.',
                cls='mb-4 text-sm'
            ),
            Ul(
                Li(
                    A(
                        Span('799', cls='font-semibold text-gray-900 dark:text-white'),
                        Span('Following'),
                        href='#',
                        cls='hover:underline'
                    ),
                    cls='me-2'
                ),
                Li(
                    A(
                        Span('3,758', cls='font-semibold text-gray-900 dark:text-white'),
                        Span('Followers'),
                        href='#',
                        cls='hover:underline'
                    )
                ),
                cls='flex text-sm'
            ),
            cls='p-3'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-user-profile',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    Button('User profile', data_popover_target='popover-user-profile', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos', cls='w-10 h-10 rounded-full'),
                    href='#'
                ),
                Div(
                    Button('Follow', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-1.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800')
                ),
                cls='flex items-center justify-between mb-2'
            ),
            P(
                A('Jese Leos', href='#'),
                cls='text-base font-semibold leading-none text-gray-900 dark:text-white'
            ),
            P(
                A('@jeseleos', href='#', cls='hover:underline'),
                cls='mb-3 text-sm font-normal'
            ),
            P(
                'Open-source contributor. Building',
                A('flowbite.com', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                '.',
                cls='mb-4 text-sm'
            ),
            Ul(
                Li(
                    A(
                        Span('799', cls='font-semibold text-gray-900 dark:text-white'),
                        Span('Following'),
                        href='#',
                        cls='hover:underline'
                    ),
                    cls='me-2'
                ),
                Li(
                    A(
                        Span('3,758', cls='font-semibold text-gray-900 dark:text-white'),
                        Span('Followers'),
                        href='#',
                        cls='hover:underline'
                    )
                ),
                cls='flex text-sm'
            ),
            cls='p-3'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-user-profile',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Company profile',
        Span(id='company-profile', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Company profile', href='#company-profile', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show more information about a company profile.'),
    component_showcase(Div(
    Button('Company profile', data_popover_target='popover-company-profile', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    A(
                        Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite logo', cls='w-8 h-8 rounded-full'),
                        href='#',
                        cls='block p-2 bg-gray-100 rounded-lg dark:bg-gray-700'
                    ),
                    cls='me-3 shrink-0'
                ),
                Div(
                    P(
                        A('Flowbite', href='#', cls='hover:underline'),
                        cls='mb-1 text-base font-semibold leading-none text-gray-900 dark:text-white'
                    ),
                    P('Tech company', cls='mb-3 text-sm font-normal'),
                    P('Open-source library of Tailwind CSS components and Figma design system.', cls='mb-4 text-sm'),
                    Ul(
                        Li(
                            Span(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M6.487 1.746c0 4.192 3.592 1.66 4.592 5.754 0 .828 1 1.5 2 1.5s2-.672 2-1.5a1.5 1.5 0 0 1 1.5-1.5h1.5m-16.02.471c4.02 2.248 1.776 4.216 4.878 5.645C10.18 13.61 9 19 9 19m9.366-6h-2.287a3 3 0 0 0-3 3v2m6-8a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 21 20',
                                    cls='w-3.5 h-3.5'
                                ),
                                cls='me-2 font-semibold text-gray-400'
                            ),
                            A('https://flowbite.com/', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                            cls='flex items-center mb-2'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(d='M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 20 18',
                                    cls='w-3.5 h-3.5'
                                ),
                                cls='me-2 font-semibold text-gray-400'
                            ),
                            Span('4,567,346 people like this including 5 of your friends', cls='-mt-1'),
                            cls='flex items-start mb-2'
                        ),
                        cls='text-sm'
                    ),
                    Div(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        A('+3', href='#', cls='flex items-center justify-center w-8 h-8 text-xs font-medium text-white bg-gray-400 border-2 border-white rounded-full hover:bg-gray-500 dark:border-gray-800'),
                        cls='flex mb-3 -space-x-3 rtl:space-x-reverse'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 18 18',
                                cls='w-3.5 h-3.5 me-2.5'
                            ),
                            'Like page',
                            type='button',
                            cls='inline-flex items-center justify-center w-full px-5 py-2 me-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                        ),
                        Button(
                            Svg(
                                Path(d='M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 3',
                                cls='w-3.5 h-3.5'
                            ),
                            id='dropdown-button',
                            data_dropdown_toggle='dropdown-menu',
                            data_dropdown_placement='right',
                            type='button',
                            cls='inline-flex items-center px-3 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg shrink-0 focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                        ),
                        cls='flex'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('Report this page', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Add to favorites', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Block this page', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Invite users', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdown-button',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-menu',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    )
                ),
                cls='flex'
            ),
            cls='p-3'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-company-profile',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-80 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    Button('Company profile', data_popover_target='popover-company-profile', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    A(
                        Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite logo', cls='w-8 h-8 rounded-full'),
                        href='#',
                        cls='block p-2 bg-gray-100 rounded-lg dark:bg-gray-700'
                    ),
                    cls='me-3 shrink-0'
                ),
                Div(
                    P(
                        A('Flowbite', href='#', cls='hover:underline'),
                        cls='mb-1 text-base font-semibold leading-none text-gray-900 dark:text-white'
                    ),
                    P('Tech company', cls='mb-3 text-sm font-normal'),
                    P('Open-source library of Tailwind CSS components and Figma design system.', cls='mb-4 text-sm'),
                    Ul(
                        Li(
                            Span(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M6.487 1.746c0 4.192 3.592 1.66 4.592 5.754 0 .828 1 1.5 2 1.5s2-.672 2-1.5a1.5 1.5 0 0 1 1.5-1.5h1.5m-16.02.471c4.02 2.248 1.776 4.216 4.878 5.645C10.18 13.61 9 19 9 19m9.366-6h-2.287a3 3 0 0 0-3 3v2m6-8a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 21 20',
                                    cls='w-3.5 h-3.5'
                                ),
                                cls='me-2 font-semibold text-gray-400'
                            ),
                            A('https://flowbite.com/', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                            cls='flex items-center mb-2'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(d='M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 20 18',
                                    cls='w-3.5 h-3.5'
                                ),
                                cls='me-2 font-semibold text-gray-400'
                            ),
                            Span('4,567,346 people like this including 5 of your friends', cls='-mt-1'),
                            cls='flex items-start mb-2'
                        ),
                        cls='text-sm'
                    ),
                    Div(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt=True, cls='w-8 h-8 border-2 border-white rounded-full dark:border-gray-800'),
                        A('+3', href='#', cls='flex items-center justify-center w-8 h-8 text-xs font-medium text-white bg-gray-400 border-2 border-white rounded-full hover:bg-gray-500 dark:border-gray-800'),
                        cls='flex mb-3 -space-x-3 rtl:space-x-reverse'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 18 18',
                                cls='w-3.5 h-3.5 me-2.5'
                            ),
                            'Like page',
                            type='button',
                            cls='inline-flex items-center justify-center w-full px-5 py-2 me-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                        ),
                        Button(
                            Svg(
                                Path(d='M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 3',
                                cls='w-3.5 h-3.5'
                            ),
                            id='dropdown-button',
                            data_dropdown_toggle='dropdown-menu',
                            data_dropdown_placement='right',
                            type='button',
                            cls='inline-flex items-center px-3 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg shrink-0 focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                        ),
                        cls='flex'
                    ),
                    Div(
                        Ul(
                            Li(
                                A('Report this page', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Add to favorites', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Block this page', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            Li(
                                A('Invite users', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                            ),
                            aria_labelledby='dropdown-button',
                            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                        ),
                        id='dropdown-menu',
                        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                    )
                ),
                cls='flex'
            ),
            cls='p-3'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-company-profile',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-80 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Image popover',
        Span(id='image-popover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image popover', href='#image-popover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to trigger a popover component with detailed information and an image when hovering over a portion of highlighted text inspired by Wikipedia and other large news outlets.'),
    component_showcase(Div(
    P(
        'Due to its central geographic location in Southern Europe,',
        A('Italy', href='#', data_popover_target='popover-image', cls='text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in insular Italy',
        cls='text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('About Italy', cls='font-semibold text-gray-900 dark:text-white'),
                    P('Italy is located in the middle of the Mediterranean Sea, in Southern Europe it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city.'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 6 10',
                            cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                        ),
                        href='#',
                        cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
                    ),
                    cls='space-y-2'
                ),
                cls='col-span-3 p-3'
            ),
            Img(src='/docs/images/popovers/italy.png', alt='Italy map', cls='h-full col-span-2'),
            cls='grid grid-cols-5'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-image',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-96 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    P(
        'Due to its central geographic location in Southern Europe,',
        A('Italy', href='#', data_popover_target='popover-image', cls='text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in insular Italy',
        cls='text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('About Italy', cls='font-semibold text-gray-900 dark:text-white'),
                    P('Italy is located in the middle of the Mediterranean Sea, in Southern Europe it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city.'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 6 10',
                            cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                        ),
                        href='#',
                        cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
                    ),
                    cls='space-y-2'
                ),
                cls='col-span-3 p-3'
            ),
            Img(src='/docs/images/popovers/italy.png', alt='Italy map', cls='h-full col-span-2'),
            cls='grid grid-cols-5'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-image',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-96 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Description popover',
        Span(id='description-popover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Description popover', href='#description-popover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Show helpful information inside a popover when hovering over a question mark button.'),
    component_showcase(Div(
    P(
        'This is just some informational text',
        Button(
            Svg(
                Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                aria_hidden='true',
                fill='currentColor',
                viewbox='0 0 20 20',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-4 h-4 ms-2 text-gray-400 hover:text-gray-500'
            ),
            Span('Show information', cls='sr-only'),
            data_popover_target='popover-description',
            data_popover_placement='bottom-end',
            type='button'
        ),
        cls='flex items-center text-sm text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            H3('Activity growth - Incremental', cls='font-semibold text-gray-900 dark:text-white'),
            P('Report helps navigate cumulative growth of community activities. Ideally, the chart should have a growing trend, as stagnating chart signifies a significant decrease of community activity.'),
            H3('Calculation', cls='font-semibold text-gray-900 dark:text-white'),
            P('For each date bucket, the all-time volume of activities is calculated. This means that activities in period n contain all activities up to period n, plus the activities generated by your community in period.'),
            A(
                'Read more',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                ),
                href='#',
                cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
            ),
            cls='p-3 space-y-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-description',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
    )
), code="""Div(
    P(
        'This is just some informational text',
        Button(
            Svg(
                Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                aria_hidden='true',
                fill='currentColor',
                viewbox='0 0 20 20',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-4 h-4 ms-2 text-gray-400 hover:text-gray-500'
            ),
            Span('Show information', cls='sr-only'),
            data_popover_target='popover-description',
            data_popover_placement='bottom-end',
            type='button'
        ),
        cls='flex items-center text-sm text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            H3('Activity growth - Incremental', cls='font-semibold text-gray-900 dark:text-white'),
            P('Report helps navigate cumulative growth of community activities. Ideally, the chart should have a growing trend, as stagnating chart signifies a significant decrease of community activity.'),
            H3('Calculation', cls='font-semibold text-gray-900 dark:text-white'),
            P('For each date bucket, the all-time volume of activities is calculated. This means that activities in period n contain all activities up to period n, plus the activities generated by your community in period.'),
            A(
                'Read more',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                ),
                href='#',
                cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
            ),
            cls='p-3 space-y-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-description',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Progress popover',
        Span(id='progress-popover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Progress popover', href='#progress-popover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Show a progress bar with details inside a popover when hovering over a settings button.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='M3 12v3c0 1.657 3.134 3 7 3s7-1.343 7-3v-3c0 1.657-3.134 3-7 3s-7-1.343-7-3z'),
            Path(d='M3 7v3c0 1.657 3.134 3 7 3s7-1.343 7-3V7c0 1.657-3.134 3-7 3S3 8.657 3 7z'),
            Path(d='M17 5c0 1.657-3.134 3-7 3S3 6.657 3 5s3.134-3 7-3 7 1.343 7 3z'),
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-4 h-4 me-2'
        ),
        'Storage status',
        data_popover_target='popover-description',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 inline-flex items-center focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-2.5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            H3('Available storage', cls='font-semibold text-gray-900 dark:text-white'),
            P(
                'This server has',
                Span('30', cls='font-semibold text-gray-900 dark:text-white'),
                'of',
                Span('150 GB', cls='font-semibold text-gray-900 dark:text-white'),
                'of block storage remaining.'
            ),
            Div(
                Div(style='width: 85%', cls='bg-red-600 h-2.5 rounded-full'),
                cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
            ),
            A(
                'Upgrade now',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                ),
                href='#',
                cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700'
            ),
            cls='p-3 space-y-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-description',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
    )
), code="""Div(
    Button(
        Svg(
            Path(d='M3 12v3c0 1.657 3.134 3 7 3s7-1.343 7-3v-3c0 1.657-3.134 3-7 3s-7-1.343-7-3z'),
            Path(d='M3 7v3c0 1.657 3.134 3 7 3s7-1.343 7-3V7c0 1.657-3.134 3-7 3S3 8.657 3 7z'),
            Path(d='M17 5c0 1.657-3.134 3-7 3S3 6.657 3 5s3.134-3 7-3 7 1.343 7 3z'),
            fill='currentColor',
            viewbox='0 0 20 20',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-4 h-4 me-2'
        ),
        'Storage status',
        data_popover_target='popover-description',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 inline-flex items-center focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-2.5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            H3('Available storage', cls='font-semibold text-gray-900 dark:text-white'),
            P(
                'This server has',
                Span('30', cls='font-semibold text-gray-900 dark:text-white'),
                'of',
                Span('150 GB', cls='font-semibold text-gray-900 dark:text-white'),
                'of block storage remaining.'
            ),
            Div(
                Div(style='width: 85%', cls='bg-red-600 h-2.5 rounded-full'),
                cls='w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700'
            ),
            A(
                'Upgrade now',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                ),
                href='#',
                cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700'
            ),
            cls='p-3 space-y-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-description',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Password strength',
        Span(id='password-strength', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Password strength', href='#password-strength', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Dynamically show the password strength progress when creating a new password positioned relative to the input element.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='email', id='email', placeholder='name@flowbite.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(data_popover_target='popover-password', data_popover_placement='bottom', type='password', id='password', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Div(
                    H3('Must have at least 6 characters', cls='font-semibold text-gray-900 dark:text-white'),
                    Div(
                        Div(cls='h-1 bg-orange-300 dark:bg-orange-400'),
                        Div(cls='h-1 bg-orange-300 dark:bg-orange-400'),
                        Div(cls='h-1 bg-gray-200 dark:bg-gray-600'),
                        Div(cls='h-1 bg-gray-200 dark:bg-gray-600'),
                        cls='grid grid-cols-4 gap-2'
                    ),
                    P('Itâ\x80\x99s better to have:'),
                    Ul(
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 12',
                                cls='w-3.5 h-3.5 me-2 text-green-400 dark:text-green-500'
                            ),
                            'Upper & lower case letters',
                            cls='flex items-center mb-1'
                        ),
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 14 14',
                                cls='w-3 h-3 me-2.5 text-gray-300 dark:text-gray-400'
                            ),
                            'A symbol (#$&)',
                            cls='flex items-center mb-1'
                        ),
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 14 14',
                                cls='w-3 h-3 me-2.5 text-gray-300 dark:text-gray-400'
                            ),
                            'A longer password (min. 12 chars.)',
                            cls='flex items-center'
                        )
                    ),
                    cls='p-3 space-y-2'
                ),
                Div(data_popper_arrow=True),
                data_popover=True,
                id='popover-password',
                role='tooltip',
                cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
            ),
            cls='mb-6'
        ),
        Div(
            Div(
                Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800'),
                cls='flex items-center h-5'
            ),
            Label('Remember me', fr='remember', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-start mb-6'
        ),
        Button('Submit', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800')
    )
), code="""Div(
    Form(
        Div(
            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='email', id='email', placeholder='name@flowbite.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(data_popover_target='popover-password', data_popover_placement='bottom', type='password', id='password', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Div(
                    H3('Must have at least 6 characters', cls='font-semibold text-gray-900 dark:text-white'),
                    Div(
                        Div(cls='h-1 bg-orange-300 dark:bg-orange-400'),
                        Div(cls='h-1 bg-orange-300 dark:bg-orange-400'),
                        Div(cls='h-1 bg-gray-200 dark:bg-gray-600'),
                        Div(cls='h-1 bg-gray-200 dark:bg-gray-600'),
                        cls='grid grid-cols-4 gap-2'
                    ),
                    P('Itâ\x80\x99s better to have:'),
                    Ul(
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 12',
                                cls='w-3.5 h-3.5 me-2 text-green-400 dark:text-green-500'
                            ),
                            'Upper & lower case letters',
                            cls='flex items-center mb-1'
                        ),
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 14 14',
                                cls='w-3 h-3 me-2.5 text-gray-300 dark:text-gray-400'
                            ),
                            'A symbol (#$&)',
                            cls='flex items-center mb-1'
                        ),
                        Li(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 14 14',
                                cls='w-3 h-3 me-2.5 text-gray-300 dark:text-gray-400'
                            ),
                            'A longer password (min. 12 chars.)',
                            cls='flex items-center'
                        )
                    ),
                    cls='p-3 space-y-2'
                ),
                Div(data_popper_arrow=True),
                data_popover=True,
                id='popover-password',
                role='tooltip',
                cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-72 dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400'
            ),
            cls='mb-6'
        ),
        Div(
            Div(
                Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800'),
                cls='flex items-center h-5'
            ),
            Label('Remember me', fr='remember', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-start mb-6'
        ),
        Button('Submit', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800')
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Placement',
        Span(id='placement', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Placement', href='#placement', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Set the position of the popover component relative to the trigger element by using the',
        Code('data-popover-placement="{top|right|bottom|left}"'),
        'data attribute and its values.'
    ),
    component_showcase(Div(
    Button('Top popover', data_popover_target='popover-top', data_popover_placement='top', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover top', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-top',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Right popover', data_popover_target='popover-right', data_popover_placement='right', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover right', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-right',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Bottom popover', data_popover_target='popover-bottom', data_popover_placement='bottom', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover bottom', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-bottom',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Left popover', data_popover_target='popover-left', data_popover_placement='left', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover left', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-left',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Top popover', data_popover_target='popover-top', data_popover_placement='top', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover top', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-top',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Right popover', data_popover_target='popover-right', data_popover_placement='right', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover right', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-right',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Bottom popover', data_popover_target='popover-bottom', data_popover_placement='bottom', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover bottom', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-bottom',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Left popover', data_popover_target='popover-left', data_popover_placement='left', type='button', cls='text-white mb-3 me-4 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover left', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-left',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Triggering',
        Span(id='triggering', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Triggering', href='#triggering', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Manually set the trigger event by adding the',
        Code('data-popover-trigger="{hover|click}"'),
        'data attribute to the trigger element choosing between a hover or click event. By default it is set to',
        Code('hover'),
        '.'
    ),
    component_showcase(Div(
    Button('Hover popover', data_popover_target='popover-hover', data_popover_trigger='hover', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-3 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover hover', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-hover',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Click popover', data_popover_target='popover-click', data_popover_trigger='click', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover click', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-click',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Hover popover', data_popover_target='popover-hover', data_popover_trigger='hover', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-3 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover hover', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-hover',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    ),
    Button('Click popover', data_popover_target='popover-click', data_popover_trigger='click', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover click', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-click',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Offset',
        Span(id='offset', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Offset', href='#offset', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Increase or decrease the default offset by adding the',
        Code('data-popover-offset="{offset}"'),
        'data attribute where the value is an integer.'
    ),
    component_showcase(Div(
    Button('Offset popover', data_popover_target='popover-offset', data_popover_offset='30', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover offset', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-offset',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Offset popover', data_popover_target='popover-offset', data_popover_offset='30', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover offset', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-offset',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Animation',
        Span(id='animation', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Animation', href='#animation', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Customize the animation of the popover component by using the utility classes from Tailwind CSS such as',
        Code('transition-opacity'),
        'and',
        Code('duration-{x}'),
        '.'
    ),
    component_showcase(Div(
    Button('Animated popover', data_popover_target='popover-animation', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover animation', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-animation',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Animated popover', data_popover_target='popover-animation', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover animation', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        Div(data_popper_arrow=True),
        data_popover=True,
        id='popover-animation',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H2(
        'Disable arrow',
        Span(id='disable-arrow', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disable arrow', href='#disable-arrow', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also disable the popover arrow by not including the',
        Code('data-popper-arrow'),
        'element.'
    ),
    component_showcase(Div(
    Button('Default popover', data_popover_target='popover-no-arrow', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover no arrow', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        data_popover=True,
        id='popover-no-arrow',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Button('Default popover', data_popover_target='popover-no-arrow', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            H3('Popover no arrow', cls='font-semibold text-gray-900 dark:text-white'),
            cls='px-3 py-2 bg-gray-100 border-b border-gray-200 rounded-t-lg dark:border-gray-600 dark:bg-gray-700'
        ),
        Div(
            P("And here's some amazing content. It's very engaging. Right?"),
            cls='px-3 py-2'
        ),
        data_popover=True,
        id='popover-no-arrow',
        role='tooltip',
        cls='absolute z-10 invisible inline-block w-64 text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 dark:text-gray-400 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The Popover API from Flowbite can be used to create an object that will show a pop-up box relative to the main trigger element based on the parameters, options, and methods that you provide.'),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Create a new Popover object with the object parameters like the trigger element, the popover content element, and extra options to set the placement and offset.'),
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
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Set the popover component as the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('triggerEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Set an element to trigger the popover when clicking or hovering (ie. a button, text).', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Use the options parameter to set the positioning of the popover element, trigger type, offset, and more.', cls='px-6 py-4'),
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
    P('Use the following options as the third parameter for the Popover object to set the positioning, offset, and the trigger type (hover or click).'),
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
                        Code('placement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td(
                        'Set the position of the popover element relative to the trigger element choosing from',
                        Code('top|right|bottom|left', cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('triggerType', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td(
                        'Set the event type that will trigger the popover content choosing between',
                        Code('hover|click|none', cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('offset', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Integer', cls='px-6 py-4 font-medium'),
                    Td('Set the offset distance between the popover and the trigger element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onHide', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the popover is hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onShow', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the popover is shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onToggle', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the popover visibility has been toggled.', cls='px-6 py-4'),
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
    P('Use the methods from the Popover object to programmatically show or hide the popover from directly JavaScript.'),
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
                        Code('show()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Popover object to show the popover content.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('hide()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Popover object to hide the popover content.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('toggle()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Popover object to toggle the visibility of the popover content.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('isVisible()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to check if the popover is visible or not.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnShow(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the popover has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnHide(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the popover has been hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnToggle(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the popover has been toggled.', cls='px-6 py-4'),
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
    P('Use following JavaScript as an example to learn how to initialize, set the options, and use the methods for the Popover object.'),
    P('First of all, set the target element as the popover itself and the trigger element which can be a button or text element.'),
    P('After that you can also set the options object to change the placement and trigger type of the popover, alongside with the callback functions.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the popover content element', cls='c1'),
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
                        Span("'popoverContent'", cls='s1'),
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
                        Span('// set the element that trigger the popover using hover or click', cls='c1'),
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
                        Span("'popoverButton'", cls='s1'),
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
                        Span('placement', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bottom'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerType', cls='nx'),
                        Span(':', cls='o'),
                        Span("'hover'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offset', cls='nx'),
                        Span(':', cls='o'),
                        Span('10', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onHide', cls='nx'),
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
                        Span("'popover is shown'", cls='s1'),
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
                        Span("'popover is hidden'", cls='s1'),
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
                        Span("'popover is toggled'", cls='s1'),
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
                        Span("'popoverContent'", cls='s1'),
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
    P('Create a new Popover object based on the options above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Popover', cls='nx'),
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
                        Span('* $triggerEl: required', cls='cm'),
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
                        Span('popover', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Popover', cls='nx'),
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
    P(
        'Use the',
        Code('show'),
        'and',
        Code('hide'),
        'methods on the Popover object to programmatically show and hide the popover element using JavaScript.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// show the popover', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('popover', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
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
                        Span('// hide the popover', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('popover', cls='nx'),
                        Span('.', cls='p'),
                        Span('hide', cls='nx'),
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
                        Span('// toggle the popover', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('popover', cls='nx'),
                        Span('.', cls='p'),
                        Span('toggle', cls='nx'),
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
                        Span('// check if popover is visible', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('popover', cls='nx'),
                        Span('.', cls='p'),
                        Span('isVisible', cls='nx'),
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
                        Span('// destroy popover object (removes event listeners and off-canvas Popper.js)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tooltip', cls='nx'),
                        Span('.', cls='p'),
                        Span('destroy', cls='nx'),
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
                        Span('// re-initialize popover object', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('tooltip', cls='nx'),
                        Span('.', cls='p'),
                        Span('init', cls='nx'),
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
    P('Use the following HTML code for the JavaScript example above.'),
    Div(
        Pre(
            Code(
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
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"popoverButton"', cls='s'),
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
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"rounded-lg bg-primary-700 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-primary-800 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Default popover', cls='cl'),
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
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('data-popover', cls='na'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"popoverContent"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"tooltip"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"invisible absolute z-10 inline-block w-64 rounded-lg border border-gray-200 bg-white text-sm text-gray-500 opacity-0 shadow-xs transition-opacity duration-300 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400"', cls='s'),
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
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"rounded-t-lg border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700"', cls='s'),
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
                        Span('h3', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-semibold text-gray-900 dark:text-white"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Popover title', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('h3', cls='nt'),
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
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"px-3 py-2"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        "And here's some amazing content. It's very engaging. Right?",
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
                        Span('data-popper-arrow', cls='na'),
                        Span('></', cls='p'),
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
        'from Flowbite then you can import the types for the Popover class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Popover', cls='nx'),
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
                        Span('PopoverOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('PopoverInterface', cls='nx'),
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
                        Span('// set the popover content element', cls='c1'),
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
                        Span("'popoverContent'", cls='s1'),
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
                        Span('// set the element that trigger the popover using hover or click', cls='c1'),
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
                        Span("'popoverButton'", cls='s1'),
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
                        Span('PopoverOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('placement', cls='nx'),
                        Span(':', cls='o'),
                        Span("'top'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerType', cls='nx'),
                        Span(':', cls='o'),
                        Span("'hover'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offset', cls='nx'),
                        Span(':', cls='o'),
                        Span('10', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onHide', cls='nx'),
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
                        Span("'popover is shown'", cls='s1'),
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
                        Span("'popover is hidden'", cls='s1'),
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
                        Span("'popover is toggled'", cls='s1'),
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
                        Span("'popoverContent'", cls='s1'),
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
                        Span('if', cls='k'),
                        Span('(', cls='p'),
                        Span('$targetEl', cls='nx'),
                        Span(')', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
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
                        Span('* targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* triggerEl: required', cls='cm'),
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
                        Span('popover', cls='nx'),
                        Span(':', cls='o'),
                        Span('PopoverInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Popover', cls='nx'),
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
                        Span('popover', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}', cls='p'),
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
