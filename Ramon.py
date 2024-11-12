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
        
        dabest_data = dabest.load(data, idx=(("Baseline 1", "T1-W", "T2-W", "T3-W","T4-W"),
                                                      ("Baseline 2", "T1-S", "T2-S", "T4-S","T4-S")),paired="baseline")

        # Plotar o gráfico de estimação
        st.write("Plotando o gráfico de estimação:")
        fig = dabest_data.mean_diff.plot()
        plt.ylim(-10,10)      
        st.pyplot(fig)
else:
    st.info("Por favor, faça o upload de um arquivo CSV.")

