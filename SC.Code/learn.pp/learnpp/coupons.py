#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:20:42 2021

@author: Fabrizio Romano
transcript: SCelis

# coupons.py
assigns a discount to customers based on their coupon value

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# coupons.py
customers = [
    dict(id=1, total=200, coupon_code="F20"),  # F20: Fixed, 20€
    dict(id=2, total=150, coupon_code="P30"),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code="P50"),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code="F15"),  # F15: Fixed, 15€
    ]
for customer in customers:
    CODE = customer['coupon_code']
    if CODE == 'F20':
        customer['discount'] = 20.0
    elif CODE == 'F15':
        customer['discount'] = 15.0
    elif CODE == 'P30':
        customer['discount'] = customer['total'] * 0.30
    elif CODE == 'P50':
        customer['discount'] = customer['total'] * 0.50
    else:
        customer['discount'] = 0.0
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
    