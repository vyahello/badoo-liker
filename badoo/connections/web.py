import functools
import weakref
from abc import ABC, abstractmethod
from typing import Any, Dict
from selenium.webdriver import ChromeOptions, Remote
from selenium.webdriver.remote.file_detector import UselessFileDetector
from badoo.logger import Logger, MainLogger

_logger: Logger = MainLogger(__name__)


class BrowserSettings(ABC):
    """The class represents `Browser` settings ."""

    @abstractmethod
    def grid_url(self) -> str:
        """Return an url to a Selenium server e.g `http://localhost:9515`."""
        pass


class Browser:
    """The class is a proxy for ``Remote`` object.

    It has the same interface that ``Remote`` object from ``selenium.webdriver`` module has.
    """

    def __init__(self, settings: BrowserSettings) -> None:
        @functools.lru_cache()
        def client() -> Remote:
            _logger.info("Starting a 'chrome' session. Connect to: %s", settings.grid_url())
            options: ChromeOptions = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            capabilities: Dict[str, Any] = options.to_capabilities()
            capabilities["idleTimeout"] = 10800
            return Remote(
                command_executor=settings.grid_url(),
                desired_capabilities=capabilities,
                file_detector=UselessFileDetector(),
            )

        self._client = client

        def close(cache) -> None:
            if cache.cache_info().currsize > 0:
                _logger.info("Closing the browser session. Disconnect from %s", settings.grid_url())
                cache().quit()

        weakref.finalize(self, close, self._client)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._client(), name)

