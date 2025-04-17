# MonsterUI Franken Components Reference

**Current Progress: 23/138 components (16.7% completed)**

This document provides a reference for all classes and methods available in the `monsterui.franken` module. Check off items that you've already implemented in your project.

## Enums/Constants

- [x] **TextT** - Text styling options
- [x] **TextPresets** - Common typography presets
- [x] **ButtonT** - Button styling options 
- [x] **ContainerT** - Container size options
- [ ] **BackgroundT** - Background style options
- [ ] **DividerT** - Divider styling options
- [ ] **SectionT** - Section styling options
- [ ] **LabelT** - Label styling options
- [ ] **NavT** - Navigation styling options
- [ ] **ScrollspyT** - Scrollspy styling options
- [x] **FlexT** - Flexbox modifiers
- [ ] **CardT** - Card styling options
- [ ] **TableT** - Table styling options
- [ ] **franken_class_map** - Default class mappings for HTML elements

## Typography Components

### Headings
- [x] `H1(*c, cls=(), **kwargs)` - H1 heading with styling
- [x] `H2(*c, cls=(), **kwargs)` - H2 heading with styling
- [x] `H3(*c, cls=(), **kwargs)` - H3 heading with styling
- [x] `H4(*c, cls=(), **kwargs)` - H4 heading with styling
- [x] `H5(*c, cls=(), **kwargs)` - H5 heading with styling
- [x] `H6(*c, cls=(), **kwargs)` - H6 heading with styling
- [ ] `Subtitle(*c, cls='mt-1.5', **kwargs)` - Text designed to go under headings

### Code
- [ ] `CodeSpan(*c, cls=(), **kwargs)` - Inline code snippet
- [ ] `CodeBlock(*c, cls=(), code_cls=(), **kwargs)` - Block of code with styling

### Text Formatting
- [ ] `Q(*c, cls=(), **kwargs)` - Styled quotation mark
- [ ] `Em(*c, cls=(), **kwargs)` - Styled emphasis text
- [ ] `Strong(*c, cls=(), **kwargs)` - Styled strong text
- [ ] `I(*c, cls=(), **kwargs)` - Styled italic text
- [ ] `Small(*c, cls=(), **kwargs)` - Styled small text
- [ ] `Mark(*c, cls=(), **kwargs)` - Styled highlighted text
- [ ] `Del(*c, cls=(), **kwargs)` - Styled deleted text
- [ ] `Ins(*c, cls=(), **kwargs)` - Styled inserted text
- [ ] `Sub(*c, cls=(), **kwargs)` - Styled subscript text
- [ ] `Sup(*c, cls=(), **kwargs)` - Styled superscript text
- [ ] `S(*c, cls=(), **kwargs)` - Styled strikethrough text
- [ ] `U(*c, cls=(), **kwargs)` - Styled underline

### Block Elements
- [ ] `Blockquote(*c, cls=(), **kwargs)` - Blockquote with styling
- [ ] `Caption(*c, cls=(), **kwargs)` - Styled caption text
- [ ] `Cite(*c, cls=(), **kwargs)` - Styled citation text
- [ ] `Time(*c, cls=(), datetime=None, **kwargs)` - Styled time element
- [ ] `Address(*c, cls=(), **kwargs)` - Styled address element
- [ ] `Abbr(*c, cls=(), title=None, **kwargs)` - Styled abbreviation
- [ ] `Dfn(*c, cls=(), **kwargs)` - Styled definition term
- [ ] `Kbd(*c, cls=(), **kwargs)` - Styled keyboard input
- [ ] `Samp(*c, cls=(), **kwargs)` - Styled sample output
- [ ] `Var(*c, cls=(), **kwargs)` - Styled variable
- [ ] `Figure(*c, cls=(), **kwargs)` - Styled figure container
- [ ] `Details(*c, cls=(), **kwargs)` - Styled details element
- [ ] `Summary(*c, cls=(), **kwargs)` - Styled summary element
- [ ] `Data(*c, value=None, cls=(), **kwargs)` - Styled data element
- [x] `Meter(*c, value=None, min=None, max=None, cls=(), **kwargs)` - Styled meter element
- [ ] `Output(*c, form=None, for_=None, cls=(), **kwargs)` - Styled output element

## Layout Components

### Containers
- [x] `Container(*c, cls=('mt-5', ContainerT.xl), **kwargs)` - Container for wrapping content
- [ ] `Titled(title="FastHTML app", *c, cls=ContainerT.xl, **kwargs)` - Standard page structure with title
- [ ] `Section(*c, cls=(), **kwargs)` - Section with styling and margins
- [ ] `Divider(*c, cls=('my-4', DividerT.icon), **kwargs)` - Divider with styling
- [ ] `DividerSplit(*c, cls=(), line_cls=(), text_cls=())` - Line divider with text
- [ ] `DividerLine(lwidth=2, y_space=4)` - Simple horizontal line divider
- [ ] `Article(*c, cls=(), **kwargs)` - Styled article container
- [ ] `ArticleTitle(*c, cls=(), **kwargs)` - Title for Article
- [ ] `ArticleMeta(*c, cls=(), **kwargs)` - Metadata component for Article

### Flexbox Layouts
- [ ] `Center(*c, vertical=True, horizontal=True, cls=(), **kwargs)` - Centers contents
- [x] `Grid(*div, cols_min=1, cols_max=4, cols_sm=None, cols_md=None, cols_lg=None, cols_xl=None, cols=None, cls='gap-4', **kwargs)` - Responsive grid layout
- [x] `DivFullySpaced(*c, cls='w-full', **kwargs)` - Div with maximally spaced components
- [x] `DivCentered(*c, cls='space-y-4', vstack=True, **kwargs)` - Div with centered components
- [x] `DivLAligned(*c, cls='space-x-4', **kwargs)` - Div with left-aligned components
- [x] `DivRAligned(*c, cls='space-x-4', **kwargs)` - Div with right-aligned components
- [x] `DivVStacked(*c, cls='space-y-4', **kwargs)` - Div with vertically stacked components
- [x] `DivHStacked(*c, cls='space-x-4', **kwargs)` - Div with horizontally stacked components

## UI Components

### Buttons
- [x] `Button(*c, cls=ButtonT.default, submit=True, **kwargs)` - Styled button

### Form Elements
- [ ] `Form(*c, cls='space-y-3', **kwargs)` - Form with spacing
- [ ] `Fieldset(*c, cls=(), **kwargs)` - Styled fieldset
- [ ] `Legend(*c, cls=(), **kwargs)` - Styled legend
- [ ] `Input(*c, cls=(), **kwargs)` - Styled input field
- [ ] `Radio(*c, cls=(), **kwargs)` - Styled radio button
- [ ] `CheckboxX(*c, cls=(), **kwargs)` - Styled checkbox
- [ ] `Range(*c, value='', label=True, min=None, max=None, step=None, cls=(), **kwargs)` - Styled range input
- [ ] `TextArea(*c, cls=(), **kwargs)` - Styled textarea
- [ ] `Switch(*c, cls=(), **kwargs)` - Styled toggle switch
- [ ] `Upload(*c, cls=(), multiple=False, accept=None, button_cls=ButtonT.default, id=None, name=None, **kwargs)` - File upload component
- [ ] `UploadZone(*c, cls=(), multiple=False, accept=None, id=None, name=None, **kwargs)` - File drop zone
- [ ] `FormLabel(*c, cls=(), **kwargs)` - Styled form label
- [ ] `Label(*c, cls=(), **kwargs)` - Pill-style label

### Form Combinations
- [ ] `UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6)` - Form section with title and description
- [ ] `GenericLabelInput(label, lbl_cls='', input_cls='', container=Div, cls='', id=None, input_fn=noop, **kwargs)` - Base for label+input combinations
- [ ] `LabelInput(label, lbl_cls='', input_cls='', cls='space-y-2', id='', **kwargs)` - Label and input combination
- [ ] `LabelTextArea(label, value='', lbl_cls='', input_cls='', cls='space-y-2', id='', **kwargs)` - Label and textarea combination
- [ ] `LabelSwitch(label, lbl_cls='', input_cls='', cls='space-x-2', id='', **kwargs)` - Label and switch combination
- [ ] `LabelRadio(label, lbl_cls='', input_cls='', container=Div, cls='flex items-center space-x-2', id='', **kwargs)` - Label and radio combination
- [ ] `LabelCheckboxX(label, lbl_cls='', input_cls='', container=Div, cls='flex items-center space-x-2', id='', **kwargs)` - Label and checkbox combination
- [ ] `LabelSelect(*option, label, lbl_cls='', input_cls='', container=Div, cls='space-y-2', id='', **kwargs)` - Label and select combination
- [ ] `Options(*c, selected_idx=None, disabled_idxs=None)` - Helper for creating select options
- [ ] `Select(*option, inp_cls=(), cls=('h-10',), cls_custom='button: uk-input-fake dropdown: w-full', id="", name="", placeholder="", searchable=False, insertable=False, select_kwargs=None, **kwargs)` - Styled select dropdown
- [ ] `LabelRange(label, lbl_cls='', input_cls='', cls='space-y-6', id='', value='', min=None, max=None, step=None, label_range=True, **kwargs)` - Label and range input combination

### Navigation
- [ ] `NavContainer(*li, cls=NavT.primary, parent=True, uk_nav=False, uk_scrollspy_nav=False, sticky=False, **kwargs)` - Navigation container
- [ ] `NavParentLi(*nav_container, cls=(), **kwargs)` - Navigation list item with nested nav
- [ ] `NavDividerLi(*c, cls=(), **kwargs)` - Navigation list item with divider
- [ ] `NavHeaderLi(*c, cls=(), **kwargs)` - Navigation list item with header
- [ ] `NavSubtitle(*c, cls=TextPresets.muted_sm, **kwargs)` - Navigation subtitle
- [ ] `NavCloseLi(*c, cls=(), **kwargs)` - Navigation list item with close button
- [ ] `NavBar(*c, brand=H3("Title"), right_cls='items-center space-x-4', mobile_cls='space-y-4', sticky=False, uk_scrollspy_nav=False, cls='p-4', scrollspy_cls=ScrollspyT.underline, menu_id=None)` - Responsive navigation bar
- [ ] `DropDownNavContainer(*li, cls=NavT.primary, parent=True, uk_nav=False, uk_dropdown=True, **kwargs)` - Dropdown navigation container
- [ ] `TabContainer(*li, cls='', alt=False, **kwargs)` - Tab container

### Cards
- [ ] `CardTitle(*c, cls=(), **kwargs)` - Card title
- [ ] `CardHeader(*c, cls=(), **kwargs)` - Card header container
- [ ] `CardBody(*c, cls=(), **kwargs)` - Card body container
- [ ] `CardFooter(*c, cls=(), **kwargs)` - Card footer container
- [ ] `CardContainer(*c, cls=CardT.default, **kwargs)` - Card container
- [ ] `Card(*c, header=None, footer=None, body_cls='space-y-6', header_cls=(), footer_cls=(), cls=(), **kwargs)` - Complete card component

### Tables
- [ ] `Table(*c, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), **kwargs)` - Styled table
- [ ] `Td(*c, cls=(), shrink=False, expand=False, small=False, **kwargs)` - Table data cell
- [ ] `Th(*c, cls=(), shrink=False, expand=False, small=False, **kwargs)` - Table header cell
- [ ] `Tbody(*rows, cls=(), sortable=False, **kwargs)` - Table body
- [ ] `TableFromLists(header_data, body_data, footer_data=None, header_cell_render=Th, body_cell_render=Td, footer_cell_render=Td, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), sortable=False, **kwargs)` - Create table from lists
- [ ] `TableFromDicts(header_data, body_data, footer_data=None, header_cell_render=Th, body_cell_render=lambda k,v : Td(v), footer_cell_render=lambda k,v : Td(v), cls=(TableT.middle, TableT.divider, TableT.hover, TableT.sm), sortable=False, **kwargs)` - Create table from dictionaries

### Modal Components
- [ ] `ModalContainer(*c, cls=(), **kwargs)` - Modal container
- [ ] `ModalDialog(*c, cls=(), **kwargs)` - Modal dialog
- [ ] `ModalHeader(*c, cls=(), **kwargs)` - Modal header
- [ ] `ModalBody(*c, cls=(), **kwargs)` - Modal body
- [ ] `ModalFooter(*c, cls=(), **kwargs)` - Modal footer
- [ ] `ModalTitle(*c, cls=(), **kwargs)` - Modal title
- [ ] `ModalCloseButton(*c, cls=(), htmx=False, **kwargs)` - Button to close modal
- [ ] `Modal(*c, header=None, footer=None, cls=(), dialog_cls=(), header_cls='p-6', body_cls='space-y-6', footer_cls=(), id='', open=False, **kwargs)` - Complete modal component

### Sliders
- [ ] `SliderContainer(*c, cls='', uk_slider=True, **kwargs)` - Slider container
- [ ] `SliderItems(*c, cls='', **kwargs)` - Slider items container
- [ ] `SliderNav(cls='uk-position-small uk-hidden-hover', prev_cls='absolute left-0 top-1/2 -translate-y-1/2', next_cls='absolute right-0 top-1/2 -translate-y-1/2', **kwargs)` - Navigation arrows for slider
- [ ] `Slider(*c, cls='', items_cls='gap-4', nav=True, nav_cls='', **kwargs)` - Complete slider component

### Miscellaneous Components
- [x] `PicSumImg(h=200, w=200, id=None, grayscale=False, blur=None, **kwargs)` - Placeholder image
- [ ] `Placeholder(*c, cls=(), **kwargs)` - Placeholder container
- [ ] `Progress(*c, cls=(), value="", max="100", **kwargs)` - Progress bar
- [x] `UkIcon(icon, height=None, width=None, stroke_width=None, cls=(), **kwargs)` - Lucide icon (similar to `Icon` in components.py)
- [ ] `UkIconLink(icon, height=None, width=None, stroke_width=None, cls=(), button=False, **kwargs)` - Icon link or button
- [x] `DiceBearAvatar(seed_name, h=20, w=20)` - Avatar using DiceBear
- [ ] `ThemePicker(color=True, radii=True, shadows=True, font=True, mode=True, cls='p-4', custom_themes=[])` - Theme selection component
- [ ] `LightboxContainer(*lightboxitem, data_uk_lightbox='counter: true', **kwargs)` - Lightbox container
- [ ] `LightboxItem(*c, href, data_alt=None, data_caption=None, cls='', **kwargs)` - Lightbox item

## Utility Functions

- [ ] `apply_classes(html_str, class_map=None, class_map_mods=None)` - Apply classes to HTML string
- [ ] `render_md(md_content, class_map=None, class_map_mods=None, img_dir=None)` - Render markdown to HTML
- [ ] `get_franken_renderer(img_dir)` - Create a custom renderer for markdown