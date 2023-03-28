import io

import cv2
import joblib
import numpy as np
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import Location

location: Location = Location()

# Load the saved model
with open(location.model, "rb") as f:
    model = joblib.load(f)

with open(location.scaler, "rb") as f:
    scaler = joblib.load(f)

# Create a FastAPI app
app = FastAPI(title="Fruit Classifier API")


class Img(BaseModel):
    img_path: str


# Define an API endpoint
@app.post("/predict", status_code=200)
async def predict(request: Img):

    try:
        # Load image
        image = cv2.imread(request.img_path, cv2.IMREAD_COLOR)
        # Preprocess the image
        image = cv2.resize(image, (100, 100))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)

        # Flatten the image
        image_flat = image.flatten()

        # Scale the flattened image data
        image_scaled = scaler.transform([image_flat])

        # Make predictions on the image data
        prediction = model.predict(image_scaled)

        # Return the predictions as a JSON response
        return {"predicted fruit": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
