from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from .model_loader import load_model

app = FastAPI()
model = load_model()

CLASS_NAMES = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

class IrisInput(BaseModel):
    values: list[float]

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: IrisInput):
    X = np.array(data.values).reshape(1, -1)
    pred_class = int(model.predict(X)[0])
    pred_name = CLASS_NAMES[pred_class]
    return {
        "class_index": pred_class,
        "class_name": pred_name
    }

## run 
# uvicorn app.main:app --reload