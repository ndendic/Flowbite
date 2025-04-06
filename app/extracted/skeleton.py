from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('Use the skeleton component to indicate a loading status with placeholder elements that look very similar to the type of content that is being loaded such as paragraphs, heading, images, videos, and more.'),
    P('You can set the width and height of these skeleton components based on the size of the content and element that it is being loaded in, such as a card or an article page.'),
    P(
        'You can also animate the skeleton component by using the',
        Code('.animate-pulse'),
        'utility class from Tailwind CSS.'
    ),
    H2(
        'Default skeleton',
        Span(id='default-skeleton', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default skeleton', href='#default-skeleton', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a placeholder when loading text content.'),
    component_showcase(Div(
    Div(
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]'),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm animate-pulse'
    )
), code="""Div(
    Div(
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[330px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[300px] mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]'),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm animate-pulse'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Image placeholder',
        Span(id='image-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image placeholder', href='#image-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a placeholder when loading an image and text content.'),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(d='M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-10 h-10 text-gray-200 dark:text-gray-600'
            ),
            cls='flex items-center justify-center w-full h-48 bg-gray-300 rounded-sm sm:w-96 dark:bg-gray-700'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[480px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[440px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[460px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]'),
            cls='w-full'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='space-y-8 animate-pulse md:space-y-0 md:space-x-8 rtl:space-x-reverse md:flex md:items-center'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(d='M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 18',
                cls='w-10 h-10 text-gray-200 dark:text-gray-600'
            ),
            cls='flex items-center justify-center w-full h-48 bg-gray-300 rounded-sm sm:w-96 dark:bg-gray-700'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[480px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[440px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[460px] mb-2.5'),
            Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 max-w-[360px]'),
            cls='w-full'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='space-y-8 animate-pulse md:space-y-0 md:space-x-8 rtl:space-x-reverse md:flex md:items-center'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Video placeholder',
        Span(id='video-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Video placeholder', href='#video-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a skeleton placeholder when loading video content.'),
    component_showcase(Div(
    Div(
        Svg(
            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
            Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM9 13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2Zm4 .382a1 1 0 0 1-1.447.894L10 13v-2l1.553-1.276a1 1 0 0 1 1.447.894v2.764Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 16 20',
            cls='w-10 h-10 text-gray-200 dark:text-gray-600'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='flex items-center justify-center h-56 max-w-sm bg-gray-300 rounded-lg animate-pulse dark:bg-gray-700'
    )
), code="""Div(
    Div(
        Svg(
            Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
            Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM9 13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2Zm4 .382a1 1 0 0 1-1.447.894L10 13v-2l1.553-1.276a1 1 0 0 1 1.447.894v2.764Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 16 20',
            cls='w-10 h-10 text-gray-200 dark:text-gray-600'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='flex items-center justify-center h-56 max-w-sm bg-gray-300 rounded-lg animate-pulse dark:bg-gray-700'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Text placeholder',
        Span(id='text-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text placeholder', href='#text-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a placeholder when loading longer pagraphs and headings.'),
    component_showcase(Div(
    Div(
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            cls='flex items-center w-full max-w-[480px]'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-80'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full max-w-[400px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            cls='flex items-center w-full max-w-[480px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-32'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            cls='flex items-center w-full max-w-[440px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-80'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full max-w-[360px]'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='space-y-2.5 animate-pulse max-w-lg'
    )
), code="""Div(
    Div(
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            cls='flex items-center w-full max-w-[480px]'
        ),
        Div(
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-80'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full max-w-[400px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            cls='flex items-center w-full max-w-[480px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-32'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-24'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-full'),
            cls='flex items-center w-full max-w-[440px]'
        ),
        Div(
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            Div(cls='h-2.5 ms-2 bg-gray-200 rounded-full dark:bg-gray-700 w-80'),
            Div(cls='h-2.5 ms-2 bg-gray-300 rounded-full dark:bg-gray-600 w-full'),
            cls='flex items-center w-full max-w-[360px]'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='space-y-2.5 animate-pulse max-w-lg'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Card placeholder',
        Span(id='card-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Card placeholder', href='#card-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a placeholder when loading content inside a card.'),
    component_showcase(Div(
    Div(
        Div(
            Svg(
                Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z'),
                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 16 20',
                cls='w-10 h-10 text-gray-200 dark:text-gray-600'
            ),
            cls='flex items-center justify-center h-48 mb-4 bg-gray-300 rounded-sm dark:bg-gray-700'
        ),
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700'),
        Div(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-10 h-10 me-3 text-gray-200 dark:text-gray-700'
            ),
            Div(
                Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2'),
                Div(cls='w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            cls='flex items-center mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm p-4 border border-gray-200 rounded-sm shadow-sm animate-pulse md:p-6 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Div(
            Svg(
                Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z'),
                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 16 20',
                cls='w-10 h-10 text-gray-200 dark:text-gray-600'
            ),
            cls='flex items-center justify-center h-48 mb-4 bg-gray-300 rounded-sm dark:bg-gray-700'
        ),
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-48 mb-4'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700 mb-2.5'),
        Div(cls='h-2 bg-gray-200 rounded-full dark:bg-gray-700'),
        Div(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-10 h-10 me-3 text-gray-200 dark:text-gray-700'
            ),
            Div(
                Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2'),
                Div(cls='w-48 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            cls='flex items-center mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm p-4 border border-gray-200 rounded-sm shadow-sm animate-pulse md:p-6 dark:border-gray-700'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Widget placeholder',
        Span(id='widget-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Widget placeholder', href='#widget-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a placeholder of skeleton when fetching data for widgets and cards inside an application.'),
    component_showcase(Div(
    Div(
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2.5'),
        Div(cls='w-48 h-2 mb-10 bg-gray-200 rounded-full dark:bg-gray-700'),
        Div(
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 dark:bg-gray-700'),
            Div(cls='w-full h-56 ms-6 bg-gray-200 rounded-t-lg dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 ms-6 dark:bg-gray-700'),
            Div(cls='w-full h-64 ms-6 bg-gray-200 rounded-t-lg dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-80 ms-6 dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 ms-6 dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-80 ms-6 dark:bg-gray-700'),
            cls='flex items-baseline mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm p-4 border border-gray-200 rounded-sm shadow-sm animate-pulse md:p-6 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Div(cls='h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32 mb-2.5'),
        Div(cls='w-48 h-2 mb-10 bg-gray-200 rounded-full dark:bg-gray-700'),
        Div(
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 dark:bg-gray-700'),
            Div(cls='w-full h-56 ms-6 bg-gray-200 rounded-t-lg dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 ms-6 dark:bg-gray-700'),
            Div(cls='w-full h-64 ms-6 bg-gray-200 rounded-t-lg dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-80 ms-6 dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-72 ms-6 dark:bg-gray-700'),
            Div(cls='w-full bg-gray-200 rounded-t-lg h-80 ms-6 dark:bg-gray-700'),
            cls='flex items-baseline mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-sm p-4 border border-gray-200 rounded-sm shadow-sm animate-pulse md:p-6 dark:border-gray-700'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'List placeholder',
        Span(id='list-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: List placeholder', href='#list-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a placeholder when loading a list of items.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-md p-4 space-y-4 border border-gray-200 divide-y divide-gray-200 rounded-sm shadow-sm animate-pulse dark:divide-gray-700 md:p-6 dark:border-gray-700'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Div(
            Div(
                Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24 mb-2.5'),
                Div(cls='w-32 h-2 bg-gray-200 rounded-full dark:bg-gray-700')
            ),
            Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 w-12'),
            cls='flex items-center justify-between pt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='max-w-md p-4 space-y-4 border border-gray-200 divide-y divide-gray-200 rounded-sm shadow-sm animate-pulse dark:divide-gray-700 md:p-6 dark:border-gray-700'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Testimonial placeholder',
        Span(id='testimonial-placeholder', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Testimonial placeholder', href='#testimonial-placeholder', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a skeleton placeholder when loading data for a testimonial section.'),
    component_showcase(Div(
    Div(
        Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 max-w-[640px] mb-2.5 mx-auto'),
        Div(cls='h-2.5 mx-auto bg-gray-300 rounded-full dark:bg-gray-700 max-w-[540px]'),
        Div(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-8 h-8 text-gray-200 dark:text-gray-700 me-4'
            ),
            Div(cls='w-20 h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 me-3'),
            Div(cls='w-24 h-2 bg-gray-200 rounded-full dark:bg-gray-700'),
            cls='flex items-center justify-center mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='animate-pulse'
    )
), code="""Div(
    Div(
        Div(cls='h-2.5 bg-gray-300 rounded-full dark:bg-gray-700 max-w-[640px] mb-2.5 mx-auto'),
        Div(cls='h-2.5 mx-auto bg-gray-300 rounded-full dark:bg-gray-700 max-w-[540px]'),
        Div(
            Svg(
                Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-8 h-8 text-gray-200 dark:text-gray-700 me-4'
            ),
            Div(cls='w-20 h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 me-3'),
            Div(cls='w-24 h-2 bg-gray-200 rounded-full dark:bg-gray-700'),
            cls='flex items-center justify-center mt-4'
        ),
        Span('Loading...', cls='sr-only'),
        role='status',
        cls='animate-pulse'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Accessibility',
        Span(id='accessibility', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Accessibility', href='#accessibility', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('role="status"'),
        'attribute on the',
        Code('<div>'),
        'wrapper element to notify Assistive Technologies when content is about to be updated and show the “Loading…” text inside a',
        Code('<span>'),
        'tag with the',
        Code('.sr-only'),
        'class to make it visible only to screen readers.'
    ),
    id='mainContent'
)
