import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import mlflow
import joblib
import os
from backend.app.core.logger import get_logger

logger = get_logger(__name__) 

MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("my-first-experiment")
mlflow.sklearn.autolog()


def train_and_save_model():
    # Load Iris dataset
    logger.info("Loading Iris dataset")
    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    params = {
        "solver": "lbfgs",
        "max_iter": 1000,
        "multi_class": "auto",
        "random_state": 8888,
    }

    logger.info(f"Training with params: {params}")

    with mlflow.start_run() as run:
        lr = LogisticRegression(**params)
        lr.fit(X_train, y_train)

        # MLflow autologged model URI
        model_uri = f"runs:/{run.info.run_id}/model"
        logger.info(f"Model stored in MLflow: {model_uri}")

    # Load model to check autologged save
    loaded_model = mlflow.sklearn.load_model(model_uri)

    # Predictions
    predictions = loaded_model.predict(X_test)

    # Prepare results
    iris_feature_names = datasets.load_iris().feature_names
    result = pd.DataFrame(X_test, columns=iris_feature_names)
    result["actual_class"] = y_test
    result["predicted_class"] = predictions

    # Save model for API
    joblib.dump(lr, MODEL_PATH)
    print(f"Saved model.pkl in {MODEL_PATH}")

    return result, lr


if __name__ == "__main__":
    logger.info("Training script started")
    df, model = train_and_save_model()
    logger.info("Training script finished")
    print(df[:4])

## run python3 train_model.py
# for train your model



# run ui mlflow for create mlflow.db
# mlflow ui \
#   --backend-store-uri sqlite:///mlflow.db \
#   --default-artifact-root ./mlruns



