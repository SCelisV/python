valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}

# algunos metodos de diccionarios
print(valoraciones['Alien'])
print(valoraciones.keys())
print(valoraciones.values())
print(valoraciones.items())
# -O-J-O- Ejecución
# 9.5
# ['Alien', 'Terminator 2', 'Arma Letal']
# [9.5, 8.9, 7.3]
# [('Alien', 9.5), ('Terminator 2', 8.9), ('Arma Letal', 7.3)]


dic = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
print("dicionario -> dic{clave:valor} \n" + str(dic))
print("\n")
# algunos metodos de dicionarios
print("dic['Alien']: \n" + str(dic['Alien']))
print("dic.keys(): \n" + str(dic.keys()))
print("dic.values(): \n" + str(dic.values()))
print("dic.items(): \n" + str(dic.items()))
# -O-J-O- Ejecución
# dicionario -> dic{clave:valor}
# {'Alien': 9.5, 'Terminator 2': 8.9, 'Arma Letal': 7.3}


# dic['Alien']:
# 9.5
# dic.keys():
# ['Alien', 'Terminator 2', 'Arma Letal']
# dic.values():
# [9.5, 8.9, 7.3]
# dic.items():
# [('Alien', 9.5), ('Terminator 2', 8.9), ('Arma Letal', 7.3)]

# Dictionaries
# similar to arrays, but works with keys and values instead indexes

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. 
# However, a dictionary, unlike a list, does not keep the order of the values stored in it. 

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
# -O-J-O- Ejecución
# Phone number of John is 938477566
# Phone number of Jack is 938377264
# Phone number of Jill is 947662781

# Removing a value
# To remove a specified index, use either one of the following notations:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
# -O-J-O- Ejecución
# {'Jack': 938377264, 'Jill': 947662781}

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

phonebook.pop("Jill")
print(phonebook)

# -O-J-O- Ejecución
# {'Jack': 938377264}

###############
#  Excercise  #
###############

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"] = 938273443
print(phonebook)
phonebook.pop("Jill")
print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781, 'Jake': 938273443}
# {'John': 938477566, 'Jack': 938377264, 'Jake': 938273443}
# Jake is listed in the phonebook.
# Jill is not listed in the phonebook.

