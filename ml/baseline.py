"""Baseline ML model training and evaluation."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from ml.features import build_feature_matrix


@dataclass
class TrainingResult:
    """Container for baseline training metrics."""

    accuracy: float
    train_size: int
    test_size: int


def train_baseline_model(df: pd.DataFrame) -> TrainingResult:
    """Train a logistic regression baseline model on sample churn data."""
    x, y = build_feature_matrix(df)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.4, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1_000)
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    accuracy = accuracy_score(y_test, preds)

    return TrainingResult(
        accuracy=accuracy,
        train_size=len(x_train),
        test_size=len(x_test),
    )
