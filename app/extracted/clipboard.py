from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The copy to clipboard component allows you to copy text, lines of code, contact details or any other data to the clipboard with a single click on a trigger element such as a button. This component can be used to copy text from an input field, textarea, code block or even address fields in a form element.'),
    P('Use cases for websites can be found in the examples below and they include copying code installation commands, API keys, URLs, addresses, contact details, sharing course URLs inside a modal and more.'),
    P('These components are built with Tailwind CSS and Flowbite and can be found on the internet on websites such as Bitly, Cloudflare, Amazon AWS and almost all open-source projects and documentations.'),
    H2(
        'Default copy to clipboard',
        Span(id='default-copy-to-clipboard', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default copy to clipboard', href='#default-copy-to-clipboard', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Make sure that you add the',
        Code('data-copy-to-clipboard-target="elementID"'),
        'data attribute to the trigger element (ie. the button) to initialize the JS behavior where the',
        Code('elementID'),
        'is the ID of the element where the source text can be found (such as input field).'
    ),
    P(
        'Use this example to copy the content of an input text field by clicking on a button and update the button text by applying the JavaScript code from the tab below based on the',
        Code('updateOnCopyCallback()'),
        'function callback from the Flowbite JS API.'
    ),
    component_showcase(Div(
    Div(
        Label('Label', fr='npm-install', cls='sr-only'),
        Input(id='npm-install', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        Button(
            Span('Copy', id='default-message'),
            Span(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-white me-1.5'
                    ),
                    'Copied!',
                    cls='inline-flex items-center'
                ),
                id='success-message',
                cls='hidden'
            ),
            data_copy_to_clipboard_target='npm-install',
            cls='col-span-2 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 items-center inline-flex justify-center'
        ),
        cls='grid grid-cols-8 gap-2 w-full max-w-[23rem]'
    )
), code="""Div(
    Div(
        Label('Label', fr='npm-install', cls='sr-only'),
        Input(id='npm-install', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        Button(
            Span('Copy', id='default-message'),
            Span(
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3 h-3 text-white me-1.5'
                    ),
                    'Copied!',
                    cls='inline-flex items-center'
                ),
                id='success-message',
                cls='hidden'
            ),
            data_copy_to_clipboard_target='npm-install',
            cls='col-span-2 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 items-center inline-flex justify-center'
        ),
        cls='grid grid-cols-8 gap-2 w-full max-w-[23rem]'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Input with copy button',
        Span(id='input-with-copy-button', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Input with copy button', href='#input-with-copy-button', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to copy the content of an input field by clicking on a button with an icon positioned inside the form element and also show a tooltip with a message when the text has been copied.'),
    P(
        'If you also want to update the text inside the tooltip and the icon, then you need to apply the JavaScript code based on the',
        Code('updateOnCopyCallback()'),
        'function callback from the Flowbite JS API.'
    ),
    component_showcase(Div(
    Div(
        Div(
            Label('Label', fr='npm-install-copy-button', cls='sr-only'),
            Input(id='npm-install-copy-button', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='npm-install-copy-button',
                data_tooltip_target='tooltip-copy-npm-install-copy-button',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-copy-npm-install-copy-button',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative'
        ),
        cls='w-full max-w-[16rem]'
    )
), code="""Div(
    Div(
        Div(
            Label('Label', fr='npm-install-copy-button', cls='sr-only'),
            Input(id='npm-install-copy-button', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='npm-install-copy-button',
                data_tooltip_target='tooltip-copy-npm-install-copy-button',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-copy-npm-install-copy-button',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative'
        ),
        cls='w-full max-w-[16rem]'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Copy button with text',
        Span(id='copy-button-with-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Copy button with text', href='#copy-button-with-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a copy button inside the input field with a text label and icon that updates to a success state when the text has been copied. Make sure that you also apply the custom JavaScript code below to enable the success and default message states.'),
    component_showcase(Div(
    Div(
        Div(
            Label('Label', fr='npm-install-copy-text', cls='sr-only'),
            Input(id='npm-install-copy-text', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full px-2.5 py-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Span(
                        Svg(
                            Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='w-3 h-3 me-1.5'
                        ),
                        Span('Copy', cls='text-xs font-semibold'),
                        cls='inline-flex items-center'
                    ),
                    id='default-message'
                ),
                Span(
                    Span(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 12',
                            cls='w-3 h-3 text-primary-700 dark:text-primary-500 me-1.5'
                        ),
                        Span('Copied', cls='text-xs font-semibold text-primary-700 dark:text-primary-500'),
                        cls='inline-flex items-center'
                    ),
                    id='success-message',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='npm-install-copy-text',
                cls='absolute end-2.5 top-1/2 -translate-y-1/2 text-gray-900 dark:text-gray-400 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-600 dark:hover:bg-gray-700 rounded-lg py-2 px-2.5 inline-flex items-center justify-center bg-white border-gray-200 border h-8'
            ),
            cls='relative'
        ),
        cls='w-full max-w-[16rem]'
    )
), code="""Div(
    Div(
        Div(
            Label('Label', fr='npm-install-copy-text', cls='sr-only'),
            Input(id='npm-install-copy-text', type='text', value='npm install flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full px-2.5 py-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Span(
                        Svg(
                            Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 18 20',
                            cls='w-3 h-3 me-1.5'
                        ),
                        Span('Copy', cls='text-xs font-semibold'),
                        cls='inline-flex items-center'
                    ),
                    id='default-message'
                ),
                Span(
                    Span(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 12',
                            cls='w-3 h-3 text-primary-700 dark:text-primary-500 me-1.5'
                        ),
                        Span('Copied', cls='text-xs font-semibold text-primary-700 dark:text-primary-500'),
                        cls='inline-flex items-center'
                    ),
                    id='success-message',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='npm-install-copy-text',
                cls='absolute end-2.5 top-1/2 -translate-y-1/2 text-gray-900 dark:text-gray-400 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-600 dark:hover:bg-gray-700 rounded-lg py-2 px-2.5 inline-flex items-center justify-center bg-white border-gray-200 border h-8'
            ),
            cls='relative'
        ),
        cls='w-full max-w-[16rem]'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Input group with copy',
        Span(id='input-group-with-copy', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Input group with copy', href='#input-group-with-copy', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a copy to clipboard button inside an input group which has a label positioned inside the input field. The icon inside the button will switch to a success state if you also apply the custom JavaScript code below.'),
    component_showcase(Div(
    Div(
        Div(
            Label('Verify your website:', fr='website-url', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Span('URL', cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg dark:bg-gray-600 dark:text-white dark:border-gray-600'),
            Div(
                Input(id='website-url', type='text', aria_describedby='helper-text-explanation', value='https://flowbite.com', readonly=True, disabled=True, cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-500 dark:text-gray-400 text-sm border-s-0 focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_tooltip_target='tooltip-website-url',
                data_copy_to_clipboard_target='website-url',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-white bg-primary-700 rounded-e-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 border border-primary-700 dark:border-primary-600 hover:border-primary-800 dark:hover:border-primary-700'
            ),
            Div(
                Span('Copy link', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-website-url',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Security certificate is required for approval', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-sm'
    )
), code="""Div(
    Div(
        Div(
            Label('Verify your website:', fr='website-url', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Span('URL', cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg dark:bg-gray-600 dark:text-white dark:border-gray-600'),
            Div(
                Input(id='website-url', type='text', aria_describedby='helper-text-explanation', value='https://flowbite.com', readonly=True, disabled=True, cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-500 dark:text-gray-400 text-sm border-s-0 focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_tooltip_target='tooltip-website-url',
                data_copy_to_clipboard_target='website-url',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-white bg-primary-700 rounded-e-lg hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 border border-primary-700 dark:border-primary-600 hover:border-primary-800 dark:hover:border-primary-700'
            ),
            Div(
                Span('Copy link', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-website-url',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Security certificate is required for approval', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-sm'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'URL shortener input group',
        Span(id='url-shortener-input-group', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: URL shortener input group', href='#url-shortener-input-group', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to copy a shortened URL to the clipboard by clicking on a button with an icon positioned inside the input field and also show a tooltip with a message when the text has been copied.'),
    component_showcase(Div(
    Div(
        Div(
            Label('Shorten URL:', fr='url-shortener', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Button('Generate', cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-white bg-primary-700 dark:bg-primary-600 border hover:bg-primary-800 dark:hover:bg-primary-700 rounded-s-lg border-primary-700 dark:border-primary-600 hover:border-primary-700 dark:hover:border-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:focus:ring-primary-800'),
            Div(
                Input(id='url-shortener', type='text', aria_describedby='helper-text-explanation', value='https://bit.ly/3U2SXcF', readonly=True, disabled=True, cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-500 dark:text-gray-400 text-sm border-s-0 focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_tooltip_target='tooltip-url-shortener',
                data_copy_to_clipboard_target='url-shortener',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-gray-500 dark:text-gray-400 hover:text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:hover:text-white dark:border-gray-600'
            ),
            Div(
                Span('Copy link', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-url-shortener',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Make sure that your URL is valid', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-sm'
    )
), code="""Div(
    Div(
        Div(
            Label('Shorten URL:', fr='url-shortener', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Button('Generate', cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-white bg-primary-700 dark:bg-primary-600 border hover:bg-primary-800 dark:hover:bg-primary-700 rounded-s-lg border-primary-700 dark:border-primary-600 hover:border-primary-700 dark:hover:border-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 dark:focus:ring-primary-800'),
            Div(
                Input(id='url-shortener', type='text', aria_describedby='helper-text-explanation', value='https://bit.ly/3U2SXcF', readonly=True, disabled=True, cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-500 dark:text-gray-400 text-sm border-s-0 focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-4 h-4'
                    ),
                    id='default-icon'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-4 h-4'
                    ),
                    id='success-icon',
                    cls='hidden'
                ),
                data_tooltip_target='tooltip-url-shortener',
                data_copy_to_clipboard_target='url-shortener',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-gray-500 dark:text-gray-400 hover:text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:hover:text-white dark:border-gray-600'
            ),
            Div(
                Span('Copy link', id='default-tooltip-message'),
                Span('Copied!', id='success-tooltip-message', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-url-shortener',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Make sure that your URL is valid', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-sm'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Copy source code block',
        Span(id='copy-source-code-block', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Copy source code block', href='#copy-source-code-block', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to copy and paste code inside a',
        Code('<pre>'),
        'and',
        Code('<code>'),
        'block by clicking on a button with an icon position inside the block and also show a tooltip with a message when the text has been copied.'
    ),
    P(
        'You need to add an extra',
        Code('data-copy-to-clipboard-content-type="innerHTML"'),
        'data attribute to the trigger element (ie. the button) to specify that the content that is to be copied is from the',
        Code('innerHTML'),
        'of the target element (ie. the code block).'
    ),
    P(
        'You also need to add the',
        Code('data-copy-to-clipboard-html-entities="true"'),
        'option to the trigger element so that the copied text will be decoded from HTML entities to plain text that will work inside your code editor.'
    ),
    component_showcase(Div(
    Div(
        Div(
            P('Card example with CTA button:', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Div(
                Pre(
                    Code('\'use client\';\n\nimport Link from \'next/link\';\nimport { Navbar } from \'flowbite-react\';\n\nfunction Component() {\n  return (\n    <Navbar fluid rounded>\n      <Navbar.Brand as={Link} href="https://flowbite-react.com">\n        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />\n        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>\n      </Navbar.Brand>\n      <Navbar.Toggle />\n      <Navbar.Collapse>\n        <Navbar.Link href="#" active>\n          Home\n        </Navbar.Link>\n        <Navbar.Link as={Link} href="#">\n          About\n        </Navbar.Link>\n        <Navbar.Link href="#">Services</Navbar.Link>\n        <Navbar.Link href="#">Pricing</Navbar.Link>\n        <Navbar.Link href="#">Contact</Navbar.Link>\n      </Navbar.Collapse>\n    </Navbar>\n  );\n}', id='code-block', cls='text-sm text-gray-500 dark:text-gray-400 whitespace-pre')
                ),
                cls='overflow-scroll max-h-full'
            ),
            Div(
                Button(
                    Span(
                        Span(
                            Svg(
                                Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 18 20',
                                cls='w-3 h-3 me-1.5'
                            ),
                            Span('Copy code', cls='text-xs font-semibold'),
                            cls='inline-flex items-center'
                        ),
                        id='default-message'
                    ),
                    Span(
                        Span(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 12',
                                cls='w-3 h-3 text-primary-700 dark:text-primary-500 me-1.5'
                            ),
                            Span('Copied', cls='text-xs font-semibold text-primary-700 dark:text-primary-500'),
                            cls='inline-flex items-center'
                        ),
                        id='success-message',
                        cls='hidden'
                    ),
                    data_copy_to_clipboard_target='code-block',
                    data_copy_to_clipboard_content_type='innerHTML',
                    data_copy_to_clipboard_html_entities='true',
                    cls='text-gray-900 dark:text-gray-400 m-0.5 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-600 dark:hover:bg-gray-700 rounded-lg py-2 px-2.5 inline-flex items-center justify-center bg-white border-gray-200 border h-8'
                ),
                cls='absolute top-2 end-2 bg-gray-50 dark:bg-gray-700'
            ),
            cls='relative bg-gray-50 rounded-lg dark:bg-gray-700 p-4 h-64'
        ),
        P('Configure Tailwind CSS and Flowbite before copying the code', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-lg'
    )
), code="""Div(
    Div(
        Div(
            P('Card example with CTA button:', cls='text-sm font-medium text-gray-900 dark:text-white'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Div(
                Pre(
                    Code('\'use client\';\n\nimport Link from \'next/link\';\nimport { Navbar } from \'flowbite-react\';\n\nfunction Component() {\n  return (\n    <Navbar fluid rounded>\n      <Navbar.Brand as={Link} href="https://flowbite-react.com">\n        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />\n        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>\n      </Navbar.Brand>\n      <Navbar.Toggle />\n      <Navbar.Collapse>\n        <Navbar.Link href="#" active>\n          Home\n        </Navbar.Link>\n        <Navbar.Link as={Link} href="#">\n          About\n        </Navbar.Link>\n        <Navbar.Link href="#">Services</Navbar.Link>\n        <Navbar.Link href="#">Pricing</Navbar.Link>\n        <Navbar.Link href="#">Contact</Navbar.Link>\n      </Navbar.Collapse>\n    </Navbar>\n  );\n}', id='code-block', cls='text-sm text-gray-500 dark:text-gray-400 whitespace-pre')
                ),
                cls='overflow-scroll max-h-full'
            ),
            Div(
                Button(
                    Span(
                        Span(
                            Svg(
                                Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 18 20',
                                cls='w-3 h-3 me-1.5'
                            ),
                            Span('Copy code', cls='text-xs font-semibold'),
                            cls='inline-flex items-center'
                        ),
                        id='default-message'
                    ),
                    Span(
                        Span(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 12',
                                cls='w-3 h-3 text-primary-700 dark:text-primary-500 me-1.5'
                            ),
                            Span('Copied', cls='text-xs font-semibold text-primary-700 dark:text-primary-500'),
                            cls='inline-flex items-center'
                        ),
                        id='success-message',
                        cls='hidden'
                    ),
                    data_copy_to_clipboard_target='code-block',
                    data_copy_to_clipboard_content_type='innerHTML',
                    data_copy_to_clipboard_html_entities='true',
                    cls='text-gray-900 dark:text-gray-400 m-0.5 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-600 dark:hover:bg-gray-700 rounded-lg py-2 px-2.5 inline-flex items-center justify-center bg-white border-gray-200 border h-8'
                ),
                cls='absolute top-2 end-2 bg-gray-50 dark:bg-gray-700'
            ),
            cls='relative bg-gray-50 rounded-lg dark:bg-gray-700 p-4 h-64'
        ),
        P('Configure Tailwind CSS and Flowbite before copying the code', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='w-full max-w-lg'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Card with API keys',
        Span(id='card-with-api-keys', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Card with API keys', href='#card-with-api-keys', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show multiple input field elements that have the copy to clipboard button inside a card component for more complex applications where you need to copy API keys, account IDs and more.'),
    P('Make sure that you also apply the custom JavaScript code with the function callback to enable the success and default message states for each input field and copy button.'),
    component_showcase(Div(
    Div(
        H2('Create a role with read only in-line policies', cls='text-lg font-semibold text-gray-900 dark:text-white mb-2'),
        P(
            'To give Flowbite read access, please create an IAM Role following',
            A('trust relationship', href='#', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium'),
            'and',
            A('inline policy', href='#', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium'),
            '.',
            cls='text-gray-500 dark:text-gray-400 mb-6'
        ),
        Label('Flowbite account ID:', fr='account-id', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='account-id', type='text', value='756593826', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-account-id'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-account-id',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='account-id',
                data_tooltip_target='tooltip-account-id',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-account-id'),
                Span('Copied!', id='success-tooltip-message-account-id', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-account-id',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-4'
        ),
        Label('API key:', fr='api-key', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='api-key', type='text', value='f4h6sd3t-jsy63ind-hsgdt7rs-jdhf76st', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-api-key'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-api-key',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='api-key',
                data_tooltip_target='tooltip-api-key',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-api-key'),
                Span('Copied!', id='success-tooltip-message-api-key', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-api-key',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-4'
        ),
        Label('Role ARN:', fr='role-arn', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='role-arn', type='text', value='123456789012:user/Flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-role-arn'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-role-arn',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='role-arn',
                data_tooltip_target='tooltip-role-arn',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-role-arn'),
                Span('Copied!', id='success-tooltip-message-role-arn', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-role-arn',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-6'
        ),
        Div(
            Button('Cancel', type='button', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
            Button('Next step', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
            cls='flex items-center space-x-4 rtl:space-x-reverse'
        ),
        cls='w-full max-w-lg bg-white dark:bg-gray-800 border-gray-200 border dark:border-gray-700 shadow-sm rounded-lg p-5'
    )
), code="""Div(
    Div(
        H2('Create a role with read only in-line policies', cls='text-lg font-semibold text-gray-900 dark:text-white mb-2'),
        P(
            'To give Flowbite read access, please create an IAM Role following',
            A('trust relationship', href='#', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium'),
            'and',
            A('inline policy', href='#', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium'),
            '.',
            cls='text-gray-500 dark:text-gray-400 mb-6'
        ),
        Label('Flowbite account ID:', fr='account-id', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='account-id', type='text', value='756593826', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-account-id'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-account-id',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='account-id',
                data_tooltip_target='tooltip-account-id',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-account-id'),
                Span('Copied!', id='success-tooltip-message-account-id', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-account-id',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-4'
        ),
        Label('API key:', fr='api-key', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='api-key', type='text', value='f4h6sd3t-jsy63ind-hsgdt7rs-jdhf76st', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-api-key'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-api-key',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='api-key',
                data_tooltip_target='tooltip-api-key',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-api-key'),
                Span('Copied!', id='success-tooltip-message-api-key', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-api-key',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-4'
        ),
        Label('Role ARN:', fr='role-arn', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
        Div(
            Input(id='role-arn', type='text', value='123456789012:user/Flowbite', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-role-arn'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-role-arn',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='role-arn',
                data_tooltip_target='tooltip-role-arn',
                cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-role-arn'),
                Span('Copied!', id='success-tooltip-message-role-arn', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-role-arn',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative mb-6'
        ),
        Div(
            Button('Cancel', type='button', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
            Button('Next step', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
            cls='flex items-center space-x-4 rtl:space-x-reverse'
        ),
        cls='w-full max-w-lg bg-white dark:bg-gray-800 border-gray-200 border dark:border-gray-700 shadow-sm rounded-lg p-5'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Copy contact details',
        Span(id='copy-contact-details', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Copy contact details', href='#copy-contact-details', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to copy the text content (ie. contact details) inside of the',
        Code('<address>'),
        'field by clicking on the copy to clipboard button positioned inside of the address card.'
    ),
    P(
        'Make sure that you set the',
        Code('data-copy-to-clipboard-content-type="textContent"'),
        'data attribute to the trigger element (ie. the button) to specify the source of the content that is to be copied.'
    ),
    component_showcase(Div(
    Div(
        H2('Contact details', cls='text-lg font-semibold text-gray-900 dark:text-white mb-2'),
        Address(
            Div(
                'Name',
                Br(),
                'Email',
                Br(),
                'Phone Number',
                cls='space-y-2 text-gray-500 dark:text-gray-400 leading-loose hidden sm:block'
            ),
            Div(
                'Bonnie Green',
                Br(),
                'name@flowbite.com',
                Br(),
                '+ 12 345 67890',
                id='contact-details',
                cls='space-y-2 text-gray-900 dark:text-white font-medium leading-loose'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-contact-details'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-contact-details',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='contact-details',
                data_copy_to_clipboard_content_type='textContent',
                data_tooltip_target='tooltip-contact-details',
                cls='absolute end-2 top-2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-contact-details'),
                Span('Copied!', id='success-tooltip-message-contact-details', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-contact-details',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative bg-gray-50 dark:bg-gray-700 dark:border-gray-600 p-4 rounded-lg border border-gray-200 not-italic grid grid-cols-2'
        ),
        cls='w-full max-w-md bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 shadow-sm rounded-lg p-5'
    )
), code="""Div(
    Div(
        H2('Contact details', cls='text-lg font-semibold text-gray-900 dark:text-white mb-2'),
        Address(
            Div(
                'Name',
                Br(),
                'Email',
                Br(),
                'Phone Number',
                cls='space-y-2 text-gray-500 dark:text-gray-400 leading-loose hidden sm:block'
            ),
            Div(
                'Bonnie Green',
                Br(),
                'name@flowbite.com',
                Br(),
                '+ 12 345 67890',
                id='contact-details',
                cls='space-y-2 text-gray-900 dark:text-white font-medium leading-loose'
            ),
            Button(
                Span(
                    Svg(
                        Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 18 20',
                        cls='w-3.5 h-3.5'
                    ),
                    id='default-icon-contact-details'
                ),
                Span(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 12',
                        cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                    ),
                    id='success-icon-contact-details',
                    cls='hidden'
                ),
                data_copy_to_clipboard_target='contact-details',
                data_copy_to_clipboard_content_type='textContent',
                data_tooltip_target='tooltip-contact-details',
                cls='absolute end-2 top-2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
            ),
            Div(
                Span('Copy to clipboard', id='default-tooltip-message-contact-details'),
                Span('Copied!', id='success-tooltip-message-contact-details', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-contact-details',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='relative bg-gray-50 dark:bg-gray-700 dark:border-gray-600 p-4 rounded-lg border border-gray-200 not-italic grid grid-cols-2'
        ),
        cls='w-full max-w-md bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 shadow-sm rounded-lg p-5'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Copy button with modal',
        Span(id='copy-button-with-modal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Copy button with modal', href='#copy-button-with-modal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an input field where you can copy the URL of the current page and also show a modal with the copied URL when the copy button is clicked.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(d='M17.5 3A3.5 3.5 0 0 0 14 7L8.1 9.8A3.5 3.5 0 0 0 2 12a3.5 3.5 0 0 0 6.1 2.3l6 2.7-.1.5a3.5 3.5 0 1 0 1-2.3l-6-2.7a3.5 3.5 0 0 0 0-1L15 9a3.5 3.5 0 0 0 6-2.4c0-2-1.6-3.5-3.5-3.5Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 24 24',
            cls='w-4 h-4 me-2'
        ),
        'Share course',
        type='button',
        data_modal_target='course-modal',
        data_modal_toggle='course-modal',
        cls='text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Share course', cls='text-lg text-gray-500 dark:text-gray-400'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-3 h-3'
                        ),
                        Span('Close modal', cls='sr-only'),
                        type='button',
                        data_modal_toggle='course-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-700 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5'
                ),
                Div(
                    Label('Share the course link below with your friends:', fr='course-url', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
                    Div(
                        Input(id='course-url', type='text', value='https://flowbite.com/docs/components/alerts/', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                        Button(
                            Span(
                                Svg(
                                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 18 20',
                                    cls='w-3.5 h-3.5'
                                ),
                                id='default-icon-course-url'
                            ),
                            Span(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 12',
                                    cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                                ),
                                id='success-icon-course-url',
                                cls='hidden'
                            ),
                            data_copy_to_clipboard_target='course-url',
                            data_tooltip_target='tooltip-course-url',
                            cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
                        ),
                        Div(
                            Span('Copy to clipboard', id='default-tooltip-message-course-url'),
                            Span('Copied!', id='success-tooltip-message-course-url', cls='hidden'),
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='tooltip-course-url',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='relative mb-4'
                    ),
                    Button('Close', type='button', data_modal_hide='course-modal', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='px-4 pb-4 md:px-5 md:pb-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-800'
            ),
            cls='relative p-4 w-full max-w-lg max-h-full'
        ),
        id='course-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button(
        Svg(
            Path(d='M17.5 3A3.5 3.5 0 0 0 14 7L8.1 9.8A3.5 3.5 0 0 0 2 12a3.5 3.5 0 0 0 6.1 2.3l6 2.7-.1.5a3.5 3.5 0 1 0 1-2.3l-6-2.7a3.5 3.5 0 0 0 0-1L15 9a3.5 3.5 0 0 0 6-2.4c0-2-1.6-3.5-3.5-3.5Z'),
            aria_hidden='true',
            xmlns='http://www.w3.org/2000/svg',
            fill='currentColor',
            viewbox='0 0 24 24',
            cls='w-4 h-4 me-2'
        ),
        'Share course',
        type='button',
        data_modal_target='course-modal',
        data_modal_toggle='course-modal',
        cls='text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Share course', cls='text-lg text-gray-500 dark:text-gray-400'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 14 14',
                            cls='w-3 h-3'
                        ),
                        Span('Close modal', cls='sr-only'),
                        type='button',
                        data_modal_toggle='course-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-700 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5'
                ),
                Div(
                    Label('Share the course link below with your friends:', fr='course-url', cls='text-sm font-medium text-gray-900 dark:text-white mb-2 block'),
                    Div(
                        Input(id='course-url', type='text', value='https://flowbite.com/docs/components/alerts/', disabled=True, readonly=True, cls='col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                        Button(
                            Span(
                                Svg(
                                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 18 20',
                                    cls='w-3.5 h-3.5'
                                ),
                                id='default-icon-course-url'
                            ),
                            Span(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5.917 5.724 10.5 15 1.5'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 12',
                                    cls='w-3.5 h-3.5 text-primary-700 dark:text-primary-500'
                                ),
                                id='success-icon-course-url',
                                cls='hidden'
                            ),
                            data_copy_to_clipboard_target='course-url',
                            data_tooltip_target='tooltip-course-url',
                            cls='absolute end-2 top-1/2 -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg p-2 inline-flex items-center justify-center'
                        ),
                        Div(
                            Span('Copy to clipboard', id='default-tooltip-message-course-url'),
                            Span('Copied!', id='success-tooltip-message-course-url', cls='hidden'),
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='tooltip-course-url',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='relative mb-4'
                    ),
                    Button('Close', type='button', data_modal_hide='course-modal', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='px-4 pb-4 md:px-5 md:pb-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-800'
            ),
            cls='relative p-4 w-full max-w-lg max-h-full'
        ),
        id='course-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('CopyClipboard'),
        'object from the Flowbite JS API to create a component with a trigger element (ie. an input field, code blocks, address tag) and target element (ie. button or text) where the content of the target element is copied to the clipboard when the trigger element is clicked.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the object parameters from the CopyClipboard object to set options such as the content type of the text that is to be copied (ie. value of an input field, text content or inner HTML) and other options.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Parameter', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Required', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('triggerEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass the trigger element (ie. a button or text) that will trigger the copy to clipboard event when being clicked.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Set the target element where the text that will be copied to the clipboard is located (ie. an input field, code block, address tag).', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Set these options to set the the content type, HTML decoder and callback function for the copy to clipboard event.', cls='px-6 py-4'),
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
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Options',
        Span(id='options', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Options', href='#options', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use these optional options for the CopyClipboard object to set the content type from where the text will be copied from, an optional HTML decoder for code blocks and function callbacks to set success and default messages.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Option', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('contentType', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Set the source of the text that will be copied: input (default), innerHTML or textContent.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('htmlEntities', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td('Set this option to true if you want to decode the HTML entities for code blocks. Default is false.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onCopy', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the text has been copied to the clipboard.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Methods',
        Span(id='methods', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Methods', href='#methods', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the following methods from the CopyClipboard component to programmatically work with the component such as copying the text on demand or updating the callback function.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Method', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('getTargetValue()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Get the value of the target element (ie. input field, code block, address tag).', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('copy()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to copy the text from the target element to the clipboard.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('decodeHTML()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to decode the HTML entities from the target element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnCopyCallback(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to update the callback function that is called when the text has been copied to the clipboard.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                )
            ),
            cls='w-full text-sm text-left text-gray-500 dark:text-gray-400'
        ),
        cls='relative my-10 overflow-x-auto shadow-md sm:rounded-lg'
    ),
    H3(
        'Example',
        Span(id='example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Example', href='#example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Check out the following example to learn how to create a new CopyClipboard component via the Flowbite JavaScript API and set up the class, options, and methods to programmatically work with the component.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the trigger element such as a button or text field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$triggerEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'copy-clipboard-button'", cls='s1'),
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
                        Span('// set the trigger element such as an input field or code block', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$targetEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'copy-text'", cls='s1'),
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
                        Span('// optional options with default values and callback functions', cls='c1'),
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
                        Span('contentType', cls='nx'),
                        Span(':', cls='o'),
                        Span("'input'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('htmlEntities', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        Span('// infinite', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onCopy', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
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
                        Span("'text copied successfully!'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span("'copy-clipboard-example'", cls='s1'),
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
    P('Next step is to create a new instance of a CopyClipboard object using the parameters we have set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('CopyClipboard', cls='nx'),
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
                        Span('* $triggerEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions: optional', cls='cm'),
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
                        Span('clipboard', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('CopyClipboard', cls='nx'),
                        Span('(', cls='p'),
                        Span('$triggerEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('$targetEl', cls='nx'),
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
    P('Set the event listeners on the button to copy the text from the input field:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('$triggerEl', cls='nx'),
                        Span('.', cls='p'),
                        Span('addEventListener', cls='nx'),
                        Span('(', cls='p'),
                        Span("'click'", cls='s1'),
                        Span(',', cls='p'),
                        Span('()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('clipboard', cls='nx'),
                        Span('.', cls='p'),
                        Span('copy', cls='nx'),
                        Span('();', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
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
    P('Now you can programmatically call the methods of the CopyClipboard component:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// get the value, inner HTML or text content of the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('clipboard', cls='nx'),
                        Span('.', cls='p'),
                        Span('getTargetValue', cls='nx'),
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
                        Span('// copy the target element text value', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('clipboard', cls='nx'),
                        Span('.', cls='p'),
                        Span('copy', cls='nx'),
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
                        Span('// update the on copy function callback', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('clipboard', cls='nx'),
                        Span('.', cls='p'),
                        Span('updateOnCopyCallback', cls='nx'),
                        Span('(()', cls='p'),
                        Span('=>', cls='p'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('// do something when the text has been copied to the clipboard', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('console', cls='nx'),
                        Span('.', cls='p'),
                        Span('log', cls='nx'),
                        Span('(', cls='p'),
                        Span("'updated on copy callback success message'", cls='s1'),
                        Span(');', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('});', cls='p'),
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
    P('Here is an example of the HTML markup that you can use for the JavaScript example above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"grid grid-cols-8 gap-2 w-full max-w-[23rem]"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('label', cls='nt'),
                        Span('for', cls='na'),
                        Span('=', cls='o'),
                        Span('"copy-text"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"sr-only"', cls='s'),
                        Span('>', cls='p'),
                        'Label',
                        Span('</', cls='p'),
                        Span('label', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('input', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"copy-text"', cls='s'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"text"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"col-span-6 bg-gray-50 border border-gray-300 text-gray-500 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-primary-500 dark:focus:border-primary-500"', cls='s'),
                        Span('value', cls='na'),
                        Span('=', cls='o'),
                        Span('"npm install flowbite"', cls='s'),
                        Span('disabled', cls='na'),
                        Span('readonly', cls='na'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"copy-clipboard-button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"col-span-2 text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm w-full sm:w-auto py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 items-center inline-flex justify-center"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"default-message"', cls='s'),
                        Span('>', cls='p'),
                        'Copy',
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
                        Span('span', cls='nt'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"success-message"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"hidden inline-flex items-center"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"w-3 h-3 text-white me-1.5"', cls='s'),
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"none"', cls='s'),
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 16 12"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        Span('stroke', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        Span('stroke-linecap', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        Span('stroke-linejoin', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        Span('stroke-width', cls='na'),
                        Span('=', cls='o'),
                        Span('"2"', cls='s'),
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"M1 5.917 5.724 10.5 15 1.5"', cls='s'),
                        Span('/>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('svg', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Copied!', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('span', cls='nt'),
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
        'from Flowbite then you can import the types for the CopyClipboard object, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('CopyClipboard', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
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
                        Span('CopyClipboardOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('CopyClipboardInterface', cls='nx'),
                        Span('}', cls='p'),
                        Span('from', cls='nx'),
                        Span("'flowbite'", cls='s1'),
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
                        Span('// set the trigger element which will be clicked (ie. a button or text)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$triggerEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'copy-clipboard-button'", cls='s1'),
                        Span(')', cls='p'),
                        Span('as', cls='nx'),
                        Span('HTMLElement', cls='nx'),
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
                        Span('// set the target element where the text will be copied from (ie. input field, code block)', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$targetEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLInputElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'copy-text'", cls='s1'),
                        Span(')', cls='p'),
                        Span('as', cls='nx'),
                        Span('HTMLInputElement', cls='nx'),
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
                        Span('// optional options with default values and callback functions', cls='c1'),
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
                        Span('CopyClipboardOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('contentType', cls='nx'),
                        Span(':', cls='o'),
                        Span("'input'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('htmlEntities', cls='nx'),
                        Span(':', cls='o'),
                        Span('false', cls='kc'),
                        Span(',', cls='p'),
                        Span('// infinite', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onCopy', cls='nx'),
                        Span(':', cls='o'),
                        Span('()', cls='p'),
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
                        Span("'text copied successfully!'", cls='s1'),
                        Span(');', cls='p'),
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
                        Span("'copy-clipboard-example'", cls='s1'),
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
                        Span('* $triggerEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* options: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* instanceOptions: optional', cls='cm'),
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
                        Span('clipboard', cls='nx'),
                        Span(':', cls='o'),
                        Span('CopyClipboardInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('CopyClipboard', cls='nx'),
                        Span('(', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$triggerEl', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$targetEl', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('options', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('instanceOptions', cls='nx'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
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
                        Span('// copy the value of the target element', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('clipboard', cls='nx'),
                        Span('.', cls='p'),
                        Span('copy', cls='nx'),
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
