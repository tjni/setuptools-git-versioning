import pytest
import subprocess

from tests.lib.util import get_version_script, get_version_module, create_pyproject_toml, create_setup_py


def test_command_pyproject_toml(repo):
    create_pyproject_toml(repo)

    assert get_version_module(repo) == "0.0.1"
    assert get_version_script(repo) == "0.0.1"


def test_command_pyproject_toml_disabled(repo):
    create_pyproject_toml(repo, {"enabled": False})

    with pytest.raises(subprocess.CalledProcessError):
        get_version_module(repo)

    with pytest.raises(subprocess.CalledProcessError):
        get_version_script(repo)


def test_command_setup_py_fail(repo):
    create_setup_py(repo)

    with pytest.raises(subprocess.CalledProcessError):
        get_version_module(repo)

    with pytest.raises(subprocess.CalledProcessError):
        get_version_script(repo)
