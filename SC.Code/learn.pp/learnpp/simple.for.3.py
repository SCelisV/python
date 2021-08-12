#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:28:05 2021

@author: Fabrizio Romano
transcript: SCelis

# simple.for.3.py
Pythonic form: there is no need to get the list of positions and retrieve elements out of a
sequence at each iteration.
The for loop can iterate over the surnames list,
and it gives back each element in order at each interaction

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# simple.for.3.py
surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)
