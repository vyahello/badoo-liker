"""A module contains a set of API to work with console logger."""
import logging
from abc import ABC, abstractmethod
from typing import Any


class LoggerError(Exception):
    """The class represents a console logger error."""

    pass


class Logger(ABC):
    """The class represents an abstraction for some logger."""

    @abstractmethod
    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        Logger(...).info("Houston, we have a %s", "interesting problem", exc_info=1)

        Args:
            message: a message to log into a console
            *args: other positional arguments
            **kwargs: other keyword arguments
        """
        pass

    @abstractmethod
    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        Logger(...).debug("Houston, we have a %s", "thorny problem", exc_info=1)

        Args:
            message: a message to log into a console
            *args: other positional arguments
            **kwargs: other keyword arguments
        """
        pass

    @abstractmethod
    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value e.g.

        Logger(...).warning("Houston, we have a %s", "bit of a problem", exc_info=1)

        Args:
            message: a message to log into a console
            *args: other positional arguments
            **kwargs: other keyword arguments
        """
        pass

    @abstractmethod
    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        Logger(...).error("Houston, we have a %s", "major problem", exc_info=1)

        Args:
            message: a message to log into a console
            *args: other positional arguments
            **kwargs: other keyword arguments
        """
        pass


class MainLogger(Logger):
    """The class represents main console logger."""

    NONSET: int = logging.NOTSET
    INFO: int = logging.INFO
    ERROR: int = logging.ERROR
    WARNING: int = logging.WARNING
    DEBUG: int = logging.DEBUG

    def __init__(self, name: str) -> None:
        self._logger: logging.Logger = logging.getLogger(name)

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger.info(message, *args, **kwargs)

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger.debug(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger.error(message, *args, **kwargs)
