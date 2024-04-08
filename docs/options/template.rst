.. _template-option:

``template``
~~~~~~~~~~~~~~~~~~~~~

Version number template for :ref:`tag-release` versioning schema.

Used if no untracked files and current commit is tagged.

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
^^^^^^^^^^^^^^^
Any string which produces :pep:`440` compliant version number after substituting all necessary values.

See :ref:`substitutions`
