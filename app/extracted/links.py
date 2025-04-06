from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('Get started with the link component to enable hyperlinks across pages and external websites applied to elements such as inline text, buttons, cards, inside paragraphs, and more.'),
    P('Hyperlinks are a great way to reduce bounce rate of the current page and encourage visitors to browse your website and become a returning user.'),
    H2(
        'Default link',
        Span(id='default-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default link', href='#default-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to set default styles to an inline link element.'),
    component_showcase(Div(
    A('Read more', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline')
), code="""Div(
    A('Read more', href='#', cls='font-medium text-primary-600 dark:text-primary-500 hover:underline')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Button',
        Span(id='button', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Button', href='#button', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to set a hyperlink on a button component.'),
    component_showcase(Div(
    A('Read more', href='#', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800')
), code="""Div(
    A('Read more', href='#', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Paragraph',
        Span(id='paragraph', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph', href='#paragraph', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to set a link inside a paragraph with an underline style.'),
    component_showcase(Div(
    P(
        'The free updates that will be provided is based on the',
        A('roadmap', href='#', cls='font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'that we have laid out for this project. It is also possible that we will provide extra updates outside of the roadmap as well.',
        cls='text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'The free updates that will be provided is based on the',
        A('roadmap', href='#', cls='font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'that we have laid out for this project. It is also possible that we will provide extra updates outside of the roadmap as well.',
        cls='text-gray-500 dark:text-gray-400'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Icon link',
        Span(id='icon-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Icon link', href='#icon-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to set a custom',
        A('SVG icon', href='https://flowbite.com/icons/'),
        'inside the hyperlink element.'
    ),
    component_showcase(Div(
    P(
        '500,000 people & companies have made over a million apps with Glide.',
        A(
            'Read their stories',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-4 h-4 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='inline-flex items-center font-medium text-primary-600 dark:text-primary-500 hover:underline'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        '500,000 people & companies have made over a million apps with Glide.',
        A(
            'Read their stories',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 14 10',
                cls='w-4 h-4 ms-2 rtl:rotate-180'
            ),
            href='#',
            cls='inline-flex items-center font-medium text-primary-600 dark:text-primary-500 hover:underline'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'CTA link',
        Span(id='cta-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: CTA link', href='#cta-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to set a hyperlink on a CTA element with text and a custom icon.'),
    component_showcase(Div(
    A(
        Svg(
            G(
                Path(d='M5.50085 30.1242C8.53625 30.1242 10.9998 27.8749 10.9998 25.1035V20.0828H5.50085C2.46546 20.0828 0.00195312 22.332 0.00195312 25.1035C0.00195312 27.8749 2.46546 30.1242 5.50085 30.1242Z', fill='#0ACF83'),
                Path(d='M0.00195312 15.062C0.00195312 12.2905 2.46546 10.0413 5.50085 10.0413H10.9998V20.0827H5.50085C2.46546 20.0827 0.00195312 17.8334 0.00195312 15.062Z', fill='#A259FF'),
                Path(d='M0.00195312 5.02048C0.00195312 2.24904 2.46546 -0.000244141 5.50085 -0.000244141H10.9998V10.0412H5.50085C2.46546 10.0412 0.00195312 7.79193 0.00195312 5.02048Z', fill='#F24E1E'),
                Path(d='M11 -0.000244141H16.4989C19.5343 -0.000244141 21.9978 2.24904 21.9978 5.02048C21.9978 7.79193 19.5343 10.0412 16.4989 10.0412H11V-0.000244141Z', fill='#FF7262'),
                Path(d='M21.9978 15.062C21.9978 17.8334 19.5343 20.0827 16.4989 20.0827C13.4635 20.0827 11 17.8334 11 15.062C11 12.2905 13.4635 10.0413 16.4989 10.0413C19.5343 10.0413 21.9978 12.2905 21.9978 15.062Z', fill='#1ABCFE'),
                clip_path='url(#clip0_4151_63004)'
            ),
            aria_hidden='true',
            viewbox='0 0 22 31',
            fill='none',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-5 h-5 me-3'
        ),
        Span('Get started with our  Figma Design System', cls='w-full'),
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 14 10',
            cls='w-4 h-4 ms-2 rtl:rotate-180'
        ),
        href='#',
        cls='inline-flex items-center justify-center p-5 text-base font-medium text-gray-500 rounded-lg bg-gray-50 hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
    )
), code="""Div(
    A(
        Svg(
            G(
                Path(d='M5.50085 30.1242C8.53625 30.1242 10.9998 27.8749 10.9998 25.1035V20.0828H5.50085C2.46546 20.0828 0.00195312 22.332 0.00195312 25.1035C0.00195312 27.8749 2.46546 30.1242 5.50085 30.1242Z', fill='#0ACF83'),
                Path(d='M0.00195312 15.062C0.00195312 12.2905 2.46546 10.0413 5.50085 10.0413H10.9998V20.0827H5.50085C2.46546 20.0827 0.00195312 17.8334 0.00195312 15.062Z', fill='#A259FF'),
                Path(d='M0.00195312 5.02048C0.00195312 2.24904 2.46546 -0.000244141 5.50085 -0.000244141H10.9998V10.0412H5.50085C2.46546 10.0412 0.00195312 7.79193 0.00195312 5.02048Z', fill='#F24E1E'),
                Path(d='M11 -0.000244141H16.4989C19.5343 -0.000244141 21.9978 2.24904 21.9978 5.02048C21.9978 7.79193 19.5343 10.0412 16.4989 10.0412H11V-0.000244141Z', fill='#FF7262'),
                Path(d='M21.9978 15.062C21.9978 17.8334 19.5343 20.0827 16.4989 20.0827C13.4635 20.0827 11 17.8334 11 15.062C11 12.2905 13.4635 10.0413 16.4989 10.0413C19.5343 10.0413 21.9978 12.2905 21.9978 15.062Z', fill='#1ABCFE'),
                clip_path='url(#clip0_4151_63004)'
            ),
            aria_hidden='true',
            viewbox='0 0 22 31',
            fill='none',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-5 h-5 me-3'
        ),
        Span('Get started with our  Figma Design System', cls='w-full'),
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 14 10',
            cls='w-4 h-4 ms-2 rtl:rotate-180'
        ),
        href='#',
        cls='inline-flex items-center justify-center p-5 text-base font-medium text-gray-500 rounded-lg bg-gray-50 hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Card link',
        Span(id='card-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Card link', href='#card-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to set a hyperlink on a card component.'),
    component_showcase(Div(
    A(
        H5('Noteworthy technology acquisitions 2021', cls='mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white'),
        P('Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.', cls='font-normal text-gray-700 dark:text-gray-400'),
        href='#',
        cls='block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700'
    )
), code="""Div(
    A(
        H5('Noteworthy technology acquisitions 2021', cls='mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white'),
        P('Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.', cls='font-normal text-gray-700 dark:text-gray-400'),
        href='#',
        cls='block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-md hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Image link',
        Span(id='image-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image link', href='#image-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to set a hyperlink on an image inside a card component.'),
    component_showcase(Div(
    Div(
        A(
            Img(src='/docs/images/blog/image-1.jpg', alt=True, cls='rounded-t-lg'),
            href='#'
        ),
        Div(
            A(
                H5('Noteworthy technology acquisitions 2021', cls='mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white'),
                href='#'
            ),
            P('Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.', cls='mb-3 font-normal text-gray-700 dark:text-gray-400'),
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
                cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
            ),
            cls='p-5'
        ),
        cls='max-w-sm bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700'
    )
), code="""Div(
    Div(
        A(
            Img(src='/docs/images/blog/image-1.jpg', alt=True, cls='rounded-t-lg'),
            href='#'
        ),
        Div(
            A(
                H5('Noteworthy technology acquisitions 2021', cls='mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white'),
                href='#'
            ),
            P('Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.', cls='mb-3 font-normal text-gray-700 dark:text-gray-400'),
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
                cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
            ),
            cls='p-5'
        ),
        cls='max-w-sm bg-white border border-gray-200 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    id='mainContent'
)
