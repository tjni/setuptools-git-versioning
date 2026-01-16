.. _tag-formatter-option:

``tag_formatter``
~~~~~~~~~~~~~~~~~

Callback to be used for formatting a tag name before template substitution.

.. note::

    This option is completely ignored if :ref:`version-file` or :ref:`version-callback` schemas are used.
    Please set up your VERSION file or callback to return proper version in the first place.

Type
^^^^
``str`` or ``Callable[[str], str]``


Default value
^^^^^^^^^^^^^^
``None``

Usage
^^^^^

It is possible to use (see :ref:`tag-release`) tag name in version number.

But tags should have :pep:`440` compatible name, like:

- ``1.2``
- ``1.2.3``
- ``1.2.3a4``
- ``1.2.3b4``
- ``1.2.3rc4``
- ``1.2.3.pre4``
- ``1.2.3.post4``
- ``1.2.3.dev4``

In case of using tag names like ``release/1.2.3`` or ``rc-1.2``,
you'll get version number which ``pip`` cannot understand.

To fix that you can define a callback which will receive current tag
name and return a properly formatted one:

.. tabs::

    .. code-tab:: python ``my_module/util.py`` file

        import re


        def format_tag_name(name):
            # If tag has name like "release/1.2.3", take only "1.2.3" part
            pattern = re.compile(r"release\/(?P<tag>[^\d.]+)")

            match = pattern.search(name)
            if match:
                return match.group("tag")

            # just left properly named tags intact
            if name.startswith("v"):
                return name

            # fail in case of wrong tag names like "release/unknown"
            raise ValueError(f"Wrong tag name: {name}")

    .. code-tab:: python ``setup.py`` file

        import setuptools
        from my_module.util import format_tag_name

        setuptools.setup(
            ...,
            setup_requires=["setuptools-git-versioning>=3.0,<4"],
            setuptools_git_versioning={
                "enabled": True,
                "dev_template": "{tag}.dev{ccount}",
                "dirty_template": "{tag}.dev{ccount}",
                "tag_formatter": format_tag_name,  # <---
            },
        )

    .. code-tab:: toml ``pyproject.toml`` file

        [build-system]
        requires = [ "setuptools>=41", "wheel", "setuptools-git-versioning>=3.0,<4", ]
        # __legacy__ is required to have access to package
        # during build step
        build-backend = "setuptools.build_meta:__legacy__"

        [project]
        dynamic = ["version"]

        [tool.setuptools-git-versioning]
        enabled = true
        dev_template = "{tag}.dev{ccount}"
        dirty_template = "{tag}.dev{ccount}"
        tag_formatter = "my_module.util:format_tag_name"  # <---

    .. note::

        Please pay attention to ``build-backend`` item in your config, it is important
        for ``setuptools-git-versioning`` to access your module source code.


Possible values
^^^^^^^^^^^^^^^

- ``None``

    Disables this feature

- function/lambda (``setup.py`` only)
- function full name in format ``"some.module:function_name"``

    Function should have signature ``(str) -> str``. It accepts original tag name and returns formatted one

    .. warning::

        Exception will be raised if module or function/lambda is missing or has invalid signature

- regexp like ``".*(?P<tag>\d+).*"``

    Regexp should have capture group named ``"tag"`` matching the expected tag name

    .. warning::

        Exception will be raised if regexp is invalid or does not have expected capture group

    .. warning::

        Exception will also be raised if tag name does not match regexp.
        So this regexp should be able to handle all possible tags in the repo
