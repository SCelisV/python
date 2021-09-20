#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.variable.positional.py

Calcula el minimo de los valores pasados como parámetros
"""

# arguments.variable.positional.py

def minimum(*n):                # este parámetro recogerá un número variable de argumentos posicionales (*)
    # print(type(n))            # n is a tuple
    if n:                       # si n no está vacío, objetos (tuplas, listas, set, dict), se evalúan como True cuando no están vacíos
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3,  2, -8.0, -7, 9)  # llamamos a la función con seis elementos - imprime -8.0
minimum()                       # no imprime nada, se podría mejorar la función lanzando un error cuando se llame a la función sin argumentos
             