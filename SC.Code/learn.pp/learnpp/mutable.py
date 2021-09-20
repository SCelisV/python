#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# mutable.py

x en la función se establece para apuntar al objeto llamador por la llamada a la función y 
dentro del cuerpo de la función, no estamos cambiando x , en el sentido de que no estamos cambiando su referencia, o, 
en otras palabras, no estamos cambiando el objeto al que apunta x.

Estamos accediendo al elemento de ese objeto en la posición 1, y cambiando su valor

"""

x = [1, 2, 3]       # las listas son mutables

def func(x):
    x[1] = 42 # this affects the caller!

func(x)
print(x) #          prints: [1, 42, 3]