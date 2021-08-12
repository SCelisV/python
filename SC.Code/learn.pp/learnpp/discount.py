#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:21:57 2021

@author: Fabrizio Romano
transcript: SCelis

# discount.py
you want to apply a 20% discount to all products in a basket list for those that
have an expiration date of today.
The way you achieve this is to use the continue statement,
which tells the looping construct ( for or while ) to stop execution of the body
immediately and go to the next iteration, if any.

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# discount.py
#/home/hadoop/anaconda3/lib/python3.8/datetyme
from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days=1)    # today + 1 day is tomorrow
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8             # equivalent to applying 20% discount
    print(
        'Price for sku', product['sku'], 'is now', product['price'])
    