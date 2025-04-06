from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The device mockup component can be used to feature a preview and screenshot of your application as if you would already use it on a mobile phone and it’s a great use case for hero and CTA sections.'),
    P('This component is built using only the utility classes from Tailwind CSS and has built-in dark mode support so it’s easy to customize, it loads very fast and integrates perfectly with Tailwind CSS and Flowbite.'),
    P('You can choose from multiple examples of mockups including phone, tablet, laptop, and even desktop devices with iOS or Android support.'),
    H2(
        'Default mockup',
        Span(id='default-mockup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default mockup', href='#default-mockup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a standard phone mockup based on Tailwind CSS and add your app screenshot inside of it with dark mode support included.'),
    component_showcase(Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px]'
    )
), code="""Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px]'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'iPhone 12 mockup (iOS)',
        Span(id='iphone-12-mockup-ios', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: iPhone 12 mockup (iOS)', href='#iphone-12-mockup-ios', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to clearly show that the preview of your application is being used on an iPhone with iOS.'),
    component_showcase(Div(
    Div(
        Div(cls='w-[148px] h-[18px] bg-gray-800 top-0 rounded-b-[1rem] left-1/2 -translate-x-1/2 absolute'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-2-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-2-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px] shadow-xl'
    )
), code="""Div(
    Div(
        Div(cls='w-[148px] h-[18px] bg-gray-800 top-0 rounded-b-[1rem] left-1/2 -translate-x-1/2 absolute'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-2-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-2-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px] shadow-xl'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Google Pixel (Android)',
        Span(id='google-pixel-android', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Google Pixel (Android)', href='#google-pixel-android', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this alternative phone mockup example if you want to feature previews for android gadgets.'),
    component_showcase(Div(
    Div(
        Div(cls='w-[148px] h-[18px] bg-gray-800 top-0 rounded-b-[1rem] left-1/2 -translate-x-1/2 absolute'),
        Div(cls='h-[32px] w-[3px] bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-xl overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-xl h-[600px] w-[300px] shadow-xl'
    )
), code="""Div(
    Div(
        Div(cls='w-[148px] h-[18px] bg-gray-800 top-0 rounded-b-[1rem] left-1/2 -translate-x-1/2 absolute'),
        Div(cls='h-[32px] w-[3px] bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-xl overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-xl h-[600px] w-[300px] shadow-xl'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Tablet mockup',
        Span(id='tablet-mockup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Tablet mockup', href='#tablet-mockup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to show an application preview inside of a responsive tablet mockup.'),
    component_showcase(Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/tablet-mockup-image.png', alt=True, cls='dark:hidden h-[426px] md:h-[654px]'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/tablet-mockup-image-dark.png', alt=True, cls='hidden dark:block h-[426px] md:h-[654px]'),
            cls='rounded-[2rem] overflow-hidden h-[426px] md:h-[654px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[454px] max-w-[341px] md:h-[682px] md:max-w-[512px]'
    )
), code="""Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-800 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/tablet-mockup-image.png', alt=True, cls='dark:hidden h-[426px] md:h-[654px]'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/tablet-mockup-image-dark.png', alt=True, cls='hidden dark:block h-[426px] md:h-[654px]'),
            cls='rounded-[2rem] overflow-hidden h-[426px] md:h-[654px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[14px] rounded-[2.5rem] h-[454px] max-w-[341px] md:h-[682px] md:max-w-[512px]'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Laptop mockup',
        Span(id='laptop-mockup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Laptop mockup', href='#laptop-mockup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a screenshot of your application inside a laptop mockup.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/laptop-screen.png', alt=True, cls='dark:hidden h-[156px] md:h-[278px] w-full rounded-lg'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/laptop-screen-dark.png', alt=True, cls='hidden dark:block h-[156px] md:h-[278px] w-full rounded-lg'),
            cls='rounded-lg overflow-hidden h-[156px] md:h-[278px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[8px] rounded-t-xl h-[172px] max-w-[301px] md:h-[294px] md:max-w-[512px]'
    ),
    Div(
        Div(cls='absolute left-1/2 top-0 -translate-x-1/2 rounded-b-xl w-[56px] h-[5px] md:w-[96px] md:h-[8px] bg-gray-800'),
        cls='relative mx-auto bg-gray-900 dark:bg-gray-700 rounded-b-xl rounded-t-sm h-[17px] max-w-[351px] md:h-[21px] md:max-w-[597px]'
    )
), code="""Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/laptop-screen.png', alt=True, cls='dark:hidden h-[156px] md:h-[278px] w-full rounded-lg'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/laptop-screen-dark.png', alt=True, cls='hidden dark:block h-[156px] md:h-[278px] w-full rounded-lg'),
            cls='rounded-lg overflow-hidden h-[156px] md:h-[278px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[8px] rounded-t-xl h-[172px] max-w-[301px] md:h-[294px] md:max-w-[512px]'
    ),
    Div(
        Div(cls='absolute left-1/2 top-0 -translate-x-1/2 rounded-b-xl w-[56px] h-[5px] md:w-[96px] md:h-[8px] bg-gray-800'),
        cls='relative mx-auto bg-gray-900 dark:bg-gray-700 rounded-b-xl rounded-t-sm h-[17px] max-w-[351px] md:h-[21px] md:max-w-[597px]'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Desktop mockup',
        Span(id='desktop-mockup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Desktop mockup', href='#desktop-mockup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a preview of your application inside a desktop device such as an iMac.'),
    component_showcase(Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/screen-image-imac.png', alt=True, cls='dark:hidden h-[140px] md:h-[262px] w-full rounded-xl'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/screen-image-imac-dark.png', alt=True, cls='hidden dark:block h-[140px] md:h-[262px] w-full rounded-xl'),
            cls='rounded-xl overflow-hidden h-[140px] md:h-[262px]'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[16px] rounded-t-xl h-[172px] max-w-[301px] md:h-[294px] md:max-w-[512px]'
    ),
    Div(cls='relative mx-auto bg-gray-900 dark:bg-gray-700 rounded-b-xl h-[24px] max-w-[301px] md:h-[42px] md:max-w-[512px]'),
    Div(cls='relative mx-auto bg-gray-800 rounded-b-xl h-[55px] max-w-[83px] md:h-[95px] md:max-w-[142px]')
), code="""Div(
    Div(
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/screen-image-imac.png', alt=True, cls='dark:hidden h-[140px] md:h-[262px] w-full rounded-xl'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/screen-image-imac-dark.png', alt=True, cls='hidden dark:block h-[140px] md:h-[262px] w-full rounded-xl'),
            cls='rounded-xl overflow-hidden h-[140px] md:h-[262px]'
        ),
        cls='relative mx-auto border-gray-800 dark:border-gray-800 bg-gray-800 border-[16px] rounded-t-xl h-[172px] max-w-[301px] md:h-[294px] md:max-w-[512px]'
    ),
    Div(cls='relative mx-auto bg-gray-900 dark:bg-gray-700 rounded-b-xl h-[24px] max-w-[301px] md:h-[42px] md:max-w-[512px]'),
    Div(cls='relative mx-auto bg-gray-800 rounded-b-xl h-[55px] max-w-[83px] md:h-[95px] md:max-w-[142px]')
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Smartwatch mockup',
        Span(id='smartwatch-mockup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Smartwatch mockup', href='#smartwatch-mockup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to showcase applications built for smartwatches.'),
    component_showcase(Div(
    Div(cls='relative mx-auto bg-gray-800 dark:bg-gray-700 rounded-t-[2.5rem] h-[63px] max-w-[133px]'),
    Div(
        Div(cls='h-[41px] w-[6px] bg-gray-800 dark:bg-gray-800 absolute -end-[16px] top-[40px] rounded-e-lg'),
        Div(cls='h-[32px] w-[6px] bg-gray-800 dark:bg-gray-800 absolute -end-[16px] top-[88px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/watch-screen-image.png', alt=True, cls='dark:hidden h-[193px] w-[188px]'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/watch-screen-image-dark.png', alt=True, cls='hidden dark:block h-[193px] w-[188px]'),
            cls='rounded-[2rem] overflow-hidden h-[193px] w-[188px]'
        ),
        cls='relative mx-auto border-gray-900 dark:bg-gray-800 dark:border-gray-800 border-[10px] rounded-[2.5rem] h-[213px] w-[208px]'
    ),
    Div(cls='relative mx-auto bg-gray-800 dark:bg-gray-700 rounded-b-[2.5rem] h-[63px] max-w-[133px]')
), code="""Div(
    Div(cls='relative mx-auto bg-gray-800 dark:bg-gray-700 rounded-t-[2.5rem] h-[63px] max-w-[133px]'),
    Div(
        Div(cls='h-[41px] w-[6px] bg-gray-800 dark:bg-gray-800 absolute -end-[16px] top-[40px] rounded-e-lg'),
        Div(cls='h-[32px] w-[6px] bg-gray-800 dark:bg-gray-800 absolute -end-[16px] top-[88px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/watch-screen-image.png', alt=True, cls='dark:hidden h-[193px] w-[188px]'),
            Img(src='https://flowbite.s3.amazonaws.com/docs/device-mockups/watch-screen-image-dark.png', alt=True, cls='hidden dark:block h-[193px] w-[188px]'),
            cls='rounded-[2rem] overflow-hidden h-[193px] w-[188px]'
        ),
        cls='relative mx-auto border-gray-900 dark:bg-gray-800 dark:border-gray-800 border-[10px] rounded-[2.5rem] h-[213px] w-[208px]'
    ),
    Div(cls='relative mx-auto bg-gray-800 dark:bg-gray-700 rounded-b-[2.5rem] h-[63px] max-w-[133px]')
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Mockup colors',
        Span(id='mockup-colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Mockup colors', href='#mockup-colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can easily update the color of the mockup by changing the background color with Tailwind CSS.'),
    component_showcase(Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-300 dark:border-gray-800 bg-gray-300 dark:bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px]'
    )
), code="""Div(
    Div(
        Div(cls='h-[32px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[72px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[124px] rounded-s-lg'),
        Div(cls='h-[46px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -start-[17px] top-[178px] rounded-s-lg'),
        Div(cls='h-[64px] w-[3px] bg-gray-300 dark:bg-gray-800 absolute -end-[17px] top-[142px] rounded-e-lg'),
        Div(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-light.png', alt=True, cls='dark:hidden w-[272px] h-[572px]'),
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/mockup-1-dark.png', alt=True, cls='hidden dark:block w-[272px] h-[572px]'),
            cls='rounded-[2rem] overflow-hidden w-[272px] h-[572px] bg-white dark:bg-gray-800'
        ),
        cls='relative mx-auto border-gray-300 dark:border-gray-800 bg-gray-300 dark:bg-gray-800 border-[14px] rounded-[2.5rem] h-[600px] w-[300px]'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    id='mainContent'
)
