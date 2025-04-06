from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('The radio component can be used to allow the user to choose a single option from one or more available options coded with the utility classes from Tailwind CSS and available in multiple styles, variants, and colors and support dark mode.'),
    P('Make sure that you have included Flowbite as a plugin inside your Tailwind CSS project to apply all the necessary styles for the radio component.'),
    H2(
        'Radio example',
        Span(id='radio-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Radio example', href='#radio-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the default example of a radio component with the checked and unchecked state.'),
    component_showcase(Div(
    Div(
        Input(id='default-radio-1', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Default radio', fr='default-radio-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center mb-4'
    ),
    Div(
        Input(checked=True, id='default-radio-2', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Checked state', fr='default-radio-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Input(id='default-radio-1', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Default radio', fr='default-radio-1', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center mb-4'
    ),
    Div(
        Input(checked=True, id='default-radio-2', type='radio', value=True, name='default-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Checked state', fr='default-radio-2', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Disabled state',
        Span(id='disabled-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disabled state', href='#disabled-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('disabled'),
        'attribute to the radio component to disallow the selection for the user.'
    ),
    component_showcase(Div(
    Div(
        Input(disabled=True, id='disabled-radio-1', type='radio', value=True, name='disabled-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Disabled radio', fr='disabled-radio-1', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='flex items-center mb-4'
    ),
    Div(
        Input(disabled=True, checked=True, id='disabled-radio-2', type='radio', value=True, name='disabled-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Disabled checked', fr='disabled-radio-2', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Input(disabled=True, id='disabled-radio-1', type='radio', value=True, name='disabled-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Disabled radio', fr='disabled-radio-1', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='flex items-center mb-4'
    ),
    Div(
        Input(disabled=True, checked=True, id='disabled-radio-2', type='radio', value=True, name='disabled-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Disabled checked', fr='disabled-radio-2', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
        cls='flex items-center'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Radio link',
        Span(id='radio-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Radio link', href='#radio-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example if you want to include an anchor tag inside the label of the radio component.'),
    component_showcase(Div(
    Div(
        Input(id='link-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label(
            'Radio button with a',
            A('link inside', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
            '.',
            fr='link-radio',
            cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'
        ),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Input(id='link-radio', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label(
            'Radio button with a',
            A('link inside', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
            '.',
            fr='link-radio',
            cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'
        ),
        cls='flex items-center'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Helper text',
        Span(id='helper-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Helper text', href='#helper-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example if you want to add a secondary text to the label for the radio component.'),
    component_showcase(Div(
    Div(
        Div(
            Input(id='helper-radio', aria_describedby='helper-radio-text', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            cls='flex items-center h-5'
        ),
        Div(
            Label('Free shipping via Flowbite', fr='helper-radio', cls='font-medium text-gray-900 dark:text-gray-300'),
            P('For orders shipped from $25 in books or $29 in other categories', id='helper-radio-text', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
            cls='ms-2 text-sm'
        ),
        cls='flex'
    )
), code="""Div(
    Div(
        Div(
            Input(id='helper-radio', aria_describedby='helper-radio-text', type='radio', value=True, cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            cls='flex items-center h-5'
        ),
        Div(
            Label('Free shipping via Flowbite', fr='helper-radio', cls='font-medium text-gray-900 dark:text-gray-300'),
            P('For orders shipped from $25 in books or $29 in other categories', id='helper-radio-text', cls='text-xs font-normal text-gray-500 dark:text-gray-300'),
            cls='ms-2 text-sm'
        ),
        cls='flex'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Bordered',
        Span(id='bordered', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Bordered', href='#bordered', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a radio input elements inside a card with border.'),
    component_showcase(Div(
    Div(
        Input(id='bordered-radio-1', type='radio', value=True, name='bordered-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Default radio', fr='bordered-radio-1', cls='w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700'
    ),
    Div(
        Input(checked=True, id='bordered-radio-2', type='radio', value=True, name='bordered-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Checked state', fr='bordered-radio-2', cls='w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700'
    )
), code="""Div(
    Div(
        Input(id='bordered-radio-1', type='radio', value=True, name='bordered-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Default radio', fr='bordered-radio-1', cls='w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700'
    ),
    Div(
        Input(checked=True, id='bordered-radio-2', type='radio', value=True, name='bordered-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
        Label('Checked state', fr='bordered-radio-2', cls='w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
        cls='flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Radio list group',
        Span(id='radio-list-group', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Radio list group', href='#radio-list-group', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a list of radio buttons inside a grouped list.'),
    component_showcase(Div(
    H3('Identification', cls='mb-4 font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Div(
                Input(id='list-radio-license', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('Driver License', fr='list-radio-license', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-id', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('State ID', fr='list-radio-id', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-military', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Military', fr='list-radio-military', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-passport', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Passport', fr='list-radio-passport', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    H3('Identification', cls='mb-4 font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Div(
                Input(id='list-radio-license', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('Driver License', fr='list-radio-license', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-id', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('State ID', fr='list-radio-id', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-military', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Military', fr='list-radio-military', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='list-radio-passport', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Passport', fr='list-radio-passport', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 rounded-t-lg dark:border-gray-600'
        ),
        cls='w-48 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Horizontal list group',
        Span(id='horizontal-list-group', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Horizontal list group', href='#horizontal-list-group', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to group up radio button components inside a list.'),
    component_showcase(Div(
    H3('Identification', cls='mb-4 font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Div(
                Input(id='horizontal-list-radio-license', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('Driver License', fr='horizontal-list-radio-license', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-id', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('State ID', fr='horizontal-list-radio-id', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-military', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Military', fr='horizontal-list-radio-military', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-passport', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Passport', fr='horizontal-list-radio-passport', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full dark:border-gray-600'
        ),
        cls='items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
), code="""Div(
    H3('Identification', cls='mb-4 font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Div(
                Input(id='horizontal-list-radio-license', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('Driver License', fr='horizontal-list-radio-license', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-id', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('State ID', fr='horizontal-list-radio-id', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-military', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Military', fr='horizontal-list-radio-military', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600'
        ),
        Li(
            Div(
                Input(id='horizontal-list-radio-passport', type='radio', value=True, name='list-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500'),
                Label('US Passport', fr='horizontal-list-radio-passport', cls='w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                cls='flex items-center ps-3'
            ),
            cls='w-full dark:border-gray-600'
        ),
        cls='items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white'
    )
)""", id="example_6",cls='mt-2 mb-6'),
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
        'Radio in dropdown',
        Span(id='radio-in-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Radio in dropdown', href='#radio-in-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Here’s an example of a list group that you can use right away.'),
    component_showcase(Div(
    Button(
        'Dropdown radio',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-2.5'
        ),
        id='dropdownHelperRadioButton',
        data_dropdown_toggle='dropdownHelperRadio',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            aria_labelledby='dropdownHelperRadioButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHelperRadio',
        data_popper_reference_hidden=True,
        data_popper_escaped=True,
        data_popper_placement='top',
        style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 6119.5px, 0px);',
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
            cls='w-2.5 h-2.5 ms-2.5'
        ),
        id='dropdownHelperRadioButton',
        data_dropdown_toggle='dropdownHelperRadio',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
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
            aria_labelledby='dropdownHelperRadioButton',
            cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
        ),
        id='dropdownHelperRadio',
        data_popper_reference_hidden=True,
        data_popper_escaped=True,
        data_popper_placement='top',
        style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 6119.5px, 0px);',
        cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-60 dark:bg-gray-700 dark:divide-gray-600'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Inline layout',
        Span(id='inline-layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Inline layout', href='#inline-layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('flex'),
        'class for a wrapper element to horizontally align the radio elements.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Input(id='inline-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline 1', fr='inline-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='inline-2-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline 2', fr='inline-2-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(checked=True, id='inline-checked-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline checked', fr='inline-checked-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(disabled=True, id='inline-disabled-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline disabled', fr='inline-disabled-radio', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
            cls='flex items-center'
        ),
        cls='flex'
    )
), code="""Div(
    Div(
        Div(
            Input(id='inline-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline 1', fr='inline-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='inline-2-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline 2', fr='inline-2-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(checked=True, id='inline-checked-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline checked', fr='inline-checked-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(disabled=True, id='inline-disabled-radio', type='radio', value=True, name='inline-radio-group', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Inline disabled', fr='inline-disabled-radio', cls='ms-2 text-sm font-medium text-gray-400 dark:text-gray-500'),
            cls='flex items-center'
        ),
        cls='flex'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Advanced layout',
        Span(id='advanced-layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Advanced layout', href='#advanced-layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a more advanced radio component to add more information and update the style of the whole card instead of just the circled dot.'),
    component_showcase(Div(
    H3('How much do you expect to use each month?', cls='mb-5 text-lg font-medium text-gray-900 dark:text-white'),
    Ul(
        Li(
            Input(type='radio', id='hosting-small', name='hosting', value='hosting-small', required=True, cls='hidden peer'),
            Label(
                Div(
                    Div('0-50 MB', cls='w-full text-lg font-semibold'),
                    Div('Good for small websites', cls='w-full'),
                    cls='block'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-5 h-5 ms-3 rtl:rotate-180'
                ),
                fr='hosting-small',
                cls='inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700'
            )
        ),
        Li(
            Input(type='radio', id='hosting-big', name='hosting', value='hosting-big', cls='hidden peer'),
            Label(
                Div(
                    Div('500-1000 MB', cls='w-full text-lg font-semibold'),
                    Div('Good for large websites', cls='w-full'),
                    cls='block'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-5 h-5 ms-3 rtl:rotate-180'
                ),
                fr='hosting-big',
                cls='inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700'
            )
        ),
        cls='grid w-full gap-6 md:grid-cols-2'
    )
), code="""Div(
    H3('How much do you expect to use each month?', cls='mb-5 text-lg font-medium text-gray-900 dark:text-white'),
    Ul(
        Li(
            Input(type='radio', id='hosting-small', name='hosting', value='hosting-small', required=True, cls='hidden peer'),
            Label(
                Div(
                    Div('0-50 MB', cls='w-full text-lg font-semibold'),
                    Div('Good for small websites', cls='w-full'),
                    cls='block'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-5 h-5 ms-3 rtl:rotate-180'
                ),
                fr='hosting-small',
                cls='inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700'
            )
        ),
        Li(
            Input(type='radio', id='hosting-big', name='hosting', value='hosting-big', cls='hidden peer'),
            Label(
                Div(
                    Div('500-1000 MB', cls='w-full text-lg font-semibold'),
                    Div('Good for large websites', cls='w-full'),
                    cls='block'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-5 h-5 ms-3 rtl:rotate-180'
                ),
                fr='hosting-big',
                cls='inline-flex items-center justify-between w-full p-5 text-gray-500 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-700 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-600 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700'
            )
        ),
        cls='grid w-full gap-6 md:grid-cols-2'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Colors',
        Span(id='colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Colors', href='#colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('text-{color}-{shade}'),
        'utility class from Tailwind CSS to change the color of the radio component.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Input(id='red-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-red-600 bg-gray-100 border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Red', fr='red-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='green-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-green-600 bg-gray-100 border-gray-300 focus:ring-green-500 dark:focus:ring-green-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Green', fr='green-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(checked=True, id='purple-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 focus:ring-purple-500 dark:focus:ring-purple-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Purple', fr='purple-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='teal-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-teal-600 bg-gray-100 border-gray-300 focus:ring-teal-500 dark:focus:ring-teal-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Teal', fr='teal-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='yellow-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-yellow-400 bg-gray-100 border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Yellow', fr='yellow-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='orange-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-orange-500 bg-gray-100 border-gray-300 focus:ring-orange-500 dark:focus:ring-orange-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Orange', fr='orange-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        cls='flex flex-wrap'
    )
), code="""Div(
    Div(
        Div(
            Input(id='red-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-red-600 bg-gray-100 border-gray-300 focus:ring-red-500 dark:focus:ring-red-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Red', fr='red-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='green-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-green-600 bg-gray-100 border-gray-300 focus:ring-green-500 dark:focus:ring-green-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Green', fr='green-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(checked=True, id='purple-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 focus:ring-purple-500 dark:focus:ring-purple-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Purple', fr='purple-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='teal-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-teal-600 bg-gray-100 border-gray-300 focus:ring-teal-500 dark:focus:ring-teal-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Teal', fr='teal-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='yellow-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-yellow-400 bg-gray-100 border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Yellow', fr='yellow-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        Div(
            Input(id='orange-radio', type='radio', value=True, name='colored-radio', cls='w-4 h-4 text-orange-500 bg-gray-100 border-gray-300 focus:ring-orange-500 dark:focus:ring-orange-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
            Label('Orange', fr='orange-radio', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
            cls='flex items-center me-4'
        ),
        cls='flex flex-wrap'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    id='mainContent'
)
