#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# return.none.py

pass es una operación nula. 
cuando se ejecuta, no ocurre nada sucede. 
es útil como marcador de posición cuando se requiere una declaración sintáctica, pero no es necesario ejecutar ningún código.

"""
# return.none.py
def func():
    pass

func()          # el retorno de esta llamada no se recoge. Se pierde..
a = func()      # el retorno de esta en cambio se recoge en `a`
print(a)        # imprime: None