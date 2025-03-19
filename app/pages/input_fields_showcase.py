from utils import component_showcase
from fh_flowbite.input_fields import (
    DefaultInputField, 
    InputWithHelperText, 
    DisabledInputField,
    LargeInputField,
    SmallInputField
)
import inspect
from fasthtml.common import Div, H2, P

def InputFieldsShowcase():
    """
    Showcase page for different types of input fields.
    """
    
    # Title section
    title = H2("Input Field Components", className="text-2xl font-bold mb-4 text-gray-900 dark:text-white")
    description = P("Various input field components following Flowbite design system.", className="mb-8 text-gray-600 dark:text-gray-400")
    
    # Default input
    default_input_code = inspect.getsource(DefaultInputField)
    default_input_component = DefaultInputField("Default input", "Type your text here")
    default_input_showcase = component_showcase(default_input_component, code=default_input_code, id="default-input")
    
    # Helper text input
    helper_text_input_code = inspect.getsource(InputWithHelperText)
    helper_text_input_component = InputWithHelperText()
    helper_text_input_showcase = component_showcase(helper_text_input_component, code=helper_text_input_code, id="helper-text-input")
    
    # Disabled input
    disabled_input_code = inspect.getsource(DisabledInputField)
    disabled_input_component = Div(
        DisabledInputField(),
        DisabledInputField("Disabled readonly input", "disabled-input-2", readonly=True),
        className="flex flex-col gap-4"
    )
    disabled_input_showcase = component_showcase(disabled_input_component, code=disabled_input_code, id="disabled-input")
    
    # Large input
    large_input_code = inspect.getsource(LargeInputField)
    large_input_component = LargeInputField()
    large_input_showcase = component_showcase(large_input_component, code=large_input_code, id="large-input")
    
    # Small input
    small_input_code = inspect.getsource(SmallInputField)
    small_input_component = SmallInputField()
    small_input_showcase = component_showcase(small_input_component, code=small_input_code, id="small-input")

    return Div(
        title,
        description,
        DefaultInputField("Page Title", "This shows the heading for this page"),
        Div(
            default_input_showcase,
            helper_text_input_showcase,
            disabled_input_showcase,
            large_input_showcase,
            small_input_showcase,
            className="flex flex-col gap-10"
        ),
        className="p-6"
    )

input_fields_showcase = InputFieldsShowcase()