"""CSV source connector implementation."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from connectors.base import Record, SourceConnector


class CSVSourceConnector(SourceConnector):
    """Extract records from a CSV file."""

    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def extract(self) -> Iterable[Record]:
        with self.file_path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                yield dict(row)
