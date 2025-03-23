from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('Following is an example of an article component, that can be used to display blog posts or other content.'),
    H2(
        'Default article',
        Span(id='default-article', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default article', href='#default-article', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following examples of alert components to show messages as feedback to your users.'),
    component_showcase(Article(
    H1('Prototyping from A to Z: best practices for successful prototypes'),
    P('Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.', cls='lead'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.'),
    P(
        'But then I found a',
        A('component library based on Tailwind CSS called Flowbite', href='#'),
        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.'
    ),
    '...',
    H2('When does design come in handy?'),
    P('While it might seem like extra work at a first glance, here are some key moments in which prototyping will come in handy:'),
    Ol(
        Li(
            Strong('Usability testing'),
            '. Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site you’ve designed? By running a usability test, you’ll be able to see how users will interact with your design once it’s live;'
        ),
        Li(
            Strong('Involving stakeholders'),
            '. Need to check if your GDPR consent boxes are displaying properly? Pass your prototype to your data protection team and they can test it for real;'
        ),
        Li(
            Strong('Impressing a client'),
            '. Prototypes can help explain or even sell your idea by providing your client with a hands-on experience;'
        ),
        Li(
            Strong('Communicating your vision'),
            '. By using an interactive medium to preview and test design elements, designers and developers can understand each other — and the project — better.'
        )
    ),
), code="""Article(
    H1('Prototyping from A to Z: best practices for successful prototypes'),
    P('Flowbite is an open-source library of UI components built with the utility-first classes from Tailwind CSS. It also includes interactive elements such as dropdowns, modals, datepickers.', cls='lead'),
    P('Before going digital, you might benefit from scribbling down some ideas in a sketchbook. This way, you can think things through before committing to an actual design project.'),
    P(
        'But then I found a',
        A('component library based on Tailwind CSS called Flowbite', href='#'),
        '. It comes with the most commonly used UI components, such as buttons, navigation bars, cards, form elements, and more which are conveniently built with the utility classes from Tailwind CSS.'
    ),
    '...',
    H2('When does design come in handy?'),
    P('While it might seem like extra work at a first glance, here are some key moments in which prototyping will come in handy:'),
    Ol(
        Li(
            Strong('Usability testing'),
            '. Does your user know how to exit out of screens? Can they follow your intended user journey and buy something from the site you’ve designed? By running a usability test, you’ll be able to see how users will interact with your design once it’s live;'
        ),
        Li(
            Strong('Involving stakeholders'),
            '. Need to check if your GDPR consent boxes are displaying properly? Pass your prototype to your data protection team and they can test it for real;'
        ),
        Li(
            Strong('Impressing a client'),
            '. Prototypes can help explain or even sell your idea by providing your client with a hands-on experience;'
        ),
        Li(
            Strong('Communicating your vision'),
            '. By using an interactive medium to preview and test design elements, designers and developers can understand each other — and the project — better.'
        )
    ),
    cls='format lg:format-lg'
)""", id="example_0",cls='mt-2 mb-6'),
    
)