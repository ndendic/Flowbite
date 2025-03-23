from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The HR component can be used to separate content using a horizontal line by adding space between elements based on multiple styles, variants, and layouts.'),
    H2(
        'Default HR',
        Span(id='default-hr', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default HR', href='#default-hr', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to separate text content with a',
        Code('Hr'),
        'horizontal line.'
    ),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Divider(),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Divider(),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Trimmed',
        Span(id='trimmed', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Trimmed', href='#trimmed', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a shorter version of the horizontal line.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Divider(cls=DividerT.trimmed),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Divider(cls=DividerT.trimmed),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every change.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Icon HR',
        Span(id='icon-hr', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Icon HR', href='#icon-hr', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to set a custom',
        A('SVG icon', href='https://flowbite.com/icons/'),
        'in the middle of the HR element.'
    ),
    component_showcase(
        Div(
            P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
            DividerSplit(Icon("quote")),
            P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil.', cls='text-gray-500 dark:text-gray-400')
        ), 
        code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Div(
        Hr(cls='w-64 h-1 my-8 bg-gray-200 border-0 rounded-sm dark:bg-gray-700'),
        Div(
            Svg(
                Path(d='M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 18 14',
                cls='w-4 h-4 text-gray-700 dark:text-gray-300'
            ),
            cls='absolute px-4 -translate-x-1/2 bg-white left-1/2 dark:bg-gray-900'
        ),
        cls='inline-flex items-center justify-center w-full'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'HR with text',
        Span(id='hr-with-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: HR with text', href='#hr-with-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to add a text in the middle of the HR component.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Div(
        Hr(cls='w-64 h-px my-8 bg-gray-200 border-0 dark:bg-gray-700'),
        Span('or', cls='absolute px-3 font-medium text-gray-900 -translate-x-1/2 bg-white left-1/2 dark:text-white dark:bg-gray-900'),
        cls='inline-flex items-center justify-center w-full'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil.', cls='text-gray-500 dark:text-gray-400')
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Div(
        Hr(cls='w-64 h-px my-8 bg-gray-200 border-0 dark:bg-gray-700'),
        Span('or', cls='absolute px-3 font-medium text-gray-900 -translate-x-1/2 bg-white left-1/2 dark:text-white dark:bg-gray-900'),
        cls='inline-flex items-center justify-center w-full'
    ),
    P('Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate critical development work, eliminate toil.', cls='text-gray-500 dark:text-gray-400')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'HR shape',
        Span(id='hr-shape', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: HR shape', href='#hr-shape', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to separate content with a HR tag as a shape instead of a line.'),
    component_showcase(Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Hr(cls='w-8 h-8 mx-auto my-8 bg-gray-200 border-0 rounded-sm md:my-12 dark:bg-gray-700'),
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-center text-gray-900 dark:text-white'
    )
), code="""Div(
    P('Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest data from other software development tools, so your IT support and operations teams have richer contextual information to rapidly respond to requests, incidents, and changes.', cls='text-gray-500 dark:text-gray-400'),
    Hr(cls='w-8 h-8 mx-auto my-8 bg-gray-200 border-0 rounded-sm md:my-12 dark:bg-gray-700'),
    Blockquote(
        P('"Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to complex dashboard. Perfect choice for your next SaaS application."'),
        cls='text-xl italic font-semibold text-center text-gray-900 dark:text-white'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
