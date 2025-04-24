from fasthtml.components import *
from fastbite.all import *
from fasthtml.svg import *

def Home():
    return Section(
    Div(cls='max-w-screen-xl px-4 py-8 mx-auto lg:py-16')(
        Div(cls='grid items-center gap-8 mb-8 lg:mb-16 lg:gap-12 lg:grid-cols-12')(
            Div(cls='col-span-6 text-center sm:mb-6 lg:text-left lg:mb-0')(
                A(href='#', role='alert', cls='inline-flex items-center justify-between px-1 py-1 pr-4 mb-6 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700')(
                    Span('New', cls='px-3 py-1 mr-3 text-xs text-white rounded-full bg-primary-600'),
                    Span("Flowbite is out! See what's new", cls='text-sm font-medium'),
                    Svg(fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg', cls='w-5 h-5 ml-2')(
                        Path(fill_rule='evenodd', d='M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', clip_rule='evenodd')
                    )
                ),
                H1('We invest in the world’s potential', cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl xl:text-6xl dark:text-white'),
                P('Here at Flowbite we focus on markets where innovation can unlock long-term value and drive economic growth.', cls='max-w-xl mx-auto mb-6 font-light text-gray-500 lg:mx-0 xl:mb-8 md:text-lg xl:text-xl dark:text-gray-400'),
                Form(action='#', cls='max-w-lg mx-auto lg:ml-0')(
                    Label('Search', fr='default-search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300'),
                    Div(cls='relative')(
                        Input(type='search', id='default-search', placeholder='Search Mockups, Logos...', required='', cls='block w-full p-4 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                        Button(type='submit', cls='text-white inline-flex items-center absolute right-2.5 bottom-2 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800')(
                            Svg(fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg', cls='w-4 h-4 mr-2 -ml-1')(
                                Path(fill_rule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clip_rule='evenodd')
                            ),
                            'Search'
                        )
                    )
                )
            ),
            Div(cls='col-span-6')(
                Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/search-mockup.png', alt='mockup', cls='dark:hidden'),
                Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/search-mockup-dark.png', alt='mockup dark', cls='hidden dark:block')
            )
        ),
        Div(cls='grid gap-8 sm:gap-12 md:grid-cols-3')(
            Div(cls='flex justify-center')(
                Svg(fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg', cls='w-6 h-6 mr-3 text-primary-600 dark:text-primary-500 shrink-0')(
                    Path(fill_rule='evenodd', d='M4 2a2 2 0 00-2 2v11a3 3 0 106 0V4a2 2 0 00-2-2H4zm1 14a1 1 0 100-2 1 1 0 000 2zm5-1.757l4.9-4.9a2 2 0 000-2.828L13.485 5.1a2 2 0 00-2.828 0L10 5.757v8.486zM16 18H9.071l6-6H16a2 2 0 012 2v2a2 2 0 01-2 2z', clip_rule='evenodd')
                ),
                Div(
                    H3('Customizable Categories', cls='mb-1 text-lg font-semibold leading-tight text-gray-900 dark:text-white'),
                    P("Host code that you don't want to share with the world in private.", cls='font-light text-gray-500 dark:text-gray-400')
                )
            ),
            Div(cls='flex justify-center')(
                Svg(fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg', cls='w-6 h-6 mr-3 text-primary-600 dark:text-primary-500 shrink-0')(
                    Path(fill_rule='evenodd', d='M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z', clip_rule='evenodd')
                ),
                Div(
                    H3('Private repos', cls='mb-1 text-lg font-semibold leading-tight text-gray-900 dark:text-white'),
                    P("Host code that you don't want to share with the world in private.", cls='font-light text-gray-500 dark:text-gray-400')
                )
            ),
            Div(cls='flex justify-center')(
                Svg(fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg', cls='w-6 h-6 mr-3 text-primary-600 dark:text-primary-500 shrink-0')(
                    Path(fill_rule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z', clip_rule='evenodd')
                ),
                Div(
                    H3('Tracking Saving Rate', cls='mb-1 text-lg font-semibold leading-tight text-gray-900 dark:text-white'),
                    P("Host code that you don't want to share with the world in private.", cls='font-light text-gray-500 dark:text-gray-400')
                )
            )
        )
    )
)