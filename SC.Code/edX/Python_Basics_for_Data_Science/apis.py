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

00#   SEASON_ID     TEAM_ID TEAM_ABBREVIATION  ... TOV  PF PLUS_MINUS
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

# =============================================================================

# Discuss API that use some kind of AI.
# Transcribe audio file using the Watson Text to Speech API
# Translate the text to a new language using the Watson Language Translator API


# In the API call, you will send a copy of the audio file to the API ( POST request )
# The API send the text transcription of what the individual is saying (this is a GET request )
# we send  the text we would like to translate into a second language to a second API
# The API translate the text

# Provide an overview:

# - API keys and end points

# API keys as a way to access the API, its the unique set of characters that the API uses to identify you and authorize you.
# Usually your first call to the API includes the API key.
# This will allow you access to the API.
# In many APIs, you may get charged for each call, sol like your password you should keep your API key a secret.

# End points is simply the location of the service. Its used to find the API on the internet just like a web address.

# - Watson Speech to Text

# !pip install ibm_watson wget
# Import SpeechToTextV1 from IBM Watson
# Primero importamos SpeechToTextV1 de ibm_watson.
from ibm_watson import SpeechToTextV1
import json
# service endpoint is based on:
# se basa en la ubicación de la instancia de servicio, almacenamos la información en la URL variable
url_s2t = ""
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# my api key
iam_apikey_s2t = ""

# speech to text adapter object, the parameters are the endpoint and API key:
# crear un objeto adaptador de voz a texto, los parámetros son el punto final y la clave API.
# This object communicate with the Watson Speech to Text service
# s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url=url_s2t)
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# wav file to convert to text
# !wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3
filename="PolynomialRegressionandPipelines.mp3"

# Creamos el objeto wav con el archivo wav usando open 
# File object create -> open file in binary format, fijamos el modo en "rb" , esto es similar al modo de lectura, pero asegura que el archivo está en modo binario.
# usamos el método recognize para devolver el texto reconocido. 

# audio=wav => the file object, el parámetro audio es el archivo objeto wav, 
# content_type => the audio file formatel parámetro tipo_contenido es el formato del archivo de audio

with open(filename, mode="rb") as wav:
    # from the speech to text adapter object send the audio to the watson services
    # Objet response is where stored the response that server send 
    response = s2t.recognize(audio=wav, content_type="audio/mp3")

    # The attribute result contains a dictionary that includes the translation:
    response.result

from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")    

response
    # result => The key results value has a list that contains a dictionary  
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)   
    # recognized_text: containt a string with a transcribed text "hello this is python "

# Language Translator

# Import Language Translator V3 from ibm_watson
from ibm_watson import LanguageTranslatorV3

# Assign the service endpoint to the variable url_l2 to obtain the service
url_lt = ""
# API key
apikey_lt = ''
# requires the date of the version
version_lt = '2018-05-01'
# language translation object LanguageTranslator
# language_translator = LanguageTranslatorV3(iam_apikey=apikey_lt, url=url_lt, version=version_lt)
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas.io.json import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
# the method return the language code of a list of the languages that the service can identify
# English "en" to Spanish "es"
# Méthod translate to traslate the text
# translation_response is an object detailed response
translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
translation_response
# text=recognized_text => Is the text 
# model_id='en-es' => Is the type of model to translate Englihs to Spanish
# Get the trasnlated text and assign it to the variable translation
translation = translation_response.get_result()
translation
# The result is a dictionary that includes the translation word count and character count 
# We can obtain the translation and assign it to the variable spanish_translation
spanish_translation = translation['translations'][0]['translation']
spanish_translation
# translate back to English
translation_new = language_translator.translate(text=spanish_translation, model_id='es-en').get_result()
# obtain the translation and assign it to the variable
translation_eng = translation_new['translations'][0]['translation']
translation_eng
# translate to French 
French_translation = language_translator.translate(text=translation_eng, model_id='en-fr').get_result()
French_translation
# - Watson Translate
 # obtain the translation and assign it to the variable
French_translation = translation_new['translations'][0]['translation']
French_translation                          
# # =============================================================================