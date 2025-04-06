from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The dropdown component can be used to show a list of menu items when clicking on an element such as a button and hiding it when focusing outside of the triggering element.'),
    P(
        'Make sure to include',
        A('Flowbite’s JavaScript file', href='https://flowbite.com/docs/getting-started/quickstart/'),
        'inside your project to enable dropdowns.'
    ),
    H2(
        'Dropdown example',
        Span(id='dropdown-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown example', href='#dropdown-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you want to show a dropdown menu when clicking on an element make sure that you add the data attribute',
        Code('data-dropdown-toggle="dropdownId"'),
        'to the element (ie. a button) that will trigger the dropdown menu.'
    ),
    P(
        'The',
        Code('dropdownId'),
        'is the id of the dropdown menu element.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDefaultButton',
        data_dropdown_toggle='dropdown',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefaultButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDefaultButton',
        data_dropdown_toggle='dropdown',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefaultButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Dropdown hover',
        Span(id='dropdown-hover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown hover', href='#dropdown-hover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-dropdown-trigger="{hover|click}"'),
        'data attribute options to set whether the dropdown should be shown when hovering or clicking on the trigger element (ie. button).'
    ),
    P(
        'There’s a 300ms default delay when showing or hiding the dropdown due to UI/UX reasons and how it may affect the interaction with other components on the page. Generally, we recommend using the',
        Code('click'),
        'method.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown hover',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownHoverButton',
        data_dropdown_toggle='dropdownHover',
        data_dropdown_trigger='hover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownHoverButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHover',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown hover',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownHoverButton',
        data_dropdown_toggle='dropdownHover',
        data_dropdown_trigger='hover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownHoverButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHover',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H3(
        'Delay duration',
        Span(id='delay-duration', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Delay duration', href='#delay-duration', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can use the',
        Code('data-dropdown-delay={milliseconds}'),
        'data attribute to set they delay on when to show or hide the dropdown menu when using hover. You may want to use this depending on how the users interact with your interface. In this example we add 500 milliseconds instead of the default 300.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown hover',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDelayButton',
        data_dropdown_toggle='dropdownDelay',
        data_dropdown_delay='500',
        data_dropdown_trigger='hover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDelayButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDelay',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown hover',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDelayButton',
        data_dropdown_toggle='dropdownDelay',
        data_dropdown_delay='500',
        data_dropdown_trigger='hover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDelayButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDelay',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Dropdown divider',
        Span(id='dropdown-divider', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown divider', href='#dropdown-divider', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can use the',
        Code('divide-y divide-gray-100'),
        'classes to add separate elements inside the dropdown menu.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown divider',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDividerButton',
        data_dropdown_toggle='dropdownDivider',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            aria_labelledby='dropdownDividerButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDivider',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown divider',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownDividerButton',
        data_dropdown_toggle='dropdownDivider',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            aria_labelledby='dropdownDividerButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDivider',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Dropdown header',
        Span(id='dropdown-header', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown header', href='#dropdown-header', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show extra information outside of the list of menu items inside the dropdown.'),
    component_showcase(Div(
    Button(
        'Dropdown header',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownInformationButton',
        data_dropdown_toggle='dropdownInformation',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownInformationButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownInformation',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown header',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownInformationButton',
        data_dropdown_toggle='dropdownInformation',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownInformationButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownInformation',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Multi-level dropdown',
        Span(id='multi-level-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Multi-level dropdown', href='#multi-level-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to enable multi-level dropdown menus by adding stacked elements inside of each other.'),
    component_showcase(Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='multiLevelDropdownButton',
        data_dropdown_toggle='multi-dropdown',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
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
                            A('Overview', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('My downloads', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Billing', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Rewards', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='doubleDropdownButton',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='doubleDropdown',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                )
            ),
            Li(
                A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='multiLevelDropdownButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='multi-dropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='multiLevelDropdownButton',
        data_dropdown_toggle='multi-dropdown',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
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
                            A('Overview', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('My downloads', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Billing', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Rewards', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='doubleDropdownButton',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='doubleDropdown',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
                )
            ),
            Li(
                A('Earnings', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='multiLevelDropdownButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='multi-dropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Dropdown with checkbox',
        Span(id='dropdown-with-checkbox', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown with checkbox', href='#dropdown-with-checkbox', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Add multiple checkbox elements inside your dropdown menu to enable more advanced input interaction.'),
    component_showcase(Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownCheckboxButton',
        data_dropdown_toggle='dropdownDefaultCheckbox',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-1', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-2', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='checkbox-item-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-3', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-3', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            aria_labelledby='dropdownCheckboxButton',
            cls='p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDefaultCheckbox',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownCheckboxButton',
        data_dropdown_toggle='dropdownDefaultCheckbox',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-1', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-2', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='checkbox-item-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-3', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-3', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            aria_labelledby='dropdownCheckboxButton',
            cls='p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDefaultCheckbox',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H3(
        'Background hover',
        Span(id='background-hover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Background hover', href='#background-hover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to update the background color of a menu item when using a list of checkbox elements.'),
    component_showcase(Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownBgHoverButton',
        data_dropdown_toggle='dropdownBgHover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-4', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-5', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='checkbox-item-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-6', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-6', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownBgHoverButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownBgHover',
        cls='z-10 hidden w-48 bg-white rounded-lg shadow-sm dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownBgHoverButton',
        data_dropdown_toggle='dropdownBgHover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-4', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-5', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='checkbox-item-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-6', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default checkbox', fr='checkbox-item-6', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownBgHoverButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownBgHover',
        cls='z-10 hidden w-48 bg-white rounded-lg shadow-sm dark:bg-gray-700'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Helper text',
        Span(id='helper-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Helper text', href='#helper-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Add an extra helper text to each checkbox element inside the dropdown menu list with this example.'),
    component_showcase(Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownHelperButton',
        data_dropdown_toggle='dropdownHelper',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-1', aria_describedby='helper-checkbox-text-1', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Enable notifications'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-1', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-1',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-2', aria_describedby='helper-checkbox-text-2', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Enable 2FA auth'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-2', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-2',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-3', aria_describedby='helper-checkbox-text-3', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Subscribe newsletter'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-3', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-3',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownHelperButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHelper',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-60 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown checkbox',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownHelperButton',
        data_dropdown_toggle='dropdownHelper',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-1', aria_describedby='helper-checkbox-text-1', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Enable notifications'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-1', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-1',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-2', aria_describedby='helper-checkbox-text-2', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Enable 2FA auth'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-2', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-2',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-checkbox-3', aria_describedby='helper-checkbox-text-3', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Subscribe newsletter'),
                            P('Some helpful instruction goes over here.', id='helper-checkbox-text-3', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-checkbox-3',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownHelperButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHelper',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-60 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Dropdown with radio',
        Span(id='dropdown-with-radio', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown with radio', href='#dropdown-with-radio', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Enable more advanced interaction with your users by adding radio input elements inside the dropdown menu.'),
    component_showcase(Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioButton',
        data_dropdown_toggle='dropdownDefaultRadio',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='default-radio-1', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='default-radio-2', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='default-radio-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(id='default-radio-3', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-3', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            aria_labelledby='dropdownRadioButton',
            cls='p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDefaultRadio',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioButton',
        data_dropdown_toggle='dropdownDefaultRadio',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='default-radio-1', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='default-radio-2', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='default-radio-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Input(id='default-radio-3', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-3', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                    cls='flex items-center'
                )
            ),
            aria_labelledby='dropdownRadioButton',
            cls='p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDefaultRadio',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Background hover',
        Span(id='background-hover-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Background hover', href='#background-hover-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to update the background color when hovering over a menu item when using radio elements.'),
    component_showcase(Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioBgHoverButton',
        data_dropdown_toggle='dropdownRadioBgHover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='default-radio-4', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='default-radio-5', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='default-radio-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='default-radio-6', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-6', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownRadioBgHoverButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRadioBgHover',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioBgHoverButton',
        data_dropdown_toggle='dropdownRadioBgHover',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Input(id='default-radio-4', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='default-radio-5', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Checked state', fr='default-radio-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='default-radio-6', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Default radio', fr='default-radio-6', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownRadioBgHoverButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRadioBgHover',
        cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Helper text',
        Span(id='helper-text-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Helper text', href='#helper-text-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add an extra helper text inside of each radio element from the dropdown menu.'),
    component_showcase(Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioHelperButton',
        data_dropdown_toggle='dropdownRadioHelper',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-4', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Individual'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-4', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-4',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-5', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Company'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-5', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-5',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-6', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Non profit'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-6', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-6',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownRadioHelperButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRadioHelper',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-60 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRadioHelperButton',
        data_dropdown_toggle='dropdownRadioHelper',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-4', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Individual'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-4', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-4',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-5', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Company'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-5', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-5',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Div(
                        Input(id='helper-radio-6', name='helper-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                        cls='flex items-center h-5'
                    ),
                    Div(
                        Label(
                            Div('Non profit'),
                            P('Some helpful instruction goes over here.', id='helper-radio-text-6', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
                            fr='helper-radio-6',
                            cls='font-medium text-gray-900 dark:text-gray-300'
                        ),
                        cls='ms-2 text-sm'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownRadioHelperButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRadioHelper',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-60 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Dropdown with toggle switch',
        Span(id='dropdown-with-toggle-switch', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown with toggle switch', href='#dropdown-with-toggle-switch', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Show a list of toggle switch elements inside the dropdown menu to enable a yes or no type of choice.'),
    component_showcase(Div(
    Button(
        'Dropdown toggle',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownToggleButton',
        data_dropdown_toggle='dropdownToggle',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Enable notifications', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Enable 2FA authentication', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Subscribe to newsletter', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownToggleButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownToggle',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-72 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Dropdown toggle',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownToggleButton',
        data_dropdown_toggle='dropdownToggle',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Enable notifications', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Enable 2FA authentication', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Label(
                        Input(type='checkbox', value=True, cls='sr-only peer'),
                        Div(cls="relative w-9 h-5 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:translate-x-[-100%] peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all dark:border-gray-500 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Subscribe to newsletter', cls='ms-3 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='inline-flex items-center w-full cursor-pointer'
                    ),
                    cls='flex p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownToggleButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownToggle',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-72 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_12",cls='mt-2 mb-6'),
    H2(
        'Dropdown with scrolling',
        Span(id='dropdown-with-scrolling', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown with scrolling', href='#dropdown-with-scrolling', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used when you want to show a long list of items that won’t affect the height of the dropdown menu by enabling a scrolling behaviour.'),
    component_showcase(Div(
    Button(
        'Project users',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownUsersButton',
        data_dropdown_toggle='dropdownUsers',
        data_dropdown_placement='bottom',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Jese Leos',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Robert Gough',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Bonnie Green',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Leslie Livingston',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Michael Gough',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Joseph Mcfall',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Roberta Casas',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Neil Sims',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            aria_labelledby='dropdownUsersButton',
            cls='h-48 py-2 overflow-y-auto text-gray-700 dark:text-gray-200'
        ),
        A(
            Svg(
                Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-4 h-4 me-2'
            ),
            'Add new user',
            href='#',
            cls='flex items-center p-3 text-sm font-medium text-primary-600 border-t border-gray-200 rounded-b-lg bg-gray-50 dark:border-gray-600 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-primary-500 hover:underline'
        ),
        id='dropdownUsers',
        cls='z-10 hidden bg-white rounded-lg shadow-sm w-60 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Project users',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownUsersButton',
        data_dropdown_toggle='dropdownUsers',
        data_dropdown_placement='bottom',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Ul(
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Jese Leos',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Robert Gough',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Bonnie Green',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Leslie Livingston',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Michael Gough',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Joseph Mcfall',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Roberta Casas',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            Li(
                A(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-6 h-6 me-2 rounded-full'),
                    'Neil Sims',
                    href='#',
                    cls='flex items-center px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white'
                )
            ),
            aria_labelledby='dropdownUsersButton',
            cls='h-48 py-2 overflow-y-auto text-gray-700 dark:text-gray-200'
        ),
        A(
            Svg(
                Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-4 h-4 me-2'
            ),
            'Add new user',
            href='#',
            cls='flex items-center p-3 text-sm font-medium text-primary-600 border-t border-gray-200 rounded-b-lg bg-gray-50 dark:border-gray-600 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-primary-500 hover:underline'
        ),
        id='dropdownUsers',
        cls='z-10 hidden bg-white rounded-lg shadow-sm w-60 dark:bg-gray-700'
    )
)""", id="example_13",cls='mt-2 mb-6'),
    H2(
        'Dropdown with search',
        Span(id='dropdown-with-search', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown with search', href='#dropdown-with-search', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example if you want to add a search bar inside the dropdown menu to be able to filter through a long list of menu items with scrolling behaviour.'),
    component_showcase(Div(
    Button(
        'Dropdown search',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownSearchButton',
        data_dropdown_toggle='dropdownSearch',
        data_dropdown_placement='bottom',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            Label('Search', fr='input-group-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='input-group-search', placeholder='Search user', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='p-3'
        ),
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-11', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Bonnie Green', fr='checkbox-item-11', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-12', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Jese Leos', fr='checkbox-item-12', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-13', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Michael Gough', fr='checkbox-item-13', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-14', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Robert Wall', fr='checkbox-item-14', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-15', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Joseph Mcfall', fr='checkbox-item-15', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-16', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Leslie Livingston', fr='checkbox-item-16', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-17', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Roberta Casas', fr='checkbox-item-17', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownSearchButton',
            cls='h-48 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200'
        ),
        A(
            Svg(
                Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-6a1 1 0 1 0 0 2h6a1 1 0 1 0 0-2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-4 h-4 me-2'
            ),
            'Delete user',
            href='#',
            cls='flex items-center p-3 text-sm font-medium text-red-600 border-t border-gray-200 rounded-b-lg bg-gray-50 dark:border-gray-600 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-red-500 hover:underline'
        ),
        id='dropdownSearch',
        cls='z-10 hidden bg-white rounded-lg shadow-sm w-60 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown search',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownSearchButton',
        data_dropdown_toggle='dropdownSearch',
        data_dropdown_placement='bottom',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            Label('Search', fr='input-group-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='input-group-search', placeholder='Search user', cls='block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='p-3'
        ),
        Ul(
            Li(
                Div(
                    Input(id='checkbox-item-11', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Bonnie Green', fr='checkbox-item-11', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(checked=True, id='checkbox-item-12', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Jese Leos', fr='checkbox-item-12', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-13', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Michael Gough', fr='checkbox-item-13', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-14', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Robert Wall', fr='checkbox-item-14', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-15', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Joseph Mcfall', fr='checkbox-item-15', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-16', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Leslie Livingston', fr='checkbox-item-16', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            Li(
                Div(
                    Input(id='checkbox-item-17', type='checkbox', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                    Label('Roberta Casas', fr='checkbox-item-17', cls='w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                    cls='flex items-center ps-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                )
            ),
            aria_labelledby='dropdownSearchButton',
            cls='h-48 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200'
        ),
        A(
            Svg(
                Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-6a1 1 0 1 0 0 2h6a1 1 0 1 0 0-2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-4 h-4 me-2'
            ),
            'Delete user',
            href='#',
            cls='flex items-center p-3 text-sm font-medium text-red-600 border-t border-gray-200 rounded-b-lg bg-gray-50 dark:border-gray-600 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-red-500 hover:underline'
        ),
        id='dropdownSearch',
        cls='z-10 hidden bg-white rounded-lg shadow-sm w-60 dark:bg-gray-700'
    )
)""", id="example_14",cls='mt-2 mb-6'),
    H2(
        'Menu icon',
        Span(id='menu-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Menu icon', href='#menu-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the menu icon trigger element on components such as cards as an alternative element to the button.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 4 15',
            cls='w-5 h-5'
        ),
        id='dropdownMenuIconButton',
        data_dropdown_toggle='dropdownDots',
        type='button',
        cls='inline-flex items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
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
            aria_labelledby='dropdownMenuIconButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDots',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    ),
    Button(
        Svg(
            Path(d='M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 16 3',
            cls='w-5 h-5'
        ),
        id='dropdownMenuIconHorizontalButton',
        data_dropdown_toggle='dropdownDotsHorizontal',
        type='button',
        cls='inline-flex items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
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
            aria_labelledby='dropdownMenuIconHorizontalButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDotsHorizontal',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        Svg(
            Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 4 15',
            cls='w-5 h-5'
        ),
        id='dropdownMenuIconButton',
        data_dropdown_toggle='dropdownDots',
        type='button',
        cls='inline-flex items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
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
            aria_labelledby='dropdownMenuIconButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDots',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    ),
    Button(
        Svg(
            Path(d='M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 16 3',
            cls='w-5 h-5'
        ),
        id='dropdownMenuIconHorizontalButton',
        data_dropdown_toggle='dropdownDotsHorizontal',
        type='button',
        cls='inline-flex items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
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
            aria_labelledby='dropdownMenuIconHorizontalButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Separated link', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownDotsHorizontal',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_15",cls='mt-2 mb-6'),
    H2(
        'Notification bell',
        Span(id='notification-bell', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Notification bell', href='#notification-bell', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a list of notifications inside your application by providing more detailed information such as the user avatar, content and time of notification triggered by a notification bell icon.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='M12.133 10.632v-1.8A5.406 5.406 0 0 0 7.979 3.57.946.946 0 0 0 8 3.464V1.1a1 1 0 0 0-2 0v2.364a.946.946 0 0 0 .021.106 5.406 5.406 0 0 0-4.154 5.262v1.8C1.867 13.018 0 13.614 0 14.807 0 15.4 0 16 .538 16h12.924C14 16 14 15.4 14 14.807c0-1.193-1.867-1.789-1.867-4.175ZM3.823 17a3.453 3.453 0 0 0 6.354 0H3.823Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 14 20',
            cls='w-5 h-5'
        ),
        Div(cls='absolute block w-3 h-3 bg-red-500 border-2 border-white rounded-full -top-0.5 start-2.5 dark:border-gray-900'),
        id='dropdownNotificationButton',
        data_dropdown_toggle='dropdownNotification',
        type='button',
        cls='relative inline-flex items-center text-sm font-medium text-center text-gray-500 hover:text-gray-900 focus:outline-none dark:hover:text-white dark:text-gray-400'
    ),
    Div(
        Div('Notifications', cls='block px-4 py-2 font-medium text-center text-gray-700 rounded-t-lg bg-gray-50 dark:bg-gray-800 dark:text-white'),
        Div(
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z'),
                            Path(d='M4.439 9a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-primary-600 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        'New message from',
                        Span('Jese Leos', cls='font-semibold text-gray-900 dark:text-white'),
                        ': "Hey, what\'s up? All set for the presentation?"',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('a few moments ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Joseph image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-gray-900 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Joseph Mcfall', cls='font-semibold text-gray-900 dark:text-white'),
                        'and',
                        Span('5 others', cls='font-medium text-gray-900 dark:text-white'),
                        'started following you.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('10 minutes ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-red-600 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Bonnie Green', cls='font-semibold text-gray-900 dark:text-white'),
                        'and',
                        Span('141 others', cls='font-medium text-gray-900 dark:text-white'),
                        'love your story. See it and view more stories.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('44 minutes ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Leslie image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M18 0H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2v4a1 1 0 0 0 1.707.707L10.414 13H18a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5 4h2a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2ZM5 4h5a1 1 0 1 1 0 2H5a1 1 0 0 1 0-2Zm2 5H5a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Zm9 0h-6a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-green-400 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Leslie Livingston', cls='font-semibold text-gray-900 dark:text-white'),
                        'mentioned you in a comment:',
                        Span('@bonnie.green', href='#', cls='font-medium text-primary-500'),
                        'what do you say?',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('1 hour ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Robert image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M11 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm8.585 1.189a.994.994 0 0 0-.9-.138l-2.965.983a1 1 0 0 0-.685.949v8a1 1 0 0 0 .675.946l2.965 1.02a1.013 1.013 0 0 0 1.032-.242A1 1 0 0 0 20 12V2a1 1 0 0 0-.415-.811Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 14',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-purple-500 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Robert Brown', cls='font-semibold text-gray-900 dark:text-white'),
                        'posted a new video: Glassmorphism - learn how to implement the new design trend.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('3 hours ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            cls='divide-y divide-gray-100 dark:divide-gray-700'
        ),
        A(
            Div(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                ),
                'View all',
                cls='inline-flex items-center'
            ),
            href='#',
            cls='block py-2 text-sm font-medium text-center text-gray-900 rounded-b-lg bg-gray-50 hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-white'
        ),
        id='dropdownNotification',
        aria_labelledby='dropdownNotificationButton',
        cls='z-20 hidden w-full max-w-sm bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-800 dark:divide-gray-700'
    )
), code="""Div(
    Button(
        Svg(
            Path(d='M12.133 10.632v-1.8A5.406 5.406 0 0 0 7.979 3.57.946.946 0 0 0 8 3.464V1.1a1 1 0 0 0-2 0v2.364a.946.946 0 0 0 .021.106 5.406 5.406 0 0 0-4.154 5.262v1.8C1.867 13.018 0 13.614 0 14.807 0 15.4 0 16 .538 16h12.924C14 16 14 15.4 14 14.807c0-1.193-1.867-1.789-1.867-4.175ZM3.823 17a3.453 3.453 0 0 0 6.354 0H3.823Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 14 20',
            cls='w-5 h-5'
        ),
        Div(cls='absolute block w-3 h-3 bg-red-500 border-2 border-white rounded-full -top-0.5 start-2.5 dark:border-gray-900'),
        id='dropdownNotificationButton',
        data_dropdown_toggle='dropdownNotification',
        type='button',
        cls='relative inline-flex items-center text-sm font-medium text-center text-gray-500 hover:text-gray-900 focus:outline-none dark:hover:text-white dark:text-gray-400'
    ),
    Div(
        Div('Notifications', cls='block px-4 py-2 font-medium text-center text-gray-700 rounded-t-lg bg-gray-50 dark:bg-gray-800 dark:text-white'),
        Div(
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z'),
                            Path(d='M4.439 9a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-primary-600 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        'New message from',
                        Span('Jese Leos', cls='font-semibold text-gray-900 dark:text-white'),
                        ': "Hey, what\'s up? All set for the presentation?"',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('a few moments ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Joseph image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-gray-900 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Joseph Mcfall', cls='font-semibold text-gray-900 dark:text-white'),
                        'and',
                        Span('5 others', cls='font-medium text-gray-900 dark:text-white'),
                        'started following you.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('10 minutes ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-red-600 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Bonnie Green', cls='font-semibold text-gray-900 dark:text-white'),
                        'and',
                        Span('141 others', cls='font-medium text-gray-900 dark:text-white'),
                        'love your story. See it and view more stories.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('44 minutes ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Leslie image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M18 0H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2v4a1 1 0 0 0 1.707.707L10.414 13H18a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5 4h2a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2ZM5 4h5a1 1 0 1 1 0 2H5a1 1 0 0 1 0-2Zm2 5H5a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Zm9 0h-6a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-green-400 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Leslie Livingston', cls='font-semibold text-gray-900 dark:text-white'),
                        'mentioned you in a comment:',
                        Span('@bonnie.green', href='#', cls='font-medium text-primary-500'),
                        'what do you say?',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('1 hour ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            A(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Robert image', cls='rounded-full w-11 h-11'),
                    Div(
                        Svg(
                            Path(d='M11 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm8.585 1.189a.994.994 0 0 0-.9-.138l-2.965.983a1 1 0 0 0-.685.949v8a1 1 0 0 0 .675.946l2.965 1.02a1.013 1.013 0 0 0 1.032-.242A1 1 0 0 0 20 12V2a1 1 0 0 0-.415-.811Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 14',
                            cls='w-2 h-2 text-white'
                        ),
                        cls='absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-purple-500 border border-white rounded-full dark:border-gray-800'
                    ),
                    cls='shrink-0'
                ),
                Div(
                    Div(
                        Span('Robert Brown', cls='font-semibold text-gray-900 dark:text-white'),
                        'posted a new video: Glassmorphism - learn how to implement the new design trend.',
                        cls='text-gray-500 text-sm mb-1.5 dark:text-gray-400'
                    ),
                    Div('3 hours ago', cls='text-xs text-primary-600 dark:text-primary-500'),
                    cls='w-full ps-3'
                ),
                href='#',
                cls='flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700'
            ),
            cls='divide-y divide-gray-100 dark:divide-gray-700'
        ),
        A(
            Div(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='w-4 h-4 me-2 text-gray-500 dark:text-gray-400'
                ),
                'View all',
                cls='inline-flex items-center'
            ),
            href='#',
            cls='block py-2 text-sm font-medium text-center text-gray-900 rounded-b-lg bg-gray-50 hover:bg-gray-100 dark:bg-gray-800 dark:hover:bg-gray-700 dark:text-white'
        ),
        id='dropdownNotification',
        aria_labelledby='dropdownNotificationButton',
        cls='z-20 hidden w-full max-w-sm bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-800 dark:divide-gray-700'
    )
)""", id="example_16",cls='mt-2 mb-6'),
    H2(
        'User avatar',
        Span(id='user-avatar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User avatar', href='#user-avatar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a list of menu items and options when a user is logged into your application.'),
    component_showcase(Div(
    Button(
        Span('Open user menu', cls='sr-only'),
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
        id='dropdownUserAvatarButton',
        data_dropdown_toggle='dropdownAvatar',
        type='button',
        cls='flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
    ),
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
            aria_labelledby='dropdownUserAvatarButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownAvatar',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        Span('Open user menu', cls='sr-only'),
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 rounded-full'),
        id='dropdownUserAvatarButton',
        data_dropdown_toggle='dropdownAvatar',
        type='button',
        cls='flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600'
    ),
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
            aria_labelledby='dropdownUserAvatarButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownAvatar',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_17",cls='mt-2 mb-6'),
    H3(
        'Avatar with name',
        Span(id='avatar-with-name', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Avatar with name', href='#avatar-with-name', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to also show the name or email of the user next to the avatar for the dropdown menu.'),
    component_showcase(Div(
    Button(
        Span('Open user menu', cls='sr-only'),
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 me-2 rounded-full'),
        'Bonnie Green',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownAvatarNameButton',
        data_dropdown_toggle='dropdownAvatarName',
        type='button',
        cls='flex items-center text-sm pe-1 font-medium text-gray-900 rounded-full hover:text-primary-600 dark:hover:text-primary-500 md:me-0 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:text-white'
    ),
    Div(
        Div(
            Div('Pro User', cls='font-medium'),
            Div('name@flowbite.com', cls='truncate'),
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
            aria_labelledby='dropdownInformdropdownAvatarNameButtonationButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownAvatarName',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        Span('Open user menu', cls='sr-only'),
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='user photo', cls='w-8 h-8 me-2 rounded-full'),
        'Bonnie Green',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownAvatarNameButton',
        data_dropdown_toggle='dropdownAvatarName',
        type='button',
        cls='flex items-center text-sm pe-1 font-medium text-gray-900 rounded-full hover:text-primary-600 dark:hover:text-primary-500 md:me-0 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:text-white'
    ),
    Div(
        Div(
            Div('Pro User', cls='font-medium'),
            Div('name@flowbite.com', cls='truncate'),
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
            aria_labelledby='dropdownInformdropdownAvatarNameButtonationButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownAvatarName',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_18",cls='mt-2 mb-6'),
    H2(
        'Dropdown navbar',
        Span(id='dropdown-navbar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown navbar', href='#dropdown-navbar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
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
                cls='inline-flex items-center p-2 ms-3 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-white dark:bg-primary-600 md:dark:bg-transparent')
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
                                cls='w-2.5 h-2.5 ms-3'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-gray-400 dark:hover:text-white dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
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
                        A('Services', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:mt-0 md:text-sm md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700 md:space-x-8 md:rtl:space-x-reverse'
                ),
                id='navbar-dropdown',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto px-4 py-2.5'
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
                cls='inline-flex items-center p-2 ms-3 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        A('Home', href='#', aria_current='page', cls='block py-2 px-3 text-white bg-primary-700 rounded-sm md:bg-transparent md:text-primary-700 md:p-0 md:dark:text-white dark:bg-primary-600 md:dark:bg-transparent')
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
                                cls='w-2.5 h-2.5 ms-3'
                            ),
                            id='dropdownNavbarLink',
                            data_dropdown_toggle='dropdownNavbar',
                            cls='flex items-center justify-between w-full py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 md:w-auto dark:text-gray-400 dark:hover:text-white dark:focus:text-white dark:border-gray-700 dark:hover:bg-gray-700 md:dark:hover:bg-transparent'
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
                        A('Services', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Pricing', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    Li(
                        A('Contact', href='#', cls='block py-2 px-3 text-gray-700 rounded-sm hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-primary-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent')
                    ),
                    cls='flex flex-col font-medium p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:mt-0 md:text-sm md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700 md:space-x-8 md:rtl:space-x-reverse'
                ),
                id='navbar-dropdown',
                cls='hidden w-full md:block md:w-auto'
            ),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto px-4 py-2.5'
        ),
        cls='bg-white border-gray-200 dark:bg-gray-900 dark:border-gray-700'
    )
)""", id="example_19",cls='mt-2 mb-6'),
    H2(
        'Dropdown datepicker',
        Span(id='dropdown-datepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown datepicker', href='#dropdown-datepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to show a date range picker inside a dropdown menu. Use the',
        Code('data-dropdown-ignore-click-outside-class={class}'),
        'option to keep the dropdown menu open when interacting with the datepicker component by setting the element’s parent class name.'
    ),
    component_showcase(Div(
    Button(
        '31 Nov',
        P('- 31 Dev', cls='ms-1'),
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-3 h-3 ms-2'
        ),
        id='dateRangeButton',
        data_dropdown_toggle='dateRangeDropdown',
        data_dropdown_ignore_click_outside_class='datepicker',
        type='button',
        cls='inline-flex items-center text-primary-700 dark:text-primary-600 font-medium hover:underline'
    ),
    Div(
        Div(
            Div(
                Div(
                    Div(
                        Svg(
                            Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(name='start', type='text', placeholder='Start date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                ),
                Span('to', cls='mx-2 text-gray-500 dark:text-gray-400'),
                Div(
                    Div(
                        Svg(
                            Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(name='end', type='text', placeholder='End date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                ),
                date_rangepicker=True,
                datepicker_autohide=True,
                cls='flex items-center'
            ),
            aria_labelledby='dateRangeButton',
            cls='p-3'
        ),
        id='dateRangeDropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-80 lg:w-96 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        '31 Nov',
        P('- 31 Dev', cls='ms-1'),
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-3 h-3 ms-2'
        ),
        id='dateRangeButton',
        data_dropdown_toggle='dateRangeDropdown',
        data_dropdown_ignore_click_outside_class='datepicker',
        type='button',
        cls='inline-flex items-center text-primary-700 dark:text-primary-600 font-medium hover:underline'
    ),
    Div(
        Div(
            Div(
                Div(
                    Div(
                        Svg(
                            Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(name='start', type='text', placeholder='Start date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                ),
                Span('to', cls='mx-2 text-gray-500 dark:text-gray-400'),
                Div(
                    Div(
                        Svg(
                            Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                        ),
                        cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
                    ),
                    Input(name='end', type='text', placeholder='End date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                ),
                date_rangepicker=True,
                datepicker_autohide=True,
                cls='flex items-center'
            ),
            aria_labelledby='dateRangeButton',
            cls='p-3'
        ),
        id='dateRangeDropdown',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-80 lg:w-96 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_20",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The dropdown menus work with buttons of all sizes including smaller or larger ones.'),
    component_showcase(Div(
    Button(
        'Small dropdown',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2 h-2 ms-2'
        ),
        id='dropdownSmallButton',
        data_dropdown_toggle='dropdownSmall',
        type='button',
        cls='inline-flex items-center px-3 py-2 mb-3 me-3 text-sm font-medium text-center text-white bg-primary-700 rounded-lg md:mb-0 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownSmallButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownSmall',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    ),
    Button(
        'Large dropdown',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownLargeButton',
        data_dropdown_toggle='dropdownLarge',
        type='button',
        cls='inline-flex items-center px-5 py-3 mb-3 font-medium text-center text-white bg-primary-700 rounded-lg md:mb-0 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownLargeButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownLarge',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
), code="""Div(
    Button(
        'Small dropdown',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2 h-2 ms-2'
        ),
        id='dropdownSmallButton',
        data_dropdown_toggle='dropdownSmall',
        type='button',
        cls='inline-flex items-center px-3 py-2 mb-3 me-3 text-sm font-medium text-center text-white bg-primary-700 rounded-lg md:mb-0 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownSmallButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownSmall',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    ),
    Button(
        'Large dropdown',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownLargeButton',
        data_dropdown_toggle='dropdownLarge',
        type='button',
        cls='inline-flex items-center px-5 py-3 mb-3 font-medium text-center text-white bg-primary-700 rounded-lg md:mb-0 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
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
            aria_labelledby='dropdownLargeButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        Div(
            A('Sign out', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
            cls='py-2'
        ),
        id='dropdownLarge',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_21",cls='mt-2 mb-6'),
    H2(
        'Placement',
        Span(id='placement', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Placement', href='#placement', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also use the',
        Code('data-dropdown-placement={top|right|bottom|left}'),
        'data attribute options to choose the placement of the dropdown menu. By default the positioning is set to the bottom side of the button.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown top',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownTopButton',
        data_dropdown_toggle='dropdownTop',
        data_dropdown_placement='top',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownTopButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownTop',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown right',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRightButton',
        data_dropdown_toggle='dropdownRight',
        data_dropdown_placement='right',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownRightButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRight',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown bottom',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownBottomButton',
        data_dropdown_toggle='dropdownBottom',
        data_dropdown_placement='bottom',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownBottomButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownBottom',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 me-3'
        ),
        'Dropdown left',
        id='dropdownLeftButton',
        data_dropdown_toggle='dropdownLeft',
        data_dropdown_placement='left',
        type='button',
        cls='mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownLeftButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownLeft',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown top',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownTopButton',
        data_dropdown_toggle='dropdownTop',
        data_dropdown_placement='top',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownTopButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownTop',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown right',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownRightButton',
        data_dropdown_toggle='dropdownRight',
        data_dropdown_placement='right',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownRightButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRight',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown bottom',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownBottomButton',
        data_dropdown_toggle='dropdownBottom',
        data_dropdown_placement='bottom',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownBottomButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownBottom',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 me-3'
        ),
        'Dropdown left',
        id='dropdownLeftButton',
        data_dropdown_toggle='dropdownLeft',
        data_dropdown_placement='left',
        type='button',
        cls='mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownLeftButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownLeft',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_22",cls='mt-2 mb-6'),
    H3(
        'Double placement',
        Span(id='double-placement', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Double placement', href='#double-placement', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can combine the placement options by using the',
        Code('top|right|bottom|left-{start|end}'),
        'values. For example,',
        Code('left-end'),
        'will position the dropdown on the left bottom, whereas',
        Code('right-end'),
        'will position it on the right bottom side.'
    ),
    component_showcase(Div(
    Button(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 me-3 rtl:rotate-180'
        ),
        'Dropdown left end',
        id='dropdownLeftEndButton',
        data_dropdown_toggle='dropdownLeftEnd',
        data_dropdown_placement='left-end',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownLeftEndButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownLeftEnd',
        cls='z-20 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown right end',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
        ),
        id='dropdownRightEndButton',
        data_dropdown_toggle='dropdownRightEnd',
        data_dropdown_placement='right-end',
        type='button',
        cls='mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownRightEndButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRightEnd',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 me-3 rtl:rotate-180'
        ),
        'Dropdown left end',
        id='dropdownLeftEndButton',
        data_dropdown_toggle='dropdownLeftEnd',
        data_dropdown_placement='left-end',
        type='button',
        cls='me-3 mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownLeftEndButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownLeftEnd',
        cls='z-20 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    ),
    Button(
        'Dropdown right end',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
        ),
        id='dropdownRightEndButton',
        data_dropdown_toggle='dropdownRightEnd',
        data_dropdown_placement='right-end',
        type='button',
        cls='mb-3 md:mb-0 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownRightEndButton',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownRightEnd',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_23",cls='mt-2 mb-6'),
    H2(
        'Dropdown offset',
        Span(id='dropdown-offset', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown offset', href='#dropdown-offset', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the offset options on the dropdown component to set the distance and skidding of the menu relative to the trigger element.'),
    H3(
        'Distance',
        Span(id='distance', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Distance', href='#distance', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-dropdown-offset-distance={pixels}'),
        'data attribute to set the number of pixels you want the dropdown menu to be offset from the trigger element.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
        ),
        id='dropdownOffsetButton',
        data_dropdown_toggle='dropdownDistance',
        data_dropdown_offset_distance='35',
        data_dropdown_offset_skidding='0',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefault',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDistance',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 6 10',
            cls='w-2.5 h-2.5 ms-3 rtl:rotate-180'
        ),
        id='dropdownOffsetButton',
        data_dropdown_toggle='dropdownDistance',
        data_dropdown_offset_distance='35',
        data_dropdown_offset_skidding='0',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefault',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownDistance',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_24",cls='mt-2 mb-6'),
    H3(
        'Skidding',
        Span(id='skidding', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Skidding', href='#skidding', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Code('data-dropdown-offset-skidding={pixels}'),
        'data attribute can be used to move up or down (or left and right) the dropdown menu along and relative to the trigger element.'
    ),
    component_showcase(Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownOffsetButton',
        data_dropdown_toggle='dropdownSkidding',
        data_dropdown_offset_distance='10',
        data_dropdown_offset_skidding='100',
        data_dropdown_placement='right',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefault',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownSkidding',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
), code="""Div(
    Button(
        'Dropdown button',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownOffsetButton',
        data_dropdown_toggle='dropdownSkidding',
        data_dropdown_offset_distance='10',
        data_dropdown_offset_skidding='100',
        data_dropdown_placement='right',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            Li(
                A('Sign out', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
            ),
            aria_labelledby='dropdownDefault',
            cls='py-2 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownSkidding',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
    )
)""", id="example_25",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'For more dropdown examples you can check out the',
        A('dropdown filter', href='https://flowbite.com/blocks/application/filter/'),
        'components from Flowbite Blocks.'
    ),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Strong('Dropdown'),
        'class from Flowbite can be used to create an object that will show a dropdown menu relative to the main trigger element (eg. a button) based on the parameters, options, and methods that you provide.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Initialize a Dropdown object with the object parameters such as the main target dropdown menu, a trigger element (eg. a button) and options to set the placement relative to the trigger element.'),
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
                        Code('targetElement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Apply the main dropdown menu element as the first parameter of the Dropdown object.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('triggerElement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Apply the trigger element, such as a button, which is required to position the dropdown menu and set a click event.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Use the options parameter to set the positioning of the dropdown menu.', cls='px-6 py-4'),
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
    P('Use the following options as the third parameter for the Dropdown class to set the placement of the dropdown menu.'),
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
                        'Set the position of the dropdown menu relative to the trigger element choosing from',
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
                        'Set the event type that will trigger the dropdown menu choosing between',
                        Code('hover|click|none', cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('offsetDistance', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td('Set the amount of pixels the dropdown menu should be offset relative to the trigger element on the X horizontal axis.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('offsetSkidding', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td('Set the number of pixels the dropdown menu should be offset relative to the trigger element on the Y horizontal axis.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('delay', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Number', cls='px-6 py-4 font-medium'),
                    Td('Set the milliseconds for which the showing or hiding of the dropdown will be delayed for when using the hover trigger type.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('ignoreClickOutsideClass', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td('Set a class for one or more elements that when they are clicked should ignore closing the dropdown (ie. offcanvas datepicker).', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onHide', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the dropdown has been hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onShow', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the dropdown has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onToggle', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the dropdown visibility has been toggled.', cls='px-6 py-4'),
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
    P('Use the methods from the Dropdown object to programmatically show or hide the dropdown menu directly from JavaScript.'),
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
                    Td('Use this method on the Dropdown object to show the dropdown menu.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('hide()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Dropdown object to hide the dropdown menu.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('toggle()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Dropdown object to toggle the visibility of the dropdown menu.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('isVisible()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Returns true or false based on the visibility of the dropdown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnShow(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when the dropdown has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnHide(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when the dropdown has been hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnToggle(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when the dropdown visibility has been changed.', cls='px-6 py-4'),
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
    P('Check out the following JavaScript example to learn how to initialize, set the options, and use the methods for the Dropdown object.'),
    P('First of all, you need to set the main target element which will be the dropdown menu and the trigger element which will can be a button or a text.'),
    P('After that, you can also optionally set an options object to set the placement of the dropdown menu and callback functions.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the dropdown menu element', cls='c1'),
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
                        Span("'dropdownMenu'", cls='s1'),
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
                        Span('// set the element that trigger the dropdown menu on click', cls='c1'),
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
                        Span("'dropdownButton'", cls='s1'),
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
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offsetSkidding', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offsetDistance', cls='nx'),
                        Span(':', cls='o'),
                        Span('10', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('delay', cls='nx'),
                        Span(':', cls='o'),
                        Span('300', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('ignoreClickOutsideClass', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
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
                        Span("'dropdown has been hidden'", cls='s1'),
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
                        Span("'dropdown has been shown'", cls='s1'),
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
                        Span("'dropdown has been toggled'", cls='s1'),
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
                        Span("'dropdownMenu'", cls='s1'),
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
    P('Create a new Dropdown object based on the options above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Dropdown', cls='nx'),
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
                        Span('dropdown', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Dropdown', cls='nx'),
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
        'methods on the Dropdown object to programmatically show or hide the dropdown menu directly from JavaScript.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// show the dropdown menu', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dropdown', cls='nx'),
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
                        Span('// hide the dropdown menu', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dropdown', cls='nx'),
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
                        Span('// toggle the dropdown menu', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dropdown', cls='nx'),
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
                        Span('// check if dropdown is visible/open', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dropdown', cls='nx'),
                        Span('.', cls='p'),
                        Span('isVisible', cls='nx'),
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
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"dropdownButton"', cls='s'),
                        Span('data-dropdown-toggle', cls='na'),
                        Span('=', cls='o'),
                        Span('"dropdown"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"', cls='s'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('>', cls='p'),
                        'Dropdown button',
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-2.5 h-2.5 ms-3"', cls='s'),
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"none"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 10 6"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        Span('stroke', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('stroke-linecap', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        Span('stroke-linejoin', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        Span('stroke-width', cls='na'),
                        Span('=', cls='o'),
                        Span('"2"', cls='s'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"m1 1 4 4 4-4"', cls='s'),
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('svg', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
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
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Dropdown menu -->', cls='c'),
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
                        Span('"dropdownMenu"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700"', cls='s'),
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
                        Span('"py-2 text-sm text-gray-700 dark:text-gray-200"', cls='s'),
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"dropdownButton"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        Span('>', cls='p'),
                        'Dashboard',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
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
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        Span('>', cls='p'),
                        'Settings',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
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
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        Span('>', cls='p'),
                        'Earnings',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
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
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        Span('>', cls='p'),
                        'Sign out',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
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
        'from Flowbite then you can import the types for the Dropdown class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Dropdown', cls='nx'),
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
                        Span('DropdownOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('DropdownInterface', cls='nx'),
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
                        Span('// set the dropdown menu element', cls='c1'),
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
                        Span("'dropdownMenu'", cls='s1'),
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
                        Span('// set the element that trigger the dropdown menu on click', cls='c1'),
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
                        Span("'dropdownButton'", cls='s1'),
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
                        Span('DropdownOptions', cls='nx'),
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
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offsetSkidding', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('offsetDistance', cls='nx'),
                        Span(':', cls='o'),
                        Span('10', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('delay', cls='nx'),
                        Span(':', cls='o'),
                        Span('300', cls='mi'),
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
                        Span("'dropdown has been hidden'", cls='s1'),
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
                        Span("'dropdown has been shown'", cls='s1'),
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
                        Span("'dropdown has been toggled'", cls='s1'),
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
                        Span("'dropdownMenu'", cls='s1'),
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
                        Span('dropdown', cls='nx'),
                        Span(':', cls='o'),
                        Span('DropdownInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Dropdown', cls='nx'),
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
                        Span('// show the dropdown', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dropdown', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
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
