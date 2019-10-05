"""Timing for Page Object Framework."""
from typing import Tuple
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Wait:
    """Interface for waiting action in the framework and tests."""

    def __init__(self, driver, timeout: int = 30, poll_frequency: float = 0.5) -> None:
        """Initialize object.

        Attributes:
            driver: engine for operating in the web browser.
            timeout: maximum time after which the exception should be rise.
            poll_frequency: define how often driver should be ask for the wait condition.
        """
        self._driver = driver
        self._timeout = timeout
        self._wait = WebDriverWait(self._driver, self._timeout, poll_frequency)

    def for_url(self, url_matcher: str) -> None:
        """Wait for url to be present."""
        self._wait.until(
            ec.url_contains(url_matcher),
            message=(
                f"Expected the '{self._driver.current_url}' to contain "
                f"'{url_matcher}' but it doesn't. Timeout {self._timeout} second(s)."
            ),
        )

    def for_element_to_disappear(self, locator: Tuple[str, str]) -> None:
        """Wait until an element is no longer on the page."""
        self._wait.until(
            ec.invisibility_of_element_located(locator),
            message=f"Expected element '{locator}' to disappear within {self._timeout} second(s) but it didn't.",
        )

    def for_element_to_be_present(self, locator: Tuple[str, str]) -> None:
        """Wait until an element appears on the page."""
        self._wait.until(
            ec.presence_of_element_located(locator),
            message=f"Expected element '{locator}' to be present within {self._timeout} second(s) but it didn't.",
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

    def for_alert_presence(self):
        """Wait until an alert is displayed on the page."""
        self._wait.until(
            ec.alert_is_present(),
            message=f"Expected alert to be present within {self._timeout} second(s) but it didn't.",
        )

    def for_all_elements_to_be_visible(self, locator: Tuple[str, str]) -> None:
        """Wait until all elements are visible on the page."""
        self._wait.until(
            ec.visibility_of_all_elements_located(locator),
            message=(
                f"Expected all elements '{locator}' to be visible within {self._timeout} second(s) but they didn't."
            ),
        )

    def for_text_to_be_present(self, locator: Tuple[str, str], text: str) -> None:
        """Wait until specific text to be present in element.

        Args:
            locator: a strategy to find an element
            text: text to be find in element
        """
        self._wait.until(
            ec.text_to_be_present_in_element(locator, text),
            message=(
                f"Expected text '{text}' to be present in {locator} element"
                f" within {self._timeout} second(s) but it didn't."
            ),
        )

    def for_text_to_disappear(self, locator: Tuple[str, str], text: str) -> None:
        """Wait until specific text to be present in element.

        Args:
            locator: a strategy to find an element
            text: text to be find in element
        """
        self._wait.until_not(
            ec.text_to_be_present_in_element(locator, text),
            message=(
                f"Expected text '{text}' to disappear in {locator} element"
                f" within {self._timeout} second(s) but it didn't."
            ),
        )
