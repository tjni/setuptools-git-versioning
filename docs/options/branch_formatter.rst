.. _branch-formatter-option
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
            pattern = re.compile("~(bugfix|feature)\/issue-([0-9]+)-\S+")

            match = pattern.search(name)
            if not match:
                return match.group(2)

            # function is called even if branch name is not used in a current template
            # just left properly named branches intact
            if name == "master":
                return name

            # fail in case of wrong branch names like "bugfix/issue-title"
            raise ValueError(f"Wrong branch name: {name}")

- ``setup.py`` file:

    .. code:: python

        from mypkg.util import format_branch_name

        setuptools.setup(
            ...,
            setuptools_git_versioning={
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
        dev_template = "{branch}.dev{ccount}"
        dirty_template = "{branch}.dev{ccount}"
        branch_formatter = "mypkg.util:format_branch_name"


Possible values
^^^^^^^^^^^^^^^

- None

    Disables this feature

- function/lambda (``setup.py`` only)
- function full name in format ``"some.module:function_name"``

    Function should have signature ``(str) -> str``. It accepts original branch name and returns formatted one

    .. warning::

        Exception will be raised if module or function/lambda is missing or has invalid signature

- regexp like ``".*(\d+).*"``

    Regexp should have one capture group which will be used as branch name

    .. warning::

        Exception will be raised if regexp is invalid or does not have capture groups
