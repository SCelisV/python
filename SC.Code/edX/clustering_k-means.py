#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Sep 10 00:16:48 2020

@author: scelis - ¯\_(ツ)_/¯
clustering_k-means.py
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/jupyter/MPML/data/bank/CC/CCGENERAL.csv')

df.head()
df.describe()
df.CREDIT_LIMIT.head()

df.info()

df.isnull().sum().sort_values(ascending=False).head()

# MINIMUM_PAYMENTS       313
# CREDIT_LIMIT             1
# TENURE                   0
# PURCHASES_FREQUENCY      0
# BALANCE                  0
# dtype: int64

df.index
df.columns 
df.shape

print(df)

df = df.drop('CUST_ID', axis=1)

