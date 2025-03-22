from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P('The number input component from Flowbite can be used to introduce numeric values inside a form such as for a quantity field, a ZIP code, a phone number, your credit card number, and more. All of the UI components are coded exclusively with Tailwind CSS.'),
    P(
        'The examples on this page have basic functionality coded with JavaScript and the quantity input has a more advanced ability to increment and decrement the value with the help of the',
        Code('data-input-counter'),
        'attribute from the Flowbite JS API.'
    ),
    H2(
        'Default number input',
        Span(id='default-number-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default number input', href='#default-number-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this component to set a number value inside a form field by applying the',
        Code('type="number"'),
        'attribute.'
    ),
    component_showcase(Div(
    Form(
        Label('Select a number:', fr='number-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='number', id='number-input', aria_describedby='helper-text-explanation', placeholder='90210', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('Select a number:', fr='number-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='number', id='number-input', aria_describedby='helper-text-explanation', placeholder='90210', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'ZIP code input',
        Span(id='zip-code-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: ZIP code input', href='#zip-code-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example with an icon and helper text to set a ZIP code value inside a form field by also applying the',
        Code('pattern'),
        'attribute to validate the input using a regular expression for a 5 digit number.'
    ),
    component_showcase(Div(
    Form(
        Label('ZIP code:', fr='zip-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 16 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='text', id='zip-input', aria_describedby='helper-text-explanation', placeholder='12345 or 12345-6789', pattern='^\\d{5}(-\\d{4})?$', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('ZIP code:', fr='zip-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(d='M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 16 20',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='text', id='zip-input', aria_describedby='helper-text-explanation', placeholder='12345 or 12345-6789', pattern='^\\d{5}(-\\d{4})?$', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Phone number',
        Span(id='phone-number', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Phone number', href='#phone-number', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this example to set a phone number inside a form field based on the',
        Code('type="phone"'),
        'attribute and a dropdown menu to select the country code.'
    ),
    component_showcase(Div(
    Form(
        Div(
            Button(
                '+1',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-phone-button',
                data_dropdown_toggle='dropdown-phone',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                'United States (+1)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.667V4.8l8.364-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.043-1.548 6.613-4.46H0V5.166h4.672L-1.941.706-.898-.842z', clip_rule='evenodd'),
                                        Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.067 4.933L21.933-.9M14.009 10.088l7.947 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.189 6.093'),
                                        Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'United Kingdom (+44)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                'Australia (+61)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                'Germany (+49)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                    Mask(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#F44653', d='M13.067.5H19.6v14h-6.533z'),
                                        Path(fill='#1035BB', fill_rule='evenodd', d='M0 14.5h6.533V.5H0v14z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='w-4 h-4 me-2'
                                ),
                                'France (+33)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                'Germany (+49)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-phone-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-phone',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-52 dark:bg-gray-700'
            ),
            Label('Phone number:', fr='phone-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Div(
                Input(type='phone', id='phone-input', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center'
        ),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Button(
                '+1',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-phone-button',
                data_dropdown_toggle='dropdown-phone',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                'United States (+1)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.667V4.8l8.364-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.043-1.548 6.613-4.46H0V5.166h4.672L-1.941.706-.898-.842z', clip_rule='evenodd'),
                                        Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.067 4.933L21.933-.9M14.009 10.088l7.947 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.189 6.093'),
                                        Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'United Kingdom (+44)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                'Australia (+61)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#262626', fill_rule='evenodd', d='M0 5.167h19.6V.5H0v4.667z', clip_rule='evenodd'),
                                        G(
                                            Path(fill='#F01515', fill_rule='evenodd', d='M0 9.833h19.6V5.167H0v4.666z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_374_135180)'
                                        ),
                                        G(
                                            Path(fill='#FFD521', fill_rule='evenodd', d='M0 14.5h19.6V9.833H0V14.5z', clip_rule='evenodd'),
                                            filter='url(#filter1_d_374_135180)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_374_135180'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_374_135180', result='shape'),
                                            id='filter0_d_374_135180',
                                            width='19.6',
                                            height='4.667',
                                            x='0',
                                            y='5.167',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_374_135180'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_374_135180', result='shape'),
                                            id='filter1_d_374_135180',
                                            width='19.6',
                                            height='4.667',
                                            x='0',
                                            y='9.833',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='w-4 h-4 me-2'
                                ),
                                'Germany (+49)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                    Mask(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#F44653', d='M13.067.5H19.6v14h-6.533z'),
                                        Path(fill='#1035BB', fill_rule='evenodd', d='M0 14.5h6.533V.5H0v14z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='w-4 h-4 me-2'
                                ),
                                'France (+33)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#262626', fill_rule='evenodd', d='M0 5.167h19.6V.5H0v4.667z', clip_rule='evenodd'),
                                        G(
                                            Path(fill='#F01515', fill_rule='evenodd', d='M0 9.833h19.6V5.167H0v4.666z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_374_135180)'
                                        ),
                                        G(
                                            Path(fill='#FFD521', fill_rule='evenodd', d='M0 14.5h19.6V9.833H0V14.5z', clip_rule='evenodd'),
                                            filter='url(#filter1_d_374_135180)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_374_135180'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_374_135180', result='shape'),
                                            id='filter0_d_374_135180',
                                            width='19.6',
                                            height='4.667',
                                            x='0',
                                            y='5.167',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_374_135180'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_374_135180', result='shape'),
                                            id='filter1_d_374_135180',
                                            width='19.6',
                                            height='4.667',
                                            x='0',
                                            y='9.833',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    cls='w-4 h-4 me-2'
                                ),
                                'Germany (+49)',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-phone-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-phone',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-52 dark:bg-gray-700'
            ),
            Label('Phone number:', fr='phone-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Div(
                Input(type='phone', id='phone-input', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center'
        ),
        cls='max-w-sm mx-auto'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Control buttons',
        Span(id='control-buttons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Control buttons', href='#control-buttons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example with control buttons to increment and decrement the value inside the input field.'),
    P(
        'If you have the',
        A('Flowbite JS', href='https://flowbite.com/docs/getting-started/quickstart/'),
        'installed in your project then you can use the',
        Code('data-input-counter'),
        'data attribute to initialize the target input field and then use the following data attributes to target the buttons that will increment and decrement the value of the input field:'
    ),
    Ul(
        Li(
            Code('data-input-counter'),
            '- initialize the input field'
        ),
        Li(
            Code('data-input-counter-increment'),
            '- increment the value of the input field'
        ),
        Li(
            Code('data-input-counter-decrement'),
            '- decrement the value of the input field'
        )
    ),
    component_showcase(Div(
    Form(
        Label('Choose quantity:', fr='quantity-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='quantity-input', data_input_counter=True, aria_describedby='helper-text-explanation', placeholder='999', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[8rem]'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Label('Choose quantity:', fr='quantity-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='quantity-input', data_input_counter=True, aria_describedby='helper-text-explanation', placeholder='999', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[8rem]'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Control buttons with icon',
        Span(id='control-buttons-with-icon', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Control buttons with icon', href='#control-buttons-with-icon', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to also add an icon inside the input field to improve the user experience.'),
    component_showcase(Div(
    Form(
        Label('Choose quantity:', fr='bedrooms-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='bedrooms-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', aria_describedby='helper-text-explanation', placeholder=True, value='3', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 8v10a1 1 0 0 0 1 1h4v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5h4a1 1 0 0 0 1-1V8M1 10l9-9 9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Bedrooms'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[11rem]'
        ),
        P('Please select the number of bedrooms.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Label('Choose quantity:', fr='bedrooms-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='bedrooms-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', aria_describedby='helper-text-explanation', placeholder=True, value='3', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 8v10a1 1 0 0 0 1 1h4v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5h4a1 1 0 0 0 1-1V8M1 10l9-9 9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Bedrooms'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[11rem]'
        ),
        P('Please select the number of bedrooms.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Counter input',
        Span(id='counter-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Counter input', href='#counter-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example as an alternative style to the control buttons example above.'),
    component_showcase(Div(
    Form(
        Label('Choose quantity:', fr='counter-input', cls='block mb-1 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='counter-input',
                cls='shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='counter-input', data_input_counter=True, placeholder=True, value='12', required=True, cls='shrink-0 text-gray-900 dark:text-white border-0 bg-transparent text-sm font-normal focus:outline-none focus:ring-0 max-w-[2.5rem] text-center'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='counter-input',
                cls='shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center'
        ),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Label('Choose quantity:', fr='counter-input', cls='block mb-1 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='counter-input',
                cls='shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='counter-input', data_input_counter=True, placeholder=True, value='12', required=True, cls='shrink-0 text-gray-900 dark:text-white border-0 bg-transparent text-sm font-normal focus:outline-none focus:ring-0 max-w-[2.5rem] text-center'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-2.5 h-2.5 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='counter-input',
                cls='shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center'
        ),
        cls='max-w-xs mx-auto'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Currency input',
        Span(id='currency-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Currency input', href='#currency-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This component can be used to set a currency value inside a form field when you need to set a price.'),
    component_showcase(Div(
    Form(
        Label('Your Email', fr='currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 2a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1M2 5h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm8 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='number', id='currency-input', placeholder='Enter amount', required=True, cls='block p-2.5 w-full z-20 ps-10 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
            cls='relative w-full'
        ),
        Button(
            'USD',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 10 6',
                cls='w-2.5 h-2.5 ms-2.5'
            ),
            id='dropdown-currency-button',
            data_dropdown_toggle='dropdown-currency',
            type='button',
            cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
        ),
        Div(
            Ul(
                Li(
                    Button(
                        Div(
                            'USD',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                Mask(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                    Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'EUR',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                Mask(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(d='M14 .5h5.6v14H14z'),
                                    Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                    fill='#FF3131',
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'CAD',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                Mask(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                    Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                    Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                    Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'GBP',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                aria_labelledby='dropdown-currency-button',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdown-currency',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
        ),
        cls='max-w-[18rem] mx-auto flex'
    )
), code="""Div(
    Form(
        Label('Your Email', fr='currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M5 2a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1M2 5h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm8 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 16',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='number', id='currency-input', placeholder='Enter amount', required=True, cls='block p-2.5 w-full z-20 ps-10 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
            cls='relative w-full'
        ),
        Button(
            'USD',
            Svg(
                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='none',
                viewbox='0 0 10 6',
                cls='w-2.5 h-2.5 ms-2.5'
            ),
            id='dropdown-currency-button',
            data_dropdown_toggle='dropdown-currency',
            type='button',
            cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
        ),
        Div(
            Ul(
                Li(
                    Button(
                        Div(
                            'USD',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                Mask(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                    Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'EUR',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                Mask(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(d='M14 .5h5.6v14H14z'),
                                    Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                    fill='#FF3131',
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'CAD',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                Li(
                    Button(
                        Div(
                            Svg(
                                Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                Mask(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    id='a',
                                    style='mask-type:luminance',
                                    width='20',
                                    height='15',
                                    x='0',
                                    y='0',
                                    maskunits='userSpaceOnUse'
                                ),
                                G(
                                    Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                    Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                    Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                    Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                    mask='url(#a)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 15',
                                cls='h-4 w-4 me-2'
                            ),
                            'GBP',
                            cls='inline-flex items-center'
                        ),
                        type='button',
                        role='menuitem',
                        cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                    )
                ),
                aria_labelledby='dropdown-currency-button',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdown-currency',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
        ),
        cls='max-w-[18rem] mx-auto flex'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Credit card input',
        Span(id='credit-card-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Credit card input', href='#credit-card-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this component to set the information needed when making an online transaction with a credit card by adding the card number, expiration date, and security code. The component uses the',
        A('Flowbite Datepicker', href='https://flowbite.com/docs/components/datepicker/'),
        '.'
    ),
    component_showcase(Div(
    Form(
        Label('Card number:', fr='card-number-input', cls='sr-only'),
        Div(
            Input(type='text', id='card-number-input', placeholder='4242 4242 4242 4242', pattern='^4[0-9]{12}(?:[0-9]{3})?$', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full pe-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(fill='currentColor', d='M23.315 4.773c-2.542 0-4.813 1.3-4.813 3.705 0 2.756 4.028 2.947 4.028 4.332 0 .583-.676 1.105-1.832 1.105-1.64 0-2.866-.73-2.866-.73l-.524 2.426s1.412.616 3.286.616c2.78 0 4.966-1.365 4.966-3.81 0-2.913-4.045-3.097-4.045-4.383 0-.457.555-.957 1.708-.957 1.3 0 2.36.53 2.36.53l.514-2.343s-1.154-.491-2.782-.491zM.062 4.95L0 5.303s1.07.193 2.032.579c1.24.442 1.329.7 1.537 1.499l2.276 8.664h3.05l4.7-11.095h-3.043l-3.02 7.543L6.3 6.1c-.113-.732-.686-1.15-1.386-1.15H.062zm14.757 0l-2.387 11.095h2.902l2.38-11.096h-2.895zm16.187 0c-.7 0-1.07.37-1.342 1.016L25.41 16.045h3.044l.589-1.68h3.708l.358 1.68h2.685L33.453 4.95h-2.447zm.396 2.997l.902 4.164h-2.417l1.515-4.164z'),
                    fill='none',
                    viewbox='0 0 36 21',
                    cls='h-6 text-[#1434CB] dark:text-white'
                ),
                cls='absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none'
            ),
            cls='relative'
        ),
        Div(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                    ),
                    cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
                ),
                Label('Card expiration date:', fr='card-expiration-input', cls='sr-only'),
                Input(datepicker=True, datepicker_format='mm/yy', id='card-expiration-input', type='text', placeholder='12/23', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative max-w-sm col-span-2'
            ),
            Div(
                Label('Card CVV code:', fr='cvv-input', cls='sr-only'),
                Input(type='number', id='cvv-input', aria_describedby='helper-text-explanation', placeholder='CVV', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='col-span-1'
            ),
            cls='grid grid-cols-3 gap-4 my-4'
        ),
        Button('Pay now', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('Card number:', fr='card-number-input', cls='sr-only'),
        Div(
            Input(type='text', id='card-number-input', placeholder='4242 4242 4242 4242', pattern='^4[0-9]{12}(?:[0-9]{3})?$', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full pe-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(fill='currentColor', d='M23.315 4.773c-2.542 0-4.813 1.3-4.813 3.705 0 2.756 4.028 2.947 4.028 4.332 0 .583-.676 1.105-1.832 1.105-1.64 0-2.866-.73-2.866-.73l-.524 2.426s1.412.616 3.286.616c2.78 0 4.966-1.365 4.966-3.81 0-2.913-4.045-3.097-4.045-4.383 0-.457.555-.957 1.708-.957 1.3 0 2.36.53 2.36.53l.514-2.343s-1.154-.491-2.782-.491zM.062 4.95L0 5.303s1.07.193 2.032.579c1.24.442 1.329.7 1.537 1.499l2.276 8.664h3.05l4.7-11.095h-3.043l-3.02 7.543L6.3 6.1c-.113-.732-.686-1.15-1.386-1.15H.062zm14.757 0l-2.387 11.095h2.902l2.38-11.096h-2.895zm16.187 0c-.7 0-1.07.37-1.342 1.016L25.41 16.045h3.044l.589-1.68h3.708l.358 1.68h2.685L33.453 4.95h-2.447zm.396 2.997l.902 4.164h-2.417l1.515-4.164z'),
                    fill='none',
                    viewbox='0 0 36 21',
                    cls='h-6 text-[#1434CB] dark:text-white'
                ),
                cls='absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none'
            ),
            cls='relative'
        ),
        Div(
            Div(
                Div(
                    Svg(
                        Path(d='M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 20 20',
                        cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                    ),
                    cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none'
                ),
                Label('Card expiration date:', fr='card-expiration-input', cls='sr-only'),
                Input(datepicker=True, datepicker_format='mm/yy', id='card-expiration-input', type='text', placeholder='12/23', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='relative max-w-sm col-span-2'
            ),
            Div(
                Label('Card CVV code:', fr='cvv-input', cls='sr-only'),
                Input(type='number', id='cvv-input', aria_describedby='helper-text-explanation', placeholder='CVV', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                cls='col-span-1'
            ),
            cls='grid grid-cols-3 gap-4 my-4'
        ),
        Button('Pay now', type='submit', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Pin code input',
        Span(id='pin-code-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pin code input', href='#pin-code-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a pin code input to set a 6 digit code. This can be used when setting up a new account or when making a payment and the code is sent via phone or email.'),
    component_showcase(Div(
    Form(
        Div(
            Div(
                Label('First code', fr='code-1', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_next='code-2', id='code-1', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Second code', fr='code-2', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-1', data_focus_input_next='code-3', id='code-2', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Third code', fr='code-3', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-2', data_focus_input_next='code-4', id='code-3', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Fourth code', fr='code-4', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-3', data_focus_input_next='code-5', id='code-4', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Fifth code', fr='code-5', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-4', data_focus_input_next='code-6', id='code-5', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Sixth code', fr='code-6', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-5', id='code-6', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='flex mb-2 space-x-2 rtl:space-x-reverse'
        ),
        P('Please introduce the 6 digit code we sent via email.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Div(
                Label('First code', fr='code-1', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_next='code-2', id='code-1', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Second code', fr='code-2', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-1', data_focus_input_next='code-3', id='code-2', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Third code', fr='code-3', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-2', data_focus_input_next='code-4', id='code-3', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Fourth code', fr='code-4', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-3', data_focus_input_next='code-5', id='code-4', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Fifth code', fr='code-5', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-4', data_focus_input_next='code-6', id='code-5', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            Div(
                Label('Sixth code', fr='code-6', cls='sr-only'),
                Input(type='text', maxlength='1', data_focus_input_init=True, data_focus_input_prev='code-5', id='code-6', required=True, cls='block w-9 h-9 py-3 text-sm font-extrabold text-center text-gray-900 bg-white border border-gray-300 rounded-lg focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
            ),
            cls='flex mb-2 space-x-2 rtl:space-x-reverse'
        ),
        P('Please introduce the 6 digit code we sent via email.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Number input with slider',
        Span(id='number-input-with-slider', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Number input with slider', href='#number-input-with-slider', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to set the value of a number input field by sliding the range slider component or by typing the value in the input field. The component uses the',
        A('Flowbite Range Slider', href='https://flowbite.com/docs/components/range-slider/'),
        '.'
    ),
    component_showcase(Div(
    Form(
        Div(
            Button(
                'USD',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-currency-button',
                data_dropdown_toggle='dropdown-currency',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                'USD',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'EUR',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                    Mask(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(d='M14 .5h5.6v14H14z'),
                                        Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                        fill='#FF3131',
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'CAD',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                        Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                        Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'GBP',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-currency-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-currency',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            Label('Your Email', fr='currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Div(
                Input(type='number', id='currency-input', placeholder='Enter amount', value='1000', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex mb-4'
        ),
        Div(
            Label('Default range', fr='price-range-input', cls='sr-only'),
            Input(id='price-range-input', type='range', value='1000', min='100', max='1500', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
            Span('Min ($100)', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6'),
            Span('$500', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
            Span('$1000', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
            Span('Max ($1500)', cls='text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6'),
            cls='relative'
        ),
        cls='max-w-[24rem] mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Button(
                'USD',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-currency-button',
                data_dropdown_toggle='dropdown-currency',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button(
                            Div(
                                'USD',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'EUR',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                    Mask(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(d='M14 .5h5.6v14H14z'),
                                        Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                        fill='#FF3131',
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'CAD',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    Li(
                        Button(
                            Div(
                                Svg(
                                    Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                    Mask(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        id='a',
                                        style='mask-type:luminance',
                                        width='20',
                                        height='15',
                                        x='0',
                                        y='0',
                                        maskunits='userSpaceOnUse'
                                    ),
                                    G(
                                        Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                        Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                        Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
                                'GBP',
                                cls='inline-flex items-center'
                            ),
                            type='button',
                            role='menuitem',
                            cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                        )
                    ),
                    aria_labelledby='dropdown-currency-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-currency',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            Label('Your Email', fr='currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
            Div(
                Input(type='number', id='currency-input', placeholder='Enter amount', value='1000', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-gray-50 border-s-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex mb-4'
        ),
        Div(
            Label('Default range', fr='price-range-input', cls='sr-only'),
            Input(id='price-range-input', type='range', value='1000', min='100', max='1500', cls='w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700'),
            Span('Min ($100)', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6'),
            Span('$500', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-1/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
            Span('$1000', cls='text-sm text-gray-500 dark:text-gray-400 absolute start-2/3 -translate-x-1/2 rtl:translate-x-1/2 -bottom-6'),
            Span('Max ($1500)', cls='text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6'),
            cls='relative'
        ),
        cls='max-w-[24rem] mx-auto'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Convert currency',
        Span(id='convert-currency', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Convert currency', href='#convert-currency', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of two number input fields and dropdowns to convert currency and even from fiat to crypto.'),
    component_showcase(Div(
    Form(
        Div(
            Div(
                Label('Your Email', fr='fiat-currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                Div(
                    Input(type='number', id='fiat-currency-input', placeholder='421 USD', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                    cls='relative w-full'
                ),
                Button(
                    'USD',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdown-fiat-currency-button',
                    data_dropdown_toggle='dropdown-fiat-currency',
                    type='button',
                    cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
                ),
                Div(
                    Ul(
                        Li(
                            Button(
                                Div(
                                    'USD',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        Mask(
                                            Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                            Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'EUR',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                        Mask(
                                            Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(d='M14 .5h5.6v14H14z'),
                                            Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                            fill='#FF3131',
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'CAD',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        Mask(
                                            Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                            Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                            Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                            Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'GBP',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        aria_labelledby='dropdown-fiat-currency-button',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdown-fiat-currency',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
                ),
                cls='flex'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M11 10H1m0 0 3-3m-3 3 3 3m1-9h10m0 0-3 3m3-3-3-3'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 14',
                    cls='w-4 h-4'
                ),
                Span('Convert currency', cls='sr-only'),
                type='button',
                cls='p-3 text-sm font-medium text-gray-500 focus:outline-none bg-gray-100 rounded-lg hover:bg-gray-200 hover:text-gray-900 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Div(
                Label('Your Email', fr='crypto-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                Div(
                    Input(type='number', id='crypto-input', placeholder='0.323 BTC', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                    cls='relative w-full'
                ),
                Button(
                    Svg(
                        Path(fill='#F7931A', d='M14.83 9.204A7.04 7.04 0 111.17 5.797a7.04 7.04 0 0113.66 3.407z'),
                        Path(fill='#fff', d='M11.104 6.498c.14-.937-.573-1.44-1.548-1.777l.316-1.269-.773-.192-.308 1.235c-.203-.05-.411-.098-.619-.145l.31-1.244-.771-.193-.317 1.269a25.752 25.752 0 01-.493-.116v-.004l-1.065-.266-.205.825s.573.132.56.14c.314.078.37.285.36.449l-.36 1.446c.022.005.05.013.08.025l-.08-.02-.506 2.026c-.038.095-.135.237-.354.183.008.011-.562-.14-.562-.14l-.383.884 1.005.251c.187.047.37.096.55.142l-.319 1.284.772.192.317-1.27c.21.058.415.11.615.16l-.315 1.264.772.193.32-1.281c1.317.249 2.308.148 2.724-1.043.336-.96-.016-1.513-.71-1.874.505-.116.886-.448.987-1.134zM9.34 8.973c-.239.96-1.854.44-2.378.31l.424-1.7c.524.13 2.203.39 1.954 1.39zm.239-2.49c-.218.874-1.562.43-1.999.321l.385-1.542c.436.109 1.84.312 1.614 1.222z'),
                        fill='none',
                        viewbox='0 0 16 15',
                        cls='h-4 w-4 me-2'
                    ),
                    'BTC',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdown-crypto-button',
                    data_dropdown_toggle='dropdown-crypto',
                    type='button',
                    cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
                ),
                Div(
                    Ul(
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#F7931A', d='M14.83 9.204A7.04 7.04 0 111.17 5.797a7.04 7.04 0 0113.66 3.407z'),
                                        Path(fill='#fff', d='M11.104 6.498c.14-.937-.573-1.44-1.548-1.777l.316-1.269-.773-.192-.308 1.235c-.203-.05-.411-.098-.619-.145l.31-1.244-.771-.193-.317 1.269a25.752 25.752 0 01-.493-.116v-.004l-1.065-.266-.205.825s.573.132.56.14c.314.078.37.285.36.449l-.36 1.446c.022.005.05.013.08.025l-.08-.02-.506 2.026c-.038.095-.135.237-.354.183.008.011-.562-.14-.562-.14l-.383.884 1.005.251c.187.047.37.096.55.142l-.319 1.284.772.192.317-1.27c.21.058.415.11.615.16l-.315 1.264.772.193.32-1.281c1.317.249 2.308.148 2.724-1.043.336-.96-.016-1.513-.71-1.874.505-.116.886-.448.987-1.134zM9.34 8.973c-.239.96-1.854.44-2.378.31l.424-1.7c.524.13 2.203.39 1.954 1.39zm.239-2.49c-.218.874-1.562.43-1.999.321l.385-1.542c.436.109 1.84.312 1.614 1.222z'),
                                        fill='none',
                                        viewbox='0 0 16 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'BTC',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#343434', d='M5 .5l-.11.364v10.582l.11.105 4.91-2.902L5 .5z'),
                                        Path(fill='#8C8C8C', d='M5 .5L.086 8.65 5 11.55V.5z'),
                                        Path(fill='#3C3C3B', d='M5 12.48l-.061.075v3.77L5 16.5l4.914-6.922L5 12.48z'),
                                        Path(fill='#8C8C8C', d='M5 16.5v-4.02L.086 9.578 5 16.5z'),
                                        Path(fill='#141414', d='M5 11.55L9.91 8.65 5 6.418v5.133z'),
                                        Path(fill='#393939', d='M.086 8.649L5 11.551V6.418L.086 8.649z'),
                                        fill='none',
                                        viewbox='0 0 10 17',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'ETH',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#C2A633', d='M16 8.5a8 8 0 11-16 0 8 8 0 0116 0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M5.355 12.685h2.761S12 13.015 12 8.567c0-4.275-3.546-4.26-4.232-4.257H5.355v3.73H4.38v.914h.974v3.73zM6.91 5.858H8c.407 0 2.458.167 2.461 2.74.003 2.542-2.064 2.54-2.396 2.539H6.91V8.954h1.715v-.913H6.91V5.858z', clip_rule='evenodd'),
                                        fill='none',
                                        viewbox='0 0 16 17',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'DOGE',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    'SOL',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        aria_labelledby='dropdown-crypto-button',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdown-crypto',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
                ),
                cls='flex'
            ),
            cls='space-x-0 space-y-4 sm:space-y-0 sm:space-x-4 rtl:space-x-reverse flex items-center flex-col sm:flex-row mb-4'
        ),
        Div(
            P('Last update: 20:45 AM, November 20, 2023', cls='text-sm text-gray-500 dark:text-gray-400'),
            Button(
                'Refresh',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-3 h-3 ms-1.5'
                ),
                type='reset',
                cls='text-sm text-primary-700 dark:text-primary-500 inline-flex items-center font-medium hover:underline'
            ),
            cls='flex justify-between items-center flex-col sm:flex-row space-y-2 sm:space-y-0'
        ),
        cls='max-w-xl mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Div(
                Label('Your Email', fr='fiat-currency-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                Div(
                    Input(type='number', id='fiat-currency-input', placeholder='421 USD', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                    cls='relative w-full'
                ),
                Button(
                    'USD',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdown-fiat-currency-button',
                    data_dropdown_toggle='dropdown-fiat-currency',
                    type='button',
                    cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
                ),
                Div(
                    Ul(
                        Li(
                            Button(
                                Div(
                                    'USD',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        Mask(
                                            Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(fill='#043CAE', d='M0 .5h19.6v14H0z'),
                                            Path(fill='#FFD429', fill_rule='evenodd', d='M9.14 3.493L9.8 3.3l.66.193-.193-.66.193-.66-.66.194-.66-.194.193.66-.193.66zm0 9.334l.66-.194.66.194-.193-.66.193-.66-.66.193-.66-.193.193.66-.193.66zm5.327-4.86l-.66.193L14 7.5l-.193-.66.66.193.66-.193-.194.66.194.66-.66-.193zm-9.994.193l.66-.193.66.193L5.6 7.5l.193-.66-.66.193-.66-.193.194.66-.194.66zm9.369-2.527l-.66.194.193-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm-8.743 4.86l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.194.193.66-.193.66zm7.034-6.568l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326 8.276l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66zM13.84 10.3l-.66.193.194-.66-.194-.66.66.194.66-.194-.193.66.193.66-.66-.193zM5.1 5.827l.66-.194.66.194-.194-.66.194-.66-.66.193-.66-.193.193.66-.193.66zm7.034 6.181l-.66.193.194-.66-.194-.66.66.194.66-.193-.193.66.193.66-.66-.194zm-5.326-7.89l.66-.193.66.193-.194-.66.194-.66-.66.194-.66-.193.193.66-.193.66z', clip_rule='evenodd'),
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'EUR',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#F5F5F5', stroke_width='.5', rx='1.75'),
                                        Mask(
                                            Rect(width='19.1', height='13.5', x='.25', y='.75', fill='#fff', stroke='#fff', stroke_width='.5', rx='1.75'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(d='M14 .5h5.6v14H14z'),
                                            Path(fill_rule='evenodd', d='M0 14.5h5.6V.5H0v14zM11.45 6.784a.307.307 0 01-.518-.277l.268-1.34-.933.466-.467-1.4-.467 1.4-.933-.466.268 1.34a.307.307 0 01-.518.277.307.307 0 00-.434 0l-.25.25-.933-.467L7 7.5l-.231.231a.333.333 0 000 .471l1.164 1.165h1.4l.234 1.4h.466l.234-1.4h1.4l1.164-1.165a.333.333 0 000-.471l-.231-.23.467-.934-.934.466-.25-.25a.307.307 0 00-.433 0z', clip_rule='evenodd'),
                                            fill='#FF3131',
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'CAD',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                        Mask(
                                            Rect(width='19.6', height='14', y='.5', fill='#fff', rx='2'),
                                            id='a',
                                            style='mask-type:luminance',
                                            width='20',
                                            height='15',
                                            x='0',
                                            y='0',
                                            maskunits='userSpaceOnUse'
                                        ),
                                        G(
                                            Path(fill='#0A17A7', d='M0 .5h19.6v14H0z'),
                                            Path(fill='#fff', fill_rule='evenodd', d='M-.898-.842L7.467 4.8V-.433h4.666V4.8l8.365-5.642L21.542.706l-6.614 4.46H19.6v4.667h-4.672l6.614 4.46-1.044 1.549-8.365-5.642v5.233H7.467V10.2l-8.365 5.642-1.044-1.548 6.614-4.46H0V5.166h4.672L-1.942.706-.898-.842z', clip_rule='evenodd'),
                                            Path(stroke='#DB1F35', stroke_linecap='round', stroke_width='.667', d='M13.068 4.933L21.933-.9M14.009 10.088l7.948 5.357M5.604 4.917L-2.686-.67M6.503 10.024l-9.19 6.093'),
                                            Path(fill='#E6273E', fill_rule='evenodd', d='M0 8.9h8.4v5.6h2.8V8.9h8.4V6.1h-8.4V.5H8.4v5.6H0v2.8z', clip_rule='evenodd'),
                                            mask='url(#a)'
                                        ),
                                        fill='none',
                                        aria_hidden='true',
                                        viewbox='0 0 20 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'GBP',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        aria_labelledby='dropdown-fiat-currency-button',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdown-fiat-currency',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
                ),
                cls='flex'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M11 10H1m0 0 3-3m-3 3 3 3m1-9h10m0 0-3 3m3-3-3-3'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 16 14',
                    cls='w-4 h-4'
                ),
                Span('Convert currency', cls='sr-only'),
                type='button',
                cls='p-3 text-sm font-medium text-gray-500 focus:outline-none bg-gray-100 rounded-lg hover:bg-gray-200 hover:text-gray-900 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600'
            ),
            Div(
                Label('Your Email', fr='crypto-input', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                Div(
                    Input(type='number', id='crypto-input', placeholder='0.323 BTC', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-e-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                    cls='relative w-full'
                ),
                Button(
                    Svg(
                        Path(fill='#F7931A', d='M14.83 9.204A7.04 7.04 0 111.17 5.797a7.04 7.04 0 0113.66 3.407z'),
                        Path(fill='#fff', d='M11.104 6.498c.14-.937-.573-1.44-1.548-1.777l.316-1.269-.773-.192-.308 1.235c-.203-.05-.411-.098-.619-.145l.31-1.244-.771-.193-.317 1.269a25.752 25.752 0 01-.493-.116v-.004l-1.065-.266-.205.825s.573.132.56.14c.314.078.37.285.36.449l-.36 1.446c.022.005.05.013.08.025l-.08-.02-.506 2.026c-.038.095-.135.237-.354.183.008.011-.562-.14-.562-.14l-.383.884 1.005.251c.187.047.37.096.55.142l-.319 1.284.772.192.317-1.27c.21.058.415.11.615.16l-.315 1.264.772.193.32-1.281c1.317.249 2.308.148 2.724-1.043.336-.96-.016-1.513-.71-1.874.505-.116.886-.448.987-1.134zM9.34 8.973c-.239.96-1.854.44-2.378.31l.424-1.7c.524.13 2.203.39 1.954 1.39zm.239-2.49c-.218.874-1.562.43-1.999.321l.385-1.542c.436.109 1.84.312 1.614 1.222z'),
                        fill='none',
                        viewbox='0 0 16 15',
                        cls='h-4 w-4 me-2'
                    ),
                    'BTC',
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 10 6',
                        cls='w-2.5 h-2.5 ms-2.5'
                    ),
                    id='dropdown-crypto-button',
                    data_dropdown_toggle='dropdown-crypto',
                    type='button',
                    cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
                ),
                Div(
                    Ul(
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#F7931A', d='M14.83 9.204A7.04 7.04 0 111.17 5.797a7.04 7.04 0 0113.66 3.407z'),
                                        Path(fill='#fff', d='M11.104 6.498c.14-.937-.573-1.44-1.548-1.777l.316-1.269-.773-.192-.308 1.235c-.203-.05-.411-.098-.619-.145l.31-1.244-.771-.193-.317 1.269a25.752 25.752 0 01-.493-.116v-.004l-1.065-.266-.205.825s.573.132.56.14c.314.078.37.285.36.449l-.36 1.446c.022.005.05.013.08.025l-.08-.02-.506 2.026c-.038.095-.135.237-.354.183.008.011-.562-.14-.562-.14l-.383.884 1.005.251c.187.047.37.096.55.142l-.319 1.284.772.192.317-1.27c.21.058.415.11.615.16l-.315 1.264.772.193.32-1.281c1.317.249 2.308.148 2.724-1.043.336-.96-.016-1.513-.71-1.874.505-.116.886-.448.987-1.134zM9.34 8.973c-.239.96-1.854.44-2.378.31l.424-1.7c.524.13 2.203.39 1.954 1.39zm.239-2.49c-.218.874-1.562.43-1.999.321l.385-1.542c.436.109 1.84.312 1.614 1.222z'),
                                        fill='none',
                                        viewbox='0 0 16 15',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'BTC',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#343434', d='M5 .5l-.11.364v10.582l.11.105 4.91-2.902L5 .5z'),
                                        Path(fill='#8C8C8C', d='M5 .5L.086 8.65 5 11.55V.5z'),
                                        Path(fill='#3C3C3B', d='M5 12.48l-.061.075v3.77L5 16.5l4.914-6.922L5 12.48z'),
                                        Path(fill='#8C8C8C', d='M5 16.5v-4.02L.086 9.578 5 16.5z'),
                                        Path(fill='#141414', d='M5 11.55L9.91 8.65 5 6.418v5.133z'),
                                        Path(fill='#393939', d='M.086 8.649L5 11.551V6.418L.086 8.649z'),
                                        fill='none',
                                        viewbox='0 0 10 17',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'ETH',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    Svg(
                                        Path(fill='#C2A633', d='M16 8.5a8 8 0 11-16 0 8 8 0 0116 0z'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M5.355 12.685h2.761S12 13.015 12 8.567c0-4.275-3.546-4.26-4.232-4.257H5.355v3.73H4.38v.914h.974v3.73zM6.91 5.858H8c.407 0 2.458.167 2.461 2.74.003 2.542-2.064 2.54-2.396 2.539H6.91V8.954h1.715v-.913H6.91V5.858z', clip_rule='evenodd'),
                                        fill='none',
                                        viewbox='0 0 16 17',
                                        cls='h-4 w-4 me-2'
                                    ),
                                    'DOGE',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        Li(
                            Button(
                                Div(
                                    'SOL',
                                    cls='inline-flex items-center'
                                ),
                                type='button',
                                role='menuitem',
                                cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white'
                            )
                        ),
                        aria_labelledby='dropdown-crypto-button',
                        cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                    ),
                    id='dropdown-crypto',
                    cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
                ),
                cls='flex'
            ),
            cls='space-x-0 space-y-4 sm:space-y-0 sm:space-x-4 rtl:space-x-reverse flex items-center flex-col sm:flex-row mb-4'
        ),
        Div(
            P('Last update: 20:45 AM, November 20, 2023', cls='text-sm text-gray-500 dark:text-gray-400'),
            Button(
                'Refresh',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M16 1v5h-5M2 19v-5h5m10-4a8 8 0 0 1-14.947 3.97M1 10a8 8 0 0 1 14.947-3.97'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 20',
                    cls='w-3 h-3 ms-1.5'
                ),
                type='reset',
                cls='text-sm text-primary-700 dark:text-primary-500 inline-flex items-center font-medium hover:underline'
            ),
            cls='flex justify-between items-center flex-col sm:flex-row space-y-2 sm:space-y-0'
        ),
        cls='max-w-xl mx-auto'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H2(
        'Advanced control buttons',
        Span(id='advanced-control-buttons', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Advanced control buttons', href='#advanced-control-buttons', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to add multiple number input fields with quantity selectors and control buttons to use for E-commerce UI similar to projects like AirBnb or Booking.'),
    component_showcase(Div(
    Form(
        Label('Choose bedrooms number:', fr='bedrooms-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='bedrooms-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', placeholder=True, value='2', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 8v10a1 1 0 0 0 1 1h4v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5h4a1 1 0 0 0 1-1V8M1 10l9-9 9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Bedrooms'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center mb-2'
        ),
        Label('Choose number of nights:', fr='nights-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='nights-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='nights-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='30', placeholder=True, value='7', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Night stays'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='nights-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center mb-2'
        ),
        Label('Choose guests:', fr='guests-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='guests-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='guests-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', placeholder=True, value='3', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M4.333 6.764a3 3 0 1 1 3.141-5.023M2.5 16H1v-2a4 4 0 0 1 4-4m7.379-8.121a3 3 0 1 1 2.976 5M15 10a4 4 0 0 1 4 4v2h-1.761M13 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm-4 6h2a4 4 0 0 1 4 4v2H5v-2a4 4 0 0 1 4-4Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Guests'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='guests-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center'
        ),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Label('Choose bedrooms number:', fr='bedrooms-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='bedrooms-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', placeholder=True, value='2', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M3 8v10a1 1 0 0 0 1 1h4v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5h4a1 1 0 0 0 1-1V8M1 10l9-9 9 9'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Bedrooms'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='bedrooms-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center mb-2'
        ),
        Label('Choose number of nights:', fr='nights-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='nights-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='nights-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='30', placeholder=True, value='7', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Night stays'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='nights-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center mb-2'
        ),
        Label('Choose guests:', fr='guests-input', cls='sr-only'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='guests-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='guests-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='5', placeholder=True, value='3', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 font-medium text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full pb-6 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M4.333 6.764a3 3 0 1 1 3.141-5.023M2.5 16H1v-2a4 4 0 0 1 4-4m7.379-8.121a3 3 0 1 1 2.976 5M15 10a4 4 0 0 1 4 4v2h-1.761M13 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm-4 6h2a4 4 0 0 1 4 4v2H5v-2a4 4 0 0 1 4-4Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 20',
                    cls='w-2.5 h-2.5 text-gray-400'
                ),
                Span('Guests'),
                cls='absolute bottom-1 start-1/2 -translate-x-1/2 rtl:translate-x-1/2 flex items-center text-xs text-gray-400 space-x-1 rtl:space-x-reverse'
            ),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='guests-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center'
        ),
        cls='max-w-xs mx-auto'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Min and max values',
        Span(id='min-and-max-values', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Min and max values', href='#min-and-max-values', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('By using the InputCounter object from the Flowbite JS API, you ca set the min and max values of a number input component by using the following data attributes:'),
    Ul(
        Li(
            Code('data-input-counter-min'),
            '- set the minimum value of the input'
        ),
        Li(
            Code('data-input-counter-max'),
            '- set the maximum value of the input'
        )
    ),
    P('These values will be enforced and validated whenever the user clicks on one of the buttons or tries to introduce the value manually.'),
    component_showcase(Div(
    Form(
        Label('Choose quantity:', fr='quantity-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='quantity-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='50', aria_describedby='helper-text-explanation', placeholder='999', value='5', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[8rem]'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Label('Choose quantity:', fr='quantity-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 2',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='decrement-button',
                data_input_counter_decrement='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-s-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            Input(type='text', id='quantity-input', data_input_counter=True, data_input_counter_min='1', data_input_counter_max='50', aria_describedby='helper-text-explanation', placeholder='999', value='5', required=True, cls='bg-gray-50 border-x-0 border-gray-300 h-11 text-center text-gray-900 text-sm focus:ring-primary-500 focus:border-primary-500 block w-full py-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            Button(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 1v16M1 9h16'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 18 18',
                    cls='w-3 h-3 text-gray-900 dark:text-white'
                ),
                type='button',
                id='increment-button',
                data_input_counter_increment='quantity-input',
                cls='bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 border border-gray-300 rounded-e-lg p-3 h-11 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none'
            ),
            cls='relative flex items-center max-w-[8rem]'
        ),
        P('Please select a 5 digit number from 0 to 9.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-xs mx-auto'
    )
)""", id="example_12",cls='mt-2 mb-6'),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Strong('InputCounter'),
        'object from the Flowbite JS API to create a number input component with increment and decrement buttons that can be used to increase or decrease the value of the input.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use the object parameters from the InputCounter object to set the target, increment, and decrement elements as well as the options object.'),
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
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Pass the target input field element that will be incremented or decremented based on click event.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('incrementEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass the increment button element that will increase the value of the target element based on click event.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('decrementEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Pass the decrement button element that will decrease the value of the target element based on click event.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Set these options to set the minimum and maximum value of the input field and the callback functions.', cls='px-6 py-4'),
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
    P('Use these optional options for the InputCounter object to set the minimum and maximum values of the input field and also to set callback functions for the increment and decrement events.'),
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
                        Code('minValue', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Integer', cls='px-6 py-4'),
                    Td('Set the minimum value of the input field.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('maxValue', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Integer', cls='px-6 py-4'),
                    Td('Set the maximum value of the input field.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onIncrement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the item has been incremented.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onDecrement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the item has been decremented.', cls='px-6 py-4'),
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
    P('Use the following methods of the InputCounter object to programmatically manipulate the behaviour of the input field.'),
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
                        Code('getCurrentValue()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to get the current value of the input field.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('increment()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method on the InputCounter object to increment the value of the input field.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('decrement()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method on the InputCounter object to decrement the value of the input field.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnIncrement(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function whenever the input field has been incremented.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnDecrement(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4'
                    ),
                    Td('Use this method to set a callback function whenever the input field has been decremented.', cls='px-6 py-4'),
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
    P('Check out the following examples to learn how to create a new InputCounter object and how to set it up with custom options and programmatically use the methods available.'),
    P('First of all, you need to set the object parameters where the target element is required and the other two are optional.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the target element of the input field', cls='c1'),
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
                        Span("'counter-input-example'", cls='s1'),
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
                        Span('// optionally set the increment and decrement elements', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$incrementEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'increment-button'", cls='s1'),
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
                        Span('const', cls='kr'),
                        Span('$decrementEl', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'decrement-button'", cls='s1'),
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
                        Span('minValue', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('maxValue', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        Span('// infinite', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onIncrement', cls='nx'),
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
                        Span("'input field value has been incremented'", cls='s1'),
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
                        Span('onDecrement', cls='nx'),
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
                        Span("'input field value has been decremented'", cls='s1'),
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
                        Span("'counter-input-example'", cls='s1'),
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
    P('Next step is to create a new instance of a InputCounter object using the parameters we have set above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('InputCounter', cls='nx'),
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
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $incrementEl: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $decrementEl: optional', cls='cm'),
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
                        Span('*/', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('const', cls='kr'),
                        Span('counterInput', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('InputCounter', cls='nx'),
                        Span('(', cls='p'),
                        Span('$targetEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('$incrementEl', cls='nx'),
                        Span(',', cls='p'),
                        Span('$decrementEl', cls='nx'),
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
    P('Now you can programmatically increment or decrement the input field using the methods of the InputCounter object.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// get the current value of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('counterInput', cls='nx'),
                        Span('.', cls='p'),
                        Span('getCurrentValue', cls='nx'),
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
                        Span('// increment the value of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('counterInput', cls='nx'),
                        Span('.', cls='p'),
                        Span('increment', cls='nx'),
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
                        Span('// decrement the value of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('counterInput', cls='nx'),
                        Span('.', cls='p'),
                        Span('decrement', cls='nx'),
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
                        Span('form', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"max-w-xs mx-auto"', cls='s'),
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
                        Span('"counter-input-example"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"block mb-1 text-sm font-medium text-gray-900 dark:text-white"', cls='s'),
                        Span('>', cls='p'),
                        'Choose quantity:',
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
                        Span('div', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"relative flex items-center"', cls='s'),
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
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"decrement-button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none"', cls='s'),
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
                        Span('"w-2.5 h-2.5 text-gray-900 dark:text-white"', cls='s'),
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
                        Span('"0 0 18 2"', cls='s'),
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
                        Span('"M1 1h16"', cls='s'),
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
                        Span('<', cls='p'),
                        Span('input', cls='nt'),
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"text"', cls='s'),
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"counter-input-example"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"shrink-0 text-gray-900 dark:text-white border-0 bg-transparent text-sm font-normal focus:outline-none focus:ring-0 max-w-[2.5rem] text-center"', cls='s'),
                        Span('placeholder', cls='na'),
                        Span('=', cls='o'),
                        Span('""', cls='s'),
                        Span('value', cls='na'),
                        Span('=', cls='o'),
                        Span('"12"', cls='s'),
                        Span('required', cls='na'),
                        Span('/>', cls='p'),
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
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"increment-button"', cls='s'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"shrink-0 bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:border-gray-600 hover:bg-gray-200 inline-flex items-center justify-center border border-gray-300 rounded-md h-5 w-5 focus:ring-gray-100 dark:focus:ring-gray-700 focus:ring-2 focus:outline-none"', cls='s'),
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
                        Span('"w-2.5 h-2.5 text-gray-900 dark:text-white"', cls='s'),
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
                        Span('"0 0 18 18"', cls='s'),
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
                        Span('"M9 1v16M1 9h16"', cls='s'),
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
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('form', cls='nt'),
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
        'from Flowbite then you can import the types for the InputCounter object, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('InputCounter', cls='nx'),
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
                        Span('InputCounterOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('InputCounterInterface', cls='nx'),
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
                        Span('// set the target element of the input field', cls='c1'),
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
                        Span("'counter-input-example'", cls='s1'),
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
                        Span('// optionally set the increment and decrement elements', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('const', cls='kr'),
                        Span('$incrementEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'increment-button'", cls='s1'),
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
                        Span('const', cls='kr'),
                        Span('$decrementEl', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('getElementById', cls='nx'),
                        Span('(', cls='p'),
                        Span("'decrement-button'", cls='s1'),
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
                        Span(':', cls='o'),
                        Span('InputCounterOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('minValue', cls='nx'),
                        Span(':', cls='o'),
                        Span('0', cls='mi'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('maxValue', cls='nx'),
                        Span(':', cls='o'),
                        Span('null', cls='kc'),
                        Span(',', cls='p'),
                        Span('// infinite', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('onIncrement', cls='nx'),
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
                        Span("'input field value has been incremented'", cls='s1'),
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
                        Span('onDecrement', cls='nx'),
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
                        Span("'input field value has been decremented'", cls='s1'),
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
                        Span("'counter-input-example'", cls='s1'),
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
                        Span('* $targetEl: required', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $incrementEl: optional', cls='cm'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('* $decrementEl: optional', cls='cm'),
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
                        Span('counterInput', cls='nx'),
                        Span(':', cls='o'),
                        Span('InputCounterInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('InputCounter', cls='nx'),
                        Span('(', cls='p'),
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
                        Span('$incrementEl', cls='nx'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('$decrementEl', cls='nx'),
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
                        Span('// increment the value of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('counterInput', cls='nx'),
                        Span('.', cls='p'),
                        Span('increment', cls='nx'),
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
                        Span('// decrement the value of the input field', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('counterInput', cls='nx'),
                        Span('.', cls='p'),
                        Span('decrement', cls='nx'),
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
