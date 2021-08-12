#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:23:40 2021

@author: Fabrizio Romano
transcript: SCelis

# compress.py
This iterator gives you back the data according to
a corresponding item in a selector being True or False :

compress('ABC', (1, 0, 1)) would give back 'A' and 'C', because they correspond to 1

0 (for false)
1 (for true)

Notice that ODD_SELECTOR and ODD_SELECTOR are 20 elements long,
while DATA is just 10 elements long
compress se detendrá en cuanto DATA haya terminado

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# compress.py
from itertools import compress
DATA = range(10)                        #  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
EVEN_SELECTOR = [1, 0] * 10             # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
ODD_SELECTOR = [0, 1] * 10              # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

EVEN_NUMBERS = list(compress(DATA, EVEN_SELECTOR))  # [0, 2, 4, 6, 8]
ODD_NUMBERS = list(compress(DATA, ODD_SELECTOR))    # [1, 3, 5, 7, 9]

print(EVEN_SELECTOR)
print(ODD_SELECTOR)
print(list(DATA))
print(EVEN_NUMBERS)
print(ODD_NUMBERS)
