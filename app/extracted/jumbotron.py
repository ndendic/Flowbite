from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The Jumbotron (hero) component can be used as the first section of your website with a focus on a marketing message to increase the likelihood of the user to continue browsing your website.'),
    P('This UI component features a heading title, a short description, an optional CTA button, background image, gradient or solid background color and it’s generally inside of a card element.'),
    P('The jumbotron component from Flowbite is responsive on all devices, natively supports dark mode and is coded with the utility classes from Tailwind CSS.'),
    H2(
        'Default jumbotron',
        Span(id='default-jumbotron', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default jumbotron', href='#default-jumbotron', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this default example to show a title, description, and two CTA buttons for the jumbotron component.'),
    component_showcase(Div(
    Section(
        Div(
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-400'),
            Div(
                A(
                    'Get started',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                A('Learn more', href='#', cls='py-3 px-5 sm:ms-4 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                cls='flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
), code="""Div(
    Section(
        Div(
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-400'),
            Div(
                A(
                    'Get started',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                A('Learn more', href='#', cls='py-3 px-5 sm:ms-4 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                cls='flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Background image',
        Span(id='background-image', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Background image', href='#background-image', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this jumbotron to apply a background image with a darkening opacity effect to improve readability.'),
    component_showcase(Div(
    Section(
        Div(
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-white md:text-5xl lg:text-6xl'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-300 lg:text-xl sm:px-16 lg:px-48'),
            Div(
                A(
                    'Get started',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                A('Learn more', href='#', cls='inline-flex justify-center hover:text-gray-900 items-center py-3 px-5 sm:ms-4 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400'),
                cls='flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0'
            ),
            cls='px-4 mx-auto max-w-screen-xl text-center py-24 lg:py-56'
        ),
        cls="bg-center bg-no-repeat bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/conference.jpg')] bg-gray-700 bg-blend-multiply"
    )
), code="""Div(
    Section(
        Div(
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-white md:text-5xl lg:text-6xl'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-300 lg:text-xl sm:px-16 lg:px-48'),
            Div(
                A(
                    'Get started',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                A('Learn more', href='#', cls='inline-flex justify-center hover:text-gray-900 items-center py-3 px-5 sm:ms-4 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400'),
                cls='flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0'
            ),
            cls='px-4 mx-auto max-w-screen-xl text-center py-24 lg:py-56'
        ),
        cls="bg-center bg-no-repeat bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/conference.jpg')] bg-gray-700 bg-blend-multiply"
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Featured video',
        Span(id='featured-video', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Featured video', href='#featured-video', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to feature a video together with a heading title, description, and CTA buttons.'),
    component_showcase(Div(
    Section(
        Div(
            Div(
                H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
                P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400'),
                Div(
                    A(
                        'Get started',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                    ),
                    A('Learn more', href='#', cls='py-3 px-5 sm:ms-4 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex flex-col space-y-4 sm:flex-row sm:space-y-0'
                ),
                cls='flex flex-col justify-center'
            ),
            Div(
                Iframe(src='https://www.youtube.com/embed/KaLxCiilHns', title='YouTube video player', frameborder='0', allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture', allowfullscreen=True, cls='mx-auto w-full lg:max-w-xl h-64 rounded-lg sm:h-96 shadow-xl')
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
), code="""Div(
    Section(
        Div(
            Div(
                H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
                P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400'),
                Div(
                    A(
                        'Get started',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                    ),
                    A('Learn more', href='#', cls='py-3 px-5 sm:ms-4 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex flex-col space-y-4 sm:flex-row sm:space-y-0'
                ),
                cls='flex flex-col justify-center'
            ),
            Div(
                Iframe(src='https://www.youtube.com/embed/KaLxCiilHns', title='YouTube video player', frameborder='0', allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture', allowfullscreen=True, cls='mx-auto w-full lg:max-w-xl h-64 rounded-lg sm:h-96 shadow-xl')
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Authentication form',
        Span(id='authentication-form', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Authentication form', href='#authentication-form', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show a sign in or register form as the first section of your website.'),
    component_showcase(Div(
    Section(
        Div(
            Div(
                H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
                P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400'),
                A(
                    'Read more about our app',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                ),
                cls='flex flex-col justify-center'
            ),
            Div(
                Div(
                    H2('Sign in to Flowbite', cls='text-2xl font-bold text-gray-900 dark:text-white'),
                    Form(
                        Div(
                            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                        ),
                        Div(
                            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                        ),
                        Div(
                            Div(
                                Input(id='remember', aria_describedby='remember', name='remember', type='checkbox', required=True, cls='w-4 h-4 border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600'),
                                cls='flex items-center h-5'
                            ),
                            Div(
                                Label('Remember this device', fr='remember', cls='font-medium text-gray-500 dark:text-gray-400'),
                                cls='ms-3 text-sm'
                            ),
                            A('Lost Password?', href='#', cls='ms-auto text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
                            cls='flex items-start'
                        ),
                        Button('Login to your account', type='submit', cls='w-full px-5 py-3 text-base font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 sm:w-auto dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        Div(
                            'Not registered yet?',
                            A('Create account', cls='text-primary-600 hover:underline dark:text-primary-500'),
                            cls='text-sm font-medium text-gray-900 dark:text-white'
                        ),
                        action='#',
                        cls='mt-8 space-y-6'
                    ),
                    cls='w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800'
                )
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16'
        ),
        cls='bg-gray-50 dark:bg-gray-900'
    )
), code="""Div(
    Section(
        Div(
            Div(
                H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
                P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400'),
                A(
                    'Read more about our app',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                ),
                cls='flex flex-col justify-center'
            ),
            Div(
                Div(
                    H2('Sign in to Flowbite', cls='text-2xl font-bold text-gray-900 dark:text-white'),
                    Form(
                        Div(
                            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                        ),
                        Div(
                            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                        ),
                        Div(
                            Div(
                                Input(id='remember', aria_describedby='remember', name='remember', type='checkbox', required=True, cls='w-4 h-4 border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600'),
                                cls='flex items-center h-5'
                            ),
                            Div(
                                Label('Remember this device', fr='remember', cls='font-medium text-gray-500 dark:text-gray-400'),
                                cls='ms-3 text-sm'
                            ),
                            A('Lost Password?', href='#', cls='ms-auto text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
                            cls='flex items-start'
                        ),
                        Button('Login to your account', type='submit', cls='w-full px-5 py-3 text-base font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 sm:w-auto dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        Div(
                            'Not registered yet?',
                            A('Create account', cls='text-primary-600 hover:underline dark:text-primary-500'),
                            cls='text-sm font-medium text-gray-900 dark:text-white'
                        ),
                        action='#',
                        cls='mt-8 space-y-6'
                    ),
                    cls='w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800'
                )
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16'
        ),
        cls='bg-gray-50 dark:bg-gray-900'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Gradient background',
        Span(id='gradient-background', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Gradient background', href='#gradient-background', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show a hero pattern with a linear gradient layout as an overlay for added effects.'),
    component_showcase(Div(
    Section(
        Div(
            A(
                Span('New', cls='text-xs bg-primary-600 rounded-full text-white px-4 py-1.5 me-3'),
                Span("Jumbotron component was launched! See what's new", cls='text-sm font-medium'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2.5 h-2.5 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex justify-between items-center py-1 px-1 pe-4 mb-7 text-sm text-primary-700 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300 hover:bg-primary-200 dark:hover:bg-primary-800'
            ),
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-200'),
            Form(
                Label('Email sign-up', fr='default-email', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
                        cls='absolute inset-y-0 rtl:inset-x-0 start-0 flex items-center ps-3.5 pointer-events-none'
                    ),
                    Input(type='email', id='default-email', placeholder='Enter your email here...', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-white focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-800 dark:border-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    Button('Sign up', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='relative'
                ),
                cls='w-full max-w-md mx-auto'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16 z-10 relative'
        ),
        Div(cls='bg-gradient-to-b from-primary-50 to-transparent dark:from-primary-900 w-full h-full absolute top-0 left-0 z-0'),
        cls="bg-white dark:bg-gray-900 bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern.svg')] dark:bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern-dark.svg')]"
    )
), code="""Div(
    Section(
        Div(
            A(
                Span('New', cls='text-xs bg-primary-600 rounded-full text-white px-4 py-1.5 me-3'),
                Span("Jumbotron component was launched! See what's new", cls='text-sm font-medium'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-2.5 h-2.5 ms-2 rtl:rotate-180'
                ),
                href='#',
                cls='inline-flex justify-between items-center py-1 px-1 pe-4 mb-7 text-sm text-primary-700 bg-primary-100 rounded-full dark:bg-primary-900 dark:text-primary-300 hover:bg-primary-200 dark:hover:bg-primary-800'
            ),
            H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
            P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-200'),
            Form(
                Label('Email sign-up', fr='default-email', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
                        cls='absolute inset-y-0 rtl:inset-x-0 start-0 flex items-center ps-3.5 pointer-events-none'
                    ),
                    Input(type='email', id='default-email', placeholder='Enter your email here...', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-white focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-800 dark:border-gray-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                    Button('Sign up', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='relative'
                ),
                cls='w-full max-w-md mx-auto'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16 z-10 relative'
        ),
        Div(cls='bg-gradient-to-b from-primary-50 to-transparent dark:from-primary-900 w-full h-full absolute top-0 left-0 z-0'),
        cls="bg-white dark:bg-gray-900 bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern.svg')] dark:bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern-dark.svg')]"
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Jumbotron with cards',
        Span(id='jumbotron-with-cards', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Jumbotron with cards', href='#jumbotron-with-cards', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show cards with headings, descriptions, and CTA buttons inside a grid layout.'),
    component_showcase(Div(
    Section(
        Div(
            Div(
                A(
                    Svg(
                        Path(d='M11 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm8.585 1.189a.994.994 0 0 0-.9-.138l-2.965.983a1 1 0 0 0-.685.949v8a1 1 0 0 0 .675.946l2.965 1.02a1.013 1.013 0 0 0 1.032-.242A1 1 0 0 0 20 12V2a1 1 0 0 0-.415-.811Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 14',
                        cls='w-2.5 h-2.5 me-1.5'
                    ),
                    'Tutorial',
                    href='#',
                    cls='bg-primary-100 text-primary-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-primary-400 mb-2'
                ),
                H1('How to quickly deploy a static website', cls='text-gray-900 dark:text-white text-3xl md:text-5xl font-extrabold mb-2'),
                P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-6'),
                A(
                    'Read more',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-2.5 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12 mb-8'
            ),
            Div(
                Div(
                    A(
                        Svg(
                            Path(d='M17 11h-2.722L8 17.278a5.512 5.512 0 0 1-.9.722H17a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1ZM6 0H1a1 1 0 0 0-1 1v13.5a3.5 3.5 0 1 0 7 0V1a1 1 0 0 0-1-1ZM3.5 15.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2ZM16.132 4.9 12.6 1.368a1 1 0 0 0-1.414 0L9 3.55v9.9l7.132-7.132a1 1 0 0 0 0-1.418Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='w-2.5 h-2.5 me-1.5'
                        ),
                        'Design',
                        href='#',
                        cls='bg-green-100 text-green-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-green-400 mb-2'
                    ),
                    H2('Start with Flowbite Design System', cls='text-gray-900 dark:text-white text-3xl font-extrabold mb-2'),
                    P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-4'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                    ),
                    cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12'
                ),
                Div(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 4 1 8l4 4m10-8 4 4-4 4M11 1 9 15'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 16',
                            cls='w-2.5 h-2.5 me-1.5'
                        ),
                        'Code',
                        href='#',
                        cls='bg-purple-100 text-purple-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-purple-400 mb-2'
                    ),
                    H2('Best react libraries around the web', cls='text-gray-900 dark:text-white text-3xl font-extrabold mb-2'),
                    P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-4'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                    ),
                    cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12'
                ),
                cls='grid md:grid-cols-2 gap-8'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
), code="""Div(
    Section(
        Div(
            Div(
                A(
                    Svg(
                        Path(d='M11 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm8.585 1.189a.994.994 0 0 0-.9-.138l-2.965.983a1 1 0 0 0-.685.949v8a1 1 0 0 0 .675.946l2.965 1.02a1.013 1.013 0 0 0 1.032-.242A1 1 0 0 0 20 12V2a1 1 0 0 0-.415-.811Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 14',
                        cls='w-2.5 h-2.5 me-1.5'
                    ),
                    'Tutorial',
                    href='#',
                    cls='bg-primary-100 text-primary-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-primary-400 mb-2'
                ),
                H1('How to quickly deploy a static website', cls='text-gray-900 dark:text-white text-3xl md:text-5xl font-extrabold mb-2'),
                P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-6'),
                A(
                    'Read more',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                    ),
                    href='#',
                    cls='inline-flex justify-center items-center py-2.5 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
                ),
                cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12 mb-8'
            ),
            Div(
                Div(
                    A(
                        Svg(
                            Path(d='M17 11h-2.722L8 17.278a5.512 5.512 0 0 1-.9.722H17a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1ZM6 0H1a1 1 0 0 0-1 1v13.5a3.5 3.5 0 1 0 7 0V1a1 1 0 0 0-1-1ZM3.5 15.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2ZM16.132 4.9 12.6 1.368a1 1 0 0 0-1.414 0L9 3.55v9.9l7.132-7.132a1 1 0 0 0 0-1.418Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 18',
                            cls='w-2.5 h-2.5 me-1.5'
                        ),
                        'Design',
                        href='#',
                        cls='bg-green-100 text-green-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-green-400 mb-2'
                    ),
                    H2('Start with Flowbite Design System', cls='text-gray-900 dark:text-white text-3xl font-extrabold mb-2'),
                    P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-4'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                    ),
                    cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12'
                ),
                Div(
                    A(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 4 1 8l4 4m10-8 4 4-4 4M11 1 9 15'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 20 16',
                            cls='w-2.5 h-2.5 me-1.5'
                        ),
                        'Code',
                        href='#',
                        cls='bg-purple-100 text-purple-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded-md dark:bg-gray-700 dark:text-purple-400 mb-2'
                    ),
                    H2('Best react libraries around the web', cls='text-gray-900 dark:text-white text-3xl font-extrabold mb-2'),
                    P('Static websites are now used to bootstrap lots of websites and are becoming the basis for a variety of tools that even influence both web designers and developers.', cls='text-lg font-normal text-gray-500 dark:text-gray-400 mb-4'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 10',
                            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                        ),
                        href='#',
                        cls='text-primary-600 dark:text-primary-500 hover:underline font-medium text-lg inline-flex items-center'
                    ),
                    cls='bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-8 md:p-12'
                ),
                cls='grid md:grid-cols-2 gap-8'
            ),
            cls='py-8 px-4 mx-auto max-w-screen-xl lg:py-16'
        ),
        cls='bg-white dark:bg-gray-900'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'For more jumbotron examples you can check out the',
        A('hero sections', href='https://flowbite.com/blocks/marketing/hero/'),
        'from Flowbite Blocks.'
    ),
    id='mainContent'
)
