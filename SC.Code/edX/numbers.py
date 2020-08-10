print(f"14.4 es un float: {type(14.4)}")
print(f"9 es un entero: {type(9)}")


print(f"5/2 da como resultado: {5/2}")
print(f"5//2 nos devuelve la parte entera de la división: {5//2}")
print(f"5%2 nos devuelve el residuo de la división, llamado modulo: {5%2}")

print(f"5*3 multiplicación: {5*3}")
print(f"5**3 exponente: {5**3}")

# Precedencia => PEMDAS => Parenthesis, Exponentiation, Multiplication and Division, Addition and Subtraction

print(f"20 - 10 / 5 * 3**2 da como resultado: {20 - 10 / 5 * 3**2}" )
print(f"(20 - 10) / (5 * 3**2) utilizando la precedencia PEMDAS podemos modificarlo: {(20 - 10) / (5 * 3**2)}" )


age = input("Digita tu edad: ")
print(f"este dato es de tipo: {type(age)}")
years = 10
new_age = int(age) + years #casting - cast to entero
print(f"en {years} años tendrás {new_age}")