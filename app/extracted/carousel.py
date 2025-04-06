from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('The carousel component can be used to cycle through a set of elements using custom options, controls, and indicators based on the JavaScript object from Flowbite.'),
    H2(
        'Default slider',
        Span(id='default-slider', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default slider', href='#default-slider', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The carousel component can be initialized by using the',
        Code('data-carousel={static|slide}'),
        'data attribute and by applying a unique',
        Code('id'),
        'attribute to the parent element.'
    ),
    Ul(
        Li(
            Code('data-carousel="static"'),
            'to prevent the carousel sliding by default'
        ),
        Li(
            Code('data-carousel="slide"'),
            'to infinitely cycle through the items'
        )
    ),
    P(
        'You can add as many carousel items as you want, but make sure that you add the',
        Code('data-carousel-item'),
        'data attribute to each of them and set a single item to active by applying the',
        Code('active'),
        'value to the data attribute.'
    ),
    P(
        'Use the',
        Code('duration-*'),
        'and the animation classes from Tailwind CSS to apply custom effects to the carousel items and don’t forget to set the',
        Code('hidden'),
        'class by default to prevent flickering.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(type='button', aria_current='true', aria_label='Slide 1', data_carousel_slide_to='0', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 2', data_carousel_slide_to='1', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 3', data_carousel_slide_to='2', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 4', data_carousel_slide_to='3', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 5', data_carousel_slide_to='4', cls='w-3 h-3 rounded-full'),
            cls='absolute z-30 flex -translate-x-1/2 bottom-5 left-1/2 space-x-3 rtl:space-x-reverse'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='default-carousel',
        data_carousel='slide',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(type='button', aria_current='true', aria_label='Slide 1', data_carousel_slide_to='0', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 2', data_carousel_slide_to='1', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 3', data_carousel_slide_to='2', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 4', data_carousel_slide_to='3', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 5', data_carousel_slide_to='4', cls='w-3 h-3 rounded-full'),
            cls='absolute z-30 flex -translate-x-1/2 bottom-5 left-1/2 space-x-3 rtl:space-x-reverse'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='default-carousel',
        data_carousel='slide',
        cls='relative w-full'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Controls',
        Span(id='controls', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Controls', href='#controls', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-carousel-prev'),
        'and',
        Code('data-carousel-next'),
        'data attribute to listen to click events which will trigger the slide event from the carousel component to each direction.'
    ),
    P('You can customize the control elements with the classes from Tailwind CSS anyhow you want.'),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='controls-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='controls-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Indicators',
        Span(id='indicators', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Indicators', href='#indicators', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Show the carousel indicators by adding the',
        Code('data-carousel-slide-to={position}'),
        'to any number or style of indicator elements where the value equals the position of the slider element.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(type='button', aria_current='true', aria_label='Slide 1', data_carousel_slide_to='0', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 2', data_carousel_slide_to='1', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 3', data_carousel_slide_to='2', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 4', data_carousel_slide_to='3', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 5', data_carousel_slide_to='4', cls='w-3 h-3 rounded-full'),
            cls='absolute z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse bottom-5 left-1/2'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='indicators-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-700 ease-in-out'
            ),
            cls='relative h-56 overflow-hidden rounded-lg md:h-96'
        ),
        Div(
            Button(type='button', aria_current='true', aria_label='Slide 1', data_carousel_slide_to='0', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 2', data_carousel_slide_to='1', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 3', data_carousel_slide_to='2', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 4', data_carousel_slide_to='3', cls='w-3 h-3 rounded-full'),
            Button(type='button', aria_current='false', aria_label='Slide 5', data_carousel_slide_to='4', cls='w-3 h-3 rounded-full'),
            cls='absolute z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse bottom-5 left-1/2'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='indicators-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Animation',
        Span(id='animation', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Animation', href='#animation', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can easily customize the duration and animation style of the carousel component by using the',
        Code('duration-*'),
        'and',
        Code('ease-*'),
        'utility classes from Tailwind CSS.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='animation-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
), code="""Div(
    Div(
        Div(
            Div(
                Img(src='/docs/images/carousel/carousel-1.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-2.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-3.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item='active',
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-4.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
            ),
            Div(
                Img(src='/docs/images/carousel/carousel-5.svg', alt='...', cls='absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2'),
                data_carousel_item=True,
                cls='hidden duration-200 ease-linear'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
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
                cls='inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none'
            ),
            type='button',
            data_carousel_next=True,
            cls='absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none'
        ),
        id='animation-carousel',
        data_carousel='static',
        cls='relative w-full'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('Carousel'),
        'class from Flowbite to create an object that you can use to apply custom styles, change the active slide item, set callback functions directly from JavaScript.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Pass the object parameters for the Carousel object to set the carousel items and options.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Parameter', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Required', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('carouselElement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Parent HTML element of the carousel component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('items', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass an array of carousel item objects including the position and the element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass an object of options to set the interval, indicators, and callback functions.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('instanceOptions', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td(
                        'Object of options that allows you to set a custom ID for the instance that is being added to the',
                        A('Instance Manager', href='https://flowbite.com/docs/getting-started/javascript/#instance-options', cls='underline hover:no-underline'),
                        'and whether to override or not an existing instance.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use these options for the Carousel object to set the default position, interval, indicators, custom styles, and callback functions.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Option', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('defaultPosition', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Integer', cls='px-6 py-4 font-medium'),
                    Td('Set the default active slider item based on its position (starts from [0-x]).', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('interval', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Integer', cls='px-6 py-4 font-medium'),
                    Td('Set the interval duration in milliseconds when the carousel is cycling.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('indicators', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4 font-medium'),
                    Td('An optional object of indicator elements and custom classes.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onNext', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the next carousel item has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onPrev', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the previous carousel item has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onChange', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4 font-medium'),
                    Td('Set a callback function when the position of the carousel item has been changed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Methods',
        Span(id='methods', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Methods', href='#methods', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following methods on the Carousel object to programmatically manipulate the behaviour.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Method', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('next()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to go to the next slide of the carousel component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('prev()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to go to the previous slide of the carousel component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('slideTo(position)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to go the carousel with the position that you set as a parameter.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('cycle()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to start cycling the carousel component based on the default interval duration.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('pause()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to stop the automatic cycling of the carousel component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('getItem(position)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Get the carousel item based on the position number that you set as a parameter.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('getActiveItem()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Get the current active carousel item.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnNext(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Set a callback function when the next carousel item has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnPrev(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Set a callback function when the previous carousel item has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnChange(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Set a callback function when the the slide item inside the carousel has been changed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Example',
        Span(id='example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Example', href='#example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Check out the following example to learn how to programmatically create a new Carousel object by passing the parameters, using the methods, and the callback functions.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('carouselElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-example'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('items', cls='nx'),
                        Span('=', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('2', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('3', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-4'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('];', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('options', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('defaultPosition', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('interval', cls='nx'),
                        Span(':', cls='o'),
                        Span('3000', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('indicators', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bg-white dark:bg-gray-800'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('items', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('2', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('3', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-4'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('],', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// callback functions', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onNext', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'next slider item is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onPrev', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'previous slider item is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onChange', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'new slider item has been shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// instance options object', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('instanceOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'carousel-example'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('override', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P('Create a new carousel object using the options set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Carousel', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('carousel', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Carousel', cls='nx'),
                        Span('(', cls='p'),
                        Span('carouselElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('items', cls='nx'),
                        Span(',', cls='p'),
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        Span('instanceOptions', cls='nx'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'Use the',
        Code('next()'),
        'and',
        Code('prev()'),
        'public methods on the carousel object to jump to the left or right carousel slide item based on the position of the current active item.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// goes to the next (right) slide', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('next', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// goes to the previous (left) slide', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('prev', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'Use the',
        Code('slideTo(position)'),
        'public method to jump to the carousel slide item with the specified position.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// jumps to the 3rd position (position starts from 0)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('slideTo', cls='nx'),
                        Span('(', cls='p'),
                        Span('2', cls='mi'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'Use the',
        Code('cycle()'),
        'method to start an automated cycling where the duration is the milliseconds of time between each slide and the',
        Code('pause()'),
        'method to clear the cycle event.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// starts or resumes the carousel cycling (automated sliding)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('cycle', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// pauses the cycling (automated sliding)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('pause', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H3(
        'HTML Markup',
        Span(id='html-markup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: HTML Markup', href='#html-markup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Here is an example of the HTML markup that you can use for the JavaScript example above. Please note that you should use the',
        Code('hidden'),
        'class from Tailwind CSS to hide the carousel items by default.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-example"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"relative w-full"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Carousel wrapper -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"relative h-56 overflow-hidden rounded-lg sm:h-64 xl:h-80 2xl:h-96"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Item 1 -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-item-1"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden duration-700 ease-in-out"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('img', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"/docs/images/carousel/carousel-1.svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('alt', cls='na'),
                        Span('=', cls='o'),
                        Span('"..."', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Item 2 -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-item-2"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden duration-700 ease-in-out"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('img', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"/docs/images/carousel/carousel-2.svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('alt', cls='na'),
                        Span('=', cls='o'),
                        Span('"..."', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Item 3 -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-item-3"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden duration-700 ease-in-out"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('img', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"/docs/images/carousel/carousel-3.svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('alt', cls='na'),
                        Span('=', cls='o'),
                        Span('"..."', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Item 4 -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-item-4"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden duration-700 ease-in-out"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('img', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('src', cls='na'),
                        Span('=', cls='o'),
                        Span('"/docs/images/carousel/carousel-4.svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('alt', cls='na'),
                        Span('=', cls='o'),
                        Span('"..."', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Slider indicators -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"absolute bottom-5 left-1/2 z-30 flex -translate-x-1/2 space-x-3 rtl:space-x-reverse"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-indicator-1"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-3 w-3 rounded-full"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-current', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-label', cls='na'),
                        Span('=', cls='o'),
                        Span('"Slide 1"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('></', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-indicator-2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-3 w-3 rounded-full"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-current', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-label', cls='na'),
                        Span('=', cls='o'),
                        Span('"Slide 2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('></', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-indicator-3"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-3 w-3 rounded-full"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-current', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-label', cls='na'),
                        Span('=', cls='o'),
                        Span('"Slide 3"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('></', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"carousel-indicator-4"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-3 w-3 rounded-full"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-current', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-label', cls='na'),
                        Span('=', cls='o'),
                        Span('"Slide 4"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('></', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Slider controls -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"data-carousel-prev"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"group absolute left-0 top-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 focus:outline-none"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/30 group-hover:bg-white/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-white dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-4 w-4 text-white dark:text-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"none"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 6 10"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linecap', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linejoin', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-width', cls='na'),
                        Span('=', cls='o'),
                        Span('"2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M5 1 1 5l4 4"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('svg', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('>', cls='p'),
                        'Previous',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"data-carousel-next"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"group absolute right-0 top-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 focus:outline-none"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/30 group-hover:bg-white/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-white dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-4 w-4 text-white dark:text-gray-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"none"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 6 10"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linecap', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linejoin', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-width', cls='na'),
                        Span('=', cls='o'),
                        Span('"2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"m1 9 4-4-4-4"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('svg', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('>', cls='p'),
                        'Next',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('button', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='html',
                cls='language-html'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'If you want to set trigger the next or previous slide item for the any button, just add some event listeners and call the',
        Code('next()'),
        'and',
        Code('prev()'),
        'methods on the Carousel object.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('$prevButton', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'data-carousel-prev'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('$nextButton', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'data-carousel-next'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$prevButton', cls='nx'),
                        Span('.', cls='p'),
                        Span('addEventListener', cls='nx'),
                        Span('(', cls='p'),
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('prev', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$nextButton', cls='nx'),
                        Span('.', cls='p'),
                        Span('addEventListener', cls='nx'),
                        Span('(', cls='p'),
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('next', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H3(
        'TypeScript',
        Span(id='typescript', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: TypeScript', href='#typescript', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you’re using the',
        A('TypeScript configuration', href='https://flowbite.com/docs/getting-started/typescript/'),
        'from Flowbite then you can import the types for the Carousel class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Carousel', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('type', cls='nx'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('CarouselItem', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('CarouselOptions', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('CarouselInterface', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('type', cls='nx'),
                        Span('{', cls='p'),
                        Span('InstanceOptions', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
                        Span(';', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('carouselElement', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-example'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('items', cls='nx'),
                        Span(':', cls='o'),
                        Span('CarouselItem', cls='nx'),
                        Span('[]', cls='p'),
                        Span('=', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('2', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('3', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-item-4'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('];', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// object options with default values', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('options', cls='nx'),
                        Span(':', cls='o'),
                        Span('CarouselOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('defaultPosition', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('interval', cls='nx'),
                        Span(':', cls='o'),
                        Span('3000', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('indicators', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bg-white dark:bg-gray-800'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'bg-white/50 dark:bg-gray-800/50 hover:bg-white dark:hover:bg-gray-800'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('items', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('1', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('2', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('position', cls='nx'),
                        Span(':', cls='o'),
                        Span('3', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('el', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'carousel-indicator-4'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('],', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// callback functions', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onNext', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'next slider item is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onPrev', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'previous slider item is shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onChange', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'new slider item has been shown'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// instance options object', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('instanceOptions', cls='nx'),
                        Span(':', cls='o'),
                        Span('InstanceOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'carousel-example'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('override', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('};', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('carousel', cls='nx'),
                        Span(':', cls='o'),
                        Span('CarouselInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Carousel', cls='nx'),
                        Span('(', cls='p'),
                        Span('carouselElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('items', cls='nx'),
                        Span(',', cls='p'),
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        Span('instanceOptions', cls='nx'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('cycle', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// set event listeners for prev and next buttons', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$prevButton', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'data-carousel-prev'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('$nextButton', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'data-carousel-next'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$prevButton', cls='nx'),
                        Span('.', cls='p'),
                        Span('addEventListener', cls='nx'),
                        Span('(', cls='p'),
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('prev', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$nextButton', cls='nx'),
                        Span('.', cls='p'),
                        Span('addEventListener', cls='nx'),
                        Span('(', cls='p'),
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('carousel', cls='nx'),
                        Span('.', cls='p'),
                        Span('next', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    id='mainContent'
)
