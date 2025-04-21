import marimo

__generated_with = "0.12.8"
app = marimo.App(width="medium", css_file="./assets/css/output.css")


@app.cell
def _():
    import marimo as mo
    from fasthtml.core import FT
    return FT, mo


@app.cell
def _(FT, mo):
    from fastbite.all import ThemeToggle
    def show(component:FT):
        comp = component.__html__()
        return mo.iframe(f"""
     <!doctype html>
     <html class="bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white font-sans antialiased">
       <head>
         <title>FastHTML page</title>
         <meta charset="utf-8">
         <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.4/dist/htmx.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/answerdotai/fasthtml-js@1.0.12/fasthtml.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/answerdotai/surreal@main/surreal.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/gnat/css-scope-inline@main/script.js"></script>     
    <link rel="icon" type="image/x-ico" href="/images/favicon-light.svg" media="(prefers-color-scheme: light)">
         <link rel="icon" type="image/x-ico" href="/images/favicon-dark.svg" media="(prefers-color-scheme: dark)">
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css">
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/simple-datatables@9.0.3" type="text/javascript"></script>
    <script src="https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-beta.8/bundles/datastar.js" type="module"></script>     
    <link rel="stylesheet" href="assets/css/output.css">
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-dark.css" media="(prefers-color-scheme: dark)">
         <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/atom-one-light.css" media="(prefers-color-scheme: light)">
    <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/highlight.min.js"></script><script src="https://cdn.jsdelivr.net/gh/arronhunt/highlightjs-copy/dist/highlightjs-copy.min.js"></script>     
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/arronhunt/highlightjs-copy/dist/highlightjs-copy.min.css">
    <script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/python.min.js"></script><script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/javascript.min.js"></script><script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/html.min.js"></script><script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/languages/css.min.js"></script><script type="module">
    hljs.addPlugin(new CopyButtonPlugin());
    hljs.configure({{'cssSelector': 'pre code:not([data-highlighted="yes"])'}});
    htmx.onLoad(hljs.highlightAll);</script><script>
        (() => {{let attempts = 0;const connect = () => {{const socket = new WebSocket(`ws://${{window.location.host}}/live-reload`);
                socket.onopen = async() => {{
                    const res = await fetch(window.location.href);
                    if (res.ok) {{ 
                        attempts ? window.location.reload() : console.log('LiveReload connected'); 
                    }}
                    }};
                socket.onclose = () => {{
                    !attempts++ ? connect() : setTimeout(() => {{ connect() }}, 1);
                    if (attempts > 1000) window.location.reload();
                }}
                }};
            connect();
        }})();
        </script>   
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
def _(Div, H1, show):
    show(Div(cls="p-4 bg-gray-950")(H1("Hello there!")))
    return


@app.cell
def _(Div, show):
    from fastbite.all import Button, ButtonT
    show(Div(cls="p-4")(Button("Click me!",cls="bg-blue-500 hover:bg-blue-700")))

    return Button, ButtonT


@app.cell
def _(Button, ButtonT):
    Button("Click me!", cls=ButtonT.primary)
    return


if __name__ == "__main__":
    app.run()
