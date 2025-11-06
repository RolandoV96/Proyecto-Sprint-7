import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

build_histogram = st.checkbox('Construir un histograma') #crea un checkbox

if build_histogram: # si el checkbox esta seleccionado
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)