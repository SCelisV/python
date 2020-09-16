#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Wed Sep 16 14:59:51 2020

@author: SCELIS
Application Program Interfaces - API - Two pieces of software talk each other via inputs and outputs

Pandas is actually set of software components , much of which is not even written in Python.
You create a dictionary, this is just data.
When you create a Pandas object with the Dataframe constructor in API lingo, this is an "instance". 
The data in the dictionary is passed along to the pandas API. 
You then use the dataframe to communicate with the API.
import pandas as pd
dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
type(df)
the method head the dataframe communicates with the API displaying the first few rows of the dataframe.
df.head()


REpresentational State Transfer - REST APIs - Client and Web Service(endpoint) talk each other via http messages normally JSON files
Rest API’s function by sending a request, the request is communicated via HTTP message. 
The HTTP message usually contains a JSON file. 
This contains instructions for what operation we would like the service or resource to perform. 
In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.

apis.py
"""

# we will use the NBA API to determine how well the Golden State Warriors performed against the Toronto Raptors. 
# We will use the API do the determined number of points the Golden State Warriors won or lost by for each game. 
# So if the value is three, the Golden State Warriors won by three points. 
# Similarly it the Golden State Warriors lost by two points the result will be negative two. 
# The API is relatively will handle a lot of the details such a Endpoints and Authentication

# Sports data is always changing
# In the nba api to make a request for a specific team, 
# we require an id
# It's stored locally in the API
# https://pypi.org/project/nba-api/
# !pip install nba_api

# one_dict => create a dictionary a partir de una lista.
def one_dict(list_dict):
    # dict_keys(['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])
    keys=list_dict[0].keys()
    # crea una lista 
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict  
          
import matplotlib.pyplot as plt
import pandas as pd

# we import the module teams
from nba_api.stats.static import teams

# get_teams (), returns a list of dictionaries the dictionary key id has a unique identifier for each team as a value 
# with have the same keys but the values depend on the team
# The dictionary key id has a unique identifier for each team as a values
nba_teams = teams.get_teams()
nba_teams[0:3]
# each element of the list corresponds to the values for each team
# [{'id': 1610612737,
#   'full_name': 'Atlanta Hawks',
#   'abbreviation': 'ATL',
#   'nickname': 'Hawks',
#   'city': 'Atlanta',
#   'state': 'Atlanta',
#   'year_founded': 1949},
#  {'id': 1610612738,
#   'full_name': 'Boston Celtics',
#   'abbreviation': 'BOS',
#   'nickname': 'Celtics',
#   'city': 'Boston',
#   'state': 'Massachusetts',
#   'year_founded': 1946},
#  {'id': 1610612739,
#   'full_name': 'Cleveland Cavaliers',
#   'abbreviation': 'CLE',
#   'nickname': 'Cavaliers',
#   'city': 'Cleveland',
#   'state': 'Ohio',
#   'year_founded': 1970}]

# convierte el dictionario de entrada en un diccionario de listas
dict_nba_team=one_dict(nba_teams)

# convert the dictionary to a DataFrame
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head(3)
#            id            full_name  ...          state year_founded
# 0  1610612737        Atlanta Hawks  ...        Atlanta         1949
# 1  1610612738       Boston Celtics  ...  Massachusetts         1946
# 2  1610612739  Cleveland Cavaliers  ...           Ohio         1970

# [3 rows x 7 columns]

# Will use the team's nickname to find the unique ID
df_teams['nickname'].unique

# <bound method Series.unique of 0             Hawks
# 1           Celtics
# 2         Cavaliers
# 3          Pelicans
# 4             Bulls
# 5         Mavericks
# 6           Nuggets
# 7          Warriors
# 8           Rockets
# 9          Clippers
# 10           Lakers
# 11             Heat
# 12            Bucks
# 13     Timberwolves
# 14             Nets
# 15           Knicks
# 16            Magic
# 17           Pacers
# 18            76ers
# 19             Suns
# 20    Trail Blazers
# 21            Kings
# 22            Spurs
# 23          Thunder
# 24          Raptors
# 25             Jazz
# 26        Grizzlies
# 27          Wizards
# 28          Pistons
# 29          Hornets
# Name: nickname, dtype: object>

# find the row for Warriors team
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors
#            id              full_name  ...       state year_founded
# 7  1610612744  Golden State Warriors  ...  California         1946

# [1 rows x 7 columns]

# can use the following line of code to access the first column of the dataframe
# we have an integer that can be used to request the warriors information
id_warriors = df_warriors[['id']].values[0][0]
id_warriors # 1610612744

# The function "League Game Finder " will make an API call, 
# its in the module stats.endpoints
# the NBA API is making a HTTP request

from nba_api.stats.endpoints import leaguegamefinder

# The information requested is provided and 
# is trasmited via HTTP response
# This is assigne to the object gamefinder.
# The gamefinder object has a method get_data_frames 
# information about all the games the warriors played
# The parameter team_id_nullable is the unique ID for the warriors. 
# (team_id_nullable=id_warriors)
# https://stats.nba.com permite muchas llamadas API de Cloud IPs y 
# Skills Network Labs utiliza un Cloud IP.

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# JSON que devuelve - response
gamefinder.get_json()

# gamefinder object has a method (get_data_frames()), 
# return a df it contains information about all the games the Warriors played

# =============================================================================

# The PLUS_MINUS column contains information on the score, 
# if the value is negative the Warriors lost by that many points, 
# if the value is positive, the warriors one by that amount of points. :
#     
# The column MATCHUP had the team the Warriors were playing, 
# GSW stands for Golden State Warriors and 
# TOR means Toronto Raptors; 
# 
# vs signifies it was a home game - juego en casa 
# the @ symbol means an away game - juego fuera de casa
# 
# you can download the dataframe from the API call for Golden State and run the rest like a video.
# ! wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl
# A PKL file is a file created by pickle, a Python module that enabless objects to be serialized to files on disk and deserialized back into the program at runtime. ... 
# The PKL file is created using Python pickle and the dump() method and is loaded using Python pickle and the load() method.
# https://stackoverflow.com/questions/24906126/how-to-unpack-pkl-file
# https://www.datacamp.com/community/tutorials/pickle-python-tutorial

# =============================================================================

games = gamefinder.get_data_frames()[0]
games.head()

#   SEASON_ID     TEAM_ID TEAM_ABBREVIATION  ... TOV  PF PLUS_MINUS
# 0     22019  1610612744               GSW  ...   9  17      -24.0
# 1     22019  1610612744               GSW  ...   7  19        4.0
# 2     22019  1610612744               GSW  ...  15  23       -8.0
# 3     22019  1610612744               GSW  ...  11  23       16.0
# 4     22019  1610612744               GSW  ...  21  24      -14.0

# [5 rows x 28 columns]
games.describe()
#             TEAM_ID          MIN  ...           PF   PLUS_MINUS
# count  3.308000e+03  3308.000000  ...  3308.000000  2186.000000
# mean   1.610613e+09   240.666566  ...    23.024486     0.204575
# std    0.000000e+00    12.027250  ...     4.890547    14.755498
# min    1.610613e+09     0.000000  ...     0.000000   -48.000000
# 25%    1.610613e+09   240.000000  ...    20.000000    -9.750000
# 50%    1.610613e+09   240.000000  ...    23.000000    -1.000000
# 75%    1.610613e+09   240.000000  ...    26.000000    10.000000
# max    1.610613e+09   460.000000  ...    41.000000    50.000000

# [8 rows x 21 columns]

file_name = "/home/hadoop/Downloads/Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

#   SEASON_ID     TEAM_ID TEAM_ABBREVIATION  ...   TOV  PF PLUS_MINUS
# 0     22019  1610612744               GSW  ...  11.0  21        3.2
# 1     22019  1610612744               GSW  ...  20.0  20       -8.0
# 2     22019  1610612744               GSW  ...  13.0  22        8.0
# 3     22019  1610612744               GSW  ...  20.0  25       10.0
# 4     22019  1610612744               GSW  ...  13.0  15       -8.0

# [5 rows x 28 columns]

# the games that the Warriors at Home
games_home=games [games ['MATCHUP']=='GSW vs. TOR']

# the games that the Warriors out at Home
games_away=games [games ['MATCHUP']=='GSW @ TOR']

# calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away
games_home.mean()['PLUS_MINUS'] # 3.730769230769231

games_away.mean()['PLUS_MINUS'] # -0.6071428571428571

# We can plot out the PLUS MINUS column 
# for the dataframes games_home 
# and  games_away. 
# We see the warriors played better at home.

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

# =============================================================================
# funcionamiento de la function: one_dict
# =============================================================================
# extrae las key
# keys=nba_teams[0].keys()
# crea un dictionario de listas, 
# donde cada key:
# 'id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 
# 'year_founded' es de tipo lista
# out_dict={ key:[] for key in keys } 
# 
# almacena los elementos de cada diccionario
# en su correspondiente lista de key
# para ir actualizando el diccionario de salida out_dict
# for team in nba_teams:
#     for key, value in team.items():
#         out_dict[key].append(value)
#  
# abbreviation=['ATL', 'BOS', 'CLE', 'NOP', 'CHI', 'DAL', 'DEN', 'GSW', 'HOU', 'LAC', 'LAL', 'MIA', 'MIL', 'MIN', 'BKN', 'NYK', 'ORL', 'IND', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'OKC', 'TOR', 'UTA', 'MEM', 'WAS', 'DET', 'CHA']
# type (abbreviation) # list
# =============================================================================