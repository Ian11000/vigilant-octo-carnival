"""Transform functions for ETL pipelines."""

from __future__ import annotations

from typing import Iterable

from connectors.base import Record


def clean_and_cast(records: Iterable[Record]) -> list[Record]:
    """Trim whitespace and cast numeric fields for sample data."""
    cleaned: list[Record] = []
    for record in records:
        transformed = {
            "customer_id": int(record["customer_id"]),
            "country": record["country"].strip(),
            "monthly_spend": float(record["monthly_spend"]),
            "churned": int(record["churned"]),
        }
        cleaned.append(transformed)
    return cleaned
