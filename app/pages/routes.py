from fasthtml.core import APIRouter
from pages.containers import containers
from pages.themes import themes
from pages.playground import playground
from pages.icons import icons_images
from pages.typography import typography
from pages.templates import page_template

rt = APIRouter()

@rt("/typography")
@page_template("Typography")
def get(req):
    return typography

@rt("/containers")
@page_template("Containers")
def get(req):
    return containers

@rt("/themes")
@page_template("Color Themes")
def get(req):
    return themes

@rt("/playground")
@page_template("Playground")
def get(req):
    return playground

@rt("/icons")
@page_template("Icons")
def get(req):
    return icons_images