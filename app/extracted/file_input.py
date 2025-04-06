from fasthtml.common import *
from fasthtml.svg import *
from fastbite.components import *
from utils import component_showcase

component = Div(
    P('The file input component can be used to upload one or more files from the device storage of the user available in multiple sizes, styles, and variants and built with the utility-first classes from Tailwind CSS including support for dark mode.'),
    P('Make sure that you have included Flowbite as a plugin inside your Tailwind CSS project to apply all the necessary styles for the file input component.'),
    H2(
        'File upload example',
        Span(id='file-upload-example', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: File upload example', href='#file-upload-example', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Get started with a simple file input component to let users upload one single file.'),
    component_showcase(Div(
    Label('Upload file', fr='file_input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='file_input', type='file', cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
), code="""Div(
    Label('Upload file', fr='file_input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='file_input', type='file', cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
)""", id="example_0",cls='mt-2 mb-6'),
    H2(
        'Helper text',
        Span(id='helper-text', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Helper text', href='#helper-text', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Add a descriptive helper text to inform users the allowed extensions and sizes of the files.'),
    component_showcase(Div(
    Label('Upload file', fr='file_input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(aria_describedby='file_input_help', id='file_input', type='file', cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    P('SVG, PNG, JPG or GIF (MAX. 800x400px).', id='file_input_help', cls='mt-1 text-sm text-gray-500 dark:text-gray-300')
), code="""Div(
    Label('Upload file', fr='file_input', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(aria_describedby='file_input_help', id='file_input', type='file', cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    P('SVG, PNG, JPG or GIF (MAX. 800x400px).', id='file_input_help', cls='mt-1 text-sm text-gray-500 dark:text-gray-300')
)""", id="example_1",cls='mt-2 mb-6'),
    H2(
        'Multiple files',
        Span(id='multiple-files', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Multiple files', href='#multiple-files', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P(
        'Apply the',
        Code('multiple'),
        'attribute to the file input component to allow more files to be uploaded.'
    ),
    component_showcase(Div(
    Label('Upload multiple files', fr='multiple_files', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='multiple_files', type='file', multiple=True, cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
), code="""Div(
    Label('Upload multiple files', fr='multiple_files', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='multiple_files', type='file', multiple=True, cls='block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
)""", id="example_2",cls='mt-2 mb-6'),
    H2(
        'Sizes',
        Span(id='sizes', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Sizes', href='#sizes', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('Choose from the small, default, and large file input sizing options.'),
    component_showcase(Div(
    Label('Small file input', fr='small_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='small_size', type='file', cls='block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    Label('Default size', fr='default_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='default_size', type='file', cls='block w-full mb-5 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    Label('Large file input', fr='large_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='large_size', type='file', cls='block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
), code="""Div(
    Label('Small file input', fr='small_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='small_size', type='file', cls='block w-full mb-5 text-xs text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    Label('Default size', fr='default_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='default_size', type='file', cls='block w-full mb-5 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'),
    Label('Large file input', fr='large_size', cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
    Input(id='large_size', type='file', cls='block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400')
)""", id="example_3",cls='mt-2 mb-6'),
    H2(
        'Dropzone',
        Span(id='dropzone', cls='absolute -top-[140px]'),
        A('#', aria_label='Link to this section: Dropzone', href='#dropzone', cls='ml-2 text-primary-700 opacity-0 transition-opacity dark:text-primary-500 group-hover:opacity-100'),
        cls='relative group'
    ),
    P('The dropzone file input component can be used to upload one or more files by clicking anywhere in the area.'),
    component_showcase(Div(
    Div(
        Label(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 16',
                    cls='w-8 h-8 mb-4 text-gray-500 dark:text-gray-400'
                ),
                P(
                    Span('Click to upload', cls='font-semibold'),
                    'or drag and drop',
                    cls='mb-2 text-sm text-gray-500 dark:text-gray-400'
                ),
                P('SVG, PNG, JPG or GIF (MAX. 800x400px)', cls='text-xs text-gray-500 dark:text-gray-400'),
                cls='flex flex-col items-center justify-center pt-5 pb-6'
            ),
            Input(id='dropzone-file', type='file', cls='hidden'),
            fr='dropzone-file',
            cls='flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600'
        ),
        cls='flex items-center justify-center w-full'
    )
), code="""Div(
    Div(
        Label(
            Div(
                Svg(
                    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2'),
                    aria_hidden='true',
                    xmlns='http://www.w3.org/2000/svg',
                    fill='none',
                    viewbox='0 0 20 16',
                    cls='w-8 h-8 mb-4 text-gray-500 dark:text-gray-400'
                ),
                P(
                    Span('Click to upload', cls='font-semibold'),
                    'or drag and drop',
                    cls='mb-2 text-sm text-gray-500 dark:text-gray-400'
                ),
                P('SVG, PNG, JPG or GIF (MAX. 800x400px)', cls='text-xs text-gray-500 dark:text-gray-400'),
                cls='flex flex-col items-center justify-center pt-5 pb-6'
            ),
            Input(id='dropzone-file', type='file', cls='hidden'),
            fr='dropzone-file',
            cls='flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600'
        ),
        cls='flex items-center justify-center w-full'
    )
)""", id="example_4",cls='mt-2 mb-6'),
    id='mainContent'
)
