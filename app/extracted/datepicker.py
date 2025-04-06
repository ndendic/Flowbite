from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P(
        'The Tailwind CSS datepicker component developed by Flowbite is built with vanilla JavaScript and using the utility-first classes from Tailwind. The datepicker features both inline and a date range picker functionality and some extra options such as autohide, custom format, positioning, and more. Check out the',
        A('timepicker component', href='https://flowbite.com/docs/forms/timepicker/'),
        'to select time alongside dates.'
    ),
    H2(
        'Getting started',
        Span(id='getting-started', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Getting started', href='#getting-started', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you want to use the datepicker component from Flowbite you have to include the Flowbite JavaScript file either via NPM or CDN. For versions before',
        Code('2.4.0'),
        'please continue using the dedicated CDN and component.'
    ),
    P(
        'Follow the',
        A('quickstart guide', href='https://flowbite.com/docs/getting-started/quickstart/'),
        'and then include the following JavaScript file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('script', cls='nt'),
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"../path/to/flowbite/dist/flowbite.min.js"', cls='s'),
                        Span('></', cls='p'),
                        Span('script', cls='nt'),
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
    P('Alternatively you can also use CDN to include the datepicker JavaScript.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('script', cls='nt'),
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"', cls='s'),
                        Span('></', cls='p'),
                        Span('script', cls='nt'),
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
    P('Also make sure that you add the source files for Tailwind in your main CSS file:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('@', cls='p'),
                        Span('import', cls='k'),
                        Span('"tailwindcss"', cls='s2'),
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
                        Span('@', cls='p'),
                        Span('source', cls='k'),
                        Span('"../node_modules/flowbite-datepicker"', cls='s2'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='css',
                cls='language-css'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'If you’d like to manually be able to manipulate the datepicker component using JavaScript then you should',
        A('install the component using NPM', href='#javascript'),
        'and include it into your JavaScript code.'
    ),
    H2(
        'Datepicker example',
        Span(id='datepicker-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Datepicker example', href='#datepicker-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the following example of an input element to create a datepicker component. All you need to do is to add the',
        Code('datepicker'),
        'data attribute to any',
        Code('input'),
        'element.'
    ),
    component_showcase(Div(
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
            cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
        ),
        Input(datepicker=True, id='default-datepicker', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
            cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
        ),
        Input(datepicker=True, id='default-datepicker', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Inline datepicker',
        Span(id='inline-datepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Inline datepicker', href='#inline-datepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('inline-datepicker'),
        'and',
        Code('data-date'),
        'data attributes to initialize and set the default date for an inline datepicker inside a block element such as a',
        Code('div'),
        '.'
    ),
    component_showcase(Div(
    Div(id='datepicker-inline', inline_datepicker=True, data_date='02/25/2024')
), code="""Div(
    Div(id='datepicker-inline', inline_datepicker=True, data_date='02/25/2024')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Date range picker',
        Span(id='date-range-picker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Date range picker', href='#date-range-picker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('date-rangepicker'),
        'data attribute and the following markup to initialize two datepickers as a range.'
    ),
    component_showcase(Div(
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
            Input(id='datepicker-range-start', name='start', type='text', placeholder='Select date start', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        Span('to', cls='mx-4 text-gray-500'),
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
            Input(id='datepicker-range-end', name='end', type='text', placeholder='Select date end', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        id='date-range-picker',
        date_rangepicker=True,
        cls='flex items-center'
    )
), code="""Div(
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
            Input(id='datepicker-range-start', name='start', type='text', placeholder='Select date start', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        Span('to', cls='mx-4 text-gray-500'),
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
            Input(id='datepicker-range-end', name='end', type='text', placeholder='Select date end', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        id='date-range-picker',
        date_rangepicker=True,
        cls='flex items-center'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Learn more about the options that you can use with the Tailwind datepicker to enable features such as autohide, action buttons, date format, orientation, and more based on the vanilla JavaScript from Flowbite.'),
    H3(
        'Autohide',
        Span(id='autohide', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Autohide', href='#autohide', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('datepicker-autohide'),
        'data attribute to make the datepicker disappear right after selecting a date.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-autohide', datepicker=True, datepicker_autohide=True, type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-autohide', datepicker=True, datepicker_autohide=True, type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H3(
        'Action buttons',
        Span(id='action-buttons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Action buttons', href='#action-buttons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'By adding the',
        Code('datepicker-buttons'),
        'data attribute you will enable the',
        Code('today'),
        'and',
        Code('clear'),
        'buttons:'
    ),
    Ul(
        Li(
            'clicking on the',
            Code('today'),
            'button will browse back to the current day/month/year'
        ),
        Li(
            'clicking on the',
            Code('clear'),
            'button will reset all selections'
        )
    ),
    P(
        'If you want the button to additionally select today’s date, add',
        Code('datepicker-autoselect-today'),
        'data attribute.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-actions', datepicker=True, datepicker_buttons=True, datepicker_autoselect_today=True, type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-actions', datepicker=True, datepicker_buttons=True, datepicker_autoselect_today=True, type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H3(
        'Date format',
        Span(id='date-format', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Date format', href='#date-format', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you want to use a custom format such as',
        Code('mm-dd-yyyy'),
        'then you can use the',
        Code('datepicker-format="{format}"'),
        'data attribute to change it.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-format', datepicker=True, datepicker_format='mm-dd-yyyy', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-format', datepicker=True, datepicker_format='mm-dd-yyyy', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H3(
        'Max and min dates',
        Span(id='max-and-min-dates', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Max and min dates', href='#max-and-min-dates', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('datepicker-min-date={format}'),
        'and',
        Code('datepicker-max-date={format}'),
        'to set the minimum and maximum dates that can be selected inside the datepicker.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-format', datepicker=True, datepicker_min_date='06/04/2024', datepicker_max_date='05/05/2025', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-format', datepicker=True, datepicker_min_date='06/04/2024', datepicker_max_date='05/05/2025', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H3(
        'Orientation',
        Span(id='orientation', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Orientation', href='#orientation', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can override the default positioning algorithm by using the',
        Code('datepicker-orientation="{top|right|bottom|left}"'),
        'data attributes. You can even combine right with bottom or left with top.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-orientation', datepicker=True, datepicker_orientation='bottom right', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-orientation', datepicker=True, datepicker_orientation='bottom right', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Title',
        Span(id='title', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Title', href='#title', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also add a title to the datepicker by using the',
        Code('datepicker-title="{title}"'),
        'data attribute.'
    ),
    component_showcase(Div(
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
        Input(id='datepicker-title', datepicker=True, datepicker_title='Flowbite datepicker', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
), code="""Div(
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
        Input(id='datepicker-title', datepicker=True, datepicker_title='Flowbite datepicker', type='text', placeholder='Select date', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='relative max-w-sm'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H3(
        'Custom colors',
        Span(id='custom-colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Custom colors', href='#custom-colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can set the',
        Code('primary'),
        'color class which is by default set to primary to add your own colors.'
    ),
    H3(
        'Language (i18n)',
        Span(id='language-i18n', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Language (i18n)', href='#language-i18n', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('We are working on the API to provide language support for the datepicker.'),
    P(
        'Until then, please refer to this',
        A('solution from GitHub', href='https://github.com/themesberg/flowbite/issues/32#issuecomment-1420422922'),
        '.'
    ),
    H2(
        'Timepicker',
        Span(id='timepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timepicker', href='#timepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the native browser timepicker input field to select a time alongside the datepicker. Check out more examples on the',
        A('timepicker', href='https://flowbite.com/docs/forms/timepicker/'),
        'component page from Flowbite.'
    ),
    component_showcase(Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none'
            ),
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        cls='max-w-[8rem] mx-auto'
    )
), code="""Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none'
            ),
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        cls='max-w-[8rem] mx-auto'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Dark mode',
        Span(id='dark-mode', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dark mode', href='#dark-mode', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you would like to enable dark mode for the datepicker please follow the',
        A('dark mode', href='https://flowbite.com/docs/customize/dark-mode/'),
        'guide on Flowbite and enable it either manually or by using a dark mode switcher.'
    ),
    H2(
        'JavaScript Behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript Behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('Tailwind CSS Datepicker'),
        'component from Flowbite to select a date or range of dates based on the Datepicker API and configure the component using the methods and options that you can pass when creating the object using JavaScript.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the object parameters from the Datepicker component to set the datepicker parent input element and the options associated with it when creating a new instance.'),
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
                        Code('datepickerEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass the main HTML element that will be rendered for the datepicker. It can be an input element or a `div` for inline rendering.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Use the options parameter to set custom datepicker options such as the default date, minimum and maximum values, action buttons and callback functions.', cls='px-6 py-4'),
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
        Span(id='options-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use these optional options for the Datepicker object to set options such as the date format, orientation, max and min dates, custom buttons, callback functions and more.'),
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
                        Code('rangePicker', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Boolean', cls='px-6 py-4'),
                    Td("If set to true then the datepicker will be converted to a date range picker. By default it's false.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('format', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td("Use this option to set a custom format for the datepicker. By default it's `mm/dd/yyyy`.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('maxDate', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Use this option to set the maximum selectable date of the datepicker component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('minDate', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Use this option to set the minimum selectable date of the datepicker component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('orientation', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td("Set the orientation of the datepicker component when it's not inline. It can be top, bottom, left, or right.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('buttons', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Boolean', cls='px-6 py-4'),
                    Td('If set to true then the "today" and "clear" action buttons will be shown that lets you select today\'s date or clear selections.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('autoSelectToday', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Integer', cls='px-6 py-4'),
                    Td("If set to 1 then it will automatically have today's date preselected.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('title', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td("Set a custom title for the datepicker component. By default it's null.", cls='px-6 py-4'),
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
    P('Use the following methods of the Datepicker object to programmatically manipulate the behaviour.'),
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
                        Code('getDate()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to get the currenctly select date from the datepicker.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('setDate()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set the date value of the datepicker component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('show()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this function to programatically show the datepicker component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('hide()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this function to programatically hide the datepicker component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('getDatepickerInstance()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to get the parent datepicker instance with the extended collection of methods and options.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnShow(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function whenever the datepicker component has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnHide(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function whenever the datepicker component has been hidden.', cls='px-6 py-4'),
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
    P('Check out the following examples to learn how to use a basic HTML markup together with the Flowbite Datepicker API JS.'),
    P('First of all, you need to select the datepicker element (it can be an input field or div for inline datepickers) and set up the options object.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the target element of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$datepickerEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'datepicker-custom'", cls='s1'),
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
                        Span('defaultDatepickerId', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('autohide', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('format', cls='nx'),
                        Span(':', cls='o'),
                        Span("'mm/dd/yyyy'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('maxDate', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('minDate', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('orientation', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bottom'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('buttons', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('autoSelectToday', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('title', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('rangePicker', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
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
                        Span('{},', cls='p'),
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
                        Span('{},', cls='p'),
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
                        Span("'datepicker-custom-example'", cls='s1'),
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
    P('Next step is to create a new instance of a Datepicker object using the parameters we have set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Datepicker', cls='nx'),
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
                        Span('* $datepickerEl: required', cls='cm'),
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
                        Span('datepicker', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Datepicker', cls='nx'),
                        Span('(', cls='p'),
                        Span('$datepickerEl', cls='nx'),
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
    P('Use the following methods to show and hide the datepicker, set or get the currently selected date and get access to the instance.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// get the currently selected date (undefined if not selected)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('getDate', cls='nx'),
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
                        Span('// set the date (or dates if date range picker)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('setDate', cls='nx'),
                        Span('(', cls='p'),
                        Span("'05/31/2024'", cls='s1'),
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
                        Span('// programatically show the datepicker', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
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
                        Span('// programatically hide the datepicker', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
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
                        Span('// use this method to get the parent datepicker instance from https://mymth.github.io/vanillajs-datepicker/#/', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('getDatepickerInstance', cls='nx'),
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
    P('Here is an example of the HTML markup that you can use for the JavaScript example above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"relative max-w-sm"', cls='s'),
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
                        Span('"absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-4 h-4 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 20 20"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"', cls='s'),
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
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('input', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"datepicker-custom"', cls='s'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"text"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"', cls='s'),
                        Span('placeholder', cls='na'),
                        Span('=', cls='o'),
                        Span('"Select date"', cls='s'),
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
        'from Flowbite then you can import the types for the Datepicker object, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Datepicker', cls='nx'),
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
                        Span('DatepickerOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('DatepickerInterface', cls='nx'),
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
                        Span('// set the target element of the input field or div', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$datepickerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLInputElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'datepicker-custom'", cls='s1'),
                        Span(')', cls='p'),
                        Span('as', cls='nx'),
                        Span('HTMLInputElement', cls='nx'),
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
                        Span('DatepickerOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('defaultDatepickerId', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('autohide', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('format', cls='nx'),
                        Span(':', cls='o'),
                        Span("'mm/dd/yyyy'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('maxDate', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('minDate', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('orientation', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bottom'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('buttons', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('autoSelectToday', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('title', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('rangePicker', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
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
                        Span('{},', cls='p'),
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
                        Span('{},', cls='p'),
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
                        Span("'datepicker-custom-example'", cls='s1'),
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
                        Span('* $datepickerEl: required', cls='cm'),
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
                        Span('datepicker', cls='nx'),
                        Span(':', cls='o'),
                        Span('DatepickerInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Datepicker', cls='nx'),
                        Span('(', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$datepickerEl', cls='nx'),
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
                        Span('// get the currently selected date (undefined if not selected)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('getDate', cls='nx'),
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
                        Span('// set the date (or dates if date range picker)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('setDate', cls='nx'),
                        Span('(', cls='p'),
                        Span("'05/31/2024'", cls='s1'),
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
                        Span('// programatically show the datepicker', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
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
                        Span('// programatically hide the datepicker', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
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
                        Span('// use this method to get the parent datepicker instance from https://mymth.github.io/vanillajs-datepicker/#/', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('datepicker', cls='nx'),
                        Span('.', cls='p'),
                        Span('getDatepickerInstance', cls='nx'),
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
        'Parent library',
        Span(id='parent-library', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Parent library', href='#parent-library', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you want to directly use the main Datepicker component instance you can either install it via NPM and import it or use the',
        Code('getDatepickerInstance()'),
        'method using our Instance Manager to call all of the extra options and methods from the',
        A('parent plugin library', href='https://github.com/themesberg/flowbite-datepicker'),
        ':'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span('npm install flowbite-datepicker --save', cls='cl'),
                    cls='line'
                ),
                data_lang='bash',
                cls='language-bash'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'After you’ve installed the NPM library, you will need to import the',
        Code('Datepicker'),
        'module:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('Datepicker', cls='nx'),
                        Span('from', cls='nx'),
                        Span("'flowbite-datepicker'", cls='s1'),
                        Span(';', cls='p'),
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
        'Initialize a new element using the',
        Code('Datepicker'),
        'constructor and optionally add your own options based on your needs:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('datepickerEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'datepickerId'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('new', cls='k'),
                        Span('Datepicker', cls='nx'),
                        Span('(', cls='p'),
                        Span('datepickerEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// options', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('});', cls='p'),
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
        'If you want to use the',
        Strong('Tailwind Date Range Picker'),
        'you have to import the',
        Code('DateRangePicker'),
        'module:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('DateRangePicker', cls='nx'),
                        Span('from', cls='nx'),
                        Span("'flowbite-datepicker'", cls='s1'),
                        Span(';', cls='p'),
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
        'Then in the same fashion you can initialize a date range picker component by using the',
        Code('DateRangePicker'),
        'constructor:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('dateRangePickerEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'dateRangePickerId'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('new', cls='k'),
                        Span('DateRangePicker', cls='nx'),
                        Span('(', cls='p'),
                        Span('dateRangePickerEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// options', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('});', cls='p'),
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
        'React support',
        Span(id='react-support', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: React support', href='#react-support', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'One of our community members built the React version of the Flowbite Datepicker and you can learn more about it on',
        A('this repository on GitHub', href='https://github.com/OMikkel/tailwind-datepicker-react', rel='nofollow'),
        '.'
    ),
    H3(
        'Turbo load support',
        Span(id='turbo-load-support', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Turbo load support', href='#turbo-load-support', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'In order to support turbo load from Ruby on Rails 7, you have to include the',
        Code('flowbite.turbo.js'),
        'file either from NPM or CDN into your project.'
    ),
    P(
        'Follow the',
        A('quickstart guide', href='https://flowbite.com/docs/getting-started/rails/'),
        'and then include the following JavaScript file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        'pin',
                        Span('"flowbite"', cls='s2'),
                        ', to:',
                        Span('"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.turbo.min.js"', cls='s2'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='bash',
                cls='language-bash'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'Don’t forget to also import it inside your',
        Code('application.js'),
        'file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('"flowbite/dist/flowbite.turbo.js"', cls='s2'),
                        Span(';', cls='p'),
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
