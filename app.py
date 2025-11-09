import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Relation Between price/kilometers')

scat_button = st.button('Scatter diagram') # crear un botón
build_histogram = st.button('histogram diagram') #crea un checkbox

if build_histogram: # si el checkbox esta seleccionado
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)


     
if scat_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

         fig_scat = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig_scat, use_container_width=True)