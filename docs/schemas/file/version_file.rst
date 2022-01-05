.. _version-file
Read some file content as current version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
both on the branches.

You can create a text file (for example, ``VERSION`` or ``VERSION.txt``)
and save here current version number:

.. code:: txt

    1.0.0

Then place it in both the branches and update your config file:

- ``setup.py``:

    .. code:: python

        import os

        HERE = os.path.dirname(__file__)
        VERSION_FILE = os.path.join(HERE, "VERSION")

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "version_file": VERSION_FILE,
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        enabled = true
        version_file = "VERSION"

When you'll try to get current version in non-master branch, the content
of this file will be returned instead default version number.

See also
"""""""""
- :ref:`version-callback`
- :ref:`version-file-option`
