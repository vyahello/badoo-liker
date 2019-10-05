"""Implements Element abstraction according to Page Object Pattern."""
import time
from typing import Any, Tuple, Union
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from badoo.web.support.wait import Wait


class Element:
    """Represents an element on the page."""

    def __init__(self, context: Any, strategy: str, locator: str) -> None:
        self._context = context
        self._locator: Tuple[str, str] = (strategy, locator)

    def set(self, value: Union[int, str], clear: bool = False, delay_in_seconds: int = None) -> None:
        """Set value for element."""
        if clear:
            self.wait_for_visibility().find().clear()
        self.wait_for_visibility().find().send_keys(value)

        if delay_in_seconds:
            time.sleep(delay_in_seconds)

    def click(self) -> None:
        """Find and click on the element."""
        self.wait_to_be_clickable().find().click()

    def hover(self) -> None:
        """Hover the mouse pointer over the element."""
        ActionChains(self._context).move_to_element(self._element()).perform()

    def is_displayed(self) -> bool:
        """Returns `True` if element is displayed otherwise `False`."""
        return self._element().is_displayed()

    def text(self) -> str:
        """Return text of the element."""
        return self._element().text

    def find(self) -> Any:
        """Return web element."""
        return self._element()

    def select_by_text(self, text: str) -> None:
        """Select by text in web element."""
        Select(self._element()).select_by_visible_text(text)

    def wait_for_disappear(self, timeout: int = 30) -> "Element":
        """Wait for element to disappear."""
        Wait(self._context, timeout=timeout).for_element_to_disappear(self._locator)
        return self

    def wait_for_presence(self, timeout: int = 30) -> "Element":
        """Wait for element to appear."""
        Wait(self._context, timeout=timeout).for_element_to_be_present(self._locator)
        return self

    def wait_for_visibility(self, timeout: int = 30) -> "Element":
        """Wait for element to be visible."""
        Wait(self._context, timeout=timeout).for_element_to_be_visible(self._locator)
        return self

    def wait_to_be_clickable(self, timeout: int = 30) -> "Element":
        """Wait for element to be clickable."""
        Wait(self._context, timeout=timeout).for_element_to_be_clickable(self._locator)
        return self

    def wait_for_text_to_be_present(self, text: str, timeout: int = 30) -> None:
        """Wait for specific text to be present in element."""
        Wait(self._context, timeout=timeout).for_text_to_be_present(self._locator, text)

    def wait_for_text_to_disappear(self, text: str, timeout: int = 30) -> None:
        """Wait for specific text to disappear in element."""
        Wait(self._context, timeout=timeout).for_text_to_disappear(self._locator, text)

    @classmethod
    def by_id(cls, context: Any, locator: str) -> "Element":
        """Create element located by ID."""
        return cls(context, By.ID, locator)

    @classmethod
    def by_class(cls, context: Any, locator: str) -> "Element":
        """Create element located by class name."""
        return cls(context, By.CLASS_NAME, locator)

    @classmethod
    def by_name(cls, context: Any, locator: str) -> "Element":
        """Create element located by name."""
        return cls(context, By.NAME, locator)

    @classmethod
    def by_css(cls, context: Any, locator: str) -> "Element":
        """Create element located by css selector."""
        return cls(context, By.CSS_SELECTOR, locator)

    @classmethod
    def by_link_text(cls, context: Any, locator: str) -> "Element":
        """Create element located by link text."""
        return cls(context, By.LINK_TEXT, locator)

    def _element(self) -> Any:
        """Find element on the page."""
        return self._context.find_element(*self._locator)
