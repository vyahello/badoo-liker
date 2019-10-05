from abc import ABC, abstractmethod
from typing import Dict, Any, TextIO, List
import yaml


class Yaml(ABC):
    """The interface to work with YAML files."""

    @property
    @abstractmethod
    def data(self) -> Dict[str, Any]:
        """Return all data for the YAML file as a dictionary."""
        pass

    @abstractmethod
    def section(self, name: str) -> Dict[str, Any]:
        """Return a root section of data from a YAML file."""
        pass


class _YamlFromStream(Yaml):
    """Represent a stream as a ``Yaml`` objects."""

    def __init__(self, stream: TextIO) -> None:
        self._yaml = yaml.safe_load(stream)

    @property
    def data(self) -> Dict[str, Any]:
        return self._yaml

    def section(self, name: str) -> Dict[str, Any]:
        return self._yaml[name]


class YamlFromPath(Yaml):
    """Represent a file (a path) as a ``Yaml`` object."""

    def __init__(self, path: str) -> None:
        self._file = path
        self._data: List[Yaml] = []

    def _parsed_yaml(self) -> Yaml:
        if not self._data:
            with open(self._file) as file:
                self._data.append(_YamlFromStream(file))
        return self._data[0]

    @property
    def data(self) -> Dict[str, Any]:
        return self._parsed_yaml().data

    def section(self, name: str) -> Dict[str, Any]:
        return self._parsed_yaml().section(name)
