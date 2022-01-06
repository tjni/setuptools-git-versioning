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
- Default value (optional)

  Used if environment variable is not set.

  - no value or empty string means that variable will be replaced with string value ``UNKNOWN``
  - ``some value`` - any plain text
  - ``{ccount}`` - any other substitution is supported
  - ``{env:MISSINGVAR:{ccount}}`` - nested substitutions are allowed too
  - ``IGNORE`` - return empty string
