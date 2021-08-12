#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:02:20 2021

@author: Fabrizio Romano
transcript: SCelis

# multiple.sequences.while.py
We want to print a pair person/age on one line for all of the both list

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""

# multiple.sequences.while.py
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
POSITION = 0
while POSITION < len(people):
    PERSON = people[POSITION]
    AGE = ages[POSITION]
    print(PERSON, AGE)
    POSITION += 1
    