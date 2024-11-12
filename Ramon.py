import streamlit as st
import pandas as pd
import dabest
import matplotlib.pyplot as plt

# Configurar o título da aplicação
st.title("Análise de Dados com Dabest")

# Fazer o upload do arquivo CSV
uploaded_file = st.file_uploader("Faça o upload de um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV
    data = pd.read_csv(uploaded_file)

    # Exibir os primeiros dados para visualização
    st.write("Dados carregados:")
    st.write(data.head())

    # Carregar os dados no Dabest
    try:
        dabest_data = dabest.load(data=data, x="Trial", y="Angulo", idx=(
                "Baseline", "T1", "T2", "T3", "T4"))

        # Plotar o gráfico de estimação
        st.write("Plotando o gráfico de estimação:")
        fig, ax = plt.subplots()
        dabest_data.mean_diff.plot(ax=ax)
        #ax.set_ylim(-4, 6)  # Ajusta os limites do eixo y

        # Exibir o gráfico no Streamlit
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
else:
    st.info("Por favor, faça o upload de um arquivo CSV.")
