#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.keyword.py

se asignan por palabra clave utilizando la sintaxis nombre=valor,  incluso cuando no respetan la posición original de la definición

"""
# arguments.keyword.py

def func(a, b, c):
    print(a, b, c)

func(c=1, b=2, a=3) # prints: 3 2 1 - sigue el orden de la firma de la función