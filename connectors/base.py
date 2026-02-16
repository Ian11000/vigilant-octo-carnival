"""Base connector interfaces for data sources and destinations."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable

Record = dict[str, Any]


class SourceConnector(ABC):
    """Interface for extracting records from a source system."""

    @abstractmethod
    def extract(self) -> Iterable[Record]:
        """Return an iterable of records."""


class DestinationConnector(ABC):
    """Interface for loading records into a destination system."""

    @abstractmethod
    def load(self, records: Iterable[Record]) -> int:
        """Load records and return the number of records written."""
