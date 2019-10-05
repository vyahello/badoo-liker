from enum import Enum
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from badoo.connections.web import Browser
from badoo.setup import Credentials
from badoo.web.support.element import Element
from badoo.web.support.page import LoginPage, Url, open_url, Page, LoginAction, open_url_with_automatic_login


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
        Element.by_class(self._browser, "js-signin-login").set(username)
        Element.by_class(self._browser, "js-signin-password").set(password)
        Element.by_css(self._browser, "button[type='submit']").click()

    def is_login_failed(self) -> bool:
        try:
            return Element.by_class(self._browser, 'new-form__error').is_displayed()
        except NoSuchElementException:
            return False


class BadooEncountersPage(Page):
    """"The class represents badoo encounters page."""

    def __init__(self, browser: Browser, credentials: Credentials) -> None:
        self._browser: Browser = browser
        self._url: Url = Url(f"{_BadooRequest.HOST}/encounters")
        self._login: LoginAction = LoginAction(BadooLoginPage(browser), credentials)

    def open(self) -> None:
        open_url_with_automatic_login(self._browser, self._url, self.loaded, self._login)

    def loaded(self) -> bool:
        return str(self._url) in self._browser.current_url

    def like(self) -> None:
        Element.by_class(self._browser, "profile-action--yes").click()
        try:
            Element.by_class(self._browser, "js-chrome-pushes-deny").wait_for_visibility(2).click()
        except TimeoutException:
            pass

    def is_mutual(self) -> bool:
        try:
            Element.by_class(self._browser, "ovl-match").wait_for_visibility(2)
            return True
        except TimeoutException:
            return False

    def send_message(self, message: str) -> None:
        Element.by_class(self._browser, "js-message").set(message, clear=True)
        Element.by_class(self._browser, "js-send-message").click()
        Element.by_class(self._browser, "js-gallery-next").wait_to_be_clickable(5)
