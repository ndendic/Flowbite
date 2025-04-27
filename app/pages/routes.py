from fasthtml.core import APIRouter
from pages.templates import components_page, components_page
from pages.containers import containers
from pages.themes import themes
from pages.playground import playground
from pages.icons import icons_images
from pages.typography import typography
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
from pages.accordion import accordion_components
from fasthtml.components import Div
rt = APIRouter()

@rt("/typography")
@components_page("Typography")
def get(req):
    return typography

@rt("/containers")
@components_page("Containers")
def get(req):
    return containers

@rt("/themes")
@components_page("Color Themes")
def get(req):
    return themes

@rt("/playground")
@components_page("Playground")
def get(req):
    return playground

@rt("/icons")
@components_page("Icons")
def get(req):
    return icons_images

@rt("/article")
@components_page("Article")
def get(req):
    return article_components

@rt("/badge")
@components_page("Badge")
def get(req):
    return badge_components

@rt("/dropdown")
@components_page("Dropdown")
def get(req):
    return dropdown_components

@rt("/forms")
@components_page("Forms")
def get(req):
    return forms_components

@rt("/markdown")
@components_page("Markdown")
def get(req):
    return markdown_components

@rt("/modals")
@components_page("Modals")
def get(req):
    return modals_components

@rt("/navigation")
@components_page("Navigation")
def get(req):
    return navigation_components

@rt("/progress")
@components_page("Progress")
def get(req):
    return progress_components

@rt("/ranges")
@components_page("Range Inputs")
def get(req):
    return ranges_components

@rt("/skeleton")
@components_page("Placeholder Components")
def get(req):
    return skeleton_components

@rt("/slider")
@components_page("Slider Components")
def get(req):
    return slider_components

@rt("/tables")
@components_page("Table Components")
def get(req):
    return tables_components

@rt("/tabs")
@components_page("Tabs Components")
def get(req):
    return tabs_components

@rt("/buttons")
@components_page("Buttons")
def get(req):
    return button_components

@rt("/accordion")
@components_page("Accordion")
def get(req):
    return accordion_components