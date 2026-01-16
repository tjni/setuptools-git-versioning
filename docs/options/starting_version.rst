.. _starting-version-option:

``starting_version``
~~~~~~~~~~~~~~~~~~~~

If you're using:

- :ref:`tag-based-release`
- :ref:`file-based-release`

without any existing tag or version file respectively, you'll get some
initial version, like ``0.0.1``

You can change this version by setting up ``starting_version`` option in your config file:

.. tabs::

    .. code-tab:: python ``setup.py`` file

        import setuptools

        setuptools.setup(
            ...,
            setup_requires=["setuptools-git-versioning>=3.0,<4"],
            setuptools_git_versioning={
                "enabled": True,
                "starting_version": "1.0.0",  # <---
            },
        )

    .. code-tab:: toml ``pyproject.toml`` file

        [build-system]
        requires = [ "setuptools>=41", "wheel", "setuptools-git-versioning>=3.0,<4", ]
        build-backend = "setuptools.build_meta"

        [project]
        dynamic = ["version"]

        [tool.setuptools-git-versioning]
        enabled = true
        starting_version = "1.0.0"  # <---

.. note::

    This option is completely ignored if :ref:`version-callback` schema is used.

Type
^^^^

``str``


Default value
^^^^^^^^^^^^^

``"0.0.1"``


Possible values
^^^^^^^^^^^^^^^

Any :pep:`440` compliant version number
