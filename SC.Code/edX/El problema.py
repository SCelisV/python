numeros = [1, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7]
print("numeros: " + str(numeros))
# Muestra por pantalla los números de esta lista que son mayores que 5.
print( "los números de la lista que son mayores que 5: ")
tot=0
for i in numeros:
  if i > 5: 
    tot += 1
    print (i)
# Indica cuántos números de la lista son mayores que 5. 
print ("hay " + str(tot) + " números de la lista mayores que 5")
# Muestra por pantalla una nueva lista que traduzca los elementos de la lista original:
# Los menores o iguales que 5 serán 0,
# Los mayores que 5 serán 1.
lst=[0 if x<=5 else 1 for x in numeros]
print ("replace: " + str(lst))
