#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:50:27 2021

@author: Fabrizio Romano
transcript: SCelis

# permutations.py

there are six permutations of ABC: ABC, ACB, BAC, BCA, CAB, and CBA

If a set has N elements, then the number of permutations of them is N! (N factorial).
For the ABC string, the permutations are 3! = 3 * 2 * 1 = 6.

--O-J-O--
El número crece proporcionalmente
al factorial del número de elementos de la permutación y
puede ser muy grande, y muy rápido

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""

# permutations.py
from itertools import permutations
print(list(permutations('ABC')))
