from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from theme_switcher import ThemeSwitcher

themes = Container(
    H1("Color Themes", cls="text-3xl font-bold mb-6"),
    P("This page showcases the different color themes available in the application.", cls="mb-8"),
    
    # Theme Switcher
    H2("Theme Switcher", cls="text-2xl font-bold mb-4"),
    P("Use the switcher below to change themes:", cls="mb-4"),
    Div(
        ThemeSwitcher(),
        cls="mb-8 inline-block"
    ),
    
    # Theme Showcase
    H2("Available Themes", cls="text-2xl font-bold mt-8 mb-4"),
    Grid(
        # Default Theme
        Card(
            H3("Default Theme", cls="text-xl font-bold mb-2"),
            P("The system default theme with grayscale primary colors."),
            Div(
                *[Div(cls=f"w-8 h-8 rounded bg-gray-{n}00") for n in range(1, 10)],
                cls="mt-4 flex gap-2 flex-wrap"
            ),
            cls="p-4"
        ),
        
        # Retro Theme
        Card(
            H3("Retro Blue Theme", cls="text-xl font-bold mb-2"),
            P("A classic blue theme with deep saturated colors."),
            Div(
                Div(cls="w-8 h-8 rounded bg-[#3c79f5]"),
                Div(cls="w-8 h-8 rounded bg-[#265aea]"),
                Div(cls="w-8 h-8 rounded bg-[#1e45d7]"),
                Div(cls="w-8 h-8 rounded bg-[#203cb6]"),
                Div(cls="w-8 h-8 rounded bg-[#1e358a]"),
                cls="mt-4 flex gap-2 flex-wrap"
            ),
            onClick="setTheme('retro')",
            cls="p-4 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800"
        ),
        
        # Emerald Theme
        Card(
            H3("Emerald Green Theme", cls="text-xl font-bold mb-2"),
            P("A fresh green theme for a natural feel."),
            Div(
                Div(cls="w-8 h-8 rounded bg-emerald-300"),
                Div(cls="w-8 h-8 rounded bg-emerald-400"),
                Div(cls="w-8 h-8 rounded bg-emerald-500"),
                Div(cls="w-8 h-8 rounded bg-emerald-600"),
                Div(cls="w-8 h-8 rounded bg-emerald-700"),
                cls="mt-4 flex gap-2 flex-wrap"
            ),
            onClick="setTheme('emerald')",
            cls="p-4 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800"
        ),
        
        # Amber Theme
        Card(
            H3("Amber Gold Theme", cls="text-xl font-bold mb-2"),
            P("A warm amber/gold theme for a cozy feeling."),
            Div(
                Div(cls="w-8 h-8 rounded bg-amber-300"),
                Div(cls="w-8 h-8 rounded bg-amber-400"),
                Div(cls="w-8 h-8 rounded bg-amber-500"),
                Div(cls="w-8 h-8 rounded bg-amber-600"),
                Div(cls="w-8 h-8 rounded bg-amber-700"),
                cls="mt-4 flex gap-2 flex-wrap"
            ),
            onClick="setTheme('amber')",
            cls="p-4 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800"
        ),
        
        # Rose Theme
        Card(
            H3("Rose Pink Theme", cls="text-xl font-bold mb-2"),
            P("A vibrant rose/pink theme for a bold look."),
            Div(
                Div(cls="w-8 h-8 rounded bg-rose-300"),
                Div(cls="w-8 h-8 rounded bg-rose-400"),
                Div(cls="w-8 h-8 rounded bg-rose-500"),
                Div(cls="w-8 h-8 rounded bg-rose-600"),
                Div(cls="w-8 h-8 rounded bg-rose-700"),
                cls="mt-4 flex gap-2 flex-wrap"
            ),
            onClick="setTheme('rose')",
            cls="p-4 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800"
        ),
        
        columns=2,
        gap=6,
        cls="mb-8"
    ),
    
    # Using Themes with Components
    H2("Using Themes with Components", cls="text-2xl font-bold mt-8 mb-4"),
    P("Themes automatically apply to all components that use the primary color variables:", cls="mb-6"),
    
    Grid(
        Button("Primary Button", cls="bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded"),
        # Alert("This is a themed alert", color="primary", icon=True),
        # Badge("Themed Badge", color="primary"),
        # Progress(value=75, color="primary"),
        columns=2,
        gap=6,
        cls="mb-8"
    ),
    
    # Dark Mode Interaction
    H2("Dark Mode Interaction", cls="text-2xl font-bold mt-8 mb-4"),
    P("Themes work in both light and dark mode. Use the dark mode toggle in the navbar to see how each theme adapts.", cls="mb-6"),
    
    # Alert(
    #     P("Note: Some themes may look better in light mode, while others shine in dark mode. Try both to see what you prefer!"),
    #     color="info"
    # ),
    
    # Theme Documentation
    H2("Theme Documentation", cls="text-2xl font-bold mt-8 mb-4"),
    P("To use color variables in your own components:", cls="mb-2"),
    Code("""
/* Using CSS Variables */
.my-component {
    background-color: var(--color-primary-500);
    color: var(--color-primary-50);
    border-color: var(--color-primary-700);
}

/* Using Tailwind Classes */
<div class="bg-primary-500 text-primary-50 border-primary-700">
    This will use the current theme colors
</div>
    """, cls="language-css p-4 rounded"),
    
    Script("""
    // Highlight the currently active theme on page load
    document.addEventListener('DOMContentLoaded', function() {
        const highlightActiveTheme = () => {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'none';
            const allCards = document.querySelectorAll('.card');
            
            // Reset all cards
            allCards.forEach(card => {
                card.classList.remove('ring-2', 'ring-primary-500', 'ring-inset');
            });
            
            // Find the theme heading matching the current theme
            document.querySelectorAll('.card h3').forEach(heading => {
                const headingText = heading.textContent.toLowerCase();
                if (
                    (currentTheme === 'retro' && headingText.includes('retro')) ||
                    (currentTheme === 'emerald' && headingText.includes('emerald')) ||
                    (currentTheme === 'amber' && headingText.includes('amber')) ||
                    (currentTheme === 'rose' && headingText.includes('rose')) ||
                    (currentTheme === 'none' && headingText.includes('default'))
                ) {
                    heading.closest('.card').classList.add('ring-2', 'ring-primary-500', 'ring-inset');
                }
            });
        };
        
        // Initial highlight
        highlightActiveTheme();
        
        // Set up a MutationObserver to watch for theme changes
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'data-theme') {
                    highlightActiveTheme();
                }
            });
        });
        
        // Start observing the document element
        observer.observe(document.documentElement, { attributes: true });
    });
    """)
) 