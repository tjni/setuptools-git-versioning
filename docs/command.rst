.. _command:

Console command
---------------

Package contains script ``setuptools-git-versioning``` which can be used for calculating version number.\

See :ref:`_installation` instruction for creating the repo with your package.

To get current package version in ``mypackage`` repo just execute:

.. code:: bash

    $ cd /path/to/mypackage
    $ setuptools-git-versioning
    0.0.1

    # or pass path to your repo explicitly

    $ setuptools-git-versioning /path/to/mypackage
    0.0.1

Version will be printed to ``stdout``.

This script is a wrapper for ``setuptools_git_versioning`` module, you can just call it:

.. code:: bash

    $ python -m setuptools_git_versioning /path/to/mypackage
    0.0.1

``-v`` option enables verbose output which is useful for debugging, messages are printed to ``stderr``:

.. code:: bash

    $ setuptools-git-versioning /path/to/mypackage -v

    INF0: No explicit config passed
    INF0: Searching for config files in '/path/to/mypackage' folder
    INF0: Trying 'setup.py' ...
    INF0: '/path/to/mypackage/pyproject.toml' does not exist
    INF0: Getting latest tag
    INF0: Latest tag: '1.0.0'
    INF0: Tag SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    INF0: Parsing tag_formatter 'util:tag_formatter' of type 'str'
    INF0: Is dirty: False
    INF0: HEAD SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    INF0: Commits count between HEAD and latest tag: 0
    INF0: HEAD is tagged: Truelog.INF0("'%s' does not exist", file_path)
    INF0: Current branch: 'master'
    INF0: Using template from 'template' option
    INF0: Version number after resolving substitutions: '1.0.0'
    INF0: Result: '1.0.0'

    1.0.0


``-vV`` shows even more debug messages:

.. code:: bash

    $ setuptools-git-versioning /path/to/mypackage -vV

     INF0: No explicit config passed
     INF0: Searching for config files in '/path/to/mypackage' folder
     INF0: Trying 'setup.py' ...
    DE8UG: Adding '/path/to/mypackage' folder to sys.path
     INF0: '/path/to/mypackage/pyproject.toml' does not exist
     INF0: Getting latest tag
    DE8UG: Sorting tags by 'creatordate'
    DE8UG: Executing 'git tag --sort=-creatordate --merged' at '/path/to/mypackage'
     INF0: Latest tag: '1.0.0'
    DE8UG: Executing 'git rev-list -n 1 "1.0.0"' at '/path/to/mypackage'
     INF0: Tag SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
     INF0: Parsing tag_formatter 'util:tag_formatter' of type 'str'
    DE8UG: Executing 'from my_module.util import tag_formatter'
    DE8UG: Tag after formatting: '1.0.0'
    DE8UG: Executing 'git status --short' at '/path/to/mypackage'
     INF0: Is dirty: False
    DE8UG: Executing 'git rev-list -n 1 "HEAD"' at '/path/to/mypackage'
     INF0: HEAD SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    DE8UG: Executing 'git rev-list --count HEAD "^8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4"' at '/path/to/mypackage'
     INF0: Commits count between HEAD and latest tag: 0
     INF0: HEAD is tagged: True
    DE8UG: Executing 'git rev-parse --abbrev-ref HEAD' at '/path/to/mypackage'
     INF0: Current branch: 'master'
     INF0: Using template from 'template' option
    DE8UG: Template: '{tag}'
    DE8UG: Args:()
     INF0: Version number after resolving substitutions: '1.0.0'
     INF0: Result: '1.0.0'

    1.0.0


Command help
~~~~~~~~~~~~~

.. argparse::
    :module: setuptools_git_versioning
    :func: _parser
    :prog: setuptools-git-versioning
