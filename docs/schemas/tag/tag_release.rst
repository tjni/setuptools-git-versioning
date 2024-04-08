.. _tag-release:

Release is a git tag
^^^^^^^^^^^^^^^^^^^^

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

And you want to use git tag as a release number instead of duplicating it in
``setup.py`` or other file.

Just :ref:`install setuptools-git-versioning <installation>`
and then tag the commit with a proper release version (e.g. ``1.0.0``):

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

Your package version is now ``1.0.0``.

If tag number had ``v`` prefix, like ``v1.0.0``, it will be trimmed.


Version number template
""""""""""""""""""""""""

By default, when you try to get current version, you'll receive version == current tag, e.g. ``1.0.0``.

You can change this template in the config file:

.. tabs::

    .. code-tab:: python ``setup.py``

        import setuptools

        setuptools.setup(
            ...,
            setup_requires=["setuptools-git-versioning>=2.0,<3"],
            setuptools_git_versioning={
                "template": "2022.{tag}",  # <---
            },
        )

    .. code-tab:: toml ``pyproject.toml``

        [build-system]
        requires = [ "setuptools>=41", "wheel", "setuptools-git-versioning>=2.0,<3", ]
        build-backend = "setuptools.build_meta"

        [tool.setuptools-git-versioning]
        template = "2022.{tag}"  # <---

In this case, for tag ``3.4`` version number will be ``2022.3.4``

.. note::

    If tag name is not :pep:`440` compliant, like ``"release/1.2.3"``,
    use :ref:`tag-formatter-option` option


See also
""""""""
- :ref:`template-option` option
- :ref:`sort-by-option` option
- :ref:`tag-formatter-option` option
- :ref:`substitutions`
- :ref:`wrong-tag-issue` issue
