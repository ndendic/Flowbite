from fasthtml.common import *
from fasthtml.svg import *
from fh_flowbite.components import *
from fh_flowbite.core import *
from theme_switcher import ThemeSwitcher

playground = Container(
    H1("Playground", cls="text-3xl font-bold mb-6"),
    DivCentered(
        NotStr("""
        <section class="bg-gray-900 text-white">
            <div class="max-w-screen-xl px-4 py-20 mx-auto text-center">
                <h1 class="text-4xl font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
                    Build stunning websites with Flowbite & Tailwind CSS
                </h1>
                <p class="mt-6 text-lg sm:text-xl text-gray-300">
                    Accelerate your development with pre-built UI components and a modern utility-first CSS framework.
                </p>
                <div class="mt-8 flex flex-col sm:flex-row justify-center gap-4">
                    <a href="#" class="px-6 py-3 text-lg font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700">
                        Get Started
                    </a>
                    <a href="#" class="px-6 py-3 text-lg font-medium text-gray-900 bg-white rounded-lg hover:bg-gray-200">
                        Learn More
                    </a>
                </div>
            </div>
        </section>

        """)
    )
) 