from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('The pagination component can be used to navigate across a series of content and data sets for various pages such as blog posts, products, and more. You can use multiple variants of this component with or without icons and even for paginating table data entries.'),
    H2(
        'Default pagination',
        Span(id='default-pagination', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default pagination', href='#default-pagination', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following list of pagination items based on two sizes powered by Tailwind CSS utility classes to indicate a series of content for your website.'),
    component_showcase(Div(
    Nav(
        Ul(
            Li(
                A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='flex items-center justify-center px-3 h-8 text-primary-600 border border-gray-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('Next', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            cls='inline-flex -space-x-px text-sm'
        ),
        aria_label='Page navigation example'
    ),
    Nav(
        Ul(
            Li(
                A('Previous', href='#', cls='flex items-center justify-center px-4 h-10 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='flex items-center justify-center px-4 h-10 text-primary-600 border border-gray-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('Next', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            cls='inline-flex -space-x-px text-base h-10'
        ),
        aria_label='Page navigation example'
    )
), code="""Div(
    Nav(
        Ul(
            Li(
                A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='flex items-center justify-center px-3 h-8 text-primary-600 border border-gray-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('Next', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            cls='inline-flex -space-x-px text-sm'
        ),
        aria_label='Page navigation example'
    ),
    Nav(
        Ul(
            Li(
                A('Previous', href='#', cls='flex items-center justify-center px-4 h-10 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='flex items-center justify-center px-4 h-10 text-primary-600 border border-gray-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('Next', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            cls='inline-flex -space-x-px text-base h-10'
        ),
        aria_label='Page navigation example'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Pagination with icons',
        Span(id='pagination-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pagination with icons', href='#pagination-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The following pagination component example shows how you can use',
        A('SVG icons', href='https://flowbite.com/icons/'),
        'instead of text to show the previous and next pages.'
    ),
    component_showcase(Div(
    Nav(
        Ul(
            Li(
                A(
                    Span('Previous', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='z-10 flex items-center justify-center px-3 h-8 leading-tight text-primary-600 border border-primary-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A(
                    Span('Next', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            cls='flex items-center -space-x-px h-8 text-sm'
        ),
        aria_label='Page navigation example'
    ),
    Nav(
        Ul(
            Li(
                A(
                    Span('Previous', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-4 h-10 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='z-10 flex items-center justify-center px-4 h-10 leading-tight text-primary-600 border border-primary-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A(
                    Span('Next', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            cls='flex items-center -space-x-px h-10 text-base'
        ),
        aria_label='Page navigation example'
    )
), code="""Div(
    Nav(
        Ul(
            Li(
                A(
                    Span('Previous', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='z-10 flex items-center justify-center px-3 h-8 leading-tight text-primary-600 border border-primary-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A(
                    Span('Next', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-2.5 h-2.5 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            cls='flex items-center -space-x-px h-8 text-sm'
        ),
        aria_label='Page navigation example'
    ),
    Nav(
        Ul(
            Li(
                A(
                    Span('Previous', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-4 h-10 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            Li(
                A('1', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('2', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('3', href='#', aria_current='page', cls='z-10 flex items-center justify-center px-4 h-10 leading-tight text-primary-600 border border-primary-300 bg-primary-50 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white')
            ),
            Li(
                A('4', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A('5', href='#', cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
            ),
            Li(
                A(
                    Span('Next', cls='sr-only'),
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 rtl:rotate-180'
                    ),
                    href='#',
                    cls='flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
                )
            ),
            cls='flex items-center -space-x-px h-10 text-base'
        ),
        aria_label='Page navigation example'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Previous and next',
        Span(id='previous-and-next', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Previous and next', href='#previous-and-next', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following markup to show simple previous and next elements.'),
    component_showcase(Div(
    Div(
        A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        A('Next', href='#', cls='flex items-center justify-center px-3 h-8 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        cls='flex'
    ),
    Div(
        A('Previous', href='#', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        A('Next', href='#', cls='flex items-center justify-center px-4 h-10 ms-3 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        cls='flex'
    )
), code="""Div(
    Div(
        A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        A('Next', href='#', cls='flex items-center justify-center px-3 h-8 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        cls='flex'
    ),
    Div(
        A('Previous', href='#', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        A('Next', href='#', cls='flex items-center justify-center px-4 h-10 ms-3 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
        cls='flex'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Previous and next with icons',
        Span(id='previous-and-next-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Previous and next with icons', href='#previous-and-next-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following code to show simple previous and next elements with icons.'),
    component_showcase(Div(
    Div(
        A(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
            ),
            'Previous',
            href='#',
            cls='flex items-center justify-center px-3 h-8 me-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        A(
            'Next',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        cls='flex'
    ),
    Div(
        A(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
            ),
            'Previous',
            href='#',
            cls='flex items-center justify-center px-4 h-10 me-3 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        A(
            'Next',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='flex items-center justify-center px-4 h-10 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        cls='flex'
    )
), code="""Div(
    Div(
        A(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
            ),
            'Previous',
            href='#',
            cls='flex items-center justify-center px-3 h-8 me-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        A(
            'Next',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        cls='flex'
    ),
    Div(
        A(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
            ),
            'Previous',
            href='#',
            cls='flex items-center justify-center px-4 h-10 me-3 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        A(
            'Next',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='flex items-center justify-center px-4 h-10 text-base font-medium text-gray-500 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
        ),
        cls='flex'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Table data pagination',
        Span(id='table-data-pagination', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table data pagination', href='#table-data-pagination', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can use the following markup to show the number of data shown inside a table element and also the previous and next action buttons.'),
    component_showcase(Div(
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button('Prev', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            Button('Next', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    ),
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button('Prev', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            Button('Next', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    )
), code="""Div(
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button('Prev', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            Button('Next', cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    ),
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button('Prev', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            Button('Next', cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Table data pagination with icons',
        Span(id='table-data-pagination-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table data pagination with icons', href='#table-data-pagination-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can use the following code to show the number of data shown inside a table element and also the previous and next action buttons coupled with icons.'),
    component_showcase(Div(
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
                ),
                'Prev',
                cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            Button(
                'Next',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                ),
                cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    ),
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
                ),
                'Prev',
                cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            Button(
                'Next',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                ),
                cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    )
), code="""Div(
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
                ),
                'Prev',
                cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            Button(
                'Next',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                ),
                cls='flex items-center justify-center px-3 h-8 text-sm font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    ),
    Div(
        Span(
            'Showing',
            Span('1', cls='font-semibold text-gray-900 dark:text-white'),
            'to',
            Span('10', cls='font-semibold text-gray-900 dark:text-white'),
            'of',
            Span('100', cls='font-semibold text-gray-900 dark:text-white'),
            'Entries',
            cls='text-sm text-gray-700 dark:text-gray-400'
        ),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 me-2 rtl:rotate-180'
                ),
                'Prev',
                cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 rounded-s hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            Button(
                'Next',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 14 10',
                    cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
                ),
                cls='flex items-center justify-center px-4 h-10 text-base font-medium text-white bg-gray-800 border-0 border-s border-gray-700 rounded-e hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'
            ),
            cls='inline-flex mt-2 xs:mt-0'
        ),
        cls='flex flex-col items-center'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    id='mainContent'
)
