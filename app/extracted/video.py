from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('Get started with the video component to embed internal video source into a native HTML 5 video player and set custom options such as autoplay or muted to enhance the user experience.'),
    H2(
        'Video player',
        Span(id='video-player', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Video player', href='#video-player', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to create a native browser video player and apply the',
        Code('w-full'),
        'utility class from Tailwind CSS to span the full width of the parent container.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Autoplay',
        Span(id='autoplay', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Autoplay', href='#autoplay', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('autoplay'),
        'attribute on the video component to automatically start the video when the page has been loaded.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        autoplay=True,
        controls=True,
        cls='w-full'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        autoplay=True,
        controls=True,
        cls='w-full'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Muted',
        Span(id='muted', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Muted', href='#muted', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('muted'),
        'attribute together with the',
        Code('autoplay'),
        'option to start the video while the sound is muted.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        autoplay=True,
        muted=True,
        controls=True,
        cls='w-full'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        autoplay=True,
        muted=True,
        controls=True,
        cls='w-full'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Set the width and height of the video component using the',
        Code('w-{size}'),
        'and',
        Code('h-{size}'),
        'utility classes from Tailwind CSS.'
    ),
    H3(
        'Width',
        Span(id='width', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Width', href='#width', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('w-{size}'),
        'class to set the width of the video component.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-96'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-96'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H3(
        'Height',
        Span(id='height', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Height', href='#height', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('h-{size}'),
        'class to set the height of the video player.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='h-80'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='h-80'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H3(
        'Responsive',
        Span(id='responsive', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Responsive', href='#responsive', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following example to make the video responsive across all devices and viewports.'),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full h-auto max-w-full'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full h-auto max-w-full'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Custom styles',
        Span(id='custom-styles', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Custom styles', href='#custom-styles', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Customize the video player appearance using the utility classes from Tailwind CSS such as',
        Code('rounded-{size}'),
        'or',
        Code('border'),
        'to set rounded-sm corners and border.'
    ),
    component_showcase(Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full h-auto max-w-full border border-gray-200 rounded-lg dark:border-gray-700'
    )
), code="""Div(
    Video(
        Source(src='/docs/videos/flowbite.mp4', type='video/mp4'),
        'Your browser does not support the video tag.',
        controls=True,
        cls='w-full h-auto max-w-full border border-gray-200 rounded-lg dark:border-gray-700'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    id='mainContent'
)
