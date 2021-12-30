import configparser
from functools import partial
import logging
import io
import os
import pytest
import shutil
import subprocess
import sys
import textwrap
import toml
import uuid

from typing import Any, Optional

try:
    from shlex import quote as cmd_quote
except ImportError:
    from pipes import quote as cmd_quote

log = logging.getLogger(__name__)
root = os.path.dirname(os.path.dirname(__file__))


def rand_str():  # type: () -> str
    return str(uuid.uuid4())


def execute(cwd, cmd, **kwargs):  # type: (str, str, **Any) -> str
    log.info(cwd)
    return subprocess.check_output(cmd, cwd=cwd, shell=True, universal_newlines=True, **kwargs)  # nosec


def create_file(
    cwd, name=None, content=None, add=True, commit=True
):  # type: (str, Optional[str], Optional[str], bool, bool) -> Optional[str]
    result = None

    if not name:
        name = rand_str()
    if content is None:
        content = rand_str()
    with open(os.path.join(cwd, name), "w") as f:
        f.write(content)

    if add:
        execute(cwd, "git add {name}".format(name=cmd_quote(name)))
        log.info(execute(cwd, "git status"))
        log.info(execute(cwd, "git diff"))

        if commit:
            msg = "Add {}".format(name)
            execute(cwd, "git commit -m {msg}".format(msg=cmd_quote(msg)))
            result = get_short_commit(cwd)

    return result


def create_pyproject_toml(
    cwd,  # type: str
    config=None,  # type: Optional[dict]
    commit=True,  # type: bool
    **kwargs  # type: Any
):  # type: (...) -> Optional[str]
    conf = configparser.ConfigParser()

    conf["metadata"] = {
        "name": "mypkg",
    }

    fd = io.StringIO()
    conf.write(fd)
    setup_cfg = fd.getvalue()
    fd.close()

    create_file(cwd, "setup.cfg", setup_cfg, commit=False, **kwargs)

    cfg = {
        "build-system": {
            "requires": [
                "setuptools>=45",
                "setuptools-localimport",
                "wheel",
                "setuptools-git-versioning",
            ],
            # with default "setuptools.build_meta" it is not possible to build package
            # which uses its own source code to get version number,
            # e.g. `version_callback` or `branch_formatter`
            # mote details: https://github.com/pypa/setuptools/issues/1642#issuecomment-457673563
            "build-backend": "setuptools_localimport",
        },
        "tool": {"setuptools-git-versioning": (config if config is not None else {})},
    }

    log.warning(toml.dumps(cfg))

    return create_file(cwd, "pyproject.toml", toml.dumps(cfg), commit=commit, **kwargs)


def create_setup_py(
    cwd,  # type: str
    config=None,  # type: Optional[dict]
    **kwargs  # type: Any
):  # type: (...) -> Optional[str]
    return create_file(
        cwd,
        "setup.py",
        textwrap.dedent(
            """
            import setuptools

            setuptools.setup(
                name="mypkg",
                version_config={config},
                packages=setuptools.find_packages(),
                setup_requires=[
                    "setuptools>=45",
                    "wheel",
                    "setuptools-git-versioning",
                ]
            )
        """
        ).format(config=config if config is not None else True),
        **kwargs
    )


@pytest.fixture(params=[create_setup_py, create_pyproject_toml])
def create_config(request):
    return request.param


def typed_config(repo, config_creator, config_type, template=None, config=None):
    if config_type == "tag":
        cfg = {}
    else:
        cfg = {"version_file": "VERSION.txt", "count_commits_from_version_file": True}

    if config_type == "tag":
        template_name = "template"
    else:
        template_name = "dev_template"

    if template:
        cfg[template_name] = template

    if config:
        cfg.update(config)

    config_creator(repo, cfg)

    if config_type == "tag":
        execute(repo, "git tag 1.2.3")
    else:
        create_file(repo, "VERSION.txt", "1.2.3")


@pytest.fixture(params=["tag", "version_file"])
def template_config(request):
    return partial(typed_config, config_type=request.param)


def get_version(cwd, **kwargs):  # type: (str, **Any) -> str
    execute(cwd, "{python} -m build --no-isolation".format(python=sys.executable), **kwargs)
    with open(os.path.join(cwd, "mypkg.egg-info/PKG-INFO")) as f:
        content = f.read().splitlines()

    for line in content:
        if line.startswith("Version: "):
            return line.replace("Version: ", "").strip()

    raise RuntimeError("Cannot get package version")


def get_version_setup_py(cwd, **kwargs):  # type: (str, **Any) -> str
    return execute(cwd, "{python} setup.py --version".format(python=sys.executable), **kwargs).strip()


def get_commit(cwd, **kwargs):  # type: (str, **Any) -> str
    return execute(cwd, "git rev-list -n 1 HEAD", **kwargs).strip()


def get_short_commit(cwd, **kwargs):  # type: (str, *Any) -> str
    return get_commit(cwd, **kwargs)[:8]


@pytest.fixture
def repo_dir(tmpdir):
    repo_dir = str(tmpdir.mkdir(rand_str()))
    # collect coverage data
    with open(os.path.join(root, ".coveragerc")) as f:
        create_file(repo_dir, ".coveragerc", f.read(), add=False, commit=False)
    os.mkdir(os.path.join(repo_dir, "reports"))

    yield repo_dir

    # move collect coverage data to reports directory
    for root_path, _dirs, files in os.walk(os.path.join(repo_dir, "reports")):
        for file in files:
            shutil.move(os.path.join(root_path, file), os.path.join(root, "reports", file))


@pytest.fixture
def repo(repo_dir):
    execute(repo_dir, "git init -b master")
    execute(repo_dir, "git config --local user.email 'tests@example.com'")
    execute(repo_dir, "git config --local user.name 'Tests runner'")
    execute(repo_dir, "git add .coveragerc")
    create_file(
        repo_dir,
        ".gitignore",
        textwrap.dedent(
            """
        .eggs
        *.egg
        *.egg-info/
        build
        dist
        *.py[oc]
        reports/
    """
        ),
    )
    create_file(repo_dir, "__init__.py", "")

    return repo_dir
