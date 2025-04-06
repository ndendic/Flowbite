from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The paragraph element is one of the most commonly used HTML tags on a document page because it is used to write longer blocks of text separated by a blank line and can massively improve the on-page SEO of the page when used correctly.'),
    P('Get started with a collection of paragraph components based on multiple styles, layouts, colors and sizes to use for your website built with the utility classes from Tailwind CSS.'),
    H2(
        'Default paragraph',
        Span(id='default-paragraph', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default paragraph', href='#default-paragraph', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a paragraph element to use inside article content or a landing page.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Leading paragraph',
        Span(id='leading-paragraph', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Leading paragraph', href='#leading-paragraph', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The leading text can be used as the first paragraph inside an article content page.'),
    component_showcase(Div(
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work and deploy.', cls='mb-3 text-lg text-gray-500 md:text-xl dark:text-gray-400'),
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work and deploy.', cls='mb-3 text-lg text-gray-500 md:text-xl dark:text-gray-400'),
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'First letter',
        Span(id='first-letter', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: First letter', href='#first-letter', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to highlight the first letter of the paragraph, often used in e-books and PDF documents.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400 first-line:uppercase first-line:tracking-widest first-letter:text-7xl first-letter:font-bold first-letter:text-gray-900 dark:first-letter:text-gray-100 first-letter:me-3 first-letter:float-start'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400 first-line:uppercase first-line:tracking-widest first-letter:text-7xl first-letter:font-bold first-letter:text-gray-900 dark:first-letter:text-gray-100 first-letter:me-3 first-letter:float-start'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Paragraph link',
        Span(id='paragraph-link', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph link', href='#paragraph-link', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add a custom styled link element inside the paragraph.'),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-medium text-primary-600 underline dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:no-underline'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        A('Link issues across Jira', href='#', cls='font-medium text-primary-600 underline dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:no-underline'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Paragraph bold',
        Span(id='paragraph-bold', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph bold', href='#paragraph-bold', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to highlight a piece of text inside the paragraph by using a bolder font weight.'),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        Strong('Link issues across Jira', cls='font-semibold text-gray-900 dark:text-white'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        Strong('Link issues across Jira', cls='font-semibold text-gray-900 dark:text-white'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Paragraph underline',
        Span(id='paragraph-underline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph underline', href='#paragraph-underline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to underline a certain part of the text inside the paragraph.'),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        U('Link issues across Jira', cls='underline'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        U('Link issues across Jira', cls='underline'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Paragraph italic',
        Span(id='paragraph-italic', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph italic', href='#paragraph-italic', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to make the font style of the text inside the paragraph italic.'),
    component_showcase(Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        Em('Link issues across Jira', cls='font-italic'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    P(
        'Track work across the enterprise through an open, collaborative platform.',
        Em('Link issues across Jira', cls='font-italic'),
        'and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.',
        cls='mb-3 text-gray-500 dark:text-gray-400'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Paragraph popover',
        Span(id='paragraph-popover', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Paragraph popover', href='#paragraph-popover', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with this example to show a popover with extra information inside paragraph elements.'),
    component_showcase(Div(
    P(
        'Due to its central geographic location in Southern Europe,',
        A('Italy', href='#', data_popover_target='popover-image', cls='font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in insular Italy',
        cls='text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('About Italy', cls='font-semibold text-gray-900 dark:text-white'),
                    P('Italy is located in the middle of the Mediterranean Sea, in Southern Europe it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city.'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 6 10',
                            cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                        ),
                        href='#',
                        cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
                    ),
                    cls='space-y-2'
                ),
                cls='col-span-3 p-3'
            ),
            Img(src='/docs/images/popovers/italy.png', alt='Italy map', cls='h-full col-span-2'),
            cls='grid grid-cols-5'
        ),
        Div(data_popper_arrow=True),
        id='popover-image',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-96 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    P(
        'Due to its central geographic location in Southern Europe,',
        A('Italy', href='#', data_popover_target='popover-image', cls='font-medium text-primary-600 underline dark:text-primary-500 hover:no-underline'),
        'has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in insular Italy',
        cls='text-gray-500 dark:text-gray-400'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('About Italy', cls='font-semibold text-gray-900 dark:text-white'),
                    P('Italy is located in the middle of the Mediterranean Sea, in Southern Europe it is also considered part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city.'),
                    A(
                        'Read more',
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 6 10',
                            cls='w-2 h-2 ms-1.5 rtl:rotate-180'
                        ),
                        href='#',
                        cls='flex items-center font-medium text-primary-600 dark:text-primary-500 dark:hover:text-primary-600 hover:text-primary-700 hover:underline'
                    ),
                    cls='space-y-2'
                ),
                cls='col-span-3 p-3'
            ),
            Img(src='/docs/images/popovers/italy.png', alt='Italy map', cls='h-full col-span-2'),
            cls='grid grid-cols-5'
        ),
        Div(data_popper_arrow=True),
        id='popover-image',
        role='tooltip',
        cls='absolute z-10 invisible inline-block text-sm text-gray-500 transition-opacity duration-300 bg-white border border-gray-200 rounded-lg shadow-xs opacity-0 w-96 dark:text-gray-400 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Layout',
        Span(id='layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Layout', href='#layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with examples of layouts for the paragraph component to separate content into multiple rows and columns.'),
    H3(
        'One column',
        Span(id='one-column', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: One column', href='#one-column', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show multiple paragraphs on a single line.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
)""", id="example_8",cls='mt-2 mb-6'),
    H3(
        'Two columns even',
        Span(id='two-columns-even', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Two columns even', href='#two-columns-even', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to separate paragraphs into two columns for better readability.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-2'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-2'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Three columns even',
        Span(id='three-columns-even', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Three columns even', href='#three-columns-even', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to separate paragraphs into three separate columns.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-3'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-3'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Two columns uneven',
        Span(id='two-columns-uneven', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Two columns uneven', href='#two-columns-uneven', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to separate paragraphs into two uneven columns.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        Div(
            P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
            P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
            cls='col-span-2'
        ),
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-3'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
    Div(
        Div(
            P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
            P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400'),
            cls='col-span-2'
        ),
        P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-gray-500 dark:text-gray-400'),
        cls='grid grid-cols-1 gap-6 sm:grid-cols-3'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='mb-3 text-gray-500 dark:text-gray-400')
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Text alignment',
        Span(id='text-alignment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Text alignment', href='#text-alignment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Align the paragraph component to the left (default), center or right side of the document page using the',
        Code('text-{left|center|right}'),
        'utility class from Tailwind CSS.'
    ),
    H3(
        'Left',
        Span(id='left', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Left', href='#left', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The default alignment of the paragraph is to the left side and you can use the',
        Code('text-left'),
        'class to align it manually.'
    ),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-left rtl:text-right text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-left rtl:text-right text-gray-500 dark:text-gray-400')
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
        'class to align the paragraph text to the center.'
    ),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-center text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-center text-gray-500 dark:text-gray-400')
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
        'utility class to align the paragraph text the right side of the page.'
    ),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-right rtl:text-left text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='mb-3 text-right rtl:text-left text-gray-500 dark:text-gray-400')
)""", id="example_14",cls='mt-2 mb-6'),
    id='mainContent'
)
