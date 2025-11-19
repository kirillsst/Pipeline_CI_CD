from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'API is working'}

def test_predict():
    payload = {"values": [5.1, 3.5, 1.4, 0.2]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "class_index" in data
    assert "class_name" in data
