from fasthtml.common import *
from fasthtml.svg import *
from fastbite.all import *

# palette_icon = Svg(
#     Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M12 7h.01m3.486 1.513h.01m-6.978 0h.01M6.99 12H7m9 4h2.706a1.957 1.957 0 0 0 1.883-1.325A9 9 0 1 0 3.043 12.89 9.1 9.1 0 0 0 8.2 20.1a8.62 8.62 0 0 0 3.769.9 2.013 2.013 0 0 0 2.03-2v-.857A2.036 2.036 0 0 1 16 16Z'),
#     aria_hidden='true',
#     xmlns='http://www.w3.org/2000/svg',
#     width='24',
#     height='24',
#     fill='none',
#     viewbox='0 0 24 24',
#     cls='w-6 h-6 text-gray-800 dark:text-white'
# )
palette_icon = Icon("palette", cls="w-4 h-4")

default_themes = {
    "none": "Default",
    "retro": "Retro Blue",
    "emerald": "Emerald Green",
    "amber": "Amber Gold",
    "rose": "Rose Pink",
    "oceanic-deep": "Oceanic Deep",
    "sunset-glow": "Sunset Glow"
}

def ThemeSwitcher(themes=default_themes):
    """
    Create a theme switcher component with a dropdown menu
    
    Args:
        themes: A dictionary of theme names and their display names. If None, default themes are used.
        
    Returns:
        A container with the theme switcher component and necessary JavaScript
    """

    # Create a unique ID for the dropdown
    dropdown_id = "theme-palette-dropdown"
    
    # Create the dropdown button
    toggle_button = Div(
        palette_icon,
        Span("Select Theme", cls="sr-only"),
        id="theme-palette-toggle",
        type="button",
        cls="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm px-2.5 py-2.5",
        data_dropdown_toggle=dropdown_id,
        aria_expanded="false"
    )
    
    # Create theme options for the dropdown
    theme_options = []
    
    for theme_value, theme_label in themes.items():
        # Create a color preview for each theme
        preview_colors = []
        
        # Different theme-specific colors to preview
        if theme_value == "retro":
            colors = ["bg-[#3c79f5]", "bg-[#265aea]", "bg-[#1e45d7]"]
        elif theme_value == "emerald":
            colors = ["bg-emerald-400", "bg-emerald-500", "bg-emerald-600"]
        elif theme_value == "amber":
            colors = ["bg-amber-400", "bg-amber-500", "bg-amber-600"]
        elif theme_value == "rose":
            colors = ["bg-rose-400", "bg-rose-500", "bg-rose-600"]
        elif theme_value == "oceanic-deep":
            colors = ["bg-primary-400", "bg-primary-500", "bg-primary-600"]
        elif theme_value == "sunset-glow":
            colors = ["bg-primary-400", "bg-primary-500", "bg-primary-600"]
        else:  # default
            colors = ["bg-gray-300", "bg-gray-400", "bg-gray-500"]
        
        # Create color preview circles
        for color_class in colors:
            preview_colors.append(
                Span(cls=f"inline-block w-3 h-3 rounded-full {color_class}")
            )
        
        # Create the theme option button
        theme_option = Button(
            Div(
                Div(*preview_colors, cls="flex space-x-1"),
                Span(theme_label, cls="ml-2 text-sm"),
                cls="flex items-center"
            ),
            type="button",
            onclick=f"setTheme('{theme_value}')",
            cls="w-full px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 text-left"
        )
        
        theme_options.append(Li(theme_option))
    
    # Create the dropdown menu
    dropdown_menu = Div(
        H6("Select Theme", cls="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-200 border-b border-gray-200 dark:border-gray-600"),
        Ul(
            *theme_options,
            cls="py-1"
        ),
        id=dropdown_id,
        cls="z-50 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600"
    )
    
    # JavaScript for theme handling
    theme_script = Script("""
    // Theme switching functionality
    document.addEventListener('DOMContentLoaded', function() {
        // Function to set theme
        window.setTheme = function(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            
            // Add active indicator to selected theme in dropdown
            const buttons = document.querySelectorAll('#theme-palette-dropdown button');
            buttons.forEach(btn => {
                // Extract theme value from the onclick attribute
                const onclickAttr = btn.getAttribute('onclick');
                const clickedTheme = onclickAttr ? onclickAttr.match(/'([^']+)'/)[1] : null;
                
                if (clickedTheme === theme) {
                    btn.classList.add('bg-gray-100', 'dark:bg-gray-600');
                } else {
                    btn.classList.remove('bg-gray-100', 'dark:bg-gray-600');
                }
            });
        };
        
        // On page load, highlight the active theme
        const savedTheme = localStorage.getItem('theme') || 'none';
        const buttons = document.querySelectorAll('#theme-palette-dropdown button');
        buttons.forEach(btn => {
            const onclickAttr = btn.getAttribute('onclick');
            const themeValue = onclickAttr ? onclickAttr.match(/'([^']+)'/)[1] : null;
            
            if (themeValue === savedTheme) {
                btn.classList.add('bg-gray-100', 'dark:bg-gray-600');
            }
        });
    });
    """)
    
    # Return both the UI component and the script
    return Div(
        Div(
            toggle_button,
            dropdown_menu,
            cls="relative"
        ),
        theme_script,
        cls="theme-switcher-container"
    ) 