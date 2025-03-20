from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('Get started with the rating component to show an aggregate of reviews and scores in the forms of stars or numbers using the utility classes from Tailwind CSS and components from Flowbite.'),
    P('You can find multiple examples on this page including different styles, sizes, and variants of the rating component and other associated elements such as a comment or card.'),
    H2(
        'Default rating',
        Span(id='default-rating', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default rating', href='#default-rating', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this simple example of a star rating component for showing review results.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 ms-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Rating with text',
        Span(id='rating-with-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Rating with text', href='#rating-with-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you also want to show a text near the stars you can use this example as a reference.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-gray-300 me-1 dark:text-gray-500'
        ),
        P('4.95', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('out of', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('5', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-gray-300 me-1 dark:text-gray-500'
        ),
        P('4.95', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('out of', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('5', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Rating count',
        Span(id='rating-count', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Rating count', href='#rating-count', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Aggregate more results by using this example to show the amount of reviews and the average score.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        P('4.95', cls='ms-2 text-sm font-bold text-gray-900 dark:text-white'),
        Span(cls='w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400'),
        A('73 reviews', href='#', cls='text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white'),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        P('4.95', cls='ms-2 text-sm font-bold text-gray-900 dark:text-white'),
        Span(cls='w-1 h-1 mx-1.5 bg-gray-500 rounded-full dark:bg-gray-400'),
        A('73 reviews', href='#', cls='text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white'),
        cls='flex items-center'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Star sizes',
        Span(id='star-sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Star sizes', href='#star-sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Check out the different sizing options for the star review component from small, medium, and large.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center mb-5'
    ),
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center mb-5'
    ),
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 ms-1 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center mb-5'
    ),
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-6 h-6 ms-2 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center mb-5'
    ),
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-yellow-300'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-8 h-8 ms-3 text-gray-300 dark:text-gray-500'
        ),
        cls='flex items-center'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Advanced rating',
        Span(id='advanced-rating', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Advanced rating', href='#advanced-rating', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This advanced rating component can be used to also show how many reviews have been posted for each star rating (eg. 4% for the 2 star ratings, 17% for 4 star rating etc).'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-gray-300 me-1 dark:text-gray-500'
        ),
        P('4.95', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('out of', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('5', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mb-2'
    ),
    P('1,745 global ratings', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
    Div(
        A('5 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 70%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('70%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('4 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 17%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('17%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('3 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 8%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('8%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('2 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 4%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('4%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('1 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 1%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('1%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-yellow-300 me-1'
        ),
        Svg(
            Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 22 20',
            cls='w-4 h-4 text-gray-300 me-1 dark:text-gray-500'
        ),
        P('4.95', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('out of', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        P('5', cls='ms-1 text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mb-2'
    ),
    P('1,745 global ratings', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
    Div(
        A('5 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 70%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('70%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('4 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 17%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('17%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('3 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 8%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('8%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('2 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 4%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('4%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    ),
    Div(
        A('1 star', href='#', cls='text-sm font-medium text-primary-600 dark:text-primary-500 hover:underline'),
        Div(
            Div(style='width: 1%', cls='h-5 bg-yellow-300 rounded-sm'),
            cls='w-2/4 h-5 mx-4 bg-gray-200 rounded-sm dark:bg-gray-700'
        ),
        Span('1%', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        cls='flex items-center mt-4'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Score rating',
        Span(id='score-rating', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Score rating', href='#score-rating', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to break up a general rating score into multiple categories using progress bars.'),
    component_showcase(Div(
    Div(
        P('8.7', cls='bg-primary-100 text-primary-800 text-sm font-semibold inline-flex items-center p-1.5 rounded-sm dark:bg-primary-200 dark:text-primary-800'),
        P('Excellent', cls='ms-2 font-medium text-gray-900 dark:text-white'),
        Span(cls='w-1 h-1 mx-2 bg-gray-900 rounded-full dark:bg-gray-500'),
        P('376 reviews', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        A('Read all reviews', href='#', cls='ms-auto text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
        cls='flex items-center mb-5'
    ),
    Div(
        Div(
            Dl(
                Dt('Staff', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 88%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.8', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Comfort', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Free WiFi', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 88%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.8', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Facilities', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 54%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('5.4', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center'
                )
            )
        ),
        Div(
            Dl(
                Dt('Value for money', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Cleanliness', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 70%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('7.0', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Location', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center'
                )
            )
        ),
        cls='gap-8 sm:grid sm:grid-cols-2'
    )
), code="""Div(
    Div(
        P('8.7', cls='bg-primary-100 text-primary-800 text-sm font-semibold inline-flex items-center p-1.5 rounded-sm dark:bg-primary-200 dark:text-primary-800'),
        P('Excellent', cls='ms-2 font-medium text-gray-900 dark:text-white'),
        Span(cls='w-1 h-1 mx-2 bg-gray-900 rounded-full dark:bg-gray-500'),
        P('376 reviews', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
        A('Read all reviews', href='#', cls='ms-auto text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
        cls='flex items-center mb-5'
    ),
    Div(
        Div(
            Dl(
                Dt('Staff', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 88%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.8', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Comfort', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Free WiFi', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 88%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.8', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Facilities', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 54%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('5.4', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center'
                )
            )
        ),
        Div(
            Dl(
                Dt('Value for money', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Cleanliness', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 70%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('7.0', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center mb-3'
                )
            ),
            Dl(
                Dt('Location', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                Dd(
                    Div(
                        Div(style='width: 89%', cls='bg-primary-600 h-2.5 rounded-sm dark:bg-primary-500'),
                        cls='w-full bg-gray-200 rounded-sm h-2.5 dark:bg-gray-700 me-2'
                    ),
                    Span('8.9', cls='text-sm font-medium text-gray-500 dark:text-gray-400'),
                    cls='flex items-center'
                )
            )
        ),
        cls='gap-8 sm:grid sm:grid-cols-2'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Rating comment',
        Span(id='rating-comment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Rating comment', href='#rating-comment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show a single rating comment and its score alongside other components such as the user profile avatar, name, post date, and more.'),
    component_showcase(Div(
    Article(
        Div(
            Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-10 h-10 me-4 rounded-full'),
            Div(
                P(
                    'Jese Leos',
                    Time('Joined on August 2014', datetime='2014-08-16 19:00', cls='block text-sm text-gray-500 dark:text-gray-400')
                ),
                cls='font-medium dark:text-white'
            ),
            cls='flex items-center mb-4'
        ),
        Div(
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-gray-300 dark:text-gray-500'
            ),
            H3('Thinking to buy another one!', cls='ms-2 text-sm font-semibold text-gray-900 dark:text-white'),
            cls='flex items-center mb-1 space-x-1 rtl:space-x-reverse'
        ),
        Footer(
            P(
                'Reviewed in the United Kingdom on',
                Time('March 3, 2017', datetime='2017-03-03 19:00')
            ),
            cls='mb-5 text-sm text-gray-500 dark:text-gray-400'
        ),
        P('This is my third Invicta Pro Diver. They are just fantastic value for money. This one arrived yesterday and the first thing I did was set the time, popped on an identical strap from another Invicta and went in the shower with it to test the waterproofing.... No problems.', cls='mb-2 text-gray-500 dark:text-gray-400'),
        P('It is obviously not the same build quality as those very expensive watches. But that is like comparing a CitroÃ«n to a Ferrari. This watch was well under Â£100! An absolute bargain.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        A('Read more', href='#', cls='block mb-5 text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
        Aside(
            P('19 people found this helpful', cls='mt-1 text-xs text-gray-500 dark:text-gray-400'),
            Div(
                A('Helpful', href='#', cls='px-2 py-1.5 text-xs font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                A('Report abuse', href='#', cls='ps-4 text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 border-gray-200 ms-4 border-s md:mb-0 dark:border-gray-600'),
                cls='flex items-center mt-3'
            )
        )
    )
), code="""Div(
    Article(
        Div(
            Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-10 h-10 me-4 rounded-full'),
            Div(
                P(
                    'Jese Leos',
                    Time('Joined on August 2014', datetime='2014-08-16 19:00', cls='block text-sm text-gray-500 dark:text-gray-400')
                ),
                cls='font-medium dark:text-white'
            ),
            cls='flex items-center mb-4'
        ),
        Div(
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-yellow-300'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-4 h-4 text-gray-300 dark:text-gray-500'
            ),
            H3('Thinking to buy another one!', cls='ms-2 text-sm font-semibold text-gray-900 dark:text-white'),
            cls='flex items-center mb-1 space-x-1 rtl:space-x-reverse'
        ),
        Footer(
            P(
                'Reviewed in the United Kingdom on',
                Time('March 3, 2017', datetime='2017-03-03 19:00')
            ),
            cls='mb-5 text-sm text-gray-500 dark:text-gray-400'
        ),
        P('This is my third Invicta Pro Diver. They are just fantastic value for money. This one arrived yesterday and the first thing I did was set the time, popped on an identical strap from another Invicta and went in the shower with it to test the waterproofing.... No problems.', cls='mb-2 text-gray-500 dark:text-gray-400'),
        P('It is obviously not the same build quality as those very expensive watches. But that is like comparing a CitroÃ«n to a Ferrari. This watch was well under Â£100! An absolute bargain.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        A('Read more', href='#', cls='block mb-5 text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'),
        Aside(
            P('19 people found this helpful', cls='mt-1 text-xs text-gray-500 dark:text-gray-400'),
            Div(
                A('Helpful', href='#', cls='px-2 py-1.5 text-xs font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                A('Report abuse', href='#', cls='ps-4 text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 border-gray-200 ms-4 border-s md:mb-0 dark:border-gray-600'),
                cls='flex items-center mt-3'
            )
        )
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Review content',
        Span(id='review-content', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Review content', href='#review-content', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show the review content from a user alongside the avatar, location, details, and the score inside a card element.'),
    component_showcase(Div(
    Article(
        Div(
            Div(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-10 h-10 rounded-full'),
                Div(
                    P('Jese Leos'),
                    Div(
                        Svg(
                            Rect(x='0.0531311', width='17', height='12.1429', rx='2', fill='white'),
                            Mask(
                                Rect(x='0.0531311', width='17', height='12.1429', rx='2', fill='white'),
                                id='mask0_3885_33060',
                                style='mask-type:alpha',
                                maskunits='userSpaceOnUse',
                                x='0',
                                y='0',
                                width='18',
                                height='13'
                            ),
                            G(
                                Path(fill_rule='evenodd', clip_rule='evenodd', d='M17.0531 0H0.0531311V0.809524H17.0531V0ZM17.0531 1.61905H0.0531311V2.42857H17.0531V1.61905ZM0.0531311 3.2381H17.0531V4.04762H0.0531311V3.2381ZM17.0531 4.85714H0.0531311V5.66667H17.0531V4.85714ZM0.0531311 6.47619H17.0531V7.28572H0.0531311V6.47619ZM17.0531 8.09524H0.0531311V8.90476H17.0531V8.09524ZM0.0531311 9.71429H17.0531V10.5238H0.0531311V9.71429ZM17.0531 11.3333H0.0531311V12.1429H17.0531V11.3333Z', fill='#D02F44'),
                                Rect(x='0.0531311', width='7.28571', height='5.66667', fill='#46467F'),
                                G(
                                    Path(fill_rule='evenodd', clip_rule='evenodd', d='M1.67216 1.21427C1.67216 1.43782 1.49095 1.61903 1.2674 1.61903C1.04386 1.61903 0.86264 1.43782 0.86264 1.21427C0.86264 0.990727 1.04386 0.809509 1.2674 0.809509C1.49095 0.809509 1.67216 0.990727 1.67216 1.21427ZM3.29121 1.21427C3.29121 1.43782 3.10999 1.61903 2.88645 1.61903C2.66291 1.61903 2.48169 1.43782 2.48169 1.21427C2.48169 0.990727 2.66291 0.809509 2.88645 0.809509C3.10999 0.809509 3.29121 0.990727 3.29121 1.21427ZM4.5055 1.61903C4.72904 1.61903 4.91026 1.43782 4.91026 1.21427C4.91026 0.990727 4.72904 0.809509 4.5055 0.809509C4.28195 0.809509 4.10074 0.990727 4.10074 1.21427C4.10074 1.43782 4.28195 1.61903 4.5055 1.61903ZM6.52931 1.21427C6.52931 1.43782 6.34809 1.61903 6.12455 1.61903C5.901 1.61903 5.71978 1.43782 5.71978 1.21427C5.71978 0.990727 5.901 0.809509 6.12455 0.809509C6.34809 0.809509 6.52931 0.990727 6.52931 1.21427ZM2.07693 2.42856C2.30047 2.42856 2.48169 2.24734 2.48169 2.0238C2.48169 1.80025 2.30047 1.61903 2.07693 1.61903C1.85338 1.61903 1.67216 1.80025 1.67216 2.0238C1.67216 2.24734 1.85338 2.42856 2.07693 2.42856ZM4.10074 2.0238C4.10074 2.24734 3.91952 2.42856 3.69597 2.42856C3.47243 2.42856 3.29121 2.24734 3.29121 2.0238C3.29121 1.80025 3.47243 1.61903 3.69597 1.61903C3.91952 1.61903 4.10074 1.80025 4.10074 2.0238ZM5.31502 2.42856C5.53856 2.42856 5.71978 2.24734 5.71978 2.0238C5.71978 1.80025 5.53856 1.61903 5.31502 1.61903C5.09148 1.61903 4.91026 1.80025 4.91026 2.0238C4.91026 2.24734 5.09148 2.42856 5.31502 2.42856ZM6.52931 2.83332C6.52931 3.05686 6.34809 3.23808 6.12455 3.23808C5.901 3.23808 5.71978 3.05686 5.71978 2.83332C5.71978 2.60978 5.901 2.42856 6.12455 2.42856C6.34809 2.42856 6.52931 2.60978 6.52931 2.83332ZM4.5055 3.23808C4.72904 3.23808 4.91026 3.05686 4.91026 2.83332C4.91026 2.60978 4.72904 2.42856 4.5055 2.42856C4.28195 2.42856 4.10074 2.60978 4.10074 2.83332C4.10074 3.05686 4.28195 3.23808 4.5055 3.23808ZM3.29121 2.83332C3.29121 3.05686 3.10999 3.23808 2.88645 3.23808C2.66291 3.23808 2.48169 3.05686 2.48169 2.83332C2.48169 2.60978 2.66291 2.42856 2.88645 2.42856C3.10999 2.42856 3.29121 2.60978 3.29121 2.83332ZM1.2674 3.23808C1.49095 3.23808 1.67216 3.05686 1.67216 2.83332C1.67216 2.60978 1.49095 2.42856 1.2674 2.42856C1.04386 2.42856 0.86264 2.60978 0.86264 2.83332C0.86264 3.05686 1.04386 3.23808 1.2674 3.23808ZM2.48169 3.64284C2.48169 3.86639 2.30047 4.04761 2.07693 4.04761C1.85338 4.04761 1.67216 3.86639 1.67216 3.64284C1.67216 3.4193 1.85338 3.23808 2.07693 3.23808C2.30047 3.23808 2.48169 3.4193 2.48169 3.64284ZM3.69597 4.04761C3.91952 4.04761 4.10074 3.86639 4.10074 3.64284C4.10074 3.4193 3.91952 3.23808 3.69597 3.23808C3.47243 3.23808 3.29121 3.4193 3.29121 3.64284C3.29121 3.86639 3.47243 4.04761 3.69597 4.04761ZM5.71978 3.64284C5.71978 3.86639 5.53856 4.04761 5.31502 4.04761C5.09148 4.04761 4.91026 3.86639 4.91026 3.64284C4.91026 3.4193 5.09148 3.23808 5.31502 3.23808C5.53856 3.23808 5.71978 3.4193 5.71978 3.64284ZM6.12455 4.85713C6.34809 4.85713 6.52931 4.67591 6.52931 4.45237C6.52931 4.22882 6.34809 4.04761 6.12455 4.04761C5.901 4.04761 5.71978 4.22882 5.71978 4.45237C5.71978 4.67591 5.901 4.85713 6.12455 4.85713ZM4.91026 4.45237C4.91026 4.67591 4.72904 4.85713 4.5055 4.85713C4.28195 4.85713 4.10074 4.67591 4.10074 4.45237C4.10074 4.22882 4.28195 4.04761 4.5055 4.04761C4.72904 4.04761 4.91026 4.22882 4.91026 4.45237ZM2.88645 4.85713C3.10999 4.85713 3.29121 4.67591 3.29121 4.45237C3.29121 4.22882 3.10999 4.04761 2.88645 4.04761C2.66291 4.04761 2.48169 4.22882 2.48169 4.45237C2.48169 4.67591 2.66291 4.85713 2.88645 4.85713ZM1.67216 4.45237C1.67216 4.67591 1.49095 4.85713 1.2674 4.85713C1.04386 4.85713 0.86264 4.67591 0.86264 4.45237C0.86264 4.22882 1.04386 4.04761 1.2674 4.04761C1.49095 4.04761 1.67216 4.22882 1.67216 4.45237Z', fill='url(#paint0_linear_3885_33060)'),
                                    filter='url(#filter0_d_3885_33060)'
                                ),
                                mask='url(#mask0_3885_33060)'
                            ),
                            Defs(
                                Filter(
                                    Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                    Fecolormatrix(in='SourceAlpha', type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0', result='hardAlpha'),
                                    Feoffset(dy='1'),
                                    Fecolormatrix(type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                    Feblend(mode='normal', in2='BackgroundImageFix', result='effect1_dropShadow_3885_33060'),
                                    Feblend(mode='normal', in='SourceGraphic', in2='effect1_dropShadow_3885_33060', result='shape'),
                                    id='filter0_d_3885_33060',
                                    x='0.86264',
                                    y='0.809509',
                                    width='5.66666',
                                    height='5.04761',
                                    filterunits='userSpaceOnUse',
                                    color_interpolation_filters='sRGB'
                                ),
                                Lineargradient(
                                    Stop(stop_color='white'),
                                    Stop(offset='1', stop_color='#F0F0F0'),
                                    id='paint0_linear_3885_33060',
                                    x1='0.86264',
                                    y1='0.809509',
                                    x2='0.86264',
                                    y2='4.85713',
                                    gradientunits='userSpaceOnUse'
                                )
                            ),
                            aria_hidden='true',
                            viewbox='0 0 18 13',
                            fill='none',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-5 me-1.5'
                        ),
                        'United States',
                        cls='flex items-center text-sm text-gray-500 dark:text-gray-400'
                    ),
                    cls='ms-4 font-medium dark:text-white'
                ),
                cls='flex items-center mb-6'
            ),
            Ul(
                Li(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M4 15V9m4 6V9m4 6V9m4 6V9M2 16h16M1 19h18M2 7v1h16V7l-8-6-8 6Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2'
                    ),
                    'Apartament with city view',
                    cls='flex items-center'
                ),
                Li(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2'
                    ),
                    '3 nights December 2021',
                    cls='flex items-center'
                ),
                Li(
                    Svg(
                        Path(d='M14.5 0A3.987 3.987 0 0 0 11 2.1a4.977 4.977 0 0 1 3.9 5.858A3.989 3.989 0 0 0 14.5 0ZM9 13h2a4 4 0 0 1 4 4v2H5v-2a4 4 0 0 1 4-4Z'),
                        Path(d='M5 19h10v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2ZM5 7a5.008 5.008 0 0 1 4-4.9 3.988 3.988 0 1 0-3.9 5.859A4.974 4.974 0 0 1 5 7Zm5 3a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm5-1h-.424a5.016 5.016 0 0 1-1.942 2.232A6.007 6.007 0 0 1 17 17h2a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5ZM5.424 9H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h2a6.007 6.007 0 0 1 4.366-5.768A5.016 5.016 0 0 1 5.424 9Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 19',
                        cls='w-3 h-3 me-2'
                    ),
                    'Family',
                    cls='flex items-center'
                ),
                cls='space-y-4 text-sm text-gray-500 dark:text-gray-400'
            )
        ),
        Div(
            Div(
                Div(
                    Footer(
                        P(
                            'Reviewed:',
                            Time('January 20, 2022', datetime='2022-01-20 19:00'),
                            cls='mb-2 text-sm text-gray-500 dark:text-gray-400'
                        )
                    ),
                    H4('Spotless, good appliances, excellent layout, host was genuinely nice and helpful.', cls='text-xl font-bold text-gray-900 dark:text-white'),
                    cls='pe-4'
                ),
                P('8.7', cls='bg-primary-700 text-white text-sm font-semibold inline-flex items-center p-1.5 rounded-sm'),
                cls='flex items-start mb-5'
            ),
            P("The flat was spotless, very comfortable, and the host was amazing. I highly recommend this accommodation for anyone visiting New York city centre. It's quite a while since we are no longer using hotel facilities but self contained places. And the main reason is poor cleanliness and staff not being trained properly. This place exceeded our expectation and will return for sure.", cls='mb-2 text-gray-500 dark:text-gray-400'),
            P('It is obviously not the same build quality as those very expensive watches. But that is like comparing a CitroÃ«n to a Ferrari. This watch was well under Â£100! An absolute bargain.', cls='mb-5 text-gray-500 dark:text-gray-400'),
            Aside(
                A(
                    Svg(
                        Path(d='M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5 me-2.5'
                    ),
                    'Helpful',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'
                ),
                A(
                    Svg(
                        Path(d='M11.955 2.117h-.114C9.732 1.535 6.941.5 4.356.5c-1.4 0-1.592.526-1.879 1.316l-2.355 7A2 2 0 0 0 2 11.5h3.956L4.4 16a1.779 1.779 0 0 0 3.332 1.061 24.8 24.8 0 0 1 4.226-5.36l-.003-9.584ZM15 11h2a1 1 0 0 0 1-1V2a2 2 0 1 0-4 0v8a1 1 0 0 0 1 1Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5 me-2.5'
                    ),
                    'Not helpful',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 group ms-5'
                ),
                cls='flex items-center mt-3'
            ),
            cls='col-span-2 mt-6 md:mt-0'
        ),
        cls='md:gap-8 md:grid md:grid-cols-3'
    )
), code="""Div(
    Article(
        Div(
            Div(
                Img(src='/docs/images/people/profile-picture-5.jpg', alt=True, cls='w-10 h-10 rounded-full'),
                Div(
                    P('Jese Leos'),
                    Div(
                        Svg(
                            Rect(x='0.0531311', width='17', height='12.1429', rx='2', fill='white'),
                            Mask(
                                Rect(x='0.0531311', width='17', height='12.1429', rx='2', fill='white'),
                                id='mask0_3885_33060',
                                style='mask-type:alpha',
                                maskunits='userSpaceOnUse',
                                x='0',
                                y='0',
                                width='18',
                                height='13'
                            ),
                            G(
                                Path(fill_rule='evenodd', clip_rule='evenodd', d='M17.0531 0H0.0531311V0.809524H17.0531V0ZM17.0531 1.61905H0.0531311V2.42857H17.0531V1.61905ZM0.0531311 3.2381H17.0531V4.04762H0.0531311V3.2381ZM17.0531 4.85714H0.0531311V5.66667H17.0531V4.85714ZM0.0531311 6.47619H17.0531V7.28572H0.0531311V6.47619ZM17.0531 8.09524H0.0531311V8.90476H17.0531V8.09524ZM0.0531311 9.71429H17.0531V10.5238H0.0531311V9.71429ZM17.0531 11.3333H0.0531311V12.1429H17.0531V11.3333Z', fill='#D02F44'),
                                Rect(x='0.0531311', width='7.28571', height='5.66667', fill='#46467F'),
                                G(
                                    Path(fill_rule='evenodd', clip_rule='evenodd', d='M1.67216 1.21427C1.67216 1.43782 1.49095 1.61903 1.2674 1.61903C1.04386 1.61903 0.86264 1.43782 0.86264 1.21427C0.86264 0.990727 1.04386 0.809509 1.2674 0.809509C1.49095 0.809509 1.67216 0.990727 1.67216 1.21427ZM3.29121 1.21427C3.29121 1.43782 3.10999 1.61903 2.88645 1.61903C2.66291 1.61903 2.48169 1.43782 2.48169 1.21427C2.48169 0.990727 2.66291 0.809509 2.88645 0.809509C3.10999 0.809509 3.29121 0.990727 3.29121 1.21427ZM4.5055 1.61903C4.72904 1.61903 4.91026 1.43782 4.91026 1.21427C4.91026 0.990727 4.72904 0.809509 4.5055 0.809509C4.28195 0.809509 4.10074 0.990727 4.10074 1.21427C4.10074 1.43782 4.28195 1.61903 4.5055 1.61903ZM6.52931 1.21427C6.52931 1.43782 6.34809 1.61903 6.12455 1.61903C5.901 1.61903 5.71978 1.43782 5.71978 1.21427C5.71978 0.990727 5.901 0.809509 6.12455 0.809509C6.34809 0.809509 6.52931 0.990727 6.52931 1.21427ZM2.07693 2.42856C2.30047 2.42856 2.48169 2.24734 2.48169 2.0238C2.48169 1.80025 2.30047 1.61903 2.07693 1.61903C1.85338 1.61903 1.67216 1.80025 1.67216 2.0238C1.67216 2.24734 1.85338 2.42856 2.07693 2.42856ZM4.10074 2.0238C4.10074 2.24734 3.91952 2.42856 3.69597 2.42856C3.47243 2.42856 3.29121 2.24734 3.29121 2.0238C3.29121 1.80025 3.47243 1.61903 3.69597 1.61903C3.91952 1.61903 4.10074 1.80025 4.10074 2.0238ZM5.31502 2.42856C5.53856 2.42856 5.71978 2.24734 5.71978 2.0238C5.71978 1.80025 5.53856 1.61903 5.31502 1.61903C5.09148 1.61903 4.91026 1.80025 4.91026 2.0238C4.91026 2.24734 5.09148 2.42856 5.31502 2.42856ZM6.52931 2.83332C6.52931 3.05686 6.34809 3.23808 6.12455 3.23808C5.901 3.23808 5.71978 3.05686 5.71978 2.83332C5.71978 2.60978 5.901 2.42856 6.12455 2.42856C6.34809 2.42856 6.52931 2.60978 6.52931 2.83332ZM4.5055 3.23808C4.72904 3.23808 4.91026 3.05686 4.91026 2.83332C4.91026 2.60978 4.72904 2.42856 4.5055 2.42856C4.28195 2.42856 4.10074 2.60978 4.10074 2.83332C4.10074 3.05686 4.28195 3.23808 4.5055 3.23808ZM3.29121 2.83332C3.29121 3.05686 3.10999 3.23808 2.88645 3.23808C2.66291 3.23808 2.48169 3.05686 2.48169 2.83332C2.48169 2.60978 2.66291 2.42856 2.88645 2.42856C3.10999 2.42856 3.29121 2.60978 3.29121 2.83332ZM1.2674 3.23808C1.49095 3.23808 1.67216 3.05686 1.67216 2.83332C1.67216 2.60978 1.49095 2.42856 1.2674 2.42856C1.04386 2.42856 0.86264 2.60978 0.86264 2.83332C0.86264 3.05686 1.04386 3.23808 1.2674 3.23808ZM2.48169 3.64284C2.48169 3.86639 2.30047 4.04761 2.07693 4.04761C1.85338 4.04761 1.67216 3.86639 1.67216 3.64284C1.67216 3.4193 1.85338 3.23808 2.07693 3.23808C2.30047 3.23808 2.48169 3.4193 2.48169 3.64284ZM3.69597 4.04761C3.91952 4.04761 4.10074 3.86639 4.10074 3.64284C4.10074 3.4193 3.91952 3.23808 3.69597 3.23808C3.47243 3.23808 3.29121 3.4193 3.29121 3.64284C3.29121 3.86639 3.47243 4.04761 3.69597 4.04761ZM5.71978 3.64284C5.71978 3.86639 5.53856 4.04761 5.31502 4.04761C5.09148 4.04761 4.91026 3.86639 4.91026 3.64284C4.91026 3.4193 5.09148 3.23808 5.31502 3.23808C5.53856 3.23808 5.71978 3.4193 5.71978 3.64284ZM6.12455 4.85713C6.34809 4.85713 6.52931 4.67591 6.52931 4.45237C6.52931 4.22882 6.34809 4.04761 6.12455 4.04761C5.901 4.04761 5.71978 4.22882 5.71978 4.45237C5.71978 4.67591 5.901 4.85713 6.12455 4.85713ZM4.91026 4.45237C4.91026 4.67591 4.72904 4.85713 4.5055 4.85713C4.28195 4.85713 4.10074 4.67591 4.10074 4.45237C4.10074 4.22882 4.28195 4.04761 4.5055 4.04761C4.72904 4.04761 4.91026 4.22882 4.91026 4.45237ZM2.88645 4.85713C3.10999 4.85713 3.29121 4.67591 3.29121 4.45237C3.29121 4.22882 3.10999 4.04761 2.88645 4.04761C2.66291 4.04761 2.48169 4.22882 2.48169 4.45237C2.48169 4.67591 2.66291 4.85713 2.88645 4.85713ZM1.67216 4.45237C1.67216 4.67591 1.49095 4.85713 1.2674 4.85713C1.04386 4.85713 0.86264 4.67591 0.86264 4.45237C0.86264 4.22882 1.04386 4.04761 1.2674 4.04761C1.49095 4.04761 1.67216 4.22882 1.67216 4.45237Z', fill='url(#paint0_linear_3885_33060)'),
                                    filter='url(#filter0_d_3885_33060)'
                                ),
                                mask='url(#mask0_3885_33060)'
                            ),
                            Defs(
                                Filter(
                                    Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                    Fecolormatrix(in='SourceAlpha', type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0', result='hardAlpha'),
                                    Feoffset(dy='1'),
                                    Fecolormatrix(type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                    Feblend(mode='normal', in2='BackgroundImageFix', result='effect1_dropShadow_3885_33060'),
                                    Feblend(mode='normal', in='SourceGraphic', in2='effect1_dropShadow_3885_33060', result='shape'),
                                    id='filter0_d_3885_33060',
                                    x='0.86264',
                                    y='0.809509',
                                    width='5.66666',
                                    height='5.04761',
                                    filterunits='userSpaceOnUse',
                                    color_interpolation_filters='sRGB'
                                ),
                                Lineargradient(
                                    Stop(stop_color='white'),
                                    Stop(offset='1', stop_color='#F0F0F0'),
                                    id='paint0_linear_3885_33060',
                                    x1='0.86264',
                                    y1='0.809509',
                                    x2='0.86264',
                                    y2='4.85713',
                                    gradientunits='userSpaceOnUse'
                                )
                            ),
                            aria_hidden='true',
                            viewbox='0 0 18 13',
                            fill='none',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='w-5 me-1.5'
                        ),
                        'United States',
                        cls='flex items-center text-sm text-gray-500 dark:text-gray-400'
                    ),
                    cls='ms-4 font-medium dark:text-white'
                ),
                cls='flex items-center mb-6'
            ),
            Ul(
                Li(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M4 15V9m4 6V9m4 6V9m4 6V9M2 16h16M1 19h18M2 7v1h16V7l-8-6-8 6Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2'
                    ),
                    'Apartament with city view',
                    cls='flex items-center'
                ),
                Li(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2'
                    ),
                    '3 nights December 2021',
                    cls='flex items-center'
                ),
                Li(
                    Svg(
                        Path(d='M14.5 0A3.987 3.987 0 0 0 11 2.1a4.977 4.977 0 0 1 3.9 5.858A3.989 3.989 0 0 0 14.5 0ZM9 13h2a4 4 0 0 1 4 4v2H5v-2a4 4 0 0 1 4-4Z'),
                        Path(d='M5 19h10v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2ZM5 7a5.008 5.008 0 0 1 4-4.9 3.988 3.988 0 1 0-3.9 5.859A4.974 4.974 0 0 1 5 7Zm5 3a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm5-1h-.424a5.016 5.016 0 0 1-1.942 2.232A6.007 6.007 0 0 1 17 17h2a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5ZM5.424 9H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h2a6.007 6.007 0 0 1 4.366-5.768A5.016 5.016 0 0 1 5.424 9Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 19',
                        cls='w-3 h-3 me-2'
                    ),
                    'Family',
                    cls='flex items-center'
                ),
                cls='space-y-4 text-sm text-gray-500 dark:text-gray-400'
            )
        ),
        Div(
            Div(
                Div(
                    Footer(
                        P(
                            'Reviewed:',
                            Time('January 20, 2022', datetime='2022-01-20 19:00'),
                            cls='mb-2 text-sm text-gray-500 dark:text-gray-400'
                        )
                    ),
                    H4('Spotless, good appliances, excellent layout, host was genuinely nice and helpful.', cls='text-xl font-bold text-gray-900 dark:text-white'),
                    cls='pe-4'
                ),
                P('8.7', cls='bg-primary-700 text-white text-sm font-semibold inline-flex items-center p-1.5 rounded-sm'),
                cls='flex items-start mb-5'
            ),
            P("The flat was spotless, very comfortable, and the host was amazing. I highly recommend this accommodation for anyone visiting New York city centre. It's quite a while since we are no longer using hotel facilities but self contained places. And the main reason is poor cleanliness and staff not being trained properly. This place exceeded our expectation and will return for sure.", cls='mb-2 text-gray-500 dark:text-gray-400'),
            P('It is obviously not the same build quality as those very expensive watches. But that is like comparing a CitroÃ«n to a Ferrari. This watch was well under Â£100! An absolute bargain.', cls='mb-5 text-gray-500 dark:text-gray-400'),
            Aside(
                A(
                    Svg(
                        Path(d='M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5 me-2.5'
                    ),
                    'Helpful',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-primary-600 hover:underline dark:text-primary-500'
                ),
                A(
                    Svg(
                        Path(d='M11.955 2.117h-.114C9.732 1.535 6.941.5 4.356.5c-1.4 0-1.592.526-1.879 1.316l-2.355 7A2 2 0 0 0 2 11.5h3.956L4.4 16a1.779 1.779 0 0 0 3.332 1.061 24.8 24.8 0 0 1 4.226-5.36l-.003-9.584ZM15 11h2a1 1 0 0 0 1-1V2a2 2 0 1 0-4 0v8a1 1 0 0 0 1 1Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 18',
                        cls='w-3.5 h-3.5 me-2.5'
                    ),
                    'Not helpful',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-primary-600 hover:underline dark:text-primary-500 group ms-5'
                ),
                cls='flex items-center mt-3'
            ),
            cls='col-span-2 mt-6 md:mt-0'
        ),
        cls='md:gap-8 md:grid md:grid-cols-3'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    id='mainContent'
)
