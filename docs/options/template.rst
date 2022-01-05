.. _template-option
``template``
~~~~~~~~~~~~~~~~~~~~~

Version number template for :ref:`tag-release` versioning schema.

Used if no untracked files and current commit is tagged.

.. note::

    This option is completely ignored if :ref:`version-file` schema is used.
    This is because all tags are set on ``master`` / ``main`` branch,
    so commits to other branches like ``develop`` are tagless.

.. note::

    This option is completely ignored if :ref:`version-callback` schema is used,
    because git commit history is not fetched in such a case.

Type
^^^^^
``str``

Default value
^^^^^^^^^^^^^
``"{tag}"``

Possible values
^^^^^^^^
See :ref:`substitutions`
