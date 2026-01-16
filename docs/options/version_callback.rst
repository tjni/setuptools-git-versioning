.. _version-callback-option:

``version_callback``
~~~~~~~~~~~~~~~~~~~~

Callback to be used for getting a version number.

Used by :ref:`version-callback` versioning schema.

.. note::

    This option conflicts with :ref:`version-file-option`, only one of them can be set.

Type
^^^^
``str`` or ``Callable[[], str]``


Default value
^^^^^^^^^^^^^
``None``


Possible values
^^^^^^^^^^^^^^^

- ``None``

    Disables this feature

- function/lambda (``setup.py`` only)
- function full name in format ``"some.module:function_name"``

    Function should have signature ``() -> str``. It should return version number

- variable (``setup.py`` only)
- variable full name in format ``"some.module:veriable_name"``

    Variable should contain ``str`` value with version number

.. note::

    If your config file is ``pyproject.toml`` you should add this to allow ``setuptools-git-versioning`` to access your module source code:

    .. code-block:: toml
        :caption: pyprojecy.toml

        [build-system]
        ...
        build-backend = "setuptools.build_meta:__legacy__"
        ...

.. warning::

    If function return value or variable content is not :pep:`440` compatible version, the exception will be raised

.. warning::

    Exception will also be raised if module or function/lambda/variable is missing
