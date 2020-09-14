#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Mon Sep 14 15:41:52 2020

@author: scelis - ¯\_(ツ)_/¯

loc is one way to select data from a data frame in Pandas

se basa en las etiquetas; 
cuando se utilizan dos argumentos se usan los encabezados de las columnas y 
el índice de filas para seleccionar los datos que se desean, 
también pude tomar un número entero como número de fila o de columna.

loc_pandas.py
"""
import pandas as pd

name_file = "/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/titanic.csv"

titanic = pd.read_csv(name_file)
titanic.head()
titanic.describe()
titanic.info()
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns)
type(titanic) # pandas.core.frame.DataFrame

titanic.loc[0,'PassengerId'] # 1
titanic.loc[0,'Name'] # 'Braund, Mr. Owen Harris'

titanic.loc[5,'PassengerId'] # 6
titanic.loc[5,'Name'] # 'Moran, Mr. James'

titanic.loc[890,'PassengerId'] # 891
titanic.loc[890,'Name'] # 'Dooley, Mr. Patrick'

# loc return a KeyError if the requested items are not found
titanic.loc[891,'PassengerId'] # ValueError: 891 is not in range

# Using loc for slicing(corte)

# Create a new df con loc slicing
# Slice df and assign values to new df using the column names

z_loc_titanic=titanic.loc[0:2, 'PassengerId':'Name'] # [3 rows(0,1,2) x 4 columns("0 PassengerId", "1 Survived", "2 Pclass", "3 Name")
z_loc_titanic.head()
z_loc_titanic.describe()
z_loc_titanic.info()
