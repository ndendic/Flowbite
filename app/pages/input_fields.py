from fasthtml.common import Div, P, H1, H2, H3, Small, Code, Pre
from fh_flowbite.input_fields import (
    InputField, SearchInput, InputWithHelper, InputGroup, DropdownInput,
    InputType, InputSize, InputColor
)

def Section(title, description, example, code_snippet):
    """Helper function to create a consistent section format for the page"""
    return Div(
        H3(title, cls="text-lg font-semibold mb-2"),
        P(description, cls="text-gray-600 dark:text-gray-400 mb-4"),
        Div(
            example,
            cls="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 mb-4"
        ),
        Div(
            Pre(
                Code(code_snippet, cls="language-python"),
                cls="text-sm"
            ),
            cls="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 mb-6"
        ),
        cls="mb-10"
    )

def input_fields():
    """Input fields showcase page"""
    
    # Basic Input Field Section
    basic_input_field_example = Div(
        InputField("First name", placeholder="John", required=True),
        InputField("Email address", type=InputType.email, placeholder="name@example.com", required=True),
        InputField("Password", type=InputType.password, placeholder="••••••••"),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    basic_input_field_code = """InputField(
    "First name", 
    placeholder="John", 
    required=True
)

InputField(
    "Email address", 
    type=InputType.email, 
    placeholder="name@example.com", 
    required=True
)

InputField(
    "Password", 
    type=InputType.password, 
    placeholder="••••••••"
)"""
    
    # Input Field States Section
    input_states_example = Div(
        InputField("Default", placeholder="Default input"),
        InputField("Success", placeholder="Success input", color=InputColor.success),
        InputField("Error", placeholder="Error input", color=InputColor.error),
        InputField("Disabled", placeholder="Disabled input", disabled=True),
        InputField("Read-only", placeholder="Read-only input", readonly=True, value="Read-only value"),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    input_states_code = """InputField(
    "Default", 
    placeholder="Default input"
)

InputField(
    "Success", 
    placeholder="Success input", 
    color=InputColor.success
)

InputField(
    "Error", 
    placeholder="Error input", 
    color=InputColor.error
)

InputField(
    "Disabled", 
    placeholder="Disabled input", 
    disabled=True
)

InputField(
    "Read-only", 
    placeholder="Read-only input", 
    readonly=True, 
    value="Read-only value"
)"""
    
    # Input Sizes Section
    input_sizes_example = Div(
        InputField("Small input", placeholder="Small input", size=InputSize.sm),
        InputField("Default input", placeholder="Default input"),
        InputField("Large input", placeholder="Large input", size=InputSize.lg),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    input_sizes_code = """InputField(
    "Small input", 
    placeholder="Small input", 
    size=InputSize.sm
)

InputField(
    "Default input", 
    placeholder="Default input"
)

InputField(
    "Large input", 
    placeholder="Large input", 
    size=InputSize.lg
)"""
    
    # Input with Helper Text Section
    input_helper_example = Div(
        InputWithHelper(
            "Email address", 
            helper_text="We'll never share your email. Read our {link}.", 
            type=InputType.email, 
            placeholder="name@example.com",
            helper_link_text="Privacy Policy", 
            helper_link_url="#privacy"
        ),
        InputWithHelper(
            "Username", 
            helper_text="Choose a unique username.", 
            placeholder="username",
            helper_link_text=None
        ),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    input_helper_code = """InputWithHelper(
    "Email address", 
    helper_text="We'll never share your email. Read our {link}.", 
    type=InputType.email, 
    placeholder="name@example.com",
    helper_link_text="Privacy Policy", 
    helper_link_url="#privacy"
)

InputWithHelper(
    "Username", 
    helper_text="Choose a unique username.", 
    placeholder="username",
    helper_link_text=None
)"""
    
    # Input Group Section
    input_group_example = Div(
        InputGroup("Price", prefix="$", type=InputType.number, placeholder="0.00"),
        InputGroup("Website", suffix=".com", type=InputType.text, placeholder="example"),
        InputGroup("Budget range", prefix="$", suffix=".00", type=InputType.number, placeholder="100"),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    input_group_code = """InputGroup(
    "Price", 
    prefix="$", 
    type=InputType.number, 
    placeholder="0.00"
)

InputGroup(
    "Website", 
    suffix=".com", 
    type=InputType.text, 
    placeholder="example"
)

InputGroup(
    "Budget range", 
    prefix="$", 
    suffix=".00", 
    type=InputType.number, 
    placeholder="100"
)"""
    
    # Search Input Section
    search_input_example = Div(
        SearchInput(placeholder="Search for items...", button_text="Search"),
        SearchInput(placeholder="Small search...", button_text="Search", size=InputSize.sm),
        SearchInput(placeholder="Large search...", button_text="Search", size=InputSize.lg),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    search_input_code = """SearchInput(
    placeholder="Search for items...", 
    button_text="Search"
)

SearchInput(
    placeholder="Small search...", 
    button_text="Search", 
    size=InputSize.sm
)

SearchInput(
    placeholder="Large search...", 
    button_text="Search", 
    size=InputSize.lg
)"""
    
    # Dropdown Input Section
    dropdown_input_example = Div(
        DropdownInput(
            "Search categories",
            dropdown_options=["All", "Products", "Services", "Blog", "Forum"],
            placeholder="Search in selected category..."
        ),
        cls="flex flex-col space-y-4 max-w-md"
    )
    
    dropdown_input_code = """DropdownInput(
    "Search categories",
    dropdown_options=["All", "Products", "Services", "Blog", "Forum"],
    placeholder="Search in selected category..."
)"""
    
    # Main Page Content
    return Div(
        # Header
        H1("Input Fields", cls="text-2xl font-bold mb-2"),
        P("A collection of input field components based on Flowbite design system.", 
          cls="text-gray-600 dark:text-gray-400 mb-8"),
        
        # Basic Input Fields Section
        Section(
            "Basic Input Fields",
            "Standard input fields with labels for collecting different types of data.",
            basic_input_field_example,
            basic_input_field_code
        ),
        
        # Input States Section
        Section(
            "Input States",
            "Input fields can have different states: default, success, error, disabled, and read-only.",
            input_states_example,
            input_states_code
        ),
        
        # Input Sizes Section
        Section(
            "Input Sizes",
            "Input fields are available in three sizes: small, medium (default), and large.",
            input_sizes_example,
            input_sizes_code
        ),
        
        # Input with Helper Text Section
        Section(
            "Input with Helper Text",
            "Input fields with additional explanatory text below to provide context or guidance.",
            input_helper_example,
            input_helper_code
        ),
        
        # Input Group Section
        Section(
            "Input Group",
            "Add prefix and/or suffix elements to input fields for common use cases like currency, domain extensions, etc.",
            input_group_example,
            input_group_code
        ),
        
        # Search Input Section
        Section(
            "Search Input",
            "Specialized input field for search functionality with search icon and submit button.",
            search_input_example,
            search_input_code
        ),
        
        # Dropdown Input Section
        Section(
            "Dropdown Input",
            "Search input with a dropdown menu for filtering options.",
            dropdown_input_example,
            dropdown_input_code
        ),
        
        cls="px-4 py-8"
    ) 