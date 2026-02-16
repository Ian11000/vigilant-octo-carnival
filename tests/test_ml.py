from __future__ import annotations

import pandas as pd

from ml.baseline import train_baseline_model


def test_train_baseline_model_returns_valid_result():
    df = pd.DataFrame(
        {
            "monthly_spend": [120.5, 80.0, 150.0, 45.0, 200.0, 95.0, 30.0, 175.0, 60.0, 140.0],
            "churned": [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        }
    )

    result = train_baseline_model(df)

    assert 0.0 <= result.accuracy <= 1.0
    assert result.train_size + result.test_size == len(df)
