from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

component = Div(
    P('The chat bubble component is the building block for creating chat interfaces where users can send messages to each other by text, voice notes, images, galleries and other attachments. These components are usually used in chat applications and social media platforms such as Facebook, Twitter/X, WhatsApp, and more.'),
    P('The examples below provide multiple variations of default, outline, and clean styles coded with the utility classes from Tailwind CSS. Some of the components may require you to include the Fastbite JavaScript to enable the dropdowns and tooltips functionality.'),
    H2(
        'Default chat bubble',
        Span(id='default-chat-bubble', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Default chat bubble', href='#default-chat-bubble', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a simple chat bubble with a text message, user profile and a timestamp.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Voice note message',
        Span(id='voice-note-message', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Voice note message', href='#voice-note-message', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a voice note message with control buttons and a dropdown menu.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 12 16',
                        cls='w-4 h-4 text-gray-800 dark:text-white'
                    ),
                    type='button',
                    cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-100 rounded-lg hover:bg-gray-200 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                ),
                Svg(
                    Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                    aria_hidden='true',
                    viewbox='0 0 185 40',
                    fill='none',
                    xmlns='http://www.w3.org/2000/svg',
                    cls='w-[145px] md:w-[185px] md:h-[40px]'
                ),
                Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5 w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='shrink-0 inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Button(
                    Svg(
                        Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='currentColor',
                        viewbox='0 0 12 16',
                        cls='w-4 h-4 text-gray-800 dark:text-white'
                    ),
                    type='button',
                    cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-100 rounded-lg hover:bg-gray-200 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                ),
                Svg(
                    Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                    Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                    Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                    aria_hidden='true',
                    viewbox='0 0 185 40',
                    fill='none',
                    xmlns='http://www.w3.org/2000/svg',
                    cls='w-[145px] md:w-[185px] md:h-[40px]'
                ),
                Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5 w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='shrink-0 inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'File attachment',
        Span(id='file-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: File attachment', href='#file-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to send a file attachment inside a chat bubble with the ability to download the file.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start my-2.5 bg-gray-50 dark:bg-gray-600 rounded-xl p-2'
                ),
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start my-2.5 bg-gray-50 dark:bg-gray-600 rounded-xl p-2'
                ),
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Image attachment',
        Span(id='image-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image attachment', href='#image-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show an image attachment with a download button when hovering over.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse mb-2'
                ),
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                    cls='group relative my-2.5'
                ),
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse mb-2'
                ),
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                    cls='group relative my-2.5'
                ),
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Image gallery',
        Span(id='image-gallery', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Image gallery', href='#image-gallery', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an image gallery based on a grid layout with the ability to download images.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse mb-2'
                ),
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 my-2.5'
                ),
                Div(
                    Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 18',
                            cls='w-3 h-3 me-1.5'
                        ),
                        'Save all',
                        cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                    ),
                    cls='flex justify-between items-center'
                ),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Bonnie Green image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Div(
                    Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                    Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse mb-2'
                ),
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 my-2.5'
                ),
                Div(
                    Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 18',
                            cls='w-3 h-3 me-1.5'
                        ),
                        'Save all',
                        cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                    ),
                    cls='flex justify-between items-center'
                ),
                cls='flex flex-col w-full max-w-[326px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    H2(
        'URL preview sharing',
        Span(id='url-preview-sharing', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: URL preview sharing', href='#url-preview-sharing', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a OG preview of the URL that is being shared inside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            P(
                A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
            ),
            A(
                Img(
                    Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                    Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                    src='https://flowbite.com/docs/images/og-image.png',
                    cls='rounded-lg mb-2'
                ),
                href='#',
                cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            P(
                A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
            ),
            A(
                Img(
                    Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                    Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                    src='https://flowbite.com/docs/images/og-image.png',
                    cls='rounded-lg mb-2'
                ),
                href='#',
                cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_5",cls='mt-2 mb-6'),
    H2(
        'Outline chat bubble',
        Span(id='outline-chat-bubble', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline chat bubble', href='#outline-chat-bubble', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a text message with the user profile and timestamp outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal text-gray-900 dark:text-white'),
                cls='flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1 w-full max-w-[320px]'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal text-gray-900 dark:text-white'),
                cls='flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1 w-full max-w-[320px]'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_6",cls='mt-2 mb-6'),
    H2(
        'Outline voice note',
        Span(id='outline-voice-note', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline voice note', href='#outline-voice-note', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a voice note with the user profile and timestamp outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Button(
                        Svg(
                            Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 12 16',
                            cls='w-4 h-4 text-gray-800 dark:text-white'
                        ),
                        type='button',
                        cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-100 rounded-lg hover:bg-gray-200 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                    ),
                    Svg(
                        Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                        aria_hidden='true',
                        viewbox='0 0 185 40',
                        fill='none',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-[145px] md:w-[185px] md:h-[40px]'
                    ),
                    Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Button(
                        Svg(
                            Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 12 16',
                            cls='w-4 h-4 text-gray-800 dark:text-white'
                        ),
                        type='button',
                        cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-100 rounded-lg hover:bg-gray-200 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                    ),
                    Svg(
                        Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                        aria_hidden='true',
                        viewbox='0 0 185 40',
                        fill='none',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-[145px] md:w-[185px] md:h-[40px]'
                    ),
                    Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_7",cls='mt-2 mb-6'),
    H2(
        'Outline file attachment',
        Span(id='outline-file-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline file attachment', href='#outline-file-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a file attachment with the user profile and timestamp outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start bg-gray-50 dark:bg-gray-600 rounded-xl p-2'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-600 dark:hover:bg-gray-500 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start bg-gray-50 dark:bg-gray-600 rounded-xl p-2'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_8",cls='mt-2 mb-6'),
    H2(
        'Outline image attachment',
        Span(id='outline-image-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline image attachment', href='#outline-image-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to send an image attachment with the user profile outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("I'm working from home today! ð\x9f\x98", cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                    cls='group relative my-2.5'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("I'm working from home today! ð\x9f\x98", cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                    cls='group relative my-2.5'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_9",cls='mt-2 mb-6'),
    H2(
        'Outline image gallery',
        Span(id='outline-image-gallery', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline image gallery', href='#outline-image-gallery', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an image gallery with the user profile and timestamp outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("I'm working from home today! ð\x9f\x98", cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 my-2.5'
                ),
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 18',
                            cls='w-3 h-3 me-1.5'
                        ),
                        'Save all',
                        cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                    ),
                    cls='flex justify-end items-center'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P("I'm working from home today! ð\x9f\x98", cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 my-2.5'
                ),
                Div(
                    Button(
                        Svg(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='none',
                            viewbox='0 0 16 18',
                            cls='w-3 h-3 me-1.5'
                        ),
                        'Save all',
                        cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                    ),
                    cls='flex justify-end items-center'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_10",cls='mt-2 mb-6'),
    H2(
        'Outline URL preview sharing',
        Span(id='outline-url-preview-sharing', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Outline URL preview sharing', href='#outline-url-preview-sharing', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a URL preview with the user profile and timestamp outside the chat bubble.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
                P(
                    A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                    cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
                ),
                A(
                    Img(
                        Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                        Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                        src='https://flowbite.com/docs/images/og-image.png',
                        cls='rounded-lg mb-2'
                    ),
                    href='#',
                    cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
                ),
                cls='flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1 w-full max-w-[320px]'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
                P(
                    A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                    cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
                ),
                A(
                    Img(
                        Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                        Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                        src='https://flowbite.com/docs/images/og-image.png',
                        cls='rounded-lg mb-2'
                    ),
                    href='#',
                    cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
                ),
                cls='flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1 w-full max-w-[320px]'
        ),
        Button(
            Svg(
                Path(d='M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'),
                aria_hidden='true',
                xmlns='http://www.w3.org/2000/svg',
                fill='currentColor',
                viewbox='0 0 4 15',
                cls='w-4 h-4 text-gray-500 dark:text-gray-400'
            ),
            id='dropdownMenuIconButton',
            data_dropdown_toggle='dropdownDots',
            data_dropdown_placement='bottom-start',
            type='button',
            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600'
        ),
        Div(
            Ul(
                Li(
                    A('Reply', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Forward', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Copy', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Report', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                Li(
                    A('Delete', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                ),
                aria_labelledby='dropdownMenuIconButton',
                cls='py-2 text-sm text-gray-700 dark:text-gray-200'
            ),
            id='dropdownDots',
            cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-40 dark:bg-gray-700 dark:divide-gray-600'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_11",cls='mt-2 mb-6'),
    H2(
        'Clean chat bubble',
        Span(id='clean-chat-bubble', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean chat bubble', href='#clean-chat-bubble', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a text message with the user profile and timestamp with a transparent background.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal py-2 text-gray-900 dark:text-white'),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P("That's awesome. I think our users will really appreciate the improvements.", cls='text-sm font-normal py-2 text-gray-900 dark:text-white'),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_12",cls='mt-2 mb-6'),
    H2(
        'Clean voice note',
        Span(id='clean-voice-note', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean voice note', href='#clean-voice-note', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a voice note with a transparent background.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Button(
                        Svg(
                            Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 12 16',
                            cls='w-4 h-4 text-gray-800 dark:text-white'
                        ),
                        type='button',
                        cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                    ),
                    Svg(
                        Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                        aria_hidden='true',
                        viewbox='0 0 185 40',
                        fill='none',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-[145px] md:w-[185px] md:h-[40px]'
                    ),
                    Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 py-2 rounded-e-xl rounded-es-xl'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Button(
                        Svg(
                            Path(d='M3 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm7 0H9a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Z'),
                            aria_hidden='true',
                            xmlns='http://www.w3.org/2000/svg',
                            fill='currentColor',
                            viewbox='0 0 12 16',
                            cls='w-4 h-4 text-gray-800 dark:text-white'
                        ),
                        type='button',
                        cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                    ),
                    Svg(
                        Rect(y='17', width='3', height='6', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='7', y='15.5', width='3', height='9', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='21', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='14', y='6.5', width='3', height='27', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='28', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='35', y='3', width='3', height='34', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='42', y='5.5', width='3', height='29', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='49', y='10', width='3', height='20', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='56', y='13.5', width='3', height='13', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='63', y='16', width='3', height='8', rx='1.5', fill='#6B7280', cls='dark:fill-white'),
                        Rect(x='70', y='12.5', width='3', height='15', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='77', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='84', y='3', width='3', height='34', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='91', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='98', y='0.5', width='3', height='39', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='105', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='112', y='6.5', width='3', height='27', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='119', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='126', y='11.5', width='3', height='17', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='133', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='140', y='2', width='3', height='36', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='147', y='7', width='3', height='26', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='154', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='161', y='9', width='3', height='22', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='168', y='13.5', width='3', height='13', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='175', y='16', width='3', height='8', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='182', y='17.5', width='3', height='5', rx='1.5', fill='#E5E7EB', cls='dark:fill-gray-500'),
                        Rect(x='66', y='16', width='8', height='8', rx='4', fill='#1C64F2'),
                        aria_hidden='true',
                        viewbox='0 0 185 40',
                        fill='none',
                        xmlns='http://www.w3.org/2000/svg',
                        cls='w-[145px] md:w-[185px] md:h-[40px]'
                    ),
                    Span('3:42', cls='inline-flex self-center items-center p-2 text-sm font-medium text-gray-900 dark:text-white'),
                    cls='flex items-center space-x-2 rtl:space-x-reverse'
                ),
                cls='flex flex-col w-full max-w-[320px] leading-1.5 py-2 rounded-e-xl rounded-es-xl'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-1'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_13",cls='mt-2 mb-6'),
    H2(
        'Clean file attachment',
        Span(id='clean-file-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean file attachment', href='#clean-file-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show a file attachment and a download button with a transparent background.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start bg-gray-50 dark:bg-gray-700 rounded-xl p-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                Div(
                    Div(
                        Span(
                            Svg(
                                G(
                                    Path(fill='#E2E5E7', d='M5.024.5c-.688 0-1.25.563-1.25 1.25v17.5c0 .688.562 1.25 1.25 1.25h12.5c.687 0 1.25-.563 1.25-1.25V5.5l-5-5h-8.75z'),
                                    Path(fill='#B0B7BD', d='M15.024 5.5h3.75l-5-5v3.75c0 .688.562 1.25 1.25 1.25z'),
                                    Path(fill='#CAD1D8', d='M18.774 9.25l-3.75-3.75h3.75v3.75z'),
                                    Path(fill='#F15642', d='M16.274 16.75a.627.627 0 01-.625.625H1.899a.627.627 0 01-.625-.625V10.5c0-.344.281-.625.625-.625h13.75c.344 0 .625.281.625.625v6.25z'),
                                    Path(fill='#fff', d='M3.998 12.342c0-.165.13-.345.34-.345h1.154c.65 0 1.235.435 1.235 1.269 0 .79-.585 1.23-1.235 1.23h-.834v.66c0 .22-.14.344-.32.344a.337.337 0 01-.34-.344v-2.814zm.66.284v1.245h.834c.335 0 .6-.295.6-.605 0-.35-.265-.64-.6-.64h-.834zM7.706 15.5c-.165 0-.345-.09-.345-.31v-2.838c0-.18.18-.31.345-.31H8.85c2.284 0 2.234 3.458.045 3.458h-1.19zm.315-2.848v2.239h.83c1.349 0 1.409-2.24 0-2.24h-.83zM11.894 13.486h1.274c.18 0 .36.18.36.355 0 .165-.18.3-.36.3h-1.274v1.049c0 .175-.124.31-.3.31-.22 0-.354-.135-.354-.31v-2.839c0-.18.135-.31.355-.31h1.754c.22 0 .35.13.35.31 0 .16-.13.34-.35.34h-1.455v.795z'),
                                    Path(fill='#CAD1D8', d='M15.649 17.375H3.774V18h11.875a.627.627 0 00.625-.625v-.625a.627.627 0 01-.625.625z'),
                                    clip_path='url(#clip0_3173_1381)'
                                ),
                                fill='none',
                                aria_hidden='true',
                                viewbox='0 0 20 21',
                                cls='w-5 h-5 shrink-0'
                            ),
                            'Fastbite Terms & Conditions',
                            cls='flex items-center gap-2 text-sm font-medium text-gray-900 dark:text-white pb-2'
                        ),
                        Span(
                            '12 Pages',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            '18 MB',
                            Svg(
                                Circle(cx='1.5', cy='2', r='1.5', fill='#6B7280'),
                                xmlns='http://www.w3.org/2000/svg',
                                aria_hidden='true',
                                width='3',
                                height='4',
                                viewbox='0 0 3 4',
                                fill='none',
                                cls='self-center'
                            ),
                            'PDF',
                            cls='flex text-xs font-normal text-gray-500 dark:text-gray-400 gap-2'
                        ),
                        cls='me-2'
                    ),
                    Div(
                        Button(
                            Svg(
                                Path(d='M14.707 7.793a1 1 0 0 0-1.414 0L11 10.086V1.5a1 1 0 0 0-2 0v8.586L6.707 7.793a1 1 0 1 0-1.414 1.414l4 4a1 1 0 0 0 1.416 0l4-4a1 1 0 0 0-.002-1.414Z'),
                                Path(d='M18 12h-2.55l-2.975 2.975a3.5 3.5 0 0 1-4.95 0L4.55 12H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2Zm-3 5a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='currentColor',
                                viewbox='0 0 20 20',
                                cls='w-4 h-4 text-gray-900 dark:text-white'
                            ),
                            type='button',
                            cls='inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-gray-50 rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-600'
                        ),
                        cls='inline-flex self-center items-center'
                    ),
                    cls='flex items-start bg-gray-50 dark:bg-gray-700 rounded-xl p-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_14",cls='mt-2 mb-6'),
    H2(
        'Clean image attachment',
        Span(id='clean-image-attachment', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean image attachment', href='#clean-image-attachment', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show an image and a download button with a transparent background.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                    cls='group relative mt-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Button(
                            Svg(
                                Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                aria_hidden='true',
                                xmlns='http://www.w3.org/2000/svg',
                                fill='none',
                                viewbox='0 0 16 18',
                                cls='w-5 h-5 text-white'
                            ),
                            data_tooltip_target='download-image',
                            cls='inline-flex items-center justify-center rounded-full h-10 w-10 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                        ),
                        Div(
                            'Download image',
                            Div(data_popper_arrow=True, cls='tooltip-arrow'),
                            id='download-image',
                            role='tooltip',
                            cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                        ),
                        cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                    ),
                    Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                    cls='group relative mt-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_15",cls='mt-2 mb-6'),
    H2(
        'Clean image gallery',
        Span(id='clean-image-gallery', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean image gallery', href='#clean-image-gallery', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Use this example to show an image gallery with a transparent background as a chat message.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 mt-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Div(
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 18',
                        cls='w-3 h-3 me-1.5'
                    ),
                    'Save all',
                    cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                ),
                cls='flex justify-between items-center'
            ),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='h-8 w-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            Div(
                P('This is the new office <3', cls='text-sm font-normal text-gray-900 dark:text-white'),
                Div(
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-1',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-1',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-2',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-2',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-2.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Div(
                            Button(
                                Svg(
                                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                                    aria_hidden='true',
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 16 18',
                                    cls='w-4 h-4 text-white'
                                ),
                                data_tooltip_target='download-image-3',
                                cls='inline-flex items-center justify-center rounded-full h-8 w-8 bg-white/30 hover:bg-white/50 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50'
                            ),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image-3',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-3.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    Div(
                        Button(
                            Span('+7', cls='text-xl font-medium text-white'),
                            Div(
                                'Download image',
                                Div(data_popper_arrow=True, cls='tooltip-arrow'),
                                id='download-image',
                                role='tooltip',
                                cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700'
                            ),
                            cls='absolute w-full h-full bg-gray-900/90 hover:bg-gray-900/50 transition-all duration-300 rounded-lg flex items-center justify-center'
                        ),
                        Img(src='/docs/images/blog/image-1.jpg', cls='rounded-lg'),
                        cls='group relative'
                    ),
                    cls='grid gap-4 grid-cols-2 mt-2'
                ),
                cls='leading-1.5 flex w-full max-w-[320px] flex-col'
            ),
            Div(
                Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                Button(
                    Svg(
                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M8 1v11m0 0 4-4m-4 4L4 8m11 4v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3'),
                        aria_hidden='true',
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 16 18',
                        cls='w-3 h-3 me-1.5'
                    ),
                    'Save all',
                    cls='text-sm text-primary-700 dark:text-primary-500 font-medium inline-flex items-center hover:underline'
                ),
                cls='flex justify-between items-center'
            ),
            cls='flex flex-col gap-2.5'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_16",cls='mt-2 mb-6'),
    H2(
        'Clean URL preview sharing',
        Span(id='clean-url-preview-sharing', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Clean URL preview sharing', href='#clean-url-preview-sharing', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('This example can be used to show a URL preview with a transparent background.'),
    component_showcase(Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            P(
                A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
            ),
            A(
                Img(
                    Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                    Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                    src='https://flowbite.com/docs/images/og-image.png',
                    cls='rounded-lg mb-2'
                ),
                href='#',
                cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5'
        ),
        cls='flex items-start gap-2.5'
    )
), code="""Div(
    Div(
        Img(src='/docs/images/people/profile-picture-3.jpg', alt='Jese image', cls='w-8 h-8 rounded-full'),
        Div(
            Div(
                Span('Bonnie Green', cls='text-sm font-semibold text-gray-900 dark:text-white'),
                Span('11:46', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
                cls='flex items-center space-x-2 rtl:space-x-reverse'
            ),
            P('Check out this open-source UI component library based on Tailwind CSS:', cls='text-sm font-normal py-2.5 text-gray-900 dark:text-white'),
            P(
                A('https://github.com/themesberg/flowbite', href='https://github.com/themesberg/flowbite', cls='text-primary-700 dark:text-primary-500 underline hover:no-underline font-medium break-all'),
                cls='text-sm font-normal pb-2.5 text-gray-900 dark:text-white'
            ),
            A(
                Img(
                    Span('GitHub - themesberg/flowbite: The most popular and open source libra ...', cls='text-sm font-medium text-gray-900 dark:text-white mb-2'),
                    Span('github.com', cls='text-xs text-gray-500 dark:text-gray-400 font-normal'),
                    src='https://flowbite.com/docs/images/og-image.png',
                    cls='rounded-lg mb-2'
                ),
                href='#',
                cls='bg-gray-50 dark:bg-gray-600 rounded-xl p-4 mb-2 hover:bg-gray-200 dark:hover:bg-gray-500'
            ),
            Span('Delivered', cls='text-sm font-normal text-gray-500 dark:text-gray-400'),
            cls='flex flex-col w-full max-w-[320px] leading-1.5'
        ),
        cls='flex items-start gap-2.5'
    )
)""", id="example_17",cls='mt-2 mb-6'),
    id='mainContent'
)
