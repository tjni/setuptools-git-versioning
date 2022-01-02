Every version built by CI is ``dirty``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually caused by some files created by CI pipeline like build
artifacts or test reports, e.g. ``dist/my_package.whl`` or
``reports/unit.xml``. If they are not mentioned in ``.gitignore`` file
they will be recognized by git as untracked. Because of that
``git status`` will report that you have uncommitted (dirty) changes in
the index, so ``setuptools-git-versioning`` will detect current version
as ``dirty``.

You should such files to the ``.gitignore`` file. See `current repo .gitignore <https://github.com/dolfinus/setuptools-git-versioning/blob/master/.gitignore>`__
as an example.
