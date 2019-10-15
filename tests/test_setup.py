import pytest
from badoo.setup import Credentials, Setup, _Browser, _Badoo
from badoo.yaml import YamlFromPath

_user: str = "user"
_pass: str = "pass"


@pytest.fixture(scope="module")
def credentials() -> Credentials:
    return Credentials(username=_user, password=_pass)


@pytest.fixture(scope="module")
def setup(data_path: str) -> Setup:
    return Setup(YamlFromPath(data_path))


@pytest.fixture(scope="module")
def browser(data_path: str) -> _Browser:
    return _Browser(YamlFromPath(data_path).section("setup")["browser"])


@pytest.fixture(scope="module")
def badoo(data_path: str) -> _Badoo:
    return _Badoo(YamlFromPath(data_path).section("setup")["badoo"])


def test_credentials_user(credentials: Credentials) -> None:
    assert credentials.username == _user


def test_credentials_pass(credentials: Credentials) -> None:
    assert credentials.password == _pass


def test_setup_browser(setup: Setup) -> None:
    assert isinstance(setup.browser(), _Browser)


def test_setup_badoo(setup: Setup) -> None:
    assert isinstance(setup.badoo(), _Badoo)


def test_browser_grid(browser: _Browser) -> None:
    assert browser.grid_url() == "test-grid"


def test_browser_proxy(browser: _Browser) -> None:
    assert browser.proxy() == "1.1.1.1:1234"


def test_badoo_username(badoo: _Badoo) -> None:
    assert badoo.credentials().username == "test-user"


def test_badoo_password(badoo: _Badoo) -> None:
    assert badoo.credentials().password == "test-pass"


def test_badoo_likes(badoo: _Badoo) -> None:
    assert badoo.likes() == 5


def test_badoo_intro_message(badoo: _Badoo) -> None:
    assert badoo.intro_message() == "test-message"
