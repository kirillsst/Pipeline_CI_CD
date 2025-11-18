from fastapi import FastAPI
from app.schemas import PredictRequest
from app.model import load_model
import numpy as np

app = FastAPI(title="ML Prediction API")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictRequest):
    model = load_model()

    data = np.array(payload.values).reshape(1, -1)

    prediction = model.predict(data)

    return {"prediction": prediction.tolist()}
