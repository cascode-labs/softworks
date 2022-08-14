# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath( '../..'))

# -- Project information -----------------------------------------------------

project = 'Softworks'
copyright = '2022, Curtis Mayberry'
author = 'Curtis Mayberry'

def get_version(relative_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, relative_path), 'r') as version_file:
        return version_file.read().strip()

# The full version, including alpha/beta/rc tags
release = get_version("../../softworks/version")


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton',
    'sphinx_panels',
    "sphinx_github_changelog",
    'sphinx_sitemap',
    'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

language = "en"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/logo/softworks_logo.jpg"

html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/cascode-labs/softworks",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fab fa-github-square",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "Latest-release",
            "url": "https://github.com/cascode-labs/softworks/releases/latest",  # required
            "icon": "fas fa-tag",
            "type": "fontawesome",
        }
    ],
    "external_links": [
      {"name": "cascode-labs", "url": "http://www.cascode-labs.org/"},
    ],
    "logo": {
        "text": "Softworks",
    },
    "footer_items": ["version", "copyright", "sphinx-version"],
    "use_edit_page_button": True,
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "cascode-labs",
    "github_repo": "softworks",
    "github_version": "main",
    "doc_path": "docs",
}

html_baseurl = 'http://www.cascode-labs.org/softworks/'

html_css_files = [
    'css/custom.css',
]
