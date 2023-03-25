from functools import partial

import pytest

from tests.lib.util import create_pyproject_toml, create_setup_py, typed_config


@pytest.fixture(params=[create_setup_py, create_pyproject_toml])
def create_config(request):
    return request.param


@pytest.fixture(params=["tag", "version_file"])
def template_config(request):
    return partial(typed_config, config_type=request.param)
