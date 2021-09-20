#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.default.py

la contrapartida, son los valores por defecto. 
sintaxis es la misma, name=value , y nos permite no tener que proporcionar un argumento si

"""
# arguments.default.py

def func(a, b, c):
    print(a, b, c)

func(a=1, b=2, c=3)         # imprime: 1 2 3
func(a=1, c=2, b=3)         # imprime: 1 3 2 - sigue el orden de la firma de la función
func(c=1, b=2, a=3)         # imprime: 3 2 1 - sigue el orden de la firma de la función
#func(1)                    # TypeError: func() missing 2 required positional arguments: 'b' and 'c'
func(b=5, a=7, c=9)         # imprime: 7 5 9 - sigue el orden de la firma de la función
#func(42, c=9)              # TypeError: func() missing 1 required positional argument: 'b'
func(42, 43, 44)            # imprime: 42, 43, 44 - sigue el orden de la firma de la función

