"""
create Pydantic models
"""

from pydantic import BaseModel, validator
from scipy.stats import loguniform


def must_be_non_negative(v: float) -> float:
    """Check if the v is non-negative

    Parameters
    ----------
    v : float
        value

    Returns
    -------
    float
        v

    Raises
    ------
    ValueError
        Raises error when v is negative
    """
    if v < 0:
        raise ValueError(f"{v} must be non-negative")
    return v


class Location(BaseModel):
    """Specify the locations of inputs and outputs"""

    train_data_raw: str = "data/raw/fruits-360/Training"
    test_data_raw: str = "data/raw/fruits-360/Test"
    data_process: str = "data/processed/fruits.pkl"
    data_final: str = "data/final/predictions.pkl"
    model: str = "models/svc.pkl"
    scaler: str = "processors/scaler.pkl"
    input_notebook: str = "notebooks/analyze_results.ipynb"
    output_notebook: str = "notebooks/results.ipynb"


class ProcessConfig(BaseModel):
    """Specify the parameters of the `process` flow"""

    fruits: list[str] = ["apple", "banana"]
    test_size: float = 0.3

    _validated_test_size = validator("test_size", allow_reuse=True)(
        must_be_non_negative
    )


class ModelParams(BaseModel):
    """Specify the parameters of the `train` flow"""

    C: list[float] = [1, 10]
    gamma: list[float] = [1, 0.1]

    _validated_fields = validator("*", allow_reuse=True, each_item=True)(
        must_be_non_negative
    )
