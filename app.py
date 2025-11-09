import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Relation Between price/kilometers')

scat_button = st.button('Scatter diagram') # crear un botón
build_histogram = st.button('histogram diagram') #crea un checkbox

car_data['level'] = pd.cut(car_data['odometer'], # corta los datos dependiendo los valores de odometro
                           bins=[0, 59999, 74999, 89999, 105000, 999999], # los acomoda en estas secciones
                           labels=['Low', 'Medium', 'High', 'Really High','Extremly high'] # le coloca el siguiente label como una columna extra
                           )

if build_histogram: # si el checkbox esta seleccionado
         # escribir un mensaje
         st.write('Amount of Cars by their odometer count')
         
         # crear un histograma con colores dependiendo su nivel de kilometraje
         fig = px.histogram(car_data, x="odometer", color="level",
                   color_discrete_map={
                       'Low': 'green',
                       'Medium': 'yellow',
                       'High': 'orange',
                       'Really High': 'red',
                       'Extremly high' : 'black'
                   }
                  )
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)


     
if scat_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Scatter Diagram showing the relation between the odometer and price of used cars')

         fig_scat = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig_scat, use_container_width=True)

