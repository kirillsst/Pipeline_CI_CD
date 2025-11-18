import os
import pytest
import joblib
from ml.train_model import train_and_save_model, MODEL_PATH

def test_train_and_save_model():
    # Lancement de l'entraînement du modèle
    result_df, model = train_and_save_model()

    # Vérifiez que le modèle a été conservé
    assert os.path.exists(MODEL_PATH), "model.pkl n'a pas été enregistré"

    # Vérification que l'objet modèle renvoyé est bien LogisticRegression
    from sklearn.linear_model import LogisticRegression
    assert isinstance(model, LogisticRegression), "Objet renvoyé non LogisticRegression"

    # Vérification de la structure du DataFrame avec les prédictions
    expected_columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "actual_class",
        "predicted_class"
    ]
    for col in expected_columns:
        assert col in result_df.columns, f"La colonne {col} est absente du DataFrame."

    # Vérifions que les prédictions ont la bonne taille
    assert len(result_df) == 30, "La taille du DataFrame avec l'échantillon de test est incorrecte."
    assert all(result_df["predicted_class"].isin([0, 1, 2])), "Valeurs incorrectes des prévisions"
