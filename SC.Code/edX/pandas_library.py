#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Aug 20 00:06:09 2020

@author: scelis
pandas biblioteca que proporciona un alto rendimiento, 
estructuras de datos fáciles de usar y 
herramientas de análisis de datos 
para Python.
pandas_library.py
https://pandas.pydata.org
https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
"""

# Trabajando con pandas -

import pandas as pd

# Asking For Help
help(pd.Series.loc)

# Pandas Data Structures

# definir una serie
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

# definir un dataFrame
data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528]}

df_Population = pd.DataFrame(data,
columns=['Country', 'Capital', 'Population'])

from sklearn.datasets import load_boston
boston_dataSet = load_boston()
desc =  boston_dataSet.DESCR

# print("Describe el dataframe: boston_dataSet => ", desc)
print("Describe el dataframe: boston_dataSet => ", desc[148:1225])

df = pd.DataFrame(boston_dataSet.data,columns=[boston_dataSet.feature_names])

# print(df)
df.describe()

# Crea la columna MEDV
df['MEDV'] = boston_dataSet.target[df.index]
df.describe()

# Display las primeras head y ultimas tail filas del df
df.head()
df.tail()

# Display el type de datos de cada columna del dataframe
df.dtypes

# Display the index columns - RangeIndex(start=0, stop=506, step=1)
df.index

# Display MultiIndex([(   'CRIM',),(     'ZN',), ... ,  (   'MEDV',)],)
df.columns 

# Display an array with head and tail
df.to_numpy()

# Transposing your data:
df_t = df.T

# Sorting by an axis: npi
df_sort = df.sort_index(axis=1, ascending=False)

# -O-J-O- DON'T WORK - Sorting by name of field - df_sort_name = df.sort_values(by='AGE') 

# Display - [9 rows x 14 columns] - filas 0 a 9 - [506 rows x 14 columns]
df[1:10]
df[0:506]

# Display la fila 10 del dataSet
df.loc[df.index[10]] 

# Display [506 rows x 2 columns]
df.loc[:, ['AGE', 'CRIM']]

# Display la fila 0, columna CRIM
df.loc[df.index[0], 'CRIM'] 

# -O-J-O- DON'T WORK - df.at[df.index[0], 'CRIM'] 

# Display [506 rows x 14 columns]
df.loc[df.index]

# Display la fila 3 de dataSet 
df.iloc[3]

# Display las fila 3 a 4 and las columnas 0 a 2
df.iloc[3:5, 0:3]

# Display las filas 1,2,4 y las columnas 0 y 1
df.iloc[[1, 2, 4], [0, 2]]

# Display - las filas 1 y 2 y todas las columnas - [2 rows x 14 columns]
df.iloc[1:3, :]

# Display - todas las fila y las columnas 1 y 3 - [506 rows x 2 columns]
df.iloc[:, 1:3]

df.iloc[0:0]
# =============================================================================
# Empty DataFrame
# Columns: [(CRIM,), (ZN,), (INDUS,), (CHAS,), (NOX,), (RM,), (AGE,), (DIS,), (RAD,), (TAX,), (PTRATIO,), (B,), (LSTAT,), (MEDV,)]
# Index: []
# 
# =============================================================================

# Display posición fila 0, columna 0
df.iloc[0:1, 0:1]

# Seleccionar una posición específica
df.iloc[0, 0]

# para obtener un acceso rápido a un elemento
df.iloc[1, 1]
df.iat[1, 1]

# Seleccionando valores de un DataFrame donde se cumple una condición booleana.
df[df > 0]

#  -O-J-O- DON'T WORK - Usando el método isin() para filtrar
df2 = df.copy()
dates = pd.date_range('20200819', periods=506)
df2['dates'] = dates
df2[df2['dates'].isin(['2020-08-29 00:00:00', '2020-10-26 00:00:00'])]

# total de filas y de columnas del dataSet
df.shape

# Display correlación de todas las variables vs la variable de respuesta/estudio
df.corr()["MEDV"].sort_values()

# I/O - files
# Read and Write to CSV
pd.read_csv('titanic.csv', header=None, nrows=5)
df.to_csv('boston.csv')

# Read and Write to Excel
pd.read_excel('titanic.xlsx')
df.to_excel('boston.xlsx', sheet_name='Boston')

# Read multiple sheets/hojas from the same file/del mismo fichero
xlsx = pd.ExcelFile('file.xlsx')
df_excel = pd.read_excel(xlsx, 'Boston02')

# Selection
# Also see NumPy Arrays
# Get one element
s['b']
# Get subset of a DataFrame
df_Population[1:]

# Selecting, Boolean Indexing & Setting
# By Position

# Select single value by row & column
df.iloc[[0],[0]]
#  -O-J-O- DON'T WORK - df.iat([0],[0])
df.iat[0,0]

# Select single value by row & column labels
# By Label
df.loc[[0], ['CRIM']]
# -O-J-O- DON'T WORK - df.at([0], ['CRIM'])

# By Label/Position
# Select single row of subset of rows
df.[2]

# Display la columna n del dataSet
# Select column by index -  - DataFrame - [506 rows x 1 columns]
X = df.iloc[df.index[0:506], [12]]

# select column by Label - DataFrame - [506 rows x 1 columns]
X = df.loc[df.index[0:506], ['LSTAT']]


# Array of float -  [[4.98][9.14]... [ 6.48][ 7.88]]
X = boston_dataSet.data[df.index[0:506],[12]].reshape(-1,1)
y = boston_dataSet.data[df.index[0:506],[13]].reshape(-1,1)
print(y)