"""Configuration file for django-start Sphinx documentation builder."""

# -- Project information ----------------------------------------------
project = "django-start"
author = "Kevin Bowen"
copyright = f"%Y, {author}"
release = "0.3.3"

# -- General configuration --------------------------------------------
extensions = [
    "sphinx.ext.duration",
    # External extensions
]
templates_path = ["_templates"]
exclude_patterns = []
source_suffix = {
    ".rst": "restructuredtext",
}

# -- Options for HTML output -----------------------------------------
html_title = "django-start"
html_theme = "furo"
language = "en"

html_static_path = ["_static"]

html_logo = "images/django_24.png"
html_favicon = "images/django_24.png"
html_last_updated_fmt = ""
html_show_sphinx = True
