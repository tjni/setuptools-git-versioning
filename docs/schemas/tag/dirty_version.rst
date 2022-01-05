.. dirty-version
**Dirty** version
^^^^^^^^^^^^^^^^^^

For example, current repo state is:

.. code:: bash

    Unstashed changes (HEAD)
    |
    commit 86269212 Current commit (master)
    |
    commit 86269212 Release commit (v1.0.0)
    |
    commit e7bdbe51 Another commit
    |
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

When you try to get current version, you'll receive version
number like ``1.0.0.post1+git.64e68cd.dirty``.

This is a PEP-440
compliant value, but sometimes you want see value like ``1.0.0.post1+dirty``.

You can change this template in the config file:

- ``setup.py``:

    .. code:: python

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "dirty_template": "{tag}.post{ccount}+dirty",
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        dirty_template = "{tag}.post{ccount}+dirty"

In this case, for 1 commit since tag ``3.4`` with some uncommitted files in the project repo
version number will be ``3.4.post1+dirty``


See also
""""""""
- :ref:`dirty-template-option`
- :ref:`substitutions`
- :ref:`sort-by-option`
