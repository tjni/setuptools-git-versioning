.. _version_callback-option
``version_callback``
~~~~~~~~~~~~~~~~~~~~~

Callback to be used for getting a version number.

Used by :ref:`version-callback` versioning schema.

.. note::

    This option is completely ignored if :ref:`version-file` or :ref:`tag-release` schemas are used.

Type
^^^^^^^^^^^^^^

``str`` or ``callable``


Default value
^^^^^^^^^^^^^^
``None``


Possible values
^^^^^^^^^^^^^^^

- None

    Disables this feature

- function/lambda (``setup.py`` only)
- function full name in format ``"some.module:function_name"``

    Function should have signature ``() -> str``. It should return version number

- variable (``setup.py`` only)
- variable full name in format ``"some.module:veriable_name"``

    Variable should contain ``str`` value with version number

.. warning::

    If function return value or variable content is not PEP-440 compatible version, the exception will be raised

.. warning::

    Exception will also be raised if module or function/lambda/variable is missing
