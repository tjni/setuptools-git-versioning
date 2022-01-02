Options
-------

Default options are:

- ``pyproject.toml``:

    .. code:: toml

        [build-system]
        requires = [
            "setuptools>=45",
            "wheel",
            "setuptools-git-versioning",
        ]
        build-backend = "setuptools.build_meta"

        [tool.setuptools_git_versioning]
        template = "{tag}"
        dev_template = "{tag}.post{ccount}+git.{sha}"
        dirty_template = "{tag}.post{ccount}+git.{sha}.dirty"
        starting_version = "0.0.1"
        count_commits_from_version_file = false

- ``setup.py``:

    .. code:: python

        setuptools.setup(
            ...,
            version_config={
                "template": "{tag}",
                "dev_template": "{tag}.post{ccount}+git.{sha}",
                "dirty_template": "{tag}.post{ccount}+git.{sha}.dirty",
                "starting_version": "0.0.1",
                "version_callback": None,
                "version_file": None,
                "count_commits_from_version_file": False,
                "branch_formatter": None,
                "sort_by": None,
            },
        )

-  ``template``: used if no untracked files and latest commit is tagged

-  ``dev_template``: used if no untracked files and latest commit isn't
    tagged

-  ``dirty_template``: used if untracked files exist or uncommitted
    changes have been made

-  ``starting_version``: static value, used if not tags exist in repo

-  ``version_callback``: variable or callback function to get version
    instead of using ``starting_version``

-  ``version_file``: path to VERSION file, to read version from it
    instead of using ``static_version``

-  ``count_commits_from_version_file``: ``True`` to fetch
    ``version_file`` last commit instead of tag commit, ``False`` otherwise

-  ``branch_formatter``: callback to be used for formatting a branch
    name before template substitution

-  ``sort_by``: format string passed to ``git tag --sort=`` command to
    sort the output. Possible values: ``version:refname`` (alphanumeric
    sort), ``committerdate`` (commit date of tag), ``taggerdate`` (tag
    creation date), ``creatordate`` (either commit date or tag creation
   date, **default**). See
    `StackOverflow <https://stackoverflow.com/questions/67206124/what-is-the-difference-between-taggerdate-and-creatordate-for-git-tags>`__
    for more info.

    Note: please do not create annotated tags in the past, it can cause
    issues with detecting versions of existing commits.

Substitutions
~~~~~~~~~~~~~

You can use these substitutions in ``template``, ``dev_template`` or
``dirty_template`` options:

-  ``{tag}``: Latest tag in the repository

-  ``{ccount}``: Number of commits since last tag or last
    ``version_file`` commit (see ``count_commits_from_version_file``)

-  ``{full_sha}``: Full sha hash of the latest commit

-  ``{sha}``: First 8 characters of the sha hash of the latest commit

-  ``{branch}``: Current branch name

-  ``{env:SOMEVAR}``: Value of environment variable ``SOMEVAR``.
    Examples:

    -  You can pass default value using ``{env:SOMEVAR:default}`` syntax.

    -  Default value for missing variables is ``UNKNOWN``. If you need to
        just skip the substitution, use ``{env:SOMEVAR:IGNORE}`` syntax.

    -  It is possible to pass another substitution instead of a default
        value using ``{env:SOMEVAR:{subst}}`` syntax,
        e.g. ``{env:BUILD_NUMBER:{ccount}}``.

-  ``{timestamp:format}``: Current timestamp rendered into a specified format. Examples:

    -  ``{timestamp}`` or ``{timestamp:%s}`` will result ``1632181549``
        (Unix timestamp).

    -  ``{timestamp:%Y-%m-%dT%H-%M-%S}`` will result
        ``2021-09-21T12:34:56``.
