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

# attributos de fecha del descriptor dt (datetime) 
# dayofweek - 0,1,2,3,4,5,6,7 = Lunes, Martes, Miercoles, Jueves, Viernes, Sábado, Domingo
marketing['day_served'] = marketing['date_served'].dt.dayofweek
marketing.info()
marketing.day_served.head(10)

# Print the data type of the is_retained column.
# Check the data type of is_retained
print(marketing['is_retained'].dtype)

# Update the data type of the is_retained column to boolean and then check its data type again.
# Convert is_retained to a boolean
marketing['is_retained'] = marketing['is_retained'].astype('bool')

# Check the data type of is_retained, again
print(marketing['is_retained'].dtype)

# =============================================================================
# add two columns to marketing:
# * day_of_week: represents the day of the week as an integer (we added a new column, day that represents the day of the week and defined a dictionary that maps the day of the week to each numerical value from 0 to 6 for this purpose.)
# * is_correct_lang: conveys whether the ad was shown to the user in their preferred language
# 
# =============================================================================
# Add a new column, channel_code, which maps the values in the subscribing_channel column to a numeric scale using the channel_dict dictionary.
# Mapping for channels
channel_dict = {"House Ads": 1, "Instagram": 2,
                "Facebook": 3, "Email": 4, "Push": 5}

# Map the channel to a channel code
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# Import numpy with the alias np.
# Add a new column, is_correct_lang, which is 'Yes' if the user was shown the ad in their preferred language, 'No' otherwise.

# Import numpy
import numpy as np

# Add the new column is_correct_lang
marketing['is_correct_lang'] = np.where(
    marketing['language_preferred'] == marketing['language_displayed'],
        'Yes', 'No'
)

# =============================================================================
# Import pandas into the environment with the alias pd.
# Read 'marketing.csv' into your environment correctly identifying date columns,'date_served' 'date_subscribed' and 'date_canceled' within your call to read_csv().
# Create a day of week column from 'date_subscribed' using dt.dayofweek
# 
# =============================================================================
# Import pandas into the environment
import pandas as pd

# Import marketing.csv with date columns
marketing = pd.read_csv('marketing.csv',
                    parse_dates = ['date_served',
                                    'date_subscribed',
                                    'date_canceled'
                                    ]
                    )
marketing.info()
# Add a DoW column (day of week) column
marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek
marketing['DoW'].head()
marketing['DoW'].dtype

# Aggregate unique - agrupa por fecha y clasifica por usuario
daily_users = marketing.groupby(['date_served'])['user_id'].nunique()
print(daily_users)


# Visualizing results
import matplotlib.pyplot as plt
daily_users.plot()

# Annotate
plt.title("Número diario de usuarios que ven los anuncios")
plt.xlabel("Fecha")
plt.ylabel("Número de usuarios")
plt.xticks(rotation=45)
plt.show()


# Group the marketing DataFrame by 'date_served' and count the number of unique user IDs.
# Group by date_served and count number of unique user_id's
daily_users = marketing.groupby(['date_served'])['user_id'].nunique()

# Print head of daily_users
print(daily_users.head())

# =============================================================================
# Use the .plot() method to visualize the results of date_served.
# Add the title 'Daily users' and the y-axis label 'Number of users'.
# Rotate the x-axis labels by 45 degrees.
# Display the plot.
# 
# =============================================================================
# Plot daily_subscribers
daily_users.plot()

# Include a title and y-axis label
plt.title('Daily users')
plt.ylabel('Number of users')

# Rotate the x-axis labels by 45 degrees
plt.xticks(rotation=45)

# Display the plot
plt.show()



# =============================================================================
# Cuantas personas de las que vieron la campaña, se hicieron clientes ó se suscribieron al servicio ofrecido?
# Tasa de conversion - Conversion rate
#                     Number of people who Convert
# Conversion rate = ----------------------------------------
#                     Total number of people we marketed to
# 
# =============================================================================

# converted = True => se ha suscrito
suscribers = marketing[marketing['converted'] == True]['user_id'].nunique()
print (suscribers)

total = marketing['user_id'].nunique()
print(total)

conv_rate = suscribers/total
print(round(conv_rate*100, 2), '%' ) # 92.86 %



# =============================================================================
# Cuanto tiempo sigue siendo cliente, ó suscriptor de un servicio?
# Tasa de retención Retention rate - 
#                       Number of people who remain subscribed
#  Retention rate = ----------------------------------------
#                      Total number of people who converted
# 
# =============================================================================

marketing.info()

# is_retained = número de usuarios que siguen siendo suscriptor después de 1mes
retained = marketing[marketing['is_retained'] == True]['user_id'].nunique()
print(retained)

suscribers = marketing[marketing['converted'] == True]['user_id'].nunique()
print (suscribers)

ret_rate = retained/suscribers
print(round(ret_rate*100, 2), '%') # 100.0 %


# =============================================================================
# Calculate the number of unique user_ids in marketing DataFrame.
# Calculate the number of people who subscribed using the converted column.
# Calculate the conversion rate.
# =============================================================================

# Calculate the number of people we marketed to
total = marketing['user_id'].nunique()

# Calculate the number of people who subscribed
subscribers = marketing[marketing['converted'] == True]['user_id'].nunique()

# Calculate the conversion rate
conversion_rate = subscribers/total
print(round(conversion_rate*100, 2), '%')

# =============================================================================
# Calculate the number of subscribers using the user_id and converted columns in the marketing DataFrame.
# Calculate the number of retained subscribers using the boolean columns user_id and is_retained.
# Calculate the retention rate.
# =============================================================================

# Calculate the number of subscribers
total_subscribers = marketing[marketing['converted'] == True]['user_id'].nunique()

# Calculate the number of people who remained subscribed
retained = marketing[marketing['is_retained']==True]['user_id'].nunique()

# Calculate the retention rate
retention_rate = retained/total_subscribers
print(round(retention_rate*100, 2), "%")

# Segmentación de clientes
# Tasa de retención de los usuarios que convirtieron haciendo click en un anuncio interno
# subscribing_channel => canal al que se ha suscrito el usuario
print(marketing.subscribing_channel.head())
house_ads = marketing\
            [marketing['subscribing_channel'] == 'House Ads']

print(house_ads.head())
            
# is_retained = número de usuarios que siguen siendo suscriptor del canal 'House Ads'
retained = house_ads\
    [house_ads['is_retained'] == True]\
        ['user_id'].nunique()
print(retained)

# converted = True => se ha suscrito en el canal 'House Ads'
suscribers = house_ads\
    [house_ads['converted'] == True]\
        ['user_id'].nunique()
print (suscribers)

ret_rate = retained/suscribers
print(round(ret_rate*100, 2), '%') #100.0 %

# Segmentación (con pandas) de clientes retenidos, agrupando por canal y encontrando el número de clientes por canal
retained = marketing\
    [marketing['is_retained'] == True]\
        .groupby(marketing['subscribing_channel'])\
            ['user_id'].nunique()

print(retained)
# subscribing_channel
# Email        25
# House Ads    26
# Instagram     1
# Name: user_id, dtype: int64            

# tasa de retención por canal numero de clientes retenidos por el número total de suscribtores
channel_ret_rate = (retained/suscribers)
print(round(channel_ret_rate*100, 2))
# subscribing_channel
# Email         96.15
# House Ads    100.00
# Instagram      3.85
# Name: user_id, dtype: float64

