.. _simple-release
Release is a git tag
~~~~~~~~~~~~~~~~~~~~

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

Then you decided to release new version: - Tag commit with a proper
release version (e.g. ``v1.0.0`` or ``1.0.0``):

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

Check current version with command ``python setup.py --version``. You'll get ``1.0.0`` as a version number.

If tag number had ``v`` prefix, like ``v1.0.0``, it will be trimmed.


Version number template
^^^^^^^^^^^^^^^^^^^^^^^

By default, when you try to get current version, you'll receive version
number like ``1.0.0``.

You can change this template just in the same ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    setuptools.setup(
        ...,
        version_config={
            "template": "2022.{tag}",
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    template = "2022.{tag}"

In this case, for tag ``3.4`` version number will be ``2021.3.4``


Dev template
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

You can change this template just in the same ``setup.py`` or ``pyproject.toml`` file:

-  For values like ``1.0.0.post1``. ``N`` in ``.postN`` suffix is a number of commits since previous release (tag):

    .. code:: python

        setuptools.setup(
            ...,
            version_config={
                "dev_template": "{tag}.post{ccount}",
            },
        )

    .. code:: toml

        [tool.setuptools-git-versioning]
        dev_template = "{tag}.post{ccount}"

-  To return just the latest tag value, like ``1.0.0``,use value ``"{tag}"``

Dirty template
^^^^^^^^^^^^^^

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

By default, when you try to get current version, you'll receive version
number like ``1.0.0.post1+git.64e68cd.dirty``. This is a PEP-440
compliant value, but sometimes you want see just ``1.0.0.post1`` value
or even ``1.0.0``.

You can change this template just in the same ``setup.py`` or ``pyproject.toml`` file:

-  For values like ``1.0.0.post1``. ``N`` in ``.postN`` suffix is a number of commits since previous release (tag):

    .. code:: python

        setuptools.setup(
            ...,
            version_config={
                "dirty_template": "{tag}.post{ccount}",
            },
        )

    .. code:: toml

        [tool.setuptools-git-versioning]
        dirty_template = "{tag}.post{ccount}"

-  To return just the latest tag value, like ``1.0.0``,use value ``"{tag}"``

Set initial version
^^^^^^^^^^^^^^^^^^^

For example, current repo state is:

.. code:: bash

    commit 86269212 Current commit (HEAD, master)
    |
    commit e7bdbe51 Another commit
    |
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

And there are just no tags in the current branch.

By default, when you try to get current version, you'll receive some
initial value, like ``0.0.1``

You can change this template just in the same ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    setuptools.setup(
        ...,
        version_config={
            "starting_version": "1.0.0",
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    starting_version = "1.0.0"
