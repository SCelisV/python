#tuplas => datos que no cambian
#=> mutable =>
lista = [10, 20, 30, 55]

print("lista_ori: ", lista) 
lista.append(3)
print("lista_bef: ", lista) 

# => inmutable =>
tupla = (10, 20, 30, 55) 
print("tupla: ", tupla) 

# tupla.append(3) => genera un error 

# Traceback (most recent call last):
#   File "basic.py", line 12, in <module>
#     tupla.append(3)
# AttributeError: 'tuple' object has no attribute 'append'

print("tupla: ", tupla) 
myString = "Hello World"

print(myString)