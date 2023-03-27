"""Python script to process the data"""

import os
from typing import Union

import cv2
import joblib
import numpy as np
import pandas as pd
from prefect import flow, task
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config import Location, ProcessConfig


@task
def load_fruit_images(fruits: list[str], path: str, dim: int = 100) -> tuple:
    if not os.path.exists(path):
        raise ValueError(f"Path '{path}' does not exist.")

    images = []
    labels = []
    for fruit in fruits:
        for subfolder_name in os.listdir(path):
            if fruit in subfolder_name.lower():
                subfolder_path = os.path.join(path, subfolder_name)
                for image_file in os.listdir(subfolder_path):
                    if image_file.endswith(".jpg"):
                        image_path = os.path.join(subfolder_path, image_file)
                        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
                        image = cv2.resize(image, (dim, dim))
                        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                        images.append(image)
                        labels.append(fruit)
    return np.array(images), np.array(labels)


@task
def scale_data(train_data: np.ndarray, test_data: np.ndarray) -> tuple:
    scaler = StandardScaler()
    scaled_train = scaler.fit_transform([i.flatten() for i in train_data])
    scaled_test = scaler.transform([i.flatten() for i in test_data])
    return scaled_train, scaled_test


@task
def split_train_test(X: pd.DataFrame, y: pd.DataFrame, test_size: int) -> dict:
    """_summary_

    Parameters
    ----------
    X : pd.DataFrame
        Features
    y : pd.DataFrame
        Target
    test_size : int
        Size of the test set
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    }


@task
def save_processed_data(data: dict, save_location: str):
    """Save processed data

    Parameters
    ----------
    data : dict
        Data to process
    save_location : str
        Where to save the data
    """
    joblib.dump(data, save_location)


@flow
def process(
    location: Location = Location(),
    config: ProcessConfig = ProcessConfig(),
):
    """Flow to process the ata

    Parameters
    ----------
    location : Location, optional
        Locations of inputs and outputs, by default Location()
    config : ProcessConfig, optional
        Configurations for processing data, by default ProcessConfig()
    """
    X_train, y_train = load_fruit_images(
        config.fruits, location.train_data_raw
    )

    split_data = split_train_test(X_train, y_train, config.test_size)  # type: ignore

    split_data["X_train"], split_data["X_test"] = scale_data(
        split_data["X_train"], split_data["X_test"]
    )

    save_processed_data(split_data, location.data_process)


if __name__ == "__main__":
    process(config=ProcessConfig(test_size=0.2))
