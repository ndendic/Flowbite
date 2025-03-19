# Franken Components Implementation Plan

This document outlines a prioritized approach for implementing the remaining components from the Franken library. The plan is organized to maximize impact and create logical groupings of related components.

## Current Progress: 23/138 components (16.7% completed)

## Priority 1: Core UI Elements (Foundation)

These components form the foundation of any UI system and will provide immediate value:

### Card Components (Complete Set)
- [ ] `CardT` - Card styling options enum
- [ ] `CardContainer(*c, cls=CardT.default, **kwargs)` - Card container
- [ ] `CardHeader(*c, cls=(), **kwargs)` - Card header container  
- [ ] `CardBody(*c, cls=(), **kwargs)` - Card body container
- [ ] `CardFooter(*c, cls=(), **kwargs)` - Card footer container
- [ ] `CardTitle(*c, cls=(), **kwargs)` - Card title
- [ ] `Card(*c, header=None, footer=None, body_cls='space-y-6', header_cls=(), footer_cls=(), cls=(), **kwargs)` - Complete card component

**Rationale**: Cards are fundamental UI elements used in nearly every web application. They're relatively simple to implement but provide significant visual structure. Having a complete card system will immediately enhance your UI capabilities.

### Basic Form Elements
- [ ] `Form(*c, cls='space-y-3', **kwargs)` - Form with spacing
- [ ] `Input(*c, cls=(), **kwargs)` - Styled input field
- [ ] `TextArea(*c, cls=(), **kwargs)` - Styled textarea
- [ ] `FormLabel(*c, cls=(), **kwargs)` - Styled form label
- [ ] `LabelInput(label, lbl_cls='', input_cls='', cls='space-y-2', id='', **kwargs)` - Label and input combination
- [ ] `LabelTextArea(label, value='', lbl_cls='', input_cls='', cls='space-y-2', id='', **kwargs)` - Label and textarea combination

**Rationale**: Form elements are essential for any interactive web application. Starting with these basic form components will provide a foundation for more complex form interfaces.

### Navigation Basics
- [ ] `NavT` - Navigation styling options enum
- [ ] `NavBar(*c, brand=H3("Title"), right_cls='items-center space-x-4', mobile_cls='space-y-4', sticky=False, uk_scrollspy_nav=False, cls='p-4', scrollspy_cls=ScrollspyT.underline, menu_id=None)` - Responsive navigation bar

**Rationale**: A navigation bar is a critical UI element for most applications and often one of the first things users interact with.

## Priority 2: Enhanced Functionality

These components build on the foundation and add more sophisticated UI capabilities:

### Interactive Form Elements
- [ ] `CheckboxX(*c, cls=(), **kwargs)` - Styled checkbox
- [ ] `Radio(*c, cls=(), **kwargs)` - Styled radio button
- [ ] `Switch(*c, cls=(), **kwargs)` - Styled toggle switch
- [ ] `Range(*c, value='', label=True, min=None, max=None, step=None, cls=(), **kwargs)` - Styled range input
- [ ] `LabelCheckboxX(label, lbl_cls='', input_cls='', container=Div, cls='flex items-center space-x-2', id='', **kwargs)` - Label and checkbox combination
- [ ] `LabelRadio(label, lbl_cls='', input_cls='', container=Div, cls='flex items-center space-x-2', id='', **kwargs)` - Label and radio combination
- [ ] `LabelSwitch(label, lbl_cls='', input_cls='', cls='space-x-2', id='', **kwargs)` - Label and switch combination
- [ ] `LabelRange(label, lbl_cls='', input_cls='', cls='space-y-6', id='', value='', min=None, max=None, step=None, label_range=True, **kwargs)` - Label and range input combination

**Rationale**: These form elements enable more interactive and diverse user inputs. They build upon the basic form elements and expand your application's interactivity.

### Additional Layout Components
- [ ] `Section(*c, cls=(), **kwargs)` - Section with styling and margins
- [ ] `SectionT` - Section styling options enum
- [ ] `Divider(*c, cls=('my-4', DividerT.icon), **kwargs)` - Divider with styling
- [ ] `DividerT` - Divider styling options enum
- [ ] `DividerSplit(*c, cls=(), line_cls=(), text_cls=())` - Line divider with text
- [ ] `DividerLine(lwidth=2, y_space=4)` - Simple horizontal line divider
- [ ] `Center(*c, vertical=True, horizontal=True, cls=(), **kwargs)` - Centers contents

**Rationale**: These layout components will enhance your ability to structure content with clear visual hierarchy and separation.

### Complete Navigation Suite
- [ ] `NavContainer(*li, cls=NavT.primary, parent=True, uk_nav=False, uk_scrollspy_nav=False, sticky=False, **kwargs)` - Navigation container
- [ ] `NavParentLi(*nav_container, cls=(), **kwargs)` - Navigation list item with nested nav
- [ ] `NavHeaderLi(*c, cls=(), **kwargs)` - Navigation list item with header
- [ ] `NavDividerLi(*c, cls=(), **kwargs)` - Navigation list item with divider
- [ ] `TabContainer(*li, cls='', alt=False, **kwargs)` - Tab container

**Rationale**: Expanding your navigation capabilities will allow for more sophisticated user interfaces and content organization.

## Priority 3: Advanced Components

These components add polish and specialized functionality:

### Modal System
- [ ] `ModalContainer(*c, cls=(), **kwargs)` - Modal container
- [ ] `ModalDialog(*c, cls=(), **kwargs)` - Modal dialog
- [ ] `ModalHeader(*c, cls=(), **kwargs)` - Modal header
- [ ] `ModalBody(*c, cls=(), **kwargs)` - Modal body
- [ ] `ModalFooter(*c, cls=(), **kwargs)` - Modal footer
- [ ] `ModalTitle(*c, cls=(), **kwargs)` - Modal title
- [ ] `ModalCloseButton(*c, cls=(), htmx=False, **kwargs)` - Button to close modal
- [ ] `Modal(*c, header=None, footer=None, cls=(), dialog_cls=(), header_cls='p-6', body_cls='space-y-6', footer_cls=(), id='', open=False, **kwargs)` - Complete modal component

**Rationale**: Modals provide important UI functionality for focused user interactions, confirmations, and forms.

### Advanced Form Controls
- [ ] `Select(*option, inp_cls=(), cls=('h-10',), cls_custom='button: uk-input-fake dropdown: w-full', id="", name="", placeholder="", searchable=False, insertable=False, select_kwargs=None, **kwargs)` - Styled select dropdown
- [ ] `Options(*c, selected_idx=None, disabled_idxs=None)` - Helper for creating select options
- [ ] `LabelSelect(*option, label, lbl_cls='', input_cls='', container=Div, cls='space-y-2', id='', **kwargs)` - Label and select combination
- [ ] `Upload(*c, cls=(), multiple=False, accept=None, button_cls=ButtonT.default, id=None, name=None, **kwargs)` - File upload component
- [ ] `UploadZone(*c, cls=(), multiple=False, accept=None, id=None, name=None, **kwargs)` - File drop zone
- [ ] `UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6)` - Form section with title and description

**Rationale**: These more advanced form components provide specialized functionality for more complex user interactions.

### Text Formatting Components
- [ ] `Subtitle(*c, cls='mt-1.5', **kwargs)` - Text designed to go under headings
- [ ] `Strong(*c, cls=(), **kwargs)` - Styled strong text
- [ ] `Em(*c, cls=(), **kwargs)` - Styled emphasis text
- [ ] `Small(*c, cls=(), **kwargs)` - Styled small text
- [ ] `Mark(*c, cls=(), **kwargs)` - Styled highlighted text
- [ ] `Blockquote(*c, cls=(), **kwargs)` - Blockquote with styling

**Rationale**: These components enhance your typography system with more expressive text formatting options.

## Priority 4: Specialized Components

These components address more specific use cases:

### Table Components
- [ ] `TableT` - Table styling options enum
- [ ] `Table(*c, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), **kwargs)` - Styled table
- [ ] `Td(*c, cls=(), shrink=False, expand=False, small=False, **kwargs)` - Table data cell
- [ ] `Th(*c, cls=(), shrink=False, expand=False, small=False, **kwargs)` - Table header cell
- [ ] `Tbody(*rows, cls=(), sortable=False, **kwargs)` - Table body
- [ ] `TableFromLists(header_data, body_data, footer_data=None, header_cell_render=Th, body_cell_render=Td, footer_cell_render=Td, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), sortable=False, **kwargs)` - Create table from lists
- [ ] `TableFromDicts(header_data, body_data, footer_data=None, header_cell_render=Th, body_cell_render=lambda k,v : Td(v), footer_cell_render=lambda k,v : Td(v), cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), sortable=False, **kwargs)` - Create table from dictionaries

**Rationale**: Tables are important for data-heavy applications, but they're specialized enough to be lower priority.

### Slider Components
- [ ] `SliderContainer(*c, cls='', uk_slider=True, **kwargs)` - Slider container
- [ ] `SliderItems(*c, cls='', **kwargs)` - Slider items container
- [ ] `SliderNav(cls='uk-position-small uk-hidden-hover', prev_cls='absolute left-0 top-1/2 -translate-y-1/2', next_cls='absolute right-0 top-1/2 -translate-y-1/2', **kwargs)` - Navigation arrows for slider
- [ ] `Slider(*c, cls='', items_cls='gap-4', nav=True, nav_cls='', **kwargs)` - Complete slider component

**Rationale**: Sliders provide specialized UI functionality for carousels and image galleries.

### Article Components
- [ ] `Article(*c, cls=(), **kwargs)` - Styled article container
- [ ] `ArticleTitle(*c, cls=(), **kwargs)` - Title for Article
- [ ] `ArticleMeta(*c, cls=(), **kwargs)` - Metadata component for Article

**Rationale**: These components are specialized for content-heavy applications like blogs.

### Utility Components
- [ ] `Progress(*c, cls=(), value="", max="100", **kwargs)` - Progress bar
- [ ] `Placeholder(*c, cls=(), **kwargs)` - Placeholder container
- [ ] `UkIconLink(icon, height=None, width=None, stroke_width=None, cls=(), button=False, **kwargs)` - Icon link or button
- [ ] `ThemePicker(color=True, radii=True, shadows=True, font=True, mode=True, cls='p-4', custom_themes=[])` - Theme selection component
- [ ] `LightboxContainer(*lightboxitem, data_uk_lightbox='counter: true', **kwargs)` - Lightbox container
- [ ] `LightboxItem(*c, href, data_alt=None, data_caption=None, cls='', **kwargs)` - Lightbox item

**Rationale**: These components provide specialized functionality that may not be needed in every application.

## Priority 5: Utility Functions and Remaining Components

### Utility Functions
- [ ] `apply_classes(html_str, class_map=None, class_map_mods=None)` - Apply classes to HTML string
- [ ] `render_md(md_content, class_map=None, class_map_mods=None, img_dir=None)` - Render markdown to HTML
- [ ] `get_franken_renderer(img_dir)` - Create a custom renderer for markdown

**Rationale**: These utilities enhance content rendering but are specialized enough to be lower priority.

### Remaining Components
- All remaining text formatting components (CodeSpan, CodeBlock, etc.)
- All remaining block elements (Figure, Details, Summary, etc.)

## Implementation Strategy

For each priority level:

1. Start by implementing the enums/constants for that section
2. Implement the base components first, then build more complex components on top of them
3. Test each component thoroughly as you implement it
4. Group related components together in your implementation sessions
5. After completing each priority level, review and ensure all components work well together

By following this prioritized approach, you'll build a comprehensive component library that grows in capability while maintaining a logical structure. Focus on completing Priority 1 components first to establish a solid foundation for your UI system. 