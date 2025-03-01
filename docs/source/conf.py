import os
import sys

sys.path.insert(0, os.path.abspath('../../PyLearn-AI'))

project = 'PyLearn-AI'
author = 'Vicente Ramos'

release = '0.1.0b3'
version = '0.1.0'

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