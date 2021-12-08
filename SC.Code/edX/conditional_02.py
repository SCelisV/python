#entrada = raw_input("Introduce un numero entero: ")

entrada = input("Introduce un numero entero: ")
# convertimos la cadena de caracteres en entero. Esta operacion se llama cast. 
numero = int(entrada)

# Ahora veamos que has puesto
if numero == 42: 
	print("Has elegido 42")
elif numero < 42: 
	print("El numero", numero, "es menor que 42")
else: 
	print("El numero", numero, "es mayor que 42")
#   OJO - Ejecucion
#   Introduce un numero entero: 45
# ('El numero', 45, 'es mayor que 42')

#numberOne = raw_input("Introduce un numero entero: ")
#numberTwo = raw_input("Introduce un numero entero: ")
numberOne = input("Introduce un numero entero: ")
numberTwo = input("Introduce un numero entero: ")
a = int(numberOne)
b = int(numberTwo)

if a == b: 
	print("%d" %a, "es igual %d" %b)
elif a < b: 
	  print("el numero %d" %a, "es menor que %d" %b)
else:
	  print("el numero %d" %a, "es mayor que %d" %b)
# OJO - Ejecucion
# Introduce un numero entero: 5
# Introduce un numero entero: 5
# ('5', 'es igual 5')
# Introduce un numero entero: 2
# Introduce un numero entero: 9
# ('el numero 2', 'es menor que 9')
# Introduce un numero entero: 9
# Introduce un numero entero: 2
# ('el numero 9', 'es mayor que 2')


# A statement is evaulated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.
# Here are some examples for objects which are considered as empty: 
# 1. An empty string: "" 
# 2. An empty list: []
# 3. The number zero: 0 
# 4. The false boolean variable: False

statement = False
another_statement = True

# O-J-O- Ejecucion:
# elif another_statement is True: 

statement = True
another_statement = False

# O-J-O- Ejecucion:
# if statement is True:

statement = False
another_statement = False

# O-J-O- Ejecucion:
# else: statement is False , another_statement is False

statement = True
another_statement = True

# O-J-O- Ejecucion:
# else: if statement is True:

if statement is True:
    # do something
    print("if statement is True: ")
elif another_statement is True: # else if
    # do something else
    print("elif another_statement is True: ")
else:
    # do another thing
    print("else: statement is False , another_statement is False")
    
print('All done')
print('==========')

x = 2
if x == 2:
    print("x equals two!") # O-J-O- Ejecucion: x equals two!
else:
    print("x does not equal to two.")
    
print('All done')
print('==========')
    
x = 9
if (x < 2):
    print('es menor que 2')
elif (x < 10):
    print('es menor que 10')
else:
    print ('No es menor que 2 ni menor que 10, es: ',x)
    
print('All done')
print('==========')

x = 0
if x < 2:
    print ('small')
elif x < 10:
    print ('Medium')
else:
    print('LARGE')
    
print('All done')
print('==========')   
  
# No Else      
x = 50
if x < 2:
    print ('small')
elif x < 10:
    print ('Medium')
    
print('All done')
print('==========')   

        
x = 0
if x < 2:
    print ('Small')
elif x < 10:
    print ('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print ('Large')
elif x < 100:
    print ('Huge')
else:
    print('Ginormous')

print('All done')
print('==========')   

x = 2
if x < 2:
    print ('Below 2')
elif x >= 2:
    print ('Two or more')
else:
    print ('Something else') # nunca se imprime 
    
print('All done')
print('==========')   

x = 6
if x < 2:
    print ('Below 2')
elif x < 20:
    print ('Below 20')
elif x < 10: # nunca se ejecuta 
    print ('Below 10')
else:
    print ('Something else')
    
print('All done')
print('==========')   


# Measure some strings:
words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

"""
cat 3
window 6
defenestrate 12
"""

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for i in users:
    print("user: ", i)

"""
user:  Hans
user:  Éléonore
user:  景太郎
"""

for i, j in users.items():
    print("user: ", i, "- status: ", j)

"""
user:  Hans - status:  active
user:  Éléonore - status:  inactive
user:  景太郎 - status:  active
"""

print("<-------------------->")

print("Strategy:  Iterate over a copy - del user status inactive")

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

for i, j in users.copy().items():
    print("user: ", i, "- status: ", j)

""" 
user:  Hans - status:  active
user:  景太郎 - status:  active
"""

print("<-------------------->")

print(" Strategy:  Create a new collection" )

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for i, j in active_users.items():
    print("user: ", i, "- status: ", j)

"""
user:  Hans - status:  active
user:  景太郎 - status:  active
"""

print("<-------------------->")

x = int(input("Please enter an integer: "))

if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')

print("<-------------------->")
