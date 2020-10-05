#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 11:27:29 2020

@author: scelis
Datasets

https://scikit-learn.org/stable/
https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html - include in anaconda3

# sklearn_library.py
"""


from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer

import pandas as pd
# =============================================================================
# forma de crear un dataSet 

# from sklearn.datasets import load_breast_cancer
# import pandas as pd
# breast_cancer = load_breast_cancer()
# data = breast_cancer.data
# features = breast_cancer.feature_names
# df_breast_cancer = pd.DataFrame(data, columns=features)

# ó

# df_breast_cancer = pd.DataFrame(breast_cancer.data,columns=[breast_cancer.feature_names])

# =============================================================================

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_test_pred)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100) 

from sklearn.metrics import r2_score
print("Entrenamiento", r2_score(y_train, y_train_pred))
print("Prueba", r2_score(y_test, y_test_pred))


# ================= TEST ========================

# Utilidades y clases de transformación para cambiar los vectores de caracteristicas en bruto en una forma adecuada para modelado
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# Dividir el conjunto de datos en conjuntos de entrenamiento y pruebas para entrenar el modelo
# y luego probar la precisión del modelo por separado
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Creación de un clasificador usando un svm - máquinas de soporte vectorial - algoritmo, 
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

# Aprender a clasificar casos desconocidos
clf.fit(X_train, y_train)

# Ejecutar predicciones
clf.predict(X_test)

# Evaluar la precisión del modelo
from sklearn.metrics import confusion_matrix

# Finalmente guardar el modelo
import pickle
s=pickle.dumps(clf)

# ================= TEST ========================