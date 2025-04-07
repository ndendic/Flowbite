from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

article=Article(
    Header(
        Address(
            Div(
                Img(src='https://flowbite.com/docs/images/people/profile-picture-2.jpg', alt='Jese Leos', cls='mr-4 w-16 h-16 rounded-full'),
                Div(
                    A('Jese Leos', href='#', rel='author', cls='text-xl font-bold text-gray-900 dark:text-white'),
                    P('Graphic Designer, educator & CEO Fastbite', cls='text-base text-gray-500 dark:text-gray-400'),
                    P(
                        Time('Feb. 8, 2022', pubdate='', datetime='2022-02-08', title='February 8th, 2022'),
                        cls='text-base text-gray-500 dark:text-gray-400'
                    )
                ),
                cls='inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white'
            ),
            cls='flex items-center mb-6 not-italic'
        ),
        H1('Best practices for successful prototypes', cls='mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white'),
        cls='mb-4 lg:mb-6 not-format'
    ),
    P('Fastbite is an open-source library of UI components built with the utility-first\r\n              classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals,\r\n              datepickers.', cls='lead'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way,\r\n              you can think things through before committing to an actual design project.'),
    P(
        'But then I found a',
        A('component library based on Tailwind CSS called\r\n                  Fastbite', href='https://flowbite.com'),
        '. It comes with the most commonly used UI components, such as buttons, navigation\r\n              bars, cards, form elements, and more which are conveniently built with the utility classes from\r\n              Tailwind CSS.'
    ),
    Figure(
        Img(src='https://flowbite.s3.amazonaws.com/typography-plugin/typography-image-1.png', alt=''),
        Figcaption('Digital art by Anonymous')
    ),
    H2('Getting started with Fastbite'),
    P('First of all you need to understand how Fastbite works. This library is not another framework.\r\n              Rather, it is a set of components based on Tailwind CSS that you can just copy-paste from the\r\n              documentation.'),
    P('It also includes a JavaScript file that enables interactive components, such as modals, dropdowns,\r\n              and datepickers which you can optionally include into your project via CDN or NPM.'),
    P(
        'You can check out the',
        A('quickstart\r\n                  guide', href='https://flowbite.com/docs/getting-started/quickstart/'),
        'to explore the elements by including the CDN files into your project. But if you want\r\n              to build a project with Fastbite I recommend you to follow the build tools steps so that you can\r\n              purge and minify the generated CSS.'
    ),
    P(
        "You'll also receive a lot of useful application UI, marketing UI, and e-commerce pages that can help\r\n              you get started with your projects even faster. You can check out this",
        A('comparison table', href='https://flowbite.com/docs/components/tables/'),
        'to better understand\r\n              the differences between the open-source and pro version of Fastbite.'
    ),
    H2('When does design come in handy?'),
    P('While it might seem like extra work at a first glance, here are some key moments in which prototyping\r\n              will come in handy:'),
    Ol(
        Li(
            Strong('Usability testing'),
            '. Does your user know how to exit out of screens? Can they\r\n                  follow your intended user journey and buy something from the site you’ve designed? By running a\r\n                  usability test, you’ll be able to see how users will interact with your design once it’s live;'
        ),
        Li(
            Strong('Involving stakeholders'),
            '. Need to check if your GDPR consent boxes are displaying\r\n                  properly? Pass your prototype to your data protection team and they can test it for real;'
        ),
        Li(
            Strong('Impressing a client'),
            '. Prototypes can help explain or even sell your idea by\r\n                  providing your client with a hands-on experience;'
        ),
        Li(
            Strong('Communicating your vision'),
            '. By using an interactive medium to preview and test\r\n                  design elements, designers and developers can understand each other — and the project — better.'
        )
    ),
    H3('Laying the groundwork for best design'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way,\r\n              you can think things through before committing to an actual design project.'),
    P(
        "Let's start by including the CSS file inside the",
        Code('head'),
        'tag of your HTML.'
    ),
    H3('Understanding typography'),
    H4('Type properties'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H4('Baseline'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H4('Measurement from the baseline'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H3('Type classification'),
    H4('Serif'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.\r\n              Typefaces with serifs are called serif typefaces. Serif fonts are classified as one of the\r\n              following:'),
    H4('Old-Style serifs'),
    Ul(
        Li('Low contrast between thick and thin strokes'),
        Li('Diagonal stress in the strokes'),
        Li('Slanted serifs on lower-case ascenders')
    ),
    Img(src='https://flowbite.s3.amazonaws.com/typography-plugin/typography-image-2.png', alt=''),
    Ol(
        Li('Low contrast between thick and thin strokes'),
        Li('Diagonal stress in the strokes'),
        Li('Slanted serifs on lower-case ascenders')
    ),
    H3('Laying the best for successful prototyping'),
    P('A serif is a small shape or projection that appears at the beginning:'),
    Blockquote(
        P('Fastbite is just awesome. It contains tons of predesigned components and pages starting from\r\n                  login screen to complex dashboard. Perfect choice for your next SaaS application.')
    ),
    H4('Code example'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.\r\n              Typefaces with serifs are called serif typefaces. Serif fonts are classified as one of the\r\n              following:'),
    Pre(
        Code('<dl class="grid grid-cols-2 gap-8 max-w-screen-md text-gray-900 sm:grid-cols-3 dark:text-white">\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">73M+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">developers</dd>\r\n</div>\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">1B+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">contributors</dd>\r\n</div>\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">4M+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">organizations</dd>\r\n</div>\r\n</dl>', cls='language-html')
    ),
    H4('Table example'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.'),
    Table(
        Thead(
            Tr(
                Th('Country'),
                Th('Date & Time'),
                Th('Amount')
            )
        ),
        Tbody(
            Tr(
                Td('United States'),
                Td('April 21, 2021'),
                Td(
                    Strong('$2,300')
                )
            ),
            Tr(
                Td('Canada'),
                Td('May 31, 2021'),
                Td(
                    Strong('$300')
                )
            ),
            Tr(
                Td('United Kingdom'),
                Td('June 3, 2021'),
                Td(
                    Strong('$2,500')
                )
            ),
            Tr(
                Td('Australia'),
                Td('June 23, 2021'),
                Td(
                    Strong('$3,543')
                )
            ),
            Tr(
                Td('Germany'),
                Td('July 6, 2021'),
                Td(
                    Strong('$99')
                )
            ),
            Tr(
                Td('France'),
                Td('August 23, 2021'),
                Td(
                    Strong('$2,540')
                )
            )
        )
    ),
    H3('Best practices for setting up your prototype'),
    P(
        Strong('Low fidelity or high fidelity?'),
        'Fidelity refers to how close a prototype will be to\r\n              the real deal. If you’re simply preparing a quick visual aid for a presentation, a low-fidelity\r\n              prototype — like a wireframe with placeholder images and some basic text — would be more than\r\n              enough. But if you’re going for more intricate usability testing, a high-fidelity prototype — with\r\n              on-brand colors, fonts and imagery — could help get more pointed results.'
    ),
    P(
        Strong('Consider your user'),
        '. To create an intuitive user flow, try to think as your user\r\n              would when interacting with your product. While you can fine-tune this during beta testing,\r\n              considering your user’s needs and habits early on will save you time by setting you on the right\r\n              path.'
    ),
    P(
        Strong('Start from the inside out'),
        '. A nice way to both organize your tasks and create more\r\n              user-friendly prototypes is by building your prototypes ‘inside out’. Start by focusing on what will\r\n              be important to your user, like a Buy now button or an image gallery, and list each element by order\r\n              of priority. This way, you’ll be able to create a prototype that puts your users’ needs at the heart\r\n              of your design.'
    ),
    P('And there you have it! Everything you need to design and share prototypes — right in Fastbite Figma.'),
    cls='mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert'
)

component = Div(
    P('Following is an example of an article component, that can be used to display blog posts or other content.'),
    H2(
        'Default article',
        Span(id='default-article', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default article', href='#default-article', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples of alert components to show messages as feedback to your users.'),
    component_showcase(article, code="""Article(
    Header(
        Address(
            Div(
                Img(src='https://flowbite.com/docs/images/people/profile-picture-2.jpg', alt='Jese Leos', cls='mr-4 w-16 h-16 rounded-full'),
                Div(
                    A('Jese Leos', href='#', rel='author', cls='text-xl font-bold text-gray-900 dark:text-white'),
                    P('Graphic Designer, educator & CEO Fastbite', cls='text-base text-gray-500 dark:text-gray-400'),
                    P(
                        Time('Feb. 8, 2022', pubdate='', datetime='2022-02-08', title='February 8th, 2022'),
                        cls='text-base text-gray-500 dark:text-gray-400'
                    )
                ),
                cls='inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white'
            ),
            cls='flex items-center mb-6 not-italic'
        ),
        H1('Best practices for successful prototypes', cls='mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white'),
        cls='mb-4 lg:mb-6 not-format'
    ),
    P('Fastbite is an open-source library of UI components built with the utility-first\r\n              classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals,\r\n              datepickers.', cls='lead'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way,\r\n              you can think things through before committing to an actual design project.'),
    P(
        'But then I found a',
        A('component library based on Tailwind CSS called\r\n                  Fastbite', href='https://flowbite.com'),
        '. It comes with the most commonly used UI components, such as buttons, navigation\r\n              bars, cards, form elements, and more which are conveniently built with the utility classes from\r\n              Tailwind CSS.'
    ),
    Figure(
        Img(src='https://flowbite.s3.amazonaws.com/typography-plugin/typography-image-1.png', alt=''),
        Figcaption('Digital art by Anonymous')
    ),
    H2('Getting started with Fastbite'),
    P('First of all you need to understand how Fastbite works. This library is not another framework.\r\n              Rather, it is a set of components based on Tailwind CSS that you can just copy-paste from the\r\n              documentation.'),
    P('It also includes a JavaScript file that enables interactive components, such as modals, dropdowns,\r\n              and datepickers which you can optionally include into your project via CDN or NPM.'),
    P(
        'You can check out the',
        A('quickstart\r\n                  guide', href='https://flowbite.com/docs/getting-started/quickstart/'),
        'to explore the elements by including the CDN files into your project. But if you want\r\n              to build a project with Fastbite I recommend you to follow the build tools steps so that you can\r\n              purge and minify the generated CSS.'
    ),
    P(
        "You'll also receive a lot of useful application UI, marketing UI, and e-commerce pages that can help\r\n              you get started with your projects even faster. You can check out this",
        A('comparison table', href='https://flowbite.com/docs/components/tables/'),
        'to better understand\r\n              the differences between the open-source and pro version of Fastbite.'
    ),
    H2('When does design come in handy?'),
    P('While it might seem like extra work at a first glance, here are some key moments in which prototyping\r\n              will come in handy:'),
    Ol(
        Li(
            Strong('Usability testing'),
            '. Does your user know how to exit out of screens? Can they\r\n                  follow your intended user journey and buy something from the site you’ve designed? By running a\r\n                  usability test, you’ll be able to see how users will interact with your design once it’s live;'
        ),
        Li(
            Strong('Involving stakeholders'),
            '. Need to check if your GDPR consent boxes are displaying\r\n                  properly? Pass your prototype to your data protection team and they can test it for real;'
        ),
        Li(
            Strong('Impressing a client'),
            '. Prototypes can help explain or even sell your idea by\r\n                  providing your client with a hands-on experience;'
        ),
        Li(
            Strong('Communicating your vision'),
            '. By using an interactive medium to preview and test\r\n                  design elements, designers and developers can understand each other — and the project — better.'
        )
    ),
    H3('Laying the groundwork for best design'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way,\r\n              you can think things through before committing to an actual design project.'),
    P(
        "Let's start by including the CSS file inside the",
        Code('head'),
        'tag of your HTML.'
    ),
    H3('Understanding typography'),
    H4('Type properties'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H4('Baseline'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H4('Measurement from the baseline'),
    P('A typeface is a collection of letters. While each letter is unique, certain shapes are shared across\r\n              letters. A typeface represents shared patterns across a collection of letters.'),
    H3('Type classification'),
    H4('Serif'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.\r\n              Typefaces with serifs are called serif typefaces. Serif fonts are classified as one of the\r\n              following:'),
    H4('Old-Style serifs'),
    Ul(
        Li('Low contrast between thick and thin strokes'),
        Li('Diagonal stress in the strokes'),
        Li('Slanted serifs on lower-case ascenders')
    ),
    Img(src='https://flowbite.s3.amazonaws.com/typography-plugin/typography-image-2.png', alt=''),
    Ol(
        Li('Low contrast between thick and thin strokes'),
        Li('Diagonal stress in the strokes'),
        Li('Slanted serifs on lower-case ascenders')
    ),
    H3('Laying the best for successful prototyping'),
    P('A serif is a small shape or projection that appears at the beginning:'),
    Blockquote(
        P('Fastbite is just awesome. It contains tons of predesigned components and pages starting from\r\n                  login screen to complex dashboard. Perfect choice for your next SaaS application.')
    ),
    H4('Code example'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.\r\n              Typefaces with serifs are called serif typefaces. Serif fonts are classified as one of the\r\n              following:'),
    Pre(
        Code('<dl class="grid grid-cols-2 gap-8 max-w-screen-md text-gray-900 sm:grid-cols-3 dark:text-white">\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">73M+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">developers</dd>\r\n</div>\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">1B+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">contributors</dd>\r\n</div>\r\n<div class="flex flex-col justify-center items-center">\r\n  <dt class="mb-2 text-3xl font-extrabold">4M+</dt>\r\n  <dd class="text-lg font-normal text-gray-500 dark:text-gray-400">organizations</dd>\r\n</div>\r\n</dl>', cls='language-html')
    ),
    H4('Table example'),
    P('A serif is a small shape or projection that appears at the beginning or end of a stroke on a letter.'),
    Table(
        Thead(
            Tr(
                Th('Country'),
                Th('Date & Time'),
                Th('Amount')
            )
        ),
        Tbody(
            Tr(
                Td('United States'),
                Td('April 21, 2021'),
                Td(
                    Strong('$2,300')
                )
            ),
            Tr(
                Td('Canada'),
                Td('May 31, 2021'),
                Td(
                    Strong('$300')
                )
            ),
            Tr(
                Td('United Kingdom'),
                Td('June 3, 2021'),
                Td(
                    Strong('$2,500')
                )
            ),
            Tr(
                Td('Australia'),
                Td('June 23, 2021'),
                Td(
                    Strong('$3,543')
                )
            ),
            Tr(
                Td('Germany'),
                Td('July 6, 2021'),
                Td(
                    Strong('$99')
                )
            ),
            Tr(
                Td('France'),
                Td('August 23, 2021'),
                Td(
                    Strong('$2,540')
                )
            )
        )
    ),
    H3('Best practices for setting up your prototype'),
    P(
        Strong('Low fidelity or high fidelity?'),
        'Fidelity refers to how close a prototype will be to\r\n              the real deal. If you’re simply preparing a quick visual aid for a presentation, a low-fidelity\r\n              prototype — like a wireframe with placeholder images and some basic text — would be more than\r\n              enough. But if you’re going for more intricate usability testing, a high-fidelity prototype — with\r\n              on-brand colors, fonts and imagery — could help get more pointed results.'
    ),
    P(
        Strong('Consider your user'),
        '. To create an intuitive user flow, try to think as your user\r\n              would when interacting with your product. While you can fine-tune this during beta testing,\r\n              considering your user’s needs and habits early on will save you time by setting you on the right\r\n              path.'
    ),
    P(
        Strong('Start from the inside out'),
        '. A nice way to both organize your tasks and create more\r\n              user-friendly prototypes is by building your prototypes ‘inside out’. Start by focusing on what will\r\n              be important to your user, like a Buy now button or an image gallery, and list each element by order\r\n              of priority. This way, you’ll be able to create a prototype that puts your users’ needs at the heart\r\n              of your design.'
    ),
    P('And there you have it! Everything you need to design and share prototypes — right in Fastbite Figma.'),
    cls='mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert'
)""", id="example_0",cls='mt-2 mb-6'),
    
)