import mlflow 

experiment = mlflow.set_experiment(experiment_name="my-first-experiment")
mlflow.set_experiment("my-first-experiment")

# Print connection information
print(f"MLflow Tracking URI: {mlflow.get_tracking_uri()}")
print(f"Active Experiment: {mlflow.get_experiment_by_name('my-first-experiment')}")

# Test logging
with mlflow.start_run():
    mlflow.log_param("test_param", "test_value")
    print("✓ Successfully connected to MLflow!")

# run command mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000