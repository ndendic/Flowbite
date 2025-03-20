from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from utils import component_showcase
from theme_switcher import ThemeSwitcher
from extracted.input_field import component as input_field_component
from extracted.file_input import component as file_input_component
component = Main(id='content-wrapper', cls='flex-auto w-full min-w-0 lg:static lg:max-h-full lg:overflow-visible')(
    Div(cls='flex w-full')(
        Div(cls='flex-auto max-w-4xl min-w-0 pt-6 lg:px-8 lg:pt-8 pb:12 xl:pb-24 lg:pb-16')(
            Div(cls='pb-4 mb-8 border-b border-gray-200 dark:border-gray-800')(
                H1('Tailwind CSS Input Field - Flowbite', id='content', cls='inline-block mb-2 text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white'),
                P('Get started with a collection of input fields built with Tailwind CSS to start accepting data from the user based on multiple sizes, variants, and input types', cls='mb-4 text-lg text-gray-600 dark:text-gray-400')
            ),
            Div(id='mainContent')(
                P('The input field is an important part of the form element that can be used to create interactive controls to accept data from the user based on multiple input types, such as text, email, number, password, URL, phone number, and more.'),
                P('On this page you will find all of the input types based on multiple variants, styles, colors, and sizes built with the utility classes from Tailwind CSS and components from Flowbite.'),
                H2(cls='relative group')(
                    'Input fields',
                    Span(id='input-fields', cls='absolute -top-[140px]'),
                    A('#', href='#input-fields', aria_label='Link to this section: Input fields', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Use this example as a generic form element which includes multiple input fields types such as text, email, password, number, URL, and phone number and use the grid layout to add multiple columns and rows.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='default-input-field-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='default-input-field-example-full-screen-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(536px, 673px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='default-input-field-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='default-input-field-example-tablet-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(579px, 673px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='default-input-field-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='default-input-field-example-mobile-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(619px, 673px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='default-input-field-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='default-input-field-example-toggle-rtl', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(919px, 673px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='default-input-field-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='default-input-field-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(965px, 673px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='default-input-field-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='default input field example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<form>\r\n    <div class="grid gap-6 mb-6 md:grid-cols-2">\r\n        <div>\r\n            <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>\r\n            <input type="text" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required />\r\n        </div>\r\n        <div>\r\n            <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>\r\n            <input type="text" id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required />\r\n        </div>\r\n        <div>\r\n            <label for="company" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Company</label>\r\n            <input type="text" id="company" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Flowbite" required />\r\n        </div>  \r\n        <div>\r\n            <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone number</label>\r\n            <input type="tel" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required />\r\n        </div>\r\n        <div>\r\n            <label for="website" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Website URL</label>\r\n            <input type="url" id="website" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="flowbite.com" required />\r\n        </div>\r\n        <div>\r\n            <label for="visitors" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Unique visitors (per month)</label>\r\n            <input type="number" id="visitors" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required />\r\n        </div>\r\n    </div>\r\n    <div class="mb-6">\r\n        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>\r\n        <input type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="john.doe@company.com" required />\r\n    </div> \r\n    <div class="mb-6">\r\n        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>\r\n        <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required />\r\n    </div> \r\n    <div class="mb-6">\r\n        <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>\r\n        <input type="password" id="confirm_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required />\r\n    </div> \r\n    <div class="flex items-start mb-6">\r\n        <div class="flex items-center h-5">\r\n        <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required />\r\n        </div>\r\n        <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree with the <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>\r\n    </div>\r\n    <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>\r\n</form>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 688px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='default-input-field-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='default-input-field-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<form>\r\n    <div class="grid gap-6 mb-6 md:grid-cols-2">\r\n        <div>\r\n            <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>\r\n            <input type="text" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required />\r\n        </div>\r\n        <div>\r\n            <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>\r\n            <input type="text" id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required />\r\n        </div>\r\n        <div>\r\n            <label for="company" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Company</label>\r\n            <input type="text" id="company" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Flowbite" required />\r\n        </div>  \r\n        <div>\r\n            <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone number</label>\r\n            <input type="tel" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required />\r\n        </div>\r\n        <div>\r\n            <label for="website" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Website URL</label>\r\n            <input type="url" id="website" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="flowbite.com" required />\r\n        </div>\r\n        <div>\r\n            <label for="visitors" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Unique visitors (per month)</label>\r\n            <input type="number" id="visitors" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required />\r\n        </div>\r\n    </div>\r\n    <div class="mb-6">\r\n        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>\r\n        <input type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="john.doe@company.com" required />\r\n    </div> \r\n    <div class="mb-6">\r\n        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>\r\n        <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required />\r\n    </div> \r\n    <div class="mb-6">\r\n        <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>\r\n        <input type="password" id="confirm_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required />\r\n    </div> \r\n    <div class="flex items-start mb-6">\r\n        <div class="flex items-center h-5">\r\n        <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required />\r\n        </div>\r\n        <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree with the <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>\r\n    </div>\r\n    <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>\r\n</form>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Form(
                                            Div(cls='grid gap-6 mb-6 md:grid-cols-2')(
                                                Div(
                                                    Label('First name', fr='first_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='text', id='first_name', placeholder='John', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                ),
                                                Div(
                                                    Label('Last name', fr='last_name', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='text', id='last_name', placeholder='Doe', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                ),
                                                Div(
                                                    Label('Company', fr='company', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='text', id='company', placeholder='Flowbite', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                ),
                                                Div(
                                                    Label('Phone number', fr='phone', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='tel', id='phone', placeholder='123-45-678', pattern='[0-9]{3}-[0-9]{2}-[0-9]{3}', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                ),
                                                Div(
                                                    Label('Website URL', fr='website', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='url', id='website', placeholder='flowbite.com', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                ),
                                                Div(
                                                    Label('Unique visitors (per month)', fr='visitors', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                    Input(type='number', id='visitors', placeholder='', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                                )
                                            ),
                                            Div(cls='mb-6')(
                                                Label('Email address', fr='email', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                Input(type='email', id='email', placeholder='john.doe@company.com', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                            ),
                                            Div(cls='mb-6')(
                                                Label('Password', fr='password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                Input(type='password', id='password', placeholder='•••••••••', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                            ),
                                            Div(cls='mb-6')(
                                                Label('Confirm password', fr='confirm_password', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                                Input(type='password', id='confirm_password', placeholder='•••••••••', required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                            ),
                                            Div(cls='flex items-start mb-6')(
                                                Div(cls='flex items-center h-5')(
                                                    Input(id='remember', type='checkbox', value='', required='', cls='w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800')
                                                ),
                                                Label(fr='remember', cls='ms-2 text-sm font-medium text-gray-900 dark:text-gray-300')(
                                                    'I agree with the',
                                                    A('terms and conditions', href='#', cls='text-blue-600 hover:underline dark:text-blue-500'),
                                                    '.'
                                                )
                                            ),
                                            Button('Submit', type='submit', cls='text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800')
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'grid gap-6 mb-6 md:grid-cols-2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'first_name',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'First name',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'first_name',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'John',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'last_name',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Last name',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'last_name',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Doe',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'company',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Company',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'company',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Flowbite',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'phone',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Phone number',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'tel',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'phone',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '123-45-678',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('pattern', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '[0-9]{3}-[0-9]{2}-[0-9]{3}',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'website',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Website URL',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'url',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'website',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'flowbite.com',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'visitors',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Unique visitors (per month)',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'number',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'visitors',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'email',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Email address',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'email',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'email',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'john.doe@company.com',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Password',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '•••••••••',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'confirm_password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Confirm password',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'confirm_password',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '•••••••••',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'flex items-start mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'flex items-center h-5',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'remember',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'checkbox',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('value', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'remember',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'ms-2 text-sm font-medium text-gray-900 dark:text-gray-300',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'I agree with the',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text-blue-600 hover:underline dark:text-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'terms and conditions',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    '.',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'submit',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Submit',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Input sizes',
                    Span(id='input-sizes', cls='absolute -top-[140px]'),
                    A('#', href='#input-sizes', aria_label='Link to this section: Input sizes', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Use the following examples to apply a small, default or large size for the input fields.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-sizes-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-sizes-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 903px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-sizes-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-sizes-example-tablet-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 903px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-sizes-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-sizes-example-mobile-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 903px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-sizes-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-sizes-example-toggle-rtl', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 903px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-sizes-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-sizes-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 903px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-sizes-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field sizes example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<div class="mb-6">\r\n    <label for="large-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Large input</label>\r\n    <input type="text" id="large-input" class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n<div class="mb-6">\r\n    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Default input</label>\r\n    <input type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n<div>\r\n    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Small input</label>\r\n    <input type="text" id="small-input" class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 306px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-sizes-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-sizes-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_escaped='', data_popper_reference_hidden='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<div class="mb-6">\r\n    <label for="large-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Large input</label>\r\n    <input type="text" id="large-input" class="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n<div class="mb-6">\r\n    <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Default input</label>\r\n    <input type="text" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n<div>\r\n    <label for="small-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Small input</label>\r\n    <input type="text" id="small-input" class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">\r\n</div>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Div(cls='mb-6')(
                                            Label('Large input', fr='large-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                            Input(type='text', id='large-input', cls='block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                        ),
                                        Div(cls='mb-6')(
                                            Label('Default input', fr='default-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                            Input(type='text', id='default-input', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                        ),
                                        Div(
                                            Label('Small input', fr='small-input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                            Input(type='text', id='small-input', cls='block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'large-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Large input',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'large-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'default-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Default input',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'default-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'small-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Small input',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'small-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Disabled state',
                    Span(id='disabled-state', cls='absolute -top-[140px]'),
                    A('#', href='#disabled-state', aria_label='Link to this section: Disabled state', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Get started with this example if you want to apply the disabled state to an input field.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-disabled-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-disabled-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 1757px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-disabled-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-disabled-example-tablet-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 1757px);', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-disabled-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-disabled-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 1757px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-disabled-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-disabled-example-toggle-rtl', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 1757px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-disabled-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-disabled-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 1757px);', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-disabled-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field disabled example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<input type="text" id="disabled-input" aria-label="disabled input" class="mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Disabled input" disabled>\r\n<input type="text" id="disabled-input-2" aria-label="disabled input 2" class="bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Disabled readonly input" disabled readonly>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 148px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-disabled-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-disabled-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_escaped='', data_popper_reference_hidden='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<input type="text" id="disabled-input" aria-label="disabled input" class="mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Disabled input" disabled>\r\n<input type="text" id="disabled-input-2" aria-label="disabled input 2" class="bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500" value="Disabled readonly input" disabled readonly>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Input(type='text', id='disabled-input', aria_label='disabled input', value='Disabled input', disabled='', cls='mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500'),
                                        Input(type='text', id='disabled-input-2', aria_label='disabled input 2', value='Disabled readonly input', disabled='', readonly='', cls='bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'disabled-input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-label', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'disabled input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6 bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('value', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Disabled input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('disabled', cls='token attr-name'),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'disabled-input-2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-label', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'disabled input 2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('value', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Disabled readonly input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('disabled', cls='token attr-name'),
                                                        Span('readonly', cls='token attr-name'),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='hidden absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Validation',
                    Span(id='validation', cls='absolute -top-[140px]'),
                    A('#', href='#validation', aria_label='Link to this section: Validation', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Use the following example to apply validation styles for success and error messages.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-validation-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-validation-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 2270px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-validation-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-validation-example-tablet-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 2270px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-validation-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-validation-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 2270px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-validation-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-validation-example-toggle-rtl', role='tooltip', data_popper_placement='top', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 2270px);', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-validation-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-validation-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 2270px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-validation-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field validation example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<div class="mb-6">\r\n  <label for="success" class="block mb-2 text-sm font-medium text-green-700 dark:text-green-500">Your name</label>\r\n  <input type="text" id="success" class="bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500" placeholder="Success input">\r\n  <p class="mt-2 text-sm text-green-600 dark:text-green-500"><span class="font-medium">Well done!</span> Some success message.</p>\r\n</div>\r\n<div>\r\n  <label for="error" class="block mb-2 text-sm font-medium text-red-700 dark:text-red-500">Your name</label>\r\n  <input type="text" id="error" class="bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500" placeholder="Error input">\r\n  <p class="mt-2 text-sm text-red-600 dark:text-red-500"><span class="font-medium">Oh, snapp!</span> Some error message.</p>\r\n</div>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 260px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-validation-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-validation-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<div class="mb-6">\r\n  <label for="success" class="block mb-2 text-sm font-medium text-green-700 dark:text-green-500">Your name</label>\r\n  <input type="text" id="success" class="bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500" placeholder="Success input">\r\n  <p class="mt-2 text-sm text-green-600 dark:text-green-500"><span class="font-medium">Well done!</span> Some success message.</p>\r\n</div>\r\n<div>\r\n  <label for="error" class="block mb-2 text-sm font-medium text-red-700 dark:text-red-500">Your name</label>\r\n  <input type="text" id="error" class="bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500" placeholder="Error input">\r\n  <p class="mt-2 text-sm text-red-600 dark:text-red-500"><span class="font-medium">Oh, snapp!</span> Some error message.</p>\r\n</div>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Div(cls='mb-6')(
                                            Label('Your name', fr='success', cls='block mb-2 text-sm font-medium text-green-700 dark:text-green-500'),
                                            Input(type='text', id='success', placeholder='Success input', cls='bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500'),
                                            P(cls='mt-2 text-sm text-green-600 dark:text-green-500')(
                                                Span('Well done!', cls='font-medium'),
                                                'Some success message.'
                                            )
                                        ),
                                        Div(
                                            Label('Your name', fr='error', cls='block mb-2 text-sm font-medium text-red-700 dark:text-red-500'),
                                            Input(type='text', id='error', placeholder='Error input', cls='bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500'),
                                            P(cls='mt-2 text-sm text-red-600 dark:text-red-500')(
                                                Span('Oh, snapp!', cls='font-medium'),
                                                'Some error message.'
                                            )
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'success',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-green-700 dark:text-green-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Your name',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'success',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-green-50 border border-green-500 text-green-900 dark:text-green-400 placeholder-green-700 dark:placeholder-green-500 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-green-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Success input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mt-2 text-sm text-green-600 dark:text-green-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'font-medium',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Well done!',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Some success message.',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'error',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-red-700 dark:text-red-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Your name',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'error',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-red-50 border border-red-500 text-red-900 placeholder-red-700 text-sm rounded-lg focus:ring-red-500 dark:bg-gray-700 focus:border-red-500 block w-full p-2.5 dark:text-red-500 dark:placeholder-red-500 dark:border-red-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Error input',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mt-2 text-sm text-red-600 dark:text-red-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'font-medium',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Oh, snapp!',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Some error message.',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Input group',
                    Span(id='input-group', cls='absolute -top-[140px]'),
                    A('#', href='#input-group', aria_label='Link to this section: Input group', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('This example can be used to add a descriptive icon or additional text inside the input field.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-group-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-group-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 3063px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-group-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-group-example-tablet-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 3063px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-group-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-group-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 3063px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-group-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-group-example-toggle-rtl', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 3063px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-group-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-group-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 3063px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-group-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field group example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<label for="input-group-1" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Email</label>\r\n<div class="relative mb-6">\r\n  <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">\r\n    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 16">\r\n        <path d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"/>\r\n        <path d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"/>\r\n    </svg>\r\n  </div>\r\n  <input type="text" id="input-group-1" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">\r\n</div>\r\n<label for="website-admin" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Username</label>\r\n<div class="flex">\r\n  <span class="inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600">\r\n    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">\r\n        <path d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z"/>\r\n    </svg>\r\n  </span>\r\n  <input type="text" id="website-admin" class="rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="elonmusk">\r\n</div>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 204px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-group-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-group-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_escaped='', data_popper_reference_hidden='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<label for="input-group-1" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Email</label>\r\n<div class="relative mb-6">\r\n  <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">\r\n    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 16">\r\n        <path d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"/>\r\n        <path d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"/>\r\n    </svg>\r\n  </div>\r\n  <input type="text" id="input-group-1" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">\r\n</div>\r\n<label for="website-admin" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Username</label>\r\n<div class="flex">\r\n  <span class="inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600">\r\n    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">\r\n        <path d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z"/>\r\n    </svg>\r\n  </span>\r\n  <input type="text" id="website-admin" class="rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="elonmusk">\r\n</div>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Label('Your Email', fr='input-group-1', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                        Div(cls='relative mb-6')(
                                            Div(cls='absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none')(
                                                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 16', cls='w-4 h-4 text-gray-500 dark:text-gray-400')(
                                                    Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
                                                    Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z')
                                                )
                                            ),
                                            Input(type='text', id='input-group-1', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                        ),
                                        Label('Username', fr='website-admin', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                        Div(cls='flex')(
                                            Span(cls='inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600')(
                                                Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-4 h-4 text-gray-500 dark:text-gray-400')(
                                                    Path(d='M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z')
                                                )
                                            ),
                                            Input(type='text', id='website-admin', placeholder='elonmusk', cls='rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'input-group-1',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Your Email',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'relative mb-6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-4 h-4 text-gray-500 dark:text-gray-400',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-hidden', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'true',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('xmlns', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'http://www.w3.org/2000/svg',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('fill', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'currentColor',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('viewBox', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '0 0 20 16',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'm10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'input-group-1',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'name@flowbite.com',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'website-admin',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Username',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'flex',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'inline-flex items-center px-3 text-sm text-gray-900 bg-gray-200 border rounded-e-0 border-gray-300 border-e-0 rounded-s-md dark:bg-gray-600 dark:text-gray-400 dark:border-gray-600',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-4 h-4 text-gray-500 dark:text-gray-400',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-hidden', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'true',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('xmlns', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'http://www.w3.org/2000/svg',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('fill', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'currentColor',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('viewBox', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '0 0 20 20',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'span'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'website-admin',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'elonmusk',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Helper text',
                    Span(id='helper-text', cls='absolute -top-[140px]'),
                    A('#', href='#helper-text', aria_label='Link to this section: Helper text', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Use this example to show a helper text below the input field for additional explanation and links.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-helper-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-helper-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 3815px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-helper-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-helper-example-tablet-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 3815px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-helper-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-helper-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 3815px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-helper-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-helper-example-toggle-rtl', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 3815px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-helper-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-helper-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 3815px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-helper-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field helper example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<label for="helper-text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>\r\n<input type="email" id="helper-text" aria-describedby="helper-text-explanation" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">\r\n<p id="helper-text-explanation" class="mt-2 text-sm text-gray-500 dark:text-gray-400">We’ll never share your details. Read our <a href="#" class="font-medium text-blue-600 hover:underline dark:text-blue-500">Privacy Policy</a>.</p>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 138px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-helper-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-helper-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs tooltip dark:bg-gray-700 opacity-0 invisible')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<label for="helper-text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>\r\n<input type="email" id="helper-text" aria-describedby="helper-text-explanation" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">\r\n<p id="helper-text-explanation" class="mt-2 text-sm text-gray-500 dark:text-gray-400">We’ll never share your details. Read our <a href="#" class="font-medium text-blue-600 hover:underline dark:text-blue-500">Privacy Policy</a>.</p>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Label('Your email', fr='helper-text', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
                                        Input(type='email', id='helper-text', aria_describedby='helper-text-explanation', placeholder='name@flowbite.com', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'),
                                        P(id='helper-text-explanation', cls='mt-2 text-sm text-gray-500 dark:text-gray-400')(
                                            'We’ll never share your details. Read our',
                                            A('Privacy Policy', href='#', cls='font-medium text-blue-600 hover:underline dark:text-blue-500'),
                                            '.'
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'helper-text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block mb-2 text-sm font-medium text-gray-900 dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Your email',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'email',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'helper-text',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-describedby', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'helper-text-explanation',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'name@flowbite.com',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'helper-text-explanation',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mt-2 text-sm text-gray-500 dark:text-gray-400',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'We’ll never share your details. Read our',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'font-medium text-blue-600 hover:underline dark:text-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Privacy Policy',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    '.',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'p'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='hidden absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Search input',
                    Span(id='search-input', cls='absolute -top-[140px]'),
                    A('#', href='#search-input', aria_label='Link to this section: Search input', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Get started with this example where the submit button is positioned inside the input field.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-search-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-search-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 4339px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-search-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-search-example-tablet-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 4339px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-search-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-search-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 4339px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-search-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-search-example-toggle-rtl', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 4339px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-search-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-search-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 4339px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-search-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field search example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body  class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<form>   \r\n    <label for="search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>\r\n    <div class="relative">\r\n        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">\r\n            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">\r\n                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>\r\n            </svg>\r\n        </div>\r\n        <input type="search" id="search" class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search" required />\r\n        <button type="submit" class="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>\r\n    </div>\r\n</form>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 94px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-search-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-search-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<form>   \r\n    <label for="search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>\r\n    <div class="relative">\r\n        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">\r\n            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">\r\n                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>\r\n            </svg>\r\n        </div>\r\n        <input type="search" id="search" class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search" required />\r\n        <button type="submit" class="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>\r\n    </div>\r\n</form>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Form(
                                            Label('Search', fr='search', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                                            Div(cls='relative')(
                                                Div(cls='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none')(
                                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-4 h-4 text-gray-500 dark:text-gray-400')(
                                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z')
                                                    )
                                                ),
                                                Input(type='search', id='search', placeholder='Search', required='', cls='block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'),
                                                Button('Search', type='submit', cls='text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800')
                                            )
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Search',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'relative',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-4 h-4 text-gray-500 dark:text-gray-400',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-hidden', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'true',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('xmlns', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'http://www.w3.org/2000/svg',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('fill', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'none',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('viewBox', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '0 0 20 20',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('stroke', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'currentColor',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linecap', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linejoin', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-width', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'm19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'submit',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Search',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                Div(cls='mt-8 -mb-5')(
                    A(href='/docs/getting-started/quickstart/', aria_label='Component requires Flowbite JavaScript', cls='inline-flex items-center justify-between px-1 py-1 pr-4 text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700')(
                        Span(aria_hidden='true', cls='text-xs bg-blue-600 rounded-full text-white px-3 py-1.5 mr-3')(
                            Svg(fill='none', stroke='currentColor', viewbox='0 0 24 24', xmlns='http://www.w3.org/2000/svg', cls='w-4 h-4')(
                                Path(stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z')
                            )
                        ),
                        Span('Requires Flowbite JS', cls='text-sm font-medium'),
                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 6 10', cls='w-2.5 h-2.5 ml-2.5')(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 9 4-4-4-4')
                        )
                    )
                ),
                H2(cls='relative group')(
                    'Dropdown input',
                    Span(id='dropdown-input', cls='absolute -top-[140px]'),
                    A('#', href='#dropdown-input', aria_label='Link to this section: Dropdown input', cls='ml-2 text-blue-700 opacity-0 transition-opacity dark:text-blue-500 group-hover:opacity-100')
                ),
                P('Use this example to show a dropdown menu right next to the input field.'),
                Div(cls='mt-8 code-example')(
                    Div(cls='w-full p-4 border border-gray-200 bg-gray-50 rounded-t-xl dark:border-gray-600 dark:bg-gray-700')(
                        Div(cls='grid grid-cols-3')(
                            Div(cls='col-span-2 sm:col-span-1')(
                                A(href='https://github.com/themesberg/flowbite/blob/main/content/forms/input-field.md', rel='noopener nofollow noreferrer', cls='inline-flex items-center justify-center h-9 mr-3 px-3 text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5 mr-2')(
                                        Path(fill_rule='evenodd', d='M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z', clip_rule='evenodd')
                                    ),
                                    'Edit on GitHub'
                                )
                            ),
                            Div(cls='items-center justify-center hidden col-span-1 space-x-2 sm:flex')(
                                Button(data_tooltip_target='input-field-dropdown-example-full-screen-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-full-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle full view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M10 14v4m-4 1h8M1 10h18M2 1h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-dropdown-example-full-screen-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(536px, 5031px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle full screen',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-dropdown-example-tablet-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-tablet-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle tablet view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 18 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M7.5 16.5h3M2 1h14a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-dropdown-example-tablet-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(579px, 5031px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle tablet view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(69px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-dropdown-example-mobile-tooltip', cls='flex items-center justify-center w-9 h-9 text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-mobile-view hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Span('Toggle mobile view', cls='sr-only'),
                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 20', cls='w-3.5 h-3.5')(
                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 14h12M1 4h12M6.5 16.5h1M2 1h10a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z')
                                    )
                                ),
                                Div(id='input-field-dropdown-example-mobile-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(619px, 5031px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    'Toggle mobile view',
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(73px, 0px);', cls='tooltip-arrow')
                                )
                            ),
                            Div(cls='flex justify-end col-span-1')(
                                Button('RTL', data_tooltip_target='input-field-dropdown-example-toggle-rtl', data_toggle_direction='ltr', type='button', cls='toggle-rtl flex items-center w-9 h-9 mr-3 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700'),
                                Div(id='input-field-dropdown-example-toggle-rtl', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(919px, 5031px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle RTL mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(67px, 0px);', cls='tooltip-arrow')
                                ),
                                Button(data_tooltip_target='input-field-dropdown-example-toggle-dark-mode-tooltip', type='button', data_toggle_dark='dark', cls='flex items-center w-9 h-9 justify-center text-xs font-medium text-gray-700 bg-white border border-gray-200 rounded-lg toggle-dark-state-example hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-gray-300 dark:focus:ring-gray-500 dark:bg-gray-800 focus:outline-none dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')(
                                    Svg(data_toggle_icon='moon', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 hidden')(
                                        Path(d='M17.8 13.75a1 1 0 0 0-.859-.5A7.488 7.488 0 0 1 10.52 2a1 1 0 0 0 0-.969A1.035 1.035 0 0 0 9.687.5h-.113a9.5 9.5 0 1 0 8.222 14.247 1 1 0 0 0 .004-.997Z')
                                    ),
                                    Svg(data_toggle_icon='sun', aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 20', cls='w-3.5 h-3.5')(
                                        Path(d='M10 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0-11a1 1 0 0 0 1-1V1a1 1 0 0 0-2 0v2a1 1 0 0 0 1 1Zm0 12a1 1 0 0 0-1 1v2a1 1 0 1 0 2 0v-2a1 1 0 0 0-1-1ZM4.343 5.757a1 1 0 0 0 1.414-1.414L4.343 2.929a1 1 0 0 0-1.414 1.414l1.414 1.414Zm11.314 8.486a1 1 0 0 0-1.414 1.414l1.414 1.414a1 1 0 0 0 1.414-1.414l-1.414-1.414ZM4 10a1 1 0 0 0-1-1H1a1 1 0 0 0 0 2h2a1 1 0 0 0 1-1Zm15-1h-2a1 1 0 1 0 0 2h2a1 1 0 0 0 0-2ZM4.343 14.243l-1.414 1.414a1 1 0 1 0 1.414 1.414l1.414-1.414a1 1 0 0 0-1.414-1.414ZM14.95 6.05a1 1 0 0 0 .707-.293l1.414-1.414a1 1 0 1 0-1.414-1.414l-1.414 1.414a1 1 0 0 0 .707 1.707Z')
                                    ),
                                    Span('Toggle dark/light mode', cls='sr-only')
                                ),
                                Div(id='input-field-dropdown-example-toggle-dark-mode-tooltip', role='tooltip', data_popper_placement='top', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate(965px, 5031px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                    Span('Toggle light mode', cls='tooltip-text'),
                                    Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(68px, 0px);', cls='tooltip-arrow')
                                )
                            )
                        )
                    ),
                    Div(cls='code-preview-wrapper')(
                        Div(id='input-field-dropdown-example', cls='flex p-0 bg-white border-gray-200 bg-gradient-to-r code-preview dark:bg-gray-900 border-x dark:border-gray-600')(
                            Div(cls='w-full code-responsive-wrapper')(
                                Iframe(title='input field dropdown example', srcdoc='<!DOCTYPE html><html lang=\'en\'><head><meta charset=\'UTF-8\'><meta name=\'viewport\' content=\'width=device-width, initial-scale=1.0\'><link rel=\'preconnect\' href=\'https://fonts.googleapis.com\'><link rel=\'preconnect\' href=\'https://fonts.gstatic.com\' crossorigin><link href=\'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap\' rel=\'stylesheet\'><link rel=\'stylesheet\' href=\'https://flowbite.com/docs/main.css?v=3.1.2a\'></head><body style=\'height: 250px\' class=\'p-5 bg-white dark:bg-gray-900 antialiased \'><div id=\'exampleWrapper\' class=\'\'>\r\n<form>\r\n    <div class="flex">\r\n        <label for="search-dropdown" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Your Email</label>\r\n        <button id="dropdown-button" data-dropdown-toggle="dropdown" class="shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800" type="button">All categories <svg class="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">\r\n    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>\r\n  </svg></button>\r\n        <div id="dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700">\r\n            <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdown-button">\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Shopping</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Images</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">News</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Finance</a>\r\n            </li>\r\n            </ul>\r\n        </div>\r\n        <div class="relative w-full">\r\n            <input type="search" id="search-dropdown" class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500" placeholder="Search" required />\r\n            <button type="submit" class="absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"><svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">\r\n    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>\r\n  </svg></button>\r\n        </div>\r\n    </div>\r\n</form>\r\n</div><script src=\'https://flowbite.com/docs/flowbite.min.js\'></script><script>window.onload = function () { const anchorTags = document.querySelectorAll(\'a\'); anchorTags.forEach(function(a){a.addEventListener(\'click\', function(ev){ev.preventDefault();})});  const dropdownEl = document.querySelector(\'[data-dropdown-toggle]\'); if (dropdownEl) {dropdownEl.click();} const modalEl = document.querySelector(\'[data-modal-toggle]\'); if(modalEl) {modalEl.click(); }  const dateRangePickerEl = document.querySelector(\'[data-rangepicker] input\'); if (dateRangePickerEl) { dateRangePickerEl.focus(); } const drawerEl = document.querySelector(\'[data-drawer-show]\'); if (drawerEl) { drawerEl.click(); }  }</script></body></html>', frameborder='0', style='height: 250px;', cls='w-full h-0 mx-auto bg-white dark:bg-gray-900 iframe-code'),
                                Div(data_component_loader='', cls='flex items-center justify-center w-full p-5 bg-white dark:bg-gray-900 hidden')(
                                    Div(role='status')(
                                        Svg(aria_hidden='true', viewbox='0 0 100 101', fill='none', xmlns='http://www.w3.org/2000/svg', cls='w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600')(
                                            Path(d='M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z', fill='currentColor'),
                                            Path(d='M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z', fill='currentFill')
                                        ),
                                        Span('Loading...', cls='sr-only')
                                    )
                                )
                            )
                        )
                    ),
                    Div(cls='code-syntax-wrapper')(
                        Div(cls='relative border-gray-200 border-y border-x code-syntax dark:border-gray-600')(
                            Div(cls='grid w-full grid-cols-2 border-b border-gray-200 bg-gray-50 rounded-t-md dark:bg-gray-700 dark:border-gray-600')(
                                Ul(cls='flex text-sm font-medium text-center text-gray-500 dark:text-gray-400')(
                                    Li(
                                        Button('HTML', type='button', data_toggle_html_code='', cls='inline-block w-full p-2 px-3 text-gray-800 bg-gray-100 hover:bg-gray-200 dark:hover:bg-gray-700 border-r border-gray-200 dark:text-white dark:bg-gray-800 dark:border-gray-600')
                                    )
                                ),
                                Div(cls='flex justify-end')(
                                    Button(data_tooltip_target='input-field-dropdown-example-copy-clipboard-tooltip', data_clipboard_content_type='html', data_tooltip_placement='bottom', type='button', data_copy_state='copy', cls='flex items-center px-3 py-2 text-xs font-medium text-gray-600 bg-gray-100 border-l border-gray-200 dark:border-gray-600 dark:text-gray-400 dark:bg-gray-800 hover:text-blue-700 dark:hover:text-white copy-to-clipboard-button')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 18 20', cls='w-3.5 h-3.5 mr-2')(
                                            Path(d='M5 9V4.13a2.96 2.96 0 0 0-1.293.749L.879 7.707A2.96 2.96 0 0 0 .13 9H5Zm11.066-9H9.829a2.98 2.98 0 0 0-2.122.879L7 1.584A.987.987 0 0 0 6.766 2h4.3A3.972 3.972 0 0 1 15 6v10h1.066A1.97 1.97 0 0 0 18 14V2a1.97 1.97 0 0 0-1.934-2Z'),
                                            Path(d='M11.066 4H7v5a2 2 0 0 1-2 2H0v7a1.969 1.969 0 0 0 1.933 2h9.133A1.97 1.97 0 0 0 13 18V6a1.97 1.97 0 0 0-1.934-2Z')
                                        ),
                                        Span('Copy', cls='copy-text')
                                    ),
                                    Div(id='input-field-dropdown-example-copy-clipboard-tooltip', role='tooltip', data_popper_placement='bottom', data_popper_reference_hidden='', data_popper_escaped='', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(688px, 44px);', cls='absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-xs opacity-0 tooltip dark:bg-gray-700')(
                                        'Copy to clipboard',
                                        Div(data_popper_arrow='', style='position: absolute; left: 0px; transform: translate(100px, 0px);', cls='tooltip-arrow')
                                    ),
                                    Div(data_clipboard_content_html='\r\n<form>\r\n    <div class="flex">\r\n        <label for="search-dropdown" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Your Email</label>\r\n        <button id="dropdown-button" data-dropdown-toggle="dropdown" class="shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800" type="button">All categories <svg class="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">\r\n    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>\r\n  </svg></button>\r\n        <div id="dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700">\r\n            <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdown-button">\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Shopping</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Images</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">News</a>\r\n            </li>\r\n            <li>\r\n                <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Finance</a>\r\n            </li>\r\n            </ul>\r\n        </div>\r\n        <div class="relative w-full">\r\n            <input type="search" id="search-dropdown" class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500" placeholder="Search" required />\r\n            <button type="submit" class="absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"><svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">\r\n    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>\r\n  </svg></button>\r\n        </div>\r\n    </div>\r\n</form>\r\n', data_clipboard_content_javascript='', cls='hidden')(
                                        Form(
                                            Div(cls='flex')(
                                                Label('Your Email', fr='search-dropdown', cls='mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white'),
                                                Button(id='dropdown-button', data_dropdown_toggle='dropdown', type='button', cls='shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800')(
                                                    'All categories',
                                                    Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 10 6', cls='w-2.5 h-2.5 ms-2.5')(
                                                        Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m1 1 4 4 4-4')
                                                    )
                                                ),
                                                Div(id='dropdown', data_popper_reference_hidden='', data_popper_escaped='', data_popper_placement='bottom', style='position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(0px, 1010px);', cls='z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700')(
                                                    Ul(aria_labelledby='dropdown-button', cls='py-2 text-sm text-gray-700 dark:text-gray-200')(
                                                        Li(
                                                            A('Shopping', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                                        ),
                                                        Li(
                                                            A('Images', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                                        ),
                                                        Li(
                                                            A('News', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                                        ),
                                                        Li(
                                                            A('Finance', href='#', cls='block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white')
                                                        )
                                                    )
                                                ),
                                                Div(cls='relative w-full')(
                                                    Input(type='search', id='search-dropdown', placeholder='Search', required='', cls='block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500'),
                                                    Button(type='submit', cls='absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800')(
                                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 20 20', cls='w-4 h-4')(
                                                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z')
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            ),
                            Div(cls='relative')(
                                Div(data_code_wrapper='', tabindex='-1', cls='overflow-hidden max-h-72')(
                                    Div(data_code_wrapper_html='')(
                                        Div(cls='highlight')(
                                            Pre(tabindex='0', cls='chroma language-html')(
                                                Code(data_lang='html', cls='language-html')(
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'flex',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('for', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search-dropdown',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Your Email',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'label'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'dropdown-button',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('data-dropdown-toggle', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'dropdown',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'button',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'All categories',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-2.5 h-2.5 ms-2.5',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-hidden', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'true',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('xmlns', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'http://www.w3.org/2000/svg',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('fill', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'none',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('viewBox', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '0 0 10 6',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('stroke', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'currentColor',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linecap', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linejoin', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-width', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'm1 1 4 4 4-4',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'dropdown',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow-sm w-44 dark:bg-gray-700',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'ul'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'py-2 text-sm text-gray-700 dark:text-gray-200',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-labelledby', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'dropdown-button',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Shopping',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Images',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'News',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('href', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '#',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    'Finance',
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'a'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'li'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'ul'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'relative w-full',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'input'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('id', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'search-dropdown',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-e-lg rounded-s-gray-100 rounded-s-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('placeholder', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'Search',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('required', cls='token attr-name'),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('type', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'submit',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-blue-700 rounded-e-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('class', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'w-4 h-4',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('aria-hidden', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'true',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('xmlns', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'http://www.w3.org/2000/svg',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('fill', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'none',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('viewBox', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '0 0 20 20',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('<', cls='token punctuation'),
                                                            'path'
                                                        ),
                                                        Span('stroke', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'currentColor',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linecap', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-linejoin', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'round',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('stroke-width', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            '2',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('d', cls='token attr-name'),
                                                        Span(cls='token attr-value')(
                                                            Span('=', cls='token punctuation attr-equals'),
                                                            Span('"', cls='token punctuation'),
                                                            'm19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z',
                                                            Span('"', cls='token punctuation')
                                                        ),
                                                        Span('/>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'svg'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'button'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'div'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    ),
                                                    Span(cls='token tag')(
                                                        Span(cls='token tag')(
                                                            Span('</', cls='token punctuation'),
                                                            'form'
                                                        ),
                                                        Span('>', cls='token punctuation')
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                Button('Expand code', data_expand_code='', type='button', cls='absolute bottom-0 left-0 py-2.5 px-5 w-full text-sm font-medium text-gray-900 bg-gray-100 border-t border-gray-200 hover:bg-gray-100 hover:text-blue-700 dark:bg-gray-700 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700')
                            )
                        )
                    )
                ),
                Aside(aria_label='Previous and next page navigation', cls='flex mt-6 mb-8 font-medium leading-6')(
                    A(href='/docs/components/video/', cls='flex items-center justify-center mr-8 text-gray-500 transition-colors duration-200 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white')(
                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 10', cls='w-3.5 h-3.5 mr-2')(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 5H1m0 0 4 4M1 5l4-4')
                        ),
                        'Video'
                    ),
                    A(href='/docs/forms/file-input/', cls='flex items-center justify-center ml-auto text-right text-gray-500 transition-colors duration-200 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white')(
                        'File Input',
                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none', viewbox='0 0 14 10', cls='w-3.5 h-3.5 ml-2')(
                            Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 5h12m0 0L9 1m4 4L9 9')
                        )
                    )
                ),
                Aside(aria_label='Subscribe to the Flowbite newsletter', cls='p-4 my-8 bg-white border border-gray-200 rounded-lg shadow-md sm:p-6 lg:p-8 dark:bg-gray-800 dark:border-gray-700')(
                    H3('Get more updates...', cls='mb-3 text-xl font-medium text-gray-900 dark:text-white'),
                    P("Do you want to get notified when a new component is added to Flowbite? Sign up for our newsletter and you'll be among the first to find out about new features, components, versions, and tools.", cls='mb-5 text-sm font-medium text-gray-500 dark:text-gray-300'),
                    Script(src='https://f.convertkit.com/ckjs/ck.5.js'),
                    Form(action='https://app.convertkit.com/forms/4692392/subscriptions', method='post', data_sv_form='4692392', data_uid='344e3b5c48', data_format='inline', data_version='5', data_options='{"settings":{"after_subscribe":{"action":"message","success_message":"Success! Now check your email to confirm your subscription.","redirect_url":""},"analytics":{"google":null,"fathom":null,"facebook":null,"segment":null,"pinterest":null,"sparkloop":null,"googletagmanager":null},"modal":{"trigger":"timer","scroll_percentage":null,"timer":5,"devices":"all","show_once_every":15},"powered_by":{"show":true,"url":"https://convertkit.com/features/forms?utm_campaign=poweredby&utm_content=form&utm_medium=referral&utm_source=dynamic"},"recaptcha":{"enabled":false},"return_visitor":{"action":"show","custom_content":""},"slide_in":{"display_in":"bottom_right","trigger":"timer","scroll_percentage":null,"timer":5,"devices":"all","show_once_every":15},"sticky_bar":{"display_in":"top","trigger":"timer","scroll_percentage":null,"timer":5,"devices":"all","show_once_every":15}},"version":"5"}', min_width='400 500 600 700', cls='seva-form formkit-form')(
                        Div(data_style='clean', cls='flex items-end mb-3')(
                            Ul(data_element='errors', data_group='alert', cls='formkit-alert formkit-alert-error'),
                            Div(data_element='fields', data_stacked='false', cls='flex items-center w-full max-w-md mb-3 seva-fields formkit-fields')(
                                Div(cls='relative w-full mr-3 formkit-field')(
                                    Label('Email address', fr='member_email', cls='hidden block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300'),
                                    Div(cls='absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none')(
                                        Svg(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='currentColor', viewbox='0 0 20 16', cls='w-3.5 h-3.5 text-gray-500 dark:text-gray-400')(
                                            Path(d='m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z'),
                                            Path(d='M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z')
                                        )
                                    ),
                                    Input(id='member_email', name='email_address', aria_label='Email Address', placeholder='Your email address...', required='', type='email', cls='formkit-input bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
                                ),
                                Button(data_element='submit', cls='formkit-submit')(
                                    Div(cls='formkit-spinner')(
                                        Div(),
                                        Div(),
                                        Div()
                                    ),
                                    Span('Subscribe', cls='px-5 py-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg cursor-pointer hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800')
                                )
                            )
                        )
                    ),
                    Div(cls='text-sm font-medium text-gray-500 dark:text-gray-300')(
                        "By subscribing, you agree with ConvertKit's",
                        A('Terms of Service', rel='nofollow', href='https://convertkit.com/terms', cls='text-blue-600 hover:underline dark:text-blue-500'),
                        'and',
                        A('Privacy Policy', rel='nofollow', href='https://convertkit.com/privacy', cls='text-blue-600 hover:underline dark:text-blue-500'),
                        '.'
                    )
                )
            )
        ),
        Div(cls='flex-none hidden w-64 pl-8 mr-8 xl:text-sm xl:block')(
            Div(cls='flex overflow-y-auto sticky top-28 flex-col justify-between pt-10 pb-6 h-[calc(100vh-5rem)]')(
                Div(cls='mb-8')(
                    H4('On this page', cls='pl-2.5 mb-2 text-sm font-semibold tracking-wide text-gray-900 uppercase dark:text-white lg:text-xs'),
                    Nav(id='TableOfContents')(
                        Ul(
                            Li(
                                A('Input fields', href='#input-fields', cls='')
                            ),
                            Li(
                                A('Input sizes', href='#input-sizes', cls='!border-blue-700 !after:opacity-100 !text-blue-700 dark:!border-blue-500 dark:!text-blue-500')
                            ),
                            Li(
                                A('Disabled state', href='#disabled-state', cls='')
                            ),
                            Li(
                                A('Validation', href='#validation', cls='')
                            ),
                            Li(
                                A('Input group', href='#input-group', cls='')
                            ),
                            Li(
                                A('Helper text', href='#helper-text', cls='')
                            ),
                            Li(
                                A('Search input', href='#search-input', cls='')
                            ),
                            Li(
                                A('Dropdown input', href='#dropdown-input', cls='')
                            )
                        )
                    ),
                    Aside(cls='w-52 mt-6 mx-auto border-t border-gray-200 dark:border-gray-700 pt-8')(
                        A(href='https://www.enhanceui.com/?ref=flowbite-sidebar', rel='nofollow noopener noreferrer', target='_blank', cls='block rounded-lg')(
                            Img(src='/docs/images/book-light.svg', alt='Enhance UI book cover light mode', cls='shadow-sm mb-3 w-36 dark:hidden'),
                            Img(src='/docs/images/book-dark.svg', alt='Enhance UI book cover dark mode', cls='shadow-sm mb-3 w-36 hidden dark:block'),
                            H4('Learn Design Concepts', cls='text-base font-semibold text-gray-900 mb-1.5 dark:text-white'),
                            P('Make better Flowbite pages by learning the fundamentals of design', cls='text-gray-500 dark:text-gray-400'),
                            Div(cls='border-t border-gray-200 dark:border-gray-700 pt-2 mt-2')(
                                H5('Teach Me Design', cls='font-medium text-gray-900 dark:text-white'),
                                P('by Adrian Twarog', cls='text-gray-500 dark:text-gray-400')
                            )
                        )
                    )
                )
            )
        )
    )
)


playground = Container(
    # input_field_component,
    file_input_component,
    DivCentered(
        NotStr("""        
        
        """)
    )
) 