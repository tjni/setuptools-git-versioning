.. _version-callback:

Execute some callback function to get current version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, current repo state is:

.. code:: bash

    commit 233f6d72 Dev branch commit (HEAD, dev)
    |
    |    commit 86269212 Release commit (v1.0.0, master)
    |    |
    |   commit e7bdbe51 Another commit
    |    /
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

By default, when you try to get current version, you'll receive some
initial value (see :ref:`starting-version-option` option),
because there are no tags in the ``dev`` branch.

If you want to get synchronized version numbers in both ``master`` and ``dev`` branches,
you can create a function in some file (for example, in the
``my_module/version.py`` file):

.. code:: python

    def get_version():
        return "1.0.0"

Then place it in both the branches and update your ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    from my_module.version import get_version

    setuptools.setup(
        ...,
        setuptools_git_versioning={
            "enabled": True,
            "version_callback": get_version,
        },
    )

.. code:: toml

    [build-system]
    # __legacy__ is required to have access to package
    # during build step
    build-backend = "setuptools.build_meta:__legacy__"

    [tool.setuptools-git-versioning]
    enabled = true
    version_callback = "my_module.version:get_version"

When you'll try to get current version in **any** branch, the result
of executing this function will be returned instead of latest tag
number.

If a value of this option is not a function but just str, it also could be used:

-  ``my_module/__init__.py`` file:

    .. code:: python

        __version__ = "1.0.0"

-  ``setup.py`` file:

    .. code:: python

        import my_module

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "version_callback": my_module.__version__,
            },
        )

-  ``pyproject.toml`` file:

    .. code:: toml

        [build-system]
        build-backend = "setuptools.build_meta:__legacy__"

        [tool.setuptools-git-versioning]
        enabled = true
        version_callback = "my_module:__version__"

**Please take into account that any tag in the branch is completely ignored if version_callback
is set**.
You should explicitly call ``setuptools_git_versioning.version_from_git`` function in the callback.

.. note::

    Callback result is returned *as is*, so it should be a :pep:`440` compatible version number

See also
""""""""
- :ref:`version-callback-option` option
- :ref:`runtime-version`
