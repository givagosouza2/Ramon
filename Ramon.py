import streamlit as st
import pandas as pd
import dabest
import matplotlib.pyplot as plt

# Título da Aplicação
st.title("Análise de Dados com DABEST")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV
    data = pd.read_csv(uploaded_file)

    # Verificar se as colunas necessárias estão presentes
    if 'Trial' not in data.columns or 'Angulo' not in data.columns:
        st.error("O arquivo CSV deve conter as colunas 'Trial' e 'Angulo'.")
    else:
        # Seleção dos limites do eixo Y
        raw_ylim = st.slider("Limite do eixo Y (dados brutos)", 0, 150, (80, 100))
        contrast_ylim = st.slider("Limite do eixo Y (diferença)", -20, 20, (-10, 10))

        # Carregar os dados no DABEST
        dabest_data = dabest.load(data=data, x="Trial", y="Angulo", idx=(
            "Baseline", "T1", "T2", "T3", "T4"))

        # Plotar o gráfico de estimação
        st.write("Plotando o gráfico de estimação:")
        fig = dabest_data.mean_diff.plt()
        plt.ylim(-10,10))      
        st.pyplot(fig)
        
        fig = dabest_data.value.plt()
        plt.ylim(80,100))      
        st.pyplot(fig)
else:
    st.info("Por favor, faça o upload de um arquivo CSV.")

