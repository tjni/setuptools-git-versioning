.. _env-substitution:

``env``
~~~~~~~~~~~~~~~~~~~~~

Substituted by environment variable.

Example
^^^^^^^
- ``"{env:MYVAR}"``
- ``"{env:MYVAR:default value}"``
- ``"{env:MYVAR:{ccount}}"``
- ``"{env:MYVAR:IGNORE}"``

Options
^^^^^^^
You can pass 2 positional options to this substitution:

- Env variable name (case sensitive)
- Default value if env variable is not set (optional)

  - no default value meaus that variable will be replaced with literal ``"UNKNOWN"``
  - ``some value`` - just plain text
  - ``{ccount}`` - any other substitution is supported (**without nesting**)
  - ``IGNORE`` - just substitute empty string
