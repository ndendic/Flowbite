from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from utils import component_showcase

component = Div(
    P(
        'The phone number input component from Flowbite can be used to set a phone number inside a form field by using the native',
        Code('type="tel"'),
        'attribute and also use a dropdown menu to select the country code.'
    ),
    P('The examples are built with the utility classes from Tailwind CSS and they are fully responsive, dark mode compatible and support RTL layouts and can be used for any type of web project.'),
    H2(
        'Default phone input',
        Span(id='default-phone-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default phone input', href='#default-phone-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use this component to set a phone number inside an input field by setting the',
        Code('type="tel"'),
        'attribute.'
    ),
    component_showcase(Div(
    Form(
        Label('Phone number:', fr='phone-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(d='M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 19 18',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        P('Select a phone number that matches the format.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('Phone number:', fr='phone-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Div(
                Svg(
                    Path(d='M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 19 18',
                    cls='w-4 h-4 text-gray-500 dark:text-gray-400'
                ),
                cls='absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none'
            ),
            Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
            cls='relative'
        ),
        P('Select a phone number that matches the format.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Phone input country code',
        Span(id='phone-input-country-code', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Phone input country code', href='#phone-input-country-code', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'This example can be used to select the country code from a dropdown menu and set the phone number inside an input field and use the',
        Code('pattern'),
        'attribute to validate the phone number.'
    ),
    component_showcase(Div(
    Form(
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
                Input(type='text', id='phone-input', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
                Input(type='text', id='phone-input', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center'
        ),
        cls='max-w-sm mx-auto'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Floating label input',
        Span(id='floating-label-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Floating label input', href='#floating-label-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Set a phone number inside an input field with a floating label inspired by Material UI from Google.'),
    component_showcase(Div(
    Form(
        Div(
            Span(
                Svg(
                    Path(d='M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 19 18',
                    cls='w-4 h-4 rtl:rotate-[270deg]'
                ),
                cls='absolute start-0 bottom-3 text-gray-500 dark:text-gray-400'
            ),
            Input(type='text', id='floating-phone-number', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder=' ', cls='block py-2.5 ps-6 pe-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-primary-500 focus:outline-none focus:ring-0 focus:border-primary-600 peer'),
            Label('Phone number', fr='floating-phone-number', cls='absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-placeholder-shown:start-6 peer-focus:start-0 peer-focus:text-primary-600 peer-focus:dark:text-primary-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto'),
            cls='relative'
        ),
        cls='max-w-xs mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Span(
                Svg(
                    Path(d='M18 13.446a3.02 3.02 0 0 0-.946-1.985l-1.4-1.4a3.054 3.054 0 0 0-4.218 0l-.7.7a.983.983 0 0 1-1.39 0l-2.1-2.1a.983.983 0 0 1 0-1.389l.7-.7a2.98 2.98 0 0 0 0-4.217l-1.4-1.4a2.824 2.824 0 0 0-4.218 0c-3.619 3.619-3 8.229 1.752 12.979C6.785 16.639 9.45 18 11.912 18a7.175 7.175 0 0 0 5.139-2.325A2.9 2.9 0 0 0 18 13.446Z'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 19 18',
                    cls='w-4 h-4 rtl:rotate-[270deg]'
                ),
                cls='absolute start-0 bottom-3 text-gray-500 dark:text-gray-400'
            ),
            Input(type='text', id='floating-phone-number', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder=' ', cls='block py-2.5 ps-6 pe-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-primary-500 focus:outline-none focus:ring-0 focus:border-primary-600 peer'),
            Label('Phone number', fr='floating-phone-number', cls='absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-placeholder-shown:start-6 peer-focus:start-0 peer-focus:text-primary-600 peer-focus:dark:text-primary-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto'),
            cls='relative'
        ),
        cls='max-w-xs mx-auto'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Verification code input',
        Span(id='verification-code-input', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Verification code input', href='#verification-code-input', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to send a verification code to the user’s phone number for authentication.'),
    component_showcase(Div(
    Form(
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center'
        ),
        P('We will send you an SMS with a verification code.', id='helper-text-explanation', cls='mt-2 mb-4 text-sm text-gray-500 dark:text-gray-400'),
        Button('Send verification code', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center'
        ),
        P('We will send you an SMS with a verification code.', id='helper-text-explanation', cls='mt-2 mb-4 text-sm text-gray-500 dark:text-gray-400'),
        Button('Send verification code', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Phone number select',
        Span(id='phone-number-select', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Phone number select', href='#phone-number-select', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to select one of your saved phone numbers from an application with a copy-paste feature.'),
    component_showcase(Div(
    Form(
        Div(
            Label('Primary phone number:', fr='phone-numbers', cls='text-sm font-medium text-gray-900 dark:text-white'),
            A('Manage numbers', href='#', cls='text-primary-700 dark:text-primary-500 text-xs font-medium hover:underline'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Div(
                Select(
                    Option('+1 234 456 7890', selected=True, value='+1 234 456 7890'),
                    Option('+1 456 234 7890', value='+1 456 234 7890'),
                    Option('+1 432 621 3163', value='+1 432 621 3163'),
                    id='phone-numbers',
                    aria_describedby='helper-text-explanation',
                    cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-900 text-sm rounded-s-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                ),
                cls='relative w-full'
            ),
            Button(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                    id='copy-icon',
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4'
                ),
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    id='copy-icon-success',
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 hidden'
                ),
                id='copy-number',
                data_copy_to_clipboard_target='phone-numbers',
                data_tooltip_target='tooltip-phone',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-gray-500 dark:text-gray-400 hover:text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:hover:text-white dark:border-gray-600'
            ),
            Div(
                Span('Copy number', id='tooltip-text'),
                Span('Copied!', id='tooltip-text-success', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-phone',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Please set your primary phone number.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Label('Primary phone number:', fr='phone-numbers', cls='text-sm font-medium text-gray-900 dark:text-white'),
            A('Manage numbers', href='#', cls='text-primary-700 dark:text-primary-500 text-xs font-medium hover:underline'),
            cls='mb-2 flex justify-between items-center'
        ),
        Div(
            Div(
                Select(
                    Option('+1 234 456 7890', selected=True, value='+1 234 456 7890'),
                    Option('+1 456 234 7890', value='+1 456 234 7890'),
                    Option('+1 432 621 3163', value='+1 432 621 3163'),
                    id='phone-numbers',
                    aria_describedby='helper-text-explanation',
                    cls='bg-gray-50 border border-e-0 border-gray-300 text-gray-900 text-sm rounded-s-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                ),
                cls='relative w-full'
            ),
            Button(
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z'),
                    id='copy-icon',
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4'
                ),
                Svg(
                    Path(d='M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z'),
                    id='copy-icon-success',
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='currentColor',
                    viewbox='0 0 18 20',
                    cls='w-4 h-4 hidden'
                ),
                id='copy-number',
                data_copy_to_clipboard_target='phone-numbers',
                data_tooltip_target='tooltip-phone',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-3 px-4 text-sm font-medium text-center text-gray-500 dark:text-gray-400 hover:text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:hover:text-white dark:border-gray-600'
            ),
            Div(
                Span('Copy number', id='tooltip-text'),
                Span('Copied!', id='tooltip-text-success', cls='hidden'),
                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                id='tooltip-phone',
                role='tooltip',
                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
            ),
            cls='flex items-center'
        ),
        P('Please set your primary phone number.', id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Authentication form',
        Span(id='authentication-form', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Authentication form', href='#authentication-form', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to authenticate users with a login form using a phone number instead of an email address.'),
    component_showcase(Div(
    Form(
        Label('Phone number:', fr='phone-input', cls='mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
            Div(
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center mt-2'
        ),
        Div(
            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white'),
            cls='mt-4'
        ),
        Div(
            Input(id='terms', aria_describedby='terms', type='checkbox', required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'),
            Label(
                'I accept the',
                A('Terms and Conditions', href='#', cls='font-medium text-primary-600 hover:underline dark:text-primary-500'),
                fr='terms',
                cls='text-gray-500 dark:text-gray-300 ms-2 text-sm'
            ),
            cls='flex items-center mt-4 mb-4'
        ),
        Button('Sign Up', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Label('Phone number:', fr='phone-input', cls='mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
            Div(
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            cls='flex items-center mt-2'
        ),
        Div(
            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white'),
            cls='mt-4'
        ),
        Div(
            Input(id='terms', aria_describedby='terms', type='checkbox', required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'),
            Label(
                'I accept the',
                A('Terms and Conditions', href='#', cls='font-medium text-primary-600 hover:underline dark:text-primary-500'),
                fr='terms',
                cls='text-gray-500 dark:text-gray-300 ms-2 text-sm'
            ),
            cls='flex items-center mt-4 mb-4'
        ),
        Button('Sign Up', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Advanced phone verification',
        Span(id='advanced-phone-verification', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Advanced phone verification', href='#advanced-phone-verification', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to verify a phone number via SMS or phone call using a dropdown component.'),
    component_showcase(Div(
    Form(
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
            Label('Phone number:', fr='phone-input', cls='text-sm font-medium sr-only text-gray-900 dark:text-white'),
            Div(
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 border-e-0 border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                'Send SMS',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-verification-option-button',
                data_dropdown_toggle='dropdown-verification-option',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('Send SMS', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Call', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-verification-option-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-verification-option',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            cls='flex items-center mt-2'
        ),
        Button('Activate account', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mt-4 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
), code="""Div(
    Form(
        Div(
            Button(
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
                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                        G(
                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                            filter='url(#filter0_d_343_121520)'
                        ),
                        mask='url(#a)'
                    ),
                    Defs(
                        Lineargradient(
                            Stop(stop_color='#fff'),
                            Stop(offset='1', stop_color='#F0F0F0'),
                            id='paint0_linear_343_121520',
                            x1='.933',
                            x2='.933',
                            y1='1.433',
                            y2='6.1',
                            gradientunits='userSpaceOnUse'
                        ),
                        Filter(
                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                            Feoffset(dy='1'),
                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                            id='filter0_d_343_121520',
                            width='6.533',
                            height='5.667',
                            x='.933',
                            y='1.433',
                            color_interpolation_filters='sRGB',
                            filterunits='userSpaceOnUse'
                        )
                    ),
                    fill='none',
                    aria_hidden='true',
                    viewbox='0 0 20 15',
                    cls='h-4 w-4 me-2'
                ),
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
                            Span(
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
                                        Path(fill='#D02F44', fill_rule='evenodd', d='M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z', clip_rule='evenodd'),
                                        Path(fill='#46467F', d='M0 .5h8.4v6.533H0z'),
                                        G(
                                            Path(fill='url(#paint0_linear_343_121520)', fill_rule='evenodd', d='M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z', clip_rule='evenodd'),
                                            filter='url(#filter0_d_343_121520)'
                                        ),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_343_121520',
                                            x1='.933',
                                            x2='.933',
                                            y1='1.433',
                                            y2='6.1',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Filter(
                                            Feflood(flood_opacity='0', result='BackgroundImageFix'),
                                            Fecolormatrix(in='SourceAlpha', result='hardAlpha', values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'),
                                            Feoffset(dy='1'),
                                            Fecolormatrix(values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'),
                                            Feblend(in2='BackgroundImageFix', result='effect1_dropShadow_343_121520'),
                                            Feblend(in='SourceGraphic', in2='effect1_dropShadow_343_121520', result='shape'),
                                            id='filter0_d_343_121520',
                                            width='6.533',
                                            height='5.667',
                                            x='.933',
                                            y='1.433',
                                            color_interpolation_filters='sRGB',
                                            filterunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    aria_hidden='true',
                                    viewbox='0 0 20 15',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                                        Path(fill='#fff', stroke='#fff', stroke_width='.667', d='M0 .167h-.901l.684.586 3.15 2.7v.609L-.194 6.295l-.14.1v1.24l.51-.319L3.83 5.033h.73L7.7 7.276a.488.488 0 00.601-.767L5.467 4.08v-.608l2.987-2.134a.667.667 0 00.28-.543V-.1l-.51.318L4.57 2.5h-.73L.66.229.572.167H0z'),
                                        Path(fill='url(#paint0_linear_374_135177)', fill_rule='evenodd', d='M0 2.833V4.7h3.267v2.133c0 .369.298.667.666.667h.534a.667.667 0 00.666-.667V4.7H8.2a.667.667 0 00.667-.667V3.5a.667.667 0 00-.667-.667H5.133V.5H3.267v2.333H0z', clip_rule='evenodd'),
                                        Path(fill='url(#paint1_linear_374_135177)', fill_rule='evenodd', d='M0 3.3h3.733V.5h.934v2.8H8.4v.933H4.667v2.8h-.934v-2.8H0V3.3z', clip_rule='evenodd'),
                                        Path(fill='#fff', fill_rule='evenodd', d='M4.2 11.933l-.823.433.157-.916-.666-.65.92-.133.412-.834.411.834.92.134-.665.649.157.916-.823-.433zm9.8.7l-.66.194.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.194zm0-8.866l-.66.193.194-.66-.194-.66.66.193.66-.193-.193.66.193.66-.66-.193zm2.8 2.8l-.66.193.193-.66-.193-.66.66.193.66-.193-.193.66.193.66-.66-.193zm-5.6.933l-.66.193.193-.66-.193-.66.66.194.66-.194-.193.66.193.66-.66-.193zm4.2 1.167l-.33.096.096-.33-.096-.33.33.097.33-.097-.097.33.097.33-.33-.096z', clip_rule='evenodd'),
                                        mask='url(#a)'
                                    ),
                                    Defs(
                                        Lineargradient(
                                            Stop(stop_color='#fff'),
                                            Stop(offset='1', stop_color='#F0F0F0'),
                                            id='paint0_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.5',
                                            gradientunits='userSpaceOnUse'
                                        ),
                                        Lineargradient(
                                            Stop(stop_color='#FF2E3B'),
                                            Stop(offset='1', stop_color='#FC0D1B'),
                                            id='paint1_linear_374_135177',
                                            x1='0',
                                            x2='0',
                                            y1='.5',
                                            y2='7.033',
                                            gradientunits='userSpaceOnUse'
                                        )
                                    ),
                                    fill='none',
                                    viewbox='0 0 20 15',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4 w-4 me-2'
                                ),
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
                            Span(
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
                            Span(
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
                            Span(
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
            Label('Phone number:', fr='phone-input', cls='text-sm font-medium sr-only text-gray-900 dark:text-white'),
            Div(
                Input(type='text', id='phone-input', aria_describedby='helper-text-explanation', pattern='[0-9]{3}-[0-9]{3}-[0-9]{4}', placeholder='123-456-7890', required=True, cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 border-e-0 border-s-0 border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-s-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-primary-500'),
                cls='relative w-full'
            ),
            Button(
                'Send SMS',
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 10 6',
                    cls='w-2.5 h-2.5 ms-2.5'
                ),
                id='dropdown-verification-option-button',
                data_dropdown_toggle='dropdown-verification-option',
                type='button',
                cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600'
            ),
            Div(
                Ul(
                    Li(
                        Button('Send SMS', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    Li(
                        Button('Call', type='button', role='menuitem', cls='inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white')
                    ),
                    aria_labelledby='dropdown-verification-option-button',
                    cls='py-2 text-sm text-gray-700 dark:text-gray-200'
                ),
                id='dropdown-verification-option',
                cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-36 dark:bg-gray-700'
            ),
            cls='flex items-center mt-2'
        ),
        Button('Activate account', type='submit', cls='text-white w-full bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 mt-4 me-2 mb-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800'),
        cls='max-w-sm mx-auto'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    id='mainContent'
)
