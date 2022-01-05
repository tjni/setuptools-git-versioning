.. _tag-release
Release is a git tag
^^^^^^^^^^^^^^^^^^^^^

You want to use git tag as a release number instead of duplicating it
setup.py or other file.

For example, current repo state is:

.. code:: bash

    commit 86269212 Release commit (HEAD, master)
    |
    commit e7bdbe51 Another commit
    |
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

Then you decided to release new version, tag commit with a proper release version (e.g. ``1.0.0``):

.. code:: bash

    commit 86269212 Release commit (v1.0.0, HEAD, master)
    |
    commit e7bdbe51 Another commit
    |
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

Tag name will be used as your package version number.
If tag number had ``v`` prefix, like ``v1.0.0``, it will be trimmed.


Version number template
""""""""""""""""""""""""

By default, when you try to get current version, you'll receive version
number like ``1.0.0``.

You can change this template in the config file:

- ``setup.py``:

    .. code:: python

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "template": "2022.{tag}",
            },
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools-git-versioning]
        template = "2022.{tag}"

In this case, for tag ``3.4`` version number will be ``2021.3.4``


See also
""""""""
- :ref:`template-option`
- :ref:`substitutions`
- :ref:`sort-by-option`
