import numpy as np
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Título
st.title("Precio de la gasolina")
#Encabezado
st.header("Calcular el precio de la gasolina con base en el año, mes y entidad")

# Imagen
st.image("precio_gasolina.jpeg", caption="Precio de la gasolina")

# Deslizadores
mes = st.sidebar.slider('Mes', 1, 12)
anio = st.sidebar.slider('Año', 2017, 2075)
entity = st.sidebar.slider('Entidad', 0, 31)
data =  pd.read_csv('gasolina_regular.csv', encoding='latin-1')
Xm = pd.DataFrame(data, columns=['Entidad', 'Mes', 'Anio'])
ym = data['Valor']

Xm_train, Xm_test, ym_train, ym_test = train_test_split(Xm, ym, test_size=0.30, random_state=0)
ym_train

LRm = LinearRegression()
LRm.fit(Xm_train,ym_train)

bm = LRm.coef_
b0m = LRm.intercept_

# bm[0] = pendiente de la entidad
# bm[1] = pendiente del mes
# bm[2] = pendiente del año
pred = b0m + bm[0]*entity + bm[1]*mes + bm[2]*anio


# Botones
boton_calcular = st.button("Calcular")

st.write('El precio mensual de la gasolina regular es de:', pred)

if boton_calcular:
    st.write(f'La suma es: {pred}')
