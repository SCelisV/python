# -*- coding: utf-8 -*-
"""
transcript: SCelis

# vat.function.py

toma los valores de entrada (iva, and precio-sin-iva) y devuelve el precio-con-iva

# diferentes formas de calcular el precio con iva
price = 100
print("price * 1.2 = ", price * 1.2)
print("price + price / 5.0 = ", price + price / 5.0)
print("price * (100 + 20)/100 = ", price * (100 + 20)/100)
print("price + price * 0.2 = ", price * 0.20)


Pythonic form

"""

# vat.function.py
# price and vat are integers
def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100

# iva is a valor en porcentaje
print(calculate_price_with_vat(100, 20))
