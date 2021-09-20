#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# mutable.assignment.py

x en la función se establece para apuntar al objeto llamador por la llamada a la función y 
dentro del cuerpo de la función, CAMBIAMOS A x , en el sentido de que estamos cambiando su referencia, o, 
en otras palabras, estamos cambiando el objeto al que apunta x ahora es un String.

"""

# mutable.assignment.py
x = [1, 2, 3]

def func(x):
    x[1] = 42                           # this changes the caller!
    x = 'something else'                # this points x to a new string object

func(x)
print(x) # still prints: [1, 42, 3]