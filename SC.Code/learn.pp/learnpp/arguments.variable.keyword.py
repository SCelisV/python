#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.variable.keyword.py

"""
# arguments.variable.keyword.py

def func(**kwargs):          # este parámetro recogerá un número variable de parámetros de clave
    print(kwargs)

# podemos pasar los argumentos name=value explícitamente, o desempaquetar un diccionario usando la misma sintaxis **.  

# Todas las llamadas son equivalentes. They print: {'a': 1, 'b': 42}
func(a=1, b=42)                     # imprime {'a': 1, 'b': 42}
func(**{'a': 1, 'b': 42})           # imprime {'a': 1, 'b': 42}
func(**dict(a=1, b=42))             # imprime {'a': 1, 'b': 42}

func(**dict(b=42, a=1))             # imprime {'b': 42, 'a': 1}
func(**{'b':42, 'a': 1})            # imprime {'b': 42, 'a': 1}