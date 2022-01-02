import pytest
import subprocess

from tests.conftest import get_version, create_pyproject_toml, create_setup_py


def test_version_config_true_pyproject_toml(repo):
    create_pyproject_toml(repo, True, add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_version_config_true_setup_py(repo, create_config):
    create_setup_py(repo, True, add=False, commit=False)

    assert get_version(repo) == "0.0.1"


def test_version_config_false(repo, create_config):
    create_config(repo, False, add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_version_config_wrong_format(repo, create_config):
    create_config(repo, [("A", "B")], add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)
