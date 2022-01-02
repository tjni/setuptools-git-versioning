.. _dev-release
Development releases (prereleases) from ``dev`` branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, current repo state is:

.. code:: bash

    commit 233f6d72 Dev branch commit (HEAD, dev)
    |
    |    commit 86269212 Current commit (v1.0.0, master)
    |    |
    |   commit e7bdbe51 Another commit
    |    /
    ...
    |
    commit 273c47eb Long long ago
    |
    ...

You want to make development releases (prereleases) from commits to a
``dev`` branch. But there are just no tags here because all of them are
placed in the ``master`` branch only.

Just like the examples above, create a file with a release number
(e.g. ``1.1.0``) in the ``dev`` branch, e.g. ``VERSION.txt``:

.. code:: txt

    1.1.0

But place here **next release number** instead of current one.

Then update your ``setup.py`` or ``pyproject.toml`` file:

.. code:: python

    import os

    HERE = os.path.dirname(__file__)
    VERSION_FILE = os.path.join(HERE, "VERSION.txt")

    setuptools.setup(
        ...,
        version_config={
            "version_file": VERSION_FILE,
            "count_commits_from_version_file": True,
            "dev_template": "{tag}.dev{ccount}",  # suffix now is not .post, but .dev
            "dirty_template": "{tag}.dev{ccount}",  # same thing here
        },
    )

.. code:: toml

    [tool.setuptools-git-versioning]
    version_file = "VERSION"
    count_commits_from_version_file = true
    dev_template = "{tag}.dev{ccount}"
    dirty_template = "{tag}.dev{ccount}"

Then you decided to release new version:

-  Merge ``dev`` branch into ``master`` branch.
-  Tag commit in the ``master`` branch with a proper release version (e.g. ``v1.1.0``). Tag will be used as a version number for the release.
-  Save next release version (e.g. ``1.2.0``) in ``VERSION`` or
   ``version.py`` file in the ``dev`` branch. **Do not place any tags in the ``dev`` branch!**
-  Next commits to a ``dev`` branch will lead to returning this next release version plus dev suffix, like ``1.1.0.dev1`` or so.
-  ``N`` in ``.devN`` suffix is a number of commits since the last change of a certain file.
-  **Note: every change of this file in the ``dev`` branch will lead to this ``N`` suffix to be reset to ``0``. Update this file only in the case when you've setting up the next release version!**
