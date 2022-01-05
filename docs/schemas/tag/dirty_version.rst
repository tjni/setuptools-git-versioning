.. _dirty-version:

*Dirty* version
^^^^^^^^^^^^^^^^^^

For example, current repo state is:

.. code:: bash

    Unstashed changes (HEAD)
    |
    commit 64e68cd4 Current commit (master)
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

And you want to generate post versions for every commit after release tag

Just :ref:`install setuptools-git-versioning <installation>`
and then your package version will be ``1.0.0.post1+git.64e68cd4.dirty``.

Version number template
""""""""""""""""""""""""

Sometimes you want see just ``1.0.0.post1+dirty`` value or even ``1.0.0+dirty``.

To get version in such a format you set a template in the config file:

- ``setup.py``:

    .. code:: python

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "dirty_template": "{tag}.post{ccount}+dirty",
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        enabled = true
        dirty_template = "{tag}.post{ccount}+dirty"


See also
""""""""
- :ref:`dirty-template-option` option
- :ref:`sort-by-option` option
- :ref:`substitutions`
