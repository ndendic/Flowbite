from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The table component represents a set of structured elements made up of rows and columns as table cells that can be used to show data sets to your website users.'),
    P('Get started with multiple variants and styles of these table components built with the utility classes from Tailwind CSS and components from Flowbite.'),
    H2(
        'Default table',
        Span(id='default-table', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default table', href='#default-table', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example of a responsive table component to show multiple rows and columns of text data.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Highlight',
        Span(id='highlight', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Highlight', href='#highlight', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Accentuate certain elements inside the table such as the rows, columns or data cells based on your needs.'),
    H3(
        'Striped rows',
        Span(id='striped-rows', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Striped rows', href='#striped-rows', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to increase the readability of the data sets by alternating the background color of every second table row.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    )
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    )
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H3(
        'Striped columns',
        Span(id='striped-columns', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Striped columns', href='#striped-columns', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to increase the readability of the table cells by alternating the background color of every second table column.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 bg-gray-50 dark:bg-gray-800'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3 bg-gray-50 dark:bg-gray-800'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$99', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$799', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$999', cls='px-6 py-4')
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 bg-gray-50 dark:bg-gray-800'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3 bg-gray-50 dark:bg-gray-800'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$99', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$799', cls='px-6 py-4'),
                    cls='border-b border-gray-200 dark:border-gray-700'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50 dark:text-white dark:bg-gray-800'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4 bg-gray-50 dark:bg-gray-800'),
                    Td('$999', cls='px-6 py-4')
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H3(
        'Hover state',
        Span(id='hover-state', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Hover state', href='#hover-state', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('hover:{bg-*}'),
        'utility class from Tailwind CSS to change the background color of a data row when hovering over the element with the cursor.'
    ),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Table layout',
        Span(id='table-layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table layout', href='#table-layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples of table layouts to show the head, foot or caption of the table.'),
    H3(
        'Table head (sortable)',
        Span(id='table-head-sortable', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table head (sortable)', href='#table-head-sortable', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the head of the table component with sortable icons.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th(
                        Div(
                            'Color',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Div(
                            'Category',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Div(
                            'Price',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th(
                        Div(
                            'Color',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Div(
                            'Category',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Div(
                            'Price',
                            A(
                                Svg(
                                    Path(d='M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 24 24',
                                    cls='w-3 h-3 ms-1.5'
                                ),
                                href='#'
                            ),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='px-6 py-3'
                    ),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H3(
        'Table foot',
        Span(id='table-foot', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table foot', href='#table-foot', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example where the',
        Code('<tfoot>'),
        'HTML element can be used in conjunction with the head and caption of the table component.'
    ),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 rounded-s-lg'),
                    Th('Qty', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3 rounded-e-lg')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            Tfoot(
                Tr(
                    Th('Total', scope='row', cls='px-6 py-3 text-base'),
                    Td('3', cls='px-6 py-3'),
                    Td('21,000', cls='px-6 py-3'),
                    cls='font-semibold text-gray-900 dark:text-white'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 rounded-s-lg'),
                    Th('Qty', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3 rounded-e-lg')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('1', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            Tfoot(
                Tr(
                    Th('Total', scope='row', cls='px-6 py-3 text-base'),
                    Td('3', cls='px-6 py-3'),
                    Td('21,000', cls='px-6 py-3'),
                    cls='font-semibold text-gray-900 dark:text-white'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H3(
        'Table caption',
        Span(id='table-caption', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table caption', href='#table-caption', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Improve accessibility by using a caption inside the table as a heading to better describe what the table is about for screen readers.'),
    component_showcase(Div(
    Div(
        Table(
            Caption(
                'Our products',
                P('Browse a list of Flowbite products designed to help you work and play, stay organized, get answers, keep in touch, grow your business, and more.', cls='mt-1 text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='p-5 text-lg font-semibold text-left rtl:text-right text-gray-900 bg-white dark:text-white dark:bg-gray-800'
            ),
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Caption(
                'Our products',
                P('Browse a list of Flowbite products designed to help you work and play, stay organized, get answers, keep in touch, grow your business, and more.', cls='mt-1 text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='p-5 text-lg font-semibold text-left rtl:text-right text-gray-900 bg-white dark:text-white dark:bg-gray-800'
            ),
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th(
                        Span('Edit', cls='sr-only'),
                        scope='col',
                        cls='px-6 py-3'
                    )
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4 text-right'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Table styles',
        Span(id='table-styles', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table styles', href='#table-styles', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with the following table styles and choose the one that best fits your application.'),
    H3(
        'Without border',
        Span(id='without-border', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Without border', href='#without-border', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a table component without any border between the table cells.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-900 uppercase dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-900 uppercase dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Table with shadow',
        Span(id='table-with-shadow', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table with shadow', href='#table-with-shadow', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to apply a shadow-sm border to the table component.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Overflow scrolling',
        Span(id='overflow-scrolling', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Overflow scrolling', href='#overflow-scrolling', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example where we apply',
        Code('overflow-x-auto'),
        'to enable horizontal scrolling if the content inside the table overflows that maximum width.'
    ),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Accessories', scope='col', cls='px-6 py-3'),
                    Th('Available', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Weight', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td('3.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td('1.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td('0.2 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Watches', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$199', cls='px-6 py-4'),
                    Td('0.12 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td('7.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple AirPods', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$399', cls='px-6 py-4'),
                    Td('38 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td('1.3 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Keyboard', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td('453 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple TV 4K', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('TV', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td('1.78 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('AirTag', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$29', cls='px-6 py-4'),
                    Td('53 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Accessories', scope='col', cls='px-6 py-3'),
                    Th('Available', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Weight', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td('3.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td('1.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td('0.2 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Watches', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$199', cls='px-6 py-4'),
                    Td('0.12 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td('7.0 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple AirPods', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$399', cls='px-6 py-4'),
                    Td('38 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td('1.3 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Keyboard', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td('453 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple TV 4K', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('TV', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td('1.78 lb.', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('AirTag', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('Yes', cls='px-6 py-4'),
                    Td('No', cls='px-6 py-4'),
                    Td('$29', cls='px-6 py-4'),
                    Td('53 g', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline ms-3'),
                        cls='flex items-center px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Table search',
        Span(id='table-search', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table search', href='#table-search', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a search bar that can be used to query through data inside the table component.'),
    component_showcase(Div(
    Div(
        Div(
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search', placeholder='Search for items', cls='block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative mt-1'
            ),
            cls='pb-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Div(
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search', placeholder='Search for items', cls='block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative mt-1'
            ),
            cls='pb-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_10",cls='mt-2 mb-6'),
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
        'Table filter',
        Span(id='table-filter', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table filter', href='#table-filter', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example with a filter bar to select certain data sets inside the table based on the options that you’ve selected.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Button(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 text-gray-500 dark:text-gray-400 me-3'
                    ),
                    'Last 30 days',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownRadioButton',
                    data_dropdown_toggle='dropdownRadio',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            Div(
                                Input(id='filter-radio-example-1', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last day', fr='filter-radio-example-1', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(checked=True, id='filter-radio-example-2', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last 7 days', fr='filter-radio-example-2', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-3', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last 30 days', fr='filter-radio-example-3', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-4', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last month', fr='filter-radio-example-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-5', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last year', fr='filter-radio-example-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        aria_labelledby='dropdownRadioButton',
                        cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdownRadio',
                    data_popper_reference_hidden=True,
                    data_popper_escaped=True,
                    data_popper_placement='top',
                    style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);',
                    cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
            Div(
                Div(
                    Svg(
                        Path(fill_rule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clip_rule='evenodd'),
                        aria_hidden='true',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 text-gray-500 dark:text-gray-400'
                    ),
                    cls='absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search', placeholder='Search for items', cls='block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Button(
                    Svg(
                        Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 text-gray-500 dark:text-gray-400 me-3'
                    ),
                    'Last 30 days',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownRadioButton',
                    data_dropdown_toggle='dropdownRadio',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            Div(
                                Input(id='filter-radio-example-1', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last day', fr='filter-radio-example-1', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(checked=True, id='filter-radio-example-2', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last 7 days', fr='filter-radio-example-2', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-3', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last 30 days', fr='filter-radio-example-3', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-4', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last month', fr='filter-radio-example-4', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        Li(
                            Div(
                                Input(id='filter-radio-example-5', type='radio', value=True, name='filter-radio', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                                Label('Last year', fr='filter-radio-example-5', cls='w-full ms-2 text-sm font-medium text-gray-900 rounded-sm dark:text-gray-300'),
                                cls='flex items-center p-2 rounded-sm hover:bg-gray-100 dark:hover:bg-gray-600'
                            )
                        ),
                        aria_labelledby='dropdownRadioButton',
                        cls='p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdownRadio',
                    data_popper_reference_hidden=True,
                    data_popper_escaped=True,
                    data_popper_placement='top',
                    style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);',
                    cls='z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow-sm dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
            Div(
                Div(
                    Svg(
                        Path(fill_rule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clip_rule='evenodd'),
                        aria_hidden='true',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 text-gray-500 dark:text-gray-400'
                    ),
                    cls='absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search', placeholder='Search for items', cls='block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Table pagination',
        Span(id='table-pagination', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table pagination', href='#table-pagination', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Paginate the table data when using larger data sets based on any given amount of results per page.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Watches', cls='px-6 py-4'),
                    Td('$199', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple AirPods', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$399', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Keyboard', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Smart Folio iPad Air', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Blue', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$79', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('AirTag', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$29', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        Nav(
            Span(
                'Showing',
                Span('1-10', cls='font-semibold text-gray-900 dark:text-white'),
                'of',
                Span('1000', cls='font-semibold text-gray-900 dark:text-white'),
                cls='text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto'
            ),
            Ul(
                Li(
                    A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
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
                cls='inline-flex -space-x-px rtl:space-x-reverse text-sm h-8'
            ),
            aria_label='Table navigation',
            cls='flex items-center flex-column flex-wrap md:flex-row justify-between pt-4'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Watches', cls='px-6 py-4'),
                    Td('$199', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple AirPods', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$399', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Keyboard', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Smart Folio iPad Air', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Blue', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$79', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('AirTag', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$29', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        Nav(
            Span(
                'Showing',
                Span('1-10', cls='font-semibold text-gray-900 dark:text-white'),
                'of',
                Span('1000', cls='font-semibold text-gray-900 dark:text-white'),
                cls='text-sm font-normal text-gray-500 dark:text-gray-400 mb-4 md:mb-0 block w-full md:inline md:w-auto'
            ),
            Ul(
                Li(
                    A('Previous', href='#', cls='flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white')
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
                cls='inline-flex -space-x-px rtl:space-x-reverse text-sm h-8'
            ),
            aria_label='Table navigation',
            cls='flex items-center flex-column flex-wrap md:flex-row justify-between pt-4'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_12",cls='mt-2 mb-6'),
    H2(
        'Checkbox selection',
        Span(id='checkbox-selection', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Checkbox selection', href='#checkbox-selection', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Checkboxes can be used inside table data rows to select multiple data sets and apply a bulk action.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple Watch', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$179', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('iPad', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Gold', cls='px-6 py-4'),
                    Td('Tablet', cls='px-6 py-4'),
                    Td('$699', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th('Apple iMac 27"', scope='row', cls='px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('PC Desktop', cls='px-6 py-4'),
                    Td('$3999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_13",cls='mt-2 mb-6'),
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
        'Table with users',
        Span(id='table-with-users', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table with users', href='#table-with-users', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a table where we show a data set of users and showing a profile picture, name, email, online status, and more.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Button(
                    Span('Action button', cls='sr-only'),
                    'Action',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownActionButton',
                    data_dropdown_toggle='dropdownAction',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            A('Reward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Promote', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Activate account', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='dropdownActionButton',
                        cls='py-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    Div(
                        A('Delete User', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                        cls='py-1'
                    ),
                    id='dropdownAction',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search-users', placeholder='Search for users', cls='block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex items-center justify-between flex-column flex-wrap md:flex-row space-y-4 md:space-y-0 pb-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Name', scope='col', cls='px-6 py-3'),
                    Th('Position', scope='col', cls='px-6 py-3'),
                    Th('Status', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Neil Sims', cls='text-base font-semibold'),
                            Div('neil.sims@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('React Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Bonnie Green', cls='text-base font-semibold'),
                            Div('bonnie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Designer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Jese Leos', cls='text-base font-semibold'),
                            Div('jese@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Vue JS Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Thomas Lean', cls='text-base font-semibold'),
                            Div('thomes@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('UI/UX Engineer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Leslie Livingston', cls='text-base font-semibold'),
                            Div('leslie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('SEO Specialist', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-red-500 me-2'),
                            'Offline',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Button(
                    Span('Action button', cls='sr-only'),
                    'Action',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownActionButton',
                    data_dropdown_toggle='dropdownAction',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            A('Reward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Promote', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Activate account', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='dropdownActionButton',
                        cls='py-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    Div(
                        A('Delete User', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                        cls='py-1'
                    ),
                    id='dropdownAction',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search-users', placeholder='Search for users', cls='block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex items-center justify-between flex-column flex-wrap md:flex-row space-y-4 md:space-y-0 pb-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Name', scope='col', cls='px-6 py-3'),
                    Th('Position', scope='col', cls='px-6 py-3'),
                    Th('Status', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Neil Sims', cls='text-base font-semibold'),
                            Div('neil.sims@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('React Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Bonnie Green', cls='text-base font-semibold'),
                            Div('bonnie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Designer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Jese Leos', cls='text-base font-semibold'),
                            Div('jese@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Vue JS Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Thomas Lean', cls='text-base font-semibold'),
                            Div('thomes@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('UI/UX Engineer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Leslie Livingston', cls='text-base font-semibold'),
                            Div('leslie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('SEO Specialist', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-red-500 me-2'),
                            'Offline',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_14",cls='mt-2 mb-6'),
    H2(
        'Table with products',
        Span(id='table-with-products', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table with products', href='#table-with-products', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example to show a list of products inside the table and show a preview image, product name, quantity selector, price and actions tab.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Span('Image', cls='sr-only'),
                        scope='col',
                        cls='px-16 py-3'
                    ),
                    Th('Product', scope='col', cls='px-6 py-3'),
                    Th('Qty', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Img(src='/docs/images/products/apple-watch.png', alt='Apple Watch', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('Apple Watch', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 me-3 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$599', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Img(src='/docs/images/products/imac.png', alt='Apple iMac', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('iMac 27"', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='ms-3'
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$2499', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Img(src='/docs/images/products/iphone-12.png', alt='iPhone 12', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('IPhone 12', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='ms-3'
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$999', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th(
                        Span('Image', cls='sr-only'),
                        scope='col',
                        cls='px-16 py-3'
                    ),
                    Th('Product', scope='col', cls='px-6 py-3'),
                    Th('Qty', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Img(src='/docs/images/products/apple-watch.png', alt='Apple Watch', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('Apple Watch', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 me-3 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$599', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Img(src='/docs/images/products/imac.png', alt='Apple iMac', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('iMac 27"', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='ms-3'
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$2499', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Img(src='/docs/images/products/iphone-12.png', alt='iPhone 12', cls='w-16 md:w-32 max-w-full max-h-full'),
                        cls='p-4'
                    ),
                    Td('IPhone 12', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        Div(
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 2',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center p-1 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            Div(
                                Input(type='number', id='first_product', placeholder='1', required=True, cls='bg-gray-50 w-14 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block px-2.5 py-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='ms-3'
                            ),
                            Button(
                                Span('Quantity button', cls='sr-only'),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 18 18',
                                    cls='w-3 h-3'
                                ),
                                type='button',
                                cls='inline-flex items-center justify-center h-6 w-6 p-1 ms-3 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                            ),
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td('$999', cls='px-6 py-4 font-semibold text-gray-900 dark:text-white'),
                    Td(
                        A('Remove', href='#', cls='font-medium text-red-600 dark:text-red-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_15",cls='mt-2 mb-6'),
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
        'Table with modal',
        Span(id='table-with-modal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table with modal', href='#table-with-modal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a modal with a form where you can edit table data by clicking on one of the rows.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Button(
                    Span('Action button', cls='sr-only'),
                    'Action',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownActionButton',
                    data_dropdown_toggle='dropdownAction',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            A('Reward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Promote', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Activate account', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='dropdownActionButton',
                        cls='py-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    Div(
                        A('Delete User', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                        cls='py-1'
                    ),
                    id='dropdownAction',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search-users', placeholder='Search for users', cls='block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex items-center justify-between flex-column md:flex-row flex-wrap space-y-4 md:space-y-0 py-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Name', scope='col', cls='px-6 py-3'),
                    Th('Position', scope='col', cls='px-6 py-3'),
                    Th('Status', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Neil Sims', cls='text-base font-semibold'),
                            Div('neil.sims@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('React Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_target='editUserModal', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Bonnie Green', cls='text-base font-semibold'),
                            Div('bonnie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Designer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Jese Leos', cls='text-base font-semibold'),
                            Div('jese@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Vue JS Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Thomas Lean', cls='text-base font-semibold'),
                            Div('thomes@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('UI/UX Engineer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Leslie Livingston', cls='text-base font-semibold'),
                            Div('leslie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('SEO Specialist', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-red-500 me-2'),
                            'Offline',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        Div(
            Div(
                Form(
                    Div(
                        H3('Edit user', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                            data_modal_hide='editUserModal',
                            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                        ),
                        cls='flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600 border-gray-200'
                    ),
                    Div(
                        Div(
                            Div(
                                Label('First Name', fr='first-name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='first-name', id='first-name', placeholder='Bonnie', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Last Name', fr='last-name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='last-name', id='last-name', placeholder='Green', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='email', name='email', id='email', placeholder='example@company.com', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Phone Number', fr='phone-number', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='number', name='phone-number', id='phone-number', placeholder='e.g. +(12)3456 789', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Department', fr='department', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='department', id='department', placeholder='Development', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Company', fr='company', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='number', name='company', id='company', placeholder='123456', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Current Password', fr='current-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='password', name='current-password', id='current-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('New Password', fr='new-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='password', name='new-password', id='new-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            cls='grid grid-cols-6 gap-6'
                        ),
                        cls='p-6 space-y-6'
                    ),
                    Div(
                        Button('Save all', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        cls='flex items-center p-6 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                    ),
                    cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
                ),
                cls='relative w-full max-w-2xl max-h-full'
            ),
            id='editUserModal',
            tabindex='-1',
            aria_hidden='true',
            cls='fixed top-0 left-0 right-0 z-50 items-center justify-center hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Button(
                    Span('Action button', cls='sr-only'),
                    'Action',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdownActionButton',
                    data_dropdown_toggle='dropdownAction',
                    type='button',
                    cls='inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700'
                ),
                Div(
                    Ul(
                        Li(
                            A('Reward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Promote', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        Li(
                            A('Activate account', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                        ),
                        aria_labelledby='dropdownActionButton',
                        cls='py-1 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    Div(
                        A('Delete User', href='#', cls='block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white'),
                        cls='py-1'
                    ),
                    id='dropdownAction',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700 dark:divide-gray-600'
                )
            ),
            Label('Search', fr='table-search', cls='sr-only'),
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
                    cls='absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none'
                ),
                Input(type='text', id='table-search-users', placeholder='Search for users', cls='block pt-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative'
            ),
            cls='flex items-center justify-between flex-column md:flex-row flex-wrap space-y-4 md:space-y-0 py-4 bg-white dark:bg-gray-900'
        ),
        Table(
            Thead(
                Tr(
                    Th(
                        Div(
                            Input(id='checkbox-all-search', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-all-search', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        scope='col',
                        cls='p-4'
                    ),
                    Th('Name', scope='col', cls='px-6 py-3'),
                    Th('Position', scope='col', cls='px-6 py-3'),
                    Th('Status', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400'
            ),
            Tbody(
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-1', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-1', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-1.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Neil Sims', cls='text-base font-semibold'),
                            Div('neil.sims@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('React Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_target='editUserModal', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Bonnie Green', cls='text-base font-semibold'),
                            Div('bonnie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Designer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-2.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Jese Leos', cls='text-base font-semibold'),
                            Div('jese@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('Vue JS Developer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-2', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-2', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-5.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Thomas Lean', cls='text-base font-semibold'),
                            Div('thomes@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('UI/UX Engineer', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-green-500 me-2'),
                            'Online',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200 hover:bg-gray-50 dark:hover:bg-gray-600'
                ),
                Tr(
                    Td(
                        Div(
                            Input(id='checkbox-table-search-3', type='checkbox', cls='w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'),
                            Label('checkbox', fr='checkbox-table-search-3', cls='sr-only'),
                            cls='flex items-center'
                        ),
                        cls='w-4 p-4'
                    ),
                    Th(
                        Img(src='/docs/images/people/profile-picture-4.jpg', alt='Jese image', cls='w-10 h-10 rounded-full'),
                        Div(
                            Div('Leslie Livingston', cls='text-base font-semibold'),
                            Div('leslie@flowbite.com', cls='font-normal text-gray-500'),
                            cls='ps-3'
                        ),
                        scope='row',
                        cls='flex items-center px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white'
                    ),
                    Td('SEO Specialist', cls='px-6 py-4'),
                    Td(
                        Div(
                            Div(cls='h-2.5 w-2.5 rounded-full bg-red-500 me-2'),
                            'Offline',
                            cls='flex items-center'
                        ),
                        cls='px-6 py-4'
                    ),
                    Td(
                        A('Edit user', href='#', type='button', data_modal_show='editUserModal', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-600'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        Div(
            Div(
                Form(
                    Div(
                        H3('Edit user', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                            data_modal_hide='editUserModal',
                            cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                        ),
                        cls='flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600 border-gray-200'
                    ),
                    Div(
                        Div(
                            Div(
                                Label('First Name', fr='first-name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='first-name', id='first-name', placeholder='Bonnie', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Last Name', fr='last-name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='last-name', id='last-name', placeholder='Green', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='email', name='email', id='email', placeholder='example@company.com', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Phone Number', fr='phone-number', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='number', name='phone-number', id='phone-number', placeholder='e.g. +(12)3456 789', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Department', fr='department', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='text', name='department', id='department', placeholder='Development', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Company', fr='company', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='number', name='company', id='company', placeholder='123456', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('Current Password', fr='current-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='password', name='current-password', id='current-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            Div(
                                Label('New Password', fr='new-password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                Input(type='password', name='new-password', id='new-password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='shadow-xs bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                                cls='col-span-6 sm:col-span-3'
                            ),
                            cls='grid grid-cols-6 gap-6'
                        ),
                        cls='p-6 space-y-6'
                    ),
                    Div(
                        Button('Save all', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        cls='flex items-center p-6 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                    ),
                    cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
                ),
                cls='relative w-full max-w-2xl max-h-full'
            ),
            id='editUserModal',
            tabindex='-1',
            aria_hidden='true',
            cls='fixed top-0 left-0 right-0 z-50 items-center justify-center hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_16",cls='mt-2 mb-6'),
    H2(
        'Comparison table',
        Span(id='comparison-table', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Comparison table', href='#comparison-table', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to compare values inside a table such as a pricing card.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Div('Tailwind CSS code', cls='flex items-center'),
                Div('Community Edition'),
                Div('Developer Edition'),
                Div('Designer Edition'),
                cls='grid grid-cols-4 p-4 text-sm font-medium text-gray-900 bg-gray-100 border-t border-b border-gray-200 gap-x-16 dark:bg-gray-800 dark:border-gray-700 dark:text-white'
            ),
            Div(
                Div(
                    'Basic components (',
                    A('view all', href='#', cls='text-primary-600 hover:underline'),
                    ')',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div(
                    'Application UI (',
                    A('view demo', href='#', cls='text-primary-600 hover:underline'),
                    ')',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div('Marketing UI pre-order', cls='text-gray-500 dark:text-gray-400'),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div('E-commerce UI pre-order', cls='text-gray-500 dark:text-gray-400'),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div(cls='text-gray-500 dark:text-gray-400'),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            cls='overflow-hidden min-w-max'
        ),
        id='detailed-pricing',
        cls='w-full overflow-x-auto'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Div('Tailwind CSS code', cls='flex items-center'),
                Div('Community Edition'),
                Div('Developer Edition'),
                Div('Designer Edition'),
                cls='grid grid-cols-4 p-4 text-sm font-medium text-gray-900 bg-gray-100 border-t border-b border-gray-200 gap-x-16 dark:bg-gray-800 dark:border-gray-700 dark:text-white'
            ),
            Div(
                Div(
                    'Basic components (',
                    A('view all', href='#', cls='text-primary-600 hover:underline'),
                    ')',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div(
                    'Application UI (',
                    A('view demo', href='#', cls='text-primary-600 hover:underline'),
                    ')',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div('Marketing UI pre-order', cls='text-gray-500 dark:text-gray-400'),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div('E-commerce UI pre-order', cls='text-gray-500 dark:text-gray-400'),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-green-500'
                    )
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 14',
                        cls='w-3 h-3 text-red-500'
                    )
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            Div(
                Div(cls='text-gray-500 dark:text-gray-400'),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                Div(
                    A('Buy now', href='#', cls='text-white block w-full bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-4 py-2.5 text-center dark:focus:ring-primary-900')
                ),
                cls='grid grid-cols-4 px-4 py-5 text-sm text-gray-700 border-b border-gray-200 gap-x-16 dark:border-gray-700'
            ),
            cls='overflow-hidden min-w-max'
        ),
        id='detailed-pricing',
        cls='w-full overflow-x-auto'
    )
)""", id="example_17",cls='mt-2 mb-6'),
    H2(
        'Table colors',
        Span(id='table-colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Table colors', href='#table-colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply any color to the table element by using the',
        Code('bg-{color}'),
        'and',
        Code('text-{color}'),
        'color class variants from Tailwind CSS.'
    ),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_18",cls='mt-2 mb-6'),
    H3(
        'Striped rows color',
        Span(id='striped-rows-color', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Striped rows color', href='#striped-rows-color', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to apply a different color to every second row inside the table.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-500 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_19",cls='mt-2 mb-6'),
    H3(
        'Striped columns color',
        Span(id='striped-columns-color', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Striped columns color', href='#striped-columns-color', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to apply a different color to every second column inside a colored table.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 bg-primary-500'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3 bg-primary-500'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3 bg-primary-500')
                ),
                cls='text-xs text-white uppercase bg-primary-600 border-b border-primary-400 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4 bg-primary-500'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4 bg-primary-500'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4 bg-primary-500'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4 bg-primary-500'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4 bg-primary-500'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3 bg-primary-500'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3 bg-primary-500'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3 bg-primary-500')
                ),
                cls='text-xs text-white uppercase bg-primary-600 border-b border-primary-400 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4 bg-primary-500'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4 bg-primary-500'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4 bg-primary-500'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4 bg-primary-500'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-b border-primary-400'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium bg-primary-500 text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4 bg-primary-500'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4 bg-primary-500'
                    ),
                    cls='bg-primary-600 border-primary-40'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_20",cls='mt-2 mb-6'),
    H3(
        'Hover state',
        Span(id='hover-state-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Hover state', href='#hover-state-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to apply a different color to every second row inside the table with a colored background.'),
    component_showcase(Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 border-b border-primary-400 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-primary-400 hover:bg-primary-500'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
), code="""Div(
    Div(
        Table(
            Thead(
                Tr(
                    Th('Product name', scope='col', cls='px-6 py-3'),
                    Th('Color', scope='col', cls='px-6 py-3'),
                    Th('Category', scope='col', cls='px-6 py-3'),
                    Th('Price', scope='col', cls='px-6 py-3'),
                    Th('Action', scope='col', cls='px-6 py-3')
                ),
                cls='text-xs text-white uppercase bg-primary-600 border-b border-primary-400 dark:text-white'
            ),
            Tbody(
                Tr(
                    Th('Apple MacBook Pro 17"', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Silver', cls='px-6 py-4'),
                    Td('Laptop', cls='px-6 py-4'),
                    Td('$2999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Microsoft Surface Pro', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('White', cls='px-6 py-4'),
                    Td('Laptop PC', cls='px-6 py-4'),
                    Td('$1999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Magic Mouse 2', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Black', cls='px-6 py-4'),
                    Td('Accessories', cls='px-6 py-4'),
                    Td('$99', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Google Pixel Phone', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Gray', cls='px-6 py-4'),
                    Td('Phone', cls='px-6 py-4'),
                    Td('$799', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-b border-primary-400 hover:bg-primary-500'
                ),
                Tr(
                    Th('Apple Watch 5', scope='row', cls='px-6 py-4 font-medium text-primary-50 whitespace-nowrap dark:text-primary-100'),
                    Td('Red', cls='px-6 py-4'),
                    Td('Wearables', cls='px-6 py-4'),
                    Td('$999', cls='px-6 py-4'),
                    Td(
                        A('Edit', href='#', cls='font-medium text-white hover:underline'),
                        cls='px-6 py-4'
                    ),
                    cls='bg-primary-600 border-primary-400 hover:bg-primary-500'
                )
            ),
            cls='w-full text-sm text-left rtl:text-right text-primary-100 dark:text-primary-100'
        ),
        cls='relative overflow-x-auto shadow-md sm:rounded-lg'
    )
)""", id="example_21",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can check out more table component examples from the following resources from Flowbite Blocks:'),
    Ul(
        Li(
            A('Advanced tables', href='https://flowbite.com/blocks/application/advanced-tables/')
        ),
        Li(
            A('Table headers', href='https://flowbite.com/blocks/application/table-headers/')
        ),
        Li(
            A('Table footers', href='https://flowbite.com/blocks/application/table-footers/')
        ),
        Li(
            A('Pricing tables', href='https://flowbite.com/blocks/marketing/pricing/')
        )
    ),
    id='mainContent'
)
