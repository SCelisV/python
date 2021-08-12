#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:45:18 2021

@author: Fabrizio Romano
transcript: SCelis

# switch.py

switch / case , that in Python is missing but
is perfectly capable of realizing such logic using if / elif / else statements.

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# switch.py
DAY_NUMBER = 4
if 1 <= DAY_NUMBER <= 5:
    DAY = 'Weekday'
elif DAY_NUMBER == 6:
    DAY = 'Saturday'
elif DAY_NUMBER == 0:
    DAY = 'Sunday'
else:
    DAY = ''
    raise ValueError(str(DAY_NUMBER) + ' is not a valid day number.')
print(DAY)

    