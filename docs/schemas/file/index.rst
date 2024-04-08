.. _file-based-release:

File-based release (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, ``setuptools-git-versioning`` can be used only within:

* git repo, which means a ``.git`` subfolder should exist in the repo root folder
* branch with at least one tag

Otherwise it will be impossible to get project version based on the git repo commits,
and ``setuptools-git-versioning`` will return version number ``0.0.1`` (or other value set up by :ref:`starting-version-option`).

But one or all of these requirements cannot be satisfied in the following cases:

* Downloading source tarball without ``.git`` folder (:issue:`77`).
* Shallow repo clone without tags (:issue:`75`).
* Getting version number from a branch which does not contain any tags (`Git-flow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`_ and its derivatives)

To avoid getting meaningless version number prefer using versioning schema described below.

.. toctree::
    :maxdepth: 1

    version_file
    dev_release_file
