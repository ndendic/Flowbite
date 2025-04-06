from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('Get started with the heading component to define titles and subtitles on a web page and also improve the on-page SEO metrics of your website by targeting high-traffic keywords on Google.'),
    P('At least one unique H1 tag should be available for each page on your website with the next tags starting from H2 to H6 for each section. Choose from a collection of custom heading components based on multiple styles and layouts built with the utility classes from Tailwind CSS.'),
    H2(
        'Default heading',
        Span(id='default-heading', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default heading', href='#default-heading', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a H1 heading in the context of a paragraph and CTA button for landing pages.'),
    component_showcase(Div(
    H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400'),
    A(
        'Learn more',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 14 10',
            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
        ),
        href='#',
        cls='inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
    )
), code="""Div(
    H1('We invest in the worldâ\x80\x99s potential', cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400'),
    A(
        'Learn more',
        Svg(
            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='none',
            viewbox='0 0 14 10',
            cls='w-3.5 h-3.5 ms-2 rtl:rotate-180'
        ),
        href='#',
        cls='inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Second-level heading',
        Span(id='second-level-heading', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Second-level heading', href='#second-level-heading', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a second-level H2 heading as the main subtitle for each section of your web page.'),
    component_showcase(Div(
    H2('Payments tool for companies', cls='text-4xl font-extrabold dark:text-white'),
    P('Start developing with an open-source library of over 450+ UI components, sections, and pages built with the utility classes from Tailwind CSS and designed in Figma.', cls='my-4 text-lg text-gray-500'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions. Accelerate critical development work, eliminate toil, and deploy changes with ease.', cls='mb-4 text-lg font-normal text-gray-500 dark:text-gray-400'),
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
        cls='inline-flex items-center text-lg text-primary-600 dark:text-primary-500 hover:underline'
    )
), code="""Div(
    H2('Payments tool for companies', cls='text-4xl font-extrabold dark:text-white'),
    P('Start developing with an open-source library of over 450+ UI components, sections, and pages built with the utility classes from Tailwind CSS and designed in Figma.', cls='my-4 text-lg text-gray-500'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions. Accelerate critical development work, eliminate toil, and deploy changes with ease.', cls='mb-4 text-lg font-normal text-gray-500 dark:text-gray-400'),
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
        cls='inline-flex items-center text-lg text-primary-600 dark:text-primary-500 hover:underline'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Highlighted heading',
        Span(id='highlighted-heading', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Highlighted heading', href='#highlighted-heading', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to highlight a certain portion of the heading text with a different color.'),
    component_showcase(Div(
    H1(
        'Get back to growth with',
        Span("the world's #1", cls='text-primary-600 dark:text-primary-500'),
        'CRM.',
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
), code="""Div(
    H1(
        'Get back to growth with',
        Span("the world's #1", cls='text-primary-600 dark:text-primary-500'),
        'CRM.',
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Heading mark',
        Span(id='heading-mark', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading mark', href='#heading-mark', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to mark one part of the heading text with a solid background for highlighting.'),
    component_showcase(Div(
    H1(
        'Regain',
        Mark('control', cls='px-2 text-white bg-primary-600 rounded-sm dark:bg-primary-500'),
        'over your days',
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
), code="""Div(
    H1(
        'Regain',
        Mark('control', cls='px-2 text-white bg-primary-600 rounded-sm dark:bg-primary-500'),
        'over your days',
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Heading gradient',
        Span(id='heading-gradient', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading gradient', href='#heading-gradient', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to highlight a portion of the heading text by using a gradient style.'),
    component_showcase(Div(
    H1(
        Span('Better Data', cls='text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400'),
        'Scalable AI.',
        cls='mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
), code="""Div(
    H1(
        Span('Better Data', cls='text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400'),
        'Scalable AI.',
        cls='mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Heading underline',
        Span(id='heading-underline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading underline', href='#heading-underline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example to underline an important part of the heading component using the offset feature from Tailwind CSS.'),
    component_showcase(Div(
    H1(
        'We invest in the',
        Span('worldâ\x80\x99s potential', cls='underline underline-offset-3 decoration-8 decoration-primary-400 dark:decoration-primary-600'),
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
), code="""Div(
    H1(
        'We invest in the',
        Span('worldâ\x80\x99s potential', cls='underline underline-offset-3 decoration-8 decoration-primary-400 dark:decoration-primary-600'),
        cls='mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white'
    ),
    P('Here at Flowbite we focus on markets where technology, innovation, and capital can unlock long-term value and drive economic growth.', cls='text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400')
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Breadcrumb context',
        Span(id='breadcrumb-context', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Breadcrumb context', href='#breadcrumb-context', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example to position a breadcrumb component above the H1 heading component.'),
    component_showcase(Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 text-gray-400 mx-1 rtl:rotate-180'
                    ),
                    A('Projects', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 text-gray-400 mx-1 rtl:rotate-180'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-3 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex mb-4'
    ),
    H2('Team management', cls='mb-4 text-3xl font-extrabold leading-none tracking-tight text-gray-900 md:text-4xl dark:text-white')
), code="""Div(
    Nav(
        Ol(
            Li(
                A(
                    Svg(
                        Path(d='m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-3 h-3 me-2.5'
                    ),
                    'Home',
                    href='#',
                    cls='inline-flex items-center text-sm font-medium text-gray-700 hover:text-primary-600 dark:text-gray-400 dark:hover:text-white'
                ),
                cls='inline-flex items-center'
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 text-gray-400 mx-1 rtl:rotate-180'
                    ),
                    A('Projects', href='#', cls='ms-1 text-sm font-medium text-gray-700 hover:text-primary-600 md:ms-2 dark:text-gray-400 dark:hover:text-white'),
                    cls='flex items-center'
                )
            ),
            Li(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 6 10',
                        cls='w-3 h-3 text-gray-400 mx-1 rtl:rotate-180'
                    ),
                    Span('Flowbite', cls='ms-1 text-sm font-medium text-gray-500 md:ms-2 dark:text-gray-400'),
                    cls='flex items-center'
                ),
                aria_current='page'
            ),
            cls='inline-flex items-center space-x-1 md:space-x-3 rtl:space-x-reverse'
        ),
        aria_label='Breadcrumb',
        cls='flex mb-4'
    ),
    H2('Team management', cls='mb-4 text-3xl font-extrabold leading-none tracking-tight text-gray-900 md:text-4xl dark:text-white')
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Badge context',
        Span(id='badge-context', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Badge context', href='#badge-context', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a badge component inside the heading text element as a secondary indicator.'),
    component_showcase(Div(
    H1(
        'Flowbite',
        Span('PRO', cls='bg-primary-100 text-primary-800 text-2xl font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-200 dark:text-primary-800 ms-2'),
        cls='flex items-center text-5xl font-extrabold dark:text-white'
    )
), code="""Div(
    H1(
        'Flowbite',
        Span('PRO', cls='bg-primary-100 text-primary-800 text-2xl font-semibold me-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-200 dark:text-primary-800 ms-2'),
        cls='flex items-center text-5xl font-extrabold dark:text-white'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Secondary text',
        Span(id='secondary-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Secondary text', href='#secondary-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add a secondary text inside the main heading component.'),
    component_showcase(Div(
    H1(
        'Flowbite',
        Small('This is secondary text', cls='ms-2 font-semibold text-gray-500 dark:text-gray-400'),
        cls='text-5xl font-extrabold dark:text-white'
    )
), code="""Div(
    H1(
        'Flowbite',
        Small('This is secondary text', cls='ms-2 font-semibold text-gray-500 dark:text-gray-400'),
        cls='text-5xl font-extrabold dark:text-white'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The heading component has six levels of importance starting from H1 which has to be unique on the page and has the greatest weight of importance all the way to H6.'),
    H3(
        'Heading one (H1)',
        Span(id='heading-one-h1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading one (H1)', href='#heading-one-h1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the H1 tag as the most important text element to indicate the title of your web page.'),
    component_showcase(Div(
    H1('Heading 1', cls='text-5xl font-extrabold dark:text-white')
), code="""Div(
    H1('Heading 1', cls='text-5xl font-extrabold dark:text-white')
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Heading two (H2)',
        Span(id='heading-two-h2', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading two (H2)', href='#heading-two-h2', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The H2 tag can be used as subtitles of the page’s sections.'),
    component_showcase(Div(
    H2('Heading 2', cls='text-4xl font-bold dark:text-white')
), code="""Div(
    H2('Heading 2', cls='text-4xl font-bold dark:text-white')
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Heading three (H3)',
        Span(id='heading-three-h3', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading three (H3)', href='#heading-three-h3', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the H3 tags inside sections that already have a H2 available.'),
    component_showcase(Div(
    H3('Heading 3', cls='text-3xl font-bold dark:text-white')
), code="""Div(
    H3('Heading 3', cls='text-3xl font-bold dark:text-white')
)""", id="example_11",cls='mt-2 mb-6'),
    H3(
        'Heading four (H4)',
        Span(id='heading-four-h4', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading four (H4)', href='#heading-four-h4', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The H4 can be generally used after H2 and H3 tags are already present and you need a more in-depth hierarchy.'),
    component_showcase(Div(
    H4('Heading 4', cls='text-2xl font-bold dark:text-white')
), code="""Div(
    H4('Heading 4', cls='text-2xl font-bold dark:text-white')
)""", id="example_12",cls='mt-2 mb-6'),
    H3(
        'Heading five (H5)',
        Span(id='heading-five-h5', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading five (H5)', href='#heading-five-h5', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The H5 tag is most often used in longer articles with other heading already available or in sidebars.'),
    component_showcase(Div(
    H5('Heading 5', cls='text-xl font-bold dark:text-white')
), code="""Div(
    H5('Heading 5', cls='text-xl font-bold dark:text-white')
)""", id="example_13",cls='mt-2 mb-6'),
    H3(
        'Heading six (H6)',
        Span(id='heading-six-h6', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Heading six (H6)', href='#heading-six-h6', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Using the H6 tag is quite rare because it means that you’ve already used all heading from H1 to H5, but you can still use it if you have a very complex article with lots of headings.'),
    component_showcase(Div(
    H6('Heading 6', cls='text-lg font-bold dark:text-white')
), code="""Div(
    H6('Heading 6', cls='text-lg font-bold dark:text-white')
)""", id="example_14",cls='mt-2 mb-6'),
    id='mainContent'
)
