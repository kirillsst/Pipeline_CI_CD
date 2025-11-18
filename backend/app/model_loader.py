import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ml", "model", "model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)
