from abc import ABC, abstractmethod
from badoo.connections.web import Browser
from badoo.logger import Logger, MainLogger
from badoo.setup import Credentials
from badoo.web.workflow import BadooEncountersPage


_logger: Logger = MainLogger(__name__)


class Liker(ABC):
    """Abstract interface for a liker service."""

    @abstractmethod
    def start(self, amount: int, mutual_message: str) -> None:
        pass


class BadooLiker(Liker):
    """Interface for badoo service liker."""

    def __init__(self, browser: Browser, credentials: Credentials) -> None:
        self._badoo_page: BadooEncountersPage = BadooEncountersPage(
            browser, credentials
        )

    def start(self, amount: int, mutual_message: str) -> None:
        _logger.info(
            "Operating %s badoo like attempts, in progress ...", amount
        )
        self._badoo_page.open()
        for _ in range(amount):
            self._badoo_page.like()
            if self._badoo_page.is_mutual_like():
                self._badoo_page.send_message(mutual_message)
        _logger.info(
            "%s badoo like attempts were successfully completed, "
            "please check your messages!",
            amount,
        )
