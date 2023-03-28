import logging
import threading
import time
from functools import lru_cache

import cv2
import joblib
import numpy as np
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import Location

location: Location = Location()


# cache model and scaler to not reload them for every request
@lru_cache(maxsize=1)
def load_model_and_scaler():

    with open(location.model, "rb") as f:
        model = joblib.load(f)

    with open(location.scaler, "rb") as f:
        scaler = joblib.load(f)

    return model, scaler


model, scaler = load_model_and_scaler()

app = FastAPI(title="Fruit Classifier API")

logging.basicConfig(filename="fruit_classifier.log", level=logging.INFO)

fruit_count = {"apple": 0, "banana": 0}


class Img(BaseModel):
    img_path: str


@app.post("/predict", status_code=200)
async def predict(request: Img):

    try:
        image = cv2.imread(request.img_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (100, 100))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)

        image_flat = image.flatten()

        image_scaled = scaler.transform([image_flat])

        prediction = model.predict(image_scaled)

        logging.info(f"Predicted Fruit: {prediction[0]}")
        fruit_count[prediction[0]] += 1

        return {"Predicted Fruit": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def log_fruit_count():
    while True:
        # Log the fruit count
        logging.info(f"Fruit count: {fruit_count}")
        # Reset the fruit count
        fruit_count["apple"] = 0
        fruit_count["banana"] = 0
        # Wait for 30 seconds before logging again
        time.sleep(30)


if __name__ == "__main__":

    thread = threading.Thread(target=log_fruit_count)
    thread.start()

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
