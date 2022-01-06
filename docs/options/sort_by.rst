.. _sort-by-option:

``sort_by``
~~~~~~~~~~~~~~~~~~~~~

Format string passed to ``git tag --sort=`` command to sort the output.

Used by :ref:`tag-release` versioning schema to get the latest tag in the current branch.

.. note::

    This option is completely ignored if :ref:`version-file` schema is used.
    This is because all tags are set on ``master`` / ``main`` branch,
    so commits to other branches like ``develop`` are tagless.

.. note::

    This option is completely ignored if :ref:`version-callback` schema is used,
    because git commit history is not fetched in such a case.

Type
^^^^^^^^^^^^^^

``str``


Default value
^^^^^^^^^^^^^^
``"creatordate"``


Possible values
^^^^^^^^^^^^^^^^
- ``"creatordate"`` (either commit date or tag creation date)

- ``"version:refname"`` (alphanumeric sort by tag name)

    .. warning::

        This field can produce wrong version numbers in some cases, not recommended to use

- ``"committerdate"`` (commit date of commit tag)

    .. warning::

        This field is missing in case of annotated tags, not recommended to use

- ``"taggerdate"`` (annotated tag creation date)

    .. warning::

        This field is missing in case of commit tags, not recommended to use

See also
""""""""
- `Git documentation <https://git-scm.com/docs/git-for-each-ref#Documentation/git-for-each-ref.txt-contentslinesN>`_

- `StackOverflow <https://stackoverflow.com/questions/67206124/what-is-the-difference-between-taggerdate-and-creatordate-for-git-tags>`_
