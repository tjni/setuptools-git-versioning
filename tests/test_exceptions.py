import pytest
import subprocess

from tests.conftest import get_version


def test_exceptions_wrong_config_format(repo, create_config):
    create_config(repo, [("A", "B")], add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_exceptions_version_config_false(repo, create_config):
    create_config(repo, False, add=False, commit=False)

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)
