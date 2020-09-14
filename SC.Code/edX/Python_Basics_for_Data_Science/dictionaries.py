#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT

Created on Fri Sep 11 13:33:22 2020

@author: scelis - ¯\_(ツ)_/¯

Dictionary has keys and values 
keys = index, has addresses, don't have to be integers, UNIQUE and IMMUTABLE
that are used to access values within a dictionary, The keys can be strings
values = elements and contain information are MUTABLE and DUPLICATES, multiple keys can hold the same value.
dictionary is enclosed in curly braces {}
Each key is separated from its value by a colon ":"
Commas separate the items
dictionaries.py
"""


# Create the dictionary

Dict = {} # Dictionary vacio
print(Dict)
type(Dict)

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict
# {'key1': 1,
#  'key2': '2',
#  'key3': [3, 3, 3],
#  'key4': (4, 4, 4),
#  'key5': 5,
#  (0, 1): 6}

# Access to the value by the key
Dict["key1"] # 1

Dict[(0, 1)] # 6

version_peliculas_dict = {
                            'Thriller': '1982',
                            'Back in Black': '1980',
                            'The Dark Side of the Moon': '1973',
                            'The Bodyguard': '1992',
                            'Bat Out of Hell': '1977',
                            'Their Greatest Hits (1971-1975)': '1976',
                            'Saturday Night Fever': '1977',
                            'Rumours': '1977'}
 
type(version_peliculas_dict)  # dict                 

# Access to the value by the key
version_peliculas_dict['Thriller'] # '1982'

# Get all the keys in dictionary - the method keys()
version_peliculas_dict.keys() 
# return a list:
# dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])

# Get all the values in dictionary - the method values() 
# return a list:
version_peliculas_dict.values() 
# dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

# Append, add, insert value with key into dictionary
version_peliculas_dict['Graduation'] = '2007'
version_peliculas_dict
# {'Thriller': '1982',
#  'Back in Black': '1980',
#  'The Dark Side of the Moon': '1973',
#  'The Bodyguard': '1992',
#  'Bat Out of Hell': '1977',
#  'Their Greatest Hits (1971-1975)': '1976',
#  'Saturday Night Fever': '1977',
#  'Rumours': '1977',
#  'Graduation': '2007'}

# Delete entries by key
del(version_peliculas_dict['Thriller'])
del(version_peliculas_dict['Graduation'])
version_peliculas_dict
# {'Back in Black': '1980',
#  'The Dark Side of the Moon': '1973',
#  'The Bodyguard': '1992',
#  'Bat Out of Hell': '1977',
#  'Their Greatest Hits (1971-1975)': '1976',
#  'Saturday Night Fever': '1977',
#  'Rumours': '1977'}

# We can verify "find" if an element is in the dictionary
# Verify the key is in the dictionary
print("The Bodyguard IN the dict?: ", 'The Bodyguard' in version_peliculas_dict)
# The Bodyguard IN the dict?:  True      
