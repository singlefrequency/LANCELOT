# Configuration file for the Sphinx documentation builder.

# -- Project information
!pip install https://github.com/revitron/revitron-sphinx-theme/archive/master.zip
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

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output


html_theme = "revitron_sphinx_theme"
html_static_path = ['_static']
html_logo = 'new_logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    "default_mode": "dark",
    'color_scheme': 'dark',
    "navbar_end": ["navbar-icon-links"]

}
#html_css_files = 'custom.css'
# -- Options for EPUB output
epub_show_urls = 'footnote'
