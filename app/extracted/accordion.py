from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.components import CodeSpan as Code
from utils import component_showcase

component = Div(
    P('The accordion component is a collection of vertically collapsing header and body elements that can be used to show and hide information based on the Tailwind CSS utility classes and JavaScript from Flowbite.'),
    P('A popular use case would be the “Frequently Asked Questions” section of a website or page when you can show questions and answers for each child element.'),
    P('There are two main options to initialize the accordion component:'),
    Ul(
        Li(
            Code('data-accordion="collapse"'),
            'show only one active child element'
        ),
        Li(
            Code('data-accordion="open"'),
            'keep multiple elements open'
        )
    ),
    P(
        'Don’t forget to set the ',
        Code('data-accordion-target="{selector}"'),
        ' data attribute to the header element where the value is the id or class of the accordion body element and the',
        Code('aria-expanded="{true|false}"'),
        ' attribute to mark the active or inactive state of the accordion.'
    ),
    H2(
        'Default accordion',
        Span(id='default-accordion', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default accordion', href='#default-accordion', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the ',
        Code('data-accordion="collapse"'),
        ' to collapse every other child element when expanding a single one.'
    ),
    component_showcase(Div(
    Div(
        H2(
            Div(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                # shape=Round.none,
                type='button',
                data_accordion_target='#accordion-collapse-body-1',
                aria_expanded='true',
                aria_controls='accordion-collapse-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-collapse-body-1',
            aria_labelledby='accordion-collapse-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-2',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-2',
            aria_labelledby='accordion-collapse-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-3',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-3',
            aria_labelledby='accordion-collapse-heading-3',
            cls='hidden'
        ),
        id='accordion-collapse',
        data_accordion='collapse'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-1',
                aria_expanded='true',
                aria_controls='accordion-collapse-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-collapse-body-1',
            aria_labelledby='accordion-collapse-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-2',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-2',
            aria_labelledby='accordion-collapse-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-3',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-3',
            aria_labelledby='accordion-collapse-heading-3',
            cls='hidden'
        ),
        id='accordion-collapse',
        data_accordion='collapse'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Always open',
        Span(id='always-open', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Always open', href='#always-open', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-accordion="open"'),
        'option to keep previously opened accordion elements unchanged.'
    ),
    component_showcase(Div(
    Div(
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'What is Flowbite?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-1',
                aria_expanded='true',
                aria_controls='accordion-open-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-open-body-1',
            aria_labelledby='accordion-open-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'Is there a Figma file available?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-2',
                aria_expanded='false',
                aria_controls='accordion-open-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-open-body-2',
            aria_labelledby='accordion-open-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'What are the differences between Flowbite and Tailwind UI?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-3',
                aria_expanded='false',
                aria_controls='accordion-open-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-open-body-3',
            aria_labelledby='accordion-open-heading-3',
            cls='hidden'
        ),
        id='accordion-open',
        data_accordion='open'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'What is Flowbite?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-1',
                aria_expanded='true',
                aria_controls='accordion-open-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-open-body-1',
            aria_labelledby='accordion-open-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'Is there a Figma file available?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-2',
                aria_expanded='false',
                aria_controls='accordion-open-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-open-body-2',
            aria_labelledby='accordion-open-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span(
                    Svg(
                        Path(fill_rule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clip_rule='evenodd'),
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-5 h-5 me-2 shrink-0'
                    ),
                    'What are the differences between Flowbite and Tailwind UI?',
                    cls='flex items-center'
                ),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-open-body-3',
                aria_expanded='false',
                aria_controls='accordion-open-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-open-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-open-body-3',
            aria_labelledby='accordion-open-heading-3',
            cls='hidden'
        ),
        id='accordion-open',
        data_accordion='open'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Color options',
        Span(id='color-options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Color options', href='#color-options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-active-classes'),
        'and',
        Code('data-inactive-classes'),
        'to set the active and inactive classes for the header element whenever the accordion is expanded by applying as many classes as you want, but make sure to separate them with a space. If the data attribute is not set or empty, it will apply the default classes.'
    ),
    P('Here’s an example where we apply the primary colors instead of gray:'),
    component_showcase(Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-1',
                aria_expanded='true',
                aria_controls='accordion-color-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-color-body-1',
            aria_labelledby='accordion-color-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-2',
                aria_expanded='false',
                aria_controls='accordion-color-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-color-body-2',
            aria_labelledby='accordion-color-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-3',
                aria_expanded='false',
                aria_controls='accordion-color-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-color-body-3',
            aria_labelledby='accordion-color-heading-3',
            cls='hidden'
        ),
        id='accordion-color',
        data_accordion='collapse',
        data_active_classes='bg-primary-100 dark:bg-gray-800 text-primary-600 dark:text-white'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-1',
                aria_expanded='true',
                aria_controls='accordion-color-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-color-body-1',
            aria_labelledby='accordion-color-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-2',
                aria_expanded='false',
                aria_controls='accordion-color-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-color-body-2',
            aria_labelledby='accordion-color-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-color-body-3',
                aria_expanded='false',
                aria_controls='accordion-color-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-800 dark:border-gray-700 dark:text-gray-400 hover:bg-primary-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-color-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-color-body-3',
            aria_labelledby='accordion-color-heading-3',
            cls='hidden'
        ),
        id='accordion-color',
        data_accordion='collapse',
        data_active_classes='bg-primary-100 dark:bg-gray-800 text-primary-600 dark:text-white'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Flush accordion',
        Span(id='flush-accordion', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Flush accordion', href='#flush-accordion', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to remove the background color and rounded borders from the accordion component.'),
    component_showcase(Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-1',
                aria_expanded='true',
                aria_controls='accordion-flush-body-1',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-1',
            aria_labelledby='accordion-flush-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-2',
                aria_expanded='false',
                aria_controls='accordion-flush-body-2',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-2',
            aria_labelledby='accordion-flush-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-3',
                aria_expanded='false',
                aria_controls='accordion-flush-body-3',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-3',
            aria_labelledby='accordion-flush-heading-3',
            cls='hidden'
        ),
        id='accordion-flush',
        data_accordion='collapse',
        data_active_classes='bg-white dark:bg-gray-900 text-gray-900 dark:text-white',
        data_inactive_classes='text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-1',
                aria_expanded='true',
                aria_controls='accordion-flush-body-1',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-1',
            aria_labelledby='accordion-flush-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-2',
                aria_expanded='false',
                aria_controls='accordion-flush-body-2',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-2',
            aria_labelledby='accordion-flush-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('What are the differences between Flowbite and Tailwind UI?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-flush-body-3',
                aria_expanded='false',
                aria_controls='accordion-flush-body-3',
                cls='flex items-center justify-between w-full py-5 font-medium rtl:text-right text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400 gap-3'
            ),
            id='accordion-flush-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='py-5 border-b border-gray-200 dark:border-gray-700'
            ),
            id='accordion-flush-body-3',
            aria_labelledby='accordion-flush-heading-3',
            cls='hidden'
        ),
        id='accordion-flush',
        data_accordion='collapse',
        data_active_classes='bg-white dark:bg-gray-900 text-gray-900 dark:text-white',
        data_inactive_classes='text-gray-500 dark:text-gray-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Arrow style',
        Span(id='arrow-style', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Arrow style', href='#arrow-style', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-accordion-icon'),
        'data attribute to optionally set an element to rotate 180 degrees when the accordion element is expanded. If the data attribute is not set, then it will not rotate.'
    ),
    component_showcase(Div(
    Div(
        H2(
            Button(
                Span('Accordion without an arrow'),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-1',
                aria_expanded='true',
                aria_controls='accordion-arrow-icon-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-900 bg-gray-100 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-arrow-icon-body-1',
            aria_labelledby='accordion-arrow-icon-heading-1'
        ),
        H2(
            Button(
                Span('Accordion with another icon'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-4 h-4 shrink-0 -me-0.5'
                ),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-2',
                aria_expanded='false',
                aria_controls='accordion-arrow-icon-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-arrow-icon-body-2',
            aria_labelledby='accordion-arrow-icon-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Accordion without arrow rotation'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-3',
                aria_expanded='false',
                aria_controls='accordion-arrow-icon-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-arrow-icon-body-3',
            aria_labelledby='accordion-arrow-icon-heading-3',
            cls='hidden'
        ),
        id='accordion-arrow-icon',
        data_accordion='open'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span('Accordion without an arrow'),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-1',
                aria_expanded='true',
                aria_controls='accordion-arrow-icon-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-900 bg-gray-100 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-arrow-icon-body-1',
            aria_labelledby='accordion-arrow-icon-heading-1'
        ),
        H2(
            Button(
                Span('Accordion with another icon'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-4 h-4 shrink-0 -me-0.5'
                ),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-2',
                aria_expanded='false',
                aria_controls='accordion-arrow-icon-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-arrow-icon-body-2',
            aria_labelledby='accordion-arrow-icon-heading-2',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Accordion without arrow rotation'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-arrow-icon-body-3',
                aria_expanded='false',
                aria_controls='accordion-arrow-icon-body-3',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-arrow-icon-heading-3'
        ),
        Div(
            Div(
                P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                Ul(
                    Li(
                        A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    Li(
                        A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                    ),
                    cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                ),
                cls='p-5 border border-t-0 border-gray-200 dark:border-gray-700'
            ),
            id='accordion-arrow-icon-body-3',
            aria_labelledby='accordion-arrow-icon-heading-3',
            cls='hidden'
        ),
        id='accordion-arrow-icon',
        data_accordion='open'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Nesting accordions',
        Span(id='nesting-accordions', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Nesting accordions', href='#nesting-accordions', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Accordions can be nested. All of the mentioned options are supported.'),
    P(
        'To enable nested accordions you need to wrap the nested accordion in an element with the',
        Code('data-accordion'),
        'attribute and don’t accidentally initialize an accordion with nested accordions’ items (e.g. by using',
        Code('$accordionBodyEl.querySelectorAll'),
        '), when using',
        A('custom JavaScript', href='#javascript-behaviour'),
        '.'
    ),
    component_showcase(Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-1',
                aria_expanded='true',
                aria_controls='accordion-collapse-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='mb-2 text-gray-500 dark:text-gray-400'
                ),
                P('What are the differences between Flowbite and Tailwind UI?', cls='mb-4 text-gray-500 dark:text-gray-400'),
                Div(
                    H2(
                        Button(
                            Span('Open source'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-1',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-1',
                            cls='flex items-center justify-between w-full p-5 rounded-t-xl font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-1'
                    ),
                    Div(
                        Div(
                            P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product.', cls='text-gray-500 dark:text-gray-400'),
                            cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-1',
                        aria_labelledby='accordion-nested-collapse-heading-1',
                        cls='hidden'
                    ),
                    H2(
                        Button(
                            Span('Architecture'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-2',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-2',
                            cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-2'
                    ),
                    Div(
                        Div(
                            P('Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='text-gray-500 dark:text-gray-400'),
                            cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-2',
                        aria_labelledby='accordion-nested-collapse-heading-2',
                        cls='hidden'
                    ),
                    H2(
                        Button(
                            Span('Can I use both?'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-3',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-3',
                            cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-3'
                    ),
                    Div(
                        Div(
                            P('We actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                            P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                            Ul(
                                Li(
                                    A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                                ),
                                Li(
                                    A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                                ),
                                cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                            ),
                            cls='p-5 border border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-3',
                        aria_labelledby='accordion-nested-collapse-heading-3',
                        cls='hidden'
                    ),
                    id='accordion-nested-collapse',
                    data_accordion='collapse'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-collapse-body-1',
            aria_labelledby='accordion-collapse-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-2',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-2',
            aria_labelledby='accordion-collapse-heading-2',
            cls='hidden'
        ),
        id='accordion-nested-parent',
        data_accordion='collapse'
    )
), code="""Div(
    Div(
        H2(
            Button(
                Span('What is Flowbite?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-1',
                aria_expanded='true',
                aria_controls='accordion-collapse-body-1',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-1'
        ),
        Div(
            Div(
                P('Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out this guide to learn how to',
                    A('get started', href='/docs/getting-started/introduction/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'and start developing websites even faster with components on top of Tailwind CSS.',
                    cls='mb-2 text-gray-500 dark:text-gray-400'
                ),
                P('What are the differences between Flowbite and Tailwind UI?', cls='mb-4 text-gray-500 dark:text-gray-400'),
                Div(
                    H2(
                        Button(
                            Span('Open source'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-1',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-1',
                            cls='flex items-center justify-between w-full p-5 rounded-t-xl font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-1'
                    ),
                    Div(
                        Div(
                            P('The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product.', cls='text-gray-500 dark:text-gray-400'),
                            cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-1',
                        aria_labelledby='accordion-nested-collapse-heading-1',
                        cls='hidden'
                    ),
                    H2(
                        Button(
                            Span('Architecture'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-2',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-2',
                            cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-2'
                    ),
                    Div(
                        Div(
                            P('Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.', cls='text-gray-500 dark:text-gray-400'),
                            cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-2',
                        aria_labelledby='accordion-nested-collapse-heading-2',
                        cls='hidden'
                    ),
                    H2(
                        Button(
                            Span('Can I use both?'),
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                                data_accordion_icon=True,
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 10 6',
                                cls='w-3 h-3 rotate-180 shrink-0'
                            ),
                            type='button',
                            data_accordion_target='#accordion-nested-collapse-body-3',
                            aria_expanded='false',
                            aria_controls='accordion-nested-collapse-body-3',
                            cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
                        ),
                        id='accordion-nested-collapse-heading-3'
                    ),
                    Div(
                        Div(
                            P('We actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                            P('Learn more about these technologies:', cls='mb-2 text-gray-500 dark:text-gray-400'),
                            Ul(
                                Li(
                                    A('Flowbite Pro', href='https://flowbite.com/pro/', cls='text-primary-600 dark:text-primary-500 hover:underline')
                                ),
                                Li(
                                    A('Tailwind UI', href='https://tailwindui.com/', rel='nofollow', cls='text-primary-600 dark:text-primary-500 hover:underline')
                                ),
                                cls='ps-5 text-gray-500 list-disc dark:text-gray-400'
                            ),
                            cls='p-5 border border-gray-200 dark:border-gray-700'
                        ),
                        id='accordion-nested-collapse-body-3',
                        aria_labelledby='accordion-nested-collapse-heading-3',
                        cls='hidden'
                    ),
                    id='accordion-nested-collapse',
                    data_accordion='collapse'
                ),
                cls='p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900'
            ),
            id='accordion-collapse-body-1',
            aria_labelledby='accordion-collapse-heading-1',
            cls='hidden'
        ),
        H2(
            Button(
                Span('Is there a Figma file available?'),
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
                    data_accordion_icon=True,
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-3 h-3 rotate-180 shrink-0'
                ),
                type='button',
                data_accordion_target='#accordion-collapse-body-2',
                aria_expanded='false',
                aria_controls='accordion-collapse-body-2',
                cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
            ),
            id='accordion-collapse-heading-2'
        ),
        Div(
            Div(
                P('Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.', cls='mb-2 text-gray-500 dark:text-gray-400'),
                P(
                    'Check out the',
                    A('Figma design system', href='https://flowbite.com/figma/', cls='text-primary-600 dark:text-primary-500 hover:underline'),
                    'based on the utility classes from Tailwind CSS and components from Flowbite.',
                    cls='text-gray-500 dark:text-gray-400'
                ),
                cls='p-5 border border-gray-200 dark:border-gray-700'
            ),
            id='accordion-collapse-body-2',
            aria_labelledby='accordion-collapse-heading-2',
            cls='hidden'
        ),
        id='accordion-nested-parent',
        data_accordion='collapse'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('Accordion'),
        'object from Flowbite to create a collection of vertically collapsing heading and content elements using object parameters, options, methods, and callback functions directly from JavaScript.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Create a new Accordion object by passing an array of accordion items and an optional options object to customize the styles and add callback functions.'),
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
                        Code('accordionEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('The parent HTML element of the accordion component.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('items', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Array of accordion items objects including the unique identifier, heading element, content element, and the active state.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Object of options that you can set to customize the style of the accordion items and set callback functions.', cls='px-6 py-4'),
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
            cls='w-full text-sm rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following options as the second parameter for the Accordion object to customize the behaviour, styles, and to set callback functions.'),
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
                        Code('alwaysOpen', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Boolean', cls='px-6 py-4'),
                    Td("If set to true then multiple accordion elements can be open at the same time. By default it's false.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('activeClasses', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4'),
                    Td('Set an array of Tailwind CSS class names to apply for the active accordion heading element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('inactiveClasses', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Array', cls='px-6 py-4'),
                    Td('Apply an array of Tailwind CSS class names to apply for the inactive accordion heading elements.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onOpen', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when a new accordion item has been opened.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onClose', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when a new accordion item has been closed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Methods',
        Span(id='methods', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Methods', href='#methods', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the object methods on the Accordion object to programmatically open, close, or toggle the visibility of a given accordion item.'),
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
                        Code('toggle(id)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to toggle an accordion item based on its current state.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('open(id)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to open an accordion item based on the id.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('close(id)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to close an accordion item based on the id.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnOpen(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when an accordion item has been opened.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnClose(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when an accordion item has been closed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnToggle(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a callback function when an accordion item has been toggled.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm rtl:text-right text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Example',
        Span(id='example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Example', href='#example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Learn more about using the Accordion object from Flowbite in this example in JavaScript.'),
    P('To get started you need to create an array of accordion item objects including a unique identifier (it can be a number as well), a trigger element (eg. a button), a content element (the content body), and the active state.'),
    P('Additionally, you can also set some options to change the default behaviour of the accordion, customize the styles, and set callback functions.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('accordionElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'accordion-example'", cls='s1'),
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
                        Span('// create an array of objects with the id, trigger element (eg. button), and the content element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('accordionItems', cls='nx'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-1'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-2'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-3'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}', cls='p'),
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
                        Span('alwaysOpen', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'text-gray-500 dark:text-gray-400'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onOpen', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been shown'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span('onClose', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been hidden'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span('onToggle', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been toggled'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span("'accordion-example'", cls='s1'),
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
    P('Create a new Accordion object using the options set above as the parameters.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Accordion', cls='nx'),
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
                        Span('/*', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* accordionEl: HTML element (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* accordionItems: array of accordion item objects (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('*/', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('accordion', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Accordion', cls='nx'),
                        Span('(', cls='p'),
                        Span('accordionElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('accordionItems', cls='nx'),
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
    P('Now you can access the object methods to programmatically open, close, and toggle the accordion items based on the unique identifier.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// open accordion item based on id', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('open', cls='nx'),
                        Span('(', cls='p'),
                        Span("'accordion-example-heading-2'", cls='s1'),
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
                        Span('// close accordion item based on id', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('close', cls='nx'),
                        Span('(', cls='p'),
                        Span("'accordion-example-heading-2'", cls='s1'),
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
                        Span('// toggle visibility of item based on id', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('toggle', cls='nx'),
                        Span('(', cls='p'),
                        Span("'accordion-example-heading-3'", cls='s1'),
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
    H3(
        'HTML Markup',
        Span(id='html-markup', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: HTML Markup', href='#html-markup', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following HTML markup example for the JavaScript script above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-1"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"', cls='s'),
                        Span('aria-expanded', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-body-1"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        'What is Flowbite?',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('data-accordion-icon', cls='na'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-6 h-6 rotate-180 shrink-0"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 20 20"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('><', cls='p'),
                        Span('path', cls='nt'),
                        Span('fill-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"', cls='s'),
                        Span('clip-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('></', cls='p'),
                        Span('path', cls='nt'),
                        Span('></', cls='p'),
                        Span('svg', cls='nt'),
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
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
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
                        Span('"accordion-example-body-1"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-1"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-2 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons, dropdowns, modals, navbars, and more.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'Check out this guide to learn how to',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"/docs/getting-started/introduction/"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-primary-600 dark:text-primary-500 hover:underline"', cls='s'),
                        Span('>', cls='p'),
                        'get started',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        'and start developing websites even faster with components on top of Tailwind CSS.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
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
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-2"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"', cls='s'),
                        Span('aria-expanded', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-body-2"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        'Is there a Figma file available?',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('data-accordion-icon', cls='na'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-6 h-6 shrink-0"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 20 20"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('><', cls='p'),
                        Span('path', cls='nt'),
                        Span('fill-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"', cls='s'),
                        Span('clip-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('></', cls='p'),
                        Span('path', cls='nt'),
                        Span('></', cls='p'),
                        Span('svg', cls='nt'),
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
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
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
                        Span('"accordion-example-body-2"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-2"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"p-5 border border-b-0 border-gray-200 dark:border-gray-700"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-2 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is first conceptualized and designed using the Figma software so everything you see in the library has a design equivalent in our Figma file.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'Check out the',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"https://flowbite.com/figma/"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-primary-600 dark:text-primary-500 hover:underline"', cls='s'),
                        Span('>', cls='p'),
                        'Figma design system',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        'based on the utility classes from Tailwind CSS and components from Flowbite.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
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
                        Span('</', cls='p'),
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-3"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800"', cls='s'),
                        Span('aria-expanded', cls='na'),
                        Span('=', cls='o'),
                        Span('"false"', cls='s'),
                        Span('aria-controls', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-body-3"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        'What are the differences between Flowbite and Tailwind UI?',
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('data-accordion-icon', cls='na'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-6 h-6 shrink-0"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 20 20"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('><', cls='p'),
                        Span('path', cls='nt'),
                        Span('fill-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"', cls='s'),
                        Span('clip-rule', cls='na'),
                        Span('=', cls='o'),
                        Span('"evenodd"', cls='s'),
                        Span('></', cls='p'),
                        Span('path', cls='nt'),
                        Span('></', cls='p'),
                        Span('svg', cls='nt'),
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
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
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
                        Span('"accordion-example-body-3"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden"', cls='s'),
                        Span('aria-labelledby', cls='na'),
                        Span('=', cls='o'),
                        Span('"accordion-example-heading-3"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"p-5 border border-t-0 border-gray-200 dark:border-gray-700"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-2 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'The main difference is that the core components from Flowbite are open source under the MIT license, whereas Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone components, whereas Tailwind UI offers sections of pages.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-2 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no technical reason stopping you from using the best of two worlds.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"mb-2 text-gray-500 dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        'Learn more about these technologies:',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('ul', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"ps-5 text-gray-500 list-disc dark:text-gray-400"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('><', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"https://flowbite.com/pro/"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-primary-600 dark:text-primary-500 hover:underline"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite Pro',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('></', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('li', cls='nt'),
                        Span('><', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"https://tailwindui.com/"', cls='s'),
                        Span('rel', cls='na'),
                        Span('=', cls='o'),
                        Span('"nofollow"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-primary-600 dark:text-primary-500 hover:underline"', cls='s'),
                        Span('>', cls='p'),
                        'Tailwind UI',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('></', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('ul', cls='nt'),
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
                data_lang='html',
                cls='language-html'
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
        'from Flowbite then you can import the types for the Accordion object, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Accordion', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span('"flowbite"', cls='s2'),
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
                        Span('AccordionOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('AccordionItem', cls='nx'),
                        Span(',', cls='p'),
                        Span('AccordionInterface', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span('"flowbite"', cls='s2'),
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
                        Span('accordionEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example'", cls='s1'),
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
                        Span('// create an array of objects with the id, trigger element (eg. button), and the content element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('accordionItems', cls='nx'),
                        Span(':', cls='o'),
                        Span('AccordionItem', cls='nx'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-1'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-1'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-2'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-2'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
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
                        Span('id', cls='nx'),
                        Span(':', cls='o'),
                        Span("'accordion-example-heading-3'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-heading-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#accordion-example-body-3'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('active', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}', cls='p'),
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
                        Span(':', cls='o'),
                        Span('AccordionOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('alwaysOpen', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('activeClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('inactiveClasses', cls='nx'),
                        Span(':', cls='o'),
                        Span("'text-gray-500 dark:text-gray-400'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onOpen', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been shown'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span('onClose', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been hidden'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span('onToggle', cls='nx'),
                        Span(':', cls='o'),
                        Span('(', cls='p'),
                        Span('item', cls='nx'),
                        Span(')', cls='p'),
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
                        Span("'accordion item has been toggled'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span('item', cls='nx'),
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
                        Span("'accordion-example'", cls='s1'),
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
                        Span('/*', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* accordionEl: HTML element (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* accordionItems: array of accordion item objects (required)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions (optional)', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('*/', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('accordion', cls='nx'),
                        Span(':', cls='o'),
                        Span('AccordionInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Accordion', cls='nx'),
                        Span('(', cls='p'),
                        Span('accordionEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('accordionItems', cls='nx'),
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
                        Span('// open accordion item based on id', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('open', cls='nx'),
                        Span('(', cls='p'),
                        Span("'accordion-example-heading-2'", cls='s1'),
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
                        Span('// destroy accordion', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('destroy', cls='nx'),
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
                        Span('// re-initialize accordion', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('accordion', cls='nx'),
                        Span('.', cls='p'),
                        Span('init', cls='nx'),
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
    id='mainContent'
)
