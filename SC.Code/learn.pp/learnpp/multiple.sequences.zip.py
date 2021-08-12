#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:02:20 2021

@author: Fabrizio Romano
transcript: SCelis

# multiple.sequences.zip.py
We want to print a pair person/age on one line for all of the both list
better Pythonic form
we're still fetching age using positional indexing,
Python gives you the zip function
notice that when the for loop asks zip(sequenceA, sequenceB) for the next element,
it gets back a tuple, not just a single object.
It gets back a tuple with as many elements as the number of sequences we feed to the zip function

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
for person, age in zip(people, ages):
    print(person, age)
    