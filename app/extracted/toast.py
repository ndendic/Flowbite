from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P(
        'The toast component can be used to enhance your website’s interactivity by pushing notifications to your visitors. You can choose from multiple styles, colors, sizes, and positions and even dismiss the component by using the',
        Code('data-dismiss-target'),
        'data attribute from Fastbite.'
    ),
    H2(
        'Default toast',
        Span(id='default-toast', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default toast', href='#default-toast', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this simple toast component with an icon, message, and dismissible close button to show alert messages to your website visitors. Make sure that you set the correct id for the',
        Code('data-dismiss-target'),
        'data attribute to enable the dismissible feature.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M15.147 15.085a7.159 7.159 0 0 1-6.189 3.307A6.713 6.713 0 0 1 3.1 15.444c-2.679-4.513.287-8.737.888-9.548A4.373 4.373 0 0 0 5 1.608c1.287.953 6.445 3.218 5.537 10.5 1.5-1.122 2.706-3.01 2.853-6.14 1.433 1.049 3.993 5.395 1.757 9.117Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 18 20',
                cls='w-4 h-4'
            ),
            Span('Fire icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-primary-500 bg-primary-100 rounded-lg dark:bg-primary-800 dark:text-primary-200'
        ),
        Div('Set yourself free.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-default',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-default',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M15.147 15.085a7.159 7.159 0 0 1-6.189 3.307A6.713 6.713 0 0 1 3.1 15.444c-2.679-4.513.287-8.737.888-9.548A4.373 4.373 0 0 0 5 1.608c1.287.953 6.445 3.218 5.537 10.5 1.5-1.122 2.706-3.01 2.853-6.14 1.433 1.049 3.993 5.395 1.757 9.117Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 18 20',
                cls='w-4 h-4'
            ),
            Span('Fire icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-primary-500 bg-primary-100 rounded-lg dark:bg-primary-800 dark:text-primary-200'
        ),
        Div('Set yourself free.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-default',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-default',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Colors',
        Span(id='colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Colors', href='#colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use these contextual toast components to show success, danger, or warning alert messages to your users.'),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Check icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200'
        ),
        Div('Item moved successfully.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-success',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-success',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Error icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200'
        ),
        Div('Item has been deleted.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-danger',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-danger',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM10 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-4a1 1 0 0 1-2 0V6a1 1 0 0 1 2 0v5Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Warning icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-orange-500 bg-orange-100 rounded-lg dark:bg-orange-700 dark:text-orange-200'
        ),
        Div('Improve password difficulty.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-warning',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-warning',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Check icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200'
        ),
        Div('Item moved successfully.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-success',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-success',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Error icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200'
        ),
        Div('Item has been deleted.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-danger',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-danger',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    ),
    Div(
        Div(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM10 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-4a1 1 0 0 1-2 0V6a1 1 0 0 1 2 0v5Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-5 h-5'
            ),
            Span('Warning icon', cls='sr-only'),
            cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-orange-500 bg-orange-100 rounded-lg dark:bg-orange-700 dark:text-orange-200'
        ),
        Div('Improve password difficulty.', cls='ms-3 text-sm font-normal'),
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
            data_dismiss_target='#toast-warning',
            aria_label='Close',
            cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
        ),
        id='toast-warning',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Simple toast',
        Span(id='simple-toast', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Simple toast', href='#simple-toast', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to show simple messages and notifications without the use of a close button.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m9 17 8 2L9 1 1 19l8-2Zm0 0V9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 18 20',
            cls='w-5 h-5 text-primary-600 dark:text-primary-500 rotate-45'
        ),
        Div('Message sent successfully.', cls='ps-4 text-sm font-normal'),
        id='toast-simple',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 space-x-4 rtl:space-x-reverse text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m9 17 8 2L9 1 1 19l8-2Zm0 0V9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 18 20',
            cls='w-5 h-5 text-primary-600 dark:text-primary-500 rotate-45'
        ),
        Div('Message sent successfully.', cls='ps-4 text-sm font-normal'),
        id='toast-simple',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 space-x-4 rtl:space-x-reverse text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Undo button',
        Span(id='undo-button', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Undo button', href='#undo-button', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this toast component to also show an “undo” button to reverse the action of the user.'),
    component_showcase(Div(
    Div(
        Div('Conversation archived.', cls='text-sm font-normal'),
        Div(
            A('Undo', href='#', cls='text-sm font-medium text-primary-600 p-1.5 hover:bg-primary-100 rounded-lg dark:text-primary-500 dark:hover:bg-gray-700'),
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
                data_dismiss_target='#toast-undo',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex items-center ms-auto space-x-2 rtl:space-x-reverse'
        ),
        id='toast-undo',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Div('Conversation archived.', cls='text-sm font-normal'),
        Div(
            A('Undo', href='#', cls='text-sm font-medium text-primary-600 p-1.5 hover:bg-primary-100 rounded-lg dark:text-primary-500 dark:hover:bg-gray-700'),
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
                data_dismiss_target='#toast-undo',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex items-center ms-auto space-x-2 rtl:space-x-reverse'
        ),
        id='toast-undo',
        role='alert',
        cls='flex items-center w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:text-gray-400 dark:bg-gray-800'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Toast message',
        Span(id='toast-message', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Toast message', href='#toast-message', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to show messages and a CTA button when receiving chat messages, comment notifications, and other use cases.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='w-8 h-8 rounded-full'),
            Div(
                Span('Jese Leos', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
                Div('Hi Neil, thanks for sharing your thoughts regarding Fastbite.', cls='mb-2 text-sm font-normal'),
                A('Reply', href='#', cls='inline-flex px-2.5 py-1.5 text-xs font-medium text-center text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-500 dark:hover:bg-primary-600 dark:focus:ring-primary-800'),
                cls='ms-3 text-sm font-normal'
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
                data_dismiss_target='#toast-message-cta',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 justify-center items-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex'
        ),
        id='toast-message-cta',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-400'
    )
), code="""Div(
    Div(
        Div(
            Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese Leos image', cls='w-8 h-8 rounded-full'),
            Div(
                Span('Jese Leos', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
                Div('Hi Neil, thanks for sharing your thoughts regarding Fastbite.', cls='mb-2 text-sm font-normal'),
                A('Reply', href='#', cls='inline-flex px-2.5 py-1.5 text-xs font-medium text-center text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-500 dark:hover:bg-primary-600 dark:focus:ring-primary-800'),
                cls='ms-3 text-sm font-normal'
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
                data_dismiss_target='#toast-message-cta',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 justify-center items-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex'
        ),
        id='toast-message-cta',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-400'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Push notification',
        Span(id='push-notification', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Push notification', href='#push-notification', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to show notifications for an action from another user such as posting a comment, receiving a like, being tagged. You can show an avatar, icon, message, and the time of the notification.'),
    component_showcase(Div(
    Div(
        Div(
            Span('New notification', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
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
                data_dismiss_target='#toast-notification',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 justify-center items-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex items-center mb-3'
        ),
        Div(
            Div(
                Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese Leos image', cls='w-12 h-12 rounded-full'),
                Span(
                    Svg(
                        Path(d='M18 4H16V9C16 10.0609 15.5786 11.0783 14.8284 11.8284C14.0783 12.5786 13.0609 13 12 13H9L6.846 14.615C7.17993 14.8628 7.58418 14.9977 8 15H11.667L15.4 17.8C15.5731 17.9298 15.7836 18 16 18C16.2652 18 16.5196 17.8946 16.7071 17.7071C16.8946 17.5196 17 17.2652 17 17V15H18C18.5304 15 19.0391 14.7893 19.4142 14.4142C19.7893 14.0391 20 13.5304 20 13V6C20 5.46957 19.7893 4.96086 19.4142 4.58579C19.0391 4.21071 18.5304 4 18 4Z', fill='currentColor'),
                        Path(d='M12 0H2C1.46957 0 0.960859 0.210714 0.585786 0.585786C0.210714 0.960859 0 1.46957 0 2V9C0 9.53043 0.210714 10.0391 0.585786 10.4142C0.960859 10.7893 1.46957 11 2 11H3V13C3 13.1857 3.05171 13.3678 3.14935 13.5257C3.24698 13.6837 3.38668 13.8114 3.55279 13.8944C3.71889 13.9775 3.90484 14.0126 4.08981 13.996C4.27477 13.9793 4.45143 13.9114 4.6 13.8L8.333 11H12C12.5304 11 13.0391 10.7893 13.4142 10.4142C13.7893 10.0391 14 9.53043 14 9V2C14 1.46957 13.7893 0.960859 13.4142 0.585786C13.0391 0.210714 12.5304 0 12 0Z', fill='currentColor'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 20 18',
                        fill='currentColor',
                        cls='w-3 h-3 text-white'
                    ),
                    Span('Message icon', cls='sr-only'),
                    cls='absolute bottom-0 right-0 inline-flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full'
                ),
                cls='relative inline-block shrink-0'
            ),
            Div(
                Div('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Div('commented on your photo', cls='text-sm font-normal'),
                Span('a few seconds ago', cls='text-xs font-medium text-primary-600 dark:text-primary-500'),
                cls='ms-3 text-sm font-normal'
            ),
            cls='flex items-center'
        ),
        id='toast-notification',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-900 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-300'
    )
), code="""Div(
    Div(
        Div(
            Span('New notification', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
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
                data_dismiss_target='#toast-notification',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 justify-center items-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex items-center mb-3'
        ),
        Div(
            Div(
                Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese Leos image', cls='w-12 h-12 rounded-full'),
                Span(
                    Svg(
                        Path(d='M18 4H16V9C16 10.0609 15.5786 11.0783 14.8284 11.8284C14.0783 12.5786 13.0609 13 12 13H9L6.846 14.615C7.17993 14.8628 7.58418 14.9977 8 15H11.667L15.4 17.8C15.5731 17.9298 15.7836 18 16 18C16.2652 18 16.5196 17.8946 16.7071 17.7071C16.8946 17.5196 17 17.2652 17 17V15H18C18.5304 15 19.0391 14.7893 19.4142 14.4142C19.7893 14.0391 20 13.5304 20 13V6C20 5.46957 19.7893 4.96086 19.4142 4.58579C19.0391 4.21071 18.5304 4 18 4Z', fill='currentColor'),
                        Path(d='M12 0H2C1.46957 0 0.960859 0.210714 0.585786 0.585786C0.210714 0.960859 0 1.46957 0 2V9C0 9.53043 0.210714 10.0391 0.585786 10.4142C0.960859 10.7893 1.46957 11 2 11H3V13C3 13.1857 3.05171 13.3678 3.14935 13.5257C3.24698 13.6837 3.38668 13.8114 3.55279 13.8944C3.71889 13.9775 3.90484 14.0126 4.08981 13.996C4.27477 13.9793 4.45143 13.9114 4.6 13.8L8.333 11H12C12.5304 11 13.0391 10.7893 13.4142 10.4142C13.7893 10.0391 14 9.53043 14 9V2C14 1.46957 13.7893 0.960859 13.4142 0.585786C13.0391 0.210714 12.5304 0 12 0Z', fill='currentColor'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 20 18',
                        fill='currentColor',
                        cls='w-3 h-3 text-white'
                    ),
                    Span('Message icon', cls='sr-only'),
                    cls='absolute bottom-0 right-0 inline-flex items-center justify-center w-6 h-6 bg-primary-600 rounded-full'
                ),
                cls='relative inline-block shrink-0'
            ),
            Div(
                Div('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Div('commented on your photo', cls='text-sm font-normal'),
                Span('a few seconds ago', cls='text-xs font-medium text-primary-600 dark:text-primary-500'),
                cls='ms-3 text-sm font-normal'
            ),
            cls='flex items-center'
        ),
        id='toast-notification',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-900 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-300'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Interactive toast',
        Span(id='interactive-toast', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Interactive toast', href='#interactive-toast', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this interactive toast component to encourage users to make a certain action such as updating to the latest software version. You can set an icon, message, and two CTA buttons.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4'
                ),
                Span('Refresh icon', cls='sr-only'),
                cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-primary-500 bg-primary-100 rounded-lg dark:text-primary-300 dark:bg-primary-900'
            ),
            Div(
                Span('Update available', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
                Div('A new software version is available for download.', cls='mb-2 text-sm font-normal'),
                Div(
                    Div(
                        A('Update', href='#', cls='inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-500 dark:hover:bg-primary-600 dark:focus:ring-primary-800')
                    ),
                    Div(
                        A('Not now', href='#', cls='inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-gray-900 bg-gray-50 border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-600 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700')
                    ),
                    cls='grid grid-cols-2 gap-2'
                ),
                cls='ms-3 text-sm font-normal'
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
                data_dismiss_target='#toast-interactive',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 items-center justify-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex'
        ),
        id='toast-interactive',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-400'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4'
                ),
                Span('Refresh icon', cls='sr-only'),
                cls='inline-flex items-center justify-center shrink-0 w-8 h-8 text-primary-500 bg-primary-100 rounded-lg dark:text-primary-300 dark:bg-primary-900'
            ),
            Div(
                Span('Update available', cls='mb-1 text-sm font-semibold text-gray-900 dark:text-white'),
                Div('A new software version is available for download.', cls='mb-2 text-sm font-normal'),
                Div(
                    Div(
                        A('Update', href='#', cls='inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-500 dark:hover:bg-primary-600 dark:focus:ring-primary-800')
                    ),
                    Div(
                        A('Not now', href='#', cls='inline-flex justify-center w-full px-2 py-1.5 text-xs font-medium text-center text-gray-900 bg-gray-50 border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-600 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700')
                    ),
                    cls='grid grid-cols-2 gap-2'
                ),
                cls='ms-3 text-sm font-normal'
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
                data_dismiss_target='#toast-interactive',
                aria_label='Close',
                cls='ms-auto -mx-1.5 -my-1.5 bg-gray-50 items-center justify-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700'
            ),
            cls='flex'
        ),
        id='toast-interactive',
        role='alert',
        cls='w-full max-w-xs p-4 text-gray-500 bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-400'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Positioning',
        Span(id='positioning', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Positioning', href='#positioning', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('fixed'),
        'class from Tailwind CSS to position these toast components relative to the main content wrapper element from your document:'
    ),
    Ul(
        Li(
            'Top left:',
            Code('fixed top-5 left-5')
        ),
        Li(
            'Top right:',
            Code('fixed top-5 right-5')
        ),
        Li(
            'Bottom left:',
            Code('fixed bottom-5 left-5')
        ),
        Li(
            'Bottom right:',
            Code('fixed bottom-5 right-5')
        )
    ),
    component_showcase(Div(
    Div(
        Div('Top left positioning.', cls='text-sm font-normal'),
        id='toast-top-left',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm top-5 left-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Top right positioning.', cls='text-sm font-normal'),
        id='toast-top-right',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm top-5 right-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Bottom right positioning.', cls='text-sm font-normal'),
        id='toast-bottom-right',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm right-5 bottom-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Bottom left positioning.', cls='text-sm font-normal'),
        id='toast-bottom-left',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm bottom-5 left-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Div('Top left positioning.', cls='text-sm font-normal'),
        id='toast-top-left',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm top-5 left-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Top right positioning.', cls='text-sm font-normal'),
        id='toast-top-right',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm top-5 right-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Bottom right positioning.', cls='text-sm font-normal'),
        id='toast-bottom-right',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm right-5 bottom-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    ),
    Div(
        Div('Bottom left positioning.', cls='text-sm font-normal'),
        id='toast-bottom-left',
        role='alert',
        cls='fixed flex items-center w-full max-w-xs p-4 space-x-4 text-gray-500 bg-gray-50 divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow-sm bottom-5 left-5 dark:text-gray-400 dark:divide-gray-700 dark:bg-gray-800'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    P(
        'You can set your own distance for the',
        Code('top-*|right-*|bottom-*|left-*'),
        'positioning classes.'
    ),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Please check out the',
        A('Dismiss object', href='https://flowbite.com/docs/components/alerts/#javascript-behaviour'),
        'documentation to learn how to programmatically work with the toast component directly from JavaScript.'
    ),
    id='mainContent'
)
