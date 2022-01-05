.. _post-release
Post release
^^^^^^^^^^^^

For example, current repo state is:

.. code:: bash

    commit 86269212 Current commit (HEAD, master)
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

By default, when you try to get current version, you'll receive version
number like ``1.0.0.post1+git.64e68cd``.

This is a PEP-440 compliant value, but sometimes you want see just
``1.0.0.post1`` value or even ``1.0.0``.

You can change this template in the config file:

- ``setup.py``:

    .. code:: python

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "dev_template": "{tag}.post{ccount}",
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        dev_template = "{tag}.post{ccount}"

In this case, for 1 commit since tag ``3.4`` version number will be ``3.4.post1``

See also
""""""""
- :ref:`dev-template-option`
- :ref:`substitutions`
- :ref:`sort-by-option`
