import streamlit as st
import pandas as pd
import dabest

# Carregar o arquivo CSV
st.title("Análise de Dados com Dabest")
uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV
    data = pd.read_csv(uploaded_file)

    # Verificar se o arquivo possui 5 colunas numéricas
    if len(data.columns) == 5:
        # Separar cada coluna em uma variável
        col1 = data.iloc[:, 0]
        col2 = data.iloc[:, 1]
        col3 = data.iloc[:, 2]
        col4 = data.iloc[:, 3]
        col5 = data.iloc[:, 4]

        # Carregar os dados no Dabest
        dabest_data = dabest.load(data=data, x="Condição", y="Angulo", idx=(
            "Baseline", "T1", "T2", "T3", "T4"))

        # Plotar o gráfico de estimação
        st.write("Plotando o gráfico de estimação:")
        fig = dabest_data.mean_diff.plot()
        st.pyplot(fig)

    else:
        st.error("O arquivo deve conter exatamente 5 colunas numéricas.")
else:
    st.info("Por favor, faça o upload de um arquivo CSV.")
