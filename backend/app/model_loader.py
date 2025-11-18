import joblib
import os
from .core.logger import get_logger

logger = get_logger(__name__)
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ml", "model", "model.pkl")

def load_model():
    logger.info(f"Loading model from: {MODEL_PATH}")
    if not os.path.exists(MODEL_PATH):
        logger.error(f"Model file not found: {MODEL_PATH}")
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    try:
        model = joblib.load(MODEL_PATH)
        logger.info("Model successfully loaded.")
        return model

    except Exception as e:
        logger.exception(f"Failed to load model: {e}")
        raise
