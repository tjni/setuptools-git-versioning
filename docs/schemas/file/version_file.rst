.. _version-file:

Read some file content as current version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
initial value (see :ref:`starting-version-option` option).

But if you want to get synchronized version numbers in
both on the branches, you can create a text file (for example, ``VERSION`` or ``VERSION.txt``)
and save here current version number:

.. code:: txt

    1.0.0

Then place it in both the branches and update your config file:

- ``setup.py``:

    .. code:: python

        # you can use os.path instead of pathlib
        from pathlib import Path

        root_path = Path(__file__).parent
        version_file = root_path / "VERSION"

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "version_file": version_file,
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        enabled = true
        version_file = "VERSION"

When you'll try to get current version in non-master branch, the content
of this file (``1.0.0``) will be returned instead default version number.

**Please take into account that any tags in the repo are ignored if this option is being used.**

See also
"""""""""
- :ref:`version-callback`
- :ref:`version-file-option` option
- :ref:`runtime-version`
