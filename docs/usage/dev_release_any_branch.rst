.. _dev-release-any-branch
Development releases (prereleases) from any branch (``feature``/``bugfix``/``preview``/``beta``/etc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like `dev-release`_, but you want to make development releases
(prereleases) with a branch name present in the version number.

In case of branch names which are PEP-440 compatible, you can just use
``{branch}`` substitution in a version template.

For example, if the branch name is something like ``alpha``, ``beta``,
``preview`` or ``rc``:

.. code:: python

    setuptools.setup(
        ...,
        version_config={
            "version_file": VERSION_FILE,
            "count_commits_from_version_file": True,
            "dev_template": "{tag}.{branch}{ccount}",
            "dirty_template": "{tag}.{branch}{ccount}",
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    version_file = "VERSION"
    count_commits_from_version_file = true
    dev_template = "{tag}.{branch}{ccount}"
    dirty_template = "{tag}.{branch}{ccount}"

Adding a commit to the ``alpha`` branch will generate a version number
like ``1.2.3a4``, new commit to the ``beta`` branch will generate a
version number like ``1.2.3b5`` and so on.

It is also possible to use branch names prefixed with a major version
number, like ``1.0-alpha`` or ``1.1.beta``:

.. code:: python

    setuptools.setup(
        ...,
        version_config={
            "count_commits_from_version_file": True,
            "dev_template": "{branch}{ccount}",
            "dirty_template": "{branch}{ccount}",
            "version_file": VERSION_FILE,
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    version_file = "VERSION"
    count_commits_from_version_file = true
    dev_template = "{branch}{ccount}"
    dirty_template = "{branch}{ccount}"

Adding a commit to the ``1.0-alpha`` branch will generate a version
number like ``1.0a2``, new commit to the ``1.2.beta`` branch will
generate a version number like ``1.2b3`` and so on.

But if branch name is not PEP-440 compatible at all, like
``feature/ABC-123`` or ``bugfix/ABC-123``, you'll get version number
which ``pip`` cannot understand.

To fix that you can define a callback which will receive current branch
name and return a properly formatted one:

- ``util.py`` file:

    .. code:: python

        import re


        def format_branch_name(name):
            # If branch has name like "bugfix/issue-1234-bug-title", take only "1234" part
            pattern = re.compile("^(bugfix|feature)\/issue-([0-9]+)-\S+")

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
            version_config={
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
