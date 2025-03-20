from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The alert component can be used to provide information to your users such as success or error messages, but also highlighted information complementing the normal flow of paragraphs and headers on a page.'),
    P('Flowbite also includes dismissible alerts which can be hidden by the users by clicking on the close icon.'),
    H2(
        'Default alert',
        Span(id='default-alert', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default alert', href='#default-alert', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples of alert components to show messages as feedback to your users.'),
    component_showcase(Div(
    Div(
        Span('Info alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Span('Danger alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Span('Success alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Span('Warning alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Span('Dark alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 text-sm text-gray-800 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300'
    )
), code="""Div(
    Div(
        Span('Info alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Span('Danger alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Span('Success alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Span('Warning alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 mb-4 text-sm text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Span('Dark alert!', cls='font-medium'),
        'Change a few things up and try submitting again.',
        role='alert',
        cls='p-4 text-sm text-gray-800 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Alerts with icon',
        Span(id='alerts-with-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Alerts with icon', href='#alerts-with-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can also include a descriptive icon to complement the message inside the alert component with the following example.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Info alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Danger alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Success alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Warning alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Dark alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 text-sm text-gray-800 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Info alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Danger alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Success alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Warning alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Dark alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 text-sm text-gray-800 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Bordered alerts',
        Span(id='bordered-alerts', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Bordered alerts', href='#bordered-alerts', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to add a border accent to the alert component instead of just a plain background.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Info alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-primary-800 border border-primary-300 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400 dark:border-primary-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Danger alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Success alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Warning alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-yellow-800 border border-yellow-300 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300 dark:border-yellow-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Dark alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 text-sm text-gray-800 border border-gray-300 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Info alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-primary-800 border border-primary-300 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400 dark:border-primary-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Danger alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Success alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Warning alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 mb-4 text-sm text-yellow-800 border border-yellow-300 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300 dark:border-yellow-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Dark alert!', cls='font-medium'),
            'Change a few things up and try submitting again.'
        ),
        role='alert',
        cls='flex items-center p-4 text-sm text-gray-800 border border-gray-300 rounded-lg bg-gray-50 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Alerts with list',
        Span(id='alerts-with-list', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Alerts with list', href='#alerts-with-list', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a list and a description inside an alert component.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3 mt-[2px]'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Ensure that these requirements are met:', cls='font-medium'),
            Ul(
                Li('At least 10 characters (and up to 100 characters)'),
                Li('At least one lowercase character'),
                Li('Inclusion of at least one special character, e.g., ! @ # ?'),
                cls='mt-1.5 list-disc list-inside'
            )
        ),
        role='alert',
        cls='flex p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3 mt-[2px]'
        ),
        Span('Danger', cls='sr-only'),
        Div(
            Span('Ensure that these requirements are met:', cls='font-medium'),
            Ul(
                Li('At least 10 characters (and up to 100 characters)'),
                Li('At least one lowercase character'),
                Li('Inclusion of at least one special character, e.g., ! @ # ?'),
                cls='mt-1.5 list-disc list-inside'
            )
        ),
        role='alert',
        cls='flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3 mt-[2px]'
        ),
        Span('Info', cls='sr-only'),
        Div(
            Span('Ensure that these requirements are met:', cls='font-medium'),
            Ul(
                Li('At least 10 characters (and up to 100 characters)'),
                Li('At least one lowercase character'),
                Li('Inclusion of at least one special character, e.g., ! @ # ?'),
                cls='mt-1.5 list-disc list-inside'
            )
        ),
        role='alert',
        cls='flex p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 inline w-4 h-4 me-3 mt-[2px]'
        ),
        Span('Danger', cls='sr-only'),
        Div(
            Span('Ensure that these requirements are met:', cls='font-medium'),
            Ul(
                Li('At least 10 characters (and up to 100 characters)'),
                Li('At least one lowercase character'),
                Li('Inclusion of at least one special character, e.g., ! @ # ?'),
                cls='mt-1.5 list-disc list-inside'
            )
        ),
        role='alert',
        cls='flex p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
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
        'Dismissing',
        Span(id='dismissing', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dismissing', href='#dismissing', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following alert elements that are also dismissible.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-1',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 text-primary-500 rounded-lg focus:ring-2 focus:ring-primary-400 p-1.5 hover:bg-primary-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-primary-400 dark:hover:bg-gray-700'
        ),
        id='alert-1',
        role='alert',
        cls='flex items-center p-4 mb-4 text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-2',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-red-50 text-red-500 rounded-lg focus:ring-2 focus:ring-red-400 p-1.5 hover:bg-red-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700'
        ),
        id='alert-2',
        role='alert',
        cls='flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-3',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700'
        ),
        id='alert-3',
        role='alert',
        cls='flex items-center p-4 mb-4 text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-4',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-yellow-50 text-yellow-500 rounded-lg focus:ring-2 focus:ring-yellow-400 p-1.5 hover:bg-yellow-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-yellow-300 dark:hover:bg-gray-700'
        ),
        id='alert-4',
        role='alert',
        cls='flex items-center p-4 mb-4 text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4 dark:text-gray-300'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple dark alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium text-gray-800 dark:text-gray-300'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-5',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-500 rounded-lg focus:ring-2 focus:ring-gray-400 p-1.5 hover:bg-gray-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        id='alert-5',
        role='alert',
        cls='flex items-center p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-1',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 text-primary-500 rounded-lg focus:ring-2 focus:ring-primary-400 p-1.5 hover:bg-primary-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-primary-400 dark:hover:bg-gray-700'
        ),
        id='alert-1',
        role='alert',
        cls='flex items-center p-4 mb-4 text-primary-800 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-2',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-red-50 text-red-500 rounded-lg focus:ring-2 focus:ring-red-400 p-1.5 hover:bg-red-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700'
        ),
        id='alert-2',
        role='alert',
        cls='flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-3',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700'
        ),
        id='alert-3',
        role='alert',
        cls='flex items-center p-4 mb-4 text-green-800 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Close', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-4',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-yellow-50 text-yellow-500 rounded-lg focus:ring-2 focus:ring-yellow-400 p-1.5 hover:bg-yellow-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-yellow-300 dark:hover:bg-gray-700'
        ),
        id='alert-4',
        role='alert',
        cls='flex items-center p-4 mb-4 text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4 dark:text-gray-300'
        ),
        Span('Info', cls='sr-only'),
        Div(
            'A simple dark alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium text-gray-800 dark:text-gray-300'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-5',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-500 rounded-lg focus:ring-2 focus:ring-gray-400 p-1.5 hover:bg-gray-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        id='alert-5',
        role='alert',
        cls='flex items-center p-4 rounded-lg bg-gray-50 dark:bg-gray-800'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Border accent',
        Span(id='border-accent', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Border accent', href='#border-accent', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to add a border accent on top of the alert component for further visual distinction.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-1',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 text-primary-500 rounded-lg focus:ring-2 focus:ring-primary-400 p-1.5 hover:bg-primary-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-primary-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-1',
        role='alert',
        cls='flex items-center p-4 mb-4 text-primary-800 border-t-4 border-primary-300 bg-primary-50 dark:text-primary-400 dark:bg-gray-800 dark:border-primary-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple danger alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-2',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-red-50 text-red-500 rounded-lg focus:ring-2 focus:ring-red-400 p-1.5 hover:bg-red-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-2',
        role='alert',
        cls='flex items-center p-4 mb-4 text-red-800 border-t-4 border-red-300 bg-red-50 dark:text-red-400 dark:bg-gray-800 dark:border-red-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple success alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-3',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-3',
        role='alert',
        cls='flex items-center p-4 mb-4 text-green-800 border-t-4 border-green-300 bg-green-50 dark:text-green-400 dark:bg-gray-800 dark:border-green-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple danger alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-4',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-yellow-50 text-yellow-500 rounded-lg focus:ring-2 focus:ring-yellow-400 p-1.5 hover:bg-yellow-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-yellow-300 dark:hover:bg-gray-700'
        ),
        id='alert-border-4',
        role='alert',
        cls='flex items-center p-4 mb-4 text-yellow-800 border-t-4 border-yellow-300 bg-yellow-50 dark:text-yellow-300 dark:bg-gray-800 dark:border-yellow-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4 dark:text-gray-300'
        ),
        Div(
            'A simple dark alert with an',
            A('example link', href='#', cls='font-semibold underline hover:text-gray-800 hover:no-underline dark:text-gray-300'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium text-gray-800 dark:text-gray-300'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-5',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-500 rounded-lg focus:ring-2 focus:ring-gray-400 p-1.5 hover:bg-gray-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        id='alert-border-5',
        role='alert',
        cls='flex items-center p-4 border-t-4 border-gray-300 bg-gray-50 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple info alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-1',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-primary-50 text-primary-500 rounded-lg focus:ring-2 focus:ring-primary-400 p-1.5 hover:bg-primary-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-primary-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-1',
        role='alert',
        cls='flex items-center p-4 mb-4 text-primary-800 border-t-4 border-primary-300 bg-primary-50 dark:text-primary-400 dark:bg-gray-800 dark:border-primary-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple danger alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-2',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-red-50 text-red-500 rounded-lg focus:ring-2 focus:ring-red-400 p-1.5 hover:bg-red-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-2',
        role='alert',
        cls='flex items-center p-4 mb-4 text-red-800 border-t-4 border-red-300 bg-red-50 dark:text-red-400 dark:bg-gray-800 dark:border-red-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple success alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-3',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-green-50 text-green-500 rounded-lg focus:ring-2 focus:ring-green-400 p-1.5 hover:bg-green-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-green-400 dark:hover:bg-gray-700'
        ),
        id='alert-border-3',
        role='alert',
        cls='flex items-center p-4 mb-4 text-green-800 border-t-4 border-green-300 bg-green-50 dark:text-green-400 dark:bg-gray-800 dark:border-green-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4'
        ),
        Div(
            'A simple danger alert with an',
            A('example link', href='#', cls='font-semibold underline hover:no-underline'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-4',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-yellow-50 text-yellow-500 rounded-lg focus:ring-2 focus:ring-yellow-400 p-1.5 hover:bg-yellow-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-yellow-300 dark:hover:bg-gray-700'
        ),
        id='alert-border-4',
        role='alert',
        cls='flex items-center p-4 mb-4 text-yellow-800 border-t-4 border-yellow-300 bg-yellow-50 dark:text-yellow-300 dark:bg-gray-800 dark:border-yellow-800'
    ),
    Div(
        Svg(
            Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 20 20',
            cls='shrink-0 w-4 h-4 dark:text-gray-300'
        ),
        Div(
            'A simple dark alert with an',
            A('example link', href='#', cls='font-semibold underline hover:text-gray-800 hover:no-underline dark:text-gray-300'),
            '. Give it a click if you like.',
            cls='ms-3 text-sm font-medium text-gray-800 dark:text-gray-300'
        ),
        Button(
            Span('Dismiss', cls='sr-only'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            type='button',
            data_dismiss_target='#alert-border-5',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-500 rounded-lg focus:ring-2 focus:ring-gray-400 p-1.5 hover:bg-gray-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        id='alert-border-5',
        role='alert',
        cls='flex items-center p-4 border-t-4 border-gray-300 bg-gray-50 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Additional content',
        Span(id='additional-content', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Additional content', href='#additional-content', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The following alert components can be used if you wish to disclose more information inside the element.'),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a info alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-primary-800 hover:bg-primary-900 focus:ring-4 focus:outline-none focus:ring-primary-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-1', aria_label='Close', cls='text-primary-800 bg-transparent border border-primary-800 hover:bg-primary-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-primary-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-primary-600 dark:border-primary-600 dark:text-primary-400 dark:hover:text-white dark:focus:ring-primary-800'),
            cls='flex'
        ),
        id='alert-additional-content-1',
        role='alert',
        cls='p-4 mb-4 text-primary-800 border border-primary-300 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400 dark:border-primary-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a danger alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info danger goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-red-800 hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-2', aria_label='Close', cls='text-red-800 bg-transparent border border-red-800 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-red-600 dark:border-red-600 dark:text-red-500 dark:hover:text-white dark:focus:ring-red-800'),
            cls='flex'
        ),
        id='alert-additional-content-2',
        role='alert',
        cls='p-4 mb-4 text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a success alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info success goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-green-800 hover:bg-green-900 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-3', aria_label='Close', cls='text-green-800 bg-transparent border border-green-800 hover:bg-green-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-green-600 dark:border-green-600 dark:text-green-400 dark:hover:text-white dark:focus:ring-green-800'),
            cls='flex'
        ),
        id='alert-additional-content-3',
        role='alert',
        cls='p-4 mb-4 text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a warning alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info warning goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-yellow-800 hover:bg-yellow-900 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-yellow-300 dark:text-gray-800 dark:hover:bg-yellow-400 dark:focus:ring-yellow-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-4', aria_label='Close', cls='text-yellow-800 bg-transparent border border-yellow-800 hover:bg-yellow-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-yellow-300 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-gray-800 dark:focus:ring-yellow-800'),
            cls='flex'
        ),
        id='alert-additional-content-4',
        role='alert',
        cls='p-4 mb-4 text-yellow-800 border border-yellow-300 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300 dark:border-yellow-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2 dark:text-gray-300'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a dark alert', cls='text-lg font-medium text-gray-800 dark:text-gray-300'),
            cls='flex items-center'
        ),
        Div('More info about this info dark goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm text-gray-800 dark:text-gray-300'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3 dark:text-gray-300'
                ),
                'View more',
                type='button',
                cls='text-white bg-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-5', aria_label='Close', cls='text-gray-800 bg-transparent border border-gray-700 hover:bg-gray-800 hover:text-white focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-gray-600 dark:hover:bg-gray-600 dark:focus:ring-gray-800 dark:text-gray-300 dark:hover:text-white'),
            cls='flex'
        ),
        id='alert-additional-content-5',
        role='alert',
        cls='p-4 border border-gray-300 rounded-lg bg-gray-50 dark:border-gray-600 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a info alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info alert goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-primary-800 hover:bg-primary-900 focus:ring-4 focus:outline-none focus:ring-primary-200 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-1', aria_label='Close', cls='text-primary-800 bg-transparent border border-primary-800 hover:bg-primary-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-primary-200 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-primary-600 dark:border-primary-600 dark:text-primary-400 dark:hover:text-white dark:focus:ring-primary-800'),
            cls='flex'
        ),
        id='alert-additional-content-1',
        role='alert',
        cls='p-4 mb-4 text-primary-800 border border-primary-300 rounded-lg bg-primary-50 dark:bg-gray-800 dark:text-primary-400 dark:border-primary-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a danger alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info danger goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-red-800 hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-2', aria_label='Close', cls='text-red-800 bg-transparent border border-red-800 hover:bg-red-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-red-600 dark:border-red-600 dark:text-red-500 dark:hover:text-white dark:focus:ring-red-800'),
            cls='flex'
        ),
        id='alert-additional-content-2',
        role='alert',
        cls='p-4 mb-4 text-red-800 border border-red-300 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 dark:border-red-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a success alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info success goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-green-800 hover:bg-green-900 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-3', aria_label='Close', cls='text-green-800 bg-transparent border border-green-800 hover:bg-green-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-green-600 dark:border-green-600 dark:text-green-400 dark:hover:text-white dark:focus:ring-green-800'),
            cls='flex'
        ),
        id='alert-additional-content-3',
        role='alert',
        cls='p-4 mb-4 text-green-800 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:text-green-400 dark:border-green-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a warning alert', cls='text-lg font-medium'),
            cls='flex items-center'
        ),
        Div('More info about this info warning goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3'
                ),
                'View more',
                type='button',
                cls='text-white bg-yellow-800 hover:bg-yellow-900 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-yellow-300 dark:text-gray-800 dark:hover:bg-yellow-400 dark:focus:ring-yellow-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-4', aria_label='Close', cls='text-yellow-800 bg-transparent border border-yellow-800 hover:bg-yellow-900 hover:text-white focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:hover:bg-yellow-300 dark:border-yellow-300 dark:text-yellow-300 dark:hover:text-gray-800 dark:focus:ring-yellow-800'),
            cls='flex'
        ),
        id='alert-additional-content-4',
        role='alert',
        cls='p-4 mb-4 text-yellow-800 border border-yellow-300 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300 dark:border-yellow-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='shrink-0 w-4 h-4 me-2 dark:text-gray-300'
            ),
            Span('Info', cls='sr-only'),
            H3('This is a dark alert', cls='text-lg font-medium text-gray-800 dark:text-gray-300'),
            cls='flex items-center'
        ),
        Div('More info about this info dark goes here. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.', cls='mt-2 mb-4 text-sm text-gray-800 dark:text-gray-300'),
        Div(
            Button(
                Svg(
                    Path(d='M10 0C4.612 0 0 5.336 0 7c0 1.742 3.546 7 10 7 6.454 0 10-5.258 10-7 0-1.664-4.612-7-10-7Zm0 10a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='me-2 h-3 w-3 dark:text-gray-300'
                ),
                'View more',
                type='button',
                cls='text-white bg-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xs px-3 py-1.5 me-2 text-center inline-flex items-center dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-800'
            ),
            Button('Dismiss', type='button', data_dismiss_target='#alert-additional-content-5', aria_label='Close', cls='text-gray-800 bg-transparent border border-gray-700 hover:bg-gray-800 hover:text-white focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-xs px-3 py-1.5 text-center dark:border-gray-600 dark:hover:bg-gray-600 dark:focus:ring-gray-800 dark:text-gray-300 dark:hover:text-white'),
            cls='flex'
        ),
        id='alert-additional-content-5',
        role='alert',
        cls='p-4 border border-gray-300 rounded-lg bg-gray-50 dark:border-gray-600 dark:bg-gray-800'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Strong('Dismiss'),
        'class from Flowbite can be used to create an object that will hide a target element or elements based on the parameters, options, and methods that you provide.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The parameters for the Dismiss object can be used to programmatically initialize and manipulate the behaviour of the dismissal of the target element.'),
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
                cls='bg-gray-50 dark:bg-gray-800'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass the element object that will be dismissed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('triggerEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass the element object that will trigger the targetEl dismission on click.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass the options object to set the trigger element, transition, duration, timing classes of the dismiss animation and callback functions.', cls='px-6 py-4'),
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
    P('Use these optional options for the Dismiss object to set the transition, duration, and timing function types based on the utility classes from Tailwind CSS.'),
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
                        Code('transition', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td(
                        'Use one of the Transition Property utility classes from Tailwind CSS to set transition type for the main element. The default value is',
                        Code('transition-opacity', cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('duration', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Integer', cls='px-6 py-4 font-medium'),
                    Td(
                        'Set the duration of the dismissing animation. The default value is',
                        Code('300', cls='text-purple-600 dark:text-purple-400'),
                        '(300 milliseconds).',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('timing', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4 font-medium'),
                    Td(
                        'Set the transition timing function utility class from Tailwind CSS. The default value is',
                        Code('ease-out', cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onHide', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the item has been dismissed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-4000'
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
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('hide()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method on the Dismiss object to hide the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnHide(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set the callback function when the item has been dismissed.', cls='px-6 py-4'),
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
    P('Check out the following JavaScript example to learn how to initialize, set the options, and use the methods for the Dismiss object.'),
    P('First of all, you should set the required target element and optionally set a trigger element which will dismiss the target element when clicked and other options to customize the animation.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// target element that will be dismissed', cls='c1'),
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
                        Span("'targetElement'", cls='s1'),
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
                        Span('// optional trigger element', cls='c1'),
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
                        Span("'triggerElement'", cls='s1'),
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
                        Span('// options object', cls='c1'),
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
                        Span('transition', cls='nx'),
                        Span(':', cls='o'),
                        Span("'transition-opacity'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('duration', cls='nx'),
                        Span(':', cls='o'),
                        Span('1000', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('timing', cls='nx'),
                        Span(':', cls='o'),
                        Span("'ease-out'", cls='s1'),
                        Span(',', cls='p'),
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
                        Span('// callback functions', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onHide', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('context', cls='nx'),
                        Span(',', cls='p'),
                        Span('targetEl', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'element has been dismissed'", cls='s1'),
                        Span(')', cls='p'),
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
                        Span('targetEl', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'targetElement'", cls='s1'),
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
    P('Create a new Dismiss object based on the options set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Dismiss', cls='nx'),
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
                        Span('* $targetEl (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $triggerEl (optional)', cls='cm'),
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
                        Span('dismiss', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Dismiss', cls='nx'),
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
    P('You can now use the methods on the Dismiss object.'),
    Div(
        Pre(
            Code(
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
                        Span('dismiss', cls='nx'),
                        Span('.', cls='p'),
                        Span('hide', cls='nx'),
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
    P('Use this HTML code for the JavaScript code example above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"triggerElement"', cls='s'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800"', cls='s'),
                        Span('>', cls='p'),
                        'Hide alert',
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
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"targetElement"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"p-4 mb-4 text-sm text-primary-800 rounded-lg bg-primary-50 dark:bg-primary-200 dark:text-primary-800"', cls='s'),
                        Span('role', cls='na'),
                        Span('=', cls='o'),
                        Span('"alert"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"font-medium"', cls='s'),
                        Span('>', cls='p'),
                        'Info alert!',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        'Change a few things up and try submitting again.',
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
        'from Flowbite then you can import the types for the Dismiss class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Dismiss', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span('"flowbite"', cls='s2'),
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
                        Span('DismissOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('DismissInterface', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span('"flowbite"', cls='s2'),
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
                        Span('// target element that will be dismissed', cls='c1'),
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
                        Span("'targetElement'", cls='s1'),
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
                        Span('// optional trigger element', cls='c1'),
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
                        Span("'triggerElement'", cls='s1'),
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
                        Span('// options object', cls='c1'),
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
                        Span('DismissOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('transition', cls='nx'),
                        Span(':', cls='o'),
                        Span("'transition-opacity'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('duration', cls='nx'),
                        Span(':', cls='o'),
                        Span('1000', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('timing', cls='nx'),
                        Span(':', cls='o'),
                        Span("'ease-out'", cls='s1'),
                        Span(',', cls='p'),
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
                        Span('// callback functions', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onHide', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('context', cls='nx'),
                        Span(',', cls='p'),
                        Span('targetEl', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'element has been dismissed'", cls='s1'),
                        Span(')', cls='p'),
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
                        Span('targetEl', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'targetElement'", cls='s1'),
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
                        Span('* $targetEl (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $triggerEl (optional)', cls='cm'),
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
                        Span('dismiss', cls='nx'),
                        Span(':', cls='o'),
                        Span('DismissInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Dismiss', cls='nx'),
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
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// programmatically hide it', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('dismiss', cls='nx'),
                        Span('.', cls='p'),
                        Span('hide', cls='nx'),
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
