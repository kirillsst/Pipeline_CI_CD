### Instructions for manually running all components of the project on your local machine.

# 1. MLflow UI
##### What it does: lets you inspect artifacts, metrics, and other logs created during model training.cript: train_model.py
* mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns
* MLflow UI is available at: http://127.0.0.1:5000
____________________________________________________________________________________________________________________________
# 2. Train the Model
##### Script: train_model.py
##### What it does: loads the Iris dataset, trains a Logistic Regression model, saves the model to ml/model/model.pkl, and logs metrics and artifacts to MLflow.
* ~/Pipeline_CI_CD/backend/ml$ python3 train_model.py
____________________________________________________________________________________________________________________________
# 3. Start the API
##### Script: backend/app/main.py (FastAPI)
##### What it does: starts the API with two endpoints:
##### *GET /* – health check, returns *{"status": "ok"}*
##### *POST /predict* – accepts input data and returns the predicted Iris class.
* ~/Pipeline_CI_CD/backend$ uvicorn app.main:app --reload
* API is available at: http://127.0.0.1:8000
____________________________________________________________________________________________________________________________
# 4. Launch Streamlit
##### Script: app/dashboard.py
##### What it does: visualizes predictions.
* ~/Pipeline_CI_CD/fontend$ streamlit run app.py
