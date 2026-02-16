"""Feature engineering utilities."""

from __future__ import annotations

import pandas as pd


NUMERIC_FEATURES = ["monthly_spend"]
TARGET = "churned"


def build_feature_matrix(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Split DataFrame into X and y for baseline model training."""
    x = df[NUMERIC_FEATURES]
    y = df[TARGET]
    return x, y
