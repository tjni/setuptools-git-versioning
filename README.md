# setuptools-git-versioning

[![PyPI version](https://badge.fury.io/py/setuptools-git-versioning.svg)](https://badge.fury.io/py/setuptools-git-versioning)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/setuptools-git-versioning)](https://badge.fury.io/py/setuptools-git-versioning)
[![Build Status](https://travis-ci.com/dolfinus/setuptools-git-versioning.svg?branch=master)](https://travis-ci.com/dolfinus/setuptools-git-versioning)

Automatically set package version using git tag/hash

## Compairing with other packages

| Package/Function                                                                                    | Lastest release | Python2 support | Python3 support | PEP 440 compatible | Separated template for not tagged HEAD | Separated template for dirty run | Using functions outside setup.py | Returning fixed version if no tags | Returning callback if no tags | Reading VERSION file if no tags |
|:----------------------------------------------------------------------------------------------------|----------------:|:---------------:|:---------------:|:------------------:|:--------------------------------------:|:--------------------------------:|:--------------------------------:|:----------------------------------:|:-----------------------------:|:-------------------------------:|
| [setuptools-git-versioning](https://github.com/dolfinus/setuptools-git-versioning)                  |            2020 |        +        |        +        |         +          |                   +                    |                +                 |                +                 |                 +                  |                +              |                +                |
| [setuptools-git-ver](https://github.com/camas/setuptools-git-ver) (Base package)                    |            2020 |        -        |        +        |         +          |                   +                    |                +                 |                -                 |                 -                  |                -              |                -                |
| [even-better-setuptools-git-version](https://github.com/ktemkin/even-better-setuptools-git-version) |            2019 |        -        |        +        |         +          |                   -                    |                -                 |                +                 |                 +                  |                -              |                -                |
| [better-setuptools-git-version](https://github.com/vivin/better-setuptools-git-version)             |            2018 |        -        |        +        |         +          |                   -                    |                -                 |                +                 |                 +                  |                -              |                -                |
| [very-good-setuptools-git-version](https://github.com/Kautenja/very-good-setuptools-git-version)    |            2018 |        -        |        +        |         -          |                   -                    |                -                 |                +                 |                 -                  |                -              |                -                |
| [setuptools-git-version](https://github.com/pyfidelity/setuptools-git-version)                      |            2018 |        +        |        +        |         -          |                   -                    |                -                 |                -                 |                 -                  |                -              |                -                |

## Installation

No need.

Adding `setup_requires=['setuptools-git-versioning']` somewhere in `setup.py` will automatically download the latest version from PyPi and save it in the `.eggs` folder when `setup.py` is run.

## Usage

To just use the default templates for versioning:

```python
setuptools.setup(
    ...
    version_config=True,
    ...
    setup_requires=['setuptools-git-versioning'],
    ...
)
```

Changing templates (also shows the defaults):

```python
setuptools.setup(
    ...
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+git.{sha}"
        "dirty_template": "{tag}.dev{ccount}+git.{sha}.dirty",
        "starting_version": "0.0.1",
        "version_callback": None,
        "version_file": None,
    },
    ...
    setup_requires=['setuptools-git-versioning'],
    ...
)
```

### Templates

- `template`: used if no untracked files and latest commit is tagged

- `dev_template`: used if no untracked files and latest commit isn't tagged

- `dirty_template`: used if untracked files exist or uncommitted changes have been made

- `starting_version`: static value, used if not tags exist in repo

- `version_callback`: variable or callback function to get version instead of using `starting_version`

- `version_file`: path to VERSION file, to read version from it instead of using `static_version`

### Format Options

- `{tag}`: Latest tag in the repository

- `{ccount}`: Number of commits since last tag

- `{sha}`: First 8 characters of the sha hash of the latest commit

- `{branch}`: Current branch name
