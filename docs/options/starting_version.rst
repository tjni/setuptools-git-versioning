.. _starting-version-option:

``starting_version``
~~~~~~~~~~~~~~~~~~~~~

If you're using:

- :ref:`tag-based-release`
- :ref:`file-based-release`

without any existing tag or version file respectively, you'll get some
initial version, like ``0.0.1``

You can change this version by setting up ``starting_version`` option in your config file:

- ``setup.py`` file

    .. code:: python

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "starting_version": "1.0.0",
            },
        )

- ``pyproject.toml`` file:
-
    .. code:: toml

        [tool.setuptools-git-versioning]
        starting_version = "1.0.0"

Type
^^^^^^^^^^^^^^

``str``


Default value
^^^^^^^^^^^^^^

``"0.0.1"``


Possible values
^^^^^^^^^^^^^^^

Any PEP-440 compliant version number
