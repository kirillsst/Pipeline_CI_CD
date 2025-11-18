import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import mlflow
import joblib
import os 

MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("my-first-experiment")
mlflow.sklearn.autolog()

# Load Iris dataset
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

with mlflow.start_run() as run:
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # Construct the correct model URI for autologged model
    model_uri = f"runs:/{run.info.run_id}/model"

# Load the model
loaded_model = mlflow.sklearn.load_model(model_uri)

# Predict
predictions = loaded_model.predict(X_test)

# Prepare results
iris_feature_names = datasets.load_iris().feature_names
result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

joblib.dump(lr, MODEL_PATH)
print(f"Saved model.pkl in {MODEL_PATH}")


print(result[:4])


# run ui mlflow
# mlflow ui \
#   --backend-store-uri sqlite:///mlflow.db \
#   --default-artifact-root ./mlruns
