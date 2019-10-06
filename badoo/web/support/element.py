"""Implements Element abstraction according to Page Object Pattern."""
import time
from abc import ABC, abstractmethod
from typing import Any, Tuple, Union
from selenium.webdriver.common.by import By
from badoo.connections.web import Browser
from badoo.web.support.wait import Wait


class Element(ABC):
    """Represents abstract interface for an element."""

    @abstractmethod
    def set(self, value: Union[int, str], clear: bool = False, delay_in_seconds: int = None) -> None:
        """Set value for element."""
        pass

    @abstractmethod
    def click(self) -> None:
        """Find and click on the element."""
        pass

    @abstractmethod
    def is_displayed(self) -> bool:
        """Returns `True` if element is displayed otherwise `False`."""
        pass

    @abstractmethod
    def wait_for_disappear(self, timeout: int = 30) -> "Element":
        """Wait for element to disappear."""
        pass

    @abstractmethod
    def wait_for_visibility(self, timeout: int = 30) -> "Element":
        """Wait for element to be visible."""
        pass

    @abstractmethod
    def wait_to_be_clickable(self, timeout: int = 30) -> "Element":
        """Wait for element to be clickable."""
        pass

    @classmethod
    @abstractmethod
    def find(cls, browser: Browser) -> "Find":
        """Find an element."""
        pass


class Find(ABC):
    """Represents abstract interface find an element."""

    @abstractmethod
    def by_id(self, location: str) -> Element:
        """Create element located by ID."""
        pass

    @abstractmethod
    def by_class(self, location: str) -> Element:
        """Create element located by class name."""
        pass

    @abstractmethod
    def by_name(self, location: str) -> Element:
        """Create element located by name."""
        pass

    @abstractmethod
    def by_css(self, location: str) -> Element:
        """Create element located by css selector."""
        pass

    @abstractmethod
    def by_link_text(self, location: str) -> Element:
        """Create element located by link text."""
        pass


class _WebFind(Find):
    """Represents interface to find web element."""

    def __init__(self, browser: Browser) -> None:
        self._browser: Browser = browser

    def by_id(self, location: str) -> Element:
        """Create element located by ID."""
        return WebElement(self._browser, By.ID, location)

    def by_class(self, location: str) -> Element:
        """Create element located by class name."""
        return WebElement(self._browser, By.CLASS_NAME, location)

    def by_name(self, location: str) -> Element:
        """Create element located by name."""
        return WebElement(self._browser, By.NAME, location)

    def by_css(self, location: str) -> Element:
        """Create element located by css selector."""
        return WebElement(self._browser, By.CSS_SELECTOR, location)

    def by_link_text(self, location: str) -> Element:
        """Create element located by link text."""
        return WebElement(self._browser, By.LINK_TEXT, location)


class WebElement(Element):
    """Represents an web element of the page."""

    def __init__(self, context: Any, strategy: str, locator: str) -> None:
        self._context = context
        self._locator: Tuple[str, str] = (strategy, locator)

    def set(self, value: Union[int, str], clear: bool = False, delay_in_seconds: int = None) -> None:
        """Set value for element."""
        if clear:
            self.wait_for_visibility()._element().clear()
        self.wait_for_visibility()._element().send_keys(value)

        if delay_in_seconds:
            time.sleep(delay_in_seconds)

    def click(self) -> None:
        """Find and click on the element."""
        self.wait_to_be_clickable()._element().click()

    def is_displayed(self) -> bool:
        """Returns `True` if element is displayed otherwise `False`."""
        return self._element().is_displayed()

    def wait_for_disappear(self, timeout: int = 30) -> "WebElement":
        """Wait for element to disappear."""
        Wait(self._context, timeout=timeout).for_element_to_disappear(self._locator)
        return self

    def wait_for_visibility(self, timeout: int = 30) -> "WebElement":
        """Wait for element to be visible."""
        Wait(self._context, timeout=timeout).for_element_to_be_visible(self._locator)
        return self

    def wait_to_be_clickable(self, timeout: int = 30) -> "WebElement":
        """Wait for element to be clickable."""
        Wait(self._context, timeout=timeout).for_element_to_be_clickable(self._locator)
        return self

    @classmethod
    def find(cls, browser: Browser) -> Find:
        return _WebFind(browser)

    def _element(self) -> Any:
        """Find element on the page."""
        return self._context.find_element(*self._locator)
