from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('Get started with a collection of list components built with Tailwind CSS for ordered and unordered lists with bullets, numbers, or icons and other styles and layouts to show a list of items inside an article or throughout your web page.'),
    H2(
        'Unordered list',
        Span(id='unordered-list', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Unordered list', href='#unordered-list', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to create a default unordered list of items using the',
        Code('list-disc'),
        'class.'
    ),
    component_showcase(Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li('At least 10 characters (and up to 100 characters)'),
        Li('At least one lowercase character'),
        Li('Inclusion of at least one special character, e.g., ! @ # ?'),
        cls='max-w-md space-y-1 text-gray-500 list-disc list-inside dark:text-gray-400'
    )
), code="""Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li('At least 10 characters (and up to 100 characters)'),
        Li('At least one lowercase character'),
        Li('Inclusion of at least one special character, e.g., ! @ # ?'),
        cls='max-w-md space-y-1 text-gray-500 list-disc list-inside dark:text-gray-400'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H3(
        'Icons',
        Span(id='icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Icons', href='#icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to apply custom icons instead of the default bullets for the list items.'),
    component_showcase(Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-green-500 dark:text-green-400 shrink-0'
            ),
            'At least 10 characters',
            cls='flex items-center'
        ),
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-green-500 dark:text-green-400 shrink-0'
            ),
            'At least one lowercase character',
            cls='flex items-center'
        ),
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-gray-500 dark:text-gray-400 shrink-0'
            ),
            'At least one special character, e.g., ! @ # ?',
            cls='flex items-center'
        ),
        cls='max-w-md space-y-1 text-gray-500 list-inside dark:text-gray-400'
    )
), code="""Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-green-500 dark:text-green-400 shrink-0'
            ),
            'At least 10 characters',
            cls='flex items-center'
        ),
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-green-500 dark:text-green-400 shrink-0'
            ),
            'At least one lowercase character',
            cls='flex items-center'
        ),
        Li(
            Svg(
                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 20 20',
                cls='w-3.5 h-3.5 me-2 text-gray-500 dark:text-gray-400 shrink-0'
            ),
            'At least one special character, e.g., ! @ # ?',
            cls='flex items-center'
        ),
        cls='max-w-md space-y-1 text-gray-500 list-inside dark:text-gray-400'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H3(
        'Nested',
        Span(id='nested', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Nested', href='#nested', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to nested another list of items inside the parent list element.'),
    component_showcase(Div(
    Ul(
        Li(
            'List item one',
            Ol(
                Li('You might feel like you are being really "organized" o'),
                Li('Nested navigation in UIs is a bad idea too, keep things as flat as possible.'),
                Li('Nesting tons of folders in your source code is also not helpful.'),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        Li(
            'List item two',
            Ul(
                Li("I'm not sure if we'll bother styling more than two levels deep."),
                Li('Two is already too much, three is guaranteed to be a bad idea.'),
                Li('If you nest four levels deep you belong in prison.'),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        Li(
            'List item three',
            Ul(
                Li("Again please don't nest lists if you want"),
                Li('Nobody wants to look at this.'),
                Li("I'm upset that we even have to bother styling this."),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        cls='space-y-4 text-gray-500 list-disc list-inside dark:text-gray-400'
    )
), code="""Div(
    Ul(
        Li(
            'List item one',
            Ol(
                Li('You might feel like you are being really "organized" o'),
                Li('Nested navigation in UIs is a bad idea too, keep things as flat as possible.'),
                Li('Nesting tons of folders in your source code is also not helpful.'),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        Li(
            'List item two',
            Ul(
                Li("I'm not sure if we'll bother styling more than two levels deep."),
                Li('Two is already too much, three is guaranteed to be a bad idea.'),
                Li('If you nest four levels deep you belong in prison.'),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        Li(
            'List item three',
            Ul(
                Li("Again please don't nest lists if you want"),
                Li('Nobody wants to look at this.'),
                Li("I'm upset that we even have to bother styling this."),
                cls='ps-5 mt-2 space-y-1 list-decimal list-inside'
            )
        ),
        cls='space-y-4 text-gray-500 list-disc list-inside dark:text-gray-400'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H3(
        'Unstyled',
        Span(id='unstyled', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Unstyled', href='#unstyled', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('list-none'),
        'class to disable the list style bullets or numbers.'
    ),
    component_showcase(Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li('At least 10 characters (and up to 100 characters)'),
        Li('At least one lowercase character'),
        Li('Inclusion of at least one special character, e.g., ! @ # ?'),
        cls='max-w-md space-y-1 text-gray-500 list-none list-inside dark:text-gray-400'
    )
), code="""Div(
    H2('Password requirements:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ul(
        Li('At least 10 characters (and up to 100 characters)'),
        Li('At least one lowercase character'),
        Li('Inclusion of at least one special character, e.g., ! @ # ?'),
        cls='max-w-md space-y-1 text-gray-500 list-none list-inside dark:text-gray-400'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Ordered list',
        Span(id='ordered-list', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Ordered list', href='#ordered-list', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('<ol>'),
        'tag to create an ordered list of items with numbers.'
    ),
    component_showcase(Div(
    H2('Top students:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ol(
        Li(
            Span('Bonnie Green', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('70', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        Li(
            Span('Jese Leos', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('63', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        Li(
            Span('Leslie Livingston', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('57', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        cls='max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400'
    )
), code="""Div(
    H2('Top students:', cls='mb-2 text-lg font-semibold text-gray-900 dark:text-white'),
    Ol(
        Li(
            Span('Bonnie Green', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('70', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        Li(
            Span('Jese Leos', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('63', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        Li(
            Span('Leslie Livingston', cls='font-semibold text-gray-900 dark:text-white'),
            'with',
            Span('57', cls='font-semibold text-gray-900 dark:text-white'),
            'points'
        ),
        cls='max-w-md space-y-1 text-gray-500 list-decimal list-inside dark:text-gray-400'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H3(
        'Nested',
        Span(id='nested-1', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Nested', href='#nested-1', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to nest multiple lists into each other.'),
    component_showcase(Div(
    Ol(
        Li(
            'List item one',
            Ul(
                Li('You might feel like you are being really "organized" o'),
                Li('Nested navigation in UIs is a bad idea too, keep things as flat as possible.'),
                Li('Nesting tons of folders in your source code is also not helpful.'),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        Li(
            'List item two',
            Ul(
                Li("I'm not sure if we'll bother styling more than two levels deep."),
                Li('Two is already too much, three is guaranteed to be a bad idea.'),
                Li('If you nest four levels deep you belong in prison.'),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        Li(
            'List item three',
            Ul(
                Li("Again please don't nest lists if you want"),
                Li('Nobody wants to look at this.'),
                Li("I'm upset that we even have to bother styling this."),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        cls='space-y-4 text-gray-500 list-decimal list-inside dark:text-gray-400'
    )
), code="""Div(
    Ol(
        Li(
            'List item one',
            Ul(
                Li('You might feel like you are being really "organized" o'),
                Li('Nested navigation in UIs is a bad idea too, keep things as flat as possible.'),
                Li('Nesting tons of folders in your source code is also not helpful.'),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        Li(
            'List item two',
            Ul(
                Li("I'm not sure if we'll bother styling more than two levels deep."),
                Li('Two is already too much, three is guaranteed to be a bad idea.'),
                Li('If you nest four levels deep you belong in prison.'),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        Li(
            'List item three',
            Ul(
                Li("Again please don't nest lists if you want"),
                Li('Nobody wants to look at this.'),
                Li("I'm upset that we even have to bother styling this."),
                cls='ps-5 mt-2 space-y-1 list-disc list-inside'
            )
        ),
        cls='space-y-4 text-gray-500 list-decimal list-inside dark:text-gray-400'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Description list',
        Span(id='description-list', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Description list', href='#description-list', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Create a description list by using the',
        Code('<dl>'),
        'tag and set the term and name with the following example.'
    ),
    component_showcase(Div(
    Dl(
        Div(
            Dt('Email address', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('yourname@flowbite.com', cls='text-lg font-semibold'),
            cls='flex flex-col pb-3'
        ),
        Div(
            Dt('Home address', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('92 Miles Drive, Newark, NJ 07103, California, USA', cls='text-lg font-semibold'),
            cls='flex flex-col py-3'
        ),
        Div(
            Dt('Phone number', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('+00 123 456 789 / +12 345 678', cls='text-lg font-semibold'),
            cls='flex flex-col pt-3'
        ),
        cls='max-w-md text-gray-900 divide-y divide-gray-200 dark:text-white dark:divide-gray-700'
    )
), code="""Div(
    Dl(
        Div(
            Dt('Email address', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('yourname@flowbite.com', cls='text-lg font-semibold'),
            cls='flex flex-col pb-3'
        ),
        Div(
            Dt('Home address', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('92 Miles Drive, Newark, NJ 07103, California, USA', cls='text-lg font-semibold'),
            cls='flex flex-col py-3'
        ),
        Div(
            Dt('Phone number', cls='mb-1 text-gray-500 md:text-lg dark:text-gray-400'),
            Dd('+00 123 456 789 / +12 345 678', cls='text-lg font-semibold'),
            cls='flex flex-col pt-3'
        ),
        cls='max-w-md text-gray-900 divide-y divide-gray-200 dark:text-white dark:divide-gray-700'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'List with icons',
        Span(id='list-with-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: List with icons', href='#list-with-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to create a list of items with',
        A('custom SVG icons', href='https://flowbite.com/icons/'),
        'instead of the default bullets.'
    ),
    component_showcase(Div(
    Ul(
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span('Individual configuration'),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span('No setup, or hidden fees'),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Team size:',
                Span('1 developer', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Premium support:',
                Span('6 months', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Free updates:',
                Span('6 months', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        cls='space-y-4 text-left text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    Ul(
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span('Individual configuration'),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span('No setup, or hidden fees'),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Team size:',
                Span('1 developer', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Premium support:',
                Span('6 months', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        Li(
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 16 12',
                cls='shrink-0 w-3.5 h-3.5 text-green-500 dark:text-green-400'
            ),
            Span(
                'Free updates:',
                Span('6 months', cls='font-semibold text-gray-900 dark:text-white')
            ),
            cls='flex items-center space-x-3 rtl:space-x-reverse'
        ),
        cls='space-y-4 text-left text-gray-500 dark:text-gray-400'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Advanced layout',
        Span(id='advanced-layout', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Advanced layout', href='#advanced-layout', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show more details for each list item such as the user’s name, email and profile picture.'),
    component_showcase(Div(
    Ul(
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Neil Sims', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$320', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='pb-3 sm:pb-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Bonnie Green', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$3467', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Michael Gough', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$67', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Thomas Lean', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$2367', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Lana Byrd', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$367', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='pt-3 pb-0 sm:pt-4'
        ),
        cls='max-w-md divide-y divide-gray-200 dark:divide-gray-700'
    )
), code="""Div(
    Ul(
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-1.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Neil Sims', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$320', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='pb-3 sm:pb-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-3.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Bonnie Green', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$3467', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-2.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Michael Gough', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$67', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-5.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Thomas Lean', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$2367', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='py-3 sm:py-4'
        ),
        Li(
            Div(
                Div(
                    Img(src='/docs/images/people/profile-picture-4.jpg', alt='Neil image', cls='w-8 h-8 rounded-full'),
                    cls='shrink-0'
                ),
                Div(
                    P('Lana Byrd', cls='text-sm font-medium text-gray-900 truncate dark:text-white'),
                    P('email@flowbite.com', cls='text-sm text-gray-500 truncate dark:text-gray-400'),
                    cls='flex-1 min-w-0'
                ),
                Div('$367', cls='inline-flex items-center text-base font-semibold text-gray-900 dark:text-white'),
                cls='flex items-center space-x-4 rtl:space-x-reverse'
            ),
            cls='pt-3 pb-0 sm:pt-4'
        ),
        cls='max-w-md divide-y divide-gray-200 dark:divide-gray-700'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Horizontal list',
        Span(id='horizontal-list', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Horizontal list', href='#horizontal-list', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to create a horizontally aligned list of items.'),
    component_showcase(Div(
    Ul(
        Li(
            A('About', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Premium', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Campaigns', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Blog', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Affiliate Program', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('FAQs', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Contact', href='#', cls='me-4 hover:underline md:me-6')
        ),
        cls='flex flex-wrap items-center justify-center text-gray-900 dark:text-white'
    )
), code="""Div(
    Ul(
        Li(
            A('About', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Premium', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Campaigns', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Blog', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Affiliate Program', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('FAQs', href='#', cls='me-4 hover:underline md:me-6')
        ),
        Li(
            A('Contact', href='#', cls='me-4 hover:underline md:me-6')
        ),
        cls='flex flex-wrap items-center justify-center text-gray-900 dark:text-white'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    id='mainContent'
)
