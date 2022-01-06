.. _dirty-template-option:

``dirty_template``
~~~~~~~~~~~~~~~~~~~~~

Version number template for :ref:`tag-release` or :ref:`version-file` versioning schemas.

Used if untracked files exist or uncommitted changes have been made.

.. note::

    This option is completely ignored if :ref:`version-callback` schema is used,
    because git commit history is not fetched in such a case.

Type
^^^^^
``str``

Default value
^^^^^^^^^^^^^
``"{tag}.post{ccount}+git.{sha}.dirty"``


Possible values
^^^^^^^^^^^^^^^
Any string which produces :pep:`440` compliant version number after substituting all necessary values.

See :ref:`substitutions`
