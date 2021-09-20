#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.variable.positional.unpacking.py

"""

# arguments.variable.positional.unpacking.py

def func(*args):                # using the * syntax, unpacking
    print(args)
values = (1, 3, 2, -8.0, -7, 9)
func(values)                    # equivalent to: func((1, 3, 2, -8.0, -7, 9),)
                                # llamamos a la función con una tupla de seis elementos - imprime -8.0
func(*values)                   # equivalent to: func(1, 3, 2, -8.0, -7, 9) -  unpacking, 
                                # lo que significa que la tupla de seis elementos es desempaquetada y 
                                # llamamos a la función con seis elementos - imprime -8.0