.. _runtime-version:

Retrieving package version at runtime
-------------------------------------

Using ``version_file`` or ``version_callback`` options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred way to set version number inside a package is
to simply store it in some file or variable/function, and
then use it in ``setup.py`` / ``pyproject.toml`` as version source.

It this case you can get current version without any access to ``.git`` folder
(which is required by ``setuptools-git-versioning``).

See:

* :ref:`version-file`
* :ref:`version-callback`

Using ``importlib``
~~~~~~~~~~~~~~~~~~~

If you have opted not to hardcode the version number inside the package,
you can retrieve it at runtime from :pep:`0566` metadata using
``importlib.metadata`` from the standard library (added in Python 3.8)
or the `importlib_metadata`_ backport:

.. code:: python

    from importlib.metadata import version, PackageNotFoundError

    try:
        __version__ = version("package-name")
    except PackageNotFoundError:
        # package is not installed
        pass

.. _importlib_metadata: https://pypi.org/project/importlib-metadata/
