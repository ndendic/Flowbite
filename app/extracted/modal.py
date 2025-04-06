from fasthtml.common import *
from fasthtml.svg import *
from fastbite import *
from utils import component_showcase

component = Div(
    P('The modal component can be used as an interactive dialog on top of the main content area of the website to show notifications and gather information using form elements from your website users.'),
    P('Get started with multiple sizes, colors, and styles built with the utility classes from Tailwind CSS and the components from Flowbite.'),
    H2(
        'Default modal',
        Span(id='modal-01', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default modal', href='#modal-01', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'In order to create a modal with Tailwind CSS you only have to add',
        Code('data-modal-target="modalId"'),
        'data attribute where',
        Code('modalId'),
        'is the ID of the modal that you are targeting.'
    ),
    P('If you want to toggle the visibility, show, or hide the modal you can use the following data attributes where the value is the unique ID of the modal component:'),
    Ul(
        Li(
            Code('data-modal-toggle="modalID"'),
            '- toggle the modal'
        ),
        Li(
            Code('data-modal-show="modalID"'),
            '- show the modal'
        ),
        Li(
            Code('data-modal-hide="modalID"'),
            '- close the modal'
        )
    ),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='modal-01', data_modal_toggle='modal-01'),
    Modal(
        P("""With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
The European Unionâs General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. 
It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them."""
            ,cls=TextT.gray
        ),
        header=[
            ModalTitle("Modal Title"),
            ModalCloseButton(modal_id="modal-id")
        ],
        footer=Button("Close", data_modal_toggle="modal-01", cls=ButtonT.primary),
        id="modal-01"
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='modal-01', data_modal_toggle='modal-01', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Terms of Service', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_hide='modal-01',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='modal-01', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='modal-01', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-2xl max-h-full'
        ),
        id='modal-01',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Static modal',
        Span(id='static-modal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Static modal', href='#static-modal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-modal-backdrop="static"'),
        'data attribute to prevent the modal from closing when clicking outside of it. This can be used with situations where you want to force the user to choose an option such as a cookie notice or when taking a survey.'
    ),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='static-modal', data_modal_toggle='static-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Static modal', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_hide='static-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='static-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='static-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-2xl max-h-full'
        ),
        id='static-modal',
        data_modal_backdrop='static',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='static-modal', data_modal_toggle='static-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Static modal', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_hide='static-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='static-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='static-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-2xl max-h-full'
        ),
        id='static-modal',
        data_modal_backdrop='static',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Pop-up modal',
        Span(id='pop-up-modal', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Pop-up modal', href='#pop-up-modal', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can use this modal example to show a pop-up decision dialog to your users especially when deleting an item and making sure if the user really wants to do that by double confirming.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='popup-modal', data_modal_toggle='popup-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
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
                    data_modal_hide='popup-modal',
                    cls='absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200'
                    ),
                    H3('Are you sure you want to delete this product?', cls='mb-5 text-lg font-normal text-gray-500 dark:text-gray-400'),
                    Button("Yes, I'm sure", data_modal_hide='popup-modal', type='button', cls='text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center'),
                    Button('No, cancel', data_modal_hide='popup-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='p-4 md:p-5 text-center'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='popup-modal',
        tabindex='-1',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='popup-modal', data_modal_toggle='popup-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
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
                    data_modal_hide='popup-modal',
                    cls='absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                ),
                Div(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 20 20',
                        cls='mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200'
                    ),
                    H3('Are you sure you want to delete this product?', cls='mb-5 text-lg font-normal text-gray-500 dark:text-gray-400'),
                    Button("Yes, I'm sure", data_modal_hide='popup-modal', type='button', cls='text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center'),
                    Button('No, cancel', data_modal_hide='popup-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='p-4 md:p-5 text-center'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='popup-modal',
        tabindex='-1',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Form element',
        Span(id='form-element', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Form element', href='#form-element', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this modal example with form input element to receive information from your users with the advantage of not having to link to another page but keeping the user on the currently active page. A great example would be a login or a register form.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='authentication-modal', data_modal_toggle='authentication-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Sign in to our platform', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_hide='authentication-modal',
                        cls='end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    Form(
                        Div(
                            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white')
                        ),
                        Div(
                            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white')
                        ),
                        Div(
                            Div(
                                Div(
                                    Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800'),
                                    cls='flex items-center h-5'
                                ),
                                Label('Remember me', fr='remember', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                                cls='flex items-start'
                            ),
                            A('Lost Password?', href='#', cls='text-sm text-primary-700 hover:underline dark:text-primary-500'),
                            cls='flex justify-between'
                        ),
                        Button('Login to your account', type='submit', cls='w-full text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        Div(
                            'Not registered?',
                            A('Create account', href='#', cls='text-primary-700 hover:underline dark:text-primary-500'),
                            cls='text-sm font-medium text-gray-500 dark:text-gray-300'
                        ),
                        action='#',
                        cls='space-y-4'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='authentication-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='authentication-modal', data_modal_toggle='authentication-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Sign in to our platform', cls='text-xl font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_hide='authentication-modal',
                        cls='end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    Form(
                        Div(
                            Label('Your email', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='email', name='email', id='email', placeholder='name@company.com', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white')
                        ),
                        Div(
                            Label('Your password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='password', name='password', id='password', placeholder='â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢â\x80¢', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white')
                        ),
                        Div(
                            Div(
                                Div(
                                    Input(id='remember', type='checkbox', value=True, required=True, cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-600 dark:border-gray-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800'),
                                    cls='flex items-center h-5'
                                ),
                                Label('Remember me', fr='remember', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                                cls='flex items-start'
                            ),
                            A('Lost Password?', href='#', cls='text-sm text-primary-700 hover:underline dark:text-primary-500'),
                            cls='flex justify-between'
                        ),
                        Button('Login to your account', type='submit', cls='w-full text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                        Div(
                            'Not registered?',
                            A('Create account', href='#', cls='text-primary-700 hover:underline dark:text-primary-500'),
                            cls='text-sm font-medium text-gray-500 dark:text-gray-300'
                        ),
                        action='#',
                        cls='space-y-4'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='authentication-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Modal with CRUD',
        Span(id='modal-with-crud', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Modal with CRUD', href='#modal-with-crud', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example of a modal to use within CRUD (Create, Read, Update, Delete) operations to create new items, update existing ones, or delete them with a form inside of the modal.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='crud-modal', data_modal_toggle='crud-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Create New Product', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='crud-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Form(
                    Div(
                        Div(
                            Label('Name', fr='name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='text', name='name', id='name', placeholder='Type product name', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2'
                        ),
                        Div(
                            Label('Price', fr='price', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='number', name='price', id='price', placeholder='$2999', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2 sm:col-span-1'
                        ),
                        Div(
                            Label('Category', fr='category', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Select(
                                Option('Select category', selected=True),
                                Option('TV/Monitors', value='TV'),
                                Option('PC', value='PC'),
                                Option('Gaming/Console', value='GA'),
                                Option('Phones', value='PH'),
                                id='category',
                                cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                            ),
                            cls='col-span-2 sm:col-span-1'
                        ),
                        Div(
                            Label('Product Description', fr='description', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Textarea(id='description', rows='4', placeholder='Write product description here', cls='block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2'
                        ),
                        cls='grid gap-4 mb-4 grid-cols-2'
                    ),
                    Button(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z', clip_rule='evenodd'),
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='me-1 -ms-1 w-5 h-5'
                        ),
                        'Add new product',
                        type='submit',
                        cls='text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='crud-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='crud-modal', data_modal_toggle='crud-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Create New Product', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='crud-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Form(
                    Div(
                        Div(
                            Label('Name', fr='name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='text', name='name', id='name', placeholder='Type product name', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2'
                        ),
                        Div(
                            Label('Price', fr='price', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Input(type='number', name='price', id='price', placeholder='$2999', required=True, cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2 sm:col-span-1'
                        ),
                        Div(
                            Label('Category', fr='category', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Select(
                                Option('Select category', selected=True),
                                Option('TV/Monitors', value='TV'),
                                Option('PC', value='PC'),
                                Option('Gaming/Console', value='GA'),
                                Option('Phones', value='PH'),
                                id='category',
                                cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
                            ),
                            cls='col-span-2 sm:col-span-1'
                        ),
                        Div(
                            Label('Product Description', fr='description', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                            Textarea(id='description', rows='4', placeholder='Write product description here', cls='block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'),
                            cls='col-span-2'
                        ),
                        cls='grid gap-4 mb-4 grid-cols-2'
                    ),
                    Button(
                        Svg(
                            Path(fill_rule='evenodd', d='M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z', clip_rule='evenodd'),
                            fill='currentColor',
                            viewbox='0 0 20 20',
                            xmlns='http://www.w3.org/2000/svg',
                            cls='me-1 -ms-1 w-5 h-5'
                        ),
                        'Add new product',
                        type='submit',
                        cls='text-white inline-flex items-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='crud-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'Modal with radio inputs',
        Span(id='modal-with-radio-inputs', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Modal with radio inputs', href='#modal-with-radio-inputs', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a list of options to your users by using advanced radio inputs with a custom design.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='select-modal', data_modal_toggle='select-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Open positions', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='select-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('Select your desired position:', cls='text-gray-500 dark:text-gray-400 mb-4'),
                    Ul(
                        Li(
                            Input(type='radio', id='job-1', name='job', value='job-1', required=True, cls='hidden peer'),
                            Label(
                                Div(
                                    Div('UI/UX Engineer', cls='w-full text-lg font-semibold'),
                                    Div('Flowbite', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-1',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        Li(
                            Input(type='radio', id='job-2', name='job', value='job-2', cls='hidden peer'),
                            Label(
                                Div(
                                    Div('React Developer', cls='w-full text-lg font-semibold'),
                                    Div('Alphabet', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-2',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        Li(
                            Input(type='radio', id='job-3', name='job', value='job-3', cls='hidden peer'),
                            Label(
                                Div(
                                    Div('Full Stack Engineer', cls='w-full text-lg font-semibold'),
                                    Div('Apple', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-3',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        cls='space-y-4 mb-4'
                    ),
                    Button('Next step', cls='text-white inline-flex w-full justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='select-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='select-modal', data_modal_toggle='select-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Open positions', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='select-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('Select your desired position:', cls='text-gray-500 dark:text-gray-400 mb-4'),
                    Ul(
                        Li(
                            Input(type='radio', id='job-1', name='job', value='job-1', required=True, cls='hidden peer'),
                            Label(
                                Div(
                                    Div('UI/UX Engineer', cls='w-full text-lg font-semibold'),
                                    Div('Flowbite', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-1',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        Li(
                            Input(type='radio', id='job-2', name='job', value='job-2', cls='hidden peer'),
                            Label(
                                Div(
                                    Div('React Developer', cls='w-full text-lg font-semibold'),
                                    Div('Alphabet', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-2',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        Li(
                            Input(type='radio', id='job-3', name='job', value='job-3', cls='hidden peer'),
                            Label(
                                Div(
                                    Div('Full Stack Engineer', cls='w-full text-lg font-semibold'),
                                    Div('Apple', cls='w-full text-gray-500 dark:text-gray-400'),
                                    cls='block'
                                ),
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 14 10',
                                    cls='w-4 h-4 ms-3 rtl:rotate-180 text-gray-500 dark:text-gray-400'
                                ),
                                fr='job-3',
                                cls='inline-flex items-center justify-between w-full p-5 text-gray-900 bg-white border border-gray-200 rounded-lg cursor-pointer dark:hover:text-gray-300 dark:border-gray-500 dark:peer-checked:text-primary-500 peer-checked:border-primary-600 dark:peer-checked:border-primary-600 peer-checked:text-primary-600 hover:text-gray-900 hover:bg-gray-100 dark:text-white dark:bg-gray-600 dark:hover:bg-gray-500'
                            )
                        ),
                        cls='space-y-4 mb-4'
                    ),
                    Button('Next step', cls='text-white inline-flex w-full justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='select-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Modal with timeline',
        Span(id='modal-with-timeline', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Modal with timeline', href='#modal-with-timeline', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a timeline of events to your users with a modal. This can be used to show a changelog of your product or a timeline of events.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='timeline-modal', data_modal_toggle='timeline-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Changelog', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='timeline-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    Ol(
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3(
                                'Flowbite Application UI v2.0.0',
                                Span('Latest', cls='bg-primary-100 text-primary-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300 ms-3'),
                                cls='flex items-start mb-1 text-lg font-semibold text-gray-900 dark:text-white'
                            ),
                            Time('Released on Nov 10th, 2023', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            Button(
                                Svg(
                                    Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                    Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 20 20',
                                    cls='w-3 h-3 me-1.5'
                                ),
                                'Download',
                                type='button',
                                cls='py-2 px-3 inline-flex items-center text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                            ),
                            cls='mb-10 ms-8'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3('Flowbite Figma v2.8.0', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
                            Time('Released on Oct 7th, 2023', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            Button(
                                Svg(
                                    Path(d='M7.50012 45C11.6401 45 15.0002 41.6399 15.0002 37.4999V29.9999H7.50012C3.36009 29.9999 0 33.3599 0 37.4999C0 41.6399 3.36009 45 7.50012 45Z', fill='#0ACF83'),
                                    Path(d='M0 22.5C0 18.36 3.36009 14.9999 7.50012 14.9999H15.0002V29.9999H7.50012C3.36009 30.0001 0 26.64 0 22.5Z', fill='#A259FF'),
                                    Path(d='M0 7.50006C0 3.36006 3.36009 0 7.50012 0H15.0002V14.9999H7.50012C3.36009 14.9999 0 11.6401 0 7.50006Z', fill='#F24E1E'),
                                    Path(d='M15.0002 0H22.4999C26.6399 0 30 3.36006 30 7.50006C30 11.6401 26.6399 14.9999 22.4999 14.9999L15.0002 14.9999V0Z', fill='#FF7262'),
                                    Path(d='M30 22.5C30 26.64 26.6399 30 22.4999 30C18.3599 30 14.9998 26.64 14.9998 22.5C14.9998 18.36 18.3599 14.9999 22.4999 14.9999C26.6399 14.9999 30 18.36 30 22.5Z', fill='#1ABCFE'),
                                    aria_hidden='true',
                                    viewbox='0 0 30 45',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='w-3 h-3 me-1.5'
                                ),
                                'Duplicate in Figma',
                                type='button',
                                cls='py-2 px-3 inline-flex items-center text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                            ),
                            cls='mb-10 ms-8'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3('Flowbite Library v1.2.2', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
                            Time('Released on December 2nd, 2021', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            cls='ms-8'
                        ),
                        cls='relative border-s border-gray-200 dark:border-gray-600 ms-3.5 mb-4 md:mb-5'
                    ),
                    Button('My Downloads', cls='text-white inline-flex w-full justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='timeline-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='timeline-modal', data_modal_toggle='timeline-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
                Div(
                    H3('Changelog', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='timeline-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    Ol(
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3(
                                'Flowbite Application UI v2.0.0',
                                Span('Latest', cls='bg-primary-100 text-primary-800 text-sm font-medium mr-2 px-2.5 py-0.5 rounded-sm dark:bg-primary-900 dark:text-primary-300 ms-3'),
                                cls='flex items-start mb-1 text-lg font-semibold text-gray-900 dark:text-white'
                            ),
                            Time('Released on Nov 10th, 2023', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            Button(
                                Svg(
                                    Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                    Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currentColor',
                                    viewbox='0 0 20 20',
                                    cls='w-3 h-3 me-1.5'
                                ),
                                'Download',
                                type='button',
                                cls='py-2 px-3 inline-flex items-center text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                            ),
                            cls='mb-10 ms-8'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3('Flowbite Figma v2.8.0', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
                            Time('Released on Oct 7th, 2023', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            Button(
                                Svg(
                                    Path(d='M7.50012 45C11.6401 45 15.0002 41.6399 15.0002 37.4999V29.9999H7.50012C3.36009 29.9999 0 33.3599 0 37.4999C0 41.6399 3.36009 45 7.50012 45Z', fill='#0ACF83'),
                                    Path(d='M0 22.5C0 18.36 3.36009 14.9999 7.50012 14.9999H15.0002V29.9999H7.50012C3.36009 30.0001 0 26.64 0 22.5Z', fill='#A259FF'),
                                    Path(d='M0 7.50006C0 3.36006 3.36009 0 7.50012 0H15.0002V14.9999H7.50012C3.36009 14.9999 0 11.6401 0 7.50006Z', fill='#F24E1E'),
                                    Path(d='M15.0002 0H22.4999C26.6399 0 30 3.36006 30 7.50006C30 11.6401 26.6399 14.9999 22.4999 14.9999L15.0002 14.9999V0Z', fill='#FF7262'),
                                    Path(d='M30 22.5C30 26.64 26.6399 30 22.4999 30C18.3599 30 14.9998 26.64 14.9998 22.5C14.9998 18.36 18.3599 14.9999 22.4999 14.9999C26.6399 14.9999 30 18.36 30 22.5Z', fill='#1ABCFE'),
                                    aria_hidden='true',
                                    viewbox='0 0 30 45',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='w-3 h-3 me-1.5'
                                ),
                                'Duplicate in Figma',
                                type='button',
                                cls='py-2 px-3 inline-flex items-center text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'
                            ),
                            cls='mb-10 ms-8'
                        ),
                        Li(
                            Span(
                                Svg(
                                    Path(fill='currentColor', d='M6 1a1 1 0 0 0-2 0h2ZM4 4a1 1 0 0 0 2 0H4Zm7-3a1 1 0 1 0-2 0h2ZM9 4a1 1 0 1 0 2 0H9Zm7-3a1 1 0 1 0-2 0h2Zm-2 3a1 1 0 1 0 2 0h-2ZM1 6a1 1 0 0 0 0 2V6Zm18 2a1 1 0 1 0 0-2v2ZM5 11v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 11v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM10 15v-1H9v1h1Zm0 .01H9v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 15v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM15 11v-1h-1v1h1Zm0 .01h-1v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM5 15v-1H4v1h1Zm0 .01H4v1h1v-1Zm.01 0v1h1v-1h-1Zm0-.01h1v-1h-1v1ZM2 4h16V2H2v2Zm16 0h2a2 2 0 0 0-2-2v2Zm0 0v14h2V4h-2Zm0 14v2a2 2 0 0 0 2-2h-2Zm0 0H2v2h16v-2ZM2 18H0a2 2 0 0 0 2 2v-2Zm0 0V4H0v14h2ZM2 4V2a2 2 0 0 0-2 2h2Zm2-3v3h2V1H4Zm5 0v3h2V1H9Zm5 0v3h2V1h-2ZM1 8h18V6H1v2Zm3 3v.01h2V11H4Zm1 1.01h.01v-2H5v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H5v2h.01v-2ZM9 11v.01h2V11H9Zm1 1.01h.01v-2H10v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM9 15v.01h2V15H9Zm1 1.01h.01v-2H10v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H10v2h.01v-2ZM14 15v.01h2V15h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM14 11v.01h2V11h-2Zm1 1.01h.01v-2H15v2Zm1.01-1V11h-2v.01h2Zm-1-1.01H15v2h.01v-2ZM4 15v.01h2V15H4Zm1 1.01h.01v-2H5v2Zm1.01-1V15h-2v.01h2Zm-1-1.01H5v2h.01v-2Z'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 20 20',
                                    cls='w-2.5 h-2.5 text-gray-500 dark:text-gray-400'
                                ),
                                cls='absolute flex items-center justify-center w-6 h-6 bg-gray-100 rounded-full -start-3.5 ring-8 ring-white dark:ring-gray-700 dark:bg-gray-600'
                            ),
                            H3('Flowbite Library v1.2.2', cls='mb-1 text-lg font-semibold text-gray-900 dark:text-white'),
                            Time('Released on December 2nd, 2021', cls='block mb-3 text-sm font-normal leading-none text-gray-500 dark:text-gray-400'),
                            cls='ms-8'
                        ),
                        cls='relative border-s border-gray-200 dark:border-gray-600 ms-3.5 mb-4 md:mb-5'
                    ),
                    Button('My Downloads', cls='text-white inline-flex w-full justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='timeline-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Modal with progress bar',
        Span(id='modal-with-progress-bar', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Modal with progress bar', href='#modal-with-progress-bar', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This modal can be used to show the progress of a task to your users. It can be used to show the progress of a file upload or a task that is being processed.'),
    component_showcase(Div(
    Button('Toggle modal', data_modal_target='progress-modal', data_modal_toggle='progress-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
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
                    data_modal_hide='progress-modal',
                    cls='absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                ),
                Div(
                    Svg(
                        Path(d='M8 5.625c4.418 0 8-1.063 8-2.375S12.418.875 8 .875 0 1.938 0 3.25s3.582 2.375 8 2.375Zm0 13.5c4.963 0 8-1.538 8-2.375v-4.019c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353c-.193.081-.394.158-.6.231l-.189.067c-2.04.628-4.165.936-6.3.911a20.601 20.601 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244c-.053-.028-.113-.053-.165-.082v4.019C0 17.587 3.037 19.125 8 19.125Zm7.09-12.709c-.193.081-.394.158-.6.231l-.189.067a20.6 20.6 0 0 1-6.3.911 20.6 20.6 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244C.112 6.035.052 6.01 0 5.981V10c0 .837 3.037 2.375 8 2.375s8-1.538 8-2.375V5.981c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 16 20',
                        cls='w-10 h-10 text-gray-400 dark:text-gray-500 mb-4'
                    ),
                    H3('Approaching Full Capacity', cls='mb-1 text-xl font-bold text-gray-900 dark:text-white'),
                    P(
                        'Choosing the right server storage solution is essential for maintaining data integrity.',
                        P(
                            Div(
                                Span('My storage', cls='text-base font-normal'),
                                Span('376,3 of 500 GB used', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                                cls='flex justify-between mb-1 text-gray-500 dark:text-gray-400'
                            ),
                            Div(
                                Div(style='width: 85%', cls='bg-orange-500 h-2.5 rounded-full'),
                                cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-600'
                            ),
                            Div(
                                Button('Upgrade to PRO', data_modal_hide='progress-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                                Button('Cancel', data_modal_hide='progress-modal', type='button', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                cls='flex items-center mt-6 space-x-4 rtl:space-x-reverse'
                            )
                        ),
                        cls='text-gray-500 dark:text-gray-400 mb-6'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='progress-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button('Toggle modal', data_modal_target='progress-modal', data_modal_toggle='progress-modal', type='button', cls='block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
    Div(
        Div(
            Div(
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
                    data_modal_hide='progress-modal',
                    cls='absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                ),
                Div(
                    Svg(
                        Path(d='M8 5.625c4.418 0 8-1.063 8-2.375S12.418.875 8 .875 0 1.938 0 3.25s3.582 2.375 8 2.375Zm0 13.5c4.963 0 8-1.538 8-2.375v-4.019c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353c-.193.081-.394.158-.6.231l-.189.067c-2.04.628-4.165.936-6.3.911a20.601 20.601 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244c-.053-.028-.113-.053-.165-.082v4.019C0 17.587 3.037 19.125 8 19.125Zm7.09-12.709c-.193.081-.394.158-.6.231l-.189.067a20.6 20.6 0 0 1-6.3.911 20.6 20.6 0 0 1-6.3-.911l-.189-.067a10.719 10.719 0 0 1-.852-.34 8.08 8.08 0 0 1-.493-.244C.112 6.035.052 6.01 0 5.981V10c0 .837 3.037 2.375 8 2.375s8-1.538 8-2.375V5.981c-.052.029-.112.054-.165.082a8.08 8.08 0 0 1-.745.353Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 16 20',
                        cls='w-10 h-10 text-gray-400 dark:text-gray-500 mb-4'
                    ),
                    H3('Approaching Full Capacity', cls='mb-1 text-xl font-bold text-gray-900 dark:text-white'),
                    P(
                        'Choosing the right server storage solution is essential for maintaining data integrity.',
                        P(
                            Div(
                                Span('My storage', cls='text-base font-normal'),
                                Span('376,3 of 500 GB used', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                                cls='flex justify-between mb-1 text-gray-500 dark:text-gray-400'
                            ),
                            Div(
                                Div(style='width: 85%', cls='bg-orange-500 h-2.5 rounded-full'),
                                cls='w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-600'
                            ),
                            Div(
                                Button('Upgrade to PRO', data_modal_hide='progress-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                                Button('Cancel', data_modal_hide='progress-modal', type='button', cls='py-2.5 px-5 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                cls='flex items-center mt-6 space-x-4 rtl:space-x-reverse'
                            )
                        ),
                        cls='text-gray-500 dark:text-gray-400 mb-6'
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='progress-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Crypto wallet',
        Span(id='crypto-wallet', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Crypto wallet', href='#crypto-wallet', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this web3 modal component to show crypto wallet connection options like MetaMask or WalletConnect when building a website based on NFT authentication and collectibles.'),
    component_showcase(Div(
    Button(
        Svg(
            Path(stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1'),
            aria_hidden='true',
            fill='none',
            stroke='currentColor',
            viewbox='0 0 24 24',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-4 h-4 me-2'
        ),
        'Connect wallet',
        type='button',
        data_modal_target='crypto-modal',
        data_modal_toggle='crypto-modal',
        cls='text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Connect wallet', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='crypto-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('Connect with one of our available wallet providers or create a new one.', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    Ul(
                        Li(
                            A(
                                Svg(
                                    Path(d='M39.0728 0L21.9092 12.6999L25.1009 5.21543L39.0728 0Z', fill='#E17726'),
                                    Path(d='M0.966797 0.0151367L14.9013 5.21656L17.932 12.7992L0.966797 0.0151367Z', fill='#E27625'),
                                    Path(d='M32.1656 27.0093L39.7516 27.1537L37.1004 36.1603L27.8438 33.6116L32.1656 27.0093Z', fill='#E27625'),
                                    Path(d='M7.83409 27.0093L12.1399 33.6116L2.89876 36.1604L0.263672 27.1537L7.83409 27.0093Z', fill='#E27625'),
                                    Path(d='M17.5203 10.8677L17.8304 20.8807L8.55371 20.4587L11.1924 16.4778L11.2258 16.4394L17.5203 10.8677Z', fill='#E27625'),
                                    Path(d='M22.3831 10.7559L28.7737 16.4397L28.8067 16.4778L31.4455 20.4586L22.1709 20.8806L22.3831 10.7559Z', fill='#E27625'),
                                    Path(d='M12.4115 27.0381L17.4768 30.9848L11.5928 33.8257L12.4115 27.0381Z', fill='#E27625'),
                                    Path(d='M27.5893 27.0376L28.391 33.8258L22.5234 30.9847L27.5893 27.0376Z', fill='#E27625'),
                                    Path(d='M22.6523 30.6128L28.6066 33.4959L23.0679 36.1282L23.1255 34.3884L22.6523 30.6128Z', fill='#D5BFB2'),
                                    Path(d='M17.3458 30.6143L16.8913 34.3601L16.9286 36.1263L11.377 33.4961L17.3458 30.6143Z', fill='#D5BFB2'),
                                    Path(d='M15.6263 22.1875L17.1822 25.4575L11.8848 23.9057L15.6263 22.1875Z', fill='#233447'),
                                    Path(d='M24.3739 22.1875L28.133 23.9053L22.8184 25.4567L24.3739 22.1875Z', fill='#233447'),
                                    Path(d='M12.8169 27.0049L11.9606 34.0423L7.37109 27.1587L12.8169 27.0049Z', fill='#CC6228'),
                                    Path(d='M27.1836 27.0049L32.6296 27.1587L28.0228 34.0425L27.1836 27.0049Z', fill='#CC6228'),
                                    Path(d='M31.5799 20.0605L27.6165 24.0998L24.5608 22.7034L23.0978 25.779L22.1387 20.4901L31.5799 20.0605Z', fill='#CC6228'),
                                    Path(d='M8.41797 20.0605L17.8608 20.4902L16.9017 25.779L15.4384 22.7038L12.3988 24.0999L8.41797 20.0605Z', fill='#CC6228'),
                                    Path(d='M8.15039 19.2314L12.6345 23.7816L12.7899 28.2736L8.15039 19.2314Z', fill='#E27525'),
                                    Path(d='M31.8538 19.2236L27.2061 28.2819L27.381 23.7819L31.8538 19.2236Z', fill='#E27525'),
                                    Path(d='M17.6412 19.5088L17.8217 20.6447L18.2676 23.4745L17.9809 32.166L16.6254 25.1841L16.625 25.1119L17.6412 19.5088Z', fill='#E27525'),
                                    Path(d='M22.3562 19.4932L23.3751 25.1119L23.3747 25.1841L22.0158 32.1835L21.962 30.4328L21.75 23.4231L22.3562 19.4932Z', fill='#E27525'),
                                    Path(d='M27.7797 23.6011L27.628 27.5039L22.8977 31.1894L21.9414 30.5138L23.0133 24.9926L27.7797 23.6011Z', fill='#F5841F'),
                                    Path(d='M12.2373 23.6011L16.9873 24.9926L18.0591 30.5137L17.1029 31.1893L12.3723 27.5035L12.2373 23.6011Z', fill='#F5841F'),
                                    Path(d='M10.4717 32.6338L16.5236 35.5013L16.4979 34.2768L17.0043 33.8323H22.994L23.5187 34.2753L23.48 35.4989L29.4935 32.641L26.5673 35.0591L23.0289 37.4894H16.9558L13.4197 35.0492L10.4717 32.6338Z', fill='#C0AC9D'),
                                    Path(d='M22.2191 30.231L23.0748 30.8354L23.5763 34.8361L22.8506 34.2234H17.1513L16.4395 34.8485L16.9244 30.8357L17.7804 30.231H22.2191Z', fill='#161616'),
                                    Path(d='M37.9395 0.351562L39.9998 6.53242L38.7131 12.7819L39.6293 13.4887L38.3895 14.4346L39.3213 15.1542L38.0875 16.2779L38.8449 16.8264L36.8347 19.1742L28.5894 16.7735L28.5179 16.7352L22.5762 11.723L37.9395 0.351562Z', fill='#763E1A'),
                                    Path(d='M2.06031 0.351562L17.4237 11.723L11.4819 16.7352L11.4105 16.7735L3.16512 19.1742L1.15488 16.8264L1.91176 16.2783L0.678517 15.1542L1.60852 14.4354L0.350209 13.4868L1.30098 12.7795L0 6.53265L2.06031 0.351562Z', fill='#763E1A'),
                                    Path(d='M28.1861 16.2485L36.9226 18.7921L39.7609 27.5398L32.2728 27.5398L27.1133 27.6049L30.8655 20.2912L28.1861 16.2485Z', fill='#F5841F'),
                                    Path(d='M11.8139 16.2485L9.13399 20.2912L12.8867 27.6049L7.72971 27.5398H0.254883L3.07728 18.7922L11.8139 16.2485Z', fill='#F5841F'),
                                    Path(d='M25.5283 5.17383L23.0847 11.7736L22.5661 20.6894L22.3677 23.4839L22.352 30.6225H17.6471L17.6318 23.4973L17.4327 20.6869L16.9139 11.7736L14.4707 5.17383H25.5283Z', fill='#F5841F'),
                                    aria_hidden='true',
                                    viewbox='0 0 40 38',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4'
                                ),
                                Span('MetaMask', cls='flex-1 ms-3 whitespace-nowrap'),
                                Span('Popular', cls='inline-flex items-center justify-center px-2 py-0.5 ms-3 text-xs font-medium text-gray-500 bg-gray-200 rounded-sm dark:bg-gray-700 dark:text-gray-400'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Svg(
                                    Path(d='M145.7 291.66C226.146 291.66 291.36 226.446 291.36 146C291.36 65.5541 226.146 0.339844 145.7 0.339844C65.2542 0.339844 0.0400391 65.5541 0.0400391 146C0.0400391 226.446 65.2542 291.66 145.7 291.66Z', fill='#3259A5'),
                                    Path(d='M195.94 155.5C191.49 179.08 170.8 196.91 145.93 196.91C117.81 196.91 95.0204 174.12 95.0204 146C95.0204 117.88 117.81 95.0897 145.93 95.0897C170.8 95.0897 191.49 112.93 195.94 136.5H247.31C242.52 84.7197 198.96 44.1797 145.93 44.1797C89.6904 44.1797 44.1104 89.7697 44.1104 146C44.1104 202.24 89.7004 247.82 145.93 247.82C198.96 247.82 242.52 207.28 247.31 155.5H195.94Z', fill='white'),
                                    aria_hidden='true',
                                    viewbox='0 0 292 292',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-5'
                                ),
                                Span('Coinbase Wallet', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Span('Opera Wallet', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Span('WalletConnect', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Svg(
                                    Path(d='M72.0998 0.600098H48.3998H24.5998H0.799805V24.4001V48.2001V49.7001V71.8001V71.9001V95.5001H24.5998V72.0001V71.9001V49.8001V48.3001V24.5001H48.3998H72.1998H95.9998V0.700104H72.0998V0.600098Z', fill='#617BFF'),
                                    Path(d='M48.5 71.8002H72.1V95.6002H73C79.1 95.6002 84.9 93.2002 89.2 88.9002C93.5 84.6002 95.9 78.8002 95.9 72.7002V48.2002H48.5V71.8002Z', fill='#617BFF'),
                                    aria_hidden='true',
                                    viewbox='0 0 96 96',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4'
                                ),
                                Span('Fortmatic', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        cls='my-4 space-y-3'
                    ),
                    Div(
                        A(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 20 20',
                                cls='w-3 h-3 me-2'
                            ),
                            'Why do I need to connect with my wallet?',
                            href='#',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 hover:underline dark:text-gray-400'
                        )
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='crypto-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Button(
        Svg(
            Path(stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1'),
            aria_hidden='true',
            fill='none',
            stroke='currentColor',
            viewbox='0 0 24 24',
            xmlns='http://www.w3.org/2000/svg',
            cls='w-4 h-4 me-2'
        ),
        'Connect wallet',
        type='button',
        data_modal_target='crypto-modal',
        data_modal_toggle='crypto-modal',
        cls='text-gray-900 bg-white hover:bg-gray-100 border border-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:focus:ring-gray-600 dark:bg-gray-800 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Connect wallet', cls='text-lg font-semibold text-gray-900 dark:text-white'),
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
                        data_modal_toggle='crypto-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm h-8 w-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('Connect with one of our available wallet providers or create a new one.', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    Ul(
                        Li(
                            A(
                                Svg(
                                    Path(d='M39.0728 0L21.9092 12.6999L25.1009 5.21543L39.0728 0Z', fill='#E17726'),
                                    Path(d='M0.966797 0.0151367L14.9013 5.21656L17.932 12.7992L0.966797 0.0151367Z', fill='#E27625'),
                                    Path(d='M32.1656 27.0093L39.7516 27.1537L37.1004 36.1603L27.8438 33.6116L32.1656 27.0093Z', fill='#E27625'),
                                    Path(d='M7.83409 27.0093L12.1399 33.6116L2.89876 36.1604L0.263672 27.1537L7.83409 27.0093Z', fill='#E27625'),
                                    Path(d='M17.5203 10.8677L17.8304 20.8807L8.55371 20.4587L11.1924 16.4778L11.2258 16.4394L17.5203 10.8677Z', fill='#E27625'),
                                    Path(d='M22.3831 10.7559L28.7737 16.4397L28.8067 16.4778L31.4455 20.4586L22.1709 20.8806L22.3831 10.7559Z', fill='#E27625'),
                                    Path(d='M12.4115 27.0381L17.4768 30.9848L11.5928 33.8257L12.4115 27.0381Z', fill='#E27625'),
                                    Path(d='M27.5893 27.0376L28.391 33.8258L22.5234 30.9847L27.5893 27.0376Z', fill='#E27625'),
                                    Path(d='M22.6523 30.6128L28.6066 33.4959L23.0679 36.1282L23.1255 34.3884L22.6523 30.6128Z', fill='#D5BFB2'),
                                    Path(d='M17.3458 30.6143L16.8913 34.3601L16.9286 36.1263L11.377 33.4961L17.3458 30.6143Z', fill='#D5BFB2'),
                                    Path(d='M15.6263 22.1875L17.1822 25.4575L11.8848 23.9057L15.6263 22.1875Z', fill='#233447'),
                                    Path(d='M24.3739 22.1875L28.133 23.9053L22.8184 25.4567L24.3739 22.1875Z', fill='#233447'),
                                    Path(d='M12.8169 27.0049L11.9606 34.0423L7.37109 27.1587L12.8169 27.0049Z', fill='#CC6228'),
                                    Path(d='M27.1836 27.0049L32.6296 27.1587L28.0228 34.0425L27.1836 27.0049Z', fill='#CC6228'),
                                    Path(d='M31.5799 20.0605L27.6165 24.0998L24.5608 22.7034L23.0978 25.779L22.1387 20.4901L31.5799 20.0605Z', fill='#CC6228'),
                                    Path(d='M8.41797 20.0605L17.8608 20.4902L16.9017 25.779L15.4384 22.7038L12.3988 24.0999L8.41797 20.0605Z', fill='#CC6228'),
                                    Path(d='M8.15039 19.2314L12.6345 23.7816L12.7899 28.2736L8.15039 19.2314Z', fill='#E27525'),
                                    Path(d='M31.8538 19.2236L27.2061 28.2819L27.381 23.7819L31.8538 19.2236Z', fill='#E27525'),
                                    Path(d='M17.6412 19.5088L17.8217 20.6447L18.2676 23.4745L17.9809 32.166L16.6254 25.1841L16.625 25.1119L17.6412 19.5088Z', fill='#E27525'),
                                    Path(d='M22.3562 19.4932L23.3751 25.1119L23.3747 25.1841L22.0158 32.1835L21.962 30.4328L21.75 23.4231L22.3562 19.4932Z', fill='#E27525'),
                                    Path(d='M27.7797 23.6011L27.628 27.5039L22.8977 31.1894L21.9414 30.5138L23.0133 24.9926L27.7797 23.6011Z', fill='#F5841F'),
                                    Path(d='M12.2373 23.6011L16.9873 24.9926L18.0591 30.5137L17.1029 31.1893L12.3723 27.5035L12.2373 23.6011Z', fill='#F5841F'),
                                    Path(d='M10.4717 32.6338L16.5236 35.5013L16.4979 34.2768L17.0043 33.8323H22.994L23.5187 34.2753L23.48 35.4989L29.4935 32.641L26.5673 35.0591L23.0289 37.4894H16.9558L13.4197 35.0492L10.4717 32.6338Z', fill='#C0AC9D'),
                                    Path(d='M22.2191 30.231L23.0748 30.8354L23.5763 34.8361L22.8506 34.2234H17.1513L16.4395 34.8485L16.9244 30.8357L17.7804 30.231H22.2191Z', fill='#161616'),
                                    Path(d='M37.9395 0.351562L39.9998 6.53242L38.7131 12.7819L39.6293 13.4887L38.3895 14.4346L39.3213 15.1542L38.0875 16.2779L38.8449 16.8264L36.8347 19.1742L28.5894 16.7735L28.5179 16.7352L22.5762 11.723L37.9395 0.351562Z', fill='#763E1A'),
                                    Path(d='M2.06031 0.351562L17.4237 11.723L11.4819 16.7352L11.4105 16.7735L3.16512 19.1742L1.15488 16.8264L1.91176 16.2783L0.678517 15.1542L1.60852 14.4354L0.350209 13.4868L1.30098 12.7795L0 6.53265L2.06031 0.351562Z', fill='#763E1A'),
                                    Path(d='M28.1861 16.2485L36.9226 18.7921L39.7609 27.5398L32.2728 27.5398L27.1133 27.6049L30.8655 20.2912L28.1861 16.2485Z', fill='#F5841F'),
                                    Path(d='M11.8139 16.2485L9.13399 20.2912L12.8867 27.6049L7.72971 27.5398H0.254883L3.07728 18.7922L11.8139 16.2485Z', fill='#F5841F'),
                                    Path(d='M25.5283 5.17383L23.0847 11.7736L22.5661 20.6894L22.3677 23.4839L22.352 30.6225H17.6471L17.6318 23.4973L17.4327 20.6869L16.9139 11.7736L14.4707 5.17383H25.5283Z', fill='#F5841F'),
                                    aria_hidden='true',
                                    viewbox='0 0 40 38',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4'
                                ),
                                Span('MetaMask', cls='flex-1 ms-3 whitespace-nowrap'),
                                Span('Popular', cls='inline-flex items-center justify-center px-2 py-0.5 ms-3 text-xs font-medium text-gray-500 bg-gray-200 rounded-sm dark:bg-gray-700 dark:text-gray-400'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Svg(
                                    Path(d='M145.7 291.66C226.146 291.66 291.36 226.446 291.36 146C291.36 65.5541 226.146 0.339844 145.7 0.339844C65.2542 0.339844 0.0400391 65.5541 0.0400391 146C0.0400391 226.446 65.2542 291.66 145.7 291.66Z', fill='#3259A5'),
                                    Path(d='M195.94 155.5C191.49 179.08 170.8 196.91 145.93 196.91C117.81 196.91 95.0204 174.12 95.0204 146C95.0204 117.88 117.81 95.0897 145.93 95.0897C170.8 95.0897 191.49 112.93 195.94 136.5H247.31C242.52 84.7197 198.96 44.1797 145.93 44.1797C89.6904 44.1797 44.1104 89.7697 44.1104 146C44.1104 202.24 89.7004 247.82 145.93 247.82C198.96 247.82 242.52 207.28 247.31 155.5H195.94Z', fill='white'),
                                    aria_hidden='true',
                                    viewbox='0 0 292 292',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-5'
                                ),
                                Span('Coinbase Wallet', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Span('Opera Wallet', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Span('WalletConnect', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        Li(
                            A(
                                Svg(
                                    Path(d='M72.0998 0.600098H48.3998H24.5998H0.799805V24.4001V48.2001V49.7001V71.8001V71.9001V95.5001H24.5998V72.0001V71.9001V49.8001V48.3001V24.5001H48.3998H72.1998H95.9998V0.700104H72.0998V0.600098Z', fill='#617BFF'),
                                    Path(d='M48.5 71.8002H72.1V95.6002H73C79.1 95.6002 84.9 93.2002 89.2 88.9002C93.5 84.6002 95.9 78.8002 95.9 72.7002V48.2002H48.5V71.8002Z', fill='#617BFF'),
                                    aria_hidden='true',
                                    viewbox='0 0 96 96',
                                    fill='none',
                                    xmlns='http://www.w3.org/2000/svg',
                                    cls='h-4'
                                ),
                                Span('Fortmatic', cls='flex-1 ms-3 whitespace-nowrap'),
                                href='#',
                                cls='flex items-center p-3 text-base font-bold text-gray-900 rounded-lg bg-gray-50 hover:bg-gray-100 group hover:shadow dark:bg-gray-600 dark:hover:bg-gray-500 dark:text-white'
                            )
                        ),
                        cls='my-4 space-y-3'
                    ),
                    Div(
                        A(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 20 20',
                                cls='w-3 h-3 me-2'
                            ),
                            'Why do I need to connect with my wallet?',
                            href='#',
                            cls='inline-flex items-center text-xs font-normal text-gray-500 hover:underline dark:text-gray-400'
                        )
                    ),
                    cls='p-4 md:p-5'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative p-4 w-full max-w-md max-h-full'
        ),
        id='crypto-modal',
        tabindex='-1',
        aria_hidden='true',
        cls='hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can use four different modal sizing options starting from small to extra large, but keep in mind that the width of these modals will remain the same when browsing on smaller devices.'),
    component_showcase(Div(
    Div(
        Button('Small modal', data_modal_target='small-modal', data_modal_toggle='small-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Default modal', data_modal_target='medium-modal', data_modal_toggle='medium-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Large modal', data_modal_target='large-modal', data_modal_toggle='large-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Extra large modal', data_modal_target='extralarge-modal', data_modal_toggle='extralarge-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        cls='block space-y-4 md:flex md:space-y-0 md:space-x-4 rtl:space-x-reverse'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Small modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='small-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='small-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='small-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-md max-h-full'
        ),
        id='small-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Default modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='medium-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='medium-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='medium-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-lg max-h-full'
        ),
        id='medium-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Large modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='large-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='large-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='large-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-4xl max-h-full'
        ),
        id='large-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Extra Large modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='extralarge-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='extralarge-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='extralarge-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-7xl max-h-full'
        ),
        id='extralarge-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Div(
        Button('Small modal', data_modal_target='small-modal', data_modal_toggle='small-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Default modal', data_modal_target='medium-modal', data_modal_toggle='medium-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Large modal', data_modal_target='large-modal', data_modal_toggle='large-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Extra large modal', data_modal_target='extralarge-modal', data_modal_toggle='extralarge-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        cls='block space-y-4 md:flex md:space-y-0 md:space-x-4 rtl:space-x-reverse'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Small modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='small-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='small-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='small-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-md max-h-full'
        ),
        id='small-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Default modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='medium-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='medium-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='medium-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-lg max-h-full'
        ),
        id='medium-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Large modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='large-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='large-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='large-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-4xl max-h-full'
        ),
        id='large-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Extra Large modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='extralarge-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='extralarge-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='extralarge-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-7xl max-h-full'
        ),
        id='extralarge-modal',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Placement',
        Span(id='placement', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Placement', href='#placement', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Use the',
        Code('data-modal-placement'),
        'data attribute on the modal element to set the position relative to the document body based on the available values from',
        Code('{top|center|bottom}-{left|center|right}'),
        '(eg.',
        Code('top-left'),
        'or',
        Code('bottom-right'),
        ').'
    ),
    P('The default position is the center of the page.'),
    component_showcase(Div(
    Div(
        Button('Top left', data_modal_target='top-left-modal', data_modal_toggle='top-left-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Top right', data_modal_target='top-right-modal', data_modal_toggle='top-right-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Bottom left', data_modal_target='bottom-left-modal', data_modal_toggle='bottom-left-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Bottom right', data_modal_target='bottom-right-modal', data_modal_toggle='bottom-right-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        cls='block space-y-4 md:flex md:space-y-0 md:space-x-4 md:rtl:space-x-reverse'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Top left modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='top-left-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='top-left-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='top-left-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='top-left-modal',
        data_modal_placement='top-left',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Top right modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='top-right-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='top-right-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='top-right-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='top-right-modal',
        data_modal_placement='top-right',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Bottom left modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='bottom-left-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='bottom-left-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='bottom-left-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='bottom-left-modal',
        data_modal_placement='bottom-left',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Bottom right modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='bottom-right-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='bottom-right-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='bottom-right-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='bottom-right-modal',
        data_modal_placement='bottom-right',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
), code="""Div(
    Div(
        Button('Top left', data_modal_target='top-left-modal', data_modal_toggle='top-left-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Top right', data_modal_target='top-right-modal', data_modal_toggle='top-right-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Bottom left', data_modal_target='bottom-left-modal', data_modal_toggle='bottom-left-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        Button('Bottom right', data_modal_target='bottom-right-modal', data_modal_toggle='bottom-right-modal', type='button', cls='block w-full md:w-auto text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
        cls='block space-y-4 md:flex md:space-y-0 md:space-x-4 md:rtl:space-x-reverse'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Top left modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='top-left-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='top-left-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='top-left-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='top-left-modal',
        data_modal_placement='top-left',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Top right modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='top-right-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='top-right-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='top-right-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='top-right-modal',
        data_modal_placement='top-right',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Bottom left modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='bottom-left-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='bottom-left-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='bottom-left-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='bottom-left-modal',
        data_modal_placement='bottom-left',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    ),
    Div(
        Div(
            Div(
                Div(
                    H3('Bottom right modal', cls='text-xl font-medium text-gray-900 dark:text-white'),
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
                        data_modal_hide='bottom-right-modal',
                        cls='text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white'
                    ),
                    cls='flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600 border-gray-200'
                ),
                Div(
                    P('With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    P('The European Unionâ\x80\x99s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.', cls='text-base leading-relaxed text-gray-500 dark:text-gray-400'),
                    cls='p-4 md:p-5 space-y-4'
                ),
                Div(
                    Button('I accept', data_modal_hide='bottom-right-modal', type='button', cls='text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'),
                    Button('Decline', data_modal_hide='bottom-right-modal', type='button', cls='py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                    cls='flex items-center p-4 md:p-5 space-x-3 rtl:space-x-reverse border-t border-gray-200 rounded-b dark:border-gray-600'
                ),
                cls='relative bg-white rounded-lg shadow-sm dark:bg-gray-700'
            ),
            cls='relative w-full max-w-2xl max-h-full'
        ),
        id='bottom-right-modal',
        data_modal_placement='bottom-right',
        tabindex='-1',
        cls='fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H2(
        'More examples',
        Span(id='more-examples', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: More examples', href='#more-examples', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('You can check out more modal component examples from the following resources from Flowbite Blocks:'),
    Ul(
        Li(
            A('CRUD read modals', href='https://flowbite.com/blocks/application/crud-read-modals/')
        ),
        Li(
            A('CRUD create modals', href='https://flowbite.com/blocks/application/crud-create-modals/')
        ),
        Li(
            A('CRUD update modals', href='https://flowbite.com/blocks/application/crud-update-modals/')
        ),
        Li(
            A('Faceted search modals', href='https://flowbite.com/blocks/application/faceted-search-modals/')
        )
    ),
    H2(
        'JavaScript behaviour',
        Span(id='javascript-behaviour', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: JavaScript behaviour', href='#javascript-behaviour', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'The',
        Strong('Modal'),
        'class from Flowbite can be used to create an object that will launch an interactive modal based on the object parameters, options, and methods that you choose to apply.'
    ),
    H3(
        'Object parameters',
        Span(id='object-parameters', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Object parameters', href='#object-parameters', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Initialize a Modal object with parameters such as the modal element and the optional options object.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Parameter', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Required', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('targetEl', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Element', cls='px-6 py-4'),
                    Td('Required', cls='px-6 py-4'),
                    Td('Set the main modal element as a JavaScript object.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('options', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Object', cls='px-6 py-4'),
                    Td('Optional', cls='px-6 py-4'),
                    Td('Use the options parameter to set the default state of the modal, placement, and animations.', cls='px-6 py-4'),
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
    P('Use the following options as the second parameter for the Modal object to set the position of the modal, custom classes for the backdrop element and the callback functions.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Option', scope='col', cls='px-6 py-3'),
                    Th('Type', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('placement', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td(
                        'Set the position of the modal element relative to the document body by choosing one of the values from',
                        Code('{top|center|right}-{left|center|right}', cls='text-purple-600 dark:text-purple-400'),
                        '. (eg. top-left or bottom-right)',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('backdrop', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td(
                        'Choose between',
                        Code('static', cls='text-purple-600 dark:text-purple-400'),
                        'or',
                        Code('dynamic', cls='text-purple-600 dark:text-purple-400'),
                        'to prevent closing the modal when clicking outside.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('backdropClasses', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('String', cls='px-6 py-4'),
                    Td(
                        'Set a string of Tailwind CSS classes for the backdrop element (eg.',
                        Code("'bg-primary-500 dark:bg-primary-400'", cls='text-purple-600 dark:text-purple-400'),
                        '.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('closable', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Boolean', cls='px-6 py-4'),
                    Td(
                        'Set to',
                        Code('false', cls='text-purple-600 dark:text-purple-400'),
                        'to disable closing the modal on hitting ESC or clicking on the backdrop.',
                        cls='px-6 py-4'
                    ),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onHide', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the modal has been hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onShow', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the modal has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('onToggle', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Function', cls='px-6 py-4'),
                    Td('Set a callback function when the modal visibility has been toggled.', cls='px-6 py-4'),
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
    P('Use the methods from the Modal object to show, hide, and toggle the visibility directly from JavaScript.'),
    Div(
        Table(
            Thead(
                Tr(
                    Th('Method', scope='col', cls='px-6 py-3'),
                    Th('Description', scope='col', cls='px-6 py-3'),
                    cls='text-xs font-medium uppercase'
                ),
                cls='bg-gray-50 dark:bg-gray-700'
            ),
            Tbody(
                Tr(
                    Td(
                        Code('toggle()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td("Use the toggle function on the Modal object to toggle the modal element's visibility.", cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('show()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use the show function on the Modal object to show the modal element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('hide()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use the hide function on the Modal object to hide the modal element.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('isHidden()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to check if the modal is hidden.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('isVisible()', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this function to check if the modal is visible.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnShow(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the modal has been shown.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnHide(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the modal has been closed.', cls='px-6 py-4'),
                    cls='border-b dark:bg-gray-800 dark:border-gray-700 border-gray-200'
                ),
                Tr(
                    Td(
                        Code('updateOnToggle(callback)', cls='text-primary-600 dark:text-primary-400'),
                        cls='px-6 py-4 font-medium'
                    ),
                    Td('Use this method to set a custom callback function when the modal visibility has been toggled.', cls='px-6 py-4'),
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
    P('Check out the following JavaScript example to learn how to initialize, set the options, and use the methods for the Modal object.'),
    P('First of all, create a new JavaScript element object for the first parameter of the Modal object and another options object to set the placement, backdrop styles, and callback functions.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// set the modal menu element', cls='c1'),
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
                        Span("'modalEl'", cls='s1'),
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
                        Span('// options with default values', cls='c1'),
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
                        Span('placement', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bottom-right'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('backdrop', cls='nx'),
                        Span(':', cls='o'),
                        Span("'dynamic'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('backdropClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'bg-gray-900/50 dark:bg-gray-900/80 fixed inset-0 z-40'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('closable', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onHide', cls='nx'),
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
                        Span("'modal is hidden'", cls='s1'),
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
                        Span('onShow', cls='nx'),
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
                        Span("'modal is shown'", cls='s1'),
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
                        Span('onToggle', cls='nx'),
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
                        Span("'modal has been toggled'", cls='s1'),
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
                        Span("'modalEl'", cls='s1'),
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
    P('Create a new Modal object based on the options above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Modal', cls='nx'),
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
                        Span('modal', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Modal', cls='nx'),
                        Span('(', cls='p'),
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
    P(
        'Use the',
        Code('show'),
        'and',
        Code('hide'),
        'methods to show and hide the modal component directly from JavaScript.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// show the modal', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
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
                        Span('// hide the modal', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('hide', cls='nx'),
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
    P(
        'Use the',
        Code('toggle'),
        'method to toggle the visibility of the modal.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// toggle the modal', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('toggle', cls='nx'),
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
    P(
        'Use the',
        Code('isHidden'),
        'or',
        Code('isVisible'),
        'method to check if the modal is visible or not.'
    ),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('// true if hidden', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('isHidden', cls='nx'),
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
                        Span('// true if visible', cls='c1'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span(cls='c1'),
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('isVisible', cls='nx'),
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
    P('Use the following HTML code for the JavaScript example above.'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('id', cls='na'),
                        Span('=', cls='o'),
                        Span('"modalEl"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('tabindex', cls='na'),
                        Span('=', cls='o'),
                        Span('"-1"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"fixed left-0 right-0 top-0 z-50 hidden h-[calc(100%-1rem)] max-h-full w-full overflow-y-auto overflow-x-hidden p-4 md:inset-0"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
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
                        Span('"relative max-h-full w-full max-w-2xl"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Modal content -->', cls='c'),
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
                        Span('"relative rounded-lg bg-white shadow-sm dark:bg-gray-700"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Modal header -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex items-start justify-between rounded-t border-b p-5 dark:border-gray-600"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('h3', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-xl font-semibold text-gray-900 dark:text-white lg:text-2xl"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Terms of Service', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('</', cls='p'),
                        Span('h3', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"ms-auto inline-flex h-8 w-8 items-center justify-center rounded-lg bg-transparent text-sm text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('svg', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"h-3 w-3"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('aria-hidden', cls='na'),
                        Span('=', cls='o'),
                        Span('"true"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('xmlns', cls='na'),
                        Span('=', cls='o'),
                        Span('"http://www.w3.org/2000/svg"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('fill', cls='na'),
                        Span('=', cls='o'),
                        Span('"none"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('viewBox', cls='na'),
                        Span('=', cls='o'),
                        Span('"0 0 14 14"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('path', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke', cls='na'),
                        Span('=', cls='o'),
                        Span('"currentColor"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linecap', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-linejoin', cls='na'),
                        Span('=', cls='o'),
                        Span('"round"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('stroke-width', cls='na'),
                        Span('=', cls='o'),
                        Span('"2"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('d', cls='na'),
                        Span('=', cls='o'),
                        Span('"m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
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
                        Span('<', cls='p'),
                        Span('span', cls='nt'),
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"sr-only"', cls='s'),
                        Span('>', cls='p'),
                        'Close modal',
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
                Span(
                    Span(
                        Span('<!-- Modal body -->', cls='c'),
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
                        Span('"space-y-6 p-6"', cls='s'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('p', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-base leading-relaxed text-gray-500 dark:text-gray-400"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('With less than a month to go before the European Union', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('enacts new consumer privacy laws for its citizens, companies', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('around the world are updating their terms of service', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('agreements to comply.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
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
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"text-base leading-relaxed text-gray-500 dark:text-gray-400"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('The European Unionâ\x80\x99s General Data Protection Regulation', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('(G.D.P.R.) goes into effect on May 25 and is meant to ensure', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('a common set of data rights in the European Union. It', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('requires organizations to notify users as soon as possible', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('of high-risk data breaches that could personally affect', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span('them.', cls='cl'),
                    cls='line'
                ),
                Span(
                    Span(
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
                        Span('div', cls='nt'),
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<!-- Modal footer -->', cls='c'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('div', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"flex items-center space-x-2 rtl:space-x-reverse rounded-b border-t border-gray-200 p-6 dark:border-gray-600"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('<', cls='p'),
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"rounded-lg bg-primary-700 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-primary-800 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('I accept', cls='cl'),
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
                        Span('button', cls='nt'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('type', cls='na'),
                        Span('=', cls='o'),
                        Span('"button"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('class', cls='na'),
                        Span('=', cls='o'),
                        Span('"rounded-lg border border-gray-200 bg-white px-5 py-2.5 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-900 focus:z-10 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:border-gray-500 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"', cls='s'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('>', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span('Decline', cls='cl'),
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
                        Span('div', cls='nt'),
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
        'from Flowbite then you can import the types for the Modal class, parameters and its options.'
    ),
    P('Here’s an example that applies the types from Flowbite to the code above:'),
    Div(
        Pre(
            Code(
                Span(
                    Span(
                        Span('import', cls='kr'),
                        Span('{', cls='p'),
                        Span('Modal', cls='nx'),
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
                        Span('ModalOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('ModalInterface', cls='nx'),
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
                        Span('const', cls='kr'),
                        Span('$modalElement', cls='nx'),
                        Span(':', cls='o'),
                        Span('HTMLElement', cls='nx'),
                        Span('=', cls='o'),
                        Span('document', cls='nb'),
                        Span('.', cls='p'),
                        Span('querySelector', cls='nx'),
                        Span('(', cls='p'),
                        Span("'#modalEl'", cls='s1'),
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
                        Span('modalOptions', cls='nx'),
                        Span(':', cls='o'),
                        Span('ModalOptions', cls='nx'),
                        Span('=', cls='o'),
                        Span('{', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('placement', cls='nx'),
                        Span(':', cls='o'),
                        Span("'bottom-right'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('backdrop', cls='nx'),
                        Span(':', cls='o'),
                        Span("'dynamic'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('backdropClasses', cls='nx'),
                        Span(':', cls='o'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span("'bg-gray-900/50 dark:bg-gray-900/80 fixed inset-0 z-40'", cls='s1'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('closable', cls='nx'),
                        Span(':', cls='o'),
                        Span('true', cls='kc'),
                        Span(',', cls='p'),
                        cls='cl'
                    ),
                    cls='line'
                ),
                Span(
                    Span(
                        Span('onHide', cls='nx'),
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
                        Span("'modal is hidden'", cls='s1'),
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
                        Span('onShow', cls='nx'),
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
                        Span("'modal is shown'", cls='s1'),
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
                        Span('onToggle', cls='nx'),
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
                        Span("'modal has been toggled'", cls='s1'),
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
                        Span("'modalEl'", cls='s1'),
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
                        Span('const', cls='kr'),
                        Span('modal', cls='nx'),
                        Span(':', cls='o'),
                        Span('ModalInterface', cls='nx'),
                        Span('=', cls='o'),
                        Span('new', cls='k'),
                        Span('Modal', cls='nx'),
                        Span('(', cls='p'),
                        Span('$modalElement', cls='nx'),
                        Span(',', cls='p'),
                        Span('modalOptions', cls='nx'),
                        Span(',', cls='p'),
                        Span('instanceOptions', cls='nx'),
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
                        Span('modal', cls='nx'),
                        Span('.', cls='p'),
                        Span('show', cls='nx'),
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
