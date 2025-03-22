from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The search input component can be used to let your users search through your website using string queries and it comes in multiple styles, variants, and sizes built with the utility classes from Tailwind CSS.'),
    P('You will also find more advanced search components on this page including dropdown category selections, search buttons positioned inside the input field, voice search fields and more.'),
    H2(
        'Search bar example',
        Span(id='search-bar-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Search bar example', href='#search-bar-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with the default example of a search input component including and icon and submit button.'),
    component_showcase(Div(
    Form(
        Label('Search', fr='default-search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='search', id='default-search', placeholder='Search Mockups, Logos...', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button('Search', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
            cls='relative'
        ),
        cls='max-w-md mx-auto'
    )
), code="""Div(
    Form(
        Label('Search', fr='default-search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
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
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='search', id='default-search', placeholder='Search Mockups, Logos...', required=True, cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button('Search', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
            cls='relative'
        ),
        cls='max-w-md mx-auto'
    )
)""", id="example_0",cls='mt-2 mb-6'),
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
        'Search with dropdown',
        Span(id='search-with-dropdown', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Search with dropdown', href='#search-with-dropdown', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this search component with a dropdown to let your users select a category in which they would like the search query to be targeted in.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Your Email', fr='search-dropdown', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                'All categories',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button',
                data_dropdown_toggle='dropdown',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('Mockups', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Templates', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Design', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Logos', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='search-dropdown', placeholder='Search Mockups, Logos, Design Templates...', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    Span('Search', cls='sr-only'),
                    type='submit',
                    cls='absolute top-0 end-0 p-2.5 text-sm font-medium h-full text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        ),
        cls='max-w-lg mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Label('Your Email', fr='search-dropdown', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                'All categories',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button',
                data_dropdown_toggle='dropdown',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('Mockups', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Templates', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Design', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Logos', type='button', cls='inline-flex w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='search-dropdown', placeholder='Search Mockups, Logos, Design Templates...', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    Span('Search', cls='sr-only'),
                    type='submit',
                    cls='absolute top-0 end-0 p-2.5 text-sm font-medium h-full text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        ),
        cls='max-w-lg mx-auto'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Simple search input',
        Span(id='simple-search-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Simple search input', href='#simple-search-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the simplest form of a search input component with an icon and a search button next to the text field.'),
    component_showcase(Div(
    Form(
        Label('Search', fr='simple-search', cls='sr-only'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='text', id='simple-search', placeholder='Search branch name...', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative w-full'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-4 h-4'
            ),
            Span('Search', cls='sr-only'),
            type='submit',
            cls='p-2.5 ms-2 text-sm font-medium text-white bg-primary-700 rounded-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        ),
        cls='flex items-center max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('Search', fr='simple-search', cls='sr-only'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='text', id='simple-search', placeholder='Search branch name...', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative w-full'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-4 h-4'
            ),
            Span('Search', cls='sr-only'),
            type='submit',
            cls='p-2.5 ms-2 text-sm font-medium text-white bg-primary-700 rounded-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        ),
        cls='flex items-center max-w-sm mx-auto'
    )
)""", id="example_2",cls='mt-2 mb-6'),
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
        'Location search',
        Span(id='location-search', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Location search', href='#location-search', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example where you can select a country in which you want to search for an address or city.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Your Email', fr='location-search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                'USA',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button-2',
                data_dropdown_toggle='dropdown-search-city',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-500 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                Svg(
                                    G(
                                        G(
                                            Path(fill='#bd3d44', d='M0 0h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                            Path(fill='#fff', d='M0 10h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                            stroke_width='1pt'
                                        ),
                                        Path(fill='#192f5d', d='M0 0h98.8v70H0z', transform='scale(3.9385)'),
                                        Path(fill='#fff', d='M8.2 3l1 2.8H12L9.7 7.5l.9 2.7-2.4-1.7L6 10.2l.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7L74 8.5l-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 7.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 24.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 21.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 38.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 35.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 52.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 49.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 66.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 63.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9z', transform='scale(3.9385)'),
                                        fill_rule='evenodd'
                                    ),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-us',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'United States',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Path(fill='#ffce00', d='M0 341.3h512V512H0z'),
                                    Path(d='M0 0h512v170.7H0z'),
                                    Path(fill='#d00', d='M0 170.7h512v170.6H0z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-de',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'Germany',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    G(
                                        Path(fill='#fff', d='M0 0h512v512H0z'),
                                        Path(fill='#009246', d='M0 0h170.7v512H0z'),
                                        Path(fill='#ce2b37', d='M341.3 0H512v512H341.3z'),
                                        fill_rule='evenodd',
                                        stroke_width='1pt'
                                    ),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-it',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'Italy',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Defs(
                                        Path(id='a', fill='#ffde00', d='M1-.3L-.7.8 0-1 .6.8-1-.3z')
                                    ),
                                    Path(fill='#de2910', d='M0 0h512v512H0z'),
                                    Use(width='30', height='20', transform='matrix(76.8 0 0 76.8 128 128)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-121 142.6 -47) scale(25.5827)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-98.1 198 -82) scale(25.6)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-74 272.4 -114) scale(25.6137)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='matrix(16 -19.968 19.968 16 256 230.4)', **{'xlink:href': '#a'}),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-cn',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2',
                                    **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                                ),
                                'China',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-button-2',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-search-city',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='location-search', placeholder='Search for city or address', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    Span('Search', cls='sr-only'),
                    type='submit',
                    cls='absolute top-0 end-0 h-full p-2.5 text-sm font-medium text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        ),
        cls='max-w-md mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Label('Your Email', fr='location-search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Button(
                Svg(
                    Rect(x='0.5', width='14', height='12', rx='2', fill='white'),
                    Mask(
                        Rect(x='0.5', width='14', height='12', rx='2', fill='white'),
                        id='mask0_12694_49953',
                        style='mask-type:alpha',
                        maskunits='userSpaceOnUse',
                        x='0',
                        y='0',
                        width='15',
                        height='12'
                    ),
                    G(
                        Path(fill_rule='evenodd', clip_rule='evenodd', d='M14.5 0H0.5V0.8H14.5V0ZM14.5 1.6H0.5V2.4H14.5V1.6ZM0.5 3.2H14.5V4H0.5V3.2ZM14.5 4.8H0.5V5.6H14.5V4.8ZM0.5 6.4H14.5V7.2H0.5V6.4ZM14.5 8H0.5V8.8H14.5V8ZM0.5 9.6H14.5V10.4H0.5V9.6ZM14.5 11.2H0.5V12H14.5V11.2Z', fill='#D02F44'),
                        Rect(x='0.5', width='6', height='5.6', fill='#46467F'),
                        G(
                            Path(fill_rule='evenodd', clip_rule='evenodd', d='M1.83317 1.20005C1.83317 1.42096 1.68393 1.60005 1.49984 1.60005C1.31574 1.60005 1.1665 1.42096 1.1665 1.20005C1.1665 0.979135 1.31574 0.800049 1.49984 0.800049C1.68393 0.800049 1.83317 0.979135 1.83317 1.20005ZM3.1665 1.20005C3.1665 1.42096 3.01727 1.60005 2.83317 1.60005C2.64908 1.60005 2.49984 1.42096 2.49984 1.20005C2.49984 0.979135 2.64908 0.800049 2.83317 0.800049C3.01727 0.800049 3.1665 0.979135 3.1665 1.20005ZM4.1665 1.60005C4.3506 1.60005 4.49984 1.42096 4.49984 1.20005C4.49984 0.979135 4.3506 0.800049 4.1665 0.800049C3.98241 0.800049 3.83317 0.979135 3.83317 1.20005C3.83317 1.42096 3.98241 1.60005 4.1665 1.60005ZM5.83317 1.20005C5.83317 1.42096 5.68393 1.60005 5.49984 1.60005C5.31574 1.60005 5.1665 1.42096 5.1665 1.20005C5.1665 0.979135 5.31574 0.800049 5.49984 0.800049C5.68393 0.800049 5.83317 0.979135 5.83317 1.20005ZM2.1665 2.40005C2.3506 2.40005 2.49984 2.22096 2.49984 2.00005C2.49984 1.77913 2.3506 1.60005 2.1665 1.60005C1.98241 1.60005 1.83317 1.77913 1.83317 2.00005C1.83317 2.22096 1.98241 2.40005 2.1665 2.40005ZM3.83317 2.00005C3.83317 2.22096 3.68393 2.40005 3.49984 2.40005C3.31574 2.40005 3.1665 2.22096 3.1665 2.00005C3.1665 1.77913 3.31574 1.60005 3.49984 1.60005C3.68393 1.60005 3.83317 1.77913 3.83317 2.00005ZM4.83317 2.40005C5.01726 2.40005 5.1665 2.22096 5.1665 2.00005C5.1665 1.77913 5.01726 1.60005 4.83317 1.60005C4.64908 1.60005 4.49984 1.77913 4.49984 2.00005C4.49984 2.22096 4.64908 2.40005 4.83317 2.40005ZM5.83317 2.80005C5.83317 3.02096 5.68393 3.20005 5.49984 3.20005C5.31574 3.20005 5.1665 3.02096 5.1665 2.80005C5.1665 2.57914 5.31574 2.40005 5.49984 2.40005C5.68393 2.40005 5.83317 2.57914 5.83317 2.80005ZM4.1665 3.20005C4.3506 3.20005 4.49984 3.02096 4.49984 2.80005C4.49984 2.57914 4.3506 2.40005 4.1665 2.40005C3.98241 2.40005 3.83317 2.57914 3.83317 2.80005C3.83317 3.02096 3.98241 3.20005 4.1665 3.20005ZM3.1665 2.80005C3.1665 3.02096 3.01727 3.20005 2.83317 3.20005C2.64908 3.20005 2.49984 3.02096 2.49984 2.80005C2.49984 2.57914 2.64908 2.40005 2.83317 2.40005C3.01727 2.40005 3.1665 2.57914 3.1665 2.80005ZM1.49984 3.20005C1.68393 3.20005 1.83317 3.02096 1.83317 2.80005C1.83317 2.57914 1.68393 2.40005 1.49984 2.40005C1.31574 2.40005 1.1665 2.57914 1.1665 2.80005C1.1665 3.02096 1.31574 3.20005 1.49984 3.20005ZM2.49984 3.60005C2.49984 3.82096 2.3506 4.00005 2.1665 4.00005C1.98241 4.00005 1.83317 3.82096 1.83317 3.60005C1.83317 3.37913 1.98241 3.20005 2.1665 3.20005C2.3506 3.20005 2.49984 3.37913 2.49984 3.60005ZM3.49984 4.00005C3.68393 4.00005 3.83317 3.82096 3.83317 3.60005C3.83317 3.37913 3.68393 3.20005 3.49984 3.20005C3.31574 3.20005 3.1665 3.37913 3.1665 3.60005C3.1665 3.82096 3.31574 4.00005 3.49984 4.00005ZM5.1665 3.60005C5.1665 3.82096 5.01726 4.00005 4.83317 4.00005C4.64908 4.00005 4.49984 3.82096 4.49984 3.60005C4.49984 3.37913 4.64908 3.20005 4.83317 3.20005C5.01726 3.20005 5.1665 3.37913 5.1665 3.60005ZM5.49984 4.80005C5.68393 4.80005 5.83317 4.62096 5.83317 4.40005C5.83317 4.17913 5.68393 4.00005 5.49984 4.00005C5.31574 4.00005 5.1665 4.17913 5.1665 4.40005C5.1665 4.62096 5.31574 4.80005 5.49984 4.80005ZM4.49984 4.40005C4.49984 4.62096 4.3506 4.80005 4.1665 4.80005C3.98241 4.80005 3.83317 4.62096 3.83317 4.40005C3.83317 4.17913 3.98241 4.00005 4.1665 4.00005C4.3506 4.00005 4.49984 4.17913 4.49984 4.40005ZM2.83317 4.80005C3.01727 4.80005 3.1665 4.62096 3.1665 4.40005C3.1665 4.17913 3.01727 4.00005 2.83317 4.00005C2.64908 4.00005 2.49984 4.17913 2.49984 4.40005C2.49984 4.62096 2.64908 4.80005 2.83317 4.80005ZM1.83317 4.40005C1.83317 4.62096 1.68393 4.80005 1.49984 4.80005C1.31574 4.80005 1.1665 4.62096 1.1665 4.40005C1.1665 4.17913 1.31574 4.00005 1.49984 4.00005C1.68393 4.00005 1.83317 4.17913 1.83317 4.40005Z', fill='url(#paint0_linear_12694_49953)'),
                            filter='url(#filter0_d_12694_49953)'
                        ),
                        mask='url(#mask0_12694_49953)'
                    ),
                    Defs(
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0', result='hardAlpha'),
                            Feoffset(dy='1'),
                            Fecolormatrix(type='matrix', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(mode='normal', in2='BackgroundImageFix', result='effect1_dropShadow_12694_49953'),
                            Feblend(mode='normal', in='SourceGraphic', in2='effect1_dropShadow_12694_49953', result='shape'),
                            id='filter0_d_12694_49953',
                            x='1.1665',
                            y='0.800049',
                            width='4.6665',
                            height='5',
                            filterunits='userSpaceOnUse',
                            color_interpolation_filters='sRGB'
                        ),
                        Lineargradient(
                            Stop(stop_color='white'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_12694_49953',
                            x1='1.1665',
                            y1='0.800049',
                            x2='1.1665',
                            y2='4.80005',
                            gradientunits='userSpaceOnUse'
                        )
                    ),
                    aria_hidden='true',
                    viewbox='0 0 15 12',
                    fill='none',
                    xmlns='http://www.w3.org/2000/svg',
                    cls='h-3 me-2'
                ),
                'USA',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-button-2',
                data_dropdown_toggle='dropdown-search-city',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-500 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                Svg(
                                    G(
                                        G(
                                            Path(fill='#bd3d44', d='M0 0h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                            Path(fill='#fff', d='M0 10h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z', transform='scale(3.9385)'),
                                            stroke_width='1pt'
                                        ),
                                        Path(fill='#192f5d', d='M0 0h98.8v70H0z', transform='scale(3.9385)'),
                                        Path(fill='#fff', d='M8.2 3l1 2.8H12L9.7 7.5l.9 2.7-2.4-1.7L6 10.2l.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7L74 8.5l-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 7.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 24.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 21.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 38.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 35.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 52.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 49.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 66.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 63.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9z', transform='scale(3.9385)'),
                                        fill_rule='evenodd'
                                    ),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-us',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'United States',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Path(fill='#ffce00', d='M0 341.3h512V512H0z'),
                                    Path(d='M0 0h512v170.7H0z'),
                                    Path(fill='#d00', d='M0 170.7h512v170.6H0z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-de',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'Germany',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    G(
                                        Path(fill='#fff', d='M0 0h512v512H0z'),
                                        Path(fill='#009246', d='M0 0h170.7v512H0z'),
                                        Path(fill='#ce2b37', d='M341.3 0H512v512H341.3z'),
                                        fill_rule='evenodd',
                                        stroke_width='1pt'
                                    ),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-it',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2'
                                ),
                                'Italy',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Defs(
                                        Path(id='a', fill='#ffde00', d='M1-.3L-.7.8 0-1 .6.8-1-.3z')
                                    ),
                                    Path(fill='#de2910', d='M0 0h512v512H0z'),
                                    Use(width='30', height='20', transform='matrix(76.8 0 0 76.8 128 128)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-121 142.6 -47) scale(25.5827)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-98.1 198 -82) scale(25.6)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='rotate(-74 272.4 -114) scale(25.6137)', **{'xlink:href': '#a'}),
                                    Use(width='30', height='20', transform='matrix(16 -19.968 19.968 16 256 230.4)', **{'xlink:href': '#a'}),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    id='flag-icon-css-cn',
                                    viewbox='0 0 512 512',
                                    cls='h-3.5 w-3.5 rounded-full me-2',
                                    **{'xmlns:xlink': 'http://www.w3.org/1999/xlink'}
                                ),
                                'China',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-button-2',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-search-city',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700'
            ),
            Div(
                Input(type='search', id='location-search', placeholder='Search for city or address', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4'
                    ),
                    Span('Search', cls='sr-only'),
                    type='submit',
                    cls='absolute top-0 end-0 h-full p-2.5 text-sm font-medium text-white bg-primary-700 rounded-e-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                ),
                cls='relative w-full'
            ),
            cls='flex'
        ),
        cls='max-w-md mx-auto'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Voice search',
        Span(id='voice-search', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Voice search', href='#voice-search', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example if you would like to enable voice search for your website and users.'),
    component_showcase(Div(
    Form(
        Label('Search', fr='voice-search', cls='sr-only'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M11.15 5.6h.01m3.337 1.913h.01m-6.979 0h.01M5.541 11h.01M15 15h2.706a1.957 1.957 0 0 0 1.883-1.325A9 9 0 1 0 2.043 11.89 9.1 9.1 0 0 0 7.2 19.1a8.62 8.62 0 0 0 3.769.9A2.013 2.013 0 0 0 13 18v-.857A2.034 2.034 0 0 1 15 15Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 21 21',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='text', id='voice-search', placeholder='Search Mockups, Logos, Design Templates...', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M15 7v3a5.006 5.006 0 0 1-5 5H6a5.006 5.006 0 0 1-5-5V7m7 9v3m-3 0h6M7 1h2a3 3 0 0 1 3 3v5a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V4a3 3 0 0 1 3-3Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'
                ),
                type='button',
                cls='absolute inset-y-0 end-0 flex items-center pe-3'
            ),
            cls='relative w-full'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-4 h-4 me-2'
            ),
            'Search',
            type='submit',
            cls='inline-flex items-center py-2.5 px-3 ms-2 text-sm font-medium text-white bg-primary-700 rounded-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        ),
        cls='flex items-center max-w-lg mx-auto'
    )
), code="""Div(
    Form(
        Label('Search', fr='voice-search', cls='sr-only'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M11.15 5.6h.01m3.337 1.913h.01m-6.979 0h.01M5.541 11h.01M15 15h2.706a1.957 1.957 0 0 0 1.883-1.325A9 9 0 1 0 2.043 11.89 9.1 9.1 0 0 0 7.2 19.1a8.62 8.62 0 0 0 3.769.9A2.013 2.013 0 0 0 13 18v-.857A2.034 2.034 0 0 1 15 15Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 21 21',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'
            ),
            Input(type='text', id='voice-search', placeholder='Search Mockups, Logos, Design Templates...', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M15 7v3a5.006 5.006 0 0 1-5 5H6a5.006 5.006 0 0 1-5-5V7m7 9v3m-3 0h6M7 1h2a3 3 0 0 1 3 3v5a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V4a3 3 0 0 1 3-3Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white'
                ),
                type='button',
                cls='absolute inset-y-0 end-0 flex items-center pe-3'
            ),
            cls='relative w-full'
        ),
        Button(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 20 20',
                cls='w-4 h-4 me-2'
            ),
            'Search',
            type='submit',
            cls='inline-flex items-center py-2.5 px-3 ms-2 text-sm font-medium text-white bg-primary-700 rounded-lg border border-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        ),
        cls='flex items-center max-w-lg mx-auto'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
