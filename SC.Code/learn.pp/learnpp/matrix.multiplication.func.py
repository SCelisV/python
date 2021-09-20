#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

#matrix.multiplication.func.py

Pythonic form

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/matrix.multiplication.func.py

"""
# this function could also be defined in another module

def matrix_mult(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]

# list(zip(r, c)) --> ver el contenido

a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

print("matrix_mult: ", matrix_mult(a, b))   # matrix_mult:  [[9, 3], [23, 7]]
