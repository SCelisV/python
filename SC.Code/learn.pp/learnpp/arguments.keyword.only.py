#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.keyword.only.py

sus casos de uso no son tan frecuentes. 
Hay dos formas de especificarlas, 
- ya sea después de los argumentos posicionales de las variables, o 

"""

# arguments.keyword.only.py

def kwo(*a, c):             # recibe un número variable de argumentos posicionales ( a ) y un keyword-only , ( c )
    print(a, c)

kwo(1, 2, 3, c=7)           # prints: (1, 2, 3) 7
kwo(c=4)                    # prints: () 4

kwo(1, 2)       # TypeError: kwo() missing 1 required keyword-only argument: 'c'            