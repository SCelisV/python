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
           
           
Según Ramón,  de esta forma no influye la edad para realizar una compra.

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
for _ in range(100000):
    edadDecada = random.choice([20, 30, 40, 50, 60, 70])
    probabilidadCompra = 0.4
    totales[edadDecada] += 1
    if (random.random() < probabilidadCompra):
        totalcompras += 1
        compras[edadDecada] += 1

P_comprar_cond_ser30 = float(compras[30]) / float(totales[30])
P_comprarAlgo = float(totalcompras) / 100000.0

print("P_comprar_cond_ser30: ", P_comprar_cond_ser30, " P_comprarAlgo: ", P_comprarAlgo) # P_comprar_cond_ser30:  0.3987604549010169  P_comprarAlgo:  0.4003

"""


"""