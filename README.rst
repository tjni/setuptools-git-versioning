*************************
setuptools-git-versioning
*************************

|ReadTheDocs| |PyPI| |PyPI License| |PyPI Python Version|
|Build| |Coverage| |pre-commit.ci|

.. |ReadTheDocs| image:: https://img.shields.io/readthedocs/setuptools-git-versioning.svg
   :target: https://setuptools-git-versioning.readthedocs.io
.. |PyPI| image:: https://badge.fury.io/py/setuptools-git-versioning.svg
   :target: https://badge.fury.io/py/setuptools-git-versioning
.. |PyPI License| image:: https://img.shields.io/pypi/l/setuptools-git-versioning.svg
   :target: https://github.com/dolfinus/setuptools-git-versioning/blob/master/LICENSE
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/setuptools-git-versioning.svg
   :target: https://badge.fury.io/py/setuptools-git-versioning
.. |Build| image:: https://github.com/dolfinus/setuptools-git-versioning/workflows/Tests/badge.svg
   :target: https://github.com/dolfinus/setuptools-git-versioning/actions
.. |Coverage| image:: https://codecov.io/gh/dolfinus/setuptools-git-versioning/branch/master/graph/badge.svg?token=GIMVHUTNW4
   :target: https://codecov.io/gh/dolfinus/setuptools-git-versioning
.. |pre-commit.ci| image:: https://results.pre-commit.ci/badge/github/dolfinus/setuptools-git-versioning/master.svg
   :target: https://results.pre-commit.ci/latest/github/dolfinus/setuptools-git-versioning/master

Use git repo data (latest tag, current commit hash, etc) for building a
version number according
`PEP-440 <https://www.python.org/dev/peps/pep-0440/>`__.

.. documentation

Documentation
--------------

See https://setuptools-git-versioning.readthedocs.io

.. contribution

Contribution Guide
------------------

See ./CONTRIBUTING.rst

.. installation

Installation
------------

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

Just add ``setuptools-git-versioning`` to ``build-sytem`` part of your ``pyproject.toml``

.. code:: toml

    [build-system]
    requires = [ "setuptools>=41", "wheel", "setuptools-git-versioning", ]
    build-backend = "setuptools.build_meta"

``setup.py``
~~~~~~~~~~~~~~

Just add ``setuptools-git-versioning`` to ``setup_requires`` part of your ``setup.py``

.. code:: python

    import setuptools

    setuptools.setup(
        ...,
        setup_requires=["setuptools-git-versioning"],
    )
