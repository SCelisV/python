#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:32:55 2021

@author: Fabrizio Romano
transcript: SCelis

# ternary.py
name = something if condition else something-else

name is assigned something if condition evaluates to True, and
name is assigned something-else if condition evaluates to False

# /home/hadoop/SCProjects/learn.pp/learnpp

Conditional programming
"""

ORDER_TOTAL = 247                               # GBP
# ternary operator
DISCOUNT = 25 if ORDER_TOTAL > 100 else 0
print(ORDER_TOTAL, DISCOUNT)
