from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

# --- Form Section ---
def _form_section():
    return Section(
        H2("Form", link=True, cls="mb-4 mt-10"),
        P("The main container for grouping form elements. Provides basic structure and spacing."),

        H3("Default Form", link=True, cls="mb-3"),
        P("Standard form layout with default spacing (", Code("cls=FormT.default"), ")."),
        component_showcase(
            Form(
                Input(id='email_default', label="Email address", type='email', placeholder='name@flowbite.com'),
                Input(id='password_default', label="Password", type='password'),
                Button("Submit", type='submit')
            ),
            code='''from fastbite.all import Form, FormLabel, Input, FormT, Button

Form(
    Input(id=\'email_default\', label="Email address", type=\'email\', placeholder=\'name@flowbite.com\'),
    Input(id=\'password_default\', label="Password", type=\'password\'),
    Button("Submit", type=\'submit\')
)''',
            id="form-default"
        ),
        Br(),

        H3("Slim Form", link=True, cls="mb-3"),
        P("A form with reduced width using ", Code("cls=FormT.slim"), "."),
        component_showcase(
            Form(
                Input(id='username_slim', label="Username", placeholder='your_username'),
                Button("Login", type='submit'),
                cls=FormT.slim
            ),
            code='''from fastbite.all import Form, FormT, FormLabel, Input, Button

Form(
    FormLabel("Username", fr="username_slim"),
    Input(id=\'username_slim\', placeholder=\'your_username\'),
    Button("Login", type=\'submit\'),
    cls=FormT.slim
)''',
            id="form-slim"
        ),
        Br(),
    )

# --- FormLabel Section ---
def _formlabel_section():
    return Section(
        H2("FormLabel", link=True, cls="mb-4 mt-10"),
        P("Used to label form inputs. Connects to an input via the ", Code("fr"), " (for) attribute. Includes variants for success and error states using ", Code("LabelInputT"), "."),

        H3("Default Label", link=True, cls="mb-3"),
        component_showcase(
            FormLabel("Default Label", fr="some_input_id"),
            code='''from fastbite.all import FormLabel

FormLabel("Default Label", fr="some_input_id")''',
            id="formlabel-default"
        ),
        Br(),

        H3("Success Label", link=True, cls="mb-3"),
        P("Use ", Code("cls=LabelInputT.success"), " for success state."),
        component_showcase(
            FormLabel("Success Label", fr="success_input_id", cls=LabelInputT.success),
            code='''from fastbite.all import FormLabel, LabelInputT

FormLabel("Success Label", fr="success_input_id", cls=LabelInputT.success)''',
            id="formlabel-success"
        ),
        Br(),

        H3("Error Label", link=True, cls="mb-3"),
        P("Use ", Code("cls=LabelInputT.error"), " for error state."),
        component_showcase(
            FormLabel("Error Label", fr="error_input_id", cls=LabelInputT.error),
            code='''from fastbite.all import FormLabel, LabelInputT

FormLabel("Error Label", fr="error_input_id", cls=LabelInputT.error)''',
            id="formlabel-error"
        ),
        Br(),
    )

# --- Input Section ---
def _input_section():
    return Section(
        H2("Input", link=True, cls="mb-4 mt-10"),
        P("A standard text input field. It can be enhanced with labels, help text, icons, and validation states using ", Code("InputT"), ". The component automatically wraps the input and associated elements in a ", Code("Div"), "."),

        H3("Default Input", link=True, cls="mb-3"),
        P("Basic input field with a placeholder."),
        component_showcase(
            Input(id='input-default', placeholder='Default input'),
            code='''from fastbite.all import Input

Input(id=\'input-default\', placeholder=\'Default input\')''',
            id="input-default"
        ),
        Br(),

        H3("Input with Label", link=True, cls="mb-3"),
        P("Using the ", Code("label"), " parameter adds a ", Code("FormLabel"), " automatically linked via the ", Code("id"), "."),
        component_showcase(
            Input(label="Your Email", id='input-label', type='email', placeholder='name@flowbite.com'),
            code='''from fastbite.all import Input

Input(label="Your Email", id=\'input-label\', type=\'email\', placeholder=\'name@flowbite.com\')''',
            id="input-label"
        ),
        Br(),

        H3("Input with Help Text", link=True, cls="mb-3"),
        P("Use the ", Code("help_text"), " parameter to add descriptive text below the input."),
        component_showcase(
            Input(label="Password", id='input-help', type='password', placeholder='••••••••', help_text="Must be at least 8 characters."),
            code='''from fastbite.all import Input

Input(label="Password", id=\'input-help\', type=\'password\', placeholder=\'••••••••\', help_text="Must be at least 8 characters.")''',
            id="input-help"
        ),
        Br(),

        H3("Input with Icon", link=True, cls="mb-3"),
        P("Use the ", Code("icon"), " parameter (provide an icon name, e.g., from Bootstrap Icons) to add an icon inside the input field."),
        component_showcase(
            Input(label="Email with Icon", id='input-icon', type='email', placeholder='name@flowbite.com',icon='lucide:mail'),
            code='''from fastbite.all import Input

Input(label="Email with Icon", id=\'input-icon\', type=\'email\', placeholder=\'name@flowbite.com\', icon=\'envelope-fill\')''',
            id="input-icon"
        ),
        Br(),

        H3("Required Input", link=True, cls="mb-3"),
        P("Setting ", Code("required=True"), " adds the HTML ", Code("required"), " attribute."),
        component_showcase(
            Input(label="Required Field", id='input-required', placeholder='Cannot be empty', required=True),
            code='''from fastbite.all import Input

Input(label="Required Field", id=\'input-required\', placeholder=\'Cannot be empty\', required=True)''',
            id="input-required"
        ),
        Br(),

        H3("Disabled Input", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the input non-interactive and applies disabled styling."),
        component_showcase(
            Input(label="Disabled Field", id='input-disabled', placeholder='Disabled input', value="Cannot change", disabled=True),
            code='''from fastbite.all import Input

Input(label="Disabled Field", id=\'input-disabled\', placeholder=\'Disabled input\', value="Cannot change", disabled=True)''',
            id="input-disabled"
        ),
        Br(),

        H3("Success State Input", link=True, cls="mb-3"),
        P("Use ", Code("cls=InputT.success"), " for validation success indication. This also styles the associated ", Code("FormLabel"), " if ", Code("lbl_cls"), " is set accordingly (e.g., ", Code("lbl_cls=LabelInputT.success"), ")."),
        component_showcase(
            Input(label="Success Input", id='input-success', placeholder='Valid input', cls=InputT.success, lbl_cls=LabelInputT.success, value="Validated Content", help_text="Looks good!"),
            code='''from fastbite.all import Input, InputT, LabelInputT

Input(
    label="Success Input", 
    id=\'input-success\', 
    placeholder=\'Valid input\', 
    cls=InputT.success, 
    lbl_cls=LabelInputT.success, # Style label too
    value="Validated Content",
    help_text="Looks good!" # Optional help text
)''',
            id="input-success"
        ),
        Br(),

        H3("Error State Input", link=True, cls="mb-3"),
        P("Use ", Code("cls=InputT.error"), " for validation error indication. Similarly, use ", Code("lbl_cls=LabelInputT.error"), " to style the label."),
        component_showcase(
            Input(label="Error Input", id='input-error', placeholder='Invalid input', cls=InputT.error, lbl_cls=LabelInputT.error, value="Incorrect Data", help_text="Please provide a valid email."),
            code='''from fastbite.all import Input, InputT, LabelInputT

Input(
    label="Error Input", 
    id=\'input-error\', 
    placeholder=\'Invalid input\', 
    cls=InputT.error, 
    lbl_cls=LabelInputT.error, # Style label too
    value="Incorrect Data",
    help_text="Please provide a valid email." # Optional help text
)''',
            id="input-error"
        ),
        Br(),
    )

# --- TextArea Section ---
def _textarea_section():
    return Section(
        H2("TextArea", link=True, cls="mb-4 mt-10"),
        P("A multi-line text input field, similar in structure and options to the ", Code("Input"), " component."),

        H3("Default TextArea", link=True, cls="mb-3"),
        P("Basic text area with a placeholder."),
        component_showcase(
            TextArea(id='textarea-default', placeholder='Your message...', rows=4),
            code='''from fastbite.all import TextArea

# Using rows=4 for a standard height
TextArea(id=\'textarea-default\', placeholder=\'Your message...\', rows=4)''',
            id="textarea-default"
        ),
        Br(),

        H3("TextArea with Label and Help Text", link=True, cls="mb-3"),
        P("Includes a ", Code("FormLabel"), " and descriptive text below using ", Code("label"), " and ", Code("help_text"), "."),
        component_showcase(
            TextArea(label="Your Comment", id='textarea-label-help', placeholder='Leave a comment...', rows=4, help_text="Write something constructive."),
            code='''from fastbite.all import TextArea

TextArea(
    label="Your Comment", 
    id=\'textarea-label-help\', 
    placeholder=\'Leave a comment...\', 
    rows=4, 
    help_text="Write something constructive."
)''',
            id="textarea-label-help"
        ),
        Br(),

        H3("Disabled TextArea", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the text area non-interactive."),
        component_showcase(
            TextArea(label="Disabled Text Area", id='textarea-disabled', placeholder='Cannot edit', rows=4, value="This content is read-only", disabled=True),
            code='''from fastbite.all import TextArea

TextArea(
    label="Disabled Text Area", 
    id=\'textarea-disabled\', 
    placeholder=\'Cannot edit\', 
    rows=4, 
    value="This content is read-only", 
    disabled=True
)''',
            id="textarea-disabled"
        ),
        Br(),
    )

# --- Select Section ---
def _select_section():
    return Section(
        H2("Select", link=True, cls="mb-4 mt-10"),
        P("A dropdown select input. It utilizes the ", Code("Options"), " helper function to create ", Code("fh.Option"), " elements easily. Like ", Code("Input"), ", it supports labels, help text, icons, and disabled states."),

        H3("Default Select", link=True, cls="mb-3"),
        P("Basic select dropdown created using ", Code("Options"), "."),
        component_showcase(
            Select(*Options("United States", "Canada", "Mexico"), id='select-default'),
            code='''from fastbite.all import Select, Options

Select(*Options("United States", "Canada", "Mexico"), id=\'select-default\')''',
            id="select-default"
        ),
        Br(),

        H3("Select with Label and Placeholder", link=True, cls="mb-3"),
        P("Using ", Code("label"), " for the ", Code("FormLabel"), " and ", Code("placeholder"), " for the default unselected text (though native select might not show placeholder text reliably across browsers)."),
        component_showcase(
            Select(
                *Options("United States", "Canada", "Mexico"), 
                label="Choose a country", 
                id='select-label-placeholder',
                # Note: Placeholder attribute on select itself is not standard
            ),
            code='''from fastbite.all import Select, Options

Select(
    *Options("United States", "Canada", "Mexico"), 
    label="Choose a country", 
    id=\'select-label-placeholder\'
    # Placeholder is usually achieved by adding an initial <option value="">Select...</option>
)''',
            id="select-label-placeholder"
        ),
        Br(),

        H3("Select with Icon and Help Text", link=True, cls="mb-3"),
        P("Adding an ", Code("icon"), " and descriptive ", Code("help_text"), "."),
        component_showcase(
            Select(
                *Options("Technology", "Business", "Creative"),
                label="Select Category",
                id='select-icon-help',
               icon='lucide:tag', # Example icon
                help_text="Choose the category that best fits."
            ),
            code='''from fastbite.all import Select, Options

Select(
    *Options("Technology", "Business", "Creative"),
    label="Select Category",
    id=\'select-icon-help\',
    icon=\'tag-fill\', 
    help_text="Choose the category that best fits."
)''',
            id="select-icon-help"
        ),
        Br(),

        H3("Disabled Select", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the select non-interactive."),
        component_showcase(
            Select(*Options("Option 1", "Option 2"), label="Disabled Select", id='select-disabled', disabled=True),
            code='''from fastbite.all import Select, Options

Select(*Options("Option 1", "Option 2"), label="Disabled Select", id=\'select-disabled\', disabled=True)''',
            id="select-disabled"
        ),
        Br(),
        # Note on Options helper: selected_idx and disabled_idxs require server-side logic or JS
        # to set the `selected` or `disabled` attributes on the generated <option> tags.
        # They are not directly showcased here for simplicity.
    )

# --- Radio Section ---
def _radio_section():
    return Section(
        H2("Radio Buttons", link=True, cls="mb-4 mt-10"),
        P("Used for selecting one option from a set. Radio buttons with the same ", Code("name"), " attribute (passed via ", Code("**kwargs"), ") form a group. Includes styling options via ", Code("RadioT"), "."),

        H3("Default Radio", link=True, cls="mb-3"),
        P("Basic radio button with a label."),
        component_showcase(
            # Group radios by giving them the same name attribute
            Div(
                Radio(label="Default radio", id='radio-default-1', name="radio-group-1"),
                Radio(label="Checked radio", id='radio-default-2', name="radio-group-1", checked=True),
            ),
            code='''from fastbite.all import Radio

# Note: 'name' attribute groups radio buttons
Radio(label="Default radio", id=\'radio-default-1\', name="radio-group-1")
Radio(label="Checked radio", id=\'radio-default-2\', name="radio-group-1", checked=True)''',
            id="radio-default"
        ),
        Br(),

        H3("Radio with Help Text", link=True, cls="mb-3"),
        P("Adding descriptive text using ", Code("help_text"), "."),
        component_showcase(
            Radio(label="Option with Help", id='radio-help', name="radio-group-2", help_text="This provides more context."),
            code='''from fastbite.all import Radio

Radio(
    label="Option with Help", 
    id=\'radio-help\', 
    name="radio-group-2", 
    help_text="This provides more context."
)''',
            id="radio-help"
        ),
        Br(),

        H3("Disabled Radio", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the radio button non-interactive."),
        component_showcase(
            Div(
                Radio(label="Disabled radio", id='radio-disabled-1', name="radio-group-3", disabled=True),
                Radio(label="Disabled checked radio", id='radio-disabled-2', name="radio-group-3", checked=True, disabled=True),
            ),
            code='''from fastbite.all import Radio

Radio(label="Disabled radio", id=\'radio-disabled-1\', name="radio-group-3", disabled=True)
Radio(label="Disabled checked radio", id=\'radio-disabled-2\', name="radio-group-3", checked=True, disabled=True)''',
            id="radio-disabled"
        ),
        Br(),

        H3("Success State Radio", link=True, cls="mb-3"),
        P("Use ", Code("cls=RadioT.success"), " for success styling."),
        component_showcase(
            Radio(label="Success Radio", id='radio-success', name="radio-group-4", cls=RadioT.success, checked=True),
            code='''from fastbite.all import Radio, RadioT

Radio(label="Success Radio", id=\'radio-success\', name="radio-group-4", cls=RadioT.success, checked=True)''',
            id="radio-success"
        ),
        Br(),

        H3("Error State Radio", link=True, cls="mb-3"),
        P("Use ", Code("cls=RadioT.error"), " for error styling."),
        component_showcase(
            Radio(label="Error Radio", id='radio-error', name="radio-group-5", cls=RadioT.error, checked=True),
            code='''from fastbite.all import Radio, RadioT

Radio(label="Error Radio", id=\'radio-error\', name="radio-group-5", cls=RadioT.error, checked=True)''',
            id="radio-error"
        ),
        Br(),
    )

# --- Checkbox Section ---
def _checkbox_section():
    return Section(
        H2("Checkbox", link=True, cls="mb-4 mt-10"),
        P("Used for selecting zero or more options from a set. Includes styling options via ", Code("CheckboxT"), "."),

        H3("Default Checkbox", link=True, cls="mb-3"),
        P("Basic checkbox with a label."),
        component_showcase(
            Div(
                Checkbox(label="Default checkbox", id='checkbox-default-1'),
                Checkbox(label="Checked checkbox", id='checkbox-default-2', checked=True),
            ),
            code='''from fastbite.all import Checkbox

Checkbox(label="Default checkbox", id=\'checkbox-default-1\')
Checkbox(label="Checked checkbox", id=\'checkbox-default-2\', checked=True)''',
            id="checkbox-default"
        ),
        Br(),

        H3("Checkbox with Help Text", link=True, cls="mb-3"),
        P("Adding descriptive text using ", Code("help_text"), "."),
        component_showcase(
            Checkbox(label="Accept terms and conditions", id='checkbox-help', help_text="You agree to our Privacy Policy."),
            code='''from fastbite.all import Checkbox

Checkbox(
    label="Accept terms and conditions", 
    id=\'checkbox-help\', 
    help_text="You agree to our Privacy Policy."
)''',
            id="checkbox-help"
        ),
        Br(),

        H3("Disabled Checkbox", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the checkbox non-interactive."),
        component_showcase(
            Div(
                Checkbox(label="Disabled checkbox", id='checkbox-disabled-1', disabled=True),
                Checkbox(label="Disabled checked checkbox", id='checkbox-disabled-2', checked=True, disabled=True),
            ),
            code='''from fastbite.all import Checkbox

Checkbox(label="Disabled checkbox", id=\'checkbox-disabled-1\', disabled=True)
Checkbox(label="Disabled checked checkbox", id=\'checkbox-disabled-2\', checked=True, disabled=True)''',
            id="checkbox-disabled"
        ),
        Br(),

        H3("Success State Checkbox", link=True, cls="mb-3"),
        P("Use ", Code("cls=CheckboxT.success"), " for success styling."),
        component_showcase(
            Checkbox(label="Success Checkbox", id='checkbox-success', cls=CheckboxT.success, checked=True),
            code='''from fastbite.all import Checkbox, CheckboxT

Checkbox(label="Success Checkbox", id=\'checkbox-success\', cls=CheckboxT.success, checked=True)''',
            id="checkbox-success"
        ),
        Br(),

        H3("Error State Checkbox", link=True, cls="mb-3"),
        P("Use ", Code("cls=CheckboxT.error"), " for error styling."),
        component_showcase(
            Checkbox(label="Error Checkbox", id='checkbox-error', cls=CheckboxT.error, checked=True),
            code='''from fastbite.all import Checkbox, CheckboxT

Checkbox(label="Error Checkbox", id=\'checkbox-error\', cls=CheckboxT.error, checked=True)''',
            id="checkbox-error"
        ),
        Br(),
    )

# --- Switch Section ---
def _switch_section():
    return Section(
        H2("Switch Toggle", link=True, cls="mb-4 mt-10"),
        P("A toggle switch, visually different but functionally similar to a checkbox. Uses ", Code("SwitchT"), " for styling."),

        H3("Default Switch", link=True, cls="mb-3"),
        P("Basic switch toggle with a label."),
        component_showcase(
            Div(
                Switch(label="Default switch", id='switch-default-1'),
                Switch(label="Checked switch", id='switch-default-2', checked=True),
            ),
            code='''from fastbite.all import Switch

Switch(label="Default switch", id=\'switch-default-1\')
Switch(label="Checked switch", id=\'switch-default-2\', checked=True)''',
            id="switch-default"
        ),
        Br(),

        H3("Disabled Switch", link=True, cls="mb-3"),
        P("Setting ", Code("disabled=True"), " makes the switch non-interactive."),
        component_showcase(
            Div(
                Switch(label="Disabled switch", id='switch-disabled-1', disabled=True),
                Switch(label="Disabled checked switch", id='switch-disabled-2', checked=True, disabled=True),
            ),
            code='''from fastbite.all import Switch

Switch(label="Disabled switch", id=\'switch-disabled-1\', disabled=True)
Switch(label="Disabled checked switch", id=\'switch-disabled-2\', checked=True, disabled=True)''',
            id="switch-disabled"
        ),
        Br(),

        H3("Success State Switch", link=True, cls="mb-3"),
        P("Use ", Code("cls=SwitchT.success"), " for success styling."),
        component_showcase(
            Switch(label="Success Switch", id='switch-success', cls=SwitchT.success, checked=True),
            code='''from fastbite.all import Switch, SwitchT

Switch(label="Success Switch", id=\'switch-success\', cls=SwitchT.success, checked=True)''',
            id="switch-success"
        ),
        Br(),

        H3("Error State Switch", link=True, cls="mb-3"),
        P("Use ", Code("cls=SwitchT.error"), " for error styling."),
        component_showcase(
            Switch(label="Error Switch", id='switch-error', cls=SwitchT.error, checked=True),
            code='''from fastbite.all import Switch, SwitchT

Switch(label="Error Switch", id=\'switch-error\', cls=SwitchT.error, checked=True)''',
            id="switch-error"
        ),
        Br(),
    )

# --- Main Showcase Function ---
def forms_showcase():
    """Page showcasing Form components"""
    return Container(
        H1("Form Components", link=True, cls="mb-8 mt-6"),
        P("Fastbite provides various components to build forms, including inputs, textareas, selects, radios, checkboxes, and switches. This page demonstrates their usage and styling options.", cls="mb-6 text-lg"),

        # Call section functions
        _form_section(),
        _formlabel_section(),
        _input_section(),
        _textarea_section(),
        _select_section(),
        _radio_section(),
        _checkbox_section(),
        _switch_section(),
    )

# Make the showcase available to the app
forms_components = forms_showcase() 