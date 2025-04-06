from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P(
        'Get started with the',
        A('Flowbite Typography', href='https://github.com/themesberg/flowbite-typography'),
        'plugin forked from the official',
        A('Tailwind CSS Typography', href='https://tailwindcss.com/docs/typography-plugin'),
        'plugin to set a custom',
        Code('format'),
        'class to a wrapper element to apply styles to all inline child elements such as headings, paragraphs, images, lists, and more and apply font sizes, font weights, colors, and spacings.'
    ),
    P(
        'You can check out this',
        A('live demo', href='https://flowbite.com/plugins/typography/'),
        'to see how content inside an article will render like.'
    ),
    H2(
        'Getting started',
        Span(id='getting-started', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Getting started', href='#getting-started', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Make sure that you have both',
        A('Node.js', href='https://nodejs.org/'),
        'and',
        A('Tailwind CSS', href='https://tailwindcss.com/'),
        'already installed in your project.'
    ),
    Ol(
        Li('Install the Flowbite Typography plugin via NPM:')
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span('npm i -D flowbite-typography', cls='cl'),
                    cls='line'
                ),
                data_lang='bash',
                cls='language-bash'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    Ol(
        Li(
            'Import the',
            Code('flowbite-typography'),
            'plugin inside your main Tailwind CSS file:'
        ),
        start='2'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('@', cls='err'),
                        Span('plugin', cls='nx'),
                        Span('"flowbite-typography"', cls='s2'),
                        Span(';', cls='p'),
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
    P(
        'Alternatively you can do the same but in your',
        Code('tailwind.config.js'),
        'file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// import the tailwind.config.js file in your main CSS file if using Tailwind CSS v4', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('module', cls='nx'),
                        Span('.', cls='p'),
                        Span('exports', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('theme', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// ...', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('plugins', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('require', cls='nx'),
                        Span('(', cls='p'),
                        Span("'flowbite-typography'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// ...', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('],', cls='p'),
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
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P('Now you can go ahead and use the new formatting classes from the Flowbite Typography plugin.'),
    H2(
        'Basic usage',
        Span(id='basic-usage', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Basic usage', href='#basic-usage', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Once you have installed the plugin inside your project you can add the',
        Code('format'),
        'class to a wrapper element and use any type of inline elements such as headings, paragraphs, images, lists, captions, links, and tables.'
    ),
    P('All of these elements will be automatically styled with proper spacing, font sizing, font weight, colors, and more based on recommended UI/UX readability and accessibility standards.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('article', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"format lg:format-lg"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h1', cls='nt'),
                        Span('>', cls='p'),
                        'Prototyping from A to Z: best practices for successful prototypes',
                        Span('</', cls='p'),
                        Span('h1', cls='nt'),
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
                        Span('"lead"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.',
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
                        Span('>', cls='p'),
                        'Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.',
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
                        Span('>', cls='p'),
                        'But then I found a',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('>', cls='p'),
                        'component library based on Tailwind CSS called Flowbite',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('...', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
                        'When does design come in handy?',
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
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        'While it might seem like extra work at a first glance, here are some key moments in which prototyping will come in handy:',
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
                        Span('ol', cls='nt'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Usability testing',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site youâ\x80\x99ve designed? By running a usability test, youâ\x80\x99ll be able to see how users will interact with your design once itâ\x80\x99s live;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Involving stakeholders',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Need to check if your GDPR consent boxes are displaying properly? Pass your prototype to your data protection team and they can test it for real;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Impressing a client',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Prototypes can help explain or even sell your idea by providing your client with a hands-on experience;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Communicating your vision',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. By using an interactive medium to preview and test design elements, designers and developers can understand each other â\x80\x94 and the project â\x80\x94 better.',
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('ol', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('article', cls='nt'),
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
    P(
        'You can also set the',
        Code('lg:format-lg'),
        'class to set increase font sizes and spacings for larger viewport devices.'
    ),
    H2(
        'Link colors',
        Span(id='link-colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Link colors', href='#link-colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can update the default primary link color to anything you’d like by setting the',
        Code('format-{color}'),
        'class:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('article', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"format lg:format-lg format-red"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h1', cls='nt'),
                        Span('>', cls='p'),
                        'Prototyping from A to Z: best practices for successful prototypes',
                        Span('</', cls='p'),
                        Span('h1', cls='nt'),
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
                        Span('"lead"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.',
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
                        Span('>', cls='p'),
                        'Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.',
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
                        Span('>', cls='p'),
                        'But then I found a',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('>', cls='p'),
                        'component library based on Tailwind CSS called Flowbite',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.',
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
                        Span('article', cls='nt'),
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
    H2(
        'Dark mode',
        Span(id='dark-mode', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dark mode', href='#dark-mode', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Enable dark mode for the typography by using the',
        Code('dark:format-invert'),
        'class on the article wrapper element:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('article', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"format lg:format-lg dark:format-invert"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h1', cls='nt'),
                        Span('>', cls='p'),
                        'The content inside this article will invert when switching to dark mode',
                        Span('</', cls='p'),
                        Span('h1', cls='nt'),
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
                        Span('"lead"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.',
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
                        Span('>', cls='p'),
                        'Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.',
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
                        Span('>', cls='p'),
                        'But then I found a',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('>', cls='p'),
                        'component library based on Tailwind CSS called Flowbite',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('...', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
                        'When does design come in handy?',
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
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        'While it might seem like extra work at a first glance, here are some key moments in which prototyping will come in handy:',
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
                        Span('ol', cls='nt'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Usability testing',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site youâ\x80\x99ve designed? By running a usability test, youâ\x80\x99ll be able to see how users will interact with your design once itâ\x80\x99s live;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Involving stakeholders',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Need to check if your GDPR consent boxes are displaying properly? Pass your prototype to your data protection team and they can test it for real;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Impressing a client',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Prototypes can help explain or even sell your idea by providing your client with a hands-on experience;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Communicating your vision',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. By using an interactive medium to preview and test design elements, designers and developers can understand each other â\x80\x94 and the project â\x80\x94 better.',
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('ol', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('article', cls='nt'),
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
    H2(
        'Max width',
        Span(id='max-width', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Max width', href='#max-width', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Override the default maximum width by setting a custom',
        Code('max-w-{size}'),
        'class next to the',
        Code('format'),
        'class:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('article', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"max-w-none format lg:format-lg format-red"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h1', cls='nt'),
                        Span('>', cls='p'),
                        'Prototyping from A to Z: best practices for successful prototypes',
                        Span('</', cls='p'),
                        Span('h1', cls='nt'),
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
                        Span('"lead"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.',
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
                        Span('>', cls='p'),
                        'Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.',
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
                        Span('>', cls='p'),
                        'But then I found a',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('>', cls='p'),
                        'component library based on Tailwind CSS called Flowbite',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.',
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
                        Span('article', cls='nt'),
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
    H2(
        'Disable format',
        Span(id='disable-format', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Disable format', href='#disable-format', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'If you want to disable formatting inside the typography content you can use the',
        Code('not-format'),
        'class:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('article', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"format lg:format-lg dark:format-invert"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h1', cls='nt'),
                        Span('>', cls='p'),
                        'The content inside this article will invert when switching to dark mode',
                        Span('</', cls='p'),
                        Span('h1', cls='nt'),
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
                        Span('"lead"', cls='s'),
                        Span('>', cls='p'),
                        'Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.',
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
                        Span('>', cls='p'),
                        'Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.',
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
                        Span('>', cls='p'),
                        'But then I found a',
                        Span('<', cls='p'),
                        Span('a', cls='nt'),
                        Span('href', cls='na'),
                        Span('=', cls='o'),
                        Span('"#"', cls='s'),
                        Span('>', cls='p'),
                        'component library based on Tailwind CSS called Flowbite',
                        Span('</', cls='p'),
                        Span('a', cls='nt'),
                        Span('>', cls='p'),
                        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.',
                        Span('</', cls='p'),
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('...', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("<!-- content that won't have styles applied -->", cls='c'),
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
                        Span('"not-format"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h2', cls='nt'),
                        Span('>', cls='p'),
                        'When does design come in handy?',
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
                        Span('p', cls='nt'),
                        Span('>', cls='p'),
                        'While it might seem like extra work at a first glance, here are some key moments in which prototyping will come in handy:',
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
                        Span('ol', cls='nt'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Usability testing',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site youâ\x80\x99ve designed? By running a usability test, youâ\x80\x99ll be able to see how users will interact with your design once itâ\x80\x99s live;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Involving stakeholders',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Need to check if your GDPR consent boxes are displaying properly? Pass your prototype to your data protection team and they can test it for real;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Impressing a client',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. Prototypes can help explain or even sell your idea by providing your client with a hands-on experience;',
                        Span('</', cls='p'),
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
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        'Communicating your vision',
                        Span('</', cls='p'),
                        Span('strong', cls='nt'),
                        Span('>', cls='p'),
                        '. By using an interactive medium to preview and test design elements, designers and developers can understand each other â\x80\x94 and the project â\x80\x94 better.',
                        Span('</', cls='p'),
                        Span('li', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('ol', cls='nt'),
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
                        Span('article', cls='nt'),
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
    H2(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Extend the plugin’s options inside the Tailwind configuration file to set your own colors, class name, and more.'),
    H3(
        'Custom colors',
        Span(id='custom-colors', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Custom colors', href='#custom-colors', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can set your own colors by extending the typography plugin inside the',
        Code('tailwind.config.js'),
        'file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('module', cls='nx'),
                        Span('.', cls='p'),
                        Span('exports', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('theme', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('extend', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('typography', cls='nx'),
                        Span(':', cls='o'),
                        Span('({', cls='p'),
                        Span('theme', cls='nx'),
                        Span('})', cls='p'),
                        Span('=>', cls='p'),
                        Span('({', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('orange', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('css', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-body'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[500]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-headings'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[900]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-lead'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[500]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-links'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[600]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-bold'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[900]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-counters'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[500]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-bullets'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[500]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-hr'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[200]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-quotes'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[900]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-quote-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[300]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-captions'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[700]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-code'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[900]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-code-bg'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[50]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-pre-code'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[100]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-pre-bg'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[900]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-th-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[300]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-td-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[200]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-th-bg'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[50]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-body'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[200]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-headings'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.white'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-lead'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[300]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-links'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.white'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-bold'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.white'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-counters'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[400]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-bullets'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[600]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-hr'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[700]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-quotes'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.pink[100]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-quote-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[700]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-captions'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[400]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-code'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.white'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-pre-code'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[300]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-pre-bg'", cls='s1'),
                        Span(':', cls='o'),
                        Span("'rgb(0 0 0 / 50%)'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-th-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[600]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-td-borders'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[700]'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'--tw-format-invert-th-bg'", cls='s1'),
                        Span(':', cls='o'),
                        Span('theme', cls='nx'),
                        Span('(', cls='p'),
                        Span("'colors.orange[700]'", cls='s1'),
                        Span('),', cls='p'),
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
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}),', cls='p'),
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
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('plugins', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('require', cls='nx'),
                        Span('(', cls='p'),
                        Span("'flowbite-typography'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// ...', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('],', cls='p'),
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
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    P(
        'Now you can use the',
        Code('format-red'),
        'class and apply these styles.'
    ),
    H3(
        'Wrapper class',
        Span(id='wrapper-class', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Wrapper class', href='#wrapper-class', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Change the default',
        Code('format'),
        'class to your own choosing by updating the',
        Code('tailwind.config.js'),
        'file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('module', cls='nx'),
                        Span('.', cls='p'),
                        Span('exports', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('theme', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// ...', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('},', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('plugins', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('require', cls='nx'),
                        Span('(', cls='p'),
                        Span("'flowbite-typography'", cls='s1'),
                        Span(')({', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('className', cls='nx'),
                        Span(':', cls='o'),
                        Span("'custom-class'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('}),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(']', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('...', cls='p'),
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
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H3(
        'Custom CSS',
        Span(id='custom-css', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Custom CSS', href='#custom-css', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can also customize the default CSS by extending the',
        Code('css'),
        'key value pair from the Tailwind configuration file:'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('module', cls='nx'),
                        Span('.', cls='p'),
                        Span('exports', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('theme', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('extend', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('typography', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('DEFAULT', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('css', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('color', cls='nx'),
                        Span(':', cls='o'),
                        Span("'#666'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('a', cls='nx'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('color', cls='nx'),
                        Span(':', cls='o'),
                        Span("'#3182ce'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'&:hover'", cls='s1'),
                        Span(':', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('color', cls='nx'),
                        Span(':', cls='o'),
                        Span("'#2c5282'", cls='s1'),
                        Span(',', cls='p'),
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
                        Span('},', cls='p'),
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
                        Span('},', cls='p'),
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
                        Span('},', cls='p'),
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
                        Span('plugins', cls='nx'),
                        Span(':', cls='o'),
                        Span('[', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('require', cls='nx'),
                        Span('(', cls='p'),
                        Span("'flowbite-typography'", cls='s1'),
                        Span('),', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// ...', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('],', cls='p'),
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
                data_lang='javascript',
                cls='language-javascript'
            ),
            tabindex='0',
            cls='chroma'
        ),
        cls='highlight'
    ),
    H2(
        'Blog templates',
        Span(id='blog-templates', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Blog templates', href='#blog-templates', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'You can check out the following',
        A('blog template', href='https://flowbite.com/blocks/publisher/blog-templates/'),
        'layouts from Flowbite Blocks that use the Typography plugin.'
    ),
    id='mainContent'
)
