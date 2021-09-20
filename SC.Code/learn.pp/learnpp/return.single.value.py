#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# return.single.value.py

la función tiene dos return, pero retorn un valor único

"""
# return.single.value.py

def factorial(n):
    if n in (0, 1):             # el factorial de 0 y de 1 es 1
        return 1
    result = n
    for k in range(2, n):       # se calcula el factorial a partir de 2 hasta n
        result *= k
    return result

f5 = factorial(5)
print(f5)                       #   120