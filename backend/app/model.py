import mlflow
from functools import lru_cache

db = mlflow.set_tracking_uri("sqlite:///mlflow.db")

@lru_cache()
def load_model():
    """
    Nous mettons le modèle en cache afin de ne pas le charger à chaque requête.
    """
    print("Loading model from MLflow...")
    return mlflow.sklearn.load_model(db)
