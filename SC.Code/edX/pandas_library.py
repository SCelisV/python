#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Aug 20 00:06:09 2020

@author: scelis - ¯\_(ツ)_/¯
pandas biblioteca que proporciona un alto rendimiento, 
estructuras de datos fáciles de usar y 
herramientas de análisis de datos 
para Python.
pandas_library.py
https://pandas.pydata.org
https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
"""

# Trabajando con pandas -

# Rows - default
# axis=0 axis='rows'

# Columns
# axis=1 axis='columns'

import pandas as banana
df_banana = banana.DataFrame({"a":[11,21,31], "b":[21,22,23]})
df_banana.head()

import pandas as pd
import numpy as np

# Reading files csv
csv_path = 'file.csv'
df_read_csv = pd.read_csv(csv_path)

# Reading files excel
xlsx_path = 'file.xlsx'
df_read_xlsx = pd.read_xlsx(xlsx_path)

# Create df from a a dictionary
songs = {
    "Album" : ["Thriller", "Back in Black", "The Dark Side of the Moon",\
               "The Bodyguard", "Bast Out of Hell", \
               'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'],
        "Released" : [1982,1980,1973,1992,1977,1976,1977,1977],
        "Length" : ["00:42:19", "00:42:22", "00:42:49", "00:57:44", "00:46:33", "", "", ""]
}

df_songs = pd.DataFrame(songs)

# Conocer todos los types de datos de df
df_songs.dtypes
df_songs.info
# Create un df basado en una columna
x=df_songs[['Length']]
type(x)

y=df_songs[['Length', "Album"]]
type(y)


# Asking For Help
help(pd.Series.loc)

# Pandas Data Structures

# definir una serie
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

# definir un DataFrame
data = {'Country': ['Belgium', 'India', 'Brazil'],
'Capital': ['Brussels', 'New Delhi', 'Brasília'],
'Population': [11190846, 1303171035, 207847528],
'Channel': ['Facebook', '', '']
}

# Crear el df DataFrame
df_Population = pd.DataFrame(data,
                             columns=['Country', 'Capital', 'Population', 'Channel'])

from sklearn.datasets import load_boston
boston_dataSet = load_boston()
type(boston_dataSet)
desc =  boston_dataSet.DESCR
print(desc)

# print("Describe el DataFrame: boston_dataSet => ", desc)
print("Describe el DataFrame: boston_dataSet => ", desc[148:1225])

df_boston = pd.DataFrame(boston_dataSet.data,
                  columns=[boston_dataSet.feature_names])

#convierte todos los datos en float (trabajar con el mismo tipos)
df_boston = df_boston.astype(np.float64)

# busca los vacios en campos númericos,los ordena y muestra las primeras columnas
df_boston.isnull().sum().sort_values(ascending=False).head(10)

# informa los elementos NA datos vacios en este caso ffill => rellena con el previo de esa misma columna
df_boston = df_boston.fillna(method ='ffill') 

# Crea la columna MEDV
df_boston['MEDV'] = boston_dataSet.target[df_boston.index]


# Crea una nueva New Boolean column dependiendo de una condición
df_Population['is_newBoolean'] = np.where(
    df_Population['Population'] > 11190846, True, False
    )

df_Population.is_newBoolean.head()

# Tipo de datos - Common data types

# Strings (objects)
# Numbers (floats, integers)
# Boolean values(True, False)
# Dates

# Display las primeras head y ultimas tail filas del df
# print(df)
print(df_boston.head())
df_boston.head()
df_boston.tail()
# Display las primeras filas de la 'name_variable'
df_boston.name_variable.head()
# returns the first few rows (the “head” of the DataFrame).
df_boston.head(10)
df_boston.tail(10)
# like summary estadístico de todas las columnas numéricas, 
# calculates a few summary statistics for each column.
# return: count, mean, std, min, 25%, 50%, 75%, max
df_boston.describe()
# para las columnas alfanumérica, return, count, unique,  top, freq
df_boston.describe(include='object') 
# las estadísticas de resumen se calculan para todas las columnas - NaN - si la estadística no es correcta para esa columna
df_boston.describe(include='all')
# especificando diferentes tipos
df_boston.describe(include=['int', 'float', 'object']) 
# especificando un tipo de percentiles que quiera analizar
df_boston.describe(percentiles=[.1,.5,.9]) 
# excluye los float
df_boston.describe(exclude='float') 
# resume of DataFrame - check column data types and non-missing values . check tipo de datos
# shows information on each of the columns, such as the data type and number of missing values.
df_boston.info()
# Display el tipo de datos de cada columna del DataFrame
df_boston.dtypes
# combine head() and tail()
print(df_boston)
# Display el tipo de datos de una columna del DataFrame
print(df_Population['Population'].dtype)
# Cambiar el tipo de datos de una columna
df_Population['Population']=df_Population['Population'].astype('int')
df_Population.dtypes
# Display the index columns - RangeIndex(start=0, stop=506, step=1)
df_boston.index
# Display MultiIndex([(   'CRIM',),(     'ZN',), ... ,  (   'MEDV',)],)
df_boston.columns 
# returns the number of rows and columns of the DataFrame.
df_boston.shape 


# Display an array with head and tail
df_boston.to_numpy()

# Transposing your data:
df_boston_t = df_boston.T

# Sorting by an axis: npi
df_boston_sort = df_boston.sort_index(axis=1, ascending=False)

# -O-J-O- DON'T WORK - Sorting by name of field - df_sort_name = df_boston.sort_values(by='AGE') 

# Display - [9 rows x 14 columns] - filas 0 a 9 - [506 rows x 14 columns]
df_boston[1:10]
df_boston[0:506]

"""
se basa en las etiquetas; 
cuando se utilizan dos argumentos se usan los encabezados de las columnas y 
el índice de filas para seleccionar los datos que se desean, 
también pude tomar un número entero como número de fila o de columna.
loc_pandas.py
"""
df_songs.loc[0,'Album'] # 'Thriller'
df_songs.loc[0,'Length'] # '00:42:19'
df_songs.loc[1,['Album','Released', 'Length' ]]
# Album       Back in Black
# Released             1980
# Length           00:42:22
# Name: 1, dtype: object

# Display la fila 10 del dataSet
df_boston.loc[df_boston.index[10]] 

# Display [506 rows x 2 columns]
df_boston.loc[:, ['AGE', 'CRIM']]

# Display la fila 0, columna CRIM
df_boston.loc[df_boston.index[0], 'CRIM'] 

# -O-J-O- DON'T WORK - df_boston.at[df_boston.index[0], 'CRIM'] 

# Display [506 rows x 14 columns]
df_boston.loc[df_boston.index]

"""
basado en números enteros.
Utiliza números de columna y números de fila para obtener los
datos en posiciones particulares en el df

iloc_pandas.py
"""

df_songs.iloc[0,0] # 'Thriller'
df_songs.iloc[0,2] # '00:42:19'
df_songs.iloc[1,[0,1,2]]

# Album       Back in Black
# Released             1980
# Length           00:42:22
# Name: 1, dtype: object


# Display la fila 3 de dataSet 
df_boston.iloc[3]

# Display las fila 3 a 4 and las columnas 0 a 2
df_boston.iloc[3:5, 0:3]

# Display las filas 1,2,4 y las columnas 0 y 1
df_boston.iloc[[1, 2, 4], [0, 2]]

# Display - las filas 1 y 2 y todas las columnas - [2 rows x 14 columns]
df_boston.iloc[1:3, :]

# Display - todas las fila y las columnas 1 y 3 - [506 rows x 2 columns]
df_boston.iloc[:, 1:3]

df_boston.iloc[0:0]
# =============================================================================
# 
# Empty DataFrame
# Columns: [(CRIM,), (ZN,), (INDUS,), (CHAS,), (NOX,), (RM,), (AGE,), (DIS,), (RAD,), (TAX,), (PTRATIO,), (B,), (LSTAT,), (MEDV,)]
# Index: []
# 
# =============================================================================

# Display posición fila 0, columna 0
df_boston.iloc[0:1, 0:1]

# Seleccionar una posición específica
df_boston.iloc[0, 0]

# para obtener un acceso rápido a un elemento
df_boston.iloc[1, 1]
df_boston.iat[1, 1]

# Seleccionando valores de un DataFrame donde se cumple una condición booleana.
df_boston[df_boston > 0]

#  -O-J-O- DON'T WORK - Usando el método isin() para filtrar
df2 = df_boston.copy()
dates = pd.date_range('20200819', periods=506)
df2['dates'] = dates
df2[df2['dates'].isin(['2020-08-29 00:00:00', '2020-10-26 00:00:00'])]

# total de filas y de columnas del dataSet
df_boston.shape

# Display correlación de todas las variables vs la variable de respuesta/estudio
df_boston.corr()["MEDV"].sort_values()

# I/O - files
# Read and Write to CSV
pd.read_csv('titanic.csv', header=None, nrows=5)

marketing = '/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/marketing.csv'
df_marketing = pd.read_csv(marketing)
type(df_marketing)
df_boston.to_csv('boston.csv')


# Read and Write to Excel
pd.read_excel('titanic.xlsx')
df_boston.to_excel('boston.xlsx', sheet_name='Boston')

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
df_boston.iloc[[0],[0]]
#  -O-J-O- DON'T WORK - df_boston.iat([0],[0])
df_boston.iat[0,0]

# Select single value by row & column labels
# By Label
df_boston.loc[[0], ['CRIM']]
# -O-J-O- DON'T WORK - df_boston.at([0], ['CRIM'])

# By Label/Position
# Select single row of subset of rows
df_boston.loc[2]

# Display la columna n del dataSet
# Select column by index -  - DataFrame - [506 rows x 1 columns]
X = df_boston.iloc[df_boston.index[0:506], [12]]

# select column by Label - DataFrame - [506 rows x 1 columns]
X = df_boston.loc[df_boston.index[0:506], ['LSTAT']]


# Array of float -  [[4.98][9.14]... [ 6.48][ 7.88]]
X = boston_dataSet.data[df_boston.index[0:506],[12]].reshape(-1,1)
y = boston_dataSet.data[df_boston.index[0:506],[13]].reshape(-1,1)
print(y)


# =============================================================================
# Remove columns a un df - drop
# =============================================================================

df_marketing.drop(columns=['PCDG', 'PCND', 'PCESV'], axis=1, inplace=True)

df_marketing.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

# =============================================================================
# Fechas
# =============================================================================

# Convertir la columna existente en tipo datetime column
df_marketing['date_served'] = pd.to_datetime(df_marketing['date_served'])


import pandas as pd

df_test=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
df_test.head()
# find the unique values in column  'a' :
df_test['a']

# return a dataframe with only the rows where column  a is less than two 

df_test_new =