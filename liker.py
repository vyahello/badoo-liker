from abc import ABC, abstractmethod
import click
from badoo.connections.web import Browser
from badoo.services import Liker, BadooLiker
from badoo.setup import Setup
from badoo.yaml import YamlFromPath


class _Executor(ABC):
    """Abstract executor interface."""

    @abstractmethod
    def run(self) -> None:
        """Runs executor."""
        pass


class _LikerExecutor(_Executor):
    """Represents liker executor item."""

    def __init__(self, setup: Setup) -> None:
        self._message_to_send: str = setup.badoo().intro_message()
        self._attempts: int = setup.badoo().likes()
        self._liker: Liker = BadooLiker(Browser(setup.browser()), setup.badoo().credentials())

    def run(self) -> None:
        self._liker.start(self._attempts, self._message_to_send)


@click.command()
@click.option("--config", "-c", help="Setup badoo config file (e.g `setup.yaml`)", default="setup.yaml")
def _run_badoo_liker(config: str) -> None:
    """The program allows to run badoo liker service."""
    executor: _Executor = _LikerExecutor(Setup(YamlFromPath(config)))
    executor.run()


if __name__ == "__main__":
    _run_badoo_liker()
