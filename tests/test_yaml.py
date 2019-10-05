import pytest
from badoo.yaml import Yaml, YamlFromPath


@pytest.fixture(scope="module")
def yaml_from_path(data_path: str) -> Yaml:
    return YamlFromPath(data_path)


def test_yaml_from_path_data(yaml_from_path: Yaml) -> None:
    assert yaml_from_path.data == {
        "setup": {
            "badoo": {
                "credentials": {"password": "test-pass", "login": "test-user"},
                "intro-massage": "test-message",
            },
            "browser": {"grid-url": "test-grid"},
        }
    }


def test_yaml_from_path_section(yaml_from_path: Yaml) -> None:
    assert yaml_from_path.section("setup") == {
        "badoo": {
            "credentials": {"password": "test-pass", "login": "test-user"},
            "intro-massage": "test-message",
        },
        "browser": {"grid-url": "test-grid"},
    }
