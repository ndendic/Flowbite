from fasthtml.components import *
from fasthtml.svg import *
from fastbite.all import *
from utils import component_showcase

typography = Div(
    H1("Typography", cls="group"),
    P("Typography is the art and technique of arranging text to make it more appealing and readable. It involves selecting fonts, adjusting spacing, and using various techniques to create a visually pleasing and effective text layout."),
    P("This page demonstrates the typography components and styling options available in Fastbite, including headings, paragraphs, text sizing, spacing, weights, and semantic text elements. These tools provide a consistent approach to text styling across your application."),
    P("All typography components are designed to be responsive, accessible, and compatible with both light and dark themes. They follow semantic HTML practices while providing enhanced visual styling."),

    H2("Headings", link=True),
    P("Heading components (", Code("H1-H6"), ") provide semantically correct HTML heading elements with appropriate styling."),
    P("Each heading has pre-defined sizes and styling that follow proper document hierarchy."),
    component_showcase(
            H1("Linked Heading 1", link=True),
            H1("Heading 1"),
            H2("Heading 2"),
            H3("Heading 3"),
            H3("Linked Heading 3", link=True),
            H4("Heading 4"),
            H5("Heading 5"),
            H6("Heading 6"),
            H6("Linked Heading 6", link=True),
            code="""H1("Linked Heading 1", link=True),
H1("Heading 1"),
H2("Heading 2"),
H3("Heading 3"),
H3("Linked Heading 3", link=True),
H4("Heading 4"),
H5("Heading 5"),
H6("Heading 6"),
H6("Linked Heading 6", link=True),""",
            id="headings"
        ),
    Br(),

    H2("Paragraph Styles", link=True),
    P("The ", Code("PT"), " enum provides various paragraph styling options for different content needs. These styles help create visual hierarchy and improve readability."),
    component_showcase(
        P("This is a default paragraph style with appropriate text color and spacing.", cls=PT.default),
        code="""P("This is a default paragraph style with appropriate text color and spacing.", cls=PT.default)""",
        id="paragraph-default"
    ),
    Br(),

    H3("Lead Paragraph"),
    P("Use the ", Code("PT.lead"), " style for introductory paragraphs that should stand out with larger text."),
    component_showcase(
        P("This is a lead paragraph with larger font size, perfect for introductions or important information.", cls=PT.lead),
        code="""P("This is a lead paragraph with larger font size, perfect for introductions or important information.", cls=PT.lead)""",
        id="paragraph-lead"
    ),
    Br(),

    H3("Capitalized First Letter"),
    P("The ", Code("PT.capital_first"), " style creates a decorative drop cap effect with the first letter enlarged and the first line capitalized."),
    component_showcase(
        P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dignissim enim et magna pharetra, at commodo elit tincidunt. Donec vel massa at dolor condimentum suscipit vel id nulla. Fusce commodo nibh sit amet urna pharetra, eget euismod orci luctus.", cls=PT.capital_first),
        code="""P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dignissim enim et magna pharetra, at commodo elit tincidunt. Donec vel massa at dolor condimentum suscipit vel id nulla. Fusce commodo nibh sit amet urna pharetra, eget euismod orci luctus.", cls=PT.capital_first)""",
        id="paragraph-capital-first"
    ),
    Br(),

    H3("Link Style"),
    P("The ", Code("PT.link"), " style formats text to appear as a clickable link with proper color and hover effects."),
    component_showcase(
        P("This paragraph is styled to look like a clickable link with appropriate colors and hover effects.", cls=PT.link),
        code="""P("This paragraph is styled to look like a clickable link with appropriate colors and hover effects.", cls=PT.link)""",
        id="paragraph-link"
    ),
    Br(),

    H3("Colored Paragraphs"),
    P("Use semantic color styles like ", Code("PT.primary"), " and ", Code("PT.secondary"), " to communicate importance or relationships."),
    component_showcase(
        Div(
            P("This paragraph uses the primary color scheme for emphasis.", cls=PT.primary),
            P("This paragraph uses the secondary color scheme for supporting information.", cls=PT.secondary)
        ),
        code="""P("This paragraph uses the primary color scheme for emphasis.", cls=PT.primary),
P("This paragraph uses the secondary color scheme for supporting information.", cls=PT.secondary)""",
        id="paragraph-colors"
    ),
    Br(),

    H3("Size Variants"),
    P("Control paragraph text size with size-specific classes like ", Code("PT.xs"), " and ", Code("PT.sm"), " for different content needs."),
    component_showcase(
        Div(
            P("This extra small paragraph is useful for captions, footnotes, or less important information.", cls=PT.xs),
            P("This small paragraph works well for secondary content while maintaining readability.", cls=PT.sm)
        ),
        code="""P("This extra small paragraph is useful for captions, footnotes, or less important information.", cls=PT.xs),
P("This small paragraph works well for secondary content while maintaining readability.", cls=PT.sm)""",
        id="paragraph-sizes"
    ),
    Br(),

    H2("List Styles", link=True),
    P("Lists help organize content in a structured way. The ", Code("ListT"), " enum provides various list styling options to handle different types of content organization."),
    component_showcase(
        Div(
            P("Unordered List (", Code("ListT.ul"), "):"),
            Ul(
                Li("First list item"),
                Li("Second list item"),
                Li("Third list item"),
                cls=ListT.ul
            ),
            Br(),
            P("Ordered List (", Code("ListT.ol"), "):"),
            Ol(
                Li("First list item"),
                Li("Second list item"),
                Li("Third list item"),
                cls=ListT.ol
            )
        ),
        code="""# Unordered List
Ul(
    Li("First list item"),
    Li("Second list item"),
    Li("Third list item"),
    cls=ListT.ul
)

# Ordered List
Ol(
    Li("First list item"),
    Li("Second list item"),
    Li("Third list item"),
    cls=ListT.ol
)""",
        id="basic-lists"
    ),
    Br(),

    H3("Definition Lists"),
    P("Definition lists (", Code("ListT.dl"), ") are perfect for displaying term-definition pairs like glossaries or metadata."),
    component_showcase(
        Dl(
            Dt("Typography", cls=ListT.dt),
            Dd("The art and technique of arranging type to make written language legible, readable, and appealing.", cls=ListT.dd),
            Dt("Responsive Design", cls=ListT.dt),
            Dd("An approach to web design that makes web pages render well on various devices and window/screen sizes.", cls=ListT.dd),
            cls=ListT.dl
        ),
        code="""Dl(
    Dt("Typography", cls=ListT.dt),
    Dd("The art and technique of arranging type to make written language legible, readable, and appealing.", cls=ListT.dd),
    Dt("Responsive Design", cls=ListT.dt),
    Dd("An approach to web design that makes web pages render well on various devices and window/screen sizes.", cls=ListT.dd),
    cls=ListT.dl
)""",
        id="definition-lists"
    ),
    Br(),

    H3("Horizontal Lists"),
    P("Horizontal lists (", Code("ListT.horizontal"), ") display list items in a row instead of a column, ideal for navigation menus or tags."),
    component_showcase(
        P("# Horizontal default"),
        Ul(
            Li("Home"),
            Li("Products"),
            Li("Services"),
            Li("About"),
            Li("Contact"),
            cls=ListT.horizontal+"gap-x-2"
        ),
        P("# Horizontal center"),
        Ul(
            Li("Home"),
            Li("Products"),
            Li("Services"),
            Li("About"),
            Li("Contact"),
            cls=ListT.horizontal_center+"gap-x-2"
        ),
        code="""Ul(
    Li("Home"),
    Li("Products"),
    Li("Services"),
    Li("About"),
    Li("Contact"),
    cls=ListT.horizontal+"gap-x-2"
),
Ul(
    Li("Home"),
    Li("Products"),
    Li("Services"),
    Li("About"),
    Li("Contact"),
    cls=ListT.horizontal_center+"gap-x-2"
)""",
        id="horizontal-lists"
    ),
    Br(),

    H3("Unstyled Lists"),
    P("Unstyled lists (", Code("ListT.unstyled"), ") remove the default bullet points or numbers, providing a clean base for custom styling."),
    component_showcase(
        Ul(
            Li("First list item"),
            Li("Second list item"),
            Li("Third list item"),
            cls=ListT.unstyled
        ),
        code="""Ul(
    Li("First list item"),
    Li("Second list item"),
    Li("Third list item"),
    cls=ListT.unstyled
)""",
        id="unstyled-lists"
    ),
    Br(),

    H3("Nested Lists"),
    P("Create hierarchical content organization with nested lists using ", Code("ListT.nested_ul"), " and ", Code("ListT.nested_ol"), "."),
    component_showcase(
        Ul(
            Li("Main item 1"),
            Li(
                "Main item 2",
                Ul(
                    Li("Nested item 2.1"),
                    Li("Nested item 2.2"),
                    Li(
                        "Nested item 2.3",
                        Ol(
                            Li("Deep nested item 2.3.1"),
                            Li("Deep nested item 2.3.2"),
                            cls=ListT.nested_ol
                        )
                    ),
                    cls=ListT.nested_ul
                )
            ),
            Li("Main item 3"),
            cls=ListT.ul
        ),
        code="""Ul(
    Li("Main item 1"),
    Li(
        "Main item 2",
        Ul(
            Li("Nested item 2.1"),
            Li("Nested item 2.2"),
            Li(
                "Nested item 2.3",
                Ol(
                    Li("Deep nested item 2.3.1"),
                    Li("Deep nested item 2.3.2"),
                    cls=ListT.nested_ol
                )
            ),
            cls=ListT.nested_ul
        )
    ),
    Li("Main item 3"),
    cls=ListT.ul
)""",
        id="nested-lists"
    ),
    Br(),

    H2("Text size"),
    P("Control the font size of text using", Code("TextT"), "enum classes. These classes provide consistent sizing across your application. The size scale ranges from xs (extra small) to 9xl, giving you fine-grained control over text dimensions."),
    component_showcase(DivHStacked(
    P("xs ", cls=TextT.xs),
    P("sm", cls=TextT.sm),
    P("base", cls=TextT.base),
    P("lg", cls=TextT.lg),
    P("xl", cls=TextT.xl),
    P("2xl", cls=TextT.text_2xl),
    P("3xl", cls=TextT.text_3xl),
    P("4xl", cls=TextT.text_4xl),
    P("5xl", cls=TextT.text_5xl),
    P("6xl", cls=TextT.text_6xl),
    P("7xl", cls=TextT.text_7xl),
    P("8xl", cls=TextT.text_8xl),
    P("9xl", cls=TextT.text_9xl), cls="gap-2"),
    code="""P("xs ", cls=TextT.xs),
P("sm", cls=TextT.sm),
P("base", cls=TextT.base),
P("lg", cls=TextT.lg),
P("xl", cls=TextT.xl),
P("2xl", cls=TextT.text_2xl),
P("3xl", cls=TextT.text_3xl),
P("4xl", cls=TextT.text_4xl),
P("5xl", cls=TextT.text_5xl),
P("6xl", cls=TextT.text_6xl),
P("7xl", cls=TextT.text_7xl),
P("8xl", cls=TextT.text_8xl),
P("9xl", cls=TextT.text_9xl),""",
    id="text-size"
),
    Br(),

    H2("Tracking Styling"),
    P("Control letter spacing (tracking) with", Code(" TextT "), "classes. Tracking adjusts the space between characters to improve readability or create visual effects."),
    P("Options range from", Code(" tracking_tighter "), "(reduced spacing) to", Code(" tracking_widest "), "(maximum spacing)."),
    component_showcase(
        P("Tracking Styling", cls=TextT.tracking_tighter),
        P("Tracking Styling", cls=TextT.tracking_tight),
        P("Tracking Styling", cls=TextT.tracking_normal),
        P("Tracking Styling", cls=TextT.tracking_wide),
        P("Tracking Styling", cls=TextT.tracking_wider),
        P("Tracking Styling", cls=TextT.tracking_widest),
    code="""P("Tracking Styling", cls=TextT.tracking_tighter),
P("Tracking Styling", cls=TextT.tracking_tight),
P("Tracking Styling", cls=TextT.tracking_normal),
P("Tracking Styling", cls=TextT.tracking_wide),
P("Tracking Styling", cls=TextT.tracking_wider),
P("Tracking Styling", cls=TextT.tracking_widest),""",
    id="tracking"
    ),
    Br(),

    H2("Highlight and color"),
    P("Apply semantic color styling to your text with ", Code("TextT"), " class variants. These colors communicate meaning and improve visual hierarchy."),
    P("Options include ", Code("highlight"), " for general emphasis, ", Code("muted"), " for less important text, and semantic colors like ", Code("primary"), " , ", Code("success"), " , and ", Code("error"), "."),
    component_showcase(
        P("Highlight Styling", cls=TextT.highlight),
        P("Highlight muted", cls=TextT.muted),
        P("Highlight primary", cls=TextT.primary),
        P("Highlight secondary", cls=TextT.secondary),
        P("Highlight success", cls=TextT.success),
        P("Highlight warning", cls=TextT.warning),
        P("Highlight error", cls=TextT.error),
        code="""P("Highlight Styling", cls=TextT.highlight),
P("Highlight muted", cls=TextT.muted),
P("Highlight primary", cls=TextT.primary),
P("Highlight secondary", cls=TextT.secondary),
P("Highlight success", cls=TextT.success),
P("Highlight warning", cls=TextT.warning),
P("Highlight error", cls=TextT.error),""",
        id="highlight-color"
    ),
    Br(),

    H2("Text weight"),
    P("Control the font weight using ", Code("TextT"), " weight classes. Font weight determines the thickness of text characters."),
    P("Options range from ", Code("thin"), " (lightest) to ", Code("black"), " (heaviest), providing precise control over text emphasis."),
    component_showcase(
        P("Text weight thin", cls=TextT.thin),
        P("Text weight extralight", cls=TextT.extralight),
        P("Text weight light", cls=TextT.light),
        P("Text weight normal", cls=TextT.normal),
        P("Text weight medium", cls=TextT.medium),
        P("Text weight semibold", cls=TextT.semibold),
        P("Text weight bold", cls=TextT.bold),
        P("Text weight extrabold", cls=TextT.extrabold),
        P("Text weight black", cls=TextT.black),
        code="""P("Text weight thin", cls=TextT.thin),
P("Text weight extralight", cls=TextT.extralight),
P("Text weight light", cls=TextT.light),
P("Text weight normal", cls=TextT.normal),
P("Text weight medium", cls=TextT.medium),
P("Text weight semibold", cls=TextT.semibold),
P("Text weight bold", cls=TextT.bold),
P("Text weight extrabold", cls=TextT.extrabold),
P("Text weight black", cls=TextT.black),""",
        id="text-weight"
    ),
    Br(),

    H2("Text style"),
    P("Apply different text styling effects with ", Code("TextT"), " classes. These include italic text, underlined text, and text transformations."),
    P("These styles help highlight information and create visual distinctions within your content."),
    component_showcase(
        P("Text style italic", cls=TextT.italic),
        P("Text style normal", cls=TextT.normal),
        P("Text style underline", cls=TextT.underline),
        P("Text style line-through", cls=TextT.line_through),
        P("Text style uppercase", cls=TextT.uppercase),
        P("Text style lowercase", cls=TextT.lowercase),
        P("Text style capitalize", cls=TextT.capitalize),
        P("Text style normal-case", cls=TextT.normal_case),
        code="""P("Text style italic", cls=TextT.italic),
P("Text style normal", cls=TextT.normal),
P("Text style underline", cls=TextT.underline),
P("Text style line-through", cls=TextT.line_through),
P("Text style uppercase", cls=TextT.uppercase),
P("Text style lowercase", cls=TextT.lowercase),
P("Text style capitalize", cls=TextT.capitalize),
P("Text style normal-case", cls=TextT.normal_case),""",
        id="text-style"
    ),
    Br(),

    H2("Text alignment"),
    P("Control text alignment with ", Code("TextT"), " alignment classes. Proper text alignment improves readability and complements your layout design."),
    P("Choose from left, right, center, justify, start, and end alignment options to best fit your content needs."),
    component_showcase(
        P("Text alignment left", cls=TextT.left),
        P("Text alignment right", cls=TextT.right),
        P("Text alignment center", cls=TextT.center),
        P("Text alignment justify", cls=TextT.justify),
        P("Text alignment start", cls=TextT.start),
        P("Text alignment end", cls=TextT.end),
        code="""P("Text alignment left", cls=TextT.left),
P("Text alignment right", cls=TextT.right),
P("Text alignment center", cls=TextT.center),
P("Text alignment justify", cls=TextT.justify),
P("Text alignment start", cls=TextT.start),
P("Text alignment end", cls=TextT.end),""",
        id="text-alignment"
    ),
    Br(),
    H2("Code"),
    P("Display code snippets with ", Code("CodeSpan"), " for inline code and ", Code("CodeBlock"), " for multi-line code blocks."),
    P("These components maintain proper formatting and provide visual distinction for code elements."),
    component_showcase(
        Div(
            P("Inline code: ", CodeSpan("Button(\"Click me\", cls=ButtonT.primary)")),
            Br(),
            P("Code block:"),
            CodeBlock(
                """Button("Default", cls=ButtonT.default),
    Button("Alternative", cls=ButtonT.alternative),
    Button("Dark", cls=ButtonT.dark),
    Button("Light", cls=ButtonT.light),"""
            )
        ),
        code="""P("Inline code: ", CodeSpan("Button(\"Click me\", cls=ButtonT.primary)")),

# Multi-line code block
CodeBlock(
    '''Button("Default", cls=ButtonT.default),
Button("Alternative", cls=ButtonT.alternative),
Button("Dark", cls=ButtonT.dark),
Button("Light", cls=ButtonT.light),'''
)""",
        id="code"
    ),
    Br(),
    H2("Keyboard Inputs"),
    P("Display keyboard shortcuts or inputs with the ", Code("Kbd"), " component. This component helps users identify keyboard combinations."),
    P("Choose between ", Code("TextT.kbd_default"), " and ", Code("TextT.kbd_advanced"), " styles to match your design needs."),
    component_showcase(
        Div(
            P("Default style: ", Kbd("Ctrl + S")),
            P("Advanced style: ", Kbd("Ctrl + Alt + Del", cls=TextT.kbd_advanced))
        ),
        code="""P("Default style: ", Kbd("Ctrl + S")),
P("Advanced style: ", Kbd("Ctrl + Alt + Del", cls=TextT.kbd_advanced))""",
        id="keyboard-inputs"
    ),
    Br(),



    H2("Special tags"),
    P("HTML provides several semantic tags for specific content types. These tags enhance accessibility and provide proper content structure."),
    Br(),

    H3("Blockquote"),
    P("Use ", Code("Blockquote"), " component to display quoted content with styling that visually separates it from regular text."),
    component_showcase(
        Blockquote(
            '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."'
        ),
        code="""Blockquote(
    '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."'
)""",
        id="blockquote-default"
    ),
    Br(),

    H4("Blockquote with icon"),
    P("Add a quotation icon to your blockquote by setting the ", Code("with_icon"), " parameter to ", Code("True"), "."),
    component_showcase(
        Blockquote(
            '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
            with_icon=True
        ),
        code="""Blockquote(
    '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
    with_icon=True
)""",
        id="blockquote-with-icon"
    ),
    Br(),

    H4("Blockquote with solid background"),
    P("Apply a solid background style to your blockquote using the ", Code("BlockquoteT.solid"), " class."),
    component_showcase(
        Blockquote(
            '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
            cls=BlockquoteT.solid
        ),
        code="""Blockquote(
    '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
    cls=BlockquoteT.solid
)""",
        id="blockquote-solid"
    ),
    Br(),

    H4("Blockquote with solid background and icon"),
    P("Combine both solid background and icon for a more prominent quotation display."),
    component_showcase(
        Blockquote(
            '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
            with_icon=True,
            cls=BlockquoteT.solid
        ),
        code="""Blockquote(
    '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."',
    with_icon=True,
    cls=BlockquoteT.solid
)""",
        id="blockquote-solid-icon"
    ),
    Br(),

    H3("Text markup tags"),
    P("HTML provides several semantic tags for marking up text with specific meaning. These components help create more accessible and semantically rich content."),
    component_showcase(
        Div(
            P("Deleted text (", Code("Del"), "):"),
            Del("This text has been deleted or removed."),
            Br(),
            P("Inserted text (", Code("Ins"), "):"),
            Ins("This text has been added or inserted."),
            Br(),
            P("Highlighted text (", Code("Mark"), "):"),
            Mark("This text is highlighted for emphasis."),
            Br(),
            P("Subscript (", Code("Sub"), "):"),
            P("H", Sub("2"), "O is the chemical formula for water."),
            Br(),
            P("Superscript (", Code("Sup"), "):"),
            P("E=mc", Sup("2"), " is Einstein's mass-energy equivalence formula.")
        ),
        code="""# Deleted text
Del("This text has been deleted or removed."),

# Inserted text
Ins("This text has been added or inserted."),

# Highlighted text
Mark("This text is highlighted for emphasis."),

# Subscript
P("H", Sub("2"), "O is the chemical formula for water."),

# Superscript
P("E=mc", Sup("2"), " is Einstein's mass-energy equivalence formula.")""",
        id="text-markup"
    ),
    Br(),

    H3("Typography semantic tags"),
    P("Use semantic typography tags to add proper meaning to text elements. These components provide visual styling that matches their semantic purpose."),
    component_showcase(
        Div(
            P("Strikethrough (", Code("S"), "):"),
            S("This text is visually crossed out."),
            Br(),
            P("Small text (", Code("Small"), "):"),
            Small("This text appears smaller than standard text."),
            Br(),
            P("Strong emphasis (", Code("Strong"), "):"),
            Strong("This text has strong importance."),
            Br(), 
            P("Citation (", Code("Cite"), "):"),
            Cite("The Origin of Species, by Charles Darwin"),
            Br(),
            P("Definition (", Code("Dfn"), "):"),
            Dfn("Typography: the art and technique of arranging type.")
        ),
        code="""# Strikethrough
S("This text is visually crossed out."),

# Small text
Small("This text appears smaller than standard text."),

# Strong emphasis
Strong("This text has strong importance."),

# Citation
Cite("The Origin of Species, by Charles Darwin"),

# Definition
Dfn("Typography: the art and technique of arranging type.")""",
        id="semantic-typography"
    ),
    Br(),

    H3("Interactive elements"),
    P("Use interactive elements to create expandable content sections and provide additional context to users."),
    component_showcase(
        Div(
            P("Details with summary:"),
            Details(
                P("This content is hidden until the user clicks the summary element."),
                cls="cursor-pointer",
                summary = "Click to expand content",                
            ),
            Br(),
            P("Abbreviation (", Code("Abbr"), "):"),
            P("The ", Abbr("HTML", title="HyperText Markup Language"), " standard is maintained by the W3C.")
        ),
        code="""# Details with summary
Details(
    P("This content is hidden until the user clicks the summary element."),
    cls="cursor-pointer",
    summary = "Click to expand content",                
),

# Abbreviation
P("The ", Abbr("HTML", title="HyperText Markup Language"), " standard is maintained by the W3C.")""",
        id="interactive-elements"
    ),
    Br(),

    H3("Specialized elements"),
    P("Use specialized elements for specific content types like address information, time, and measurements."),
    component_showcase(
        Div(
            P("Address:"),
            Address("123 Web Development Lane, Internet City, Web 12345"),
            Br(),
            P("Time:"),
            Time("2023-04-01T13:45:00", datetime="2023-04-01T13:45:00"),
            Br(),
            # P("Meter (progress indicator):"),
            # Meter(value=70, min=0, max=100)
        ),
        code="""# Address
Address("123 Web Development Lane, Internet City, Web 12345"),

# Time
Time("2023-04-01T13:45:00", datetime="2023-04-01T13:45:00")""",
        id="specialized-elements"
    ),
    Br(),
   
    
    # Div(cls="relative max-w-sm")(
    #     Div(
    #         cls="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none"
    #     )(
    #         Svg(
    #             aria_hidden="true",
    #             xmlns="http://www.w3.org/2000/svg",
    #             fill="currentColor",
    #             viewbox="0 0 20 20",
    #             cls="w-4 h-4 text-gray-500 dark:text-gray-400",
    #         )(
    #             Path(
    #                 d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
    #             )
    #         )
    #     ),
    #     Input(
    #         id="datepicker",
    #         type="text",
    #         placeholder="Select date",
    #         cls="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
    #     ),
    #     Script("""
    #             document.addEventListener('DOMContentLoaded', function() {
    #                 const datepickerEl = document.getElementById('datepicker');
    #                 new Datepicker(datepickerEl, {
    #                     // options
    #                 }); 
    #             });
    #         """),
    # ),
    # cls="format"
)
