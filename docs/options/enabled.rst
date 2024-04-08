.. _enabled-option:

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
