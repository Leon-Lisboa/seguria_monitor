import streamlit as st
import pandas as pd
import requests

st.title("🔍 Monitoramento de Segurança com IA")

data_input = st.text_area("Insira os dados de log (formato JSON):")

if st.button("Enviar para análise"):
    try:
        data_dict = eval(data_input)
        response = requests.post("http://localhost:8000/monitor", json=data_dict)
        result = response.json()
        st.success("Análise realizada")
        st.write(result)
    except Exception as e:
        st.error(f"Erro: {e}")