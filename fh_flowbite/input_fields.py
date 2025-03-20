from fasthtml.components import Div, Label, Input, P, A
from .components import Round
def DefaultInputField(label_text="Default input", placeholder="", input_id="default-input"):
    """
    Creates a default input field component.

    Args:
        label_text (str): Text for the label. Defaults to "Default input".
        placeholder (str): Placeholder text for the input. Defaults to empty string.
        input_id (str): ID for the input field and htmlFor for the label. Defaults to "default-input".

    Returns:
        Div: A Div component containing the label and input field.
    """
    return Div(
        Label( label_text, fr=input_id, cls='block mb-2 text-sm font-medium text-gray-900 dark:text-white'),
        Input(type='text', id=input_id, placeholder=placeholder, required='', cls='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500')
    )

def InputWithHelperText(label_text="Your email", placeholder="name@flowbite.com", helper_text="We'll never share your details. Read our", link_text="Privacy Policy", input_id="helper-text", helper_id="helper-text-explanation"):
    """
    Creates an input field component with helper text.

    Args:
        label_text (str): Text for the label. Defaults to "Your email".
        placeholder (str): Placeholder text for the input. Defaults to "name@flowbite.com".
        helper_text (str): Text for the helper message. Defaults to "We'll never share your details. Read our".
        link_text (str): Text for the link in helper text. Defaults to "Privacy Policy".
        input_id (str): ID for the input field and htmlFor for the label. Defaults to "helper-text".
        helper_id (str): ID for the helper text paragraph. Defaults to "helper-text-explanation".

    Returns:
        Div: A Div component containing the label, input field, and helper text.
    """
    return Div(
        Label(label_text, className="block mb-2 text-sm font-medium text-gray-900 dark:text-white", htmlFor=input_id),
        Input(
            type="email", 
            id=input_id, 
            aria_describedby=helper_id, 
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", 
            placeholder=placeholder
        ),
        P(
            helper_text,
            A(link_text, href="#", className="font-medium text-blue-600 hover:underline dark:text-blue-500"),
            ".",
            id=helper_id,
            className="mt-2 text-sm text-gray-500 dark:text-gray-400"
        )
    )

def DisabledInputField(value="Disabled input", input_id="disabled-input", readonly=False):
    """
    Creates a disabled input field component.

    Args:
        value (str): Value for the input field. Defaults to "Disabled input".
        input_id (str): ID for the input field. Defaults to "disabled-input".
        readonly (bool): Whether the input should be readonly. Defaults to False.

    Returns:
        Input: A disabled input field component.
    """
    input_props = {
        "type": "text",
        "id": input_id,
        "aria_label": f"disabled input{' readonly' if readonly else ''}",
        "className": "bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
        "value": value,
        "disabled": True
    }
    
    if readonly:
        input_props["readonly"] = True
    
    if not readonly:
        input_props["className"] = "mb-6 " + input_props["className"]
    
    return Input(**input_props)

def LargeInputField(input_id="large-input"):
    """
    Creates a large input field component.
    
    Args:
        input_id (str): ID for the input field. Defaults to "large-input".
        
    Returns:
        Input: A large input field component.
    """
    return Input(
        type="text", 
        id=input_id, 
        className="block w-full p-4 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    )

def SmallInputField(label_text="Small input", input_id="small-input"):
    """
    Creates a small input field component.
    
    Args:
        label_text (str): Text for the label. Defaults to "Small input".
        input_id (str): ID for the input field and htmlFor for the label. Defaults to "small-input".
        
    Returns:
        Div: A Div component containing the label and a small input field.
    """
    return Div(
        Label(label_text, className="block mb-2 text-sm font-medium text-gray-900 dark:text-white", htmlFor=input_id),
        Input(
            type="text", 
            id=input_id, 
            className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        )
    ) 