.. _version-callback
Callback/variable as current version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, current repo state is:

.. code:: bash

    commit 233f6d72 Dev branch commit (HEAD, dev)
    |
    |    commit 86269212 Current commit (v1.0.0, master)
    |    |
    |   commit e7bdbe51 Another commit
    |    /
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

And there are just no tags in the current branch (``dev``) because all
of them are placed in the ``master`` branch only.

By default, when you try to get current version, you'll receive some
initial value. But if you want to get synchronized version numbers in
both on the branches?

You can create a function in some file (for example, in the
``__init__.py`` file of your module):

.. code:: python

    def get_version():
        return "1.0.0"

Then place it in both the branches and update your ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    from mypkg.mymodule import get_version

    setuptools.setup(
        ...,
        version_config={
            "version_callback": get_version,
        },
    )

.. code:: toml

    [build-system]
    # __legacy__ is required to have access to package
    # during build step
    build-backend = "setuptools.build_meta:__legacy__"

    [tool.setuptools-git-versioning]
    version_callback = "mypkg.mymodule:get_version"

When you'll try to get current version in non-master branch, the result
of executing this function will be returned instead of latest tag
number.

If a value of this option is not a function but just str, it also could be used:

-  ``__init__.py`` file:

    .. code:: python

        __version__ = "1.0.0"

-  ``setup.py`` file:

    .. code:: python

        from mypkg.mymodule import __version__

        setuptools.setup(
            ...,
            version_config={
                "version_callback": __version__,
            },
        )

-  ``pyproject.toml`` file:

    .. code:: toml

        [build-system]
        build-backend = "setuptools.build_meta:__legacy__"

        [tool.setuptools-git-versioning]
        version_callback = "mypkg.mymodule:__version__"

**Please take into account that ``version_callback`` is ignored if tag
is present**
