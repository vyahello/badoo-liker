"""The module contains basic abstractions which have to be used while designing page objects."""
import time
from abc import ABC, abstractmethod
from typing import Any, Callable
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from badoo.connections.web import Browser
from badoo.logger import Logger, MainLogger
from badoo.setup import Credentials
from badoo.web.support.element import Element
from badoo.web.support.wait import Wait

_logger: Logger = MainLogger(__name__)


class Url:
    """The class represents an URL to a page."""

    def __init__(self, host: str, path: str = "", protocol: str = "https") -> None:
        self._host = host
        self._path = path
        self._protocol = protocol

    def matcher(self) -> str:
        """Returns a path of the URL."""
        return self._path

    def host(self) -> str:
        """Returns a domain name (host)."""
        return self._host

    def __str__(self) -> str:
        return f"{self._protocol}://{self._host}/{self._path}"


class Page(ABC):
    """The base class for all objects which represents a WEB page."""

    @abstractmethod
    def open(self) -> None:
        """Opens the page."""
        pass

    @abstractmethod
    def loaded(self) -> bool:
        """Returns ``True`` if the page is open, otherwise, ``False``. """
        pass


def _is_page_not_reachable(browser: Browser) -> bool:
    """Returns `True` if web page is not reachable due to networking issue otherwise `False`.

    Args:
        browser: a current browser session
    """
    try:
        return Element.by_class(browser, "neterror").is_displayed()
    except NoSuchElementException:
        return False


def open_url(browser: Browser, url: Url, timeout: int = 30) -> None:
    """Open a given URL in the browser."""
    _logger.debug("Open URL: %s", url)
    browser.get(str(url))
    if _is_page_not_reachable(browser):
        raise RuntimeError(f"WEB page '{url}' is not reachable due to networking issue!")
    Wait(browser, timeout=timeout).for_url(url.matcher())


class LoginPage(Page):
    """The base class for all objects which represents a login WEB page."""

    @abstractmethod
    def login(self, username: str, password: str) -> None:
        """Perform a login action with given credentials. """
        pass

    @abstractmethod
    def is_login_failed(self) -> bool:
        """Says if a login is failed or not."""
        pass


class LoginPageError(Exception):
    """The class represents an error that occurs during login procedure via WEB UI."""

    pass


class LoginAction:
    """A callable object which logins with a desired login page."""

    def __init__(self, login_page: LoginPage, credentials: Credentials) -> None:
        self._page = login_page
        self._credentials = credentials

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        if not self._page.loaded():
            self._page.open()
        self._page.login(self._credentials.username, self._credentials.password)
        for iteration in range(1, 601):
            if self._page.loaded():
                if self._page.is_login_failed():
                    raise RuntimeError(
                        f"Unable to login using {self._page.__class__.__name__} with {self._credentials}."
                    )
                time.sleep(1)
                _logger.debug("Login process still in progress. Waiting time is %s second(s)", iteration)
                continue
            break
        else:
            raise RuntimeError(
                f"Unable to login using '{self._page.__class__.__name__}' class "
                f"due to unexpected behavior of login functionally."
            )


def open_url_with_automatic_login(
    browser: Browser, url: Url, is_url_loaded: Callable[[], bool], login_action: LoginAction
) -> None:
    """Open a given URL in the browser and perform login if required.

    The login action will be executed if the initial URL won't be loaded successfully.
    """
    if not is_url_loaded():
        try:
            open_url(browser, url, timeout=10)
            login_action()
        except TimeoutException:
            if not is_url_loaded():
                login_action()
