#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.keyword.only2.py

sus casos de uso no son tan frecuentes. 
Hay dos formas de especificarlas, 
- después de un simple *

"""

# arguments.keyword.only2.py

def kwo(a, b=42, *, c):         # recibe un argumento posicional ( a ) , un keyword argument ( b) , y un keyword-only, ( c )
    print(a, b, c)

kwo(3, b=7, c=99)       # prints: 3 7 99
kwo(3, c=13)            # prints: 3 42 13
kwo(3, 23)              # TypeError: kwo() missing 1 required keyword-only argument: 'c'
