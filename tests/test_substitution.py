from datetime import datetime
import pytest
import re

from tests.conftest import execute, get_version


@pytest.mark.parametrize(
    "branch, suffix",
    [
        ("alpha", "a"),
        ("beta", "b"),
        ("dev", ".dev"),
        ("pre", "rc"),
        ("preview", "rc"),
        ("post", ".post"),
    ],
)
def test_substitution_branch(repo, template_config, create_config, branch, suffix):
    execute(repo, "git checkout -b {branch}".format(branch=branch))
    template_config(repo, create_config, template="{tag}{branch}0")

    assert get_version(repo) == "1.2.3{suffix}0".format(suffix=suffix)


@pytest.mark.parametrize(
    "template, pipeline_id, suffix",
    [
        # leading zeros are removed by setuptools
        ("{tag}.post{env:PIPELINE_ID:123}", "0234", "234"),
        ("{tag}.post{env:PIPELINE_ID:123}", "234", "234"),
        ("{tag}.post{env:PIPELINE_ID:123}", None, "123"),
        ("{tag}.post{env:PIPELINE_ID:IGNORE}", "0234", "234"),
        ("{tag}.post{env:PIPELINE_ID:IGNORE}", "234", "234"),
        ("{tag}.post{env:PIPELINE_ID:IGNORE}", None, "0"),
        ("{tag}.post{env:PIPELINE_ID:{ccount}}", "0234", "234"),
        ("{tag}.post{env:PIPELINE_ID:{ccount}}", "234", "234"),
        ("{tag}.post{env:PIPELINE_ID:{ccount}}", None, "0"),
        ("{tag}.post{env:PIPELINE_ID}", "0234", "234"),
        ("{tag}.post{env:PIPELINE_ID}", "234", "234"),
        ("{tag}.post{env:PIPELINE_ID}", None, "UNKNOWN"),
    ],
)
def test_substitution_env(repo, template_config, create_config, template, pipeline_id, suffix):
    template_config(repo, create_config, template=template)

    env = {}
    if pipeline_id is not None:
        env = {"PIPELINE_ID": pipeline_id}

    assert get_version(repo, env=env) == "1.2.3.post{suffix}".format(suffix=suffix)


@pytest.mark.parametrize(
    "template, fmt, callback",
    [
        ("{tag}.post{timestamp}", "{tag}.post{}", lambda dt: (int(dt.strftime("%s")) // 100,)),
        ("{tag}.post{timestamp:%s}", "{tag}.post{}", lambda dt: (int(dt.strftime("%s")) // 100,)),
        (
            "{timestamp:%Y}.{timestamp:%m}.{timestamp:%d}+{timestamp:%H%M%S}",
            "{}.{}.{}+{}",
            lambda dt: (dt.year, dt.month, dt.day, dt.strftime("%H%M")),
        ),
        (
            "{tag}.post{ccount}+{timestamp:%Y-%m-%dT%H-%M-%S}",
            "{tag}.post{ccount}+{}",
            lambda dt: (dt.strftime("%Y.%m.%dt%H.%M"),),
        ),
    ],
)
def test_substitution_timestamp(repo, template_config, create_config, template, fmt, callback):
    template_config(repo, create_config, template=template)

    value = fmt.format(tag="1.2.3", ccount=0, *callback(datetime.now()))
    pattern = re.compile(r"([^\d\w])0+(\d+[^\d\w]|\d+$)")
    while True:
        # leading zeros are removed even in local part of version
        new_value = pattern.sub(r"\1\2", value)
        if new_value == value:
            break
        value = new_value
    assert new_value in get_version(repo)
