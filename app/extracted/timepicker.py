from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The timepicker component from Fastbite can be used to choose the hours and minutes of a given day through the usage of input fields such as the native HTML time field or even checkbox fields with predefined time interval which are popularly used for calendar event creation.'),
    P('The examples on this page are all built with Tailwind CSS and some of the examples require you to install the Fastbite JavaScript dependency to make the interactive UI components functional such as the datepicker, dropdowns, modals and the drawers.'),
    P('The timepicker component is often used together with a datepicker so the more advanced examples on this page show you a combination of these two components where you can select both the date (year, month and day) and then the time of the day for the event.'),
    H2(
        'Default timepicker',
        Span(id='default-timepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default timepicker', href='#default-timepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a simple input field with the native browser timepicker.'),
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
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Timepicker with icon',
        Span(id='timepicker-with-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timepicker with icon', href='#timepicker-with-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to select a time via an input field where you can add an icon to the input group.'),
    component_showcase(Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block flex-1 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Span(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-s-0 border-s-0 border-gray-300 rounded-e-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600'
            ),
            cls='flex'
        ),
        cls='max-w-[8.5rem] mx-auto'
    )
), code="""Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block flex-1 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Span(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-s-0 border-s-0 border-gray-300 rounded-e-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600'
            ),
            cls='flex'
        ),
        cls='max-w-[8.5rem] mx-auto'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Timepicker with dropdown',
        Span(id='timepicker-with-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timepicker with dropdown', href='#timepicker-with-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a timepicker together with a dropdown menu where you can add options such as selecting the timezone or the duration of an event in minutes or hours.'),
    component_showcase(Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block flex-1 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                'Duration',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-duration-button',
                data_dropdown_toggle='dropdown-duration',
                type='button',
                cls='border-s-0 shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('30 minutes', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('1 hour', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('2 hours', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-duration-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-duration',
                cls='z-10 hidden bg-gray-50 divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            cls='flex'
        ),
        cls='max-w-[13rem] mx-auto'
    )
), code="""Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block flex-1 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                'Duration',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-duration-button',
                data_dropdown_toggle='dropdown-duration',
                type='button',
                cls='border-s-0 shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('30 minutes', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('1 hour', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('2 hours', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-duration-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-duration',
                cls='z-10 hidden bg-gray-50 divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            cls='flex'
        ),
        cls='max-w-[13rem] mx-auto'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Timepicker with select',
        Span(id='timepicker-with-select', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timepicker with select', href='#timepicker-with-select', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a select input next to the timepicker to select an option like a timezone.'),
    component_showcase(Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='shrink-0 rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Select(
                Option('EST - GMT-5 (New York)', value='America/New_York', selected=True),
                Option('PST - GMT-8 (Los Angeles)', value='America/Los_Angeles'),
                Option('GMT - GMT+0 (London)', value='Europe/London'),
                Option('CET - GMT+1 (Paris)', value='Europe/Paris'),
                Option('JST - GMT+9 (Tokyo)', value='Asia/Tokyo'),
                Option('AEDT - GMT+11 (Sydney)', value='Australia/Sydney'),
                Option('MST - GMT-7 (Canada)', value='Canada/Mountain'),
                Option('CST - GMT-6 (Canada)', value='Canada/Central'),
                Option('EST - GMT-5 (Canada)', value='Canada/Eastern'),
                Option('CET - GMT+1 (Berlin)', value='Europe/Berlin'),
                Option('GST - GMT+4 (Dubai)', value='Asia/Dubai'),
                Option('SGT - GMT+8 (Singapore)', value='Asia/Singapore'),
                id='timezones',
                name='timezone',
                required=True,
                cls='bg-gray-50 border border-s-0 border-gray-300 text-gray-900 text-sm rounded-e-lg focus:ring-primary-500 focus:border-primary-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            ),
            cls='flex'
        )
    )
), code="""Div(
    Form(
        Label('Select time:', fr='time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Input(type='time', id='time', min='09:00', max='18:00', value='00:00', required=True, cls='shrink-0 rounded-none rounded-s-lg bg-gray-50 border text-gray-900 leading-none focus:ring-primary-500 focus:border-primary-500 block text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Select(
                Option('EST - GMT-5 (New York)', value='America/New_York', selected=True),
                Option('PST - GMT-8 (Los Angeles)', value='America/Los_Angeles'),
                Option('GMT - GMT+0 (London)', value='Europe/London'),
                Option('CET - GMT+1 (Paris)', value='Europe/Paris'),
                Option('JST - GMT+9 (Tokyo)', value='Asia/Tokyo'),
                Option('AEDT - GMT+11 (Sydney)', value='Australia/Sydney'),
                Option('MST - GMT-7 (Canada)', value='Canada/Mountain'),
                Option('CST - GMT-6 (Canada)', value='Canada/Central'),
                Option('EST - GMT-5 (Canada)', value='Canada/Eastern'),
                Option('CET - GMT+1 (Berlin)', value='Europe/Berlin'),
                Option('GST - GMT+4 (Dubai)', value='Asia/Dubai'),
                Option('SGT - GMT+8 (Singapore)', value='Asia/Singapore'),
                id='timezones',
                name='timezone',
                required=True,
                cls='bg-gray-50 border border-s-0 border-gray-300 text-gray-900 text-sm rounded-e-lg focus:ring-primary-500 focus:border-primary-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
            ),
            cls='flex'
        )
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Timepicker range selector',
        Span(id='timepicker-range-selector', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timepicker range selector', href='#timepicker-range-selector', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to select a time interval using two input field often used for the duration of an event.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            )
        ),
        Div(
            Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            )
        ),
        cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4'
    )
), code="""Div(
    Form(
        Div(
            Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            )
        ),
        Div(
            Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            )
        ),
        cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Timerange with dropdown',
        Span(id='timerange-with-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timerange with dropdown', href='#timerange-with-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the timerange picker inside a dropdown only when clicking on a button.'),
    component_showcase(Div(
    Button(
        'Choose time',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownTimepickerButton',
        data_dropdown_toggle='dropdownTimepicker',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            Div(
                Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            Div(
                Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4 mb-2'
        ),
        Button('Save time', id='saveTimeButton', type='button', cls='text-primary-700 dark:text-primary-500 text-sm hover:underline p-0'),
        id='dropdownTimepicker',
        cls='z-10 hidden bg-gray-50 rounded-lg shadow-sm w-auto dark:bg-gray-700 p-3'
    )
), code="""Div(
    Button(
        'Choose time',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 10 6',
            cls='w-2.5 h-2.5 ms-3'
        ),
        id='dropdownTimepickerButton',
        data_dropdown_toggle='dropdownTimepicker',
        type='button',
        cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
    ),
    Div(
        Div(
            Div(
                Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            Div(
                Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4 mb-2'
        ),
        Button('Save time', id='saveTimeButton', type='button', cls='text-primary-700 dark:text-primary-500 text-sm hover:underline p-0'),
        id='dropdownTimepicker',
        cls='z-10 hidden bg-gray-50 rounded-lg shadow-sm w-auto dark:bg-gray-700 p-3'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Timerange picker with toggle',
        Span(id='timerange-picker-with-toggle', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Timerange picker with toggle', href='#timerange-picker-with-toggle', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show or hide the timepicker when clicking on an trigger element.'),
    component_showcase(Div(
    Div(
        Button(
            'Select time',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m8 10 4 4 4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='none',
                viewbox='0 0 24 24',
                cls='w-8 h-8 ms-0.5'
            ),
            id='selectTimeToggle',
            data_collapse_toggle='time-range-container',
            type='button',
            cls='text-primary-700 dark:text-primary-500 text-base font-medium hover:underline p-0 inline-flex items-center mb-2'
        ),
        Div(
            Div(
                Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            Div(
                Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            id='time-range-container',
            cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4 mb-2 hidden'
        ),
        cls='w-[16rem]'
    )
), code="""Div(
    Div(
        Button(
            'Select time',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m8 10 4 4 4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='none',
                viewbox='0 0 24 24',
                cls='w-8 h-8 ms-0.5'
            ),
            id='selectTimeToggle',
            data_collapse_toggle='time-range-container',
            type='button',
            cls='text-primary-700 dark:text-primary-500 text-base font-medium hover:underline p-0 inline-flex items-center mb-2'
        ),
        Div(
            Div(
                Label('Start time:', fr='start-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='start-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            Div(
                Label('End time:', fr='end-time', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
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
                    Input(type='time', id='end-time', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    cls='relative'
                )
            ),
            id='time-range-container',
            cls='max-w-[16rem] mx-auto grid grid-cols-2 gap-4 mb-2 hidden'
        ),
        cls='w-[16rem]'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Inline timepicker buttons',
        Span(id='inline-timepicker-buttons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Inline timepicker buttons', href='#inline-timepicker-buttons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This is an advanced example that you can use to show the details of an event and select a date of the event based on the',
        A('Fastbite Datepicker', href='https://flowbite.com/docs/components/datepicker/'),
        'and select the time using a predefined set of time intervals based on checkbox elements.'
    ),
    component_showcase(Div(
    H2('Digital Transformation', cls='text-xl text-gray-900 dark:text-white font-bold mb-2'),
    Div(
        Div(
            Svg(
                Path(fill_rule='evenodd', d='M5 5a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1h1a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1h1a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1 2 2 0 0 1 2 2v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7a2 2 0 0 1 2-2ZM3 19v-7a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Zm6.01-6a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm2 0a1 1 0 1 1 2 0 1 1 0 0 1-2 0Zm6 0a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm-10 4a1 1 0 1 1 2 0 1 1 0 0 1-2 0Zm6 0a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm2 0a1 1 0 1 1 2 0 1 1 0 0 1-2 0Z', clip_rule='evenodd'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='currentColor',
                viewbox='0 0 24 24',
                cls='w-5 h-5 text-gray-400 me-2'
            ),
            Span('30.06.2024', cls='text-gray-900 dark:text-white text-base font-medium'),
            cls='flex items-center'
        ),
        Div(
            Svg(
                Path(fill_rule='evenodd', d='M11.906 1.994a8.002 8.002 0 0 1 8.09 8.421 7.996 7.996 0 0 1-1.297 3.957.996.996 0 0 1-.133.204l-.108.129c-.178.243-.37.477-.573.699l-5.112 6.224a1 1 0 0 1-1.545 0L5.982 15.26l-.002-.002a18.146 18.146 0 0 1-.309-.38l-.133-.163a.999.999 0 0 1-.13-.202 7.995 7.995 0 0 1 6.498-12.518ZM15 9.997a3 3 0 1 1-5.999 0 3 3 0 0 1 5.999 0Z', clip_rule='evenodd'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='currentColor',
                viewbox='0 0 24 24',
                cls='w-5 h-5 text-gray-400 me-2'
            ),
            Span('California, USA', cls='text-gray-900 dark:text-white text-base font-medium'),
            cls='flex items-center'
        ),
        cls='flex items-center space-x-4 rtl:space-x-reverse mb-3'
    ),
    Div(
        Div(
            Div('Participants', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-2'),
            Div(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                Img(src='/docs/images/people/profile-picture-2.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                Img(src='/docs/images/people/profile-picture-3.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                A('+99', href='#', cls='flex items-center justify-center w-8 h-8 text-xs font-medium text-white bg-gray-700 border border-white rounded-full hover:bg-gray-600 dark:border-gray-800'),
                cls='flex -space-x-4 rtl:space-x-reverse'
            )
        ),
        Div(
            Div('Duration', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-3'),
            Span('30 min', cls='text-gray-900 dark:text-white text-base font-medium block')
        ),
        Div(
            Div('Meeting Type', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-3'),
            Span('Web conference', cls='text-gray-900 dark:text-white text-base font-medium block')
        ),
        cls='flex items-start space-x-4 rtl:space-x-reverse mb-5'
    ),
    Div(
        Div(inline_datepicker=True, datepicker_buttons=True, datepicker_autoselect_today=True, cls='mx-auto sm:mx-0'),
        Div(
            H3('Wednesday 30 June 2024', cls='text-gray-900 dark:text-white text-base font-medium mb-3 text-center'),
            Button(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    width='24',
                    height='24',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-800 dark:text-white me-2'
                ),
                'Pick a time',
                type='button',
                data_collapse_toggle='timetable',
                cls='inline-flex items-center w-full py-2 px-5 me-2 justify-center text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            Label('Pick a time', cls='sr-only'),
            Ul(
                Li(
                    Input(type='radio', id='10-am', value=True, name='timetable', cls='hidden peer'),
                    Label('10:00 AM', fr='10-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='10-30-am', value=True, name='timetable', cls='hidden peer'),
                    Label('10:30 AM', fr='10-30-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='11-am', value=True, name='timetable', cls='hidden peer'),
                    Label('11:00 AM', fr='11-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='11-30-am', value=True, name='timetable', cls='hidden peer'),
                    Label('11:30 AM', fr='11-30-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='12-am', value=True, name='timetable', checked=True, cls='hidden peer'),
                    Label('12:00 AM', fr='12-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='12-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('12:30 PM', fr='12-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='1-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('01:00 PM', fr='1-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='1-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('01:30 PM', fr='1-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='2-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('02:00 PM', fr='2-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='2-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('02:30 PM', fr='2-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='3-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('03:00 PM', fr='3-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='3-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('03:30 PM', fr='3-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                id='timetable',
                cls='grid w-full grid-cols-2 gap-2 mt-5'
            ),
            cls='sm:ms-7 sm:ps-5 sm:border-s border-gray-200 dark:border-gray-800 w-full sm:max-w-[15rem] mt-5 sm:mt-0'
        ),
        cls='pt-5 border-t border-gray-200 dark:border-gray-800 flex sm:flex-row flex-col sm:space-x-5 rtl:space-x-reverse'
    )
), code="""Div(
    H2('Digital Transformation', cls='text-xl text-gray-900 dark:text-white font-bold mb-2'),
    Div(
        Div(
            Svg(
                Path(fill_rule='evenodd', d='M5 5a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1h1a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1h1a1 1 0 0 0 1-1 1 1 0 1 1 2 0 1 1 0 0 0 1 1 2 2 0 0 1 2 2v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7a2 2 0 0 1 2-2ZM3 19v-7a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Zm6.01-6a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm2 0a1 1 0 1 1 2 0 1 1 0 0 1-2 0Zm6 0a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm-10 4a1 1 0 1 1 2 0 1 1 0 0 1-2 0Zm6 0a1 1 0 1 0-2 0 1 1 0 0 0 2 0Zm2 0a1 1 0 1 1 2 0 1 1 0 0 1-2 0Z', clip_rule='evenodd'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='currentColor',
                viewbox='0 0 24 24',
                cls='w-5 h-5 text-gray-400 me-2'
            ),
            Span('30.06.2024', cls='text-gray-900 dark:text-white text-base font-medium'),
            cls='flex items-center'
        ),
        Div(
            Svg(
                Path(fill_rule='evenodd', d='M11.906 1.994a8.002 8.002 0 0 1 8.09 8.421 7.996 7.996 0 0 1-1.297 3.957.996.996 0 0 1-.133.204l-.108.129c-.178.243-.37.477-.573.699l-5.112 6.224a1 1 0 0 1-1.545 0L5.982 15.26l-.002-.002a18.146 18.146 0 0 1-.309-.38l-.133-.163a.999.999 0 0 1-.13-.202 7.995 7.995 0 0 1 6.498-12.518ZM15 9.997a3 3 0 1 1-5.999 0 3 3 0 0 1 5.999 0Z', clip_rule='evenodd'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                width='24',
                height='24',
                fill='currentColor',
                viewbox='0 0 24 24',
                cls='w-5 h-5 text-gray-400 me-2'
            ),
            Span('California, USA', cls='text-gray-900 dark:text-white text-base font-medium'),
            cls='flex items-center'
        ),
        cls='flex items-center space-x-4 rtl:space-x-reverse mb-3'
    ),
    Div(
        Div(
            Div('Participants', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-2'),
            Div(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                Img(src='/docs/images/people/profile-picture-2.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                Img(src='/docs/images/people/profile-picture-3.jpg', alt=True, cls='w-8 h-8 border border-white rounded-full dark:border-gray-800'),
                A('+99', href='#', cls='flex items-center justify-center w-8 h-8 text-xs font-medium text-white bg-gray-700 border border-white rounded-full hover:bg-gray-600 dark:border-gray-800'),
                cls='flex -space-x-4 rtl:space-x-reverse'
            )
        ),
        Div(
            Div('Duration', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-3'),
            Span('30 min', cls='text-gray-900 dark:text-white text-base font-medium block')
        ),
        Div(
            Div('Meeting Type', cls='text-base font-normal text-gray-500 dark:text-gray-400 mb-3'),
            Span('Web conference', cls='text-gray-900 dark:text-white text-base font-medium block')
        ),
        cls='flex items-start space-x-4 rtl:space-x-reverse mb-5'
    ),
    Div(
        Div(inline_datepicker=True, datepicker_buttons=True, datepicker_autoselect_today=True, cls='mx-auto sm:mx-0'),
        Div(
            H3('Wednesday 30 June 2024', cls='text-gray-900 dark:text-white text-base font-medium mb-3 text-center'),
            Button(
                Svg(
                    Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    width='24',
                    height='24',
                    fill='currentColor',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 text-gray-800 dark:text-white me-2'
                ),
                'Pick a time',
                type='button',
                data_collapse_toggle='timetable',
                cls='inline-flex items-center w-full py-2 px-5 me-2 justify-center text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            Label('Pick a time', cls='sr-only'),
            Ul(
                Li(
                    Input(type='radio', id='10-am', value=True, name='timetable', cls='hidden peer'),
                    Label('10:00 AM', fr='10-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='10-30-am', value=True, name='timetable', cls='hidden peer'),
                    Label('10:30 AM', fr='10-30-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='11-am', value=True, name='timetable', cls='hidden peer'),
                    Label('11:00 AM', fr='11-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='11-30-am', value=True, name='timetable', cls='hidden peer'),
                    Label('11:30 AM', fr='11-30-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='12-am', value=True, name='timetable', checked=True, cls='hidden peer'),
                    Label('12:00 AM', fr='12-am', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='12-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('12:30 PM', fr='12-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='1-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('01:00 PM', fr='1-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='1-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('01:30 PM', fr='1-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='2-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('02:00 PM', fr='2-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='2-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('02:30 PM', fr='2-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='3-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('03:00 PM', fr='3-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                Li(
                    Input(type='radio', id='3-30-pm', value=True, name='timetable', cls='hidden peer'),
                    Label('03:30 PM', fr='3-30-pm', cls='inline-flex items-center justify-center w-full p-2 text-sm font-medium text-center bg-gray-50 border rounded-lg cursor-pointer text-primary-600 border-primary-600 dark:hover:text-white dark:border-primary-500 dark:peer-checked:border-primary-500 peer-checked:border-primary-600 peer-checked:bg-primary-600 hover:text-white peer-checked:text-white dark:peer-checked:text-white hover:bg-primary-500 dark:text-primary-500 dark:bg-gray-900 dark:hover:bg-primary-600 dark:hover:border-primary-600 dark:peer-checked:bg-primary-500')
                ),
                id='timetable',
                cls='grid w-full grid-cols-2 gap-2 mt-5'
            ),
            cls='sm:ms-7 sm:ps-5 sm:border-s border-gray-200 dark:border-gray-800 w-full sm:max-w-[15rem] mt-5 sm:mt-0'
        ),
        cls='pt-5 border-t border-gray-200 dark:border-gray-800 flex sm:flex-row flex-col sm:space-x-5 rtl:space-x-reverse'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Modal with timepicker',
        Span(id='modal-with-timepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Modal with timepicker', href='#modal-with-timepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to select a date and time inside of a modal component based on the',
        A('Fastbite Datepicker', href='https://flowbite.com/docs/components/datepicker/'),
        'and select a time interval using checkbox elements with predefined time values for event time scheduling.'
    ),
    component_showcase(Div(
    Button(
        Svg(
            Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            width='24',
            height='24',
            fill='currentColor',
            viewbox='0 0 24 24',
            cls='w4 h-4 me-1'
        ),
        'Schedule appointment',
        type='button',
        data_modal_target='timepicker-modal',
        data_modal_toggle='timepicker-modal',
        cls='text-gray-900 bg-gray-50 hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Schedule an appointment', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-3 h-3'
                        ),
                        Span('Close modal', cls='sr-only'),
                        type='button',
                        data_modal_toggle='timepicker-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 border-b rounded-t dark:border-gray-700 border-gray-200'
                ),
                Div(
                    Div(inline_datepicker=True, datepicker_autoselect_today=True, cls='mx-auto sm:mx-0 flex justify-center my-5 [&>div>div]:shadow-none [&>div>div]:bg-gray-50 [&_div>button]:bg-gray-50'),
                    Label('Pick your time', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
                    Ul(
                        Li(
                            Input(type='radio', id='10-am', value=True, name='timetable', cls='hidden peer'),
                            Label('10:00 AM', fr='10-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='10-30-am', value=True, name='timetable', cls='hidden peer'),
                            Label('10:30 AM', fr='10-30-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='11-am', value=True, name='timetable', cls='hidden peer'),
                            Label('11:00 AM', fr='11-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='11-30-am', value=True, name='timetable', cls='hidden peer'),
                            Label('11:30 AM', fr='11-30-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='12-am', value=True, name='timetable', checked=True, cls='hidden peer'),
                            Label('12:00 AM', fr='12-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='12-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('12:30 PM', fr='12-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='1-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('01:00 PM', fr='1-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='1-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('01:30 PM', fr='1-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='2-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('02:00 PM', fr='2-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='2-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('02:30 PM', fr='2-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='3-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('03:00 PM', fr='3-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='3-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('03:30 PM', fr='3-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        id='timetable',
                        cls='grid w-full grid-cols-3 gap-2 mb-5'
                    ),
                    Div(
                        Button('Save', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
                        Button('Discard', type='button', data_modal_hide='timepicker-modal', cls='py-2.5 px-5 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                        cls='grid grid-cols-2 gap-2'
                    ),
                    cls='p-4 pt-0'
                ),
                cls='relative bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800'
            ),
            cls='relative p-4 w-full max-w-[23rem] max-h-full'
        ),
        id='timepicker-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button(
        Svg(
            Path(fill_rule='evenodd', d='M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z', clip_rule='evenodd'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            width='24',
            height='24',
            fill='currentColor',
            viewbox='0 0 24 24',
            cls='w4 h-4 me-1'
        ),
        'Schedule appointment',
        type='button',
        data_modal_target='timepicker-modal',
        data_modal_toggle='timepicker-modal',
        cls='text-gray-900 bg-gray-50 hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Schedule an appointment', cls='text-lg font-semibold text-gray-900 dark:text-white'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-3 h-3'
                        ),
                        Span('Close modal', cls='sr-only'),
                        type='button',
                        data_modal_toggle='timepicker-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 border-b rounded-t dark:border-gray-700 border-gray-200'
                ),
                Div(
                    Div(inline_datepicker=True, datepicker_autoselect_today=True, cls='mx-auto sm:mx-0 flex justify-center my-5 [&>div>div]:shadow-none [&>div>div]:bg-gray-50 [&_div>button]:bg-gray-50'),
                    Label('Pick your time', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
                    Ul(
                        Li(
                            Input(type='radio', id='10-am', value=True, name='timetable', cls='hidden peer'),
                            Label('10:00 AM', fr='10-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='10-30-am', value=True, name='timetable', cls='hidden peer'),
                            Label('10:30 AM', fr='10-30-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='11-am', value=True, name='timetable', cls='hidden peer'),
                            Label('11:00 AM', fr='11-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='11-30-am', value=True, name='timetable', cls='hidden peer'),
                            Label('11:30 AM', fr='11-30-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='12-am', value=True, name='timetable', checked=True, cls='hidden peer'),
                            Label('12:00 AM', fr='12-am', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='12-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('12:30 PM', fr='12-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='1-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('01:00 PM', fr='1-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='1-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('01:30 PM', fr='1-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='2-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('02:00 PM', fr='2-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='2-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('02:30 PM', fr='2-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='3-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('03:00 PM', fr='3-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        Li(
                            Input(type='radio', id='3-30-pm', value=True, name='timetable', cls='hidden peer'),
                            Label('03:30 PM', fr='3-30-pm', cls='inline-flex items-center justify-center w-full px-2 py-1 text-sm font-medium text-center hover:text-gray-900 dark:hover:text-white bg-gray-50 dark:bg-gray-800 border rounded-lg cursor-pointer text-gray-500 border-gray-200 dark:border-gray-700 dark:peer-checked:border-primary-500 peer-checked:border-primary-700 dark:hover:border-gray-600 dark:peer-checked:text-primary-500 peer-checked:bg-primary-50 peer-checked:text-primary-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-600 dark:peer-checked:bg-primary-900')
                        ),
                        id='timetable',
                        cls='grid w-full grid-cols-3 gap-2 mb-5'
                    ),
                    Div(
                        Button('Save', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
                        Button('Discard', type='button', data_modal_hide='timepicker-modal', cls='py-2.5 px-5 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                        cls='grid grid-cols-2 gap-2'
                    ),
                    cls='p-4 pt-0'
                ),
                cls='relative bg-gray-50 rounded-lg shadow-sm dark:bg-gray-800'
            ),
            cls='relative p-4 w-full max-w-[23rem] max-h-full'
        ),
        id='timepicker-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Drawer with timepicker',
        Span(id='drawer-with-timepicker', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Drawer with timepicker', href='#drawer-with-timepicker', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show multiple time interval selections inside of a drawer component to schedule time based on multiple entries (ie. days of the week) using the native browser time selection input element.'),
    component_showcase(Div(
    Div(
        Button('Set time schedule', type='button', data_drawer_target='drawer-timepicker', data_drawer_show='drawer-timepicker', aria_controls='drawer-timepicker', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='text-center'
    ),
    Div(
        H5('Time schedule', id='drawer-label', cls='inline-flex items-center mb-6 text-base font-semibold text-gray-500 uppercase dark:text-gray-400'),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            Span('Close menu', cls='sr-only'),
            type='button',
            data_drawer_hide='drawer-timepicker',
            aria_controls='drawer-timepicker',
            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white'
        ),
        Form(
            Div(
                Div(
                    Span('Business hours', cls='text-gray-900 dark:text-white text-base font-medium'),
                    Label(
                        Input(type='checkbox', value=True, name='business-hours', cls='sr-only peer'),
                        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-gray-50 after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Business hours', cls='sr-only'),
                        cls='inline-flex items-center cursor-pointer'
                    ),
                    cls='flex justify-between items-center mb-3'
                ),
                P('Enable or disable business working hours for all weekly working days', cls='text-sm text-gray-500 dark:text-gray-400 font-normal'),
                cls='rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-600 dark:bg-gray-700 mb-6'
            ),
            Div(
                Label(
                    Span('Select a timezone', cls='me-1'),
                    Button(
                        Svg(
                            Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                            aria_hidden='true',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-4 h-4 text-gray-400 cursor-pointer hover:text-gray-900 dark:hover:text-white dark:text-gray-500'
                        ),
                        Span('Details', cls='sr-only'),
                        type='button',
                        data_tooltip_target='tooltip-timezone'
                    ),
                    Div(
                        'Select a timezone that fits your location to accurately display time-related information.',
                        Div(data_popper_arrow=True, cls='tooltip-arrow'),
                        id='tooltip-timezone',
                        role='tooltip',
                        cls='inline-block absolute invisible z-10 py-2 px-3 max-w-sm text-xs font-normal text-white bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                    ),
                    fr='timezones',
                    cls='flex items-center mb-2 text-sm font-medium text-gray-900 dark:text-white'
                ),
                Select(
                    Option('Choose a timezone', selected=True, value=True),
                    Option('EST (Eastern Standard Time) - GMT-5 (New York)', value='America/New_York'),
                    Option('PST (Pacific Standard Time) - GMT-8 (Los Angeles)', value='America/Los_Angeles'),
                    Option('GMT (Greenwich Mean Time) - GMT+0 (London)', value='Europe/London'),
                    Option('CET (Central European Time) - GMT+1 (Paris)', value='Europe/Paris'),
                    Option('JST (Japan Standard Time) - GMT+9 (Tokyo)', value='Asia/Tokyo'),
                    Option('AEDT (Australian Eastern Daylight Time) - GMT+11 (Sydney)', value='Australia/Sydney'),
                    Option('MST (Mountain Standard Time) - GMT-7 (Canada)', value='Canada/Mountain'),
                    Option('CST (Central Standard Time) - GMT-6 (Canada)', value='Canada/Central'),
                    Option('EST (Eastern Standard Time) - GMT-5 (Canada)', value='Canada/Eastern'),
                    Option('CET (Central European Time) - GMT+1 (Berlin)', value='Europe/Berlin'),
                    Option('GST (Gulf Standard Time) - GMT+4 (Dubai)', value='Asia/Dubai'),
                    Option('SGT (Singapore Standard Time) - GMT+8 (Singapore)', value='Asia/Singapore'),
                    id='timezones',
                    name='timezone',
                    required=True,
                    cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                ),
                cls='pb-6 mb-6 border-b border-gray-200 dark:border-gray-700'
            ),
            Div(
                Div(
                    Div(
                        Input(checked=True, id='monday', name='days', type='checkbox', value='monday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Mon', fr='monday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-monday', cls='sr-only'),
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
                            Input(type='time', id='start-time-monday', name='start-time-monday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-monday', cls='sr-only'),
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
                            Input(type='time', id='end-time-monday', name='end-time-monday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='tuesday', name='days', type='checkbox', value='tuesday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Tue', fr='tuesday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-tuesday', cls='sr-only'),
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
                            Input(type='time', id='start-time-tuesday', name='start-time-tuesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-tuesday', cls='sr-only'),
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
                            Input(type='time', id='end-time-tuesday', name='end-time-tuesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(checked=True, id='wednesday', name='days', type='checkbox', value='wednesday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Wed', fr='wednesday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-wednesday', cls='sr-only'),
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
                            Input(type='time', id='start-time-wednesday', name='start-time-wednesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-wednesday', cls='sr-only'),
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
                            Input(type='time', id='end-time-wednesday', name='end-time-wednesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='thursday', name='days', type='checkbox', value='thursday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Thu', fr='thursday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-thursday', cls='sr-only'),
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
                            Input(type='time', id='start-time-thursday', name='start-time-thursday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-thursday', cls='sr-only'),
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
                            Input(type='time', id='end-time-thursday', name='end-time-thursday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='friday', name='days', type='checkbox', value='friday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Fri', fr='friday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-friday', cls='sr-only'),
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
                            Input(type='time', id='start-time-friday', name='start-time-friday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-friday', cls='sr-only'),
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
                            Input(type='time', id='end-time-friday', name='end-time-friday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 12h14m-7 7V5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    width='24',
                    height='24',
                    fill='none',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 me-1'
                ),
                'Add interval',
                type='button',
                cls='inline-flex items-center justify-center w-full py-2.5 mb-4 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            Div(
                Button('Close', type='button', data_drawer_hide='drawer-timepicker', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                Button('Save all', type='submit', cls='text-white w-full inline-flex items-center justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                cls='grid grid-cols-2 gap-4 bottom-4 left-0 w-full md:px-4 md:absolute'
            )
        ),
        id='drawer-timepicker',
        tabindex='-1',
        aria_labelledby='drawer-timepicker-label',
        cls='fixed top-0 left-0 z-40 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-gray-50 w-96 dark:bg-gray-800'
    )
), code="""Div(
    Div(
        Button('Set time schedule', type='button', data_drawer_target='drawer-timepicker', data_drawer_show='drawer-timepicker', aria_controls='drawer-timepicker', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='text-center'
    ),
    Div(
        H5('Time schedule', id='drawer-label', cls='inline-flex items-center mb-6 text-base font-semibold text-gray-500 uppercase dark:text-gray-400'),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 14',
                cls='w-3 h-3'
            ),
            Span('Close menu', cls='sr-only'),
            type='button',
            data_drawer_hide='drawer-timepicker',
            aria_controls='drawer-timepicker',
            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 absolute top-2.5 end-2.5 inline-flex items-center justify-center dark:hover:bg-gray-600 dark:hover:text-white'
        ),
        Form(
            Div(
                Div(
                    Span('Business hours', cls='text-gray-900 dark:text-white text-base font-medium'),
                    Label(
                        Input(type='checkbox', value=True, name='business-hours', cls='sr-only peer'),
                        Div(cls="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 dark:bg-gray-600 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-gray-50 after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600 dark:peer-checked:bg-primary-600"),
                        Span('Business hours', cls='sr-only'),
                        cls='inline-flex items-center cursor-pointer'
                    ),
                    cls='flex justify-between items-center mb-3'
                ),
                P('Enable or disable business working hours for all weekly working days', cls='text-sm text-gray-500 dark:text-gray-400 font-normal'),
                cls='rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-600 dark:bg-gray-700 mb-6'
            ),
            Div(
                Label(
                    Span('Select a timezone', cls='me-1'),
                    Button(
                        Svg(
                            Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                            aria_hidden='true',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-4 h-4 text-gray-400 cursor-pointer hover:text-gray-900 dark:hover:text-white dark:text-gray-500'
                        ),
                        Span('Details', cls='sr-only'),
                        type='button',
                        data_tooltip_target='tooltip-timezone'
                    ),
                    Div(
                        'Select a timezone that fits your location to accurately display time-related information.',
                        Div(data_popper_arrow=True, cls='tooltip-arrow'),
                        id='tooltip-timezone',
                        role='tooltip',
                        cls='inline-block absolute invisible z-10 py-2 px-3 max-w-sm text-xs font-normal text-white bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                    ),
                    fr='timezones',
                    cls='flex items-center mb-2 text-sm font-medium text-gray-900 dark:text-white'
                ),
                Select(
                    Option('Choose a timezone', selected=True, value=True),
                    Option('EST (Eastern Standard Time) - GMT-5 (New York)', value='America/New_York'),
                    Option('PST (Pacific Standard Time) - GMT-8 (Los Angeles)', value='America/Los_Angeles'),
                    Option('GMT (Greenwich Mean Time) - GMT+0 (London)', value='Europe/London'),
                    Option('CET (Central European Time) - GMT+1 (Paris)', value='Europe/Paris'),
                    Option('JST (Japan Standard Time) - GMT+9 (Tokyo)', value='Asia/Tokyo'),
                    Option('AEDT (Australian Eastern Daylight Time) - GMT+11 (Sydney)', value='Australia/Sydney'),
                    Option('MST (Mountain Standard Time) - GMT-7 (Canada)', value='Canada/Mountain'),
                    Option('CST (Central Standard Time) - GMT-6 (Canada)', value='Canada/Central'),
                    Option('EST (Eastern Standard Time) - GMT-5 (Canada)', value='Canada/Eastern'),
                    Option('CET (Central European Time) - GMT+1 (Berlin)', value='Europe/Berlin'),
                    Option('GST (Gulf Standard Time) - GMT+4 (Dubai)', value='Asia/Dubai'),
                    Option('SGT (Singapore Standard Time) - GMT+8 (Singapore)', value='Asia/Singapore'),
                    id='timezones',
                    name='timezone',
                    required=True,
                    cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                ),
                cls='pb-6 mb-6 border-b border-gray-200 dark:border-gray-700'
            ),
            Div(
                Div(
                    Div(
                        Input(checked=True, id='monday', name='days', type='checkbox', value='monday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Mon', fr='monday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-monday', cls='sr-only'),
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
                            Input(type='time', id='start-time-monday', name='start-time-monday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-monday', cls='sr-only'),
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
                            Input(type='time', id='end-time-monday', name='end-time-monday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='tuesday', name='days', type='checkbox', value='tuesday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Tue', fr='tuesday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-tuesday', cls='sr-only'),
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
                            Input(type='time', id='start-time-tuesday', name='start-time-tuesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-tuesday', cls='sr-only'),
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
                            Input(type='time', id='end-time-tuesday', name='end-time-tuesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(checked=True, id='wednesday', name='days', type='checkbox', value='wednesday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Wed', fr='wednesday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-wednesday', cls='sr-only'),
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
                            Input(type='time', id='start-time-wednesday', name='start-time-wednesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-wednesday', cls='sr-only'),
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
                            Input(type='time', id='end-time-wednesday', name='end-time-wednesday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='thursday', name='days', type='checkbox', value='thursday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Thu', fr='thursday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-thursday', cls='sr-only'),
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
                            Input(type='time', id='start-time-thursday', name='start-time-thursday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-thursday', cls='sr-only'),
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
                            Input(type='time', id='end-time-thursday', name='end-time-thursday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Div(
                Div(
                    Div(
                        Input(id='friday', name='days', type='checkbox', value='friday', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                        Label('Fri', fr='friday', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                        cls='flex items-center min-w-[4rem]'
                    ),
                    Div(
                        Label('Start time:', fr='start-time-friday', cls='sr-only'),
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
                            Input(type='time', id='start-time-friday', name='start-time-friday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Label('End time:', fr='end-time-friday', cls='sr-only'),
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
                            Input(type='time', id='end-time-friday', name='end-time-friday', min='09:00', max='18:00', value='00:00', required=True, cls='bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='relative'
                        ),
                        cls='w-full max-w-[7rem]'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M8.586 2.586A2 2 0 0 1 10 2h4a2 2 0 0 1 2 2v2h3a1 1 0 1 1 0 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8a1 1 0 0 1 0-2h3V4a2 2 0 0 1 .586-1.414ZM10 6h4V4h-4v2Zm1 4a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Zm4 0a1 1 0 1 0-2 0v8a1 1 0 1 0 2 0v-8Z', clip_rule='evenodd'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                width='24',
                                height='24',
                                fill='currentColor',
                                viewbox='0 0 24 24',
                                cls='w-5 h-5'
                            ),
                            Span('Delete', cls='sr-only'),
                            type='button',
                            cls='inline-flex items-center p-1.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100'
                        )
                    ),
                    cls='flex items-center justify-between'
                ),
                cls='mb-6'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 12h14m-7 7V5'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    width='24',
                    height='24',
                    fill='none',
                    viewbox='0 0 24 24',
                    cls='w-4 h-4 me-1'
                ),
                'Add interval',
                type='button',
                cls='inline-flex items-center justify-center w-full py-2.5 mb-4 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            Div(
                Button('Close', type='button', data_drawer_hide='drawer-timepicker', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                Button('Save all', type='submit', cls='text-white w-full inline-flex items-center justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                cls='grid grid-cols-2 gap-4 bottom-4 left-0 w-full md:px-4 md:absolute'
            )
        ),
        id='drawer-timepicker',
        tabindex='-1',
        aria_labelledby='drawer-timepicker-label',
        cls='fixed top-0 left-0 z-40 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-gray-50 w-96 dark:bg-gray-800'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    id='mainContent'
)
