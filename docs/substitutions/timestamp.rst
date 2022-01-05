.. _timestamp-substitution
``timestamp``
~~~~~~~~~~~~~~~~~~~~~

Substituted by current timestamp with formatting it.

Example
^^^^^^^
``"{timestamp}"``
``"{timestamp:%s}"``
``"{timestamp:%Y-%m-%dT%H-%M-%S}"``

Options
^^^^^
You can pass 1 positional option to this substitution:

- Format (optional)

  Could be any format supported by `stftime <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_.

  - no format means ``%s`` (unix timestamp, e.g. ``1641342388``)
  - ``%Y-%m-%dT%H-%M-%S`` means current datetime like ``"2021-12-31T11-22-33"``)


  .. note::

    ``setuptools`` is removing all leading zeros (e.g. ``00`` in ``1.001.002``)
    to produce PEP-440 compliant version number.

    If you're using datetime as your
    version number, you can get unexpected results like ``"2021.1.1"`` instead of
    ``"2021.01.01"`` because of such removal.

    So it is recommended to use timestamp either in local version part (``git.sha`` in ``1.2.3+git.sha``)
    or to use just year number in public version (``1.2.3``).
