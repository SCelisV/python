#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT

Created on Fri Sep 11 11:27:11 2020

@author: scelis - ¯\_(ツ)_/¯


Sets - Conjuntos
Collection UNORDERED, with a curly bracket {}. Python will automatically remove duplicate items

like lists y tuplas integers, strings, float and other types of python pueden ser contenidos en una list

only one of a particular element in a set = no repetidos
sets.py
"""

# Created
Set = {"pop", "rock", "soul", "hard" "rock", "rock", "R&B", "disco", "latina"}
# {'R&B', 'disco', 'hardrock', 'latina', 'pop', 'rock', 'soul'}

# Convertir una lista en un set - cast - # Convert list to set

L=["Michael Jackson", 10.1, 1982]
Set_L = set(L) # cast 
type(Set_L) # set
len(Set_L)



album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
type(album_list) # list
album_set = set(album_list) 
album_set
# {'00:42:19',
#  10.0,
#  1982,
#  '30-Nov-82',
#  46.0,
#  65,
#  'Michael Jackson',
#  None,
#  'Pop, Rock, R&B',
#  'Thriller'}
type(album_set) # set   

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])

music_genres
# {'R&B',
#  'disco',
#  'folk rock',
#  'hard rock',
#  'pop',
#  'progressive rock',
#  'rock',
#  'soft rock',
#  'soul'}
type(music_genres) # set

# Set operations

# Add Method insert a new item in a set, not duplicate, # Add element to set
# If we add the same element twice, nothing will happen as there can be no duplicates in a set
A = {"Thriller", "Back in Black", "AC/DC"}
A.add("NSYNC")
print("Set A: ", A) # Set A:  {'NSYNC', 'Thriller', 'AC/DC', 'Back in Black'}

# Remove, del a item from a set, # Remove the element from set
A.remove("NSYNC") 
print("Set A: ", A) # Set A:  {'Thriller', 'AC/DC', 'Back in Black'}
A.remove("NSYNC") # if not exist => return KeyError: 'NSYNC'

# IN, saber si hay un elemento en el conjunto, We can verify "find" if an element is in the set 

"AC/DC" in A # True
"NSYNC" in A # False

# Sets Logic Operations, Mathematical operations

album_set_1 = {"Thriller", "Back in Black", "AC/DC"}
print("Set album_set_1: ", album_set_1) # Set album_set_1:  {'Thriller', 'AC/DC', 'Back in Black'}

album_set_2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}
print("Set album_set_2: ", album_set_2) # Set album_set_2:  {'The Dark Side of the Moon', 'AC/DC', 'Back in Black'}

album_set_3 = {"Thriller", "Back in Black", "AC/DC"}
print("Set album_set_3: ", album_set_3) # Set album_set_3:  {'Thriller', 'AC/DC', 'Back in Black'}

album_set_4 = {"The Dark Side of the Moon", "Thriller", "Back in Black", "AC/DC"}
print("Set album_set_4: ", album_set_4) # Set album_set_4:  {"The Dark Side of the Moon", "Thriller", "Back in Black", "AC/DC"}

# intersection = new set = & = esta en set_1 AND en set_2, # Find the intersections
album_intercept = album_set_1 & album_set_2
print("Set intersection: ", album_intercept) # Set intersection:  {'AC/DC', 'Back in Black'}
 
# Use intersection method to find the intersection 
album_set_1.intersection(album_set_2)   
print("Set intersection: ", album_set_1.intersection(album_set_2)) # Set intersection:  {'AC/DC', 'Back in Black'}

# difference in both way, bidirectional 
# You can find all the elements that are only contained in a Set
# Find the difference in set1 but not set2
album_difference = album_set_1 != album_set_2
print("The set's are differents?: ", album_difference) # The set's are differents?:  True
album_difference = album_set_1 != album_set_3
print("The set's are differents?: ", album_difference)

album_set_1.difference(album_set_2)  
print("Set difference: ", album_set_1.difference(album_set_2)) # Set difference:  {'Thriller'}

# The elements in album_set2 but not in album_set1
album_set_2.difference(album_set_1)  
print("Set difference: ", album_set_2.difference(album_set_1)) # Set difference:  {'The Dark Side of the Moon'}


# Union = new set = union = concat - # Find the union of two sets
album_set_1 = {"Thriller", "Back in Black", "AC/DC"}
print("Set album_set_1: ", album_set_1) # Set album_set_1:  {'Thriller', 'AC/DC', 'Back in Black'}
album_set_1.union(album_set_2)
print("Union sets album_set_1: ", album_set_1) # Union sets album_set_1:  {'Thriller', 'AC/DC', 'Back in Black'}

# check if a set is a superset or subset of another set, respectively
# El album_set_3 esta encapsulado en el album_set_1? issubset , incluido
album_set_3 = {"Back in Black", "AC/DC"}
print("Set album_set_3: ", album_set_3) # Set album_set_3:  {'AC/DC', 'Back in Black'}

album_set_4.issubset(album_set_3) 
print("album_set_4, es un subset de album_set_3?: ", album_set_4.issubset(album_set_3)) # album_set_4, es un subset de album_set_3?:  False

album_set_1.issubset(album_set_3) 
print("album_set_1, es un subset de album_set_3?: ", album_set_1.issubset(album_set_3) ) # album_set_1, es un subset de album_set_3?:  True


# Check if superset
set(album_set_4).issuperset(album_set_2)   
print("album_set_4, es un superSet de album_set_2?: ", set(album_set_4).issuperset(album_set_2)) # album_set_4, es un superSet de album_set_2?:  True

set(album_set_2).issuperset(album_set_4)   
print("album_set_2, es un superSet de album_set_4?: ", set(album_set_2).issuperset(album_set_2)) # album_set_2, es un superSet de album_set_4?:  True

# Check if subset
set({"Back in Black", "AC/DC"}).issubset(album_set_1) # True

# Check if superset
album_set_1.issuperset({"Back in Black", "AC/DC"}) # True

# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) = sum(B)
listA = [1, 2, 2, 1]
setA = set(listA)

setB = set([1, 2, 2, 1])

sum_A = sum(setA)
sum_B = sum(setB)

print("sum(A): ", sum_A)
print("sum(B): ", sum_B)

sum_A == sum_B