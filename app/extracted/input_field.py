from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The input field is an important part of the form element that can be used to create interactive controls to accept data from the user based on multiple input types, such as text, email, number, password, URL, phone number, and more.'),
    P('On this page you will find all of the input types based on multiple variants, styles, colors, and sizes built with the utility classes from Tailwind CSS and components from Flowbite.'),
    H2(
        'Input fields',
        Span(id='input-fields', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Input fields', href='#input-fields', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example as a generic form element which includes multiple input fields types such as text, email, password, number, URL, and phone number and use the grid layout to add multiple columns and rows.'),
    component_showcase(Div(
    Form(
        Div(
            Div(
                Label('First name', fr='first_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='first_name', placeholder='John', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Last name', fr='last_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='last_name', placeholder='Doe', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Company', fr='company', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='company', placeholder='Flowbite', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Phone number', fr='phone', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='tel', id='phone', placeholder='123-45-678', pattern='[0-9]{3}-[0-9]{2}-[0-9]{3}', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Website URL', fr='website', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='url', id='website', placeholder='flowbite.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Unique visitors (per month)', fr='visitors', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='number', id='visitors', placeholder=True, required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='grid gap-6 mb-6 md:grid-cols-2'
        ),
        Div(
            Label('Email address', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='email', id='email', placeholder='john.doe@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Confirm password', fr='confirm_password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', id='confirm_password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Div(
                Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'),
                cls='flex items-center h-5'
            ),
            Label(
                'I agree with the',
                A('terms and conditions', href='#', cls='text-primary-600 hover:underline dark:text-primary-500'),
                '.',
                fr='remember',
                cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'
            ),
            cls='flex items-start mb-6'
        ),
        Button('Submit', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800')
    )
), code="""Div(
    Form(
        Div(
            Div(
                Label('First name', fr='first_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='first_name', placeholder='John', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Last name', fr='last_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='last_name', placeholder='Doe', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Company', fr='company', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', id='company', placeholder='Flowbite', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Phone number', fr='phone', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='tel', id='phone', placeholder='123-45-678', pattern='[0-9]{3}-[0-9]{2}-[0-9]{3}', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Website URL', fr='website', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='url', id='website', placeholder='flowbite.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Unique visitors (per month)', fr='visitors', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='number', id='visitors', placeholder=True, required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='grid gap-6 mb-6 md:grid-cols-2'
        ),
        Div(
            Label('Email address', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='email', id='email', placeholder='john.doe@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Label('Confirm password', fr='confirm_password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', id='confirm_password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='mb-6'
        ),
        Div(
            Div(
                Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'),
                cls='flex items-center h-5'
            ),
            Label(
                'I agree with the',
                A('terms and conditions', href='#', cls='text-primary-600 hover:underline dark:text-primary-500'),
                '.',
                fr='remember',
                cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'
            ),
            cls='flex items-start mb-6'
        ),
        Button('Submit', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800')
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Input sizes',
        Span(id='input-sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Input sizes', href='#input-sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples to apply a small, default or large size for the input fields.'),
    component_showcase(Div(
    Div(
        Label('Large input', fr='large-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='large-input', cls='block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='mb-6'
    ),
    Div(
        Label('Default input', fr='default-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='default-input', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='mb-6'
    ),
    Div(
        Label('Small input', fr='small-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='small-input', cls='block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
    )
), code="""Div(
    Div(
        Label('Large input', fr='large-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='large-input', cls='block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='mb-6'
    ),
    Div(
        Label('Default input', fr='default-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='default-input', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='mb-6'
    ),
    Div(
        Label('Small input', fr='small-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id='small-input', cls='block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Disabled state',
        Span(id='disabled-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disabled state', href='#disabled-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example if you want to apply the disabled state to an input field.'),
    component_showcase(Div(
    Input(type='text', id='disabled-input', aria_label='disabled input', value='Disabled input', disabled=True, cls='mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
    Input(type='text', id='disabled-input-2', aria_label='disabled input 2', value='Disabled readonly input', disabled=True, readonly=True, cls='bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500')
), code="""Div(
    Input(type='text', id='disabled-input', aria_label='disabled input', value='Disabled input', disabled=True, cls='mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
    Input(type='text', id='disabled-input-2', aria_label='disabled input 2', value='Disabled readonly input', disabled=True, readonly=True, cls='bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Validation',
        Span(id='validation', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Validation', href='#validation', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example to apply validation styles for success and error messages.'),
    component_showcase(Div(
    Div(
        Label('Your name', fr='success', cls='block mb-2 text-sm font-medium text-green-700 dark:text-green-500'),
        Input(type='text', id='success', placeholder='Success input', cls='bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500'),
        P(
            Span('Well done!', cls='font-medium'),
            'Some success message.',
            cls='mt-2 text-sm text-green-600 dark:text-green-500'
        ),
        cls='mb-6'
    ),
    Div(
        Label('Your name', fr='error', cls='block mb-2 text-sm font-medium text-red-700 dark:text-red-500'),
        Input(type='text', id='error', placeholder='Error input', cls='bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'),
        P(
            Span('Oh, snapp!', cls='font-medium'),
            'Some error message.',
            cls='mt-2 text-sm text-red-600 dark:text-red-500'
        )
    )
), code="""Div(
    Div(
        Label('Your name', fr='success', cls='block mb-2 text-sm font-medium text-green-700 dark:text-green-500'),
        Input(type='text', id='success', placeholder='Success input', cls='bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500'),
        P(
            Span('Well done!', cls='font-medium'),
            'Some success message.',
            cls='mt-2 text-sm text-green-600 dark:text-green-500'
        ),
        cls='mb-6'
    ),
    Div(
        Label('Your name', fr='error', cls='block mb-2 text-sm font-medium text-red-700 dark:text-red-500'),
        Input(type='text', id='error', placeholder='Error input', cls='bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'),
        P(
            Span('Oh, snapp!', cls='font-medium'),
            'Some error message.',
            cls='mt-2 text-sm text-red-600 dark:text-red-500'
        )
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Input group',
        Span(id='input-group', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Input group', href='#input-group', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add a descriptive icon or additional text inside the input field.'),
    component_showcase(Div(
    Label('Your Email', fr='input-group-1', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Div(
        Div(
            Svg(
                Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
                Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 16',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
        ),
        Input(type='text', id='input-group-1', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative mb-6'
    ),
    Label('Username', fr='website-admin', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Div(
        Span(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            cls='inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600'
        ),
        Input(type='text', id='website-admin', placeholder='elonmusk', cls='rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-primary-500 focus:border-primary-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='flex'
    )
), code="""Div(
    Label('Your Email', fr='input-group-1', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Div(
        Div(
            Svg(
                Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
                Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 16',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
        ),
        Input(type='text', id='input-group-1', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative mb-6'
    ),
    Label('Username', fr='website-admin', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Div(
        Span(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            cls='inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600'
        ),
        Input(type='text', id='website-admin', placeholder='elonmusk', cls='rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-primary-500 focus:border-primary-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='flex'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Helper text',
        Span(id='helper-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Helper text', href='#helper-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a helper text below the input field for additional explanation and links.'),
    component_showcase(Div(
    Label('Your email', fr='helper-text', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(type='email', id='helper-text', aria_describedby='helper-text-explanation', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
    P(
        'Weâ\x80\x99ll never share your details. Read our',
        A('Privacy Policy', href='#', cls='font-medium text-primary-600 hover:underline dark:text-primary-500'),
        '.',
        id='helper-text-explanation',
        cls='mt-2 text-sm text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    Label('Your email', fr='helper-text', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(type='email', id='helper-text', aria_describedby='helper-text-explanation', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
    P(
        'Weâ\x80\x99ll never share your details. Read our',
        A('Privacy Policy', href='#', cls='font-medium text-primary-600 hover:underline dark:text-primary-500'),
        '.',
        id='helper-text-explanation',
        cls='mt-2 text-sm text-gray-500 dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Search input',
        Span(id='search-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Search input', href='#search-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example where the submit button is positioned inside the input field.'),
    component_showcase(Div(
    Form(
        Label('Search', fr='search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
            Input(type='search', id='search', placeholder='Search', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button('Search', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
            cls='relative'
        )
    )
), code="""Div(
    Form(
        Label('Search', fr='search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
            Input(type='search', id='search', placeholder='Search', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button('Search', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
            cls='relative'
        )
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
        'Dropdown input',
        Span(id='dropdown-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropdown input', href='#dropdown-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a dropdown menu right next to the input field.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Your Email', fr='search-dropdown', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                'All categories',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button',
                data_dropdown_toggle='dropdown',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800'
            ),
            Div(
                Ul(
                    Li(
                        A('Shopping', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Images', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('News', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Finance', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='search-dropdown', placeholder='Search', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    type='submit',
                    cls='absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        )
    )
), code="""Div(
    Form(
        Div(
            Label('Your Email', fr='search-dropdown', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                'All categories',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button',
                data_dropdown_toggle='dropdown',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800'
            ),
            Div(
                Ul(
                    Li(
                        A('Shopping', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Images', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('News', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        A('Finance', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='search-dropdown', placeholder='Search', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    type='submit',
                    cls='absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        )
    )
)""", id="example_7",cls='mt-2 mb-6'),
    id='mainContent'
)
