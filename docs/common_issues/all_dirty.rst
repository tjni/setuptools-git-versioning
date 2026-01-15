.. _all-dirty-issue:

Every version built by CI is ``dirty``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually caused by some files created by CI pipeline like build
artifacts or test reports, e.g. ``dist/my_package.whl`` or
``reports/unit.xml``. If these files are not mentioned in ``.gitignore`` file
they will be recognized by git as untracked. Because of that
``git status`` will report that you have **uncommitted (dirty) changes** in
the index, so ``setuptools-git-versioning`` will detect current version
as ``dirty``.

You should such files to the ``.gitignore`` file. In most the cases adding these lines solves the issue:

.. code-block:: txt
    :caption: .gitignore

    build/
    dist/
    eggs/
    *.egg*
    venv

See `full example <https://github.com/dolfinus/setuptools-git-versioning/blob/master/.gitignore>`_.
