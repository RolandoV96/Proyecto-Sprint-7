import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Relation Between price/kilometers')

scat_button = st.button('Scatter diagram') # crear un botón
build_histogram = st.button('histogram diagram') #crea un checkbox

data = np.random.randn(1000)
df = pd.DataFrame({'value': data})

# 2. Definir los rangos y colores
# Puedes definir los rangos de forma personalizada.
# Aquí creamos rangos de ejemplo:
df['range'] = pd.cut(df['value'], bins=[-3, -1, 0, 1, 3], labels=['Muy bajo', 'Bajo', 'Medio', 'Alto'])

# 3. Crear el histograma con colores por rango
fig = px.histogram(df, x="value", color="range",
                   color_discrete_map={
                       'Muy bajo': 'red',
                       'Bajo': 'orange',
                       'Medio': 'yellow',
                       'Alto': 'green'
                   },
                   title="Histograma con colores por rango"
                  )

# 4. Mostrar el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

if build_histogram: # si el checkbox esta seleccionado
         # escribir un mensaje
         st.write('Amount of Cars by their odometer count')
         
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

