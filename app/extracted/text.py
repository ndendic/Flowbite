from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('Get started with a collection of text customization examples to learn how to update the size, font weight, style, decoration and spacing of inline text elements using Tailwind CSS.'),
    H2(
        'Font size',
        Span(id='font-size', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Font size', href='#font-size', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to set the font size of inline text elements using the',
        Code('text-{size}'),
        'class.'
    ),
    component_showcase(Div(
    P('Aa', cls='text-xs text-gray-900 dark:text-white'),
    P('Aa', cls='text-sm text-gray-900 dark:text-white'),
    P('Aa', cls='text-base text-gray-900 dark:text-white'),
    P('Aa', cls='text-lg text-gray-900 dark:text-white'),
    P('Aa', cls='text-xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-2xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-3xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-5xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-6xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-gray-900 text-7xl dark:text-white'),
    P('Aa', cls='text-gray-900 text-8xl dark:text-white'),
    P('Aa', cls='text-gray-900 text-9xl dark:text-white')
), code="""Div(
    P('Aa', cls='text-xs text-gray-900 dark:text-white'),
    P('Aa', cls='text-sm text-gray-900 dark:text-white'),
    P('Aa', cls='text-base text-gray-900 dark:text-white'),
    P('Aa', cls='text-lg text-gray-900 dark:text-white'),
    P('Aa', cls='text-xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-2xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-3xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-5xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-6xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-gray-900 text-7xl dark:text-white'),
    P('Aa', cls='text-gray-900 text-8xl dark:text-white'),
    P('Aa', cls='text-gray-900 text-9xl dark:text-white')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Font weight',
        Span(id='font-weight', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Font weight', href='#font-weight', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to the font weight of an inline text element using the',
        Code('font-{size}'),
        'class.'
    ),
    component_showcase(Div(
    P('Aa', cls='text-4xl font-thin text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 font-extralight dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-normal text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-medium text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-semibold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-bold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-extrabold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-black text-gray-900 dark:text-white')
), code="""Div(
    P('Aa', cls='text-4xl font-thin text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 font-extralight dark:text-white'),
    P('Aa', cls='text-4xl text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-normal text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-medium text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-semibold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-bold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-extrabold text-gray-900 dark:text-white'),
    P('Aa', cls='text-4xl font-black text-gray-900 dark:text-white')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Text color',
        Span(id='text-color', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text color', href='#text-color', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-{color}'),
        'classes from Tailwind CSS to set the color of the inline text.'
    ),
    component_showcase(Div(
    P('This text is in the primary color.', cls='text-primary-600'),
    P('This text is in the green color.', cls='text-green-500'),
    P('This text is in the red color.', cls='text-red-600'),
    P('This text is in the purple color.', cls='text-purple-600'),
    P('This text is in the teal color.', cls='text-teal-600')
), code="""Div(
    P('This text is in the primary color.', cls='text-primary-600'),
    P('This text is in the green color.', cls='text-green-500'),
    P('This text is in the red color.', cls='text-red-600'),
    P('This text is in the purple color.', cls='text-purple-600'),
    P('This text is in the teal color.', cls='text-teal-600')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Letter spacing',
        Span(id='letter-spacing', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Letter spacing', href='#letter-spacing', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Increase or decrease the spacing between letters using the',
        Code('tracking-{type}'),
        'class.'
    ),
    component_showcase(Div(
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-tighter text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-tight text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-normal text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-wide text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-wider text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-widest text-gray-500 md:text-lg dark:text-gray-400')
), code="""Div(
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-tighter text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-tight text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-normal text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-wide text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-wider text-gray-500 md:text-lg dark:text-gray-400'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='tracking-widest text-gray-500 md:text-lg dark:text-gray-400')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Text Decoration',
        Span(id='text-decoration', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text Decoration', href='#text-decoration', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Set decoration for the inline text elements such as underline, line through or uppercase using classes from Tailwind CSS.'),
    H3(
        'Underline',
        Span(id='underline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Underline', href='#underline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Underline text by using the',
        Code('underline'),
        'class or disable it using',
        Code('no-underline'),
        '.'
    ),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-indigo-500'),
        'and ingest data from other',
        A(
            'software development',
            A(
                'tools, so your IT support and operations teams have richer contextual information to rapidly respond to',
                A('requests', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-green-500'),
                ',',
                A('incidents', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-red-500'),
                ', and',
                A('changes', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-sky-500'),
                '.'
            ),
            href='#',
            cls='font-semibold text-gray-900 underline dark:text-white decoration-primary-500'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-indigo-500'),
        'and ingest data from other',
        A(
            'software development',
            A(
                'tools, so your IT support and operations teams have richer contextual information to rapidly respond to',
                A('requests', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-green-500'),
                ',',
                A('incidents', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-red-500'),
                ', and',
                A('changes', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-sky-500'),
                '.'
            ),
            href='#',
            cls='font-semibold text-gray-900 underline dark:text-white decoration-primary-500'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H3(
        'Line through',
        Span(id='line-through', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Line through', href='#line-through', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Set a strikethrough line on a text element using the',
        Code('line-through'),
        'class.'
    ),
    component_showcase(Div(
    Span('$109', cls='text-lg font-medium text-gray-900 line-through dark:text-white'),
    Span('$79', cls='ms-3 text-lg font-medium text-gray-900 dark:text-white')
), code="""Div(
    Span('$109', cls='text-lg font-medium text-gray-900 line-through dark:text-white'),
    Span('$79', cls='ms-3 text-lg font-medium text-gray-900 dark:text-white')
)""", id="example_5",cls='mt-2 mb-6'),
    H3(
        'Uppercase',
        Span(id='uppercase', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Uppercase', href='#uppercase', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Force uppercase characters for a given portion of text using the',
        Code('uppercase'),
        'class.'
    ),
    component_showcase(Div(
    P(
        'The crypto',
        Span('identity', cls='uppercase'),
        'primitive.',
        cls='text-lg font-medium text-gray-900 dark:text-white'
    )
), code="""Div(
    P(
        'The crypto',
        Span('identity', cls='uppercase'),
        'primitive.',
        cls='text-lg font-medium text-gray-900 dark:text-white'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Font style',
        Span(id='font-style', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Font style', href='#font-style', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Set italic or non italic styles with the utility classes from Tailwind CSS.'),
    H3(
        'Italic',
        Span(id='italic', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Italic', href='#italic', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('italic'),
        'class from Tailwind CSS to set italic font style to a text element.'
    ),
    component_showcase(Div(
    P(
        'The crypto',
        Span('identity', cls='italic'),
        'primitive.',
        cls='text-lg font-medium text-gray-900 dark:text-white'
    )
), code="""Div(
    P(
        'The crypto',
        Span('identity', cls='italic'),
        'primitive.',
        cls='text-lg font-medium text-gray-900 dark:text-white'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Normal',
        Span(id='normal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Normal', href='#normal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Text elements by default are non-italic.'),
    component_showcase(Div(
    P('The crypto identity primitive.', cls='text-lg font-medium text-gray-900 dark:text-white')
), code="""Div(
    P('The crypto identity primitive.', cls='text-lg font-medium text-gray-900 dark:text-white')
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Line Height',
        Span(id='line-height', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Line Height', href='#line-height', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Set the height between lines using the',
        Code('leading-{type}'),
        'classes from Tailwind CSS.'
    ),
    H3(
        'Leading normal',
        Span(id='leading-normal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Leading normal', href='#leading-normal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('leading-normal'),
        'class to set default line height.'
    ),
    component_showcase(Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-normal text-gray-900 dark:text-white')
), code="""Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-normal text-gray-900 dark:text-white')
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Leading relaxed',
        Span(id='leading-relaxed', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Leading relaxed', href='#leading-relaxed', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('leading-relaxed'),
        'class to increase the space between lines.'
    ),
    component_showcase(Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-relaxed text-gray-900 dark:text-white')
), code="""Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-relaxed text-gray-900 dark:text-white')
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Leading loose',
        Span(id='leading-loose', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Leading loose', href='#leading-loose', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('leading-loose'),
        'class to set a large amount of space between text lines.'
    ),
    component_showcase(Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-loose text-gray-900 dark:text-white')
), code="""Div(
    P('The Al-powered app will help you improve yourself by analysing your everyday life.', cls='max-w-lg text-3xl font-semibold leading-loose text-gray-900 dark:text-white')
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Text Align',
        Span(id='text-align', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text Align', href='#text-align', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples to align the text content to the left, center, or right side of the page.'),
    H3(
        'Left',
        Span(id='left', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Left', href='#left', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-left'),
        'class to align the text to the left side of the page.'
    ),
    component_showcase(Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-left rtl:text-right text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-left rtl:text-right text-gray-500 dark:text-gray-400')
)""", id="example_12",cls='mt-2 mb-6'),
    H3(
        'Center',
        Span(id='center', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Center', href='#center', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-center'),
        'class to align the text content to the center of the page.'
    ),
    component_showcase(Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-center text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-center text-gray-500 dark:text-gray-400')
)""", id="example_13",cls='mt-2 mb-6'),
    H3(
        'Right',
        Span(id='right', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Right', href='#right', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-right'),
        'class to align the text element to the right side of the page.'
    ),
    component_showcase(Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-right rtl:text-left text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-right rtl:text-left text-gray-500 dark:text-gray-400')
)""", id="example_14",cls='mt-2 mb-6'),
    H3(
        'Text justify',
        Span(id='text-justify', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text justify', href='#text-justify', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-justify'),
        'class to justify the text content.'
    ),
    component_showcase(Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-justify text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Get started with an enterprise-level, professionally designed, fully responsive, and HTML semantic set of web pages, sections and over 400+ components crafted with the utility classes from Tailwind CSS and based on the Fastbite component library', cls='text-justify text-gray-500 dark:text-gray-400')
)""", id="example_15",cls='mt-2 mb-6'),
    H2(
        'Whitespace',
        Span(id='whitespace', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Whitespace', href='#whitespace', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Configure the whitespace behaviour of inline text elements using classes from Tailwind CSS.'),
    H3(
        'Normal',
        Span(id='normal-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Normal', href='#normal-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('whitespace-normal'),
        'class to set the default whitespace behaviour.'
    ),
    component_showcase(Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-normal dark:text-gray-400'
    )
), code="""Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-normal dark:text-gray-400'
    )
)""", id="example_16",cls='mt-2 mb-6'),
    H3(
        'Nowrap',
        Span(id='nowrap', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Nowrap', href='#nowrap', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('whitespace-nowrap'),
        'class to prevent text being added to a new line when the full width has been reached.'
    ),
    component_showcase(Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-nowrap dark:text-gray-400'
    )
), code="""Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-nowrap dark:text-gray-400'
    )
)""", id="example_17",cls='mt-2 mb-6'),
    H3(
        'Pre line',
        Span(id='pre-line', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pre line', href='#pre-line', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('whitespace-pre-line'),
        'class to add whitespace exactly how it has been set from the source code.'
    ),
    component_showcase(Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-pre-line dark:text-gray-400'
    )
), code="""Div(
    P(
        'This is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.\nThis is some text. This is some text. This is some text.',
        P(),
        cls='text-gray-500 whitespace-pre-line dark:text-gray-400'
    )
)""", id="example_18",cls='mt-2 mb-6'),
    H2(
        'Text Decoration Style',
        Span(id='text-decoration-style', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text Decoration Style', href='#text-decoration-style', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Update the text decoration style using the',
        Code('decoration-{*}'),
        'classes from Tailwind CSS.'
    ),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-indigo-500'),
        'and ingest data from other',
        A(
            'software development',
            A(
                'tools, so your IT support and operations teams have richer contextual information to rapidly respond to',
                A('requests', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-green-500 decoration-dotted'),
                ',',
                A('incidents', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-red-500 decoration-dashed'),
                ', and',
                A('changes', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-sky-500 decoration-wavy'),
                '.'
            ),
            href='#',
            cls='font-semibold text-gray-900 underline dark:text-white decoration-primary-500 decoration-double'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-indigo-500'),
        'and ingest data from other',
        A(
            'software development',
            A(
                'tools, so your IT support and operations teams have richer contextual information to rapidly respond to',
                A('requests', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-green-500 decoration-dotted'),
                ',',
                A('incidents', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-red-500 decoration-dashed'),
                ', and',
                A('changes', href='#', cls='font-semibold text-gray-900 underline dark:text-white decoration-sky-500 decoration-wavy'),
                '.'
            ),
            href='#',
            cls='font-semibold text-gray-900 underline dark:text-white decoration-primary-500 decoration-double'
        ),
        cls='text-gray-500 dark:text-gray-400'
    )
)""", id="example_19",cls='mt-2 mb-6'),
    H2(
        'Opacity',
        Span(id='opacity', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Opacity', href='#opacity', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('text-{color}-{opacity}'),
        'class from Tailwind CSS to set the opacity of inline text elements.'
    ),
    component_showcase(Div(
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/100 dark:text-primary-500/100'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/75 dark:text-primary-500/75'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/50 dark:text-primary-500/50'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/25 dark:text-primary-500/25')
), code="""Div(
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/100 dark:text-primary-500/100'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/75 dark:text-primary-500/75'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/50 dark:text-primary-500/50'),
    P('Fastbite app will help you improve yourself by analysing your everyday life.', cls='text-xl font-semibold text-primary-600/25 dark:text-primary-500/25')
)""", id="example_20",cls='mt-2 mb-6'),
    id='mainContent'
)
