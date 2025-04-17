# Franken UI vs. Fastbite Component Comparison

This document outlines the key differences between the Franken UI components found in `monsterui/franken.py` and the Fastbite components in `fastbite/components/` to aid in migration.

## I. VEnum Comparison

### A. VEnum Classes in Franken UI ONLY

These `VEnum` classes exist in Franken UI but do not have a direct equivalent in Fastbite's `base_styles.py`:

-   `LabelT`: Used for pill-style labels (`uk-label`) in Franken. Fastbite uses `LabelInputT` for form labels and lacks a direct VEnum for this specific style.
-   `ScrollspyT`: Used for styling scrollspy behavior in Franken's `NavBar`.

### B. VEnum Classes in Fastbite ONLY

Fastbite introduces many new, often more granular VEnums, frequently based directly on Tailwind CSS classes:

-   `Round`
-   `BtnColor`
-   `FormT`
-   `LabelInputT`
-   `InputT`
-   `PT` (Paragraph styles)
-   `ButtonSize`
-   `ButtonOutline`
-   `HAT` (Hover Anchor Tag styles)
-   `ContainerSize` (Different concept from Franken's `ContainerT`)
-   `BadgeT`
-   `IconT`
-   `RadioT`
-   `CheckboxT`
-   `SwitchT`
-   `ModalT`
-   `NavbarT`
-   `ProgressT`
-   `RangeT`
-   `PlaceholderT`
-   `SliderItemT`
-   `TabContainerT`
-   `TabItemT`
-   `Border`
-   `Shadow`
-   `Bg`

### C. Common VEnums: Notable Value/Concept Differences

Several VEnums share names but differ significantly in their values or approach:

-   **`TextT`**: Fastbite's version is far more extensive, using Tailwind directly. Franken includes UIkit-mapped values like `paragraph`, `lead`, `meta`.
-   **`TextPresets`**: Implementations differ. Fastbite includes heading presets (`h1`-`h6`).
-   **`BackgroundT`**: Fastbite offers many more color/gradient/hover options. Franken's is simpler.
-   **`ButtonT`**: Represent different concepts. Franken's defines *styles* (primary, secondary, ghost). Fastbite's defines semantic *types* and uses `ButtonSize`, `ButtonOutline`, `BtnColor` for styling specifics.
-   **`DividerT`**: Different variants offered (e.g., Franken `icon`, Fastbite `trimmed`).
-   **`SectionT`**: Different sizing logic (Franken uses UIkit sizes `xs`-`xl`, Fastbite uses `ContainerSize`).
-   **`AT` (Anchor)**: Mostly similar; Fastbite adds a `nav` variant.
-   **`ListT`**: Very different. Franken uses UIkit styles (`decimal`, `hyphen`). Fastbite uses HTML/Tailwind styles (`ul`, `ol`, `dl`).
-   **`NavT`**: Fastbite includes structural styles (`child_list`, `parent_li`).
-   **`CardT`**: Fastbite is more granular, including element styles (`title`, `body`, `footer`).
-   **`TableT`**: Fastbite is much more granular (container, row, cell styles). Franken uses higher-level modifiers.
-   **`FlexT`**: Functionally similar, but Fastbite uses direct Tailwind, Franken sometimes maps.

## II. Component Comparison

### A. Franken UI Components Potentially Missing Direct Fastbite Equivalents

These components/functions from `franken.py` may require manual recreation or adaptation using Fastbite's primitives or different patterns:

-   **Semantic HTML Wrappers:**
    -   `Q`, `Em`, `Strong`, `I`, `Small`, `Mark`, `Del`, `Ins`, `Sub`, `Sup`
    -   `Caption`, `Cite`, `Time`, `Address`, `Abbr`, `Dfn`, `Kbd`, `Samp`, `Var`
    -   `Figure`, `Details`, `Summary`, `Data`, `Meter`, `S`, `U`, `Output`
    -   *(Migration Note: Use standard `fasthtml.common` tags like `fh.Em` and style with Fastbite `VEnum`s like `TextT`)*
-   **Code Display:**
    -   `CodeSpan` (Inline code)
    -   `CodeBlock`
    -   *(Migration Note: Check `fastbite.components.markdown` for block handling; inline spans might need a custom solution.)*
-   **Headings/Structure:**
    -   `H1`-`H6` (Styled versions in Franken)
    -   `Subtitle`
    -   `Titled` (Page structure helper)
    -   *(Migration Note: Use `TextPresets` for headings in Fastbite and compose page structure manually.)*
-   **Layout Helpers:**
    -   `Center`, `Grid`
    -   `DivFullySpaced`, `DivCentered`, `DivLAligned`, `DivRAligned`, `DivVStacked`, `DivHStacked`
    -   *(Migration Note: Recreate using Fastbite's `FlexT`, `containers.py`, and potentially custom functions.)*
-   **Form Helpers:**
    -   `Fieldset`, `Legend`
    -   `FormLabel`, `Label` (Pill style)
    -   `UkFormSection`
    -   `GenericLabelInput`, `LabelInput`, `LabelTextArea`, `LabelSwitch`, `LabelRadio`, `LabelCheckboxX`, `LabelSelect`, `Options`, `Select`, `LabelRange`
    -   *(Migration Note: Adapt to Fastbite's form components in `forms.py` using VEnums like `LabelInputT`, `InputT`.)*
-   **Navigation Helpers:**
    -   `NavParentLi`, `NavDividerLi`, `NavHeaderLi`, `NavSubtitle`, `NavCloseLi`
    -   `DropDownNavContainer`
    -   *(Migration Note: Adapt to Fastbite's `navigation.py` structure and `NavT` VEnum.)*
-   **Table Helpers:**
    -   `Td`, `Th`, `Tbody` (Franken versions have extra parameters)
    -   `TableFromLists`, `TableFromDicts`
    -   *(Migration Note: Use helpers from Fastbite's `tables.py` and its granular `TableT` VEnum.)*
-   **Misc UI:**
    -   `PicSumImg`
    -   `UkIcon`, `UkIconLink`
    -   `DiceBearAvatar`
    -   `ThemePicker` (Fastbite has `theme_switcher.py`, compare functionality)
    -   `LightboxContainer`, `LightboxItem`
-   **Utilities:**
    -   `DividerSplit`, `DividerLine`
    -   `apply_classes`, `render_md`, `get_franken_renderer` (Markdown helpers)
    -   *(Migration Note: Check Fastbite's `divider.py` and `markdown.py` for equivalents or adapt.)*

---

*Next Steps: Detailed parameter comparison for overlapping components.* 