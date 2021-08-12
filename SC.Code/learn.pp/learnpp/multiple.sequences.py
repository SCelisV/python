#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:02:20 2021

@author: Fabrizio Romano
transcript: SCelis

# multiple.sequences.py
We want to print a pair person/age on one line for all of the both list

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)
    