.. _tag_filter-option:

``tag_filter``
~~~~~~~~~~~~~~~~~~~~~

Callback to be used for filtering tag names before formatting and template
substitution.

.. note::

    This option is completely ignored if :ref:`version-callback` schema is used,
    because git commit history is not fetched in such a case.

Type
^^^^^
``str`` or ``callable``

Default value
^^^^^^^^^^^^^
``None``

Usage
^^^^^^

Set when multiple products are tagged in a single repo.

If, for example, your repo has:

- ``product_x/1.2.0``
- ``product_x/1.2.1``
- ``product_x/1.3.0``
- ``product_y/2.0.0``
- ``product_y/2.1.0``

and you only want versions from ``product_y``, simply set:

.. code:: toml

    tag_filter = "product_y/(?P<tag>.*)"

This will limit the tags considered to those that start with ``product_y``.

You will likely still need to construct a :ref:`tag-formatter-option` that
extract version number from a tag.  To make thing easier, you can often
use the same regexp/callback for both ``tag_filter`` and ``tag_formatter``.

Possible values
^^^^^^^^^^^^^^^
- ``None``

    Disables this feature

- function full name in format ``"some.module:function_name"``

    Function should have signature ``(str) -> bool``. It accepts original
    tag name and returns ``True`` if tag is accepted and ``False`` if not.
    You can return other value type, like ``str`` or ``None``, it will be
    treated as ``bool``.

    .. warning::

        Exception will be raised if module or function/lambda is missing or has invalid signature

- regexp like ``"tag-prefix/.*"`` or ``"tag-prefix/(?P<tag>.*)"``

    .. note::

        The ``<tag>`` group isn't required for the filter, but makes it simpler to
        share with the ``tag_formatter`` option.

    .. warning::

        Exception will be raised if regexp is invalid

    .. warning::

        If regexp doesn't match any tag, the filter will return the empty list, and
        the default "0.0.1" version will be selected.
