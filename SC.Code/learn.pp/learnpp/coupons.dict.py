#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:46:19 2021

@author: Fabrizio Romano
transcript: SCelis

# coupons.dict.py
assigns a discount to customers based on their coupon value
Pythonic form
intentamos obtener algo del diccionario basado en un código
(nuestro código_de_cupón ), y utilizando dict.get(key, default) ,
nos aseguramos de que también se puede utilizar
cuando el código no está en el diccionario y necesitamos un valor por defecto

aplicando el porcentaje * total + fijo ,
obtenemos el descuento correcto.
Cuando porcentaje es 0 , la fórmula sólo da la cantidad fija,
y da porcentaje * total cuando el fijo es 0 .

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# coupons.dict.py
customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, 20€
    dict(id=2, total=150, coupon_code="P30"),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code="P50"),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code="F15"),  # F15: Fixed, 15€
    ]
discounts = {
    'F20': (0.0, 20.0),                        # each value is (percent, fixed)
    'P30': (0.3, 0.0),
    'P50': (0.5, 0.0),
    'F15': (0.0, 15.0),
    }
for customer in customers:
    CODE = customer['coupon_code']
    PERCENT, FIXED = discounts.get(CODE, (0.0, 0.0))
    customer['discount'] = PERCENT * customer['total'] + FIXED
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
    