import os
import pytest
import shutil
import textwrap

from tests.lib.util import rand_str, create_file, execute

root = os.path.dirname(os.path.dirname(__file__))


@pytest.fixture
def repo_dir(tmpdir):
    repo_dir = str(tmpdir.mkdir(rand_str()))
    # collect coverage data
    with open(os.path.join(root, ".coveragerc")) as f:
        create_file(repo_dir, ".coveragerc", f.read(), add=False, commit=False)
    os.mkdir(os.path.join(repo_dir, "reports"))

    yield repo_dir

    if os.environ.get("CI", "false").lower() in ["1", "true"]:
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
