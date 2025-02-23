import os
import sys

sys.path.insert(0, os.path.abspath('../../pylearnlite'))

project = 'PyLearnLite'
author = 'Your Name'
release = '0.1.0-beta'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}