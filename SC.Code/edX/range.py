# class range(stop)
# class range(start, stop[, step])

# The arguments (start, stop[, step] MUST BE integers 
# (either built-in int or any object that implements the __index__ special method). 
# If start ommited, it defaults to 0. 
# If step omitted, it defaults to 1. 
# If step is zero, ValueError.

# For a positive step, the contents of a range r are determined:
# r[i] = start + step*i where i >= 0 and r[i] < stop

# For a negative step, the contents of the range are still determined:
# r[i] = start + step*i where i >= 0 and r[i] > stop.

"""
En muchos sentidos el objeto devuelto por range() se comporta como si fuera una lista, pero en realidad no lo es. 
Es un objeto que devuelve los elementos sucesivos de la secuencia deseada cuando se itera sobre él
"""

lst00=[i for i in range(10)]
print(str(lst00)) # -O-J-O Ejecución: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst00=[i for i in range(1, 11)]
print(str(lst00)) # -O-J-O Ejecución: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst00=[i for i in range(0, 30, 5)]
print(str(lst00)) # -O-J-O Ejecución: [0, 5, 10, 15, 20, 25]

lst00=[i for i in range(0, 10, 3)]
print(str(lst00)) # -O-J-O Ejecución: [0, 3, 6, 9]

lst00=[i for i in range(0, -10, -1)]
print(str(lst00)) # -O-J-O Ejecución: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

lst00=[i for i in range(0)]
print(str(lst00)) # -O-J-O Ejecución: []

lst00=[i for i in range(1, 0)]
print(str(lst00)) # -O-J-O Ejecución: []

lst00=[i for i in range(0, -10, -1)]
print(str(lst00)) # -O-J-O Ejecución: [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

lst00=[i for i in range(-10, -1)]
print(str(lst00)) # -O-J-O Ejecución: [-10, -9, -8, -7, -6, -5, -4, -3, -2]

# lst00=[i for i in range(0, 10, 0)]
# print(str(lst00)) # -O-J-O Ejecución: ValueError: range() arg 3 must not be zero

# Ranges containing absolute values larger than sys.maxsize are permitted but some features (such as len()) may raise OverflowError.
# sys.maxsize: An integer giving the maximum value a variable of type Py_ssize_t can take. 
# It’s usually 
# 2**31 - 1 on a 32-bit platform = 2.147.483.648
# 2**63 - 1 on a 64-bit platform = 9.223.372.036.854.775.808
# but some features (such as len()) may raise OverflowError.

r = [i for i in range(0, 20, 2)]
print(r)
print(11 in r) # -O-J-O Ejecución: False
print(10 in r) # -O-J-O Ejecución: True
print(r.index(10)) # -O-J-O Ejecución: 5 (print position where the value is 10)
print(r.index(4)) # -O-J-O Ejecución: 2
print(r[5]) # -O-J-O Ejecución: 10 (print value where position is 5)
print(r[:5]) # -O-J-O Ejecución: [0, 2, 4, 6, 8]
print(r[-1]) # -O-J-O Ejecución: 18

# == when range are the same sequence of VALUES

if (range(0) == range(2, 1, 3)):
  print ("iguales") # -O-J-O Ejecución: iguales
else:
  print("diferentes")

if (range(0, 3, 2) == range(0, 4, 2)):
  print ("iguales") # -O-J-O Ejecución: iguales
else:
  print("diferentes")

print("--------------------")

for number in range(1,8):
  print(number)

# -O-J-O- Ejecución

# 1
# 2
# 3
# 4
# 5
# 6
# 7

print("--------------------")

for letter in "Hello":
  print(letter)

# -O-J-O- Ejecución

# H
# e
# l
# l
# o

print("--------------------")

count = 4


while count <= 10:
  print(count)
  count += 1


# -O-J-O- Ejecución

# 4
# 5
# 6
# 7
# 8
# 9
# 10

print("<-------------------->")

for i in range(5):
    print(i)

"""
0
1
2
3
4
"""

print("<-------------------->")

print(list(range(5, 10)))
"""
[5, 6, 7, 8, 9]
"""

print(list(range(0, 10, 3)))
"""
[0, 3, 6, 9]
"""

print(list(range(-10, -100, -30)))
"""
[-10, -40, -70]
"""

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

"""
0 Mary
1 had
2 a
3 little
4 lamb
"""

print(sum(range(4)))                                    # 0 + 1 + 2 + 3 = 6


