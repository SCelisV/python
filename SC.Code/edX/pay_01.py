#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:00:13 2020
IN-WORK-OUT
@author: scelis
"""

#Calcula el pago de las horas trabajadas

sh = input("Digite el número de horas que ha trabajado: ")
sp = input("Digite el precio de la hora de trabajo: ")
fh = float(sh)
fp = float(sp)

print (fh, fp)

if fh > 40:
#   calculo del total de horas: regulares
    hr = fh * fp
#   calculo del Overtime - Horas Extras
    he = (fh - 40.0) * ( fp * 0.5)
#   calculo del total de horas: regulares +  extras
    th = hr + he
else:
#   calculo del total de horas: regulares
    hr = fh * fp
    th = hr
 
print("Vas a recibir un pago de: ", th)