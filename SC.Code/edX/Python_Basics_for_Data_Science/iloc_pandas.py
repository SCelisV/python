#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Mon Sep 14 15:41:52 2020

@author: scelis - ¯\_(ツ)_/¯

iloc is one way to select data from a data frame in Pandas
basado en números enteros.
Utiliza números de columna y números de fila para obtener los
datos en posiciones particulares en el df

iloc_pandas.py
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

titanic.iloc[0,0] # 1
titanic.iloc[0,3] # 'Braund, Mr. Owen Harris'

titanic.iloc[5,0] # 6
titanic.iloc[5,3] # 'Moran, Mr. James'

titanic.iloc[890,0] # 891
titanic.iloc[890,3] # 'Dooley, Mr. Patrick'

# iloc return a KeyError if the requested items are not found
titanic.iloc[891,0] # IndexError: single positional indexer is out-of-bounds



# Using iloc for slicing(corte)

# Create a new df con iloc slicing
# Slice df and assign values to new df using the column names

z_iloc_titanic=titanic.iloc[0:3, 0:4] # [3 rows(0,1,2) x 4 columns("0 PassengerId", "1 Survived", "2 Pclass", "3 Name")
z_iloc_titanic.head()
z_iloc_titanic.describe()
z_iloc_titanic.info()