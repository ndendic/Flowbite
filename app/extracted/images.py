from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('Get started with a collection of responsive image components coded with the utility classes from Tailwind CSS that you can use inside articles, cards, sections, and other components based on multiple styles, sizes, layouts, and hover animations.'),
    H2(
        'Default image',
        Span(id='default-image', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default image', href='#default-image', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show the a responsive image that won’t grow beyond the maximum original width.'),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-full')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-full')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Image caption',
        Span(id='image-caption', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image caption', href='#image-caption', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add a caption for the image often used inside articles.'),
    component_showcase(Div(
    Figure(
        Img(src='/docs/images/examples/image-3@2x.jpg', alt='image description', cls='h-auto max-w-full rounded-lg'),
        Figcaption('Image caption', cls='mt-2 text-sm text-center text-gray-500 dark:text-gray-400'),
        cls='max-w-lg'
    )
), code="""Div(
    Figure(
        Img(src='/docs/images/examples/image-3@2x.jpg', alt='image description', cls='h-auto max-w-full rounded-lg'),
        Figcaption('Image caption', cls='mt-2 text-sm text-center text-gray-500 dark:text-gray-400'),
        cls='max-w-lg'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Rounded corners',
        Span(id='rounded-corners', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Rounded corners', href='#rounded-corners', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Apply rounded corners to the image by using the specific utility classes from Tailwind CSS.'),
    H3(
        'Border radius',
        Span(id='border-radius', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Border radius', href='#border-radius', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to apply rounded corners to the image by using the',
        Code('rounded-{size}'),
        'class where the size can be anything from small to extra large.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg rounded-lg')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg rounded-lg')
)""", id="example_2",cls='mt-2 mb-6'),
    H3(
        'Full circle',
        Span(id='full-circle', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Full circle', href='#full-circle', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to mask the image inside a circle using the',
        Code('rounded-full'),
        'utility class from Tailwind CSS.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-4@2x.jpg', alt='image description', cls='rounded-full w-96 h-96')
), code="""Div(
    Img(src='/docs/images/examples/image-4@2x.jpg', alt='image description', cls='rounded-full w-96 h-96')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Image shadow',
        Span(id='image-shadow', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image shadow', href='#image-shadow', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to show a shadow effect for the image using the',
        Code('shadow-{size}'),
        'utility class.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-2@2x.jpg', alt='image description', cls='h-auto max-w-xl rounded-lg shadow-xl dark:shadow-gray-800')
), code="""Div(
    Img(src='/docs/images/examples/image-2@2x.jpg', alt='image description', cls='h-auto max-w-xl rounded-lg shadow-xl dark:shadow-gray-800')
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Retina-ready',
        Span(id='retina-ready', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Retina-ready', href='#retina-ready', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('srcset'),
        'attribute to set Retina-ready images with double resolution.'
    ),
    component_showcase(Div(
    Img(srcset='/docs/images/examples/image-1.jpg 1x, /docs/images/examples/image-1@2x.jpg 2x', alt='image description', cls='w-full h-auto max-w-xl rounded-lg')
), code="""Div(
    Img(srcset='/docs/images/examples/image-1.jpg 1x, /docs/images/examples/image-1@2x.jpg 2x', alt='image description', cls='w-full h-auto max-w-xl rounded-lg')
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Image card',
        Span(id='image-card', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image card', href='#image-card', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to make the image a card item with a link and a short text description.'),
    component_showcase(Div(
    Figure(
        A(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='rounded-lg'),
            href='#'
        ),
        Figcaption(
            P('Do you want to get notified when a new component is added to Flowbite?'),
            cls='absolute px-4 text-lg text-white bottom-6'
        ),
        cls='relative max-w-sm transition-all duration-300 cursor-pointer filter grayscale hover:grayscale-0'
    )
), code="""Div(
    Figure(
        A(
            Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='rounded-lg'),
            href='#'
        ),
        Figcaption(
            P('Do you want to get notified when a new component is added to Flowbite?'),
            cls='absolute px-4 text-lg text-white bottom-6'
        ),
        cls='relative max-w-sm transition-all duration-300 cursor-pointer filter grayscale hover:grayscale-0'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Image effects',
        Span(id='image-effects', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image effects', href='#image-effects', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use image effects such as grayscale or blur to change the appearances of the image when being hovered.'),
    H3(
        'Grayscale',
        Span(id='grayscale', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Grayscale', href='#grayscale', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the filter option and apply a grayscale to the image element using the',
        Code('grayscale'),
        'class.'
    ),
    component_showcase(Div(
    Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='h-auto max-w-lg transition-all duration-300 rounded-lg cursor-pointer filter grayscale hover:grayscale-0')
), code="""Div(
    Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='h-auto max-w-lg transition-all duration-300 rounded-lg cursor-pointer filter grayscale hover:grayscale-0')
)""", id="example_7",cls='mt-2 mb-6'),
    H3(
        'Blur',
        Span(id='blur', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Blur', href='#blur', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply a blur by using the',
        Code('blur-{size}'),
        'utility class from Tailwind CSS to an image component.'
    ),
    component_showcase(Div(
    Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='h-auto max-w-lg transition-all duration-300 rounded-lg blur-xs hover:blur-none')
), code="""Div(
    Img(src='https://flowbite.s3.amazonaws.com/blocks/marketing-ui/content/content-gallery-3.png', alt='image description', cls='h-auto max-w-lg transition-all duration-300 rounded-lg blur-xs hover:blur-none')
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Alignment',
        Span(id='alignment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Alignment', href='#alignment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Align the image component to the left, center or right side of the document page using margin styles.'),
    H3(
        'Left',
        Span(id='left', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Left', href='#left', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('By default, the image component will be aligned to the left side of the page.'),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg')
)""", id="example_9",cls='mt-2 mb-6'),
    H3(
        'Center',
        Span(id='center', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Center', href='#center', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Horizontally align the image to the center of the page using the',
        Code('mx-auto'),
        'class.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg mx-auto')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg mx-auto')
)""", id="example_10",cls='mt-2 mb-6'),
    H3(
        'Right',
        Span(id='right', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Right', href='#right', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('ml-auto'),
        '(or',
        Code('ms-auto'),
        ') class to align the image to the right side of the page.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg ms-auto')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-lg ms-auto')
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Set the size of the image using the',
        Code('w-{size}'),
        'and',
        Code('h-{size}'),
        'or',
        Code('max-w-{size}'),
        'utility classes from Tailwind CSS to set the width and height of the element.'
    ),
    H3(
        'Small',
        Span(id='small', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Small', href='#small', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('max-w-xs'),
        'class to set a small size of the image.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-xs')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-xs')
)""", id="example_12",cls='mt-2 mb-6'),
    H3(
        'Medium',
        Span(id='medium', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Medium', href='#medium', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('max-w-md'),
        'class to set a medium size of the image.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-md')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-md')
)""", id="example_13",cls='mt-2 mb-6'),
    H3(
        'Large',
        Span(id='large', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Large', href='#large', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('max-w-xl'),
        'class to set a large size of the image.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-xl')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-xl')
)""", id="example_14",cls='mt-2 mb-6'),
    H3(
        'Full width',
        Span(id='full-width', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Full width', href='#full-width', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('max-w-full'),
        'class to set the full width of the image as long as it doesn’t become larger than the original source.'
    ),
    component_showcase(Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-full')
), code="""Div(
    Img(src='/docs/images/examples/image-1@2x.jpg', alt='image description', cls='h-auto max-w-full')
)""", id="example_15",cls='mt-2 mb-6'),
    id='mainContent'
)
