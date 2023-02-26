.. _runtime-version:

Retrieving package version at runtime
-------------------------------------

Using ``version_file`` option (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of using :ref:`version_file <version-file>` option you can directly read the ``VERSION`` file content,
and use at as version number.

To resolve version number in runtime, you should move ``VERSION`` file to your module subfolder:

- ``setup.py``:

    Create ``MANIFEST.in`` file in the project root:

    .. code::

        include my_module/VERSION

    Then make few changes in ``setup.py``:

    .. code:: python

        ...

        # change VERSION file path
        version_file = root_path / "my_module" / "VERSION"

        setuptools.setup(
            ...,
            setuptools_git_versioning={
                "enabled": True,
                "version_file": version_file,
            },
            # read MANIFEST.in and include files mentioned here to the package
            include_package_data=True,
            # this package will read some included files in runtime, avoid installing it as .zip
            zip_safe=False,
        )

- ``pyproject.toml``:

    .. code:: toml

        [tool.setuptools.package-data]
        # include VERSION file to a package
        my_module = ["VERSION"]
        # this package will read some included files in runtime, avoid installing it as .zip
        zip-safe = false

        [tool.setuptools-git-versioning]
        enabled = true
        # change the file path
        version_file = "my_module/VERSION"

And then read this file:

.. code:: python

    # content of my_module/__init__.py

    from pathlib import Path

    # you can use os.path and open() as well
    __version__ = Path(__file__).parent.joinpath("VERSION").read_text()


Using ``version_callback`` option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of using :ref:`version_callback <version-callback>` option you can directly call this callback inside a module:

.. code:: python

    # content of my_module/__init__.py

    from my_module.version import get_version

    __version__ = get_version()


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

Using ``pkg_resources``
~~~~~~~~~~~~~~~~~~~~~~~

In some cases ``importlib`` cannot properly detect package version,
for example it was compiled into executable file, so it uses some
custom import mechanism.

Instead, you can use ``pkg_resources`` which is included in ``setuptools``
(but has a significant runtime cost):

.. code:: python

    from pkg_resources import get_distribution, DistributionNotFound

    try:
        __version__ = get_distribution("package-name").version
    except DistributionNotFound:
        # package is not installed
        pass

However, this does place a runtime dependency on setuptools,
and can add up to a few 100ms overhead for the package import time.

Calling internals of ``setuptools_git_versioning`` module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

    This way is STRONGLY DISCOURAGED. Functions in the module
    are not a part of public API, and could be changed in the future without
    maintaining backward compatibility.

.. warning::

    Use this ONLY in CI/CD tools.

    NEVER use ``setuptools_git_versioning`` inside your package, because ``.git``
    folder is not being included into it, and target OS can lack of ``git`` executable.

    ``.git`` folder and ``git`` executable presence is crucial
    for ``setuptools-git-versioning`` to work properly.

.. code:: python

    from setuptools_git_versioning import get_version

    # uses setup.py or pyproject.toml as config source
    version = get_version()

    from setuptools_git_versioning import get_tag, get_all_tags

    # calls `git` executable to get latest tag merged into HEAD history tree
    latest_tag = get_tag()

    # calls `git` executable to get all the tags in the repo
    all_tags = get_all_tags()
