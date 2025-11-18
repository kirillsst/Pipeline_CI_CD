import streamlit as st
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("streamlit_app")

logger.info("Streamlit started")
st.title("Iris Flower Classifier 🌸")

st.write("Entrez les caractéristiques de la fleur d'iris :")

sepal_length = st.number_input("Sepal length (cm)", 0.0, 10.0, 5.1)
sepal_width  = st.number_input("Sepal width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal length (cm)", 0.0, 10.0, 1.4)
petal_width  = st.number_input("Petal width (cm)", 0.0, 10.0, 0.2)

API_URL = "http://127.0.0.1:8000/predict"

if st.button("Predict"):
    payload = {"values": [sepal_length, sepal_width, petal_length, petal_width]}
    logger.info(f"Loading from URL API: {API_URL}")
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        
        st.success(f"Classe prédite: {data['class_name']} ({data['class_index']})")
        
        if "probabilities" in data:
            st.write("Probabilités par classe :")
            for idx, prob in enumerate(data["probabilities"]):
                st.write(f"{idx}: {prob:.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de requête API : {e}")

## run 
# streamlit run app/streamlit_app.py
