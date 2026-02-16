# DataBridge Lab

DataBridge Lab is a starter repository for experimenting with:

- **Data Engineering connectors** (reading from source systems and loading into destinations)
- **Data movement pipelines** (extract, transform, load)
- **Machine Learning workflows** (feature prep + baseline model training)

It is designed as a practical sandbox for testing tools and patterns used by both Data Engineers and Data Scientists.

## Project Goals

- Create reusable connector interfaces.
- Build simple local connectors (CSV source and JSON destination) to prototype quickly.
- Provide an extensible pipeline runner for ETL jobs.
- Include a machine learning baseline workflow that trains and evaluates a model.
- Offer tests so the repository can be used safely for experimentation.

## Repository Structure

```text
.
├── connectors/
│   ├── base.py
│   ├── csv_source.py
│   └── json_destination.py
├── pipelines/
│   ├── etl.py
│   └── transforms.py
├── ml/
│   ├── baseline.py
│   └── features.py
├── data/
│   ├── sample_input.csv
│   └── output/
├── tests/
│   ├── test_etl.py
│   └── test_ml.py
├── pyproject.toml
├── requirements.txt
└── run_demo.py
```

## Quick Start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the ETL + ML demo:

```bash
python run_demo.py
```

3. Run tests:

```bash
pytest
```

## How to Extend

- Add a new source connector by implementing `SourceConnector` in `connectors/base.py`.
- Add a new destination connector by implementing `DestinationConnector` in `connectors/base.py`.
- Add transformation logic in `pipelines/transforms.py`.
- Swap the model in `ml/baseline.py` with your preferred algorithm.

## Suggested Next Steps

- Add database connectors (PostgreSQL, BigQuery, Snowflake).
- Add orchestration examples with Airflow, Dagster, or Prefect.
- Add data validation with Great Expectations.
- Add experiment tracking with MLflow.
