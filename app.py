import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir el histograma
hist_button = st.button('Construir histograma') 

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el gráfico de dispersión (ajustar las columnas según tus datos)
    fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Precio")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)


