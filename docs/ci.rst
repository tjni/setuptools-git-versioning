.. _ci:

CI configuration
----------------

By default, CI workflows use shallow clone of the repo to speed up clone process.
But this leads to cloning repo without any tags, and thus generating version number like ``0.0.1``.

To avoid this, please use following settings:

.. code-block:: yaml
    :caption: Github Actions

    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      with:
        fetch-depth: 0

.. code-block:: yaml
    :caption: Gitlab CI

    variables:
      GIT_DEPTH: 0
