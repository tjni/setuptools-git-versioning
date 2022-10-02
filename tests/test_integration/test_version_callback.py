import os
import subprocess
import pytest

from tests.lib.util import (
    create_file,
    get_version,
    get_version_setup_py,
    create_tag,
    get_version_script,
    get_version_module,
)

pytestmark = pytest.mark.all


VERSION_PY = """def get_version():
    return "{version}"

__version__ = "{version}"
"""


SETUP_PY_CALLABLE = """from coverage.control import Coverage

coverage = Coverage()
coverage.start()

try:
    import setuptools
    from version import get_version

    setuptools.setup(
        version_config={
            "version_callback": get_version
        },
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


SETUP_PY_STR = """from coverage.control import Coverage

coverage = Coverage()
coverage.start()

try:
    import setuptools

    from version import __version__

    setuptools.setup(
        version_config={
            "version_callback": __version__
        },
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


@pytest.mark.parametrize(
    "version_callback",
    [
        "version:get_version",
        "version:__version__",
    ],
    ids=["callable", "str"],
)
def test_version_callback(repo, version_callback, create_config):
    create_file(repo, "version.py", VERSION_PY.format(version="1.0.0"), commit=False)

    create_config(repo, {"version_callback": version_callback})

    assert get_version(repo) == "1.0.0"
    assert get_version_script(repo) == "1.0.0"
    assert get_version_module(repo) == "1.0.0"

    # path to the repo can be passed as positional argument
    assert get_version_script(os.getcwd(), args=[repo]) == "1.0.0"
    assert get_version_module(os.getcwd(), args=[repo]) == "1.0.0"

    # git status does not influence callback result
    create_file(repo)
    assert get_version(repo) == "1.0.0"

    create_file(repo)
    assert get_version(repo) == "1.0.0"


@pytest.mark.parametrize(
    "setup_py",
    [
        SETUP_PY_CALLABLE,
        SETUP_PY_STR,
    ],
    ids=["callable", "str"],
)
def test_version_callback_setup_py_direct_import(repo, setup_py):
    create_file(repo, "version.py", VERSION_PY.format(version="1.0.0"), commit=False)
    create_file(
        repo,
        "setup.py",
        setup_py,
    )

    assert get_version_setup_py(repo) == "1.0.0"
    assert get_version_script(repo) == "1.0.0"
    assert get_version_module(repo) == "1.0.0"

    # path to the repo can be passed as positional argument
    assert get_version_script(os.getcwd(), args=[repo]) == "1.0.0"
    assert get_version_module(os.getcwd(), args=[repo]) == "1.0.0"

    # git status does not influence callback result
    create_file(repo)
    assert get_version_setup_py(repo) == "1.0.0"

    create_file(repo)
    assert get_version_setup_py(repo) == "1.0.0"


@pytest.mark.parametrize("create_version_py", [True, False])
def test_version_callback_missing(repo, create_version_py, create_config):
    version_callback = "version:wtf"

    if create_version_py:
        create_file(repo, "version.py", "", commit=False)

    create_config(repo, {"version_callback": version_callback})

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.parametrize(
    "version, real_version",
    [
        ("1.0.0", "1.0.0"),
        ("v1.2.3", "1.2.3"),
    ],
)
def test_version_callback_drop_leading_v(repo, version, real_version, create_config):
    create_file(repo, "version.py", VERSION_PY.format(version=version), commit=False)
    create_config(repo, {"version_callback": "version:get_version"})
    assert get_version(repo) == real_version


def test_version_callback_wrong_version_number(repo, create_config):
    create_file(repo, "version.py", VERSION_PY.format(version="alpha1.2.3"), commit=False)
    create_config(repo, {"version_callback": "version:get_version"})

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_version_callback_not_a_repo(repo_dir, create_config):
    version = "1.0.0"
    create_file(repo_dir, "version.py", VERSION_PY.format(version=version), add=False, commit=False)
    create_config(
        repo_dir,
        {"version_callback": "version:get_version"},
        add=False,
        commit=False,
    )

    assert get_version(repo_dir) == version
    assert get_version_script(repo_dir) == version
    assert get_version_module(repo_dir) == version

    # path to the repo can be passed as positional argument
    assert get_version_script(os.getcwd(), args=[repo_dir]) == version
    assert get_version_module(os.getcwd(), args=[repo_dir]) == version


def test_version_callback_has_more_priority_than_tag(repo, create_config):
    version = "1.0.0"

    create_file(repo, "version.py", VERSION_PY.format(version=version), commit=False)
    create_config(repo, {"version_callback": "version:get_version"})

    create_tag(repo, "1.2.3")
    assert get_version(repo) == version


def test_version_callback_conflicts_with_version_file(repo, create_config):
    create_config(
        repo,
        {
            "version_file": "VERSION.txt",
            "version_callback": "version:get_version",
        },
    )

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.flaky(reruns=3)  # sha and full_sha can start with 0 which are removed, just try again
@pytest.mark.parametrize(
    "version_callback",
    [
        "version:get_version",
        "version:__version__",
    ],
    ids=["callable", "str"],
)
@pytest.mark.parametrize(
    "template",
    [
        "{tag}.post{env:PIPELINE_ID:123}",
        "{tag}.post{env:PIPELINE_ID:123}",
        "{tag}.post{env:PIPELINE_ID:IGNORE}",
        "{tag}.post{env:PIPELINE_ID:IGNORE}",
        "{tag}.post{env:PIPELINE_ID:{ccount}}",
        "{tag}.post{env:PIPELINE_ID:{ccount}}",
        "{tag}.post{timestamp}",
        "{tag}.post{timestamp:%s}",
        "{timestamp:%Y}.{timestamp:%m}.{timestamp:%d}+{timestamp:%H%M%S}",
        "{tag}.post{ccount}+{timestamp:%Y-%m-%dT%H-%M-%S}",
        "{tag}.post{ccount}+git.{full_sha}",
        "{tag}.post{ccount}+git.{sha}",
        "{tag}.post{ccount}",
        "{tag}.{branch}{ccount}",
        "{tag}",
    ],
)
def test_version_callback_template_substitutions_are_ignored(
    repo,
    template,
    version_callback,
    create_config,
):
    version = "1.0.0"

    create_file(
        repo,
        "version.py",
        VERSION_PY.format(version=version),
        commit=False,
    )
    create_config(repo, {"version_callback": version_callback, "dev_template": template})

    assert get_version(repo) == version
