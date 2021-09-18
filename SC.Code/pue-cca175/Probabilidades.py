from numpy import random
random.seed(0)

"""
NO ESTOY DE ACUERDO
"""
"""
Probabilidad condicionada

Tomando los casos en los que B se cumple, P ( A ∣ B ) se puede interpretar como la parte en los que también se cumple A

         P(A∩B)    P(A) P(B) 
P(A|B) = ------- = ---------
           P(B)       P(B)  
"""
# veces que alguien ha visitado la tienda (compre o no),
totales = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}

# veces que alguien de un rango de edad realiza una compra
compras = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}

#print("type(totales):", type(totales), " totales: ", totales)
#print("type(compras):", type(compras), " compras: ", compras)
"""
type(totales): <class 'dict'>  totales:  {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
type(compras): <class 'dict'>  compras:  {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
"""
totalcompras = 0
n_range = 10000
years = 100.0
for _ in range(n_range):
    edadDecada = random.choice([20, 30, 40, 50, 60, 70])     #   asigna aleatoriamente
    #print("edadDecada: ", edadDecada)
    probabilidadCompra = float(edadDecada) / years         # cast a float
    #print("probabilidadCompra = float(edadDecada) / 100.0: ", probabilidadCompra)
    totales[edadDecada] += 1                                # aumenta en uno el total de la decada seleccionada
    #print("totales: ", totales)
    if (random.random() < probabilidadCompra):              # Si el numero random generado "es decir, compra", es menor que la probabilidad de compra
        #print("random.random(): ", random.random())
        #print("random.random() < probabilidadCompra: ", random.random() < probabilidadCompra)
        totalcompras += 1
        #print("totalcompras: ", totalcompras)               # aumenta el total de las compras
        compras[edadDecada] += 1
        #print("compras[edadDecada]: ", compras[edadDecada]) # aumenta las compras en esa decada

"""

edadDecada:  60
probabilidadCompra = float(edadDecada) / 100.0:  0.6
totales:  {20: 0, 30: 0, 40: 0, 50: 0, 60: 1, 70: 0}            
random.random():  0.8442657485810173
random.random() < probabilidadCompra:  False
totalcompras:  1
compras[edadDecada]:  1
edadDecada:  30
probabilidadCompra = float(edadDecada) / 100.0:  0.3
totales:  {20: 0, 30: 1, 40: 0, 50: 0, 60: 1, 70: 0}
edadDecada:  40
probabilidadCompra = float(edadDecada) / 100.0:  0.4
totales:  {20: 0, 30: 1, 40: 1, 50: 0, 60: 1, 70: 0}
edadDecada:  20
probabilidadCompra = float(edadDecada) / 100.0:  0.2
totales:  {20: 1, 30: 1, 40: 1, 50: 0, 60: 1, 70: 0}
edadDecada:  40
probabilidadCompra = float(edadDecada) / 100.0:  0.4
totales:  {20: 1, 30: 1, 40: 2, 50: 0, 60: 1, 70: 0}
edadDecada:  20
probabilidadCompra = float(edadDecada) / 100.0:  0.2
totales:  {20: 2, 30: 1, 40: 2, 50: 0, 60: 1, 70: 0}
edadDecada:  30
probabilidadCompra = float(edadDecada) / 100.0:  0.3
totales:  {20: 2, 30: 2, 40: 2, 50: 0, 60: 1, 70: 0}
random.random():  0.08712929970154071
random.random() < probabilidadCompra:  True
totalcompras:  2
compras[edadDecada]:  1
edadDecada:  50
probabilidadCompra = float(edadDecada) / 100.0:  0.5
totales:  {20: 2, 30: 2, 40: 2, 50: 1, 60: 1, 70: 0}
edadDecada:  20
probabilidadCompra = float(edadDecada) / 100.0:  0.2
totales:  {20: 3, 30: 2, 40: 2, 50: 1, 60: 1, 70: 0}
edadDecada:  20
probabilidadCompra = float(edadDecada) / 100.0:  0.2
totales:  {20: 4, 30: 2, 40: 2, 50: 1, 60: 1, 70: 0}

"""

"""
Probabilidad de tener 30 años ( suponiendo que podemos tener 100 años)
( 30 / 100 ) = 0.3

Probabilidad de comprar algo: ( totalcompras / n_range )

1- Calcular la probabilidad condicionada de que un sujeto realice una compra sabiendo que
pertenece al rango de los 30 años de edad

         P(A∩B)    P(A) P(B) 
P(A|B) = ------- = ---------
           P(B)       P(B)  
    
compras [30] / totales [30]

"""