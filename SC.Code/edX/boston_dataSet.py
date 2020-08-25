#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Wed Aug 19 15:28:50 2020

@author: scelis

Regresión Lineal y Regresión Múltiple - BostonDataSet - 
"""

# London.py
from sklearn.datasets import load_boston
boston_dataSet = load_boston()
desc =  boston_dataSet.DESCR

# print("Describe el dataframe: boston_dataSet => ", desc)
print("Describe el dataframe: boston_dataSet => \n", desc[148:1225])

import pandas as pd

# boston_dataSet = load_boston()
# data = boston_dataSet.data
# features = boston_dataSet.feature_names
# df = pd.DataFrame(data, columns=features)

# ó

df = pd.DataFrame(boston_dataSet.data,columns=[boston_dataSet.feature_names])

# print(df)
df.describe()


# Crea la columna MEDV
df['MEDV'] = boston_dataSet.target[df.index]
df_summary = df.describe()
 
# (506, 14)
df.shape

# Lista la matriz de correlación -  [14 rows x 14 columns], 0)
df.corr(),df.index[0]
# ó
df.corr()
# ó
corr_pairs = df.corr()

#correlación de todas las variables vs la variable de respuesta/estudio
df.corr().iloc[13, 0:13].sort_values()
# ó
corr_pairs.iloc[13, 0:13].sort_values()


# Dibuja la matriz de correlación
import seaborn as  sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
#%matplotlib inline
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(),annot=True)
plt.show()

# para nuestro studio vamos a tomar: (lás más cercanas a -1 y 1)
    
# =============================================================================
# LSTAT     -0.737663
# RM         0.695360
# 
# =============================================================================
# Correlación positiva => > 0 , aumenta una variable por tanto aumenta la otra.
# ex: RM vs MDEV
# Correlación negativa => < 0, aumenta una variable y disminuye la otra.
# ex: LSTAT vs MDEV

# DataFrame - [506 rows x 1 columns]
X = df.loc[df.index[0:506], ['LSTAT']]
print(X)

y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
X = boston_dataSet.data[df.index[0:506],[12]].reshape(-1,1)
# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array


# boston_dataSet.py => calculo del modelo de regresión lineal 
# Cuadrados mínimos ordinarios Regresión lineal
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal lm
lm = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lm.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.5419571999998836, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lm.coef_

lm.intercept_

y_train_pred = lm.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lm.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5472683211519955
# Prueba 0.5330003840140722

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)

# Graficamos 
import matplotlib.pyplot as plt
import numpy as np

# Le decimos a python que grafique en el mismo fichero
# Mute inline plotting

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# En X_plot guardamos valores distribuidos entre 0 y 40
# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,40).reshape(-1, 1) # ordenados por columna
# print(X_plot)

X_plot = np.linspace(0,40).reshape(1, -1) # ordenados por fila
# print(X_plot)

# Con el modelo predecimos X_plot
y_plot = lm.predict(X_plot)

# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--")

# ================================================================
# Que pasaría si intentamos utilizar múltiples variables independientes en el mismo modelo.

# Redefinimos la variable X como un subconjunto de datos: DataFrame - [506 rows x 1 columns]
# [506 rows x 2 columns]
X = df.loc[df.index[0:506], ['LSTAT', 'AGE']]
print(X)

# [506 rows x 1 columns]
y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df.iloc[df.index[0:506], [6,12]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array


# boston_dataSet.py => calculo del modelo de regresión lineal 
# Cuadrados mínimos ordinarios Regresión lineal
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal múltiple (lmm)
lmm = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lmm.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.548590009185747, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lmm.coef_

lmm.intercept_

y_train_pred = lmm.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5520920948986159
# Prueba 0.5426647322726053

# Vemos que no hay mucha diferencia entre los dos modelos

# ----------------

# [506 rows x 2 columns]
X = df.loc[df.index[0:506], ['RM', 'AGE']]
print(X)

# [506 rows x 1 columns]
y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df.iloc[df.index[0:506], [5,6]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array


# boston_dataSet.py => calculo del modelo de regresión multiple 
# Cuadrados mínimos ordinarios Regresión lineal
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal múltiple (lmm)
lmm2 = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lmm2.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.5291686548306225, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lmm2.coef_

lmm2.intercept_

y_train_pred = lmm2.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm2.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5480820218090987
# Prueba 0.49742229782888514

# Vemos que ha empeorado un poco 

# ----------------

# [506 rows x 2 columns]
X = df.loc[df.index[0:506], ['RM', 'LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df.iloc[df.index[0:506], [5,12]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array

# boston_dataSet.py => calculo del modelo de regresión multiple 
# Cuadrados mínimos ordinarios Regresión lineal
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal múltiple (lmm)
lmm3 = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lmm3.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.5291686548306225, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lmm3.coef_

lmm3.intercept_

y_train_pred = lmm3.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm3.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.6453978719945989
# Prueba 0.620475389449678

# Vemos que ha mejorado el modelo 

# ----------------

# [506 rows x 12 columns]
X = df.loc[df.index[0:506],['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df.drop('MEDV', axis=1) # Eliminamos la columna de respuesta

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array

# boston_dataSet.py => calculo del modelo de regresión multiple 
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal múltiple (lmm)
lmm4 = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lmm4.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.7355053338711364, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lmm4.coef_

lmm4.intercept_

y_train_pred = lmm4.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm4.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.7581323045862294
# Prueba 0.6975641751193842

# Vemos que ha mejorado el modelo utilizando todas las columnas


# ----------------

# [506 rows x 12 columns]
X = df.loc[df.index[0:506],['CRIM','ZN','INDUS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df.loc[df.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df.drop(['MEDV', 'CHAS'], axis=1) # Eliminamos la columna de respuesta

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df.index].reshape(-1,1)

# Creamos el split de datos - dividir los conjuntos o matrices en trenes aleatorios y subconjuntos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # p primeros datos del array

# boston_dataSet.py => calculo del modelo de regresión multiple 
from sklearn.linear_model import LinearRegression

# Creando el modelo de regresion líneal múltiple (lmm)
lmm5 = LinearRegression().fit(X_train,y_train) # ajustar el modelo lineal
lmm5.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un modelo es 0.7306812298857916, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del modelo.

# Coeficientes
lmm5.coef_

lmm5.intercept_

y_train_pred = lmm5.predict(X_train) # Predice usando el modelo lineal con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm5.predict(X_test) # Predice usando el modelo lineal con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.7522680521704352
# Prueba 0.6944820133786174

# Vemos que no hay mucha diferencia quitando una variable que no está muy correlacionada

