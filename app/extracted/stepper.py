from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The stepper component can be used to show a numbered list of steps next to a form component to indicate the progress and number of steps that are required to complete and submit the form data.'),
    P('There are multiple examples that you can use including horizontal or vertical aligned stepper components, different sizes, styles, and showing icons or numbers all coded with the utility classes from Tailwind CSS.'),
    H2(
        'Default stepper',
        Span(id='default-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default stepper', href='#default-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a list of form steps with a number and title of the step in a horizontal alignment.'),
    component_showcase(Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5'
                ),
                'Personal',
                Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
                cls="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500"
            ),
            cls="flex md:w-full items-center text-primary-600 dark:text-primary-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
        ),
        Li(
            Span(
                Span('2', cls='me-2'),
                'Account',
                Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
                cls="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500"
            ),
            cls="flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
        ),
        Li(
            Span('3', cls='me-2'),
            'Confirmation',
            cls='flex items-center'
        ),
        cls='flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base'
    )
), code="""Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 20',
                    cls='w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5'
                ),
                'Personal',
                Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
                cls="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500"
            ),
            cls="flex md:w-full items-center text-primary-600 dark:text-primary-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
        ),
        Li(
            Span(
                Span('2', cls='me-2'),
                'Account',
                Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
                cls="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500"
            ),
            cls="flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"
        ),
        Li(
            Span('3', cls='me-2'),
            'Confirmation',
            cls='flex items-center'
        ),
        cls='flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Progress stepper',
        Span(id='progress-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Progress stepper', href='#progress-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the progress of the stepper component based only on icons and showing a checkmark when the step has been finished.'),
    component_showcase(Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 12',
                    cls='w-3.5 h-3.5 text-primary-600 lg:w-4 lg:h-4 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-primary-100 rounded-full lg:h-12 lg:w-12 dark:bg-primary-800 shrink-0'
            ),
            cls="flex w-full items-center text-primary-600 dark:text-primary-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-primary-100 after:border-4 after:inline-block dark:after:border-primary-800"
        ),
        Li(
            Span(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-gray-500 lg:w-5 lg:h-5 dark:text-gray-100'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700"
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-gray-500 lg:w-5 lg:h-5 dark:text-gray-100'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls='flex items-center w-full'
        ),
        cls='flex items-center w-full'
    )
), code="""Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 12',
                    cls='w-3.5 h-3.5 text-primary-600 lg:w-4 lg:h-4 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-primary-100 rounded-full lg:h-12 lg:w-12 dark:bg-primary-800 shrink-0'
            ),
            cls="flex w-full items-center text-primary-600 dark:text-primary-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-primary-100 after:border-4 after:inline-block dark:after:border-primary-800"
        ),
        Li(
            Span(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-gray-500 lg:w-5 lg:h-5 dark:text-gray-100'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700"
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-gray-500 lg:w-5 lg:h-5 dark:text-gray-100'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls='flex items-center w-full'
        ),
        cls='flex items-center w-full'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Detailed stepper',
        Span(id='detailed-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Detailed stepper', href='#detailed-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an extra subtitle next to the number and the title of the steppper component based on an ordered list element.'),
    component_showcase(Div(
    Ol(
        Li(
            Span('1', cls='flex items-center justify-center w-8 h-8 border border-primary-600 rounded-full shrink-0 dark:border-primary-500'),
            Span(
                H3('User info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-primary-600 dark:text-primary-500 space-x-2.5 rtl:space-x-reverse'
        ),
        Li(
            Span('2', cls='flex items-center justify-center w-8 h-8 border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            Span(
                H3('Company info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-gray-500 dark:text-gray-400 space-x-2.5 rtl:space-x-reverse'
        ),
        Li(
            Span('3', cls='flex items-center justify-center w-8 h-8 border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            Span(
                H3('Payment info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-gray-500 dark:text-gray-400 space-x-2.5 rtl:space-x-reverse'
        ),
        cls='items-center w-full space-y-4 sm:flex sm:space-x-8 sm:space-y-0 rtl:space-x-reverse'
    )
), code="""Div(
    Ol(
        Li(
            Span('1', cls='flex items-center justify-center w-8 h-8 border border-primary-600 rounded-full shrink-0 dark:border-primary-500'),
            Span(
                H3('User info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-primary-600 dark:text-primary-500 space-x-2.5 rtl:space-x-reverse'
        ),
        Li(
            Span('2', cls='flex items-center justify-center w-8 h-8 border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            Span(
                H3('Company info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-gray-500 dark:text-gray-400 space-x-2.5 rtl:space-x-reverse'
        ),
        Li(
            Span('3', cls='flex items-center justify-center w-8 h-8 border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            Span(
                H3('Payment info', cls='font-medium leading-tight'),
                P('Step details here', cls='text-sm')
            ),
            cls='flex items-center text-gray-500 dark:text-gray-400 space-x-2.5 rtl:space-x-reverse'
        ),
        cls='items-center w-full space-y-4 sm:flex sm:space-x-8 sm:space-y-0 rtl:space-x-reverse'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Vertical stepper',
        Span(id='vertical-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Vertical stepper', href='#vertical-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a list of steps aligned vertically where you can indicate the completed, currently active, and the unexplored steps.'),
    component_showcase(Div(
    Ol(
        Li(
            Div(
                Div(
                    Span('User info', cls='sr-only'),
                    H3('1. User info', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-green-700 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:border-green-800 dark:text-green-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Account info', cls='sr-only'),
                    H3('2. Account info', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-green-700 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:border-green-800 dark:text-green-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Social accounts', cls='sr-only'),
                    H3('3. Social accounts', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-primary-700 bg-primary-100 border border-primary-300 rounded-lg dark:bg-gray-800 dark:border-primary-800 dark:text-primary-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Review', cls='sr-only'),
                    H3('4. Review', cls='font-medium'),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-gray-900 bg-gray-100 border border-gray-300 rounded-lg dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Confirmation', cls='sr-only'),
                    H3('5. Confirmation', cls='font-medium'),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-gray-900 bg-gray-100 border border-gray-300 rounded-lg dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            )
        ),
        cls='space-y-4 w-72'
    )
), code="""Div(
    Ol(
        Li(
            Div(
                Div(
                    Span('User info', cls='sr-only'),
                    H3('1. User info', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-green-700 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:border-green-800 dark:text-green-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Account info', cls='sr-only'),
                    H3('2. Account info', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-green-700 border border-green-300 rounded-lg bg-green-50 dark:bg-gray-800 dark:border-green-800 dark:text-green-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Social accounts', cls='sr-only'),
                    H3('3. Social accounts', cls='font-medium'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-4 h-4'
                    ),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-primary-700 bg-primary-100 border border-primary-300 rounded-lg dark:bg-gray-800 dark:border-primary-800 dark:text-primary-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Review', cls='sr-only'),
                    H3('4. Review', cls='font-medium'),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-gray-900 bg-gray-100 border border-gray-300 rounded-lg dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            )
        ),
        Li(
            Div(
                Div(
                    Span('Confirmation', cls='sr-only'),
                    H3('5. Confirmation', cls='font-medium'),
                    cls='flex items-center justify-between'
                ),
                role='alert',
                cls='w-full p-4 text-gray-900 bg-gray-100 border border-gray-300 rounded-lg dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400'
            )
        ),
        cls='space-y-4 w-72'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Breadcrumb stepper',
        Span(id='breadcrumb-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Breadcrumb stepper', href='#breadcrumb-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the number of steps similar to how a breadcrumb component looks like by using double chevron icons between the items.'),
    component_showcase(Div(
    Ol(
        Li(
            Span('1', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-primary-600 rounded-full shrink-0 dark:border-primary-500'),
            'Personal',
            Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m7 9 4-4-4-4M1 9l4-4-4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 12 10',
                cls='w-3 h-3 ms-2 sm:ms-4 rtl:rotate-180'
            ),
            cls='flex items-center text-primary-600 dark:text-primary-500'
        ),
        Li(
            Span('2', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            'Account',
            Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m7 9 4-4-4-4M1 9l4-4-4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 12 10',
                cls='w-3 h-3 ms-2 sm:ms-4 rtl:rotate-180'
            ),
            cls='flex items-center'
        ),
        Li(
            Span('3', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            'Review',
            cls='flex items-center'
        ),
        cls='flex items-center w-full p-3 space-x-2 text-sm font-medium text-center text-gray-500 bg-white border border-gray-200 rounded-lg shadow-xs dark:text-gray-400 sm:text-base dark:bg-gray-800 dark:border-gray-700 sm:p-4 sm:space-x-4 rtl:space-x-reverse'
    )
), code="""Div(
    Ol(
        Li(
            Span('1', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-primary-600 rounded-full shrink-0 dark:border-primary-500'),
            'Personal',
            Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m7 9 4-4-4-4M1 9l4-4-4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 12 10',
                cls='w-3 h-3 ms-2 sm:ms-4 rtl:rotate-180'
            ),
            cls='flex items-center text-primary-600 dark:text-primary-500'
        ),
        Li(
            Span('2', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            'Account',
            Span('Info', cls='hidden sm:inline-flex sm:ms-2'),
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m7 9 4-4-4-4M1 9l4-4-4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 12 10',
                cls='w-3 h-3 ms-2 sm:ms-4 rtl:rotate-180'
            ),
            cls='flex items-center'
        ),
        Li(
            Span('3', cls='flex items-center justify-center w-5 h-5 me-2 text-xs border border-gray-500 rounded-full shrink-0 dark:border-gray-400'),
            'Review',
            cls='flex items-center'
        ),
        cls='flex items-center w-full p-3 space-x-2 text-sm font-medium text-center text-gray-500 bg-white border border-gray-200 rounded-lg shadow-xs dark:text-gray-400 sm:text-base dark:bg-gray-800 dark:border-gray-700 sm:p-4 sm:space-x-4 rtl:space-x-reverse'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Timeline stepper',
        Span(id='timeline-stepper', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timeline stepper', href='#timeline-stepper', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show the number of steps inside a timeline component using icons, title, and subtitle for each step.'),
    component_showcase(Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 12',
                    cls='w-3.5 h-3.5 text-green-500 dark:text-green-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-green-200 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-green-900'
            ),
            H3('Personal Info', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Account Info', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Review', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Confirmation', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='ms-6'
        ),
        cls='relative text-gray-500 border-s border-gray-200 dark:border-gray-700 dark:text-gray-400'
    )
), code="""Div(
    Ol(
        Li(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 12',
                    cls='w-3.5 h-3.5 text-green-500 dark:text-green-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-green-200 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-green-900'
            ),
            H3('Personal Info', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Account Info', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Review', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='mb-10 ms-6'
        ),
        Li(
            Span(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full -start-4 ring-4 ring-white dark:ring-gray-900 dark:bg-gray-700'
            ),
            H3('Confirmation', cls='font-medium leading-tight'),
            P('Step details here', cls='text-sm'),
            cls='ms-6'
        ),
        cls='relative text-gray-500 border-s border-gray-200 dark:border-gray-700 dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Stepper with form',
        Span(id='stepper-with-form', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Stepper with form', href='#stepper-with-form', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show the stepper component next to a form layout and change the content based on which currently step your are completing.'),
    component_showcase(Div(
    Ol(
        Li(
            Div(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-primary-100 rounded-full lg:h-12 lg:w-12 dark:bg-primary-800 shrink-0'
            ),
            cls="flex w-full items-center text-primary-600 dark:text-primary-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-primary-100 after:border-4 after:inline-block dark:after:border-primary-800"
        ),
        Li(
            Div(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM2 12V6h16v6H2Z'),
                    Path(d='M6 8H4a1 1 0 0 0 0 2h2a1 1 0 0 0 0-2Zm8 0H9a1 1 0 0 0 0 2h5a1 1 0 1 0 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700"
        ),
        Li(
            Div(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls='flex items-center w-full'
        ),
        cls='flex items-center w-full mb-4 sm:mb-5'
    ),
    Form(
        H3('Invoice details', cls='mb-4 text-lg font-medium leading-none text-gray-900 dark:text-white'),
        Div(
            Div(
                Label('Username', fr='username', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', name='username', id='username', placeholder='username.example', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Confirm password', fr='confirm-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='password', name='confirm-password', id='confirm-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='grid gap-4 mb-4 sm:grid-cols-2'
        ),
        Button('Next Step: Payment Info', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        action='#'
    )
), code="""Div(
    Ol(
        Li(
            Div(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM6.5 3a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3.014 13.021l.157-.625A3.427 3.427 0 0 1 6.5 9.571a3.426 3.426 0 0 1 3.322 2.805l.159.622-6.967.023ZM16 12h-3a1 1 0 0 1 0-2h3a1 1 0 0 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Zm0-3h-3a1 1 0 1 1 0-2h3a1 1 0 1 1 0 2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-primary-100 rounded-full lg:h-12 lg:w-12 dark:bg-primary-800 shrink-0'
            ),
            cls="flex w-full items-center text-primary-600 dark:text-primary-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-primary-100 after:border-4 after:inline-block dark:after:border-primary-800"
        ),
        Li(
            Div(
                Svg(
                    Path(d='M18 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM2 12V6h16v6H2Z'),
                    Path(d='M6 8H4a1 1 0 0 0 0 2h2a1 1 0 0 0 0-2Zm8 0H9a1 1 0 0 0 0 2h5a1 1 0 1 0 0-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 14',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls="flex w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-100 after:border-4 after:inline-block dark:after:border-gray-700"
        ),
        Li(
            Div(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300'
                ),
                cls='flex items-center justify-center w-10 h-10 bg-gray-100 rounded-full lg:h-12 lg:w-12 dark:bg-gray-700 shrink-0'
            ),
            cls='flex items-center w-full'
        ),
        cls='flex items-center w-full mb-4 sm:mb-5'
    ),
    Form(
        H3('Invoice details', cls='mb-4 text-lg font-medium leading-none text-gray-900 dark:text-white'),
        Div(
            Div(
                Label('Username', fr='username', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='text', name='username', id='username', placeholder='username.example', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Confirm password', fr='confirm-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                Input(type='password', name='confirm-password', id='confirm-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='grid gap-4 mb-4 sm:grid-cols-2'
        ),
        Button('Next Step: Payment Info', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        action='#'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    id='mainContent'
)
