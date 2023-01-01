# Configuration file for the Sphinx documentation builder.

# -- Project information
import revitron_sphinx_theme

project = 'LANCELOT'
copyright = '2022, Oleksii Sokoliuk'
author = 'Oleksii Sokoliuk'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx_rtd_theme",
    "revitron_sphinx_theme"
]

autodoc_mock_imports = ['pyrevit', 'rpw', 'Autodesk', 'clr', 'System', 'Microsoft']

add_module_names = False

napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Open Graph extension config. https://pypi.org/project/sphinxext-opengraph/
ogp_site_url = "https://revitron.readthedocs.io/"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['modules.rst']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

html_theme = 'revitron_sphinx_theme'
html_theme_options = {
    'navigation_depth': 5,
    'github_url': 'https://github.com/revitron/revitron',
    'color_scheme': 'dark'
}

html_title = 'Revitron'

html_context = {
    'landing_page': {
        'menu': [{
            'title': 'Revitron UI',
            'url': 'https://revitron-ui.readthedocs.io/'
        }, {
            'title': 'Developer Guide',
            'url': 'revitron.html'
        }, {
            'title': '♡ Sponsor',
            'url': 'https://github.com/sponsors/marcantondahmen'
        }]
    }
}

html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = []
