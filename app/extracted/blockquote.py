from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('Get started with a collection of blockquote components when quoting external sources such as quotes inside an article, user reviews, and testimonials based on multiple examples of layouts, styles, and contexts.'),
    P(
        'The main',
        Code('<blockquote>'),
        'HTML tag can be used together with the',
        Code('<cite>'),
        'tag or attribute to also mention the source of the quote content.'
    ),
    H2(
        'Default blockquote',
        Span(id='default-blockquote', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default blockquote', href='#default-blockquote', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to quote an external source inside a blockquote element.'),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Solid background',
        Span(id='solid-background', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Solid background', href='#solid-background', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used as an alternative style to the default one by applying a solid background color.'),
    component_showcase(Div(
    P('Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site youâ\x80\x99ve designed? By running a usability test, youâ\x80\x99ll be able to see how users will interact with your design once itâ\x80\x99s live.', cls='text-gray-500 dark:text-gray-400'),
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-xl italic font-medium leading-relaxed text-gray-900 dark:text-white'),
        cls='p-4 my-4 border-s-4 border-gray-300 bg-gray-50 dark:border-gray-500 dark:bg-gray-800'
    ),
    P('First of all you need to understand how Flowbite works. This library is not another framework. Rather, it is a set of components based on Tailwind CSS that you can just copy-paste from the documentation.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site youâ\x80\x99ve designed? By running a usability test, youâ\x80\x99ll be able to see how users will interact with your design once itâ\x80\x99s live.', cls='text-gray-500 dark:text-gray-400'),
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-xl italic font-medium leading-relaxed text-gray-900 dark:text-white'),
        cls='p-4 my-4 border-s-4 border-gray-300 bg-gray-50 dark:border-gray-500 dark:bg-gray-800'
    ),
    P('First of all you need to understand how Flowbite works. This library is not another framework. Rather, it is a set of components based on Tailwind CSS that you can just copy-paste from the documentation.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Blockquote icon',
        Span(id='blockquote-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Blockquote icon', href='#blockquote-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an icon above the blockquote text content.'),
    component_showcase(Div(
    Blockquote(
        Svg(
            Path(d='M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 18 14',
            cls='w-8 h-8 text-gray-400 dark:text-gray-600 mb-4'
        ),
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        Svg(
            Path(d='M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 18 14',
            cls='w-8 h-8 text-gray-400 dark:text-gray-600 mb-4'
        ),
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Paragraph context',
        Span(id='paragraph-context', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph context', href='#paragraph-context', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a blockquote component between multiple paragraph elements.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        Blockquote(
            P('" Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application. "', cls='text-xl italic font-semibold text-gray-900 dark:text-white'),
            cls='mb-3'
        ),
        cls='grid grid-cols-1 md:gap-6 md:grid-cols-2'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        Blockquote(
            P('" Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application. "', cls='text-xl italic font-semibold text-gray-900 dark:text-white'),
            cls='mb-3'
        ),
        cls='grid grid-cols-1 md:gap-6 md:grid-cols-2'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'User testimonial',
        Span(id='user-testimonial', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User testimonial', href='#user-testimonial', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used for user testimonials by mentioning the author and occupation of the author.'),
    component_showcase(Div(
    Figure(
        Svg(
            Path(d='M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 18 14',
            cls='w-10 h-10 mx-auto mb-3 text-gray-400 dark:text-gray-600'
        ),
        Blockquote(
            P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-2xl italic font-medium text-gray-900 dark:text-white')
        ),
        Figcaption(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png', alt='profile picture', cls='w-6 h-6 rounded-full'),
            Div(
                Cite('Michael Gough', cls='pe-3 font-medium text-gray-900 dark:text-white'),
                Cite('CEO at Google', cls='ps-3 text-sm text-gray-500 dark:text-gray-400'),
                cls='flex items-center divide-x-2 rtl:divide-x-reverse divide-gray-500 dark:divide-gray-700'
            ),
            cls='flex items-center justify-center mt-6 space-x-3 rtl:space-x-reverse'
        ),
        cls='max-w-screen-md mx-auto text-center'
    )
), code="""Div(
    Figure(
        Svg(
            Path(d='M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 18 14',
            cls='w-10 h-10 mx-auto mb-3 text-gray-400 dark:text-gray-600'
        ),
        Blockquote(
            P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-2xl italic font-medium text-gray-900 dark:text-white')
        ),
        Figcaption(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png', alt='profile picture', cls='w-6 h-6 rounded-full'),
            Div(
                Cite('Michael Gough', cls='pe-3 font-medium text-gray-900 dark:text-white'),
                Cite('CEO at Google', cls='ps-3 text-sm text-gray-500 dark:text-gray-400'),
                cls='flex items-center divide-x-2 rtl:divide-x-reverse divide-gray-500 dark:divide-gray-700'
            ),
            cls='flex items-center justify-center mt-6 space-x-3 rtl:space-x-reverse'
        ),
        cls='max-w-screen-md mx-auto text-center'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'User Review',
        Span(id='user-review', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: User Review', href='#user-review', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a user review with rating stars and the name and occupation of the author.'),
    component_showcase(Div(
    Figure(
        Div(
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5'
            ),
            cls='flex items-center mb-4 text-yellow-300'
        ),
        Blockquote(
            P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-2xl font-semibold text-gray-900 dark:text-white')
        ),
        Figcaption(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png', alt='profile picture', cls='w-6 h-6 rounded-full'),
            Div(
                Cite('Bonnie Green', cls='pe-3 font-medium text-gray-900 dark:text-white'),
                Cite('CTO at Flowbite', cls='ps-3 text-sm text-gray-500 dark:text-gray-400'),
                cls='flex items-center divide-x-2 rtl:divide-x-reverse divide-gray-300 dark:divide-gray-700'
            ),
            cls='flex items-center mt-6 space-x-3 rtl:space-x-reverse'
        ),
        cls='max-w-screen-md'
    )
), code="""Div(
    Figure(
        Div(
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5 me-1'
            ),
            Svg(
                Path(d='M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 22 20',
                cls='w-5 h-5'
            ),
            cls='flex items-center mb-4 text-yellow-300'
        ),
        Blockquote(
            P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."', cls='text-2xl font-semibold text-gray-900 dark:text-white')
        ),
        Figcaption(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png', alt='profile picture', cls='w-6 h-6 rounded-full'),
            Div(
                Cite('Bonnie Green', cls='pe-3 font-medium text-gray-900 dark:text-white'),
                Cite('CTO at Flowbite', cls='ps-3 text-sm text-gray-500 dark:text-gray-400'),
                cls='flex items-center divide-x-2 rtl:divide-x-reverse divide-gray-300 dark:divide-gray-700'
            ),
            cls='flex items-center mt-6 space-x-3 rtl:space-x-reverse'
        ),
        cls='max-w-screen-md'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Alignment',
        Span(id='alignment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Alignment', href='#alignment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Choose from the following examples the blockquote text alignment from starting from left, center to right based on the utility classes from Tailwind CSS.'),
    H3(
        'Left',
        Span(id='left', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Left', href='#left', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The default alignment of the blockquote text content is the left side of the document.'),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-left text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-left text-gray-900 dark:text-white'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H3(
        'Center',
        Span(id='center', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Center', href='#center', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-center'),
        'class from Tailwind CSS to align the text content inside the blockquote to the center.'
    ),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-center text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-center text-gray-900 dark:text-white'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Right',
        Span(id='right', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Right', href='#right', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-right'),
        'utility class from Tailwind CSS to align the blockquote text content to the right side of the page.'
    ),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-right text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-right text-gray-900 dark:text-white'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Choose from one of the multiple sizes for the default blockquote component based on the surrounding elements and sizes.'),
    H3(
        'Small',
        Span(id='small', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Small', href='#small', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-lg'),
        'font size class from Tailwind CSS to apply the small size for the blockquote component.'
    ),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-lg italic font-semibold text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-lg italic font-semibold text-gray-900 dark:text-white'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Medium',
        Span(id='medium', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Medium', href='#medium', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-xl'),
        'utility class to set the default size for the blockquote element.'
    ),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-gray-900 dark:text-white'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Large',
        Span(id='large', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Large', href='#large', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Code('text-2xl'),
        'class can be used to set a large size for the blockquote component.'
    ),
    component_showcase(Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-2xl italic font-semibold text-gray-900 dark:text-white'
    )
), code="""Div(
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-2xl italic font-semibold text-gray-900 dark:text-white'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    id='mainContent'
)
