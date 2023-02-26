.. _file-based-release:

File-based release (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Prefer this schema because it allows to get a version number in the following cases:
        * Downloading source tarball without ``.git`` folder (:issue:`77`).
        * Shallow repo clone without tags (:issue:`75`).
        * Getting version number from a branch which does not contain any tags (`Git-flow <https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow>`__ and its derivatives)

.. toctree::
    :maxdepth: 1

    version_file
    dev_release_file
