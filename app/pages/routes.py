from fasthtml.core import APIRouter
from pages.containers import containers
from pages.themes import themes
from pages.playground import playground
from pages.icons import icons_images
from pages.typography import typography
from pages.templates import page_template
from pages.article import article_components
from pages.badge import badge_components
from pages.dropdown import dropdown_components
from pages.forms import forms_components

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

@rt("/article")
@page_template("Article")
def get(req):
    return article_components

@rt("/badge")
@page_template("Badge")
def get(req):
    return badge_components

@rt("/dropdown")
@page_template("Dropdown")
def get(req):
    return dropdown_components

@rt("/forms")
@page_template("Forms")
def get(req):
    return forms_components