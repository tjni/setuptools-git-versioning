.. _sphinx_usage-issue:

Sphinx usage
~~~~~~~~~~~~

To determine current project version in Sphinx with the following config:

.. code-block:: python
    :caption: docs/conf.py

    # -- Path setup --------------------------------------------------------------

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.

    import os
    import sys
    from pathlib import Path

    PROJECT_ROOT_DIR = Path(__file__).parent.parent.resolve()

    sys.path.insert(0, os.fspath(PROJECT_ROOT_DIR))

    # The short X.Y version
    version = "???"
    # The full version, including alpha/beta/rc tags
    release = "???"

Add these lines:

.. code-block:: python
    :caption: docs/conf.py

    from setuptools_git_versioning import get_version

    # to resolve pyproject.toml, setup.py or version_file, we need to pass package root explicitly,
    # as Sphinx uses docs/ as current working directory
    ver = get_version(root=PROJECT_ROOT_DIR)

    # The short X.Y version
    version = ver.base_version
    # The full version, including alpha/beta/rc tags
    release = ver.public
