Wrong tag ordering/latest tag number detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This could be caused by some unusual way of creating tags in your repo.

Annotated tags
^^^^^^^^^^^^^^

If you're using annotated tags in your git repo, please avoid creating them in non-chronological order.
This can cause issues with detecting versions of existing commits.

Multiple tags on commit
^^^^^^^^^^^^^^^^^^^^^^^

Please do not add multiple tags for the same commit.
It is impossible to automatically determine which one is latest because of ambiguity -
both tag and commit have a creation date, and it is not possible to sort tags by multiple columns.

See also
^^^^^^^^
- :ref:`sort-by-option` option
