#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fabrizio Romano
transcript: SCelis

# functions.defining.ideal.py

Pythonic form

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/

"""
def do_report(data_source):
    # fetch and prepare data
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)
    
    
# run algorithms on data
final_data = analyse(polished_data)

# create and return report
report = Report(final_data)
return report

