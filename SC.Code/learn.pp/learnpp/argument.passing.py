#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# argument.passing.py

func se llama con x , dentro de su ámbito local, se crea y , y se apunta a el mismo objeto al que apunta x

"""
x = 3
def func(y):
    print(y)

func(x)             # prints: 3
