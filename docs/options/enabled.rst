.. _enabled-option
``enabled``
~~~~~~~~~~~~~~~~~~~~~

Enables ``setuptools-git-versioning`` for current project

Type
^^^^^
``bool``

Default value
^^^^^^^^^^^^^

Missing ``setuptools_git_versioning`` keyword in ``setup.py``
or missing ``setuptools-git-versioning`` section in ``pyproject.toml``
or empty dict (``{}``)
is the same as ``"enabled": False``.

**This is because we don't want to mess up existing projects which are not using this tool**

If any other config value is set, default value is ``True``.

.. warning::

    Previously it was allowed to pass boolean value to the entire config, like:

    .. code:: python

        setup(setuptools_git_versioning=False, ...)

    This has the same meaning as ``"enabled"`` option of config, but it is deprecated since v1.8.0.

    Please replace this value with new syntax. The old syntax support will be removed in v2.0.0
