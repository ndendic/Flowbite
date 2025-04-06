from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The textarea component is a multi-line text field input that can be used to receive longer chunks of text from the user in the form of a comment box, description field, and more.'),
    P('From the examples on this page you will find multiple styles and variants of the textarea component coded with the utility classes from Tailwind CSS including a WYSIWYG editor, comment box, chatroom textarea, all available in dark mode as well.'),
    H2(
        'Textarea example',
        Span(id='textarea-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Textarea example', href='#textarea-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with the default example of a textarea component below.'),
    component_showcase(Div(
    Label('Your message', fr='message', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Textarea(id='message', rows='4', placeholder='Write your thoughts here...', cls='block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
), code="""Div(
    Label('Your message', fr='message', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Textarea(id='message', rows='4', placeholder='Write your thoughts here...', cls='block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'WYSIWYG Editor',
        Span(id='wysiwyg-editor', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: WYSIWYG Editor', href='#wysiwyg-editor', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you want to add other actions as buttons alongside your textarea component, such as with a WYSIWYG editor, then you can use the example below.'),
    component_showcase(Div(
    Form(
        Div(
            Div(
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linejoin='round', stroke_width='2', d='M1 6v8a5 5 0 1 0 10 0V4.5a3.5 3.5 0 1 0-7 0V13a2 2 0 0 0 4 0V6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 12 20',
                                cls='w-4 h-4'
                            ),
                            Span('Attach file', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Embed map', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z'),
                                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Upload image', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                                Path(d='M14.067 0H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.933-2ZM6.709 13.809a1 1 0 1 1-1.418 1.409l-2-2.013a1 1 0 0 1 0-1.412l2-2a1 1 0 0 1 1.414 1.414L5.412 12.5l1.297 1.309Zm6-.6-2 2.013a1 1 0 1 1-1.418-1.409l1.3-1.307-1.295-1.295a1 1 0 0 1 1.414-1.414l2 2a1 1 0 0 1-.001 1.408v.004Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Format code', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM13.5 6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm-7 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm3.5 9.5A5.5 5.5 0 0 1 4.6 11h10.81A5.5 5.5 0 0 1 10 15.5Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Add emoji', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        cls='flex items-center space-x-1 rtl:space-x-reverse sm:pe-4'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9.5 3h9.563M9.5 9h9.563M9.5 15h9.563M1.5 13a2 2 0 1 1 3.321 1.5L1.5 17h5m-5-15 2-1v6m-2 0h4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 21 18',
                                cls='w-4 h-4'
                            ),
                            Span('Add list', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Settings', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M18 2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2ZM2 18V7h6.7l.4-.409A4.309 4.309 0 0 1 15.753 7H18v11H2Z'),
                                Path(d='M8.139 10.411 5.289 13.3A1 1 0 0 0 5 14v2a1 1 0 0 0 1 1h2a1 1 0 0 0 .7-.288l2.886-2.851-3.447-3.45ZM14 8a2.463 2.463 0 0 0-3.484 0l-.971.983 3.468 3.468.987-.971A2.463 2.463 0 0 0 14 8Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Timeline', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Download', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        cls='flex flex-wrap items-center space-x-1 rtl:space-x-reverse sm:ps-4'
                    ),
                    cls='flex flex-wrap items-center divide-gray-200 sm:divide-x sm:rtl:divide-x-reverse dark:divide-gray-600'
                ),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 1h5m0 0v5m0-5-5 5M1.979 6V1H7m0 16.042H1.979V12M18 12v5.042h-5M13 12l5 5M2 1l5 5m0 6-5 5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 19 19',
                        cls='w-4 h-4'
                    ),
                    Span('Full screen', cls='sr-only'),
                    type='button',
                    data_tooltip_target='tooltip-fullscreen',
                    cls='p-2 text-gray-500 rounded-sm cursor-pointer sm:ms-auto hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                ),
                Div(
                    'Show full screen',
                    Div(data_popper_arrow=True, cls='tooltip-arrow'),
                    id='tooltip-fullscreen',
                    role='tooltip',
                    cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                ),
                cls='flex items-center justify-between px-3 py-2 border-b border-gray-200 dark:border-gray-600 border-gray-200'
            ),
            Div(
                Label('Publish post', fr='editor', cls='sr-only'),
                Textarea(id='editor', rows='8', placeholder='Write an article...', required=True, cls='block w-full px-0 text-sm text-gray-800 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'),
                cls='px-4 py-2 bg-white rounded-b-lg dark:bg-gray-800'
            ),
            cls='w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
        ),
        Button('Publish post', type='submit', cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800')
    )
), code="""Div(
    Form(
        Div(
            Div(
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linejoin='round', stroke_width='2', d='M1 6v8a5 5 0 1 0 10 0V4.5a3.5 3.5 0 1 0-7 0V13a2 2 0 0 0 4 0V6'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 12 20',
                                cls='w-4 h-4'
                            ),
                            Span('Attach file', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Embed map', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M14.066 0H7v5a2 2 0 0 1-2 2H0v11a1.97 1.97 0 0 0 1.934 2h12.132A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.934-2ZM10.5 6a1.5 1.5 0 1 1 0 2.999A1.5 1.5 0 0 1 10.5 6Zm2.221 10.515a1 1 0 0 1-.858.485h-8a1 1 0 0 1-.9-1.43L5.6 10.039a.978.978 0 0 1 .936-.57 1 1 0 0 1 .9.632l1.181 2.981.541-1a.945.945 0 0 1 .883-.522 1 1 0 0 1 .879.529l1.832 3.438a1 1 0 0 1-.031.988Z'),
                                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.98 2.98 0 0 0 .13 5H5Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Upload image', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z'),
                                Path(d='M14.067 0H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18V2a1.97 1.97 0 0 0-1.933-2ZM6.709 13.809a1 1 0 1 1-1.418 1.409l-2-2.013a1 1 0 0 1 0-1.412l2-2a1 1 0 0 1 1.414 1.414L5.412 12.5l1.297 1.309Zm6-.6-2 2.013a1 1 0 1 1-1.418-1.409l1.3-1.307-1.295-1.295a1 1 0 0 1 1.414-1.414l2 2a1 1 0 0 1-.001 1.408v.004Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 16 20',
                                cls='w-4 h-4'
                            ),
                            Span('Format code', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM13.5 6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm-7 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm3.5 9.5A5.5 5.5 0 0 1 4.6 11h10.81A5.5 5.5 0 0 1 10 15.5Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Add emoji', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        cls='flex items-center space-x-1 rtl:space-x-reverse sm:pe-4'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9.5 3h9.563M9.5 9h9.563M9.5 15h9.563M1.5 13a2 2 0 1 1 3.321 1.5L1.5 17h5m-5-15 2-1v6m-2 0h4'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 21 18',
                                cls='w-4 h-4'
                            ),
                            Span('Add list', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Settings', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M18 2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2ZM2 18V7h6.7l.4-.409A4.309 4.309 0 0 1 15.753 7H18v11H2Z'),
                                Path(d='M8.139 10.411 5.289 13.3A1 1 0 0 0 5 14v2a1 1 0 0 0 1 1h2a1 1 0 0 0 .7-.288l2.886-2.851-3.447-3.45ZM14 8a2.463 2.463 0 0 0-3.484 0l-.971.983 3.468 3.468.987-.971A2.463 2.463 0 0 0 14 8Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Timeline', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4'
                            ),
                            Span('Download', cls='sr-only'),
                            type='button',
                            cls='p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                        ),
                        cls='flex flex-wrap items-center space-x-1 rtl:space-x-reverse sm:ps-4'
                    ),
                    cls='flex flex-wrap items-center divide-gray-200 sm:divide-x sm:rtl:divide-x-reverse dark:divide-gray-600'
                ),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 1h5m0 0v5m0-5-5 5M1.979 6V1H7m0 16.042H1.979V12M18 12v5.042h-5M13 12l5 5M2 1l5 5m0 6-5 5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 19 19',
                        cls='w-4 h-4'
                    ),
                    Span('Full screen', cls='sr-only'),
                    type='button',
                    data_tooltip_target='tooltip-fullscreen',
                    cls='p-2 text-gray-500 rounded-sm cursor-pointer sm:ms-auto hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                ),
                Div(
                    'Show full screen',
                    Div(data_popper_arrow=True, cls='tooltip-arrow'),
                    id='tooltip-fullscreen',
                    role='tooltip',
                    cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                ),
                cls='flex items-center justify-between px-3 py-2 border-b border-gray-200 dark:border-gray-600 border-gray-200'
            ),
            Div(
                Label('Publish post', fr='editor', cls='sr-only'),
                Textarea(id='editor', rows='8', placeholder='Write an article...', required=True, cls='block w-full px-0 text-sm text-gray-800 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'),
                cls='px-4 py-2 bg-white rounded-b-lg dark:bg-gray-800'
            ),
            cls='w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
        ),
        Button('Publish post', type='submit', cls='inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800')
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Comment box',
        Span(id='comment-box', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Comment box', href='#comment-box', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Most often the textarea component is used as the main text field input element in comment sections. Use this example to also apply a helper text and buttons below the textarea itself.'),
    component_showcase(Div(
    Form(
        Div(
            Div(
                Label('Your comment', fr='comment', cls='sr-only'),
                Textarea(id='comment', rows='4', placeholder='Write a comment...', required=True, cls='w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'),
                cls='px-4 py-2 bg-white rounded-t-lg dark:bg-gray-800'
            ),
            Div(
                Button('Post comment', type='submit', cls='inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800'),
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linejoin='round', stroke_width='2', d='M1 6v8a5 5 0 1 0 10 0V4.5a3.5 3.5 0 1 0-7 0V13a2 2 0 0 0 4 0V6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 12 20',
                            cls='w-4 h-4'
                        ),
                        Span('Attach file', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    Button(
                        Svg(
                            Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='w-4 h-4'
                        ),
                        Span('Set location', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    Button(
                        Svg(
                            Path(d='M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-4 h-4'
                        ),
                        Span('Upload image', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    cls='flex ps-0 space-x-1 rtl:space-x-reverse sm:ps-2'
                ),
                cls='flex items-center justify-between px-3 py-2 border-t dark:border-gray-600 border-gray-200'
            ),
            cls='w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
        )
    ),
    P(
        'Remember, contributions to this topic should follow our',
        A('Community Guidelines', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
        '.',
        cls='ms-auto text-xs text-gray-500 dark:text-gray-400'
    )
), code="""Div(
    Form(
        Div(
            Div(
                Label('Your comment', fr='comment', cls='sr-only'),
                Textarea(id='comment', rows='4', placeholder='Write a comment...', required=True, cls='w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400'),
                cls='px-4 py-2 bg-white rounded-t-lg dark:bg-gray-800'
            ),
            Div(
                Button('Post comment', type='submit', cls='inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800'),
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linejoin='round', stroke_width='2', d='M1 6v8a5 5 0 1 0 10 0V4.5a3.5 3.5 0 1 0-7 0V13a2 2 0 0 0 4 0V6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 12 20',
                            cls='w-4 h-4'
                        ),
                        Span('Attach file', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    Button(
                        Svg(
                            Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 16 20',
                            cls='w-4 h-4'
                        ),
                        Span('Set location', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    Button(
                        Svg(
                            Path(d='M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 20 18',
                            cls='w-4 h-4'
                        ),
                        Span('Upload image', cls='sr-only'),
                        type='button',
                        cls='inline-flex justify-center items-center p-2 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
                    ),
                    cls='flex ps-0 space-x-1 rtl:space-x-reverse sm:ps-2'
                ),
                cls='flex items-center justify-between px-3 py-2 border-t dark:border-gray-600 border-gray-200'
            ),
            cls='w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
        )
    ),
    P(
        'Remember, contributions to this topic should follow our',
        A('Community Guidelines', href='#', cls='text-primary-600 dark:text-primary-500 hover:underline'),
        '.',
        cls='ms-auto text-xs text-gray-500 dark:text-gray-400'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Chatroom input',
        Span(id='chatroom-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Chatroom input', href='#chatroom-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('If you want to build a chatroom component you will usually want to use a textarea element to allow users to write multi-line chunks of text.'),
    component_showcase(Div(
    Form(
        Label('Your message', fr='chat', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(fill='currentColor', d='M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z'),
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M18 1H2a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z'),
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 18',
                    cls='w-5 h-5'
                ),
                Span('Upload image', cls='sr-only'),
                type='button',
                cls='inline-flex justify-center p-2 text-gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13.408 7.5h.01m-6.876 0h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM4.6 11a5.5 5.5 0 0 0 10.81 0H4.6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-5 h-5'
                ),
                Span('Add emoji', cls='sr-only'),
                type='button',
                cls='p-2 text-gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Textarea(id='chat', rows='1', placeholder='Your message...', cls='block mx-4 p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(d='m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-5 h-5 rotate-90 rtl:-rotate-90'
                ),
                Span('Send message', cls='sr-only'),
                type='submit',
                cls='inline-flex justify-center p-2 text-primary-600 rounded-full cursor-pointer hover:bg-primary-100 dark:text-primary-500 dark:hover:bg-gray-600'
            ),
            cls='flex items-center px-3 py-2 rounded-lg bg-gray-50 dark:bg-gray-700'
        )
    )
), code="""Div(
    Form(
        Label('Your message', fr='chat', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(fill='currentColor', d='M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z'),
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M18 1H2a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1Z'),
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0ZM7.565 7.423 4.5 14h11.518l-2.516-3.71L11 13 7.565 7.423Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 18',
                    cls='w-5 h-5'
                ),
                Span('Upload image', cls='sr-only'),
                type='button',
                cls='inline-flex justify-center p-2 text-gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13.408 7.5h.01m-6.876 0h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM4.6 11a5.5 5.5 0 0 0 10.81 0H4.6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-5 h-5'
                ),
                Span('Add emoji', cls='sr-only'),
                type='button',
                cls='p-2 text-gray-500 rounded-lg cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Textarea(id='chat', rows='1', placeholder='Your message...', cls='block mx-4 p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(d='m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-5 h-5 rotate-90 rtl:-rotate-90'
                ),
                Span('Send message', cls='sr-only'),
                type='submit',
                cls='inline-flex justify-center p-2 text-primary-600 rounded-full cursor-pointer hover:bg-primary-100 dark:text-primary-500 dark:hover:bg-gray-600'
            ),
            cls='flex items-center px-3 py-2 rounded-lg bg-gray-50 dark:bg-gray-700'
        )
    )
)""", id="example_3",cls='mt-2 mb-6'),
    id='mainContent'
)
