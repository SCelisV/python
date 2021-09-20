#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.default.error.py


"""
# arguments.default.error.py

def func(a, b=4, c=88):
    print(a, b, c)

func(1, c=2, b=42)          # 1 42 2 - el paso de valores de forma posicional - sigue el orden de la firma de la función - 
func(1, c=2, a=42)          # TypeError: func() got multiple values for argument 'a' 
#func(b=1, c=2, 42)          # Error de sintaxis