import os
import shutil
import textwrap
from pathlib import Path

import pytest

from tests.lib.util import create_file, execute

root = Path(__file__).parent.parent


@pytest.fixture
def repo_dir(tmp_path_factory: pytest.TempPathFactory):
    repo_dir = tmp_path_factory.mktemp("repo")
    coveragerc = root.joinpath(".coveragerc")
    reports = repo_dir.joinpath("reports")

    # collect coverage data
    shutil.copy(coveragerc, repo_dir)

    reports.mkdir(parents=True, exist_ok=True)

    yield repo_dir

    if os.environ.get("CI", "false").lower() in ["1", "true"]:
        # move collect coverage data to reports directory
        for file in reports.iterdir():
            file.rename(reports / file.name)


@pytest.fixture
def repo(repo_dir):
    execute(repo_dir, "git", "init", "-b", "master")
    execute(repo_dir, "git", "config", "--local", "user.email", "tests@example.com")
    execute(repo_dir, "git", "config", "--local", "user.name", "Tests runner")
    execute(repo_dir, "git", "add", ".coveragerc")
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
