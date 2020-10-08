#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
@author: scelis - ¯\_(ツ)_/¯

Classification.py

Es un enfoque de Aprendizaje supervisado.

Método de categorización ó clasificación de algunos elementos desconocidos en un set discreto de clases

Predicting the item class/category or case.

Intenta aprender la relación entre un set de variables y un objetivo.

La variable objetivo es categorica con valores discretos.

Como funcionan las clasificaciones y los clasificadores?

Dado un set de datos, de entrenamiento con sus etiquetas, se determina la clase para un caso de prueba.

    - clasificadores binarios (0,1):
        
Conociendo datos previos de los clientes y de los prestamos que no se han pagado.    
Podemos predecir que clientes podrían tener un impago futuro.
(edad, ingresos, educación, etc...)

Estos clientes de "riesgo", pueden o no tener ofrecimientos alternativos, 
ó se les puede negar la concesión de un nuevo crédito.

    - clasificadores multi-clases:
    
Conociendo datos de pacientes que han sufrido la misma enfermedad,
y en su tratamiento, cada paciente responde mejor a uno de varios medicamentos,
Podemos predecir cual medicamente es mejor para un paciente futuro.

Applications: 
    Spam detection, image recognition, speech recognition, hand writing recognition
    identificación bio-metrica, clasificación de documentos
    una celula es Maligna ó Benigna
    un cliente se va a retirar ó no - ratio de abandono
    un cliente incumple sus pagos ó no
    categorizar a los clientes
    un cliente responde o no a una campaña publicitaria
    
    Muchos problemas pueden ser explresados como asociaciones entre
    las caracteristicas y la variable objetivo cuando disponemos de datos etiquetados.
    
# ==========================
#     -.- Algoritmos de Classification:
# ==========================
    
    - Arboles de decisión - Decision Trees (ID3, C4.5, C5.0)
        (https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf)
        CART - Árboles de clasificación y regresión 
        pretenden explicar o predecir una variable a partir de un conjunto de variables predictoras utilizando un conjunto de reglas sencillas. 
    - Naive Bayes
    - Linear Discriminant Analysis
    - k-Nearest Neighbors - K vecinos más cercanos - KNN 
    - Logistic Regression
    - Neural Networks - Redes neuronales - recibir, procesar y transmitir información
    - Support Vector Machines (SVM) - Máquinas de Soporte Vectorial
    

            - k-Nearest Neighbor - K vecinos más cercanos - KNN 

Estima la probabilidad de que un elemento "x" pertenezca a una clase "C", a partir de la información proporcionada.

Podemos asignar una etiqueta de clase a un cliente nuevo basandome en los clientes cercanos a él?

Hasta que punto podemos confiar en nuestro juicio si esta basadon en nuestro PRIMER vecino más próximo..?

Cuantos vecinos próximos podemos elegir para definir la clase de nuestro cliente?

Definir los vecinos más próximos, este algoritmo toma un montón de puntos marcados y los utiliza para aprender a etiquetar otros puntos.

Basado en la similitud de otros casos.

Se dice que son vecinos los puntos cercanos entre si a nuestro punto objetivo.

Casos similares con las mismas etiquetas de clase - Similar cases with same class labels are near each other.

Por tanto la distancia entre dos casos es una medida de su disimilitud.

Para calcular esta medida, se utiliza la distancia Euclidiana. - Euclidean distance.

1. Elejir un valor para K
2. Calcular la distancia desde el nuevo caso (exclusión de cada uno de los casos del conjunto de datos)
3. Buscar las k-observaciones en los datos de entrenamiento que son "más próximos" al caso de estudio
4. Predecir la respuesta del punto de datos desconocido utilizando el valor de la respuesta más popular de los vecinos más próximos.

Tener cuidado:
    
    1. Como seleccionar la K correcta?
    
        Si elegimos un K bajo -> mala predicción ya que no tenemos en cuenta la mayoria de los puntos que hay alrededor.
        y estamos capturando el ruido de los datos, ó puntos anomalos.
        Puede dar lugar a un exceso de ajuste. overfitting, es decir, no se generaliza lo suficiente.
        
        Si elegimos un K alto -> mala predicción ya que el modelo se vuelve demasiado generalizado.
        
        La solución general es reservar una parte de sus datos para probar la precisión del modelo.
        
        y probar estos datos con los diferentes valores desde k=1, y calcular la precisión utilizando todos los ejemplos de pruebas.
        hasta encontrar el mejor k == mejor precisión.
    
    
    2. Como calcular la similitud entre los casos?
        
        Si solo tenemos una caracteristica, facilmente podemos utilizar la distancia Minkowski para calcular la distancia entre ellos.
        Esta distancia puede ser considerada como una generalización de Euclidean distance and Manhattan distance.
        
        Si tenemos varias caracteristicas, se puede utilizar la misma distancia pero en un espacio bi/dimensional. 
        Por lo tanto tenemos que normalizar el conjunto de caracteristicas para obtener la medida de disimilitud precisa.
        
        Hay otras medidas, pero son altamente dependientes del tipo de datos y del dominio de la clasificación.
   
Este análisis se puede utilizar para calcular valores de objetivos continuos.
y por lo tanto utilizaremos el promedio de los vecinos más próximos. 

- Predecir los precios de un piso dependiendo de por ejemplo el número de habitaciones, año de construcción, metros cuadrados.. etc.


Métricas de Evaluación: Explican el rendimiento de un modelo. - Usando datos de pruebas.
    
    
    
    Básicamente comparamos los valores reales en el set de pruebas con los valores pronosticados (predicciones de nuestro modelo).
    De tal forma proporcionamos una perspectiva hacia areas que pueden requerir mejoras.
    
    - Jaccard index - coeficiente de similaridad - El tamaño de la intersección dividido por el tamañño de la unión de los dos set de etiquetas. (reales-predicciones).
    
    
    Ex: hay 8 predicciones correctas 
    
        y_real (0,0,0,0,0,1,1,1,1,1)
        y_pred (1,1,0,0,0,1,1,1,1,1)
        
        8/(10+10-8) = 0.66 sería el indice de precisión => Higher Accuracy

        1.0 = coinciden TODAS las predicciones con los valores reales.
        0.0 = No coincide NINGUNA predicción con los valores reales. 
        
    - F1 - Score -  Matriz de Confusión - Muestra las predicciones corregidas y erroneas, 
        en comparación con las etiquetas reales.
        Muestra la habilidad del modelo para predecir correctamente ó separar las clases.
        
    SI vs SI => PC ó TP => Positivo Correcto
    NO vs NO => NC ó TN => Negativo Correcto
    SI vs NO => FP => Falsos Positivos => Error Tipo 1
    NO vs SI => FN => Falsos Negativos => Error Tipo 2
    
    Cada FILA muestra las etiquetas Reales / Verdaderas y 
    Cada COLUMNA muestra las predicciones.
    
    | PC ó TP |    FN   |
   ----------------------
   |    FP   | NC ó TN |
    
    Precisión = Positive Predicted Value: (PC ó TP) / (PC ó TP) + FP
    Recall: (PC ó TP) / (PC ó TP) + FN
    
    F1 - Score es el promedio armónico de a precisión y el recall.
    
    Donde el F1 - Score 
    alcanza su mejor valor en 1. Que representa la precisión y el recall perfecto.
    alcanza su peor valor en 0.
    
    F1 - Score = 2x(Precisión * Recall) / (Precisión + Recall)
    
    Muestra si el modelo tiene un buen valor tanto para el recall como para la precisión.
    
    Podemos decir que la precisión promedio es el promedio del F1 - Score para las etiquetas.
    
    La precisión sirve para saber la probabilidad de acierto en la predicción => (PC ó TP) + (NC ó TN) / Total
    La tasa de error sirve para saber la probabilidad de error en la predicción => (FP + FN) / Total
        
    - Log Loss - Logarithmic loss - A veces la salida de un clasificador es la probabilidad de una etiqueta de clase, en lugar de la etiqueta.
    
    En una regresión logistica, la salida puede ser la probabilidad de ratio de abandono de un cliente, es decir, 
    
    si = 1. Esta probabilidad es un valor entre 0 y 1.
    
    Este algoritmo mide el rendimiento de un clasificador donde la salida pronosticada es un valor de probabilidad entre 0 y 1.
    
    Mide que tan lejos está cada predicción con respecto a la etiqueta real.
    
    Luego se calcula el log loss promedio en todas las filas de los datos de pruebas.
    
    Evidentemente los clasificadores más idóneos tienen valores progresivamente más pequeños de log loss.
    
    Por tanto el clasificador con menor log loss tiene una mejor precisión.

"""
"""
# ==========================
# k-Nearest Neighbor - K vecinos más cercanos - KNN - Ejemplo con dataSet de telecomunicaciones
# ==========================
"""
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing

namefile = "/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Machine_Learning/teleCust1000t.csv"

df_telecomunicaciones = pd.read_csv(namefile)
df_telecomunicaciones.head(10)
#    region  tenure  age  marital  ...  retire  gender  reside  custcat
# 0       2      13   44        1  ...     0.0       0       2        1
# 1       3      11   33        1  ...     0.0       0       6        4
# 2       3      68   52        1  ...     0.0       1       2        3
# 3       2      33   33        0  ...     0.0       1       1        1
# 4       2      23   30        1  ...     0.0       0       4        3
# 5       2      41   39        0  ...     0.0       1       1        3
# 6       3      45   22        1  ...     0.0       1       5        2
# 7       2      38   35        0  ...     0.0       0       3        4
# 8       3      45   59        1  ...     0.0       0       5        3
# 9       1      68   41        1  ...     0.0       0       3        2

# [10 rows x 12 columns]


# Cuantas clases hay en el dataSet
df_telecomunicaciones['custcat'].value_counts()
# 3    281
# 1    266
# 4    236
# 2    217
# Name: custcat, dtype: int64

# La variable objeto es custcat, que es la clasificacion de clientes, a saber: 
#     1- Servicio Básico -> 266
#     2- E-Servicio -> 217
#     3- Servicio Plus -> 281
#     4- Servicio Total -> 236

# Histograma de ingreso (consumo y ahorro) obtenido por una entidad
df_telecomunicaciones.hist(column='income', bins=50)

df_telecomunicaciones.describe()
#           region       tenure  ...       reside      custcat
# count  1000.0000  1000.000000  ...  1000.000000  1000.000000
# mean      2.0220    35.526000  ...     2.331000     2.487000
# std       0.8162    21.359812  ...     1.435793     1.120306
# min       1.0000     1.000000  ...     1.000000     1.000000
# 25%       1.0000    17.000000  ...     1.000000     1.000000
# 50%       2.0000    34.000000  ...     2.000000     3.000000
# 75%       3.0000    54.000000  ...     3.000000     3.000000
# max       3.0000    72.000000  ...     8.000000     4.000000

# [8 rows x 12 columns]

df_telecomunicaciones.shape
# (1000, 12)

# Columnas del dataFrame
df_telecomunicaciones.columns
# Index(['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed',
#        'employ', 'retire', 'gender', 'reside', 'custcat'],
#       dtype='object')

# defino la variable X
X=df_telecomunicaciones[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values
X[0:5]

# array([[  2.,  13.,  44.,   1.,   9.,  64.,   4.,   5.,   0.,   0.,   2.],
#        [  3.,  11.,  33.,   1.,   7., 136.,   5.,   5.,   0.,   0.,   6.],
#        [  3.,  68.,  52.,   1.,  24., 116.,   1.,  29.,   0.,   1.,   2.],
#        [  2.,  33.,  33.,   0.,  12.,  33.,   2.,   0.,   0.,   1.,   1.],
#        [  2.,  23.,  30.,   1.,   9.,  30.,   1.,   2.,   0.,   0.,   4.]])

# defino la variable y
y=df_telecomunicaciones['custcat'].values
y[0:5]

# array([1, 4, 3, 1, 3])

# Normalizar los datos
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]

# array([[-0.02696767, -1.055125  ,  0.18450456,  1.0100505 , -0.25303431,
#         -0.12650641,  1.0877526 , -0.5941226 , -0.22207644, -1.03459817,
#         -0.23065004],
#        [ 1.19883553, -1.14880563, -0.69181243,  1.0100505 , -0.4514148 ,
#          0.54644972,  1.9062271 , -0.5941226 , -0.22207644, -1.03459817,
#          2.55666158],
#        [ 1.19883553,  1.52109247,  0.82182601,  1.0100505 ,  1.23481934,
#          0.35951747, -1.36767088,  1.78752803, -0.22207644,  0.96655883,
#         -0.23065004],
#        [-0.02696767, -0.11831864, -0.69181243, -0.9900495 ,  0.04453642,
#         -0.41625141, -0.54919639, -1.09029981, -0.22207644,  0.96655883,
#         -0.92747794],
#        [-0.02696767, -0.58672182, -0.93080797,  1.0100505 , -0.25303431,
#         -0.44429125, -1.36767088, -0.89182893, -0.22207644, -1.03459817,
#          1.16300577]])

# Creamos el split de datos - dividir en subconjuntos aleatorios de datos de entrenamiento y datos de prueba
# test 20% train 80% aleatorios semilla = 100
from sklearn.model_selection import train_test_split
# test_size=0.2 => 20% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. 
# Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100) 
#  primeros datos del array
X_train[:5] 
# array([[ 1.19883553,  0.77164739,  0.98115637, -0.9900495 , -0.4514148 ,
#         -0.17323947,  0.26927811,  1.09287993, -0.22207644, -1.03459817,
#         -0.92747794],
#        [-1.25277087,  1.70845375,  0.82182601,  1.0100505 ,  0.93724861,
#         -0.13585302, -1.36767088,  1.29135082, -0.22207644, -1.03459817,
#          0.46617787],
#        [ 1.19883553, -0.68040245,  0.18450456, -0.9900495 ,  1.33400958,
#         -0.28539883, -1.36767088,  0.1005255 , -0.22207644,  0.96655883,
#         -0.23065004],
#        [-1.25277087, -0.11831864, -0.61214725,  1.0100505 , -0.94736601,
#         -0.46298447, -1.36767088, -0.79259348, -0.22207644,  0.96655883,
#          0.46617787],
#        [-1.25277087, -0.77408309, -1.16980352,  1.0100505 , -0.84817577,
#         -0.39755818, -0.54919639, -0.69335804, -0.22207644, -1.03459817,
#          2.55666158]])

print ('Set de Entrenamiento:', X_train.shape,  y_train.shape)
# Set de Entrenamiento: (800, 11) (800,)
print ('Set de Prueba:', X_test.shape,  y_test.shape)
# Set de Prueba: (200, 11) (200,)

from sklearn.neighbors import KNeighborsClassifier

# Probamos con k=1
k=1
#Entrenar el Modelo y Predecir - classification model kn
cmkn_telecomunicaciones = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
cmkn_telecomunicaciones
# KNeighborsClassifier(n_neighbors=1)

# Predecir con los datos de prueba
ypred = cmkn_telecomunicaciones.predict(X_test)
ypred[0:5]
# array([4, 3, 4, 1, 3])

# En clasificación multietiqueta, la función classification accuracy score computa la certeza del subconjunto. 
# Esta función es igual a la función jaccard_similarity_score. 
# Básicamente, calcula cómo se relacionan las etiquetas actuales con las etiquetas predichas dentro del set de pruebas.

from sklearn import metrics
print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, cmkn_telecomunicaciones.predict(X_train)))
# Entrenar el set de Certeza:  1.0
print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, ypred))
# Probar el set de Certeza:  0.32

# Probamos con k=4
k=4
#Entrenar el Modelo y Predecir - classification model kn
cmkn2_telecomunicaciones = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
cmkn2_telecomunicaciones
# KNeighborsClassifier(n_neighbors=4)

# Predecir con los datos de prueba
ypred = cmkn2_telecomunicaciones.predict(X_test)
ypred[0:5]
# array([4, 1, 3, 2, 3])

# En clasificación multietiqueta, la función classification accuracy score computa la certeza del subconjunto. 
# Esta función es igual a la función jaccard_similarity_score. 
# Básicamente, calcula cómo se relacionan las etiquetas actuales con las etiquetas predichas dentro del set de pruebas.

from sklearn import metrics
print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, cmkn2_telecomunicaciones.predict(X_train)))
# Entrenar el set de Certeza:  0.54375
print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, ypred))
# Probar el set de Certeza:  0.375

# Probamos con k=6
k=6
#Entrenar el Modelo y Predecir - classification model kn
cmkn3_telecomunicaciones = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
cmkn3_telecomunicaciones
# KNeighborsClassifier(n_neighbors=6)

# Predecir con los datos de prueba
ypred = cmkn3_telecomunicaciones.predict(X_test)
ypred[0:5]
# array([2, 3, 3, 2, 1])

# En clasificación multietiqueta, la función classification accuracy score computa la certeza del subconjunto. 
# Esta función es igual a la función jaccard_similarity_score. 
# Básicamente, calcula cómo se relacionan las etiquetas actuales con las etiquetas predichas dentro del set de pruebas.

from sklearn import metrics
print("Entrenar el set de Certeza: ", metrics.accuracy_score(y_train, cmkn3_telecomunicaciones.predict(X_train)))
# Entrenar el set de Certeza:  0.485
print("Probar el set de Certeza: ", metrics.accuracy_score(y_test, ypred))
# Probar el set de Certeza:  0.39

# Podemos calcular la certeza de KNN para diferentes Ks.

Ks = 10
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
ConfustionMx = [];

for n in range(1,Ks):
    
    #Entrenar el Modelo y Predecir
    number=str(n)
    nameModel = "cmkn"+number+"_telecomunicaciones"
    # print(nameModel)
    nameModel = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    ypred=nameModel.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, ypred)
    std_acc[n-1]=np.std(ypred==y_test)/np.sqrt(ypred.shape[0])

mean_acc
# array([0.32 , 0.34 , 0.36 , 0.375, 0.39 , 0.39 , 0.395, 0.365, 0.365])

# Graficamos 
plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Certeza ', '+/- 3xstd'))
plt.ylabel('Certeza ')
plt.xlabel('Número de Vecinos (K)')
# plt.tight_layout()
plt.show()

# Imprime la media maxima 0.395
# mean_acc.max()
# Return el indice del máximo 6 
# mean_acc.argmax() 
# mean_acc.argmax()+1

print( "La mejor aproximación de certeza fue con ", mean_acc.max(), "con k=", mean_acc.argmax()+1) 
# La mejor aproximación de certeza fue con  0.395 con k= 7

"""


            - Arboles de decisión - Decision Trees (ID3, C4.5, C5.0) 
            
(https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf)

Pretenden explicar o predecir una variable a partir de un conjunto de variables predictoras utilizando un conjunto de reglas sencillas. 

The basic intiuition behind a decision tree is to map out all possible decision paths in the form of a tree.

Los arboles de decisión se crean dividiendo el conjunto de datos de entrenamiento en nodos distintos, 
donde un nodo contiene todo o la mayoría de una categoría, de una categoría de los datos.

La decisión de elegir A ó B se verán influenciadas por otras variables de decisión.

Se trata de probar un atributo e ir ramificando los casos, basandose en el resultado de la prueba.

Cada nodo interno, corresponde a una prueba.
y cada rama se corresponde con un resultado de la prueba.
y cada nodo de hoja asigna un caso a una clase.

Se puede crear un argol de decisiones teniendo en cuenta los atributos uno por uno.
1. Elije un atributo del dataSet
2. Calcular la importancia del atributo en la división de los dato, para ver si se trata de un atributo efectivo o no.
3. Dividir los datos en función del valor del mejor atributo.
4. Go to 1 and repeat para el resto de los atributos.

Al final se podrá usar para predecir la clase de los casos desconocidos.

Cual atributo es el mejor ó más predictivo para dividir los datos en función de esa caracteristica.

Se trata de una selección errónea de atributos cuando por una o más divisiones de los datos no tenemos suficiente información para determinar si es adecuado.

Se trata de un mejor opción cuando comparando el resultado de los atributos en los nodos es más puro, es decir, que los nodos son mayoritariamente A ó B.
More Predictiveness, Less Impurity, Lower Entropy.

En tal caso volvemos a probar la selección erronea bajo esta mejor opción y ver si podemos tomar una decisión más pura.

Un nodo se considera "puro" si en el 100% de los casos, los nodos caen en una categoría especifica del campo objetivo.

Se utiliza el particionamiento recursivo para dividir los registros en segmentos, minimizando la impureza en cada paso.

La impureza de los nodos se calcula mediante la "Entropía", de los datos en el nodo.

Entropia es la cantidad de desorden de la información ó la cantidad de aleatoriedad en los datos, ó
la cantidad de aleatoriedad en los datos.
Esta depende de la cantidad de datos aleatorios que se encuentran en ese nodo y se calcula para cada nodo.

En los Arboles de decisión se busca que tengan la entropía más pequeña en sus nodos.
Se usa para calcular la homogeneidad de las muestras en ese nodo.

Si las muestras son completamente homogeneas = 0;
Si las muestras son divididas equitativamente = 1.

Es decir, que si todos los datos de un nodo son ó únicamente A ó únicamente B la entropia es 0.
Y si la mitad de los datos son A y la otra mitad son B entonces la entropia es 1.

Se calcula utilizando la tala de frecuencias del atributo.

Ejemplo: tenemos 14 ocurrencias en total.
9 son A y 5 son de B, se puede incorporar estos números para calcular la impureza del atributo antes de dividirlo. E=0.94

Si seleccionamos otro atributo con dos valores y tenemos que de esos dos valores hay 6 para A y 2 para B. E=0.811
y los otros 6 tienen 3 valores de A y 3 de B para estos casos E=1.00

y así sucesivamente.

El árbol con la mayor ganancia de información después de la división, es decir, la información que puede aumentar el nivel de certeza después de la división.

CART - Árboles de clasificación (asigna una etiqueta) y Árboles de regresión (asigna una valor) 


"""
"""
# ==========================
# Arboles de decisión - Decision Trees - Ejemplo con dataSet drugs
# ==========================
"""
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

namefile = "/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Machine_Learning/drug200.csv"

df_Drugs = pd.read_csv(namefile, delimiter=",")
df_Drugs.head(10)

#    Age Sex      BP Cholesterol  Na_to_K   Drug
# 0   23   F    HIGH        HIGH   25.355  drugY
# 1   47   M     LOW        HIGH   13.093  drugC
# 2   47   M     LOW        HIGH   10.114  drugC
# 3   28   F  NORMAL        HIGH    7.798  drugX
# 4   61   F     LOW        HIGH   18.043  drugY
# 5   22   F  NORMAL        HIGH    8.607  drugX
# 6   49   F  NORMAL        HIGH   16.275  drugY
# 7   41   M     LOW        HIGH   11.037  drugC
# 8   60   M  NORMAL        HIGH   15.171  drugY
# 9   43   M     LOW      NORMAL   19.368  drugY

df_Drugs[0:5]

#    Age Sex      BP Cholesterol  Na_to_K   Drug
# 0   23   F    HIGH        HIGH   25.355  drugY
# 1   47   M     LOW        HIGH   13.093  drugC
# 2   47   M     LOW        HIGH   10.114  drugC
# 3   28   F  NORMAL        HIGH    7.798  drugX
# 4   61   F     LOW        HIGH   18.043  drugY


df_Drugs.describe()

#               Age     Na_to_K
# count  200.000000  200.000000
# mean    44.315000   16.084485
# std     16.544315    7.223956
# min     15.000000    6.269000
# 25%     31.000000   10.445500
# 50%     45.000000   13.936500
# 75%     58.000000   19.380000
# max     74.000000   38.247000

df_Drugs.shape
# (200, 6)

len(df_Drugs)
# 200

# Columnas del dataFrame
df_Drugs.columns
# Index(['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug'], dtype='object')

# defino la variable X
X=df_Drugs[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']] .values
X.shape
# (200, 5)
X[0:5]

# array([[23, 'F', 'HIGH', 'HIGH', 25.355],
#        [47, 'M', 'LOW', 'HIGH', 13.093],
#        [47, 'M', 'LOW', 'HIGH', 10.113999999999999],
#        [28, 'F', 'NORMAL', 'HIGH', 7.797999999999999],
#        [61, 'F', 'LOW', 'HIGH', 18.043]], dtype=object)

# Algunas características son categorícas, tales como:
# Sex, Blood Pressure (Presión Sanguínea), Cholesterol.
# Desafortunadamente, los árboles de Decisión Sklearn no manejan variables categóricas. 
# Pero las podemos convertir en valores numéricos. 
# pandas.get_dummies() Convertir variable categórica en indicadores de variables.

# Normalización de los datos
from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1]) 
# Transforma ['F','M'] en valores [0,1] respectivamente
X[:,1]
# array([0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1,
#        1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1,
#        0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0,
#        1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1,
#        0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
#        1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1,
#        1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0,
#        1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
#        1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
#        1, 0], dtype=object)

le_BP = preprocessing.LabelEncoder()
le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])
# Transforma ['LOW', 'NORMAL', 'HIGH'] en valores [0,1,2] respectivamente
X[:,2]
# array([0, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 0, 1, 1, 2, 0, 1, 0, 1, 0, 1, 2,
#        1, 1, 1, 0, 0, 2, 1, 1, 2, 0, 1, 0, 2, 2, 0, 1, 2, 2, 2, 0, 2, 2,
#        2, 2, 0, 1, 2, 1, 0, 2, 1, 0, 0, 1, 0, 0, 2, 0, 1, 0, 1, 1, 0, 2,
#        0, 2, 2, 0, 0, 2, 2, 2, 0, 1, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 2, 1,
#        0, 2, 2, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2, 0, 1, 2, 1, 0, 2,
#        0, 2, 1, 1, 2, 0, 2, 2, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 1, 2, 2, 1,
#        1, 2, 0, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1, 0, 1, 1, 0, 0, 2, 1,
#        1, 1, 0, 1, 1, 1, 2, 0, 2, 0, 0, 1, 1, 2, 1, 0, 2, 1, 2, 1, 0, 0,
#        0, 2, 2, 2, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 2,
#        2, 1], dtype=object)

le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3]) 
# Transforma [ 'NORMAL', 'HIGH'] en valores [0,1] respectivamente
X[:,3]
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0,
#        1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0,
#        1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
#        0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
#        1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0,
#        0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
#        1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1,
#        1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0,
#        1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
#        1, 1], dtype=object)

X.shape
# (200, 5)
X[0:5]
# array([[23, 0, 0, 0, 25.355],
#        [47, 1, 1, 0, 13.093],
#        [47, 1, 1, 0, 10.113999999999999],
#        [28, 0, 2, 0, 7.797999999999999],
#        [61, 0, 1, 0, 18.043]], dtype=object)

# defino la variable y
y=df_Drugs['Drug'].values
y.shape
# (200,)
y[0:5]
# array(['drugY', 'drugC', 'drugC', 'drugX', 'drugY'], dtype=object)

from sklearn.model_selection import train_test_split
# test_size=0.3 => 30% representan la proporción del conjunto de datos a incluir en la división de la prueba
# random_state => semilla aleatoria => Controla la "barajar" aplicada a los datos antes de aplicar la división. 
# Pasa un int para una salida reproducible a través de múltiples llamadas de función
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=100) 
#  primeros datos del array
X_train[:5] 


# array([[31, 1, 0, 1, 17.069000000000003],
#        [28, 0, 2, 0, 7.797999999999999],
#        [57, 0, 2, 1, 25.893],
#        [31, 1, 0, 0, 30.366],
#        [62, 1, 2, 0, 16.594]], dtype=object)

X_train.shape
# (140, 5)
len(X_train)
# 140
y_train.shape
# (140,)
len(y_train)
# 140

X_test.shape
# (60, 5)
len(X_test)
# 60
y_test.shape
# (60,)
len(y_test)
# 60

# Definiendo la profundidad, creando el modelo, entrenando el modelo
from sklearn.tree import DecisionTreeClassifier
tmc_Drugs = DecisionTreeClassifier(criterion="entropy", max_depth = 4).fit(X_train,y_train)
tmc_Drugs # muestra los parámetros por omisión
# DecisionTreeClassifier(criterion='entropy', max_depth=4)

# Prediciendo valores de entrenamiento
y_train_pred = tmc_Drugs.predict(X_train)
y_train_pred[0:5]
# array(['drugY', 'drugX', 'drugY', 'drugY', 'drugY'], dtype=object)

# Prediciendo valores de prueba
y_test_pred = tmc_Drugs.predict(X_test)
y_test_pred[0:5]
# array(['drugY', 'drugY', 'drugY', 'drugY', 'drugX'], dtype=object)

from sklearn.tree import export_graphviz
export_graphviz(tmc_Drugs)
print(export_graphviz(tmc_Drugs))
# https://dreampuf.github.io/GraphvizOnline/
# digraph Tree {
# node [shape=box] ;
# 0 [label="X[4] <= 14.588\nentropy = 1.968\nsamples = 140\nvalue = [20, 8, 11, 41, 60]"] ;
# 1 [label="X[2] <= 0.5\nentropy = 1.72\nsamples = 80\nvalue = [20, 8, 11, 41, 0]"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
# 2 [label="X[0] <= 50.5\nentropy = 0.863\nsamples = 28\nvalue = [20, 8, 0, 0, 0]"] ;
# 1 -> 2 ;
# 3 [label="entropy = 0.0\nsamples = 20\nvalue = [20, 0, 0, 0, 0]"] ;
# 2 -> 3 ;
# 4 [label="entropy = 0.0\nsamples = 8\nvalue = [0, 8, 0, 0, 0]"] ;
# 2 -> 4 ;
# 5 [label="X[2] <= 1.5\nentropy = 0.744\nsamples = 52\nvalue = [0, 0, 11, 41, 0]"] ;
# 1 -> 5 ;
# 6 [label="X[3] <= 0.5\nentropy = 0.995\nsamples = 24\nvalue = [0, 0, 11, 13, 0]"] ;
# 5 -> 6 ;
# 7 [label="entropy = 0.0\nsamples = 11\nvalue = [0, 0, 11, 0, 0]"] ;
# 6 -> 7 ;
# 8 [label="entropy = 0.0\nsamples = 13\nvalue = [0, 0, 0, 13, 0]"] ;
# 6 -> 8 ;
# 9 [label="entropy = 0.0\nsamples = 28\nvalue = [0, 0, 0, 28, 0]"] ;
# 5 -> 9 ;
# 10 [label="entropy = 0.0\nsamples = 60\nvalue = [0, 0, 0, 0, 60]"] ;
# 0 -> 10 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
# }

from sklearn import metrics
import matplotlib.pyplot as plt
print("Precisión de los Arboles de Decisión Classifier: ", metrics.accuracy_score(y_test,y_test_pred))
# Precisión de los Arboles de Decisión Classifier:  0.9833333333333333

# -O-J-O- No funciono - 

# # https://pypi.org/project/graphviz/
# # pip install six
# # pip install graphviz
# from graphviz import Digraph
# dot = Digraph(comment='The Drugs Arboles de Decisión Classifier')

# # dot  # doctest: +ELLIPSIS
# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')
# print(dot.source)
# dot.render('test-output/The Drugs.gv', view=True) 
# 'test-output/he Drugs.gv.pdf'


"""
# ==========================
# Arboles de regresión - Decision Trees - Ejemplo con dataSet Boston
# ==========================

Árboles de regresión (asigna una valor)

Se hacen diferentes intervalos y a cada uno se asigna un valor de tal forma se podrá identificar cada punto a que rango pertenece

El procedimiento para generar un árbol de regresión empieza partiendo la totalidad del intervalo de los datos de la variable independiente x en diferentes intervalos pequeños. En nuestro ejemplo aprovecharemos que es posible identificar que los datos parecen estar agrupados en los siguientes cuatro intervalos:  
Asignarle un valor numérico a una entrada x de la cuál no se conocía su valor de salida y previamente.

    𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜4: 0.75 ≤ 𝑥 ≤ 1.0 => 𝑦=15
    𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜3: 0.5 ≤ 𝑥 < 0.75 => 𝑦=20
    𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜2: 0.25 ≤ 𝑥 < 0.5 => 𝑦=15
    𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜1: 0 ≤ 𝑥 < 0.25 => 𝑦=10
    
Todos los valores dentro del primer intervalo son muy cercanos al valor de 𝑦=10, de igual manera se pueden establecer relaciones similares para los valores de los demás intervalos.

Posterior a las observaciones que hemos realizado podemos construir un conjunto de reglas basadas en el valor de x que tiene la variable y representarlas en forma de un diagrama que se conoce como árbol de regresión y 
se utiliza para asignarle un valor numérico a una entrada x de la cuál no se conocía su valor de salida y previamente. 
Para ejemplificar lo anterior suponga que existe un valor de entrada tal que 𝑥∗=0.4 para el cuál no se conoce con exactitud su valor de salida 𝑦, 

Se podría proponer:
    
    Si (x > 0.5):
        Si (x > 0.75):
            y = 15
        SiNo:
            y = 20
    SiNo: Si (x > 0.25):
                y = 15
          SiNo:
                y = 10
    
Por lo tanto el valor de salida para el valor de entrada de 𝑥=0.4 será 𝑦=15.
    
"""
from sklearn.datasets import load_boston

# Cargamos un conjunto de datos
boston_dataset = load_boston()
import pandas as pd
df_Boston = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
# Agregamos la variable de respuesta
df_Boston['MEDV'] = boston_dataset.target[df_Boston.index]
df_Boston.head()
#       CRIM    ZN  INDUS  CHAS    NOX  ...    TAX  PTRATIO       B  LSTAT  MEDV
# 0  0.00632  18.0   2.31   0.0  0.538  ...  296.0     15.3  396.90   4.98  24.0
# 1  0.02731   0.0   7.07   0.0  0.469  ...  242.0     17.8  396.90   9.14  21.6
# 2  0.02729   0.0   7.07   0.0  0.469  ...  242.0     17.8  392.83   4.03  34.7
# 3  0.03237   0.0   2.18   0.0  0.458  ...  222.0     18.7  394.63   2.94  33.4
# 4  0.06905   0.0   2.18   0.0  0.458  ...  222.0     18.7  396.90   5.33  36.2

df_Boston.corr()["MEDV"].sort_values()
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
# MEDV       1.000000
# Name: MEDV, dtype: float64

# Preparamos datos
X = df_Boston["LSTAT"].values.reshape(-1, 1)
y = df_Boston["MEDV"].values.reshape(-1, 1)

# Normalizamos datos
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()
X = X_scaler.fit_transform(X)
X.shape
# (200, 5)
X[0:5]
# array([[0.08967991],
#        [0.2044702 ],
#        [0.06346578],
#        [0.03338852],
#        [0.09933775]])

y = y_scaler.fit_transform(y)
y.shape
# (200,)
y[0:5]
# array([[0.42222222],
#        [0.36888889],
#        [0.66      ],
#        [0.63111111],
#        [0.69333333]])

# Creamos un split de datos
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=100)

X_train.shape
# (339, 1)
len(X_train)
# 339
y_train.shape
# (339, 1)
len(y_train)
# 339

X_test.shape
# (167, 1)
len(X_test)
# 167
y_test.shape
#  (167, 1)
len(y_test)
# 167

from sklearn.tree import DecisionTreeRegressor
# Definir los niveles de profundidad
tmr_Boston = DecisionTreeRegressor(max_depth=2)
# Creando el modelo y entrenando
tmr_Boston = tmr_Boston.fit(X_train,y_train.reshape(-1))
# Prediciendo valores de entrenamiento
y_train_pred = tmr_Boston.predict(X_train)
# Prediciendo valores de validación
y_test_pred = tmr_Boston.predict(X_test)

# Graficamos

import matplotlib.pyplot as plt
import numpy as np
# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train,alpha=0.5)
# Creamos un scatter plot con los datos de validación
plt.scatter(X_test, y_test,alpha=0.5)
# En X_plot guardamos valores distribuidos entre 0 y 40
X_plot = np.linspace(0,1,1000).reshape(-1, 1)
y_plot = tmr_Boston.predict(X_plot)
# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--");

# https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html
from sklearn.tree import export_graphviz
export_graphviz(tmr_Boston)
print(export_graphviz(tmr_Boston))
# https://dreampuf.github.io/GraphvizOnline/
# digraph Tree {
# node [shape=box] ;
# 0 [label="X[0] <= 0.169\nmse = 0.039\nsamples = 339\nvalue = 0.391"] ;
# 1 [label="X[0] <= 0.08\nmse = 0.037\nsamples = 110\nvalue = 0.583"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
# 2 [label="mse = 0.03\nsamples = 31\nvalue = 0.777"] ;
# 1 -> 2 ;
# 3 [label="mse = 0.019\nsamples = 79\nvalue = 0.506"] ;
# 1 -> 3 ;
# 4 [label="X[0] <= 0.396\nmse = 0.014\nsamples = 229\nvalue = 0.298"] ;
# 0 -> 4 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
# 5 [label="mse = 0.007\nsamples = 132\nvalue = 0.366"] ;
# 4 -> 5 ;
# 6 [label="mse = 0.008\nsamples = 97\nvalue = 0.206"] ;
# 4 -> 6 ;
# }

from sklearn.metrics import r2_score
# Calculamos el error 
print("Entrenamiento de los Arboles de Decisión Regressor", r2_score(y_train, y_train_pred))
print("Prueba de los Arboles de Decisión Regressor", r2_score(y_test, y_test_pred))
# Entrenamiento de los Arboles de Decisión Regressor 0.686183783521107
# Prueba de los Arboles de Decisión Regressor 0.5894049706991193


"""
# 4. ->  -> SVM -> SVR - Supervisado
"""
# Buscan encontrar un hiperplano que separe los puntos compuestos en una categoria de otra. 
# Delimitar con notoriedad cada una de las características de los diferentes conjuntos.
# Las máquinas de soporte vectorial buscan encontrar un hiperplano que separe de forma óptima a los puntos que componen diferentes categorías unos de los otros. 
# Este tipo de algoritmo suele utilizarse para predecir a que categoría pertencerá un nuevo punto del que no se tenía información con anterioridad.
# SVR -> Regresión de Soporte Vectorial - Supervisado - SVR
# Support Vector Regression es un algoritmo de regresión basado en las máquinas de soporte vectorial utilizados para clasificar elementos de diferentes conjuntos. 
# En la siguiente sección se explicara cómo funciona el algoritmo SVR con datos lineales, 
# pero es importante saber que este algoritmo también funciona para datos no lineales.

# Objetivos: Máximizar el margen(las bandas de soporte que rodean a la línea de regresión) para abarcar la mayoría de los puntos de nuestro módelo y Minimizar el error

#     https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR
#     https://scikit-learn.org/stable/modules/svm.html#tips-on-practical-use
# 
# =============================================================================

"""
# 6. -> Redes neuronales => recibir, procesar y transmitir información
"""
# Perceptrón => neurona artificial, la unión de varios crean una red neuronal artificial. <=> simulan a las humanas y son capaces de transmitir señales entre ellas e ir modificando las entradas de las neuronas para obtener valores de salida
# Aprenden a partir de la experiencia para predecir

# Se compone de:
# - Canales/Señales de entrada - Dentritas
# - Función de activación - Soma o núcleo - (unión sumadora)
# - Canal de salida y Axón.

"""  n
 Σ WiXi + b
i=0  """




"""
