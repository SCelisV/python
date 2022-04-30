#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: SCelis

# test_03.py
# some test
# SC.Code/learn.pp/learnpp/SkillAssessments

"""
lst_1 = [1,2,3]
for x in lst_1:
    print("x*2: " , x*2) 
    print("x%2: " , x%2) 
    """
x*2:  2
x%2:  1
x*2:  4
x%2:  0
x*2:  6
x%2:  1
    """
lst_2 = [x*2 for x in lst_1 if x%2 == 0]

print("lst_1: ", lst_1) # lst_1:  [1, 2, 3]
print("lst_2: ", lst_2) # lst_2:  [4]

