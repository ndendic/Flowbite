from fasthtml.common import *
from fastbite.all import *
from utils import component_showcase

# --- Basic Modal Section ---
def _modal_basic_section():
    modal_id = "modal-basic"
    return Section(
        H2("Basic Modal", link=True, cls="mb-4 mt-10"),
        P("The ", Code("Modal"), " component provides a convenient way to create modals with header, body, and footer sections. It uses Flowbite's JavaScript for toggling visibility."),
        P("You need a trigger element (like a button) with ", Code(f'data_modal_target="#{modal_id}"'), " and ", Code(f'data_modal_toggle="{modal_id}"'), " attributes."),
        component_showcase(
            # Trigger Button
            Button("Toggle Basic Modal", 
                   data_modal_target=f'#{modal_id}', 
                   data_modal_toggle=modal_id),
            # Modal Component (hidden by default)
            Modal(
                P("This is the default modal body content.", cls=TextT.gray), 
                P("You can put any content here."),
                header=[
                    ModalTitle("Default Modal Header"),
                    ModalCloseButton(modal_id=modal_id) # Use the specific close button
                ],
                footer=Div(
                    Button("Accept", cls=ButtonT.primary, data_modal_toggle=modal_id), # Use toggle to close
                    Button("Decline", cls=ButtonT.secondary, data_modal_toggle=modal_id),
                    cls="space-x-2"
                ),
                id=modal_id
            ),
            code=f'''from fastbite.all import Modal, ModalTitle, ModalCloseButton, Button, ButtonT, TextT, P, Div

modal_id = "{modal_id}"

# Trigger Button
Button("Toggle Basic Modal", 
       data_modal_target=f'#{{modal_id}}', 
       data_modal_toggle='{modal_id}')

# Modal Component
Modal(
    P("This is the default modal body content.", cls=TextT.gray), 
    P("You can put any content here."),
    header=[
        ModalTitle("Default Modal Header"),
        ModalCloseButton(modal_id=modal_id)
    ],
    footer=Div(
        Button("Accept", cls=ButtonT.primary, data_modal_toggle=modal_id),
        Button("Decline", cls=ButtonT.secondary, data_modal_toggle=modal_id),
        cls="space-x-2"
    ),
    id=modal_id
)
''',
            id="modal-basic-showcase"
        ),
        Br(),
    )

# --- Modal Sizing Section ---
def _modal_sizing_section():
    section_content = [
        H2("Modal Sizing", link=True, cls="mb-4 mt-10"),
        P("Control the width of the modal dialog using the ", Code("dialog_cls"), " parameter with size variants from ", Code("ModalT"), " (e.g., ", Code("ModalT.sm"), ", ", Code("ModalT.xl"), "). The default is ", Code("ModalT.lg"), ".")
    ]
    
    sizes = {
        'sm': ModalT.sm,
        'lg': ModalT.lg, # Default, shown for comparison
        'xl': ModalT.xl,
        '4xl': ModalT._4xl,
        '7xl': ModalT._7xl,
    }
    
    for name, size_cls in sizes.items():
        modal_id = f"modal-size-{name}"
        section_content.extend([
            H3(f"{name.upper()} Modal", link=True, cls="mb-3"),
            component_showcase(
                # Trigger Button
                Button(f"Toggle {name.upper()} Modal", 
                       data_modal_target=f'#{modal_id}', 
                       data_modal_toggle=modal_id),
                # Modal Component
                Modal(
                    P(f"This modal uses ", Code(f"dialog_cls=ModalT.{name}"), f" resulting in the '{size_cls}' class."),
                    header=[
                        ModalTitle(f"{name.upper()} Modal Example"),
                        ModalCloseButton(modal_id=modal_id)
                    ],
                    footer=Button("Close", cls=ButtonT.secondary, data_modal_toggle=modal_id),
                    id=modal_id,
                    dialog_cls=size_cls
                ),
                code=f'''from fastbite.all import Modal, ModalT, ModalTitle, ModalCloseButton, Button, ButtonT, P

modal_id = "{modal_id}"

# Trigger
Button(f"Toggle {name.upper()} Modal", 
       data_modal_target=f'#{{modal_id}}', 
       data_modal_toggle='{modal_id}')

# Modal
Modal(
    P("Modal body content..."),
    header=[
        ModalTitle("{name.upper()} Modal Example"),
        ModalCloseButton(modal_id=modal_id)
    ],
    footer=Button("Close", cls=ButtonT.secondary, data_modal_toggle=modal_id),
    id=modal_id,
    dialog_cls=ModalT.{name} # Sets the size class '{size_cls}'
)
''',
                id=f"modal-size-{name}-showcase"
            ),
            Br()
        ])
        
    return Section(*section_content)

# --- Modal Placement Section ---
def _modal_placement_section():
    section_content = [
        H2("Modal Placement", link=True, cls="mb-4 mt-10"),
        P("Position the modal within the viewport using the ", Code("placement"), " parameter. Use placement variants from ", Code("ModalT"), " (e.g., ", Code("ModalT.top_center"), ", ", Code("ModalT.bottom_right"), "). The default is ", Code("ModalT.center"), ".")
    ]
    
    placements = {
        'top-center': ModalT.top_center,
        'top-right': ModalT.top_right,
        'center-left': ModalT.center_left,
        'bottom-center': ModalT.bottom_center,
        'bottom-right': ModalT.bottom_right,
    }
    
    for name, placement_cls in placements.items():
        modal_id = f"modal-placement-{name.replace('-', '_')}"
        name_title = name.replace('-', ' ').title()
        name_code = name.replace('-', '_')
        section_content.extend([
            H3(f"{name_title} Placement", link=True, cls="mb-3"),
            component_showcase(
                # Trigger Button
                Button(f"Toggle {name_title} Modal", 
                       data_modal_target=f'#{modal_id}', 
                       data_modal_toggle=modal_id),
                # Modal Component
                Modal(
                    P(f"This modal uses ", Code(f"placement=ModalT.{name_code}"), f" resulting in the '{placement_cls}' class on the container."),
                    header=[
                        ModalTitle(f"{name_title} Placement Example"),
                        ModalCloseButton(modal_id=modal_id)
                    ],
                    footer=Button("Close", cls=ButtonT.secondary, data_modal_toggle=modal_id),
                    id=modal_id,
                    placement=placement_cls,
                    dialog_cls=ModalT.md # Use a smaller size for placement demo
                ),
                code=f'''from fastbite.all import Modal, ModalT, ModalTitle, ModalCloseButton, Button, ButtonT, P

modal_id = "{modal_id}"

# Trigger
Button(f"Toggle {name_title} Modal", 
       data_modal_target=f'#{{modal_id}}', 
       data_modal_toggle='{modal_id}')

# Modal
Modal(
    P("Modal body content..."),
    header=[
        ModalTitle("{name_title} Example"),
        ModalCloseButton(modal_id=modal_id)
    ],
    footer=Button("Close", cls=ButtonT.secondary, data_modal_toggle=modal_id),
    id=modal_id,
    placement=ModalT.{name_code} # Sets the placement class '{placement_cls}'
)
''',
                id=f"modal-placement-{name}-showcase"
            ),
            Br()
        ])
        
    return Section(*section_content)

# --- Modal Subcomponents Section ---
def _modal_subcomponents_section():
    return Section(
        H2("Modal Subcomponents (Building Blocks)", link=True, cls="mb-4 mt-10"),
        P("The main ", Code("Modal"), " component is built using several underlying components. You can use these individually for more custom modal structures if needed."),
        
        H3(Code("ModalContainer(*c, id, cls, placement, **kwargs)"), link=True, cls="mb-2"),
        P("The outermost container for the modal. Handles visibility, placement, and overflow. Corresponds to ", Code("ModalT.container"), "."),
        Br(),
        
        H3(Code("ModalDialog(*c, cls, **kwargs)"), link=True, cls="mb-2"),
        P("The dialog box itself, containing the modal content. Controls the width (", Code("cls"), ") and basic appearance. Corresponds to ", Code("ModalT.dialog"), " and ", Code("ModalT.dialog_inner"), "."),
        Br(),

        H3(Code("ModalHeader(*c, cls, **kwargs)"), link=True, cls="mb-2"),
        P("The header section, typically containing a title and close button. Corresponds to ", Code("ModalT.header"), "."),
        Br(),

        H3(Code("ModalBody(*c, cls, **kwargs)"), link=True, cls="mb-2"),
        P("The main content area of the modal. Corresponds to ", Code("ModalT.body"), "."),
        Br(),

        H3(Code("ModalFooter(*c, cls, **kwargs)"), link=True, cls="mb-2"),
        P("The footer section, usually containing action buttons. Corresponds to ", Code("ModalT.footer"), "."),
        Br(),

        H3(Code("ModalTitle(*c, cls, **kwargs)"), link=True, cls="mb-2"),
        P("A styled H3 element for the modal title. Corresponds to ", Code("ModalT.title"), "."),
        Br(),

        H3(Code("ModalCloseButton(*c, cls, modal_id, **kwargs)"), link=True, cls="mb-2"),
        P("A pre-styled close button (using an 'X' icon) that can be used in the header. Requires the ", Code("modal_id"), " to target the correct modal container via the ", Code("data-modal-toggle"), " attribute (handled internally). Corresponds to ", Code("ModalT.close_btn"), "."),
        Br(),
    )

# --- Main Showcase Function ---
def modals_showcase():
    """Page showcasing Modal components"""
    return Container(
        H1("Modal Components", link=True, cls="mb-8 mt-6"),
        P("Modals are used to display content in a layer above the main page. Fastbite provides components based on Flowbite's modal structure and requires Flowbite's JavaScript for interaction.", cls="mb-6 text-lg"),

        # Call section functions
        _modal_basic_section(),
        _modal_sizing_section(),
        _modal_placement_section(),
        _modal_subcomponents_section(),
    )

# Make the showcase available to the app
modals_components = modals_showcase() 