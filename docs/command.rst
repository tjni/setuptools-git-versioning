.. _command:

Console command
-----------------------------------

Package contains script `setuptools-git-versioning` which can be used for calculating version number.\

See :ref:`_installation` instruction for creating the repo with your package.

To get current package version in `mypackage` repo just execute:

.. code:: bash

    $ cd /path/to/mypackage
    $ setuptools-git-versioning
    0.0.1

    # or pass path to your repo explicitly

    $ setuptools-git-versioning /path/to/mypackage
    0.0.1

Version will be printed to ``stdout``.

This script is a wrapper for ``setuptools_git_versioning`` module, you just call it:

.. code:: bash

    $ python -m setuptools_git_versioning /path/to/mypackage
    0.0.1

``-v`` option enables verbose output which is useful for debugging, messages are printed to ``stderr``:

.. code:: bash

    $ setuptools-git-versioning /path/to/mypackage -v

    INFO: No explicit config passed
    INFO: Searching for config files in '/path/to/mypackage' folder
    INFO: Trying 'setup.py' ...
    INFO: '/path/to/mypackage/pyproject.toml' does not exist
    INFO: Getting latest tag
    INFO: Latest tag: '1.0.0'
    INFO: Tag SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    INFO: Parsing tag_formatter 'util:tag_formatter' of type 'str'
    INFO: Is dirty: False
    INFO: HEAD SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    INFO: Commits count between HEAD and latest tag: 0
    INFO: HEAD is tagged: True
    INFO: Current branch: 'master'
    INFO: Using template from 'template' option
    INFO: Version number after resolving substitutions: '1.0.0'
    INFO: Result: '1.0.0'

    1.0.0


``-vv`` shows even more debug messages:

.. code:: bash

    $ setuptools-git-versioning /path/to/mypackage -vvv

     INFO: No explicit config passed
     INFO: Searching for config files in '/path/to/mypackage' folder
     INFO: Trying 'setup.py' ...
    DEBUG: Adding '/path/to/mypackage' folder to sys.path
     INFO: '/path/to/mypackage/pyproject.toml' does not exist
     INFO: Getting latest tag
    DEBUG: Sorting tags by 'creatordate'
    DEBUG: Executing 'git tag --sort=-creatordate --merged' at '/path/to/mypackage'
     INFO: Latest tag: '1.0.0'
    DEBUG: Executing 'git rev-list -n 1 "1.0.0"' at '/path/to/mypackage'
     INFO: Tag SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
     INFO: Parsing tag_formatter 'util:tag_formatter' of type 'str'
    DEBUG: Executing 'from mypkg.util import tag_formatter'
    DEBUG: Tag after formatting: '1.0.0'
    DEBUG: Executing 'git status --short' at '/path/to/mypackage'
     INFO: Is dirty: False
    DEBUG: Executing 'git rev-list -n 1 "HEAD"' at '/path/to/mypackage'
     INFO: HEAD SHA-256: '8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4'
    DEBUG: Executing 'git rev-list --count HEAD "^8dc9881eacd373cb34c5d3f99a6ad9e2349a79c4"' at '/path/to/mypackage'
     INFO: Commits count between HEAD and latest tag: 0
     INFO: HEAD is tagged: True
    DEBUG: Executing 'git rev-parse --abbrev-ref HEAD' at '/path/to/mypackage'
     INFO: Current branch: 'master'
     INFO: Using template from 'template' option
    DEBUG: Template: '{tag}'
    DEBUG: Args:()
     INFO: Version number after resolving substitutions: '1.0.0'
     INFO: Result: '1.0.0'

    1.0.0


Command help
~~~~~~~~~~~~~

.. argparse::
    :module: setuptools_git_versioning
    :func: _parser
    :prog: setuptools-git-versioning
