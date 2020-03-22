from typing import Dict, Any
from uyaml.loader import Yaml
from badoo.connections.web import BrowserSettings


class Credentials:
    """The class represents a credentials as an object."""

    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self._password: str = password

    def __str__(self):
        return f'{self.__class__.__name__}[user = "{self.username}"; pass = "{self.password}]"'

    @property
    def username(self) -> str:
        """Return a user name."""
        return self._username

    @property
    def password(self) -> str:
        """Return a password."""
        return self._password


class _Browser(BrowserSettings):
    """Represents browser settings defined in setup file."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self._data: Dict[str, Any] = data

    def grid_url(self) -> str:
        return self._data["grid-url"]

    def proxy(self) -> str:
        return self._data["proxy"]


class _Badoo:
    """Represents badoo settings defined in setup file."""

    def __init__(self, data: Dict[str, Any]) -> None:
        self._data: Dict[str, Any] = data

    def credentials(self) -> Credentials:
        return Credentials(self._data["credentials"]["login"], self._data["credentials"]["password"])

    def likes(self) -> int:
        return self._data["likes"]

    def intro_message(self) -> str:
        return self._data["intro-massage"]


class Setup:
    def __init__(self, yaml: Yaml) -> None:
        self._data: Dict[str, Any] = yaml.section(name="setup")

    def browser(self) -> BrowserSettings:
        return _Browser(self._data["browser"])

    def badoo(self) -> _Badoo:
        return _Badoo(self._data["badoo"])
