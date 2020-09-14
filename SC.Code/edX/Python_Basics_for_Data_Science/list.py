#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Sep 10 18:28:17 2020

@author: scelis - ¯\_(ツ)_/¯

List are an ordered sequence - MUTABLE, as comma-separated within parentheses []

integers, strings, float and other lists pueden ser contenidos en una list
list.py
"""

# The address of each element within a list is called an index
# Indexing
# the list within square brackets [ ], with your content inside the parenthesis and separated by commas
# We can use negative and regular indexing
L=["Michael Jackson", 10.1, 1982]
# 'Michael Jackson'
L[0]
L[-3]

# 10.1
L[1]
L[-2]

# 1982
L[2]
L[-1]

# We can nest other lists - listas anidadas
L=["Michael Jackson", 10.1, 1982, [1,2],('A',1)]
# 'Michael Jackson'
L[0]
# 10.1
L[1]
# 1982
L[2]
# [1, 2]
L[3]
# 1
L[3][0]
# 2
L[3][1]

# ('A', 1)
L[4]
# 'A'
L[4][0]
# 1
L[4][1]

# Slicing -  the last two elements
L[3:5] # [[1, 2], ('A', 1)]

# Concatenar una lista con (+)
L1=L+["pop", 10] # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'pop', 10]

A1 = [1, 'a']
B1= [2, 1, 'd']
A1 = A1+B1
A1 # [1, 'a', 2, 1, 'd']

# extend lo que hace es add dos elementos a la lista existente
# add new elements to the list
L.extend(["rock",20]) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'rock', 20]

# Use extend to add elements to list - we apply extend we add two new elements to the list
L2 = [ "Michael Jackson", 10.2]
L2.extend(['pop', 10])
L2 # ['Michael Jackson', 10.2, 'pop', 10]

A2 = [1, 'a']
B2 = [2, 1, 'd']
A2.extend(B2)
A2 # [1, 'a', 2, 1, 'd']

# we apply append add one element to the list - have one new element 
L.append(["rock",20]) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'rock', 20, ['rock', 20]]

L.append(["pop",10])
# ['Michael Jackson',
#  10.1,
#  1982,
#  [1, 2],
#  ('A', 1),
#  'rock',
#  20,
#  ['rock', 20],
#  ['pop', 10]]

# we have one new element 
L3 = [ "Michael Jackson", 10.2]
L3.append(['a','b'])
L3 # ['Michael Jackson', 10.2, ['a', 'b']]
len(L3)
type(L3)
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Antes cambio:', A) # Antes cambio: ['disco', 10, 1.2]
A[0] = 'hard rock'
print('Después cambio:', A) # Después cambio: ['hard rock', 10, 1.2]

# elimina, borra un elemento de la lista
print('Antes cambio:', A) # Antes cambio: ['hard rock', 10, 1.2]
del(A[1])
print('Después cambio:', A) # Después cambio: ['hard rock', 1.2] 


# split - Convert String to list, # Split the string, default is by space ""
"Michael Jackson".split() # ['Michael', 'Jackson']

# Split the string by comma
"A,B,C,D".split(",") # ['A', 'B', 'C', 'D']

# When we set one variable B equal to A; both A and B are referencing the same list in memory:
# Alias, are reference at the same list

A=["hard rock", 10,1.2]
B=A
print('A:', A) # A: ['hard rock', 10, 1.2]
print('B:', B) # B: ['hard rock', 10, 1.2]

A[0] # 'hard rock'
# ['hard rock', 10, 1.2]
B[0] # 'hard rock'

# Examine the copy by reference
print('B[0]:', B[0]) # B[0]: hard rock
A[0] = "banana"
print('B[0]:', B[0]) # B[0]: banana


# Clone, crea una new list, reference a diferentes list
# Clone (clone by value) the list A then Variable B references a new copy or clone of the original lis
A=["hard rock", 10,1.2]
print('A:', A) # A: ['hard rock', 10, 1.2]
B=A[:]
print('B:', B) # B: ['hard rock', 10, 1.2]

print('A:', A) # A: ['hard rock', 10, 1.2]
print('A[0]:', A[0]) # A[0]: banana
print('B[0]:', B[0]) # B[0]: hard rock

# Change the first element of the list to an uppercase 
B[0].upper() # 'HARD ROCK'

# Help on class list in module builtins: 
help(A)
# or
help(list)
# because
type(A) # list

