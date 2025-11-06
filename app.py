import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write('Favor de seleccionar que tipo de grafico mostrar') # instrucciones para la app
build_histogram = st.checkbox('Construir un histograma') #crea un checkbox
scat_button = st.button('Construir histograma') # crear un botón

if build_histogram: # si el checkbox esta seleccionado
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig_hist = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(         fig_hist = px.histogram(car_data, x="odometer")
, use_container_width=True)
   
if scat_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig_scatter = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(scat_button, use_container_width=True)