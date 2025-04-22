import marimo

__generated_with = "0.12.8"
app = marimo.App(width="medium", css_file="./assets/css/output.css")


@app.cell
def _():
    import marimo as mo
    from fasthtml.core import FT, to_xml
    from fasthtml.common import Script, Link
    from fastbite.all import fastbite_hdrs, fastbite_ftrs
    return FT, Link, Script, fastbite_ftrs, fastbite_hdrs, mo, to_xml


@app.cell
def _(Link, Script, fastbite_hdrs, to_xml):
    h = (fastbite_hdrs,
    Script(src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.8/bundles/datastar.js", type="module"),
    Link(rel="stylesheet", href="/css/output.css"))
    hdr=""
    for i in h: hdr += to_xml(i)
    hdr
    return h, hdr, i


@app.cell
def _(FT, mo, to_xml):
    from fastbite.all import ThemeToggle

    def show(component:FT, hdrs:list|tuple=[], ftrs:list|tuple=[]):
        comp = component.__html__()
        hdr = "" 
        for h in hdrs: hdr += to_xml(h)
        return mo.iframe(f"""
     <html data-theme="ocean-deep" class="bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white font-sans antialiased">
       <head>
         <title>FastHTML page</title>
         <meta charset="utf-8">
         <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.4/dist/htmx.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/answerdotai/fasthtml-js@1.0.12/fasthtml.js"></script>
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css">
    <script src="https://cdn.jsdelivr.net/npm/simple-datatables@9.0.3" type="text/javascript"></script>
    <script src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.8/bundles/datastar.js" type="module"></script>     
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/ndendic/flowbite@latest/assets/css/output.css">
    {hdr}
    </head>
       <body reload-attempts="1" reload-interval="1000">

    {comp}

    <script src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"></script>

        </body>
     </html>
    """)
    return ThemeToggle, show


@app.cell
def _():
    from fastbite.all import H1
    from fasthtml.components import Div
    return Div, H1


@app.cell
def _():
    name = "Nikolas"
    return (name,)


@app.cell
def _(Div, H1, name, show):
    show(Div(cls="p-4 bg-gray-950")(H1(f"Hello there, {name}!")))
    return


@app.cell
def _(Div, show):
    from fastbite.all import Button, ButtonT
    show(Div(cls="p-4")(Button("Click me!",cls="bg-primary-500 hover:bg-primary-700")))
    return Button, ButtonT


if __name__ == "__main__":
    app.run()
