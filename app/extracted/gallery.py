from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The gallery component can be used to show multiple images inside a masonry grid layout styles with the utility-first classes from Tailwind CSS to show a collection of pictures to your users based on various layouts, styles, sizes, and colors.'),
    P('This component is recommended for usage within marketing UI interfaces and website sections when you want to show pictures of your team members, office pictures, or even case study images.'),
    H2(
        'Default gallery',
        Span(id='default-gallery', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default gallery', href='#default-gallery', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show a collection of images inside a gallery with three pictures on a row.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 md:grid-cols-3 gap-4'
    )
), code="""Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 md:grid-cols-3 gap-4'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Masonry grid',
        Span(id='masonry-grid', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Masonry grid', href='#masonry-grid', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show the images inside a masonry grid layouts with four columns.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        cls='grid grid-cols-2 md:grid-cols-4 gap-4'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/masonry/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid gap-4'
        ),
        cls='grid grid-cols-2 md:grid-cols-4 gap-4'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Featured image',
        Span(id='featured-image', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Featured image', href='#featured-image', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to feature the most important image and show a row of five pictures below.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/featured/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid grid-cols-5 gap-4'
        ),
        cls='grid gap-4'
    )
), code="""Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/featured/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
            ),
            cls='grid grid-cols-5 gap-4'
        ),
        cls='grid gap-4'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Quad gallery',
        Span(id='quad-gallery', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Quad gallery', href='#quad-gallery', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show four larger images with two items on a row.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 gap-2'
    )
), code="""Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 gap-2'
    )
)""", id="example_3",cls='mt-2 mb-6'),
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
            Span('Requires Fastbite JS', cls='text-sm font-medium'),
            Svg(
                Path(d='m1 9 4-4-4-4', stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2'),
                aria_hidden='true',
                fill='none',
                viewbox='0 0 6 10',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-2.5 h-2.5 ml-2.5'
            ),
            aria_label='Component requires Fastbite JavaScript',
            href='/docs/getting-started/quickstart/',
            cls='inline-flex items-center justify-between px-1 py-1 pr-4 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700'
        ),
        cls='mt-8 -mb-5'
    ),
    H2(
        'Gallery with slider',
        Span(id='gallery-with-slider', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Gallery with slider', href='#gallery-with-slider', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example uses the',
        A('carousel slider', href='https://flowbite.com/docs/components/carousel/'),
        'functionality to show multiple images inside a slider gallery.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Button(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180'
                ),
                Span('Previous', cls='sr-only'),
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-50/30 dark:bg-gray-800/30 group-hover:bg-gray-50/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_prev=True,
            cls='absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        Button(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180'
                ),
                Span('Next', cls='sr-only'),
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-50/30 dark:bg-gray-800/30 group-hover:bg-gray-50/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='gallery',
        data_carousel='slide',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Button(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 1 1 5l4 4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180'
                ),
                Span('Previous', cls='sr-only'),
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-50/30 dark:bg-gray-800/30 group-hover:bg-gray-50/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_prev=True,
            cls='absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        Button(
            Span(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 6 10',
                    cls='w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180'
                ),
                Span('Next', cls='sr-only'),
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-50/30 dark:bg-gray-800/30 group-hover:bg-gray-50/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='gallery',
        data_carousel='slide',
        cls='relative w-full'
    )
)""", id="example_4",cls='mt-2 mb-6'),
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
            Span('Requires Fastbite JS', cls='text-sm font-medium'),
            Svg(
                Path(d='m1 9 4-4-4-4', stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2'),
                aria_hidden='true',
                fill='none',
                viewbox='0 0 6 10',
                xmlns='http://www.w3.org/2000/svg',
                cls='w-2.5 h-2.5 ml-2.5'
            ),
            aria_label='Component requires Fastbite JavaScript',
            href='/docs/getting-started/quickstart/',
            cls='inline-flex items-center justify-between px-1 py-1 pr-4 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700'
        ),
        cls='mt-8 -mb-5'
    ),
    H2(
        'Custom slider controls',
        Span(id='custom-slider-controls', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Custom slider controls', href='#custom-slider-controls', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example uses an alternative style for the control button for the carousel slider component.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-5 h-5'
                    ),
                    Span('Previous', cls='sr-only'),
                    cls='text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white'
                ),
                type='button',
                data_carousel_prev=True,
                cls='flex justify-center items-center me-4 h-full cursor-pointer group focus:outline-none'
            ),
            Button(
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-5 h-5'
                    ),
                    Span('Next', cls='sr-only'),
                    cls='text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white'
                ),
                type='button',
                data_carousel_next=True,
                cls='flex justify-center items-center h-full cursor-pointer group focus:outline-none'
            ),
            cls='flex justify-center items-center pt-4'
        ),
        id='custom-controls-gallery',
        data_carousel='slide',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-5 h-5'
                    ),
                    Span('Previous', cls='sr-only'),
                    cls='text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white'
                ),
                type='button',
                data_carousel_prev=True,
                cls='flex justify-center items-center me-4 h-full cursor-pointer group focus:outline-none'
            ),
            Button(
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 14 10',
                        cls='rtl:rotate-180 w-5 h-5'
                    ),
                    Span('Next', cls='sr-only'),
                    cls='text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white'
                ),
                type='button',
                data_carousel_next=True,
                cls='flex justify-center items-center h-full cursor-pointer group focus:outline-none'
            ),
            cls='flex justify-center items-center pt-4'
        ),
        id='custom-controls-gallery',
        data_carousel='slide',
        cls='relative w-full'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Gallery with tag filters',
        Span(id='gallery-with-tag-filters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Gallery with tag filters', href='#gallery-with-tag-filters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a list of tags and filter the images below based on the activately selected tag.'),
    component_showcase(Div(
    Div(
        Button('All categories', type='button', cls='text-primary-700 hover:text-white border border-primary-600 bg-gray-50 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:border-primary-500 dark:text-primary-500 dark:hover:text-white dark:hover:bg-primary-500 dark:bg-gray-900 dark:focus:ring-primary-800'),
        Button('Shoes', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Bags', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Electronics', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Gaming', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        cls='flex items-center justify-center py-4 md:py-8 flex-wrap'
    ),
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 md:grid-cols-3 gap-4'
    )
), code="""Div(
    Div(
        Button('All categories', type='button', cls='text-primary-700 hover:text-white border border-primary-600 bg-gray-50 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:border-primary-500 dark:text-primary-500 dark:hover:text-white dark:hover:bg-primary-500 dark:bg-gray-900 dark:focus:ring-primary-800'),
        Button('Shoes', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Bags', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Electronics', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        Button('Gaming', type='button', cls='text-gray-900 border border-white hover:border-gray-200 dark:border-gray-900 dark:bg-gray-900 dark:hover:border-gray-700 bg-gray-50 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-full text-base font-medium px-5 py-2.5 text-center me-3 mb-3 dark:text-white dark:focus:ring-gray-800'),
        cls='flex items-center justify-center py-4 md:py-8 flex-wrap'
    ),
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-10.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/gallery/square/image-11.jpg', alt=True, cls='h-auto max-w-full rounded-lg')
        ),
        cls='grid grid-cols-2 md:grid-cols-3 gap-4'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    id='mainContent'
)
