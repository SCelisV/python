# Lists are very similar to arrays. 
# They can contain any type of variable, and they can contain as many variables as you wish. 
# Lists can also be iterated over in a very simple manner. 
# Here is an example of how to build a list.

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #  -O-J-O- Ejecución 1
print(mylist[1]) #  -O-J-O- Ejecución 2
print(mylist[2]) #  -O-J-O- Ejecución 3

#  -O-J-O- Ejecución out 1,2,3
for x in mylist:
    print(x)

print("--------------------")
print("one list")
mylist = []
mylist.append("a")
mylist.append("b")
mylist.append("c")
print(mylist[0]) #  -O-J-O- Ejecución a
print(mylist[1]) #  -O-J-O- Ejecución b
print(mylist[2]) #  -O-J-O- Ejecución c
#  -O-J-O- Ejecución out a,b,c
x = 0
for x in mylist:
    print(x)

print("--------------------")
print("other list")
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #  -O-J-O- Ejecución 1
print(mylist[1]) #  -O-J-O- Ejecución 2
print(mylist[2]) #  -O-J-O- Ejecución 3

#  -O-J-O- Ejecución out 1,2,3
for x in mylist:
    print("x: ", x)
    
print("--------------------")

# - O-J-O- Genera el siguiente error: - 
# 
# mylist = [1,2,3]
# print(mylist[10])

# Accessing an index which does not exist generates an exception (an error).

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     print(mylist[10])
# IndexError: list index out of range

# - O-J-O- Genera el siguiente error: - 

print("--------------------")
print ("second list")
numbers = [1, 2, 3, 4, 5]
strings = ["a", "b", "c", "d", "e"]
names = ["John", "Eric", "Jessica"]
second_name = names[1]

print(numbers)
print(strings)
print (names)
print("The second name on the names list is %s" % second_name)


#  -O-J-O- Ejecución out:
# [1, 2, 3, 4, 5]
# ['a', 'b', 'c', 'd', 'e']
# ['John', 'Eric', 'Jessica']
# The second name on the names list is Eric

print("--------------------")
print ("three list")
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#  -O-J-O- Ejecución out
# three list
# [1, 3, 5, 7, 2, 4, 6, 8]

print("--------------------")
print ("four list")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

#  -O-J-O- Ejecución out
# x_list contains 10 objects
# y_list contains 10 objects
# big_list contains 20 objects

# testing
print("testing some code: ")

if x_list.count(x) == 10 and y_list.count(y) == 10:
  print ("y..")
    
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


###############
#  Excercise  #
###############

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 
# You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. 

# Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print("--------------------")

# listas creadas a partir de un rango: range.py => ver este fichero de ejemplos

# range (n...., n-1)
lista_00 = list(range (1,10))
print(f"este ćodigo: list(range (1,10)) crea una lista a partir usando la función range(rango): {lista_00}, comprobamos su tipo: {type(lista_00)}")

lista_00 = list(range (1,11))
print(f"este ćodigo: list(range (1,11)) crea una lista a partir usando la función range(rango): {lista_00}, comprobamos su tipo: {type(lista_00)}")

# métodos de una lista
# print(dir(lista_00))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(f"con este código: len(lista_00), podemos saber cuantos elementos hay en el elemento lista_00: {len(lista_00)}")
print(f"con este código: len(lista_00), podemos saber cuantos elementos hay en el elemento lista_00: {len(lista_00)}")

print("--------------------")





print("--------------------")
