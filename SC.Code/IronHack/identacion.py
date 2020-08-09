################################################################
#Este código da error de indentación. 
#print(x) debería estár más a la derecha
################################################################
for x in range(10): 
print(x)

# OJO - Ejecucion
# File "main.py", line 1SyntaxError: Non-ASCII character '\xc3' in file main.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

# Este codigo tiene doble indentacion
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes: 
	# en este nivel estamos dentro del primer for
	print(">>> estamos dentro del primer for hablando de", estudiante)
	for peli, valoracion in valoraciones.items(): 
		# en este nivel estamos dentro del segundo for
		print(">>> estamos dentro del segundo for hablando de", peli, "y de", estudiante)
		print(estudiante, "vio", peli, "y le puso una nota de", valoracion)


# O-J-O - Ejecucion
# ('>>> estamos dentro del primer for hablando de', 'Harry')
# ('>>> estamos dentro del segundo for hablando de', 'Alien', 'y de', 'Harry')('Harry', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('>>> estamos dentro del segundo for hablando de', 'Terminator 2', 'y de', 'Harry')
# ('Harry', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('>>> estamos dentro del segundo for hablando de', 'Arma Letal', 'y de', 'Harry')('Harry', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)('>>> estamos dentro del primer for hablando de', 'Hermione')('>>> estamos dentro del segundo for hablando de', 'Alien', 'y de', 'Hermione')
# ('Hermione', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('>>> estamos dentro del segundo for hablando de', 'Terminator 2', 'y de', 'Hermione')
# ('Hermione', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('>>> estamos dentro del segundo for hablando de', 'Arma Letal', 'y de', 'Hermione')
# ('Hermione', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)
# ('>>> estamos dentro del primer for hablando de', 'Ron')('>>> estamos dentro del segundo for hablando de', 'Alien', 'y de', 'Ron')('Ron', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('>>> estamos dentro del segundo for hablando de', 'Terminator 2', 'y de', 'Ron')('Ron', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('>>> estamos dentro del segundo for hablando de', 'Arma Letal', 'y de', 'Ron')
# ('Ron', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)

# Python uses indentation to define code blocks, instead of brackets. 
# The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. 
# Notice that code blocks do not need any termination.

# A statement is evaulated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.
# Here are some examples for objects which are considered as empty: 
# 1. An empty string: "" 
# 2. An empty list: []
# 3. The number zero: 0 
# 4. The false boolean variable: False

if statement is True:
    # do something
    print("if statement is True: ")
elif another_statement is True: # else if
    # do something else
    print("elif another_statement is True: ")
else:
    # do another thing
    print("else: statement is False , another_statement is False")

x = 2
if x == 2:
    print("x equals two!") # O-J-O- Ejecucion: x equals two!
else:
    print("x does not equal to two.")