import itertools
import pytest
import subprocess
import textwrap
import toml

from tests.conftest import get_version, get_version_setup_py, create_file, create_pyproject_toml, create_setup_py


def test_config_not_set(repo, create_config):
    create_config(repo, NotImplemented)

    assert get_version(repo) == "0.0.0"


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_not_used(repo, option):
    create_file(
        repo,
        "setup.py",
        textwrap.dedent(
            """
            from coverage.control import Coverage

            coverage = Coverage()
            coverage.start()

            try:
                import setuptools

                setuptools.setup(
                    name="mypkg",
                    {option}=None,
                )
            finally:
                coverage.stop()
                coverage.save()
            """
        ).format(option=option),
    )

    cfg = {
        "build-system": {
            "requires": [
                "setuptools>=41",
                "wheel",
                "coverage",
            ],
            "build-backend": "setuptools.build_meta",
        }
    }

    create_file(
        repo,
        "pyproject.toml",
        toml.dumps(cfg),
    )

    assert get_version_setup_py(repo) == "0.0.0"
    assert get_version(repo, isolated=False) == "0.0.0"
    assert get_version(repo, isolated=True) == "0.0.0"


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_enabled_false(repo, create_config, option):
    create_config(repo, {"enabled": False}, option=option)

    assert get_version(repo) == "0.0.0"


@pytest.mark.parametrize(
    "value",
    [True, False],
)
def test_config_bool_pyproject_toml(repo, value):
    create_pyproject_toml(repo, value)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_false_setup_py(repo, option):
    create_setup_py(repo, False, option=option)

    assert get_version_setup_py(repo) == "0.0.0"


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_true_setup_py(repo, option):
    create_setup_py(repo, False, option=option)

    assert get_version_setup_py(repo) == "0.0.0"


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_enabled_true(repo, create_config, option):
    create_config(repo, {"enabled": True}, option=option)

    assert get_version(repo) == "0.0.1"


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_wrong_format(repo, create_config, option):
    create_config(repo, [("A", "B")], option=option)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_both_setup_py_and_pyproject_toml(repo, option):
    create_pyproject_toml(repo)
    create_setup_py(repo, option=option)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.parametrize(
    "option",
    ["version_config", "setuptools_git_versioning"],
)
def test_config_pyproject_toml_is_used_then_setup_py_is_empty(repo, option):
    create_pyproject_toml(repo, {"starting_version": "2.3.4"}, add=False, commit=False)
    create_setup_py(repo, NotImplemented, option=option, add=False, commit=False)

    assert get_version(repo) == "2.3.4"


@pytest.mark.parametrize(
    "version_config, setuptools_git_versioning",
    itertools.combinations(
        [
            False,
            True,
            {"enabled": True},
            {"enabled": False},
            {"any": "abc"},
        ],
        2,
    ),
)
def test_config_both_old_and_new_config_are_set(repo, version_config, setuptools_git_versioning):
    create_file(
        repo,
        "setup.py",
        textwrap.dedent(
            """
            from coverage.control import Coverage

            coverage = Coverage()
            coverage.start()

            try:
                import setuptools

                setuptools.setup(
                    name="mypkg",
                    setuptools_git_versioning={setuptools_git_versioning},
                    version_config={version_config},
                    setup_requires=[
                        "setuptools>=41",
                        "wheel",
                        "setuptools-git-versioning",
                    ]
                )
            finally:
                coverage.stop()
                coverage.save()
            """
        ).format(version_config=version_config, setuptools_git_versioning=setuptools_git_versioning),
    )

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)
