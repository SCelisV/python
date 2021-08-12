#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:32:55 2021

@author: Fabrizio Romano
transcript: SCelis

# ternary.2.py
# classic if/else form
# /home/hadoop/SCProjects/learn.pp/learnpp

Conditional programming
"""

ORDER_TOTAL = 247
if ORDER_TOTAL > 100:
    DISCOUNT = 25
else:
    DISCOUNT = 0
print(ORDER_TOTAL, DISCOUNT)
