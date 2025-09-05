import pandas as pd
import plotly.express as px
import streamlit as st

# Titulo do APP
st.header("📊 Dashboard de Anúncios de Carros")

# Carrega o Dataset
car_data = pd.read_csv("vehicles_us.csv")

# Botao para o Histograma
hist_button = st.checkbox("Criar Histograma")

if hist_button:
    st.write(
        "Criando um histograma para o conjunto de dados de anúncios de vendas de carro")

    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox("Criar gráfico de dispersão")

if scatter_button:  # se o botão for clicado
    st.write("Criando um gráfico de dispersão (Preço vs Quilometragem)")

    # criar scatter (odometer x price)
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # exibir o gráfico Plotly interativo
    st.plotly_chart(fig2, use_container_width=True)
