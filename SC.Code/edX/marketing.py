#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Tue Sep  8 12:26:29 2020

@author: scelis - ¯\_(ツ)_/¯
marketing.py
"""
import pandas as pd
import numpy as np

# leer/read un csv file
marketing = pd.read_csv('/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/marketing.csv')
marketing.head()
marketing.describe()
marketing.info()

# tipo de datos de una columna
print(marketing['converted'].dtype)
print(marketing['Unnamed: 0'].dtype)

# eliminar una columna
marketing.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

# cambiar el tipo de datos de una columna
marketing['converted'] = marketing['converted'].astype('bool')

# Crea una nueva New Boolean column dependiendo de una condición
marketing['is_house_ads'] = np.where(
    marketing['marketing_channel'] == 'House Ads', True, False
    )

# Consultar los datos de una sola columna
marketing.is_house_ads.head()

# crear una columna con códigos de canal 

# Asigna los canales a códigos numericos
channel_dict = {"House Ads":1, "Instagram":2,
                "Facebook":3, "Email":4, "Push":5}

marketing.marketing_channel.head()
# 0    House Ads
# 1    House Ads
# 2    House Ads
# 3    House Ads
# 4    House Ads

marketing.channel_code.head()

# Mapping values to existing columns,
marketing['channel_code'] = marketing['marketing_channel'].map(channel_dict)
marketing['channel_code'].head()
# 0    1
# 1    1
# 2    1
# 3    1
# 4    1
# Name: channel_code, dtype: int64

# Columnas de fechas
# leer/read un csv file asegurando que las columnas de fecha se lean correctamente como columnas de fechas
# parse_dates
marketing2 = pd.read_csv('/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/marketing.csv',
                        parse_dates=['date_served', 
                                     'date_subscribed',
                                     'date_canceled'
                                     ]                      
                        )
marketing2.head()
marketing2.describe()
marketing2.info()
 # 2   date_served          60 non-null     datetime64[ns]
 # 9   date_subscribed      60 non-null     datetime64[ns]
 # 10  date_canceled        18 non-null     datetime64[ns] 
# or
# Convertir la columna existente en tipo datetime column
marketing['date_served'] = pd.to_datetime(marketing['date_served'])
marketing['date_subscribed'] = pd.to_datetime(marketing['date_subscribed'])
marketing['date_canceled'] = pd.to_datetime(marketing['date_canceled'])
marketing.info()


