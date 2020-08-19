#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Wed Aug 19 15:28:50 2020

@author: scelis

"""

# London.py
from sklearn.datasets import load_boston
boston_dataSet = load_boston()
desc =  boston_dataSet.DESCR

# print("Describe el dataframe: boston_dataSet => ", desc)
print("Describe el dataframe: boston_dataSet => ", desc[148:1225])

import pandas as pd
df = pd.DataFrame(boston_dataSet.data,columns=[boston_dataSet.feature_names])

# print(df)
df.describe()


# Crea la columna MEDV
df['MEDV'] = boston_dataSet.target[df.index]
ds_summary = df.describe()

df.shape


# Crea la matriz de correlación

import seaborn as  sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
%matplotlib inline
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(),annot=True)



import numpy as np
