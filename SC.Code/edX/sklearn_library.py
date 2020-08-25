#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 11:27:29 2020

@author: scelis
Datasets

https://scikit-learn.org/stable/
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