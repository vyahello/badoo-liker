"""Timing for Page Object Framework."""
from typing import Tuple
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from badoo.connections.web import Browser


class Wait:
    """Interface for waiting action in the framework and tests."""

    def __init__(self, browser: Browser, timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """Initialize object.

        Attributes:
            browser: engine for operating in the web browser.
            timeout: maximum time after which the exception should be rise.
            poll_frequency: define how often driver should be ask for the wait condition.
        """
        self._browser: Browser = browser
        self._timeout: int = timeout
        self._wait: WebDriverWait = WebDriverWait(self._browser, self._timeout, poll_frequency)

    def for_url(self, url_matcher: str) -> None:
        """Wait for url to be present."""
        self._wait.until(
            ec.url_contains(url_matcher),
            message=(
                f"Expected the '{self._browser.current_url}' to contain "
                f"'{url_matcher}' but it doesn't. Timeout {self._timeout} second(s)."
            ),
        )

    def for_element_to_disappear(self, locator: Tuple[str, str]) -> None:
        """Wait until an element is no longer on the page."""
        self._wait.until(
            ec.invisibility_of_element_located(locator),
            message=f"Expected element '{locator}' to disappear within {self._timeout} second(s) but it didn't.",
        )

    def for_element_to_be_visible(self, locator: Tuple[str, str]) -> None:
        """Wait until an element is visible on the page."""
        self._wait.until(
            ec.visibility_of_element_located(locator),
            message=f"Expected element '{locator}' to be visible within {self._timeout} second(s) but it didn't.",
        )

    def for_element_to_be_clickable(self, locator: Tuple[str, str]) -> None:
        """Wait until an element on the page can be clicked."""
        self._wait.until(
            ec.element_to_be_clickable(locator),
            message=f"Expected element '{locator}' to be clickable within {self._timeout} second(s) but it didn't.",
        )
