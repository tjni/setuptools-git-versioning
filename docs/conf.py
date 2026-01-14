# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from pathlib import Path

from packaging.version import Version

PROJECT_ROOT_DIR = Path(__file__).parent.parent.resolve()

sys.path.insert(0, os.fspath(PROJECT_ROOT_DIR))

from setuptools_git_versioning import version_from_git  # noqa: E402

ver = Version(version_from_git())

# The short X.Y version
version = ver.base_version
# The full version, including alpha/beta/rc tags
release = ver.public

# -- Project information -----------------------------------------------------

project = "setuptools-git-versioning"
copyright = "2020-present, dolfinus"
author = "dolfinus"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx_autodoc_typehints",
    "changelog",
    "numpydoc",
    "sphinxarg.ext",
    "sphinx_tabs.tabs",
    "sphinx_last_updated_by_git",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumds.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_title = f"setuptools-git-versioning {version}"
html_extra_path = ["robots.txt"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
# html_static_path = ['_static']


extlinks = {
    "github-user": ("https://github.com/%s", "@%s"),
    "issue": ("https://github.com/dolfinus/setuptools-git-versioning/issues/%s", "#%s"),
    "pr": ("https://github.com/dolfinus/setuptools-git-versioning/pull/%s", "#%s"),
}

changelog_sections = [
    "general",
    "core",
    "dependency",
    "config",
    "docs",
    "ci",
    "tests",
    "dev",
]

changelog_caption_class = ""

changelog_inner_tag_sort = ["breaking", "deprecated", "feature", "bug", "refactor"]
changelog_hide_sections_from_tags = True

changelog_render_ticket = "https://github.com/dolfinus/setuptools-git-versioning/issues/%s"
changelog_render_pullreq = {"default": "https://github.com/dolfinus/setuptools-git-versioning/pull/%s"}
changelog_render_changeset = "https://github.com/dolfinus/setuptools-git-versioning/commit/%s"

language = "en"

default_role = "any"
todo_include_todos = False

numpydoc_show_class_members = False
pygments_style = "sphinx"

autoclass_content = "both"
