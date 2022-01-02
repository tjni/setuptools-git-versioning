.. _version-file
Read some file content as current version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like the previous example, but instead you can save current version
in a simple test file instead of ``.py`` script.

Just create a file (for example, ``VERSION`` or ``VERSION.txt``) and
place here a version number:

.. code:: txt

    1.0.0

Then place it in both the branches and update your ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    import os

    HERE = os.path.dirname(__file__)
    VERSION_FILE = os.path.join(HERE, "VERSION")

    setuptools.setup(
        ...,
        version_config={
            "version_file": VERSION_FILE,
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    version_file = "VERSION"

When you'll try to get current version in non-master branch, the content
of this file will be returned instead.
