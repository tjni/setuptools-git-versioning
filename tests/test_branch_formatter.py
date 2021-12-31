import textwrap
import pickle
import pytest
import subprocess

from tests.conftest import execute, create_file, get_version


@pytest.mark.parametrize(
    "branch, suffix",
    [
        ("1234", "1234"),
        ("feature/issue-1234-add-a-great-feature", "1234"),
    ],
)
@pytest.mark.parametrize(
    "branch_formatter",
    [
        "util:branch_formatter",
        r".*?([\d]+).*",
    ],
)
def test_branch_formatter(repo, template_config, create_config, branch_formatter, branch, suffix):
    execute(repo, "git checkout -b {branch}".format(branch=branch))

    create_file(
        repo,
        "util.py",
        textwrap.dedent(
            """
            import re

            def branch_formatter(branch):
                return re.sub("[^\\d]+", "", branch)
        """
        ),
    )

    template_config(
        repo,
        create_config,
        template="{tag}{branch}{ccount}",
        config={
            "branch_formatter": branch_formatter,
        },
    )

    assert get_version(repo) == "1.2.3{suffix}0".format(suffix=suffix)


@pytest.mark.parametrize("create_util", [True, False])
def test_branch_formatter_missing(repo, template_config, create_config, create_util):
    if create_util:
        create_file(
            repo,
            "util.py",
            textwrap.dedent(
                """
                import re

                def branch_formatter(branch):
                    return re.sub("[^\\d]+", "", branch)
            """
            ),
        )

    template_config(
        repo,
        create_config,
        config={
            "branch_formatter": "util:wtf",
        },
    )

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_branch_formatter_wrong_format(repo, template_config, create_config):
    template_config(
        repo,
        create_config,
        config={
            "branch_formatter": "util:wtf",
        },
    )

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_branch_formatter_not_callable(repo, template_config, create_config):
    create_file(
        repo,
        "util.py",
        textwrap.dedent(
            """
            import re

            branch_formatter = re.compile("[^\\d]+")
        """
        ),
    )

    template_config(
        repo,
        create_config,
        config={
            "branch_formatter": "util:branch_formatter",
        },
    )

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_branch_formatter_setup_py_direct_import(repo, template_config):
    branch = "feature/issue-1234-add-a-great-feature"
    suffix = ".1234"

    execute(repo, "git checkout -b {branch}".format(branch=branch))

    def config_creator(root, cfg):
        return create_file(
            repo,
            "setup.py",
            textwrap.dedent(
                """
                import re
                import setuptools
                import pickle

                def branch_formatter(branch):
                    return re.sub("[^\\d]+", "", branch)

                version_config = pickle.loads({cfg})
                version_config["branch_formatter"] = branch_formatter

                setuptools.setup(
                    name="mypkg",
                    version_config=version_config,
                    setup_requires=[
                        "setuptools>=41",
                        "wheel",
                        "setuptools-git-versioning",
                    ]
                )
            """.format(
                    cfg=pickle.dumps(cfg)
                )
            ),
        )

    template_config(repo, config_creator, template="{tag}.{branch}{ccount}")

    assert get_version(repo) == "1.2.3{suffix}0".format(suffix=suffix)
