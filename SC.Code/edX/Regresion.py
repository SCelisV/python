"""
IN-WORK-OUT
@author: scelis - ¯\_(ツ)_/¯

Regresion.py

Is the process of predicting a continuos value - valor continuo

Aprendizaje supervisado, Método matemático que modela la relación entre una variable dependiente "y" y una ó varias variables independientes "x" por medio de una expresión líneal que busca asemejarse a en medida de lo posible a los datos reales.

La clave de la regresión es que nuestro valor dependiente debe ser continuo, y no puede ser un valor discreto.

Una variable dependiente (Y) es el "estado", "resultado", "objetivo", de estudio y predicción, valores continuos.

Una variable independientes (X) ó explicativas, son la "causa" de ese "estado ó objetivo", pueden estar en escala de medición categorica ó continua.

Aproximación de un modelo lineal que se utiliza para describir la relación entre dos ó más variables.

En resumen podemos decir que utilizamos datos historicos y a partir de ellos se hace un modelo, para predecir un resultado nuevo ó desconocido.

    -.- Simple Regression, se utiliza una variable independiente para estimar una variable dependiente.
        - Regresión líneal: (Simple Linear Regression).

        - Regresión NO líneal: (Simple Non-Linear Regression)

        La linealidad de la regresión se basa en la naturaleza de la relación entre la independencia y la dependencia. (Predict co2 emisions vs Engine Size of all cars)

    -.- Multiple Regression
        - Multiple Linear Regression
        - Multiple Non-linear Regression

        Hay más de una variable independiente presente. (Predict co2emisions vs EngineSize and Cylinders of all cars)
        En función de la relación entre las variable dependiente e independientes, puede ser linear or no linear.

    Applications: 
    Sales forecasting. Previsión de ventas. - Predecir las ventas anuales totales de un vendedor a partir de variables independientes como edad, educación, años de experiencia.
    Satisfaction analysis. Analisis de Satisfacción. - Determinar la satisfacción individual basado en factores demográficos y psicológicos.
    Price estimation. Estimación de precios. - Predecir el precio de una casa en un área, basado en su tamaño, número de habitaciones.
    Employment income. Ingreso de empleo. - Predecir los ingresos para las variables independientes, como las horas de trabajo, educación, ocupación, sexo, edad, años de experiencia...etc.
    Drug response, Stock prices, Finanzas, Salud.
    
    - Ordinal regression
    - Poisson regression
    - Fast forest quantile regression
    - Linear, Polynomial, Lasso, Stepwise, Ridge regression
    - Bayesian linear regression
    - Neural network regression
    - Decision fores regression
    - Boosted decision tree regression
    - KNN (K-nearest neighbors)

.-. Simple Linear Regression: Variables: 
                                    1 (y) dependiente(continua): co2 emission
                                    1 (x) independiente: Engine Size


.-. Multiple Linear Regression: Variables: 
                                    1 (y) dependiente(continua): co2 emission
                                    1 ó más variables (y) independientes. Engine Size and Cylinders



Linear Regression. Regresión Lineal.
Para entender la regresion lineal, debemos trazar las variables por medio de un Scatter-plot (Diagrama de dispersion)
Los cambios de una variable explican el comportamiento de la otra
Indican la relacion lineal entre las variables
Con la regresion lineal se puede ajustar una línea a traveś de los datos

EngineSize -> variable independiente
co2emisions -> variable dependiente ó objetivo.

A medida que aumenta el EngineSize también aumenta las co2emisions

Un buen modelo de esta relacion (recta), nos servirá para predecir el valor de emisiones de un nuevo tamaño de motor

Esta línea es un polinomio de una sóla variable.

La regresion lineal estima los coeficientes de la línea, de tal manera que encontremos la mejor línea para i"ajustar" los datos.
Esta línea estimaría mejor la emisión de los data points desconocidos

Para encontrar el mejor modelo, comparamos:
    el valor real de la emisión de un coche vs
    el valor de la prediccion de la emisión de ese coche

Esa diferencia es el Error residual del modelo, es decir que la línea no es precisa.

Es decir el error es la distancia desde el punto de datos hasta la línea de regresión ajustada.

La medida de todos los errores residuales muestra lo mal que encaja la línea con todo el conjunto de datos.

MSE -> error de cuadrado medio

El objetivo del modelo es encontrar una línea que minimice la media de todos estos errores, es decir, 
el error medio de la predicción utilizando la línea de ajuste debe minimizarse.

Minimizar la ecuación de MSE y para ello se deben encontrar los mejores parámetros para la ecuación que define la recta.

    Podemos usar una simple ecuación para estimar estos coeficientes de ajuste de la recta.
    sabiendo que uno de ellos es la intercepción y el otro la pendiente de la recta.
    Podemos estimarlos directamente a partir de los datos.
    Se requiere que calculemos la media de las columnas independientes y dependientes.

Dibujará una recta y=mx+b => que nos indicará la tendencia del conjunto de datos, y nos ayudará a predecir en función de un valor X un valor Y. 
# y => coordenada Y, variable dependiente
# m => pendiente
# x => coordenada X, variable independiente
# b => Ordenada en el Origen, intercepción, el punto Y donde la línea cruza el eje Y, relación X,Y

Este tipo de regresión es la más básica y fácil de entender, es rápida, no se requiere ajuste de parámetros.
Es fácil de interpretar.

El objetivo de la regresión es crear un modelo para predecir "con precisión" un caso desconocido.
por tanto se debe realizar una evaluación del modelo.

Metricas para la precisión de los modelos de regresión

1. Train and Test en el mismo dataset:
    Utilizar todo el dataset para el entrenamiento y construir el modelo usando este conjunto de entrenamiento.
    Seleccionar una pequeña porción del dataset sin etiquetas, estas no se utilizan para la predicción sino para valores reales, del conjunto de pruebas.
    pasamos estas variables al modelo objetivo y predecimos los valores de destino.
    Comparamos estos valores con los valores actuales de dataset.
    Se calcula el error promedio de los valores calculados vs los valores del dataset.
    Precisión de formación: porcentaje de predicciones correctas que se hace el modelo cuando se utiliza el dataset de prueba.
    No es necesariamente algo bueno ya que puede significar un sobreajuste de los datos (over-fitting), es decir, 
    el modelo esta demasiado formado en el dataset, y se puede capturar ruido y producir un modelo No generalizado.
        
    Precisión de fuera de la muestra:
    Es el porcentaje de las predicciones correctas en las que el modelo realiza sobre datos en los que NO ha sido formado el modelo.
    
    Probablemente esta opción tendrá una precisión baja fuera de la muestra.
           
2. División del dataset en Train and Test:
    Seleccionamos una parte del dataset para formación y el resto para testing.
    El modelo se basa en el conjunto de formación.
    Entonces, el conjunto de caracteristicas de prueba se pasa al modelo para la predicción,
    Y finalmente los valores pronosticados para el conjunto de pruebas se comparan con los valores reales.
    Implica la división del dataSet en conjuntos de train and test, mutuamente excluyentes, después de lo cual, se forman con el conjunto de formación y se prueban respectivamente
    Esto proporcinará una evaluación más precisa sobre la precisión de fuera de la muestra, ya que la prueba del dataset no forma parte del entrenamiento.
    Más realistia para el mundo real.
    El modelo no conoce estos datos por tanto realmente es una prueba de la muestra.
    Sin embargo forme el modelo con el conjunto de daos de prueba.
    Altamente dependiente de los datos del dataset.
    
3. k-fold- Cross Validation:
    Separar el dataset en varias partes, y calcular la precisión en cada una de estas
    - primer 25% para test y el resto para training
    - segundo 25% para test y el resto para training
    - tercer 25% para test y el resto para training
    - cuarto 25% para test y el resto para training
    Al final se saca un promedio de estas precisiones, teniendo en cuenta que cada parte es distinta,
    no se usa ningún dato de training en varias partes.

"""
"""
    -.- Simple  Regression

# ==========================
# Ejemplo con dataSet Boston
# ==========================

"""

from sklearn.datasets import load_boston
boston_dataSet = load_boston()
desc =  boston_dataSet.DESCR

# print("Describe el dataframe: boston_dataSet => ", desc)
print("Describe el dataframe: boston_dataSet => \n", desc[148:1225])

import pandas as pd

# Create el data frame

# data = boston_dataSet.data
# features = boston_dataSet.feature_names
# df_Boston = pd.DataFrame(data, columns=features)

# ó

df_Boston = pd.DataFrame(boston_dataSet.data,columns=[boston_dataSet.feature_names])

# print(df_Boston)

df_Boston.describe()

#              CRIM          ZN       INDUS  ...     PTRATIO           B       LSTAT
# count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  506.000000
# mean     3.613524   11.363636   11.136779  ...   18.455534  356.674032   12.653063
# std      8.601545   23.322453    6.860353  ...    2.164946   91.294864    7.141062
# min      0.006320    0.000000    0.460000  ...   12.600000    0.320000    1.730000
# 25%      0.082045    0.000000    5.190000  ...   17.400000  375.377500    6.950000
# 50%      0.256510    0.000000    9.690000  ...   19.050000  391.440000   11.360000
# 75%      3.677083   12.500000   18.100000  ...   20.200000  396.225000   16.955000
# max     88.976200  100.000000   27.740000  ...   22.000000  396.900000   37.970000

# [8 rows x 13 columns]

# Crea la columna MEDV
df_Boston['MEDV'] = boston_dataSet.target[df_Boston.index]
df_Boston_summary = df_Boston.describe()

#              CRIM          ZN       INDUS  ...           B       LSTAT        MEDV
# count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  506.000000
# mean     3.613524   11.363636   11.136779  ...  356.674032   12.653063   22.532806
# std      8.601545   23.322453    6.860353  ...   91.294864    7.141062    9.197104
# min      0.006320    0.000000    0.460000  ...    0.320000    1.730000    5.000000
# 25%      0.082045    0.000000    5.190000  ...  375.377500    6.950000   17.025000
# 50%      0.256510    0.000000    9.690000  ...  391.440000   11.360000   21.200000
# 75%      3.677083   12.500000   18.100000  ...  396.225000   16.955000   25.000000
# max     88.976200  100.000000   27.740000  ...  396.900000   37.970000   50.000000

# [8 rows x 14 columns]

# Return una tupla de dimensiones (506, 14)
df_Boston.shape

# Lista la matriz de correlación -  [14 rows x 14 columns], 0)
df_Boston.corr(),df_Boston.index[0]
# ó
df_Boston.corr()
#              CRIM        ZN     INDUS  ...         B     LSTAT      MEDV
# CRIM     1.000000 -0.200469  0.406583  ... -0.385064  0.455621 -0.388305
# ZN      -0.200469  1.000000 -0.533828  ...  0.175520 -0.412995  0.360445
# INDUS    0.406583 -0.533828  1.000000  ... -0.356977  0.603800 -0.483725
# CHAS    -0.055892 -0.042697  0.062938  ...  0.048788 -0.053929  0.175260
# NOX      0.420972 -0.516604  0.763651  ... -0.380051  0.590879 -0.427321
# RM      -0.219247  0.311991 -0.391676  ...  0.128069 -0.613808  0.695360
# AGE      0.352734 -0.569537  0.644779  ... -0.273534  0.602339 -0.376955
# DIS     -0.379670  0.664408 -0.708027  ...  0.291512 -0.496996  0.249929
# RAD      0.625505 -0.311948  0.595129  ... -0.444413  0.488676 -0.381626
# TAX      0.582764 -0.314563  0.720760  ... -0.441808  0.543993 -0.468536
# PTRATIO  0.289946 -0.391679  0.383248  ... -0.177383  0.374044 -0.507787
# B       -0.385064  0.175520 -0.356977  ...  1.000000 -0.366087  0.333461
# LSTAT    0.455621 -0.412995  0.603800  ... -0.366087  1.000000 -0.737663
# MEDV    -0.388305  0.360445 -0.483725  ...  0.333461 -0.737663  1.000000

# [14 rows x 14 columns]

# crea un dataframe con los datos de la matriz de correlación
df_Boston_corr_pairs = df_Boston.corr()

# correlación ordenadas de todas las variables vs la variable de respuesta/estudio
df_Boston_corr_pairs.iloc[13, 0:13].sort_values()

# ó
df_Boston.corr().iloc[13, 0:13].sort_values()
# LSTAT     -0.737663
# PTRATIO   -0.507787
# INDUS     -0.483725
# TAX       -0.468536
# NOX       -0.427321
# CRIM      -0.388305
# RAD       -0.381626
# AGE       -0.376955
# CHAS       0.175260
# DIS        0.249929
# B          0.333461
# ZN         0.360445
# RM         0.695360
# Name: (MEDV,), dtype: float64

# Dibuja la matriz de correlación
import seaborn as  sns
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)
plt.figure(figsize=(12, 10))
sns.heatmap(df_Boston.corr(),annot=True)
plt.show()

# para nuestro studio vamos a tomar las variables con la correlación más cercana a -1 y 1 respectivamente.

# ========================
# LSTAT     -0.737663
# ========================
# Correlación negativa => < 0, aumenta una variable y disminuye la otra.
# ex: LSTAT vs MDEV

# DataFrame - [506 rows x 1 columns] - Definimos nuestra variable independiente
X = df_Boston.loc[df_Boston.index[0:506], ['LSTAT']]
print(X)

# DataFrame - [506 rows x 1 columns] - Definimos nuestras variable dependiente
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

plt.scatter(X, y,  color='green')
plt.xlabel("LSTAT")
plt.ylabel("MDEV")
plt.show()

# Definimos cuales son nuestras variables dependientes e independientes

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
# todas las filas de una columna de todo el dataSet
X = boston_dataSet.data[df_Boston.index[0:506],[12]].reshape(-1,1) 

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
# todas las filas de una columna de todo el dataSet
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)  

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. 
# Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
X_train[:5] #  primeros datos del array

# Cuadrados mínimos ordinarios Regresión líneal
from sklearn.linear_model import LinearRegression

# Crear el módelo de regresión líneal y entrenar
lm_Boston = LinearRegression().fit(X_train,y_train) 
# ajustar el módelo líneal
lm_Boston.score(X,y) 
# Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.5419571999998836, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lm_Boston.coef_
# array([[-0.88979169]])

lm_Boston.intercept_
# array([33.78869391])

# Predice usando el módelo líneal con los datos de entrenamiento
y_train_pred = lm_Boston.predict(X_train) 
type(y_train_pred)
print(y_train_pred[:5])

# Predice usando el módelo líneal con los datos de prueba
y_test_pred = lm_Boston.predict(X_test) 
print(y_test_pred[:5])

# Comparamos el r2 tanto para los datos de entrenamiento y sus predicciones
from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5472683211519955
# Prueba 0.5330003840140722

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 44.647754400183324

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

# ordenados por columna
X_plot = np.linspace(0,40).reshape(-1, 1) 
# print(X_plot)

# ordenados por fila - 
#X_plot = np.linspace(0,40).reshape(1, -1) 
# print(X_plot)

# Con el módelo predecimos X_plot
y_plot = lm_Boston.predict(X_plot)

# Graficamos el módelo
plt.plot(X_plot, y_plot,"r--")   

# ========================
# RM         0.695360
# ========================
# Correlación positiva => > 0 , aumenta una variable por tanto aumenta la otra.
# ex: RM vs MDEV

# DataFrame - [506 rows x 1 columns] - Definimos nuestra variable independiente
X = df_Boston.loc[df_Boston.index[0:506], ['RM']]
print(X)

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
# todas las filas de una columna de todo el dataSet
X = boston_dataSet.data[df_Boston.index[0:506],[5]].reshape(-1,1) 

# DataFrame - [506 rows x 1 columns] - Definimos nuestras variable dependiente
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

plt.scatter(X, y,  color='orange')
plt.xlabel("RM")
plt.ylabel("MDEV")
plt.show()

# Definimos cuales son nuestras variables dependientes e independientes

# Array of float -  [[4.98][9.14] ... [ 6.48][ 7.88]]
# todas las filas de una columna de todo el dataSet
X = boston_dataSet.data[df_Boston.index[0:506],[5]].reshape(-1,1) 

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
# todas las filas de una columna de todo el dataSet
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)  

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. 
# Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
X_train[:5] #  primeros datos del array

# Cuadrados mínimos ordinarios Regresión líneal
from sklearn.linear_model import LinearRegression

# Crear el módelo de regresión líneal y entrenar
lm2_Boston = LinearRegression().fit(X_train,y_train) 
# ajustar el módelo líneal
lm2_Boston.score(X,y) 
# Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.4823090772690438, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lm2_Boston.coef_
# array([[8.64906232]]

lm2_Boston.intercept_
# array([-31.86288286])

# Predice usando el módelo líneal con los datos de entrenamiento
y_train_pred = lm2_Boston.predict(X_train) 
type(y_train_pred)
print(y_train_pred[:5])

# Predice usando el módelo líneal con los datos de prueba
y_test_pred = lm2_Boston.predict(X_test) 
print(y_test_pred[:5])

# Comparamos el r2 tanto para los datos de entrenamiento y sus predicciones
from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.49622962949522476
# Prueba 0.45892115722284954

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 51.73013950439218

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

# ordenados por columna
X_plot = np.linspace(0,10).reshape(-1, 1) 
print(X_plot)

# ordenados por fila - 
# X_plot = np.linspace(0,40).reshape(1, -1) 
# print(X_plot)


# Con el módelo predecimos X_plot
y_plot = lm2_Boston.predict(X_plot)

# Graficamos el módelo
plt.plot(X_plot, y_plot,"r--")

# ========================

"""
# ===================================
# Ejemplo con dataSet FuelConsumption
# ===================================

data:    
!wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

Hemos descargado el dataset de consumo de combustible, 
FuelConsumption.csv, el cual contiene ratings específicos al consumo de combustible y emisiones de dióxido de carbono para aquellos vehículos ligeros en la venta minorista dentro de Canadá. 
https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64

- MODELYEAR e.g. 2014
- MAKE e.g. Acura
- MODEL e.g. ILX
- VEHICLE CLASS e.g. SUV
- ENGINE SIZE e.g. 4.7
- CYLINDERS e.g 6
- TRANSMISSION e.g. A6
- FUEL CONSUMPTION in CITY(L/100 km) e.g. 9.9
- FUEL CONSUMPTION in HWY (L/100 km) e.g. 8.9
- FUEL CONSUMPTION COMB (L/100 km) e.g. 9.2
- CO2 EMISSIONS (g/km) e.g. 182   --> low --> 0

"""
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df_FuelConsumption = pd.read_csv("FuelConsumption.csv")

df_FuelConsumption.head()
# [5 rows x 13 columns]

df_FuelConsumption.describe
# MODELYEAR   MAKE  ... FUELCONSUMPTION_COMB_MPG CO2EMISSIONS
# 0          2014  ACURA  ...                       33          196
# 1          2014  ACURA  ...                       29          221
# 2          2014  ACURA  ...                       48          136
# 3          2014  ACURA  ...                       25          255
# 4          2014  ACURA  ...                       27          244
#         ...    ...  ...                      ...          ...
# 1062       2014  VOLVO  ...                       24          271
# 1063       2014  VOLVO  ...                       25          264
# 1064       2014  VOLVO  ...                       24          271
# 1065       2014  VOLVO  ...                       25          260
# 1066       2014  VOLVO  ...                       22          294

# [1067 rows x 13 columns]

df_FuelConsumption.describe()
#        MODELYEAR   ENGINESIZE  ...  FUELCONSUMPTION_COMB_MPG  CO2EMISSIONS
# count     1067.0  1067.000000  ...               1067.000000   1067.000000
# mean      2014.0     3.346298  ...                 26.441425    256.228679
# std          0.0     1.415895  ...                  7.468702     63.372304
# min       2014.0     1.000000  ...                 11.000000    108.000000
# 25%       2014.0     2.000000  ...                 21.000000    207.000000
# 50%       2014.0     3.400000  ...                 26.000000    251.000000
# 75%       2014.0     4.300000  ...                 31.000000    294.000000
# max       2014.0     8.400000  ...                 60.000000    488.000000

# [8 rows x 8 columns]

# Extraemos algunas columnas
cdf_FuelConsumption = df_FuelConsumption [['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
      # ENGINESIZE  CYLINDERS  FUELCONSUMPTION_COMB  CO2EMISSIONS
# 0            2.0          4                   8.5           196
# 1            2.4          4                   9.6           221
# 2            1.5          4                   5.9           136
# 3            3.5          6                  11.1           255
# 4            3.5          6                  10.6           244
#          ...        ...                   ...           ...
# 1062         3.0          6                  11.8           271
# 1063         3.2          6                  11.5           264
# 1064         3.0          6                  11.8           271
# 1065         3.2          6                  11.3           260
# 1066         3.2          6                  12.8           294

# [1067 rows x 4 columns]

cdf_FuelConsumption.head(9)
#    ENGINESIZE  CYLINDERS  FUELCONSUMPTION_COMB  CO2EMISSIONS
# 0         2.0          4                   8.5           196
# 1         2.4          4                   9.6           221
# 2         1.5          4                   5.9           136
# 3         3.5          6                  11.1           255
# 4         3.5          6                  10.6           244
# 5         3.5          6                  10.0           230
# 6         3.5          6                  10.1           232
# 7         3.7          6                  11.1           255
# 8         3.7          6                  11.6           267

# Histograma de las variables seleccionadas
viz_FuelConsumption = cdf_FuelConsumption
viz_FuelConsumption.hist(color='green')
plt.show()

# Diagrama de dispersión de cada una de las variables vs CO2emission

plt.scatter(cdf_FuelConsumption.FUELCONSUMPTION_COMB, cdf_FuelConsumption.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf_FuelConsumption.ENGINESIZE, cdf_FuelConsumption.CO2EMISSIONS,  color='green')
plt.xlabel("ENGINESIZE")
plt.ylabel("Emission")
plt.show()

plt.scatter(cdf_FuelConsumption.CYLINDERS, cdf_FuelConsumption.CO2EMISSIONS,  color='orange')
plt.xlabel("CYLINDERS")
plt.ylabel("Emission")
plt.show()

# Crea un arreglo aleatorio con el 80% de los datos de todo el dataSet
msk = np.random.rand(len(df_FuelConsumption)) < 0.8
# Selecciona los True para entrenamiento
train_FuelConsumption = cdf_FuelConsumption[msk]
# Selecciona los False para prueba
test_FuelConsumption = cdf_FuelConsumption[~msk]

# Diagrama de dispersión del tamaño del motor comparado con las emisiones

plt.scatter(train_FuelConsumption.ENGINESIZE, train_FuelConsumption.CO2EMISSIONS,  color='green')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

# Creamos el modelo

from sklearn import linear_model
lm_FuelConsumption = linear_model.LinearRegression()

# extrae los datos de nuestra variable independiente del data frame de entrenamiento y lo convierte en un numpy array  
train_X = np.asanyarray(train_FuelConsumption[['ENGINESIZE']])

# extrae los datos de nuestra variable dependiente del data frame de entrenamiento y lo convierte en un numpy array  
train_y = np.asanyarray(train_FuelConsumption[['CO2EMISSIONS']])

# Entrena el modelo con estos datos
lm_FuelConsumption.fit (train_X, train_y)

# The coefficients pendiente e intercepción de la recta:
 
print ('Coefficients: ', lm_FuelConsumption.coef_)
print ('Intercept: ',lm_FuelConsumption.intercept_)

# Coefficients:  [[39.04696629]]
# Intercept:  [125.16938052]

# Dibujamos la recta del modelo sobre los datos de estudio:
  
plt.scatter(train_FuelConsumption.ENGINESIZE, train_FuelConsumption.CO2EMISSIONS,  color='green')
plt.plot(train_X, lm_FuelConsumption.coef_[0][0]*train_X + lm_FuelConsumption.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")

"""
Existen distintas métricas de evaluación de modelos, utilicemos MSE para calcular la exactitud de nuestro modelo basado en el set de prueba:

- Error absoluto de media: Es una media del valor absoluto de los errores. Es la métrica más fácil de comprender ya que simplemente es el promedio de los errores.
- Error Cuadrado Medio (MSE): El Error Cuadrado Medio (MSE) es la media del error cuadrático. Es más popular que el error de Media absoluto porque hace foco en grandes errores. Esto se debe a que el término cuadrático tiene errores más grandes que van creciendo en comparación con más pequeños.
- Error Cuadrático Medio (RMSE).
- R-cuadrática no es un error, sino que es una medida popular para darle precisión a nuestro modelo. Representa cuán cerca están los datos de la linea de regresión ajustada. Mientras más alto el R-cuadrático, mejor se encontrará ajustado el modelo respecto de los datos. El puntaje mejor posible es 1.0 y puede tomar valores negativos (porque el modelo puede ser arbitrariamente peor).

"""
from sklearn.metrics import r2_score

test_X = np.asanyarray(test_FuelConsumption[['ENGINESIZE']])
test_y = np.asanyarray(test_FuelConsumption[['CO2EMISSIONS']])

test_y_ = lm_FuelConsumption.predict(test_X)

print("Error medio absoluto: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Suma residual de los cuadrados (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )

# Error medio absoluto: 23.79
# Suma residual de los cuadrados (MSE): 942.91
# R2-score: 0.66

"""
    -.- Multiple Regression
        - Multiple Linear Regression

Nos sirve para:
    
- identificar el efecto que tienen las variables independientes en una variable dependiente?
- Predecir el impacto de cambios, es decir, entender como cambia la variable dependiente, cuando cambiamos las variables independientes.

El objetivo y es una combinación líneal de variables independientes, x.

Identificar predictores significativos de la variable de resultados.

Vector de parámetros y vector de conjunto de características, en un espacio multidimensional.

En este tipo de regresión la línea se denomina plano o hiper-plano. Por tanto el objetivo de este tipo de regresión es encontrar el mejor hiper-plano para nuestros datos.

Se debe encontrar el vector que mejor predice el valor del campo objetivo en cada fila, minimizando el error de la predicción.

Los parametros optimizados son los que conducen a un modelo con los errores menos graves.

Calculamos el error residual de cada fila en nuestro caso.

MSE - La media de todos los errores residuales, muestra que tan malo es el modelo.

Como encontrar el vector de coeficientes para la regresión lineal múltiple-

- minimos cuadrados ordinarios: tratan de estimar los valores minimizando el MSE, utilizando operaciones de aǵebra lineal para estimar los valores óptimos.

- enfoque de optimización para buscar los mejores parámetros, por ejemplo usando Gradient Descent, que inicia la optimización con valores aleatorios.

Cuantas variables independientes debemos usar? - evitar Overfit  (Sobreajuste)

Estas variables deben ser continuas?, se pueden incorporar convirtiendolas en numericas.

# ==========================
# Ejemplo con dataSet Boston
# ==========================

"""

# Redefinimos la variable X como un subconjunto de datos: DataFrame - [506 rows x 1 columns]
# [506 rows x 2 columns]
X = df_Boston.loc[df_Boston.index[0:506], ['LSTAT', 'AGE']]
print(X)

# [506 rows x 1 columns]
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df_Boston.iloc[df_Boston.index[0:506], [6,12]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # 5 primeros datos del array

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión múltiple
from sklearn.linear_model import LinearRegression

# Creando el módelo de regresión múltiple (lmm)
lmm_Boston = LinearRegression().fit(X_train,y_train) # ajustar el módelo
lmm_Boston.score(X,y) 
# Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.548590009185747, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmm_Boston.coef_
# array([[ 0.02703707, -0.9519301 ]])

lmm_Boston.intercept_
# array([32.73513282])

y_train_pred = lmm_Boston.predict(X_train) # Predice usando el módelo de regresión múltiple con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm_Boston.predict(X_test) # Predice usando el módelo de regresión múltiple con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5520920948986159
# Prueba 0.5426647322726053

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 43.72378908476468

# Vemos que no hay mucha diferencia entre los dos módelos

# ====================

# [506 rows x 2 columns]
X = df_Boston.loc[df_Boston.index[0:506], ['RM', 'AGE']]
print(X)

# [506 rows x 1 columns]
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df_Boston.iloc[df_Boston.index[0:506], [5,6]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # 5 primeros datos del array

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión múltiple
from sklearn.linear_model import LinearRegression

# Creando el módelo de regresión múltiple (lmm)
lmm2_Boston = LinearRegression().fit(X_train,y_train) # ajustar el módelo de regresión múltiple
lmm2_Boston.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.5291686548306225, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmm2_Boston.coef_
# array([[ 7.97818051, -0.07314422]])

lmm2_Boston.intercept_
# array([-22.67179459])

y_train_pred = lmm2_Boston.predict(X_train) # Predice usando el módelo de regresión múltiple con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm2_Boston.predict(X_test) # Predice usando el módelo de regresión múltiple con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.5480820218090987
# Prueba 0.49742229782888514

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 48.04921684179839

# Vemos que ha empeorado un poco 

# ====================

# [506 rows x 2 columns]
X = df_Boston.loc[df_Boston.index[0:506], ['RM', 'LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
X = df_Boston.iloc[df_Boston.index[0:506], [5,12]]

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # 5 primeros datos del array

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión múltiple
from sklearn.linear_model import LinearRegression

# Creando el módelo de regresión múltiple (lmm)
lmm3_Boston = LinearRegression().fit(X_train,y_train) # ajustar el módelo de regresión múltiple
lmm3_Boston.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.6360996567240672, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmm3_Boston.coef_
# array([[ 4.90198731, -0.59206716]])

lmm3_Boston.intercept_
# array([-0.81750634])

y_train_pred = lmm3_Boston.predict(X_train) # Predice usando el módelo de regresión múltiple con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm3_Boston.predict(X_test) # Predice usando el módelo de regresión múltiple con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.6453978719945989
# Prueba 0.620475389449678

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 36.28465853211026 

# Vemos que ha mejorado el módelo 

# ====================

# [506 rows x 12 columns]
X = df_Boston.loc[df_Boston.index[0:506],['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
# Eliminamos la columna de respuesta
X = df_Boston.drop('MEDV', axis=1) 

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # 5 primeros datos del array

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión múltiple
from sklearn.linear_model import LinearRegression

# Creando el módelo de regresión múltiple (lmm)
lmm4_Boston= LinearRegression().fit(X_train,y_train) # ajustar el módelo de regresión múltiple
lmm4_Boston.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.7355053338711364, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmm4_Boston.coef_
# array([[-7.08506031e-02,  3.83545105e-02,  1.64586726e-03,
#          2.68064794e+00, -1.40457528e+01,  3.87983706e+00,
#         -1.47321271e-02, -1.46902169e+00,  2.72037962e-01,
#         -1.38898308e-02, -9.29309865e-01,  1.06770120e-02,
#         -4.35484842e-01]])

lmm4_Boston.intercept_
# array([33.93984638])

y_train_pred = lmm4_Boston.predict(X_train) # Predice usando el módelo de regresión múltiple con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm4_Boston.predict(X_test) # Predice usando el módelo de regresión múltiple con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.7581323045862294
# Prueba 0.6975641751193842

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 28.914542900809323

# Vemos que ha mejorado el módelo utilizando todas las columnas

# ====================

# [506 rows x 12 columns]
X = df_Boston.loc[df_Boston.index[0:506],['CRIM','ZN','INDUS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
print(X)

# [506 rows x 1 columns]
y = df_Boston.loc[df_Boston.index[0:506], ['MEDV']]
print(y)

# Array of float - No hacemos el reshape, porque tenemos un número de filas y columnas definido - no hay que cambiarlo
# Eliminamos la columna de respuesta
X = df_Boston.drop(['MEDV', 'CHAS'], axis=1) 

# Variable de respuesta Array of float -  [[24.]21.6] ... [22. ][11.9]]
y = boston_dataSet.target[df_Boston.index].reshape(-1,1)

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 33% train 67% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 
# test_size=0.33 => 33% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train[:5] # 5 primeros datos del array

# lineal_multilineal_polinomial_SVR_Regresion.py => calculo del módelo de regresión múltiple
from sklearn.linear_model import LinearRegression

# Creando el módelo de regresión múltiple (lmm)
lmm5_Boston = LinearRegression().fit(X_train,y_train) # ajustar el módelo de regresión múltiple
lmm5_Boston.score(X,y) # Devuelve el coeficiente de determinación R² de la predicción
# R-squared - R²:  
 # 0 significa que la variable dependiente no se puede predecir por la variable independiente, 
 # 1 significa que se predice sin error.

# R-cuadrado explica en qué medida la varianza de una variable explica la varianza de la segunda. 
# Así pues, si el R² de un módelo es 0.7306812298857916, entonces aproximadamente el 54% de la variación observada puede ser explicada por las entradas del módelo.

# Coeficientes
lmm5_Boston.coef_
# array([[-7.79260455e-02,  4.00381988e-02,  2.22392025e-02,
#         -1.41712353e+01,  3.95945961e+00, -1.23201513e-02,
#         -1.48611798e+00,  3.04304732e-01, -1.56558846e-02,
#         -9.39436208e-01,  1.11704340e-02, -4.42040007e-01]])

lmm5_Boston.intercept_
# array([33.89013281])

y_train_pred = lmm5_Boston.predict(X_train) # Predice usando el módelo de regresión múltiple con los datos de entrenamiento
type(y_train_pred)
print(y_train_pred[:5])
y_test_pred = lmm5_Boston.predict(X_test) # Predice usando el módelo de regresión múltiple con los datos de prueba
print(y_test_pred[:5])

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))

# Entrenamiento 0.7522680521704352
# Prueba 0.6944820133786174

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)
# 29.20921466436714

# Vemos que no hay mucha diferencia quitando una variable que no está muy correlacionada

"""
# ===================================
# Ejemplo con dataSet FuelConsumption
# ===================================

"""
df_FuelConsumption = pd.read_csv("FuelConsumption.csv")

cdf_FuelConsumption = df_FuelConsumption[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf_FuelConsumption.head(9)
#    ENGINESIZE  CYLINDERS  ...  FUELCONSUMPTION_COMB  CO2EMISSIONS
# 0         2.0          4  ...                   8.5           196
# 1         2.4          4  ...                   9.6           221
# 2         1.5          4  ...                   5.9           136
# 3         3.5          6  ...                  11.1           255
# 4         3.5          6  ...                  10.6           244
# 5         3.5          6  ...                  10.0           230
# 6         3.5          6  ...                  10.1           232
# 7         3.7          6  ...                  11.1           255
# 8         3.7          6  ...                  11.6           267

# [9 rows x 6 columns]

plt.scatter(cdf_FuelConsumption.ENGINESIZE, cdf_FuelConsumption.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

msk = np.random.rand(len(df_FuelConsumption)) < 0.8
train = cdf_FuelConsumption[msk]
test = cdf_FuelConsumption[~msk]

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

from sklearn import linear_model
lmm_FuelConsumption = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
lmm_FuelConsumption.fit (x, y)
# The coefficients
print ('Coefficients: ', lmm_FuelConsumption.coef_)
# Coefficients:  [[10.9019738   7.68215694  9.37134365]]

# Como se mencionó anteriormente, Coefficient e Intercept , son los parámetros de la línea curva de ajuste. Dado que se trata de una regresión lineal múltiple, con 3 parámetros, y sabiendo que los parámetros son la intercepción y los coeficientes del hiperplano, sklearn puede estimarlos a partir de nuestros datos. Scikit-learn utiliza el método de los mínimos cuadrados ordinarios para resolver este problema.
# Ordinary Least Squares (OLS)

# OLS es un método para estimar los parámetros desconocidos en un modelo de regresión lineal. OLS elige los parámetros de una función lineal de un conjunto de variables explicativas minimizando la suma de los cuadrados de las diferencias entre la variable objetivo dependiente y las previstas por la función lineal. En otras palabras, intenta minimizar la suma de errores cuadrados (SSE) o 
# el error cuadrado medio (MSE) entre la variable objetivo (y) y nuestro resultado previsto (ℎ𝑎𝑡ℎ𝑎𝑡𝑦) en todas las muestras del conjunto de datos.

# OLS puede encontrar los mejores parámetros usando los siguientes métodos:

# - Resolución analítica de los parámetros del modelo mediante ecuaciones de forma cerrada
# - Utilizando un algoritmo de optimización (Descenso de Gradiente, Descenso de Gradiente Estocástico, Método de Newton, etc.)


y_pred = lmm_FuelConsumption.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Residual sum of squares: %.2f"
      % np.mean((y_pred- y) ** 2))
# Residual sum of squares: 567.82

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % lmm_FuelConsumption.score(x, y))
# Variance score: 0.88

lmm2_FuelConsumption = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])
y = np.asanyarray(train[['CO2EMISSIONS']])
lmm2_FuelConsumption.fit (x, y)
print ('Coefficients: ', lmm2_FuelConsumption.coef_)
# Coefficients:  [[10.95123646  7.47495424  5.66040218  3.54695623]]

y_= lmm2_FuelConsumption.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Residual sum of squares: %.2f"
      % np.mean((y_ - y) ** 2))
# Residual sum of squares: 567.07

print('Variance score: %.2f' % lmm2_FuelConsumption.score(x, y))
# Variance score: 0.88