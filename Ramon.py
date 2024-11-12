import streamlit as st
import pandas as pd
import dabest

# Carregar o arquivo CSV
st.title("Análise de Dados com Dabest")
uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV
    data = pd.read_csv(uploaded_file)

    # Carregar os dados no Dabest
    dabest_data = dabest.load(data=data, x="Trial", y="Angulo", idx=(
            "Baseline", "T1", "T2", "T3", "T4"))

    # Plotar o gráfico de estimação
    st.write("Plotando o gráfico de estimação:")
    fig = dabest_data.mean_diff.plot(raw_ylim=(80, 100),
    contrast_ylim=(-10, 10))
    st.pyplot(fig)
else:
    st.info("Por favor, faça o upload de um arquivo CSV.")
