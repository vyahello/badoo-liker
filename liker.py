import sys
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from badoo.connections.web import Browser
from badoo.services import Liker, BadooLiker
from badoo.setup import Setup
from badoo.yaml import YamlFromPath


class Executor(ABC):
    """Abstract executor interface."""

    @abstractmethod
    def run(self) -> None:
        """Runs executor."""
        pass


def _setup() -> Setup:
    parser = ArgumentParser(description="This program allows to run badoo liker service.")
    parser.add_argument(
        "--config",
        "-c",
        help="Setup config file (e.g `config.yaml`)",
        type=str,
        required=True,
        default="setup.yaml",
    )
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    return Setup(YamlFromPath(vars(args)["setup"]))


class LikerExecutor(Executor):
    """Represents liker executor item."""

    def __init__(self, setup: Setup) -> None:
        self._message_to_send: str = setup.badoo().intro_message()
        self._attempts: int = setup.badoo().likes()
        self._liker: Liker = BadooLiker(Browser(setup.browser()), setup.badoo().credentials())

    def run(self) -> None:
        self._liker.start(self._attempts, self._message_to_send)


def _run_badoo_liker(setup: Setup) -> None:
    """Runs badoo liker."""
    executor: LikerExecutor = LikerExecutor(setup)
    executor.run()


if __name__ == "__main__":
    _run_badoo_liker(_setup())
