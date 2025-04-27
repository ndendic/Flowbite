from fasthtml.components import *
from fastbite.all import *
from navigation import Sidebar, Main, Navbar
from fasthtml.components import Div


def is_htmx(request=None):
    "Check if the request is an HTMX request"
    return request and "hx-request" in request.headers


def site_page(title, content):
    return (
        Title(title),
        Body(
            Navbar(),
            Sidebar(),
            Main(content,cls="mx-4")   
        ),
    )

def page_template(title):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            content = func(request)
            if is_htmx(request):
                return content
            return site_page(title, content)
        return wrapper
    return decorator

def components_page(title):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            content = Div(cls='max-w-4xl')(func(request))
            if is_htmx(request):
                return content
            return site_page(title, content)
        return wrapper
    return decorator