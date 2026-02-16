"""JSON destination connector implementation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from connectors.base import DestinationConnector, Record


class JSONDestinationConnector(DestinationConnector):
    """Load records into a JSON file destination."""

    def __init__(self, output_path: str | Path) -> None:
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self, records: Iterable[Record]) -> int:
        materialized = list(records)
        with self.output_path.open("w", encoding="utf-8") as handle:
            json.dump(materialized, handle, indent=2)
        return len(materialized)
