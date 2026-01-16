.. _ccount-substitution:

``ccount``
~~~~~~~~~~

Substituted by current number of commits since tag (in case of using :ref:`tag-release`)
or since last commit to a version file (in case of using :ref:`version-file` with :ref:`count-commits-option` option).

If commit counts cannot be determined, ``0`` value is used (since v3.0.0).

Example
^^^^^^^
``"{ccount}"``

Options
^^^^^^^
No
