import pytest
from enum import Enum
from testfixtures import LogCapture
from badoo.logger import Logger, MainLogger, LoggerError


class _ExpectedTestLogger(Enum):
    """Class represents test logger."""

    INFO: str = "Test info"
    ERROR: str = "Test error"
    WARNING: str = "Test warning"
    DEBUG: str = "Test debug"


@pytest.fixture(scope="module")
def logger() -> Logger:
    return MainLogger(__name__)


def test_logger_info(logger: Logger) -> None:
    with LogCapture() as logs:
        logger.info(_ExpectedTestLogger.INFO.value)
    assert _ExpectedTestLogger.INFO.value in str(logs)


def test_logger_error(logger: Logger) -> None:
    with LogCapture() as logs:
        logger.error(_ExpectedTestLogger.ERROR.value)
    assert _ExpectedTestLogger.ERROR.value in str(logs)


def test_logger_warning(logger: Logger) -> None:
    with LogCapture() as logs:
        logger.warning(_ExpectedTestLogger.WARNING.value)
    assert _ExpectedTestLogger.WARNING.value in str(logs)


def test_logger_debug(logger: Logger) -> None:
    logger.set_level(logger.DEBUG)
    with LogCapture() as logs:
        logger.debug(_ExpectedTestLogger.DEBUG.value)
    assert _ExpectedTestLogger.DEBUG.value in str(logs)


def test_set_logger_error(logger: Logger) -> None:
    with pytest.raises(LoggerError):
        logger.set_level(None)
