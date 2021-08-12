#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:14:01 2021

@author: Fabrizio Romano
transcript: SCelis

# simple.for.2.py
len(surnames) is the length of the surnames list
range(len(surnames)) is actually transformed into range(3)
This gives us the range [0, 3), which is basically a sequence ( 0 , 1 , 2 ).
Rivest-Shamir-Adleman (RSA) algorithm

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
surnames = ['Rivest', 'Shamir', 'Adleman']
for name in surnames:
    print(name)
for position in range(len(surnames)):
    print(position, surnames[position])
for position in range(len(surnames)):
    print(surnames[position][0], end='')
print()
