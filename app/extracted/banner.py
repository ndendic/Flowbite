from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('Get started with the sticky banner component coded with Tailwind CSS and Flowbite to show marketing, informational and CTA messages to your website visitors fixed to the top or bottom part of the page as the user scroll down the main content area.'),
    P('Explore the following examples based on various styles, sizes, and positionings to leverage the sticky banner component and increase marketing conversions with a responsive element supporting dark mode.'),
    H2(
        'Default sticky banner',
        Span(id='default-sticky-banner', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default sticky banner', href='#default-sticky-banner', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this free example to show a text message for announcement with a CTA link, an icon element and a close button to dismiss the banner.'),
    component_showcase(Div(
    Div(
        Div(
            P(
                Span(
                    Svg(
                        Path(d='M15 1.943v12.114a1 1 0 0 1-1.581.814L8 11V5l5.419-3.871A1 1 0 0 1 15 1.943ZM7 4H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2v5a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V4ZM4 17v-5h1v5H4ZM16 5.183v5.634a2.984 2.984 0 0 0 0-5.634Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 19',
                        cls='w-3 h-3 text-gray-500 dark:text-gray-400'
                    ),
                    Span('Light bulb', cls='sr-only'),
                    cls='inline-flex p-1 me-3 bg-gray-200 rounded-full dark:bg-gray-600 w-6 h-6 items-center justify-center shrink-0'
                ),
                Span(
                    'New brand identity has been launched for the',
                    A('Flowbite Library', href='https://flowbite.com', cls='inline font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline')
                ),
                cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'
            ),
            cls='flex items-center mx-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#sticky-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center'
        ),
        id='sticky-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex justify-between w-full p-4 border-b border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Div(
            P(
                Span(
                    Svg(
                        Path(d='M15 1.943v12.114a1 1 0 0 1-1.581.814L8 11V5l5.419-3.871A1 1 0 0 1 15 1.943ZM7 4H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2v5a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V4ZM4 17v-5h1v5H4ZM16 5.183v5.634a2.984 2.984 0 0 0 0-5.634Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 19',
                        cls='w-3 h-3 text-gray-500 dark:text-gray-400'
                    ),
                    Span('Light bulb', cls='sr-only'),
                    cls='inline-flex p-1 me-3 bg-gray-200 rounded-full dark:bg-gray-600 w-6 h-6 items-center justify-center shrink-0'
                ),
                Span(
                    'New brand identity has been launched for the',
                    A('Flowbite Library', href='https://flowbite.com', cls='inline font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline')
                ),
                cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'
            ),
            cls='flex items-center mx-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#sticky-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center'
        ),
        id='sticky-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex justify-between w-full p-4 border-b border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Bottom banner position',
        Span(id='bottom-banner-position', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Bottom banner position', href='#bottom-banner-position', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to position the sticky banner to the bottom side of the page instead of the top side.'),
    component_showcase(Div(
    Div(
        Div(
            P(
                Span(
                    Svg(
                        Path(d='M18.435 7.546A2.32 2.32 0 0 1 17.7 5.77a3.354 3.354 0 0 0-3.47-3.47 2.322 2.322 0 0 1-1.776-.736 3.357 3.357 0 0 0-4.907 0 2.281 2.281 0 0 1-1.776.736 3.414 3.414 0 0 0-2.489.981 3.372 3.372 0 0 0-.982 2.49 2.319 2.319 0 0 1-.736 1.775 3.36 3.36 0 0 0 0 4.908A2.317 2.317 0 0 1 2.3 14.23a3.356 3.356 0 0 0 3.47 3.47 2.318 2.318 0 0 1 1.777.737 3.36 3.36 0 0 0 4.907 0 2.36 2.36 0 0 1 1.776-.737 3.356 3.356 0 0 0 3.469-3.47 2.319 2.319 0 0 1 .736-1.775 3.359 3.359 0 0 0 0-4.908ZM8.5 5.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm3 9.063a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm2.207-6.856-6 6a1 1 0 0 1-1.414-1.414l6-6a1 1 0 0 1 1.414 1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                    ),
                    Span('Discount', cls='sr-only'),
                    cls='inline-flex p-1 me-3 bg-gray-200 rounded-full dark:bg-gray-600 w-6 h-6 items-center justify-center'
                ),
                Span(
                    'Get 5% commission per sale',
                    A(
                        'Become a partner',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3 h-3 ms-2 rtl:rotate-180'
                        ),
                        href='https://flowbite.com',
                        cls='flex items-center ms-0 text-sm font-medium text-primary-600 md:ms-1 md:inline-flex dark:text-primary-500 hover:underline'
                    )
                ),
                cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'
            ),
            cls='flex items-center mx-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#bottom-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center'
        ),
        id='bottom-banner',
        tabindex='-1',
        cls='fixed bottom-0 start-0 z-50 flex justify-between w-full p-4 border-t border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Div(
            P(
                Span(
                    Svg(
                        Path(d='M18.435 7.546A2.32 2.32 0 0 1 17.7 5.77a3.354 3.354 0 0 0-3.47-3.47 2.322 2.322 0 0 1-1.776-.736 3.357 3.357 0 0 0-4.907 0 2.281 2.281 0 0 1-1.776.736 3.414 3.414 0 0 0-2.489.981 3.372 3.372 0 0 0-.982 2.49 2.319 2.319 0 0 1-.736 1.775 3.36 3.36 0 0 0 0 4.908A2.317 2.317 0 0 1 2.3 14.23a3.356 3.356 0 0 0 3.47 3.47 2.318 2.318 0 0 1 1.777.737 3.36 3.36 0 0 0 4.907 0 2.36 2.36 0 0 1 1.776-.737 3.356 3.356 0 0 0 3.469-3.47 2.319 2.319 0 0 1 .736-1.775 3.359 3.359 0 0 0 0-4.908ZM8.5 5.5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm3 9.063a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm2.207-6.856-6 6a1 1 0 0 1-1.414-1.414l6-6a1 1 0 0 1 1.414 1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400'
                    ),
                    Span('Discount', cls='sr-only'),
                    cls='inline-flex p-1 me-3 bg-gray-200 rounded-full dark:bg-gray-600 w-6 h-6 items-center justify-center'
                ),
                Span(
                    'Get 5% commission per sale',
                    A(
                        'Become a partner',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3 h-3 ms-2 rtl:rotate-180'
                        ),
                        href='https://flowbite.com',
                        cls='flex items-center ms-0 text-sm font-medium text-primary-600 md:ms-1 md:inline-flex dark:text-primary-500 hover:underline'
                    )
                ),
                cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'
            ),
            cls='flex items-center mx-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#bottom-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center'
        ),
        id='bottom-banner',
        tabindex='-1',
        cls='fixed bottom-0 start-0 z-50 flex justify-between w-full p-4 border-t border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Marketing CTA banner',
        Span(id='marketing-cta-banner', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Marketing CTA banner', href='#marketing-cta-banner', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this free example to show a text message for announcement with a CTA link, an icon element and a close button to dismiss the banner. Set a different width by using the',
        Code('max-w-{*}'),
        'utility classes from Tailwind CSS.'
    ),
    component_showcase(Div(
    Div(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-6 me-2'),
                Span('Flowbite', cls='self-center text-lg font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center mb-2 border-gray-200 md:pe-4 md:me-4 md:border-e md:mb-0 dark:border-gray-600'
            ),
            P('Build websites even faster with components on top of Tailwind CSS', cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col items-start mb-3 me-4 md:items-center md:flex-row md:mb-0'
        ),
        Div(
            A('Sign up', href='#', cls='px-5 py-2 me-2 text-xs font-medium text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#marketing-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center shrink-0'
        ),
        id='marketing-banner',
        tabindex='-1',
        cls='fixed z-50 flex flex-col md:flex-row justify-between w-[calc(100%-2rem)] p-4 -translate-x-1/2 bg-white border border-gray-100 rounded-lg shadow-xs lg:max-w-7xl left-1/2 top-6 dark:bg-gray-700 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Div(
            A(
                Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-6 me-2'),
                Span('Flowbite', cls='self-center text-lg font-semibold whitespace-nowrap dark:text-white'),
                href='https://flowbite.com/',
                cls='flex items-center mb-2 border-gray-200 md:pe-4 md:me-4 md:border-e md:mb-0 dark:border-gray-600'
            ),
            P('Build websites even faster with components on top of Tailwind CSS', cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col items-start mb-3 me-4 md:items-center md:flex-row md:mb-0'
        ),
        Div(
            A('Sign up', href='#', cls='px-5 py-2 me-2 text-xs font-medium text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#marketing-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center shrink-0'
        ),
        id='marketing-banner',
        tabindex='-1',
        cls='fixed z-50 flex flex-col md:flex-row justify-between w-[calc(100%-2rem)] p-4 -translate-x-1/2 bg-white border border-gray-100 rounded-lg shadow-xs lg:max-w-7xl left-1/2 top-6 dark:bg-gray-700 dark:border-gray-600'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Newsletter sign-up banner',
        Span(id='newsletter-sign-up-banner', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Newsletter sign-up banner', href='#newsletter-sign-up-banner', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to encourage your website visitors to sign up to your email newsletter by showing an inline form inside the sticky banner on the top side of your page.'),
    component_showcase(Div(
    Div(
        Div(
            Form(
                Label('Sign up for our newsletter', fr='email', cls='shrink-0 mb-2 me-auto text-sm font-medium text-gray-500 md:mb-0 md:me-4 dark:text-gray-400 md:m-0'),
                Input(type='email', id='email', placeholder='Enter your email', required=True, cls='bg-white border border-gray-300 text-gray-900 md:w-64 mb-2 md:mb-0 md:me-4 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                Button('Subscribe', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                cls='flex flex-col items-center w-full md:flex-row'
            ),
            cls='flex items-center shrink-0 w-full mx-auto sm:w-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#newsletter-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center absolute top-2.5 end-2.5 md:relative md:top-auto md:end-auto'
        ),
        id='newsletter-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex justify-between w-full p-4 border-b border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Div(
            Form(
                Label('Sign up for our newsletter', fr='email', cls='shrink-0 mb-2 me-auto text-sm font-medium text-gray-500 md:mb-0 md:me-4 dark:text-gray-400 md:m-0'),
                Input(type='email', id='email', placeholder='Enter your email', required=True, cls='bg-white border border-gray-300 text-gray-900 md:w-64 mb-2 md:mb-0 md:me-4 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                Button('Subscribe', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                cls='flex flex-col items-center w-full md:flex-row'
            ),
            cls='flex items-center shrink-0 w-full mx-auto sm:w-auto'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#newsletter-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center absolute top-2.5 end-2.5 md:relative md:top-auto md:end-auto'
        ),
        id='newsletter-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex justify-between w-full p-4 border-b border-gray-200 bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Informational banner',
        Span(id='informational-banner', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Informational banner', href='#informational-banner', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to share important information with your website visitors by showing a heading and a paragraph inside the sticky banner and two CTA buttons with links.'),
    component_showcase(Div(
    Div(
        Div(
            H2('Integration is the key', cls='mb-1 text-base font-semibold text-gray-900 dark:text-white'),
            P('You can integrate Flowbite with many tools to make your work even more efficient and lightning fast based on Tailwind CSS.', cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-4 md:mb-0 md:me-4'
        ),
        Div(
            A(
                Svg(
                    Path(d='M9 1.334C7.06.594 1.646-.84.293.653a1.158 1.158 0 0 0-.293.77v13.973c0 .193.046.383.134.55.088.167.214.306.366.403a.932.932 0 0 0 .5.147c.176 0 .348-.05.5-.147 1.059-.32 6.265.851 7.5 1.65V1.334ZM19.707.653C18.353-.84 12.94.593 11 1.333V18c1.234-.799 6.436-1.968 7.5-1.65a.931.931 0 0 0 .5.147.931.931 0 0 0 .5-.148c.152-.096.279-.235.366-.403.088-.167.134-.357.134-.55V1.423a1.158 1.158 0 0 0-.293-.77Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 18',
                    cls='w-3 h-3 me-2'
                ),
                'Learn more',
                href='#',
                cls='inline-flex items-center justify-center px-3 py-2 me-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            A(
                'Get started',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3 h-3 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex items-center justify-center px-3 py-2 me-2 text-xs font-medium text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#informational-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center shrink-0'
        ),
        id='informational-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex flex-col justify-between w-full p-4 border-b border-gray-200 md:flex-row bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
), code="""Div(
    Div(
        Div(
            H2('Integration is the key', cls='mb-1 text-base font-semibold text-gray-900 dark:text-white'),
            P('You can integrate Flowbite with many tools to make your work even more efficient and lightning fast based on Tailwind CSS.', cls='flex items-center text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='mb-4 md:mb-0 md:me-4'
        ),
        Div(
            A(
                Svg(
                    Path(d='M9 1.334C7.06.594 1.646-.84.293.653a1.158 1.158 0 0 0-.293.77v13.973c0 .193.046.383.134.55.088.167.214.306.366.403a.932.932 0 0 0 .5.147c.176 0 .348-.05.5-.147 1.059-.32 6.265.851 7.5 1.65V1.334ZM19.707.653C18.353-.84 12.94.593 11 1.333V18c1.234-.799 6.436-1.968 7.5-1.65a.931.931 0 0 0 .5.147.931.931 0 0 0 .5-.148c.152-.096.279-.235.366-.403.088-.167.134-.357.134-.55V1.423a1.158 1.158 0 0 0-.293-.77Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 20 18',
                    cls='w-3 h-3 me-2'
                ),
                'Learn more',
                href='#',
                cls='inline-flex items-center justify-center px-3 py-2 me-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
            ),
            A(
                'Get started',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3 h-3 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex items-center justify-center px-3 py-2 me-2 text-xs font-medium text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 14',
                    cls='w-3 h-3'
                ),
                Span('Close banner', cls='sr-only'),
                data_dismiss_target='#informational-banner',
                type='button',
                cls='shrink-0 inline-flex justify-center w-7 h-7 items-center text-gray-400 hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 dark:hover:bg-gray-600 dark:hover:text-white'
            ),
            cls='flex items-center shrink-0'
        ),
        id='informational-banner',
        tabindex='-1',
        cls='fixed top-0 start-0 z-50 flex flex-col justify-between w-full p-4 border-b border-gray-200 md:flex-row bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'For more sticky banner examples you can check',
        A('banner sections', href='https://flowbite.com/blocks/marketing/banner/'),
        'from Flowbite Blocks.'
    ),
    id='mainContent'
)
