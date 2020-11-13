"""A module contains a set of API to work with console logger."""
import functools
import logging
from abc import ABC, abstractmethod
from typing import Any, Callable, Union


class LoggerError(Exception):
    """The class represents a console logger error."""

    pass


class Logger(ABC):
    """The class represents an abstraction for some logger."""

    NONSET: int
    INFO: int
    ERROR: int
    WARNING: int
    DEBUG: int

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

    @abstractmethod
    def set_level(self, level: Union[str, int]) -> None:
        """Sets the logging level of this logger.

        Args:
            level: a level to be set. Level must be an `int` or an `str`.

        Raises:
            `LoggerError` if level parameter is invalid
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
        @functools.lru_cache()
        def client() -> logging.Logger:
            """Sets up main logger client.

            Returns: a main logger
            """
            logger: logging.Logger = logging.getLogger(name)
            handler: logging.Handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    fmt="[%(asctime)s %(levelname)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
            )
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger

        self._logger: Callable[[], logging.Logger] = client

    def info(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().info(message, *args, **kwargs)

    def debug(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().debug(message, *args, **kwargs)

    def warning(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().warning(message, *args, **kwargs)

    def error(self, message: str, *args: Any, **kwargs: Any) -> None:
        self._logger().error(message, *args, **kwargs)

    def set_level(self, level: Union[str, int]) -> None:
        if isinstance(level, str) or isinstance(level, int):
            self._logger().setLevel(level)
        else:
            raise LoggerError('Logging level must be an "int" or an "str"!')
