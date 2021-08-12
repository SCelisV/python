#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:32:55 2021

@author: Fabrizio Romano
transcript: SCelis

# taxes.2.py
If my INCOME is less than $10,000, I won't pay any taxes
If it is between $10,000 and $30,000, I'll pay 20% in taxes.
If it is between $30,000 and $100,000, I'll pay 35% in taxes, and
if it's over $100,000, I'll (pay 45% in taxes.
Change some < to <= and set income to be one of the boundary values (10,000, 30,000, 100,000)
# /home/hadoop/SCProjects/learn.pp/learnpp

Conditional programming
"""
INCOME = 100000
#1 if expression of income < 10000 evaluates to False #1 is not executed.
if INCOME < 10000:
    TAX_COEFFICIENT = 0.0
#2 elif income < 30000 . This one evaluates to True , therefore block #2 is executed,
#  entonces pyton reanuda la ejecución después de toda la clausula if / elif / elif / else
#  se ejecuta el print(mandatory)
elif INCOME <= 30000:
    TAX_COEFFICIENT = 0.20
#3
elif INCOME <= 100000:
    TAX_COEFFICIENT = 0.35
#4 Its blocko f code is executed when none of the preceding
#  if / elif /.../ elif expressions
#  has evaluatedto True
else:
    TAX_COEFFICIENT = 0.45
print('I will pay:', INCOME * TAX_COEFFICIENT, 'in taxes')
