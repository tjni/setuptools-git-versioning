from datetime import datetime, timedelta
import pytest
import time

from tests.conftest import execute, create_file, get_commit, get_version, get_short_commit


@pytest.mark.parametrize(
    "template, subst",
    [
        (None, "1.0.0"),
        ("{tag}.post{ccount}+git.{full_sha}", "1.0.0.post0+git.{full_sha}"),
        ("{tag}.post{ccount}+git.{sha}", "1.0.0.post0+git.{sha}"),
        ("{tag}.post{ccount}", "1.0.0.post0"),
        ("{tag}", "1.0.0"),
    ],
)
def test_tag(repo, create_config, template, subst):
    if template:
        create_config(repo, {"template": template})
    else:
        create_config(repo)

    execute(repo, "git tag 1.0.0")

    full_sha = get_commit(repo)
    sha = get_short_commit(repo)
    assert get_version(repo) == subst.format(sha=sha, full_sha=full_sha)


@pytest.mark.parametrize(
    "template, subst",
    [
        (None, "1.0.0.post1+git.{sha}"),
        ("{tag}.post{ccount}+git.{full_sha}", "1.0.0.post1+git.{full_sha}"),
        ("{tag}.post{ccount}+git.{sha}", "1.0.0.post1+git.{sha}"),
        ("{tag}.post{ccount}", "1.0.0.post1"),
        ("{tag}", "1.0.0"),
    ],
)
def test_tag_dev(repo, create_config, template, subst):
    if template:
        create_config(repo, {"dev_template": template})
    else:
        create_config(repo)

    execute(repo, "git tag 1.0.0")
    create_file(repo)

    full_sha = get_commit(repo)
    sha = get_short_commit(repo)
    assert get_version(repo) == subst.format(sha=sha, full_sha=full_sha)


@pytest.mark.parametrize(
    "template, subst",
    [
        (None, "1.0.0.post0+git.{sha}.dirty"),
        ("{tag}.post{ccount}+git.{full_sha}.dirty", "1.0.0.post0+git.{full_sha}.dirty"),
        ("{tag}.post{ccount}+git.{sha}.dirty", "1.0.0.post0+git.{sha}.dirty"),
        ("{tag}.post{ccount}+dirty", "1.0.0.post0+dirty"),
        ("{tag}+dirty", "1.0.0+dirty"),
    ],
)
@pytest.mark.parametrize("add", [True, False])
def test_tag_dirty(repo, create_config, add, template, subst):
    if template:
        create_config(repo, {"dirty_template": template})
    else:
        create_config(repo)

    execute(repo, "git tag 1.0.0")
    create_file(repo, add=add, commit=False)

    full_sha = get_commit(repo)
    sha = get_short_commit(repo)
    assert get_version(repo) == subst.format(sha=sha, full_sha=full_sha)


@pytest.mark.parametrize("starting_version, version", [(None, "0.0.1"), ("1.2.3", "1.2.3")])
def test_tag_no_tag(repo, create_config, starting_version, version):
    if starting_version:
        create_config(repo, {"starting_version": starting_version})
    else:
        create_config(repo)

    assert get_version(repo) == version


@pytest.mark.parametrize(
    "tag, version",
    [
        ("1.0.0", "1.0.0"),
        ("v1.2.3", "1.2.3"),
    ],
)
def test_tag_drop_leading_v(repo, create_config, tag, version):
    create_config(repo)

    execute(repo, "git tag {tag}".format(tag=tag))
    assert get_version(repo) == version


def test_tag_missing(repo, create_config):
    create_config(repo)
    assert get_version(repo) == "0.0.1"


def test_tag_not_a_repo(repo_dir, create_config):
    create_config(repo_dir, add=False, commit=False)

    assert get_version(repo_dir) == "0.0.1"


def test_tag_non_linear_history(repo, create_config):
    execute(repo, "git checkout -b dev")
    create_file(repo, commit=False)
    create_config(repo)

    execute(repo, "git checkout master")
    create_file(repo, commit=False)
    create_config(repo)
    execute(repo, "git tag 1.0.0")

    execute(repo, "git checkout dev")
    create_file(repo)
    assert get_version(repo) == "0.0.1"


def test_tag_linear_history(repo, create_config):
    execute(repo, "git tag 1.0.0")
    execute(repo, "git checkout -b dev")
    create_config(repo)

    sha = get_short_commit(repo)
    assert get_version(repo) == "1.0.0.post1+git.{sha}".format(sha=sha)


@pytest.mark.parametrize(
    "starting_version",
    [
        "1.0.0",
        "1.2.3",
    ],
)
def test_tag_missing_with_starting_version(repo, create_config, starting_version):
    create_config(repo, {"starting_version": starting_version})

    assert get_version(repo) == starting_version


@pytest.mark.parametrize("tag_opts", ["", "-a -m 'Some message'"])
def test_tag_sort_by_version(repo, create_config, tag_opts):
    sort_by = "version:refname"
    create_config(repo, {"sort_by": sort_by})

    commits = {}

    tags_to_commit = [
        "1.1.0",
        "1.1.10",
        "1.1.1",
    ]

    for i, tag in enumerate(tags_to_commit):
        create_file(repo, commit=False)
        dt = datetime.now() - timedelta(days=len(tags_to_commit) - i)
        execute(repo, "git commit -m 'Some commit' --date {dt}".format(dt=dt.isoformat()))
        commits[tag] = get_short_commit(repo)

    tags_to_create = [
        "1.1.0",
        "1.1.10",
        "1.1.1",
    ]

    for tag in tags_to_create:
        execute(repo, "git tag {tag_opts} {tag} {commit}".format(tag=tag, tag_opts=tag_opts, commit=commits[tag]))

    # the result is not stable because latest tag (by name)
    # has nothing in common with commit creation time
    # so it could mess everything up: https://github.com/dolfinus/setuptools-git-versioning/issues/22
    # that's why this value is not default
    assert "1.1.10" in get_version(repo)


@pytest.mark.parametrize("tag_opts", ["", "-a -m 'Some message'"])
def test_tag_sort_by_commit_date(repo, create_config, tag_opts):
    sort_by = "committerdate"
    create_config(repo, {"sort_by": sort_by})

    commits = {}
    tags_to_commit = [
        "1.1.10",
        "1.1.0",
        "1.1.1",
    ]

    for i, tag in enumerate(tags_to_commit):
        create_file(repo, commit=False)
        dt = datetime.now() - timedelta(days=len(tags_to_commit) - i)
        execute(repo, "git commit -m 'Some commit' --date {dt}".format(dt=dt.isoformat()))
        commits[tag] = get_short_commit(repo)
        time.sleep(1)

    tags_to_create = [
        "1.1.0",
        "1.1.1",
        "1.1.10",
    ]

    for tag in tags_to_create:
        execute(repo, "git tag {tag_opts} {tag} {commit}".format(tag=tag, tag_opts=tag_opts, commit=commits[tag]))

    if not tag_opts:
        assert get_version(repo) == "1.1.1"
    else:
        assert get_version(repo).startswith("1.1")
        # the result is totally random because annotaged tags have no such field at all
        # https://github.com/dolfinus/setuptools-git-versioning/issues/23


@pytest.mark.parametrize("tag_opts", ["", "-a -m 'Some message'"])
def test_tag_sort_by_tag_date(repo, create_config, tag_opts):
    sort_by = "taggerdate"
    create_config(repo, {"sort_by": sort_by})

    commits = {}
    tags_to_commit = [
        "1.1.10",
        "1.1.0",
        "1.1.1",
    ]

    for i, tag in enumerate(tags_to_commit):
        create_file(repo, commit=False)
        dt = datetime.now() - timedelta(days=len(tags_to_commit) - i)
        execute(repo, "git commit -m 'Some commit' --date {dt}".format(dt=dt.isoformat()))
        commits[tag] = get_short_commit(repo)

    tags_to_create = [
        "1.1.0",
        "1.1.1",
        "1.1.10",
    ]

    for tag in tags_to_create:
        execute(repo, "git tag {tag_opts} {tag} {commit}".format(tag=tag, tag_opts=tag_opts, commit=commits[tag]))
        time.sleep(1)

    if tag_opts:
        # the result is not stable because latest tag (by creation time)
        # has nothing in common with commit creation time
        assert "1.1.10" in get_version(repo)
    else:
        assert get_version(repo).startswith("1.1")
        # the result is totally random because annotaged tags have no such field at all
        # https://github.com/dolfinus/setuptools-git-versioning/issues/23


@pytest.mark.parametrize("sort_by", [None, "creatordate"])
@pytest.mark.parametrize("tag_opts", ["", "-a -m 'Some message'"])
def test_tag_sort_by_create_date(repo, create_config, tag_opts, sort_by):
    if sort_by:
        create_config(repo, {"sort_by": sort_by})
    else:
        create_config(repo)

    commits = {}
    tags_to_commit = [
        "1.1.0",
        "1.1.10",
        "1.1.1",
    ]

    for i, tag in enumerate(tags_to_commit):
        create_file(repo, commit=False)
        dt = datetime.now() - timedelta(days=len(tags_to_commit) - i)
        execute(repo, "git commit -m 'Some commit' --date {dt}".format(dt=dt.isoformat()))
        commits[tag] = get_short_commit(repo)
        time.sleep(1)

    tags_to_create = [
        "1.1.10",
        "1.1.1",
        "1.1.0",
    ]

    for tag in tags_to_create:
        execute(repo, "git tag {tag_opts} {tag} {commit}".format(tag=tag, tag_opts=tag_opts, commit=commits[tag]))
        time.sleep(1)

    if tag_opts:
        # the result is not stable because latest tag (by creation time)
        # has nothing in common with commit creation time
        # so it is not recommended to create annotated tags in the past
        assert "1.1.0" in get_version(repo)
    else:
        # but at least creatordate field is present in both tag types
        # https://stackoverflow.com/questions/67206124
        # so this is a default value
        assert get_version(repo) == "1.1.1"
