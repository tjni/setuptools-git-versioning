Changelog
==========

1.13
----

.. changelog::
    :version: 1.13.3

    .. change::
        :tags: general, feature

        Test PyPy 3.10 support

    .. change::
        :tags: ci, feature

        Push release using ``Trusted publishers`` feature of PyPI.org

.. changelog::
    :version: 1.13.3
    :released: 14.03.2023

    .. change::
        :tags: docs, bugfix
        :tickets: 78

        Move ``zip-safe`` option to ``tool.setuptools`` section of ``pyproject.toml``.

        Thanks to :github-user:`cclecle`

.. changelog::
    :version: 1.13.2
    :released: 26.02.2023

    .. change::
        :tags: docs, feature
        :tickets: 77, 75

        Recommend users to use file-based schema instead of tag-based due some cases.

    .. change::
        :tags: docs, feature
        :tickets: 17

        Add small example of ``.gitignore`` file to common issues section. Thanks to :github-user:`aram-eskandari`

    .. change::
        :tags: docs, feature
        :tickets: 55

        Improve examples of fetching package version in runtime.

.. changelog::
    :version: 1.13.1
    :released: 13.11.2022

    .. change::
        :tags: general, feature
        :tickets: 72, 49

        Build and publish sdist package again

    .. change::
        :tags: general, bugfix
        :tickets: 72, 49

        Allow to install package from ``.tar.gz`` without ``--no-build-isolation`` flag

    .. change::
        :tags: ci, feature

        Publish development releases to `Test PyPI <test.pypi.org>`_

    .. change::
        :tags: ci, feature

        Use ``pypa/gh-action-pypi-publish`` Github action to publish releases to PyPI

    .. change::
        :tags: ci, bugfix

        Remove local part of version because it is not allowed in PyPI

    .. change::
        :tags: dependency, bugfix
        :tickets: 72

        Get rid of ``deprecated`` package dependency

.. changelog::
    :version: 1.13.0
    :released: 01.11.2022

    .. change::
        :tags: dependency, feature

        For Python 3.11 use built-in ``tomllib`` instead of ``toml`` package

    .. change::
        :tags: docs, feature
        :tickets: 55

        Add documentation about fetching package version in runtime

    .. change::
        :tags: core, breaking

        Make all internal functions private

    .. change::
        :tags: docs, feature

        Add description for some functions

    .. change::
        :tags: core, feature
        :pullreq: 69
        :tickets: 68

        Add ``tag_filter`` option. Special thanks to :github-user:`vortechs2000`

1.12
----

.. changelog::
    :version: 1.12.1
    :released: 24.10.2022

    .. change::
        :tags: core, bug
        :tickets: 67

        Make version sanitization less strict, allow to automatically convert some cases, e.g.
        ``1.0.0+feature/abc`` to ``1.0.0+feature.abc``

.. changelog::
    :version: 1.12.0
    :released: 13.10.2022

    .. change::
        :tags: core, breaking

        Sanitize ``starting_version`` according :pep:`440`

    .. change::
        :tags: core, breaking

        Do not remove leading non-numeric symbols from version number (except ``v``)

1.11
----

.. changelog::
    :version: 1.11.0
    :released: 02.10.2022

    .. change::
        :tags: core, feature
        :tickets: 58

        Allow ``setuptools-git-versioning`` script to infer version from ``setup.py`` if ``pyproject.toml`` is missing

    .. change::
        :tags: core, breaking

        Raise error if ``pyproject.toml`` exists, but is not a file

    .. change::
        :tags: core, feature

        Add ``cwd`` argument to most of functions, allowing to get versions of a specific repo without changing current directory

    .. change::
        :tags: dev, feature

        Add info and debug messages to the module

    .. change::
        :tags: docs, feature
        :tickets: 58

        Add documentation for ``setuptools-git-versioning`` script

    .. change::
        :tags: tests, refactoring

        Use builtin type annotations (instead of type comments) in ``tests/lib/util.py``,
        use modern annotations syntax (``type | None`` instead of ``Optional[type]``)

1.10
----

.. changelog::
    :version: 1.10.1
    :released: 03.09.2022

    .. change::
        :tags: core, feature
        :tickets: 58

        Add ``setuptools-git-versioning`` script to infer version from ``pyproject.toml`` config

    .. change::
        :tags: core, feature

        Check Python 3.11 support

.. changelog::
    :version: 1.10.0
    :released: 18.07.2022

    .. change::
        :tags: core, breaking
        :tickets: 56

        :ref:`version-callback-option` option is used even if there are some tags in the current branch

    .. change::
        :tags: config, feature

        Raise exception if both :ref:`version-callback-option` and :ref:`version-file-option` options are set

    .. change::
        :tags: core, feature

        Remove all non-numeric symbols from version prefix, not just ``v``

1.9
----

.. changelog::
    :version: 1.9.2
    :released: 21.03.2022

    .. change::
        :tags: general
        :tickets: 49

        Add ``setup_requires`` item to ``setup.py``

.. changelog::
    :version: 1.9.1
    :released: 21.03.2022

    .. change::
        :tags: general
        :tickets: 49

        Remove ``pyproject.toml`` file from ``.tag.gz`` package

.. changelog::
    :version: 1.9.0
    :released: 21.03.2022

    .. change::
        :tags: general, breaking

        Drop Python 2.7, 3.5 and 3.6 support. Minimal supported Python version is now 3.7

    .. change::
        :tags: core, feature
        :tickets: 49

        Do not fail on ``toml`` and ``packaging`` modules import while installing ``setuptools-git-versioning`` from ``tag.gz`` file

    .. change::
        :tags: ci, bug

        Fix creating multiple releases for the same tag

1.8
----

.. changelog::
    :version: 1.8.1
    :released: 10.01.2022

    .. change::
        :tags: core, bug
        :tickets: 35

        Fix issue with empty ``pyproject.toml``

.. changelog::
    :version: 1.8.0
    :released: 07.01.2022

    .. change::
        :tags: general, breaking
        :pullreq: 37

        Drop Python 3.3 and 3.4 support

    .. change::
        :tags: general, deprecated

        Python 2.7, 3.5 and 3.6 support is deprecated due to their end of life.

    .. change::
        :tags: core, deprecated

        ``get_branch_tags`` function is renamed to ``get_tags``.

        It will be removed in ``2.0.0`` release. A warning message is added

    .. change::
        :tags: config, deprecated

        ``version_config`` keyword in ``setup.py`` is renamed to ``setuptools_git_versioning``.

        It will be removed in ``2.0.0`` release. A warning message is added

    .. change::
        :tags: config, deprecated

        Prefer using ``"enabled": True`` / ``"enabled": False`` option
        instead of pure boolean values (``True``, ``False``) for config.

        Old behavior is deprecated and will be removed in ``2.0`` version. A warning message is added

    .. change::
        :tags: core, feature
        :pullreq: 37
        :tickets: 35

        Add support of reading config from ``pyproject.toml``.

        Thanks to :github-user:`Bloodmallet`

    .. change::
        :tags: core, feature

        Allow to pass regexp to ``branch_formatter`` option

    .. change::
        :tags: core, feature
        :tickets: 31

        Add ``tag_formatter`` option

    .. change::
        :tags: core, feature

        Allow nested default values to be passed to ``env`` substitution

    .. change::
        :tags: tests, feature

        Add integration tests

    .. change::
        :tags: ci, feature

        Check test coverage and fail if it has been decreased

    .. change::
        :tags: ci, feature

        Build docs using ReadTheDocs project

    .. change::
        :tags: docs, feature

        Major docs improvement

    .. change::
        :tags: docs, feature

        Added CHANGELOG.rst

    .. change::
        :tags: docs

        Add ``miniver`` and ``versioningit`` to comparison table

1.7
----

.. changelog::
    :version: 1.7.4
    :released: 31.10.2021

    .. change::
        :tags: ci, feature

        Change release workflow action from ``actions/create-release@v1``
        to ``softprops/action-gh-release@v1``

.. changelog::
    :version: 1.7.3
    :released: 31.10.2021

    .. change::
        :tags: ci, feature

        Change release workflow action from ``actions/create-release@v1``
        to ``softprops/action-gh-release@v1``

.. changelog::
    :version: 1.7.2
    :released: 28.10.2021

    .. change::
        :tags: core, feature
        :tickets: 29

        String leading 'v' symbol from tag name

.. changelog::
    :version: 1.7.1
    :released: 28.10.2021

    .. change::
        :tags: core, feature
        :tickets: 29

        String leading 'v' symbol from tag name

.. changelog::
    :version: 1.7.0
    :released: 21.09.2021

    .. change::
        :tags: core, feature

        Add support of ``env`` variables substitution

    .. change::
        :tags: core, feature

        Add support of ``timestamp`` substitution


1.6
----

.. changelog::
    :version: 1.6.1
    :released: 16.09.2021

    .. change::
        :tags: core, bug
        :tickets: 23

        Fix sorting for annotated tags

.. changelog::
    :version: 1.6.0
    :released: 15.09.2021

    .. change::
        :tags: ci, bug

        Fix skipping duplicated runs

    .. change::
        :tags: ci, feature

        Add automerge action for ``precommit-ci`` bot

    .. change::
        :tags: ci, bug

        Fix tests workflow

    .. change::
        :tags: core, bug
        :tickets: 22

        Sort tags by commit date instead of name

    .. change::
        :tags: ci, bug

        Fix release pipeline



1.5
----

.. changelog::
    :version: 1.5.0
    :released: 16.08.2021

    .. change::
        :tags: docs
        :tickets: 15

        Add ``setuptools-scm`` and ``versioneer`` to comparison table

    .. change::
        :tags: docs, feature
        :tickets: 17
        :pullreq: 16

        Add resolution for issue when all versions produced by CI pipeline are ``dirty``

    .. change::
        :tags: ci, feature

        Skip duplicated Github Actions runs

    .. change::
        :tags: dev, feature

        Add ``pre-commit`` hooks and commit changes made by it


1.4
----

.. changelog::
    :version: 1.4.0
    :released: 12.05.2021

    .. change::
        :tags: ci, bug

        Use absolute paths in ``setup.py``

    .. change::
        :tags: dev, bug
        :pullreq: 13

        Add JetBrains config files to ``.gitignore``.

        Thanks to :github-user:`LeComptoirDesPharmacies`

    .. change::
        :tags: core, feature
        :pullreq: 14

        Add ``branch_formatter`` option.

        Thanks to :github-user:`LeComptoirDesPharmacies`


1.3
----

.. changelog::
    :version: 1.3.6
    :released: 12.03.2021

    .. change::
        :tags: general, bug

        Update package short description

    .. change::
        :tags: general

        Set license in ``setup.py`` file

.. changelog::
    :version: 1.3.5
    :released: 12.03.2021

    .. change::
        :tags: docs, bug

        Fix comparison table typo

    .. change::
        :tags: docs, feature

        Add license column into comparison table

.. changelog::
    :version: 1.3.4
    :released: 12.03.2021

    .. change::
        :tags: docs, feature

        Add list of supported substitutions into comparison table

    .. change::
        :tags: docs

        Add ``bad-setuptools-git-version`` and ``another-setuptools-git-version``
        to comparison table

.. changelog::
    :version: 1.3.3
    :released: 12.03.2021

    .. change::
        :tags: core, bug
        :pullreq: 11

        Replace forbidden chars in local version label.

        Thanks to :github-user:`ajasmin`

.. changelog::
    :version: 1.3.2
    :released: 12.03.2021

    .. change::
        :tags: docs, bug

        Fix minor typos in documentation

.. changelog::
    :version: 1.3.1
    :released: 12.03.2021

    .. change::
        :tags: docs, feature
        :tickets: 8

        Add Windows support column into comparison table

    .. change::
        :tags: ci, bug

        Fix Github Actions

    .. change::
        :tags: core, bug
        :tickets: 10

        Replace default suffix for dev and dirty versions from ``dev`` to ``post``

    .. change::
        :tags: docs, feature
        :tickets: 10

        Major documentation update

.. changelog::
    :version: 1.3.0
    :released: 01.03.2021

    .. change::
        :tags: core, feature
        :tickets: 9

        Add ``full_sha`` substitution support


1.2
----

.. changelog::
    :version: 1.2.10
    :released: 04.02.2021

    .. change::
        :tags: ci, bug
        :pullreq: 7

        Fix release workflow

    .. change::
        :tags: ci, feature
        :pullreq: 7

        Add some issue and PR automatization

    .. change::
        :tags: core, bug
        :tickets: 8

        Fix Windows compatibility

.. changelog::
    :version: 1.2.9
    :released: 20.01.2021

    .. change::
        :tags: ci, feature
        :pullreq: 7

        Use Github Actions instead of TravisCI

.. changelog::
    :version: 1.2.8
    :released: 29.11.2020

    .. change::
        :tags: docs, bug
        :pullreq: 6

        Fixed typo in code examples.

        Thanks to :github-user:`Stedders`

.. changelog::
    :version: 1.2.7
    :released: 24.11.2020

    .. change::
        :tags: core, bug
        :pullreq: 5

        Fix python error if no tag is found.

        Thanks to :github-user:`bmiklautz`

.. changelog::
    :version: 1.2.6
    :released: 07.10.2020

    .. change::
        :tags: core, bug

        Fix version detection in case of missing .git folder

.. changelog::
    :version: 1.2.5
    :released: 30.09.2020

    .. change::
        :tags: dependency, bug

        Fix Python 2.7 dependencies

.. changelog::
    :version: 1.2.4
    :released: 30.09.2020

    .. change::
        :tags: dependency, bug

        Fix Python 2.7 dependencies

.. changelog::
    :version: 1.2.3
    :released: 16.09.2020

    .. change::
        :tags: core, feature

        Add ``get_all_tags`` function

    .. change::
        :tags: core, feature

        Add ``get_branch_tags`` function

.. changelog::
    :version: 1.2.2
    :released: 14.09.2020

    .. change::
        :tags: core, bug

        Fix building version from VERSION file

.. changelog::
    :version: 1.2.1
    :released: 10.09.2020

    .. change::
        :tags: core, feature

        Add ``count_commits_from_version_file`` option

.. changelog::
    :version: 1.2.0
    :released: 10.09.2020

    .. change::
        :tags: core, feature

        Add ``version_file`` option


1.1
----
.. changelog::
    :version: 1.1.14
    :released: 10.09.2020

    .. change::
        :tags: core, feature

        Add ``version_callback`` option

.. changelog::
    :version: 1.1.13
    :released: 21.08.2020

    .. change::
        :tags: ci, bug
        :tickets: 4

        Use ``six`` module for accessing ``collections.abc``

.. changelog::
    :version: 1.1.12
    :released: 20.08.2020

    .. change::
        :tags: ci, bug
        :tickets: 4

        Fix package name misspell

.. changelog::
    :version: 1.1.11
    :released: 18.08.2020

    .. change::
        :tags: dependency, bug

        Remove ``flake8`` from ``requirements.txt``

.. changelog::
    :version: 1.1.10
    :released: 18.08.2020

    .. change::
        :tags: dependency, bug

        Make ``setuptools`` version check less strict

.. changelog::
    :version: 1.1.9
    :released: 17.08.2020

    .. change::
        :tags: general, feature

        Test Python 3.9 support

    .. change::
        :tags: ci, bug
        :tickets: 3

        Include ``requirements.txt`` into ``.tar.gz`` file

.. changelog::
    :version: 1.1.8
    :released: 14.08.2020

    .. change::
        :tags: general, feature

        Add Python 3.3 and 3.4 support

.. changelog::
    :version: 1.1.7
    :released: 10.08.2020

    .. change::
        :tags: ci, bug

        Fix TravisCI deploy

.. changelog::
    :version: 1.1.6

    .. change::
        :tags: core, feature

        Add backward compatibility with ``git`` < 2.2

    .. change::
        :tags: docs, feature

        Add supported python versions badge

.. changelog::
    :version: 1.1.5
    :released: 07.08.2020

    .. change::
        :tags: core, bug
        :pullreq: 1

        Fix runtime error on Python 3.3 and 3.4.

        Thanks to :github-user:`WildCard65`

.. changelog::
    :version: 1.1.4
    :released: 07.08.2020

    .. change::
        :tags: core, feature

        Add ``branch`` substitution support

.. changelog::
    :version: 1.1.3
    :released: 30.07.2020

    .. change::
        :tags: core, feature

        Add ``starting_version`` option

    .. change::
        :tags: ci, bug

        Fix TravisCI build

.. changelog::
    :version: 1.1.2
    :released: 29.07.2020

    .. change::
        :tags: ci, bug

        Fix Python 2 version build

    .. change::
        :tags: dependency, bug

        Fix ``requirements.txt``

.. changelog::
    :version: 1.1.1

    .. change::
        :tags: general, feature

        Change package name to ``setuptools-git-versioning`` and publish it on PyPi.org

.. changelog::
    :version: 1.1.0

    .. change::
        :tags: general

        Create fork of unmaintained repo `setuptools-git-ver <https://github.com/camas/setuptools-git-ver>`_

    .. change::
        :tags: core, feature

        Added Python2 support.

        Typehints moved to comments section.
        Python 3 syntax replaced with Python 2 compatible one

    .. change::
        :tags: core, feature

        Make internal functions public

    .. change::
        :tags: core, feature

        Add ``get_tags`` method
