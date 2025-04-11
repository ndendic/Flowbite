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
from pages.markdown import markdown_components
from pages.modals import modals_components
from pages.navigation import navigation_components
from pages.progress import progress_components
from pages.ranges import ranges_components
from pages.skeleton import skeleton_components
from pages.slider import slider_components
from pages.tables import tables_components
from pages.tabs import tabs_components
from pages.buttons import button_components

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

@rt("/markdown")
@page_template("Markdown")
def get(req):
    return markdown_components

@rt("/modals")
@page_template("Modals")
def get(req):
    return modals_components

@rt("/navigation")
@page_template("Navigation")
def get(req):
    return navigation_components

@rt("/progress")
@page_template("Progress")
def get(req):
    return progress_components

@rt("/ranges")
@page_template("Range Inputs")
def get(req):
    return ranges_components

@rt("/skeleton")
@page_template("Placeholder Components")
def get(req):
    return skeleton_components

@rt("/slider")
@page_template("Slider Components")
def get(req):
    return slider_components

@rt("/tables")
@page_template("Table Components")
def get(req):
    return tables_components

@rt("/tabs")
@page_template("Tabs Components")
def get(req):
    return tabs_components

@rt("/buttons")
@page_template("Buttons")
def get(req):
    return button_components