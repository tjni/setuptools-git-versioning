import pytest
import subprocess

from tests.conftest import get_version, create_pyproject_toml, create_setup_py


def test_version_config_true_setup_py(repo, create_config):
    create_config(repo, True, add=False, commit=False)

    assert get_version(repo) == "0.0.1"


def test_version_config_not_set(repo, create_config):
    create_config(repo, NotImplemented, add=False, commit=False)

    assert get_version(repo) == "0.0.1"


def test_version_config_false(repo, create_config):
    create_config(repo, False, add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_version_config_wrong_format(repo, create_config):
    create_config(repo, [("A", "B")], add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_version_config_setup_py_has_more_priority_than_pyproject_toml(repo):
    create_pyproject_toml(repo, {"starting_version": "2.3.4"}, add=False, commit=False)
    create_setup_py(repo, {"starting_version": "1.2.3"}, add=False, commit=False)

    assert get_version(repo) == "1.2.3"


def test_version_config_pyproject_toml_is_used_then_setup_py_is_empty(repo):
    create_pyproject_toml(repo, {"starting_version": "2.3.4"}, add=False, commit=False)
    create_setup_py(repo, NotImplemented, add=False, commit=False)

    assert get_version(repo) == "2.3.4"
