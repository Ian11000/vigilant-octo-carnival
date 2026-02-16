from __future__ import annotations

import json

from connectors.csv_source import CSVSourceConnector
from connectors.json_destination import JSONDestinationConnector
from pipelines.etl import run_etl


def test_run_etl_writes_expected_records(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_json = tmp_path / "output.json"

    input_csv.write_text(
        "customer_id,country,monthly_spend,churned\n"
        "1,USA,10.0,0\n"
        "2,India,20.0,1\n",
        encoding="utf-8",
    )

    loaded_count = run_etl(
        CSVSourceConnector(input_csv),
        JSONDestinationConnector(output_json),
    )

    assert loaded_count == 2
    rows = json.loads(output_json.read_text(encoding="utf-8"))
    assert rows[0]["customer_id"] == 1
    assert rows[1]["churned"] == 1
