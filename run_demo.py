"""Run a demo ETL pipeline and baseline ML training."""

from __future__ import annotations

import json

import pandas as pd

from connectors.csv_source import CSVSourceConnector
from connectors.json_destination import JSONDestinationConnector
from ml.baseline import train_baseline_model
from pipelines.etl import run_etl


def main() -> None:
    source = CSVSourceConnector("data/sample_input.csv")
    destination = JSONDestinationConnector("data/output/transformed.json")

    loaded_count = run_etl(source, destination)

    with open("data/output/transformed.json", "r", encoding="utf-8") as handle:
        records = json.load(handle)

    df = pd.DataFrame(records)
    result = train_baseline_model(df)

    print(f"Loaded records: {loaded_count}")
    print(f"Baseline accuracy: {result.accuracy:.3f}")
    print(f"Train/Test sizes: {result.train_size}/{result.test_size}")


if __name__ == "__main__":
    main()
