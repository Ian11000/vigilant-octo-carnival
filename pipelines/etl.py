"""Simple ETL runner."""

from __future__ import annotations

from connectors.base import DestinationConnector, SourceConnector
from pipelines.transforms import clean_and_cast


def run_etl(source: SourceConnector, destination: DestinationConnector) -> int:
    """Run extraction, transformation, and load steps."""
    raw_records = source.extract()
    transformed_records = clean_and_cast(raw_records)
    loaded_count = destination.load(transformed_records)
    return loaded_count
