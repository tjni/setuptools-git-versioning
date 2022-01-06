import pytest
import subprocess
import textwrap

from tests.conftest import execute, create_file, get_version

pytestmark = pytest.mark.all


@pytest.mark.parametrize(
    "tag, version",
    [
        ("1.0.0", "1.0.0"),
        ("release/1.0.0", "1.0.0"),
        ("unknown", "0.0.0"),
    ],
)
def test_tag_formatter_external(repo, create_config, tag, version):
    create_file(
        repo,
        "util.py",
        textwrap.dedent(
            r"""
            import re

            def tag_formatter(tag):
                return re.sub(r"[^\d.]+", "", tag)
            """
        ),
    )

    create_config(
        repo,
        {
            "tag_formatter": "util:tag_formatter",
        },
    )
    execute(repo, "git tag {tag}".format(tag=tag))

    assert get_version(repo) == version


@pytest.mark.parametrize("create_util", [True, False])
def test_tag_formatter_external_missing(repo, create_config, create_util):
    if create_util:
        create_file(
            repo,
            "util.py",
            textwrap.dedent(
                r"""
                import re

                def tag_formatter(tag):
                    return re.sub(r"[^\d.]+", "", tag)
                """
            ),
        )

    create_config(
        repo,
        {
            "tag_formatter": "util:wtf",
        },
    )
    execute(repo, "git tag 1.0.0")

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_tag_formatter_external_not_callable(repo, create_config):
    create_file(
        repo,
        "util.py",
        textwrap.dedent(
            r"""
            import re

            tag_formatter = re.compile(r"[^\d.]+")
            """
        ),
    )

    create_config(
        repo,
        {
            "tag_formatter": "util:tag_formatter",
        },
    )
    execute(repo, "git tag 1.0.0")

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_tag_formatter_external_setup_py_direct_import(repo):
    create_file(
        repo,
        "setup.py",
        textwrap.dedent(
            r"""
            from coverage.control import Coverage

            coverage = Coverage()
            coverage.start()

            try:
                import re
                import setuptools

                def tag_formatter(tag):
                    return re.sub(r"[^\d.]+", "", tag)

                setuptools.setup(
                    name="mypkg",
                    setuptools_git_versioning={
                        "tag_formatter": tag_formatter
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
        ),
    )

    execute(repo, "git tag release/1.0.0")

    assert get_version(repo) == "1.0.0"


@pytest.mark.parametrize(
    "tag, version",
    [
        ("1.0.0", "1.0.0"),
        ("release/1.0.0", "1.0.0"),
    ],
)
def test_tag_formatter_regexp(repo, create_config, tag, version):
    create_config(
        repo,
        {
            "tag_formatter": r".*?(?P<tag>[\d.]+).*",
        },
    )
    execute(repo, "git tag {tag}".format(tag=tag))

    assert get_version(repo) == version


def test_tag_formatter_regexp_not_match(repo, create_config):
    create_config(
        repo,
        {
            "tag_formatter": r".*?(?P<tag>[\d.]+).*",
        },
    )

    execute(repo, "git tag unknown")

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


@pytest.mark.parametrize("regexp", [r".*?([\d.]+).*", r".*?(?P<unknown>[\d.]+).*"])
def test_tag_formatter_regexp_no_capture_group(repo, create_config, regexp):
    create_config(
        repo,
        {
            "tag_formatter": regexp,
        },
    )

    execute(repo, "git tag 1.0.0")

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_tag_formatter_regexp_wrong_format(repo, create_config):
    create_config(
        repo,
        {
            "tag_formatter": "(",
        },
    )

    execute(repo, "git tag 1.0.0")

    with pytest.raises(subprocess.CalledProcessError):
        get_version(repo)


def test_tag_formatter_no_tag(repo, create_config):
    create_config(
        repo,
        {
            "tag_formatter": "(",
        },
    )

    assert get_version(repo) == "0.0.1"


@pytest.mark.parametrize(
    "count_commits",
    [True, False],
)
def test_tag_formatter_ignored_if_version_file_set(repo, create_config, count_commits):
    create_config(
        repo,
        {
            "version_file": "VERSION.txt",
            "count_commits_from_version_file": count_commits,
            "dev_template": "{tag}",
            "tag_formatter": "(",
        },
    )
    create_file(repo, "VERSION.txt", "1.0.0")

    assert get_version(repo) == "1.0.0"


@pytest.mark.parametrize(
    "version_callback",
    ["version:get_version", "version:__version__"],
)
def test_tag_formatter_ignored_if_version_callback_set(repo, create_config, version_callback):
    create_file(
        repo,
        "version.py",
        textwrap.dedent(
            """
            def get_version():
                return "1.0.0"

            __version__ = "1.0.0"
            """
        ),
    )
    create_config(
        repo,
        {
            "version_callback": version_callback,
            "tag_formatter": "(",
        },
    )

    assert get_version(repo) == "1.0.0"
