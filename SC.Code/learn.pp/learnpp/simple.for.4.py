#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:36:42 2021

@author: Fabrizio Romano
transcript: SCelis

# simple.for.4.py
if you wanted to print the position Or
if you actually needed it?
You can use the enumerate built-in function
enumerate(surnames) devuelve una tupla position, en cada iteración:
Se puede llamar a enumerate con un parámetro como enumerate(iterable, start),
y empezará desde start, en lugar de 0.

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# simple.for.4.py
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)
for position, surname in enumerate(surnames):
    print(surnames[position][0], end='')
