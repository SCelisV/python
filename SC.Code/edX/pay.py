#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Jun 26 18:35:39 2020

@author: scelis
"""

#Calcula el pago de las horas trabajadas
hour = input("Digite el número de horas que ha trabajado: ")
cost = input("Digite el precio de la hora de trabajo: ")
pay = float(hour) * float(cost)
print("Vas a recibir un pago de: ", pay)