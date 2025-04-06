from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The footer is one of the most underestimated sections of a website being located at the very bottom of every page, however, it can be used as a way to try to convince users to stay on your website if they haven’t found the information they’ve been looking for inside the main content area.'),
    P('Use these footer sections coded with the utility classes from Tailwind CSS and components from Flowbite to offer valuable information to your users such as the brand’s logo, sitemap links, copyright notice, social media profiles, and more.'),
    H2(
        'Default footer',
        Span(id='default-footer', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default footer', href='#default-footer', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this footer component to show a copyright notice and some helpful website links.'),
    component_showcase(Div(
    Footer(
        Div(
            Span(
                'Â© 2023',
                A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                '. All Rights Reserved.',
                cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
            ),
            Ul(
                Li(
                    A('About', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Contact', href='#', cls='hover:underline')
                ),
                cls='flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0'
            ),
            cls='w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between'
        ),
        cls='bg-white rounded-lg shadow-sm m-4 dark:bg-gray-800'
    )
), code="""Div(
    Footer(
        Div(
            Span(
                'Â© 2023',
                A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                '. All Rights Reserved.',
                cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
            ),
            Ul(
                Li(
                    A('About', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
                ),
                Li(
                    A('Contact', href='#', cls='hover:underline')
                ),
                cls='flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0'
            ),
            cls='w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between'
        ),
        cls='bg-white rounded-lg shadow-sm m-4 dark:bg-gray-800'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Footer with logo',
        Span(id='footer-with-logo', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Footer with logo', href='#footer-with-logo', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this component to show your brand’s logo, a few website links and the copyright notice on a second row.'),
    component_showcase(Div(
    Footer(
        Div(
            Div(
                A(
                    Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                    Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                    href='https://flowbite.com/',
                    cls='flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse'
                ),
                Ul(
                    Li(
                        A('About', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Contact', href='#', cls='hover:underline')
                    ),
                    cls='flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400'
                ),
                cls='sm:flex sm:items-center sm:justify-between'
            ),
            Hr(cls='my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8'),
            Span(
                'Â© 2023',
                A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                '. All Rights Reserved.',
                cls='block text-sm text-gray-500 sm:text-center dark:text-gray-400'
            ),
            cls='w-full max-w-screen-xl mx-auto p-4 md:py-8'
        ),
        cls='bg-white rounded-lg shadow-sm dark:bg-gray-900 m-4'
    )
), code="""Div(
    Footer(
        Div(
            Div(
                A(
                    Img(src='https://flowbite.com/docs/images/logo.svg', alt='Flowbite Logo', cls='h-8'),
                    Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                    href='https://flowbite.com/',
                    cls='flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse'
                ),
                Ul(
                    Li(
                        A('About', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
                    ),
                    Li(
                        A('Contact', href='#', cls='hover:underline')
                    ),
                    cls='flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400'
                ),
                cls='sm:flex sm:items-center sm:justify-between'
            ),
            Hr(cls='my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8'),
            Span(
                'Â© 2023',
                A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                '. All Rights Reserved.',
                cls='block text-sm text-gray-500 sm:text-center dark:text-gray-400'
            ),
            cls='w-full max-w-screen-xl mx-auto p-4 md:py-8'
        ),
        cls='bg-white rounded-lg shadow-sm dark:bg-gray-900 m-4'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Social media icons',
        Span(id='social-media-icons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Social media icons', href='#social-media-icons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This footer component can be used to show your brand’s logo, multiple rows of website links, a copyright notice and social media profile icons including Twitter, Facebook, Instagram, and more.'),
    component_showcase(Div(
    Footer(
        Div(
            Div(
                Div(
                    A(
                        Img(src='https://flowbite.com/docs/images/logo.svg', alt='FlowBite Logo', cls='h-8 me-3'),
                        Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                        href='https://flowbite.com/',
                        cls='flex items-center'
                    ),
                    cls='mb-6 md:mb-0'
                ),
                Div(
                    Div(
                        H2('Resources', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Flowbite', href='https://flowbite.com/', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Tailwind CSS', href='https://tailwindcss.com/', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    Div(
                        H2('Follow us', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Github', href='https://github.com/themesberg/flowbite', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Discord', href='https://discord.gg/4eeurUVvTy', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    Div(
                        H2('Legal', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Privacy Policy', href='#', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Terms & Conditions', href='#', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    cls='grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3'
                ),
                cls='md:flex md:justify-between'
            ),
            Hr(cls='my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8'),
            Div(
                Span(
                    'Â© 2023',
                    A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                    '. All Rights Reserved.',
                    cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
                ),
                Div(
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 8 19',
                            cls='w-4 h-4'
                        ),
                        Span('Facebook page', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(d='M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 16',
                            cls='w-4 h-4'
                        ),
                        Span('Discord community', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 17',
                            cls='w-4 h-4'
                        ),
                        Span('Twitter page', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('GitHub account', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('Dribbble account', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    cls='flex mt-4 sm:justify-center sm:mt-0'
                ),
                cls='sm:flex sm:items-center sm:justify-between'
            ),
            cls='mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8'
        ),
        cls='bg-white dark:bg-gray-900'
    )
), code="""Div(
    Footer(
        Div(
            Div(
                Div(
                    A(
                        Img(src='https://flowbite.com/docs/images/logo.svg', alt='FlowBite Logo', cls='h-8 me-3'),
                        Span('Flowbite', cls='self-center text-2xl font-semibold whitespace-nowrap dark:text-white'),
                        href='https://flowbite.com/',
                        cls='flex items-center'
                    ),
                    cls='mb-6 md:mb-0'
                ),
                Div(
                    Div(
                        H2('Resources', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Flowbite', href='https://flowbite.com/', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Tailwind CSS', href='https://tailwindcss.com/', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    Div(
                        H2('Follow us', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Github', href='https://github.com/themesberg/flowbite', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Discord', href='https://discord.gg/4eeurUVvTy', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    Div(
                        H2('Legal', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                        Ul(
                            Li(
                                A('Privacy Policy', href='#', cls='hover:underline'),
                                cls='mb-4'
                            ),
                            Li(
                                A('Terms & Conditions', href='#', cls='hover:underline')
                            ),
                            cls='text-gray-500 dark:text-gray-400 font-medium'
                        )
                    ),
                    cls='grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3'
                ),
                cls='md:flex md:justify-between'
            ),
            Hr(cls='my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8'),
            Div(
                Span(
                    'Â© 2023',
                    A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
                    '. All Rights Reserved.',
                    cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
                ),
                Div(
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 8 19',
                            cls='w-4 h-4'
                        ),
                        Span('Facebook page', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(d='M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 16',
                            cls='w-4 h-4'
                        ),
                        Span('Discord community', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 17',
                            cls='w-4 h-4'
                        ),
                        Span('Twitter page', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('GitHub account', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('Dribbble account', cls='sr-only'),
                        href='#',
                        cls='text-gray-500 hover:text-gray-900 dark:hover:text-white ms-5'
                    ),
                    cls='flex mt-4 sm:justify-center sm:mt-0'
                ),
                cls='sm:flex sm:items-center sm:justify-between'
            ),
            cls='mx-auto w-full max-w-screen-xl p-4 py-6 lg:py-8'
        ),
        cls='bg-white dark:bg-gray-900'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Sitemap links',
        Span(id='sitemap-links', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sitemap links', href='#sitemap-links', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you have a website with many pages you can use this footer component to show a sitemap spanning the entire width of a row followed below by a copyright notice and social media icons.'),
    component_showcase(Div(
    Footer(
        Div(
            Div(
                Div(
                    H2('Company', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('About', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Careers', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Brand Center', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Blog', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Help center', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('Discord Server', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Twitter', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Facebook', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Contact Us', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Legal', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('Privacy Policy', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Licensing', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Terms & Conditions', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Download', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('iOS', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Android', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Windows', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('MacOS', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                cls='grid grid-cols-2 gap-8 px-4 py-6 lg:py-8 md:grid-cols-4'
            ),
            Div(
                Span(
                    'Â© 2023',
                    A('Flowbiteâ\x84¢', href='https://flowbite.com/'),
                    '. All Rights Reserved.',
                    cls='text-sm text-gray-500 dark:text-gray-300 sm:text-center'
                ),
                Div(
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 8 19',
                            cls='w-4 h-4'
                        ),
                        Span('Facebook page', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(d='M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 16',
                            cls='w-4 h-4'
                        ),
                        Span('Discord community', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 17',
                            cls='w-4 h-4'
                        ),
                        Span('Twitter page', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('GitHub account', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('Dribbble account', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    cls='flex mt-4 sm:justify-center md:mt-0 space-x-5 rtl:space-x-reverse'
                ),
                cls='px-4 py-6 bg-gray-100 dark:bg-gray-700 md:flex md:items-center md:justify-between'
            ),
            cls='mx-auto w-full max-w-screen-xl'
        ),
        cls='bg-white dark:bg-gray-900'
    )
), code="""Div(
    Footer(
        Div(
            Div(
                Div(
                    H2('Company', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('About', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Careers', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Brand Center', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Blog', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Help center', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('Discord Server', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Twitter', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Facebook', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Contact Us', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Legal', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('Privacy Policy', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Licensing', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Terms & Conditions', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                Div(
                    H2('Download', cls='mb-6 text-sm font-semibold text-gray-900 uppercase dark:text-white'),
                    Ul(
                        Li(
                            A('iOS', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Android', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('Windows', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        Li(
                            A('MacOS', href='#', cls='hover:underline'),
                            cls='mb-4'
                        ),
                        cls='text-gray-500 dark:text-gray-400 font-medium'
                    )
                ),
                cls='grid grid-cols-2 gap-8 px-4 py-6 lg:py-8 md:grid-cols-4'
            ),
            Div(
                Span(
                    'Â© 2023',
                    A('Flowbiteâ\x84¢', href='https://flowbite.com/'),
                    '. All Rights Reserved.',
                    cls='text-sm text-gray-500 dark:text-gray-300 sm:text-center'
                ),
                Div(
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 8 19',
                            cls='w-4 h-4'
                        ),
                        Span('Facebook page', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(d='M16.942 1.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.585 11.585 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3A17.392 17.392 0 0 0 .182 13.218a15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.63 10.63 0 0 1-1.706-.83c.143-.106.283-.217.418-.33a11.664 11.664 0 0 0 10.118 0c.137.113.277.224.418.33-.544.328-1.116.606-1.71.832a12.52 12.52 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM6.678 10.813a1.941 1.941 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 21 16',
                            cls='w-4 h-4'
                        ),
                        Span('Discord community', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M20 1.892a8.178 8.178 0 0 1-2.355.635 4.074 4.074 0 0 0 1.8-2.235 8.344 8.344 0 0 1-2.605.98A4.13 4.13 0 0 0 13.85 0a4.068 4.068 0 0 0-4.1 4.038 4 4 0 0 0 .105.919A11.705 11.705 0 0 1 1.4.734a4.006 4.006 0 0 0 1.268 5.392 4.165 4.165 0 0 1-1.859-.5v.05A4.057 4.057 0 0 0 4.1 9.635a4.19 4.19 0 0 1-1.856.07 4.108 4.108 0 0 0 3.831 2.807A8.36 8.36 0 0 1 0 14.184 11.732 11.732 0 0 0 6.291 16 11.502 11.502 0 0 0 17.964 4.5c0-.177 0-.35-.012-.523A8.143 8.143 0 0 0 20 1.892Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 17',
                            cls='w-4 h-4'
                        ),
                        Span('Twitter page', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('GitHub account', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    A(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 0a10 10 0 1 0 10 10A10.009 10.009 0 0 0 10 0Zm6.613 4.614a8.523 8.523 0 0 1 1.93 5.32 20.094 20.094 0 0 0-5.949-.274c-.059-.149-.122-.292-.184-.441a23.879 23.879 0 0 0-.566-1.239 11.41 11.41 0 0 0 4.769-3.366ZM8 1.707a8.821 8.821 0 0 1 2-.238 8.5 8.5 0 0 1 5.664 2.152 9.608 9.608 0 0 1-4.476 3.087A45.758 45.758 0 0 0 8 1.707ZM1.642 8.262a8.57 8.57 0 0 1 4.73-5.981A53.998 53.998 0 0 1 9.54 7.222a32.078 32.078 0 0 1-7.9 1.04h.002Zm2.01 7.46a8.51 8.51 0 0 1-2.2-5.707v-.262a31.64 31.64 0 0 0 8.777-1.219c.243.477.477.964.692 1.449-.114.032-.227.067-.336.1a13.569 13.569 0 0 0-6.942 5.636l.009.003ZM10 18.556a8.508 8.508 0 0 1-5.243-1.8 11.717 11.717 0 0 1 6.7-5.332.509.509 0 0 1 .055-.02 35.65 35.65 0 0 1 1.819 6.476 8.476 8.476 0 0 1-3.331.676Zm4.772-1.462A37.232 37.232 0 0 0 13.113 11a12.513 12.513 0 0 1 5.321.364 8.56 8.56 0 0 1-3.66 5.73h-.002Z', clip_rule='evenodd'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            cls='w-4 h-4'
                        ),
                        Span('Dribbble account', cls='sr-only'),
                        href='#',
                        cls='text-gray-400 hover:text-gray-900 dark:hover:text-white'
                    ),
                    cls='flex mt-4 sm:justify-center md:mt-0 space-x-5 rtl:space-x-reverse'
                ),
                cls='px-4 py-6 bg-gray-100 dark:bg-gray-700 md:flex md:items-center md:justify-between'
            ),
            cls='mx-auto w-full max-w-screen-xl'
        ),
        cls='bg-white dark:bg-gray-900'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Sticky footer',
        Span(id='sticky-footer', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sticky footer', href='#sticky-footer', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to set create a sticky footer by using a fixed position to the bottom of the document page as the user scrolls up or down the main content area.'),
    component_showcase(Div(
    Footer(
        Span(
            'Â© 2023',
            A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
            '. All Rights Reserved.',
            cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
        ),
        Ul(
            Li(
                A('About', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Contact', href='#', cls='hover:underline')
            ),
            cls='flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0'
        ),
        cls='fixed bottom-0 left-0 z-20 w-full p-4 bg-white border-t border-gray-200 shadow-sm md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600'
    )
), code="""Div(
    Footer(
        Span(
            'Â© 2023',
            A('Flowbiteâ\x84¢', href='https://flowbite.com/', cls='hover:underline'),
            '. All Rights Reserved.',
            cls='text-sm text-gray-500 sm:text-center dark:text-gray-400'
        ),
        Ul(
            Li(
                A('About', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Privacy Policy', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Licensing', href='#', cls='hover:underline me-4 md:me-6')
            ),
            Li(
                A('Contact', href='#', cls='hover:underline')
            ),
            cls='flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0'
        ),
        cls='fixed bottom-0 left-0 z-20 w-full p-4 bg-white border-t border-gray-200 shadow-sm md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('For more footer examples you can check out the footer sections from Flowbite Blocks:'),
    Ul(
        Li(
            A('Footers for dashboard', href='https://flowbite.com/blocks/application/dashboard-footer/')
        ),
        Li(
            A('Footers for marketing', href='https://flowbite.com/blocks/marketing/footer/')
        )
    ),
    id='mainContent'
)
