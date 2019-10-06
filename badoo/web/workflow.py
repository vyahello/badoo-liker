from enum import Enum
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from badoo.connections.web import Browser
from badoo.setup import Credentials
from badoo.web.support.element import WebElement, Element
from badoo.web.support.page import LoginPage, Url, open_url, Page, LoginPath, open_url_with_automatic_login


class BadooError(Exception):
    """Represents custom badoo exception."""

    pass


class _BadooRequest(Enum):
    """Class represents enumeration for badoo items."""

    HOST: str = "badoo.com"

    def __str__(self) -> str:
        return self.value


class BadooLoginPage(LoginPage):
    """"The class represents badoo login page."""

    def __init__(self, browser: Browser) -> None:
        self._browser: Browser = browser
        self._url: Url = Url(f"{_BadooRequest.HOST}/en/signin")

    def open(self) -> None:
        open_url(self._browser, self._url)

    def loaded(self) -> bool:
        return str(self._url) == self._browser.current_url

    def login(self, username: str, password: str) -> None:
        WebElement.find(self._browser).by_class("js-signin-login").set(username)
        WebElement.find(self._browser).by_class("js-signin-password").set(password)
        WebElement.find(self._browser).by_css("button[type='submit']").click()

    def is_login_failed(self) -> bool:
        try:
            return WebElement.find(self._browser).by_class("new-form__error").is_displayed()
        except NoSuchElementException:
            return False


class BadooEncountersPage(Page):
    """"The class represents badoo encounters page."""

    def __init__(self, browser: Browser, credentials: Credentials) -> None:
        self._browser: Browser = browser
        self._url: Url = Url(f"{_BadooRequest.HOST}/encounters")
        self._login: LoginPath = LoginPath(BadooLoginPage(browser), credentials)

    def open(self) -> None:
        open_url_with_automatic_login(self._browser, self._url, self.loaded, self._login)

    def loaded(self) -> bool:
        return str(self._url) in self._browser.current_url

    def like(self) -> None:
        if self._is_blocker_visible():
            self._browser.refresh()

        WebElement.find(self._browser).by_class("profile-action--yes").click()

        if self._is_out_of_votes():
            raise BadooError("Sorry! You've hit the vote limit!")

        try:
            WebElement.find(self._browser).by_class("js-chrome-pushes-deny").wait_for_visibility(1).click()
        except TimeoutException:
            pass

    def is_mutual_like(self) -> bool:
        try:
            self._match().wait_for_visibility(1)
            return True
        except TimeoutException:
            return False

    def send_message(self, message: str) -> None:
        WebElement.find(self._browser).by_class("js-message").set(message, clear=True)
        WebElement.find(self._browser).by_class("js-send-message").click()
        self._match().wait_for_disappear(2)
        WebElement.find(self._browser).by_class("confirmation").wait_for_disappear(2)

    def _match(self) -> Element:
        return WebElement.find(self._browser).by_class("ovl-match")

    def _is_blocker_visible(self) -> bool:
        try:
            return WebElement.find(self._browser).by_class("ovl").wait_for_visibility(1).is_displayed()
        except TimeoutException:
            return False

    def _is_out_of_votes(self) -> bool:
        try:
            return WebElement.find(self._browser).by_class("ovl__content").wait_for_visibility(1).is_displayed()
        except TimeoutException:
            return False
