.. _branch-formatter-option:

``branch_formatter``
~~~~~~~~~~~~~~~~~~~~~

Callback to be used for formatting a branch name before template substitution

Type
^^^^^^^^^^^^^^

``str`` or ``callable``


Default value
^^^^^^^^^^^^^^
``None``

Usage
^^^^^^

It is possible to use (see :ref:`dev-release-any-branch`) branch name in version number.

But branches should have PEP-440 compatible name, like:

- ``alpha``
- ``beta``
- ``rc``
- ``preview``
- ``pre``
- ``post``
- ``dev``

In case of using branch names like ``feature/ABC-123`` or ``bugfix/ABC-123``,
you'll get version number which ``pip`` cannot understand.

To fix that you can define a callback which will receive current branch
name and return a properly formatted one:

- ``mypkg/util.py`` file:

    .. code:: python

        import re


        def format_branch_name(name):
            # If branch has name like "bugfix/issue-1234-bug-title", take only "1234" part
            pattern = re.compile("^(bugfix|feature)\/issue-(?P<branch>[0-9]+)-\S+")

            match = pattern.search(name)
            if match:
                return match.group("branch")

            # function is called even if branch name is not used in a current template
            # just left properly named branches intact
            if name in ["master", "dev"]:
                return name

            # fail in case of wrong branch names like "bugfix/issue-unknown"
            raise ValueError(f"Wrong branch name: {name}")

- ``setup.py`` file:

    .. code:: python

        from mypkg.util import format_branch_name

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "dev_template": "{branch}.dev{ccount}",
                "dirty_template": "{branch}.dev{ccount}",
                "branch_formatter": format_branch_name,
            },
        )

- ``pyproject.toml`` file:

    .. code:: toml

        [build-system]
        # __legacy__ is required to have access to package
        # during build step
        build-backend = "setuptools.build_meta:__legacy__"

        [tool.setuptools-git-versioning]
        enabled = true
        dev_template = "{branch}.dev{ccount}"
        dirty_template = "{branch}.dev{ccount}"
        branch_formatter = "mypkg.util:format_branch_name"

    .. note::

        Please pay attention to ``build-backend`` item in your config, it is important
        for ``setuptools-git-versioning`` to access your module source code.


Possible values
^^^^^^^^^^^^^^^

- ``None``

    Disables this feature

- function/lambda (``setup.py`` only)
- function full name in format ``"some.module:function_name"``

    Function should have signature ``(str) -> str``. It accepts original branch name and returns formatted one

    .. warning::

        Exception will be raised if module or function/lambda is missing or has invalid signature

- regexp like ``".*(?P<branch>\d+).*"``

    Regexp should have capture group named ``"branch"`` which should match the expected branch name

    .. warning::

        Exception will be raised if regexp is invalid or does not have expected capture group

    .. warning::

        Exception will also be raised if branch name does not match regexp
