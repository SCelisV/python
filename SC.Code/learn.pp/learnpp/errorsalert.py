#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:32:55 2021

@author: Fabrizio Romano
transcript: SCelis

# errorsalert.py
Say your program encounters an error. If the alert system is the console, we print the error.
If the alert system is an email, we send it according to the severity of the error.
If the alert system is anything other than console or email,
we don't know what to do, therefore we do nothing
# /home/hadoop/SCProjects/learn.pp/learnpp

Conditional programming
"""
# other value can be 'email'
ALERT_SYSTEM = 'email'
# other values: 'medium' or 'low'
ERROR_SEVERITY = 'low'
ERROR_MESSAGE = 'OMG! Something terrible happened!'

if ALERT_SYSTEM == 'console':
    print(ERROR_MESSAGE)
elif ALERT_SYSTEM == 'email':
    if ERROR_SEVERITY == 'critical':
        print('admin@example.com', ERROR_MESSAGE)
    elif ERROR_SEVERITY == 'medium':
        print('support.1@example.com', ERROR_MESSAGE)
    else:
        print('support.2@example.com', ERROR_MESSAGE)
