#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# assignment.py

Cuando se ejecuta la línea x = 7, dentro del ámbito local de la función func, x , apunta a un entero con un valor de 7 , 
el global no se modifica.
"""

x = 3
def func(x):
    x = 7 # defining a local x, not changing the global one

func(x)
print(x) # prints: 3
