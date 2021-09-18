#################################################################
#Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
#################################################################

x = "Hello World!"
y = "H-e-l-l-o- -W-o-r-l-d"

# [star:end]
print(x, x[2:]) # -O-J-O- Ejecución: Hello World! llo World!

print(x, x[:2]) # -O-J-O- Ejecución: Hello World! He

print(x, x[:-2]) # -O-J-O- Ejecución: Hello World! Hello Worl

print(x, x[-2:]) # -O-J-O- Ejecución: Hello World! d!

print(x, x[2:-2]) # -O-J-O- Ejecución: Hello World! llo Worl

print(y, y[::2]) # -O-J-O- Ejecución: H-e-l-l-o- -W-o-r-l-d Hello World

print(y, len(y)) # -O-J-O- Ejecución: H-e-l-l-o- -W-o-r-l-d 21

# Basic String Operations
# Strings are bits of text. 
# They can be defined as anything between quotes:

astring = "Hello world!"
astring2 = 'Hello world!'

# As you can see, the first thing you learned was printing a simple sentence. 
# This sentence was stored by Python as a string. However, instead of immediately printing strings out, we will explore the various things you can do to them. 
# You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes.
# For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this

astring = "Hello world!"
print("single quotes are ' '") # -O-J-O- Ejecución: single quotes are ' '

print(len(astring)) # -O-J-O- Ejecución: 12 , because "Hello world!" is 12 characters long, including punctuation and spaces.

astring = "Hello world!" 
print(astring.index("o")) # -O-J-O- Ejecución:  4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.
# Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

astring = "Hello world!"
print(astring.count("l")) # -O-J-O- Ejecución: 3, This counts the number of l's in the string.

print(astring[11]) # -O-J-O- Ejecución: !, #Si sólo tiene un número entre paréntesis, extrae el carácter que ocupa esa posición. start things at 0 instead of 1

print(astring[:3]) # -O-J-O- Ejecución: Hel, # Si se omite el primer número pero se mantiene el colon, se extrae desde el principio hasta el número que dejó en. start things at 0 instead of 1

print(astring[2:]) # -O-J-O- Ejecución: llo world!, # Si omite el segundo número, se extrae desde el primer número hasta el final. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # -O-J-O- Ejecución:  lo w, starting at index 3, and ending at index 6. You can even put negative numbers inside the brackets. 
# start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # -O-J-O- Ejecución: lo w
print(astring[3:7:1]) # -O-J-O- Ejecución: lo w, the characters of string from 3 to 7 skipping one character. Extrae un caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # -O-J-O- Ejecución: lo w, 
print(astring[3:7:2]) # -O-J-O- Ejecución: l, the characters of string from 3 to 7 skipping three character. Extrae primer caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # -O-J-O- Ejecución: lo w, 
print(astring[3:7:3]) # -O-J-O- Ejecución: lw, the characters of string from 3 to 7 skipping three character. Extrae primero y último caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

# reverse a string like this
astring = "Hello world!"
print(astring[::-1]) # -O-J-O- Ejecución: !dlrow olleH

###############
#  Excercise  #
###############

# s = "Hey there! what should this string be?"

s = "Strings are awesome!"
  # "01234567890123456789"
  # "01234567a901a3456789"
  # "Strin567a901a3456789"
  # "Strings ar01a3456789"
  # "Strings ar01a34some!"
  # " t i g   r   w s m !" odd
  # "S r n s a e a e o e " even
  # "01234567890123456789"

# Length should be 20
print("Length of s = %d" % len(s)) # -O-J-O- Ejecución: Length of s = 20

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a")) # -O-J-O- Ejecución: The first occurrence of the letter a = 8

# Number of a's should be 2
print("a occurs %d times" % s.count("a")) # -O-J-O- Ejecución: a occurs 2 times

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5 # -O-J-O- Ejecución: The first five characters are 'Strin'

print("The next five characters are '%s'" % s[5:10]) # 5 to 10 # -O-J-O- Ejecución: The next five characters are 'gs ar'

print("The thirteenth character is '%s'" % s[12]) # Just number 12 # -O-J-O- Ejecución: The thirteenth character is 'a'

print("The characters with odd ('IMPAR') index are '%s'" %s[1::2]) # Start 1 hasta el final extrae cada 2 (0-based indexing) # -O-J-O- Ejecución: The characters with odd ('IMPAR') index are 'tig r wsm!'

print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end # -O-J-O- Ejecución: The last five characters are 'some!'

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper()) # -O-J-O- Ejecución: String in uppercase: STRINGS ARE AWESOME!
print("String in lowercase: %s" % s.lower()) # -O-J-O- Ejecución: String in lowercase: strings are awesome!

astring = "Hello world!"
print(astring.startswith("Hello")) # -O-J-O- Ejecución: True, the string starts with something
print(astring.endswith("asdfasdfasdf")) # -O-J-O- Ejecución: False, the string ends with something,

print("-----------------")

mystring = "Hello world!"
o = (mystring.index("o"))

print("la primera 'o' en la cadena %s esta en la posicion %d " % (mystring, o))
# -O-J-O- Ejecución: la primera 'o' en la cadena Hello world! esta en la posicion 4

char = "l"
mycount = mystring.count("l")

print("la cadena contiene %d %s " %(mycount, char ))
# -O-J-O- Ejecución: la cadena contiene 3 l


print("upper", mystring.upper()) # -O-J-O- Ejecución: upper HELLO WORLD!
print("lower", mystring.lower()) # -O-J-O- Ejecución: lower hello world!

print("split", mystring.split(" ")) # -O-J-O- Ejecución: split ['Hello', 'world!'], This splits the string into a bunch of strings grouped together in a list.

# String Formatting
# Python uses C-style string formatting to create new, formatted strings. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, 
# which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

name = "John"
print("Hello, %s!" % name) # -O-J-O- Ejecución: Hello, John!

# To use two or more argument specifiers, use a tuple (parentheses):

name = "John"
age = 23
print("%s is %d years old." % (name, age)) # -O-J-O- Ejecución: John is 23 years old.

# Any object which is not a string can be formatted using the %s operator as well. 
# The string which returns from the "repr" method of that object is formatted as the string. 
# For example:

mylist = [1,2,3]
print("A list: %s" % mylist) # -O-J-O- Ejecución: A list: [1, 2, 3]

###############
#  Excercise  #
###############

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. 
# Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data) # -O-J-O- Ejecución: Hello John Doe. Your current balance is $53.44.

mensaje = "this is an string: Hello World"
print(mensaje) # -O-J-O- Ejecución: this is an string: Hello World

a = 40
print(a) # -O-J-O- Ejecución: 40
print("this is a: " + str(a)) # -O-J-O- Ejecución: this is a: 40

b = 2
print(b) # -O-J-O- Ejecución: 2
print("this is b: " + str(b)) # -O-J-O- Ejecución: this is b: 2

c = a + b
print(c) # -O-J-O- Ejecución: 42
print("this is a Result c = a + b: " + str(c)) # -O-J-O- Ejecución: this is a Result c = a + b: 42

myStr = "Hello World, Hola Mundo esto es una cadena"
# dir(myStr) # Que podemos hacer con cierto tipo de dato
print("dir(tipo de dato) # Que podemos hacer con cierto tipo de dato - métodos")
# print(dir(myStr))

# -O-J-O- Ejecución
# dir(tipo de dato) # Que podemos hacer con cierto tipo de dato - métodos
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print("01. ", myStr.upper()) # Mayúscula
print("02. ", myStr.lower()) # Minúscula
print("03. ", myStr.swapcase()) # Mayúscula a Minúscula y viceversa
print("04. ", myStr.capitalize()) # rimera letra en Mayúscula
print("05. ", myStr.replace('Hello', 'bye').upper()) # métodos encadenados
print("06. ", myStr.count('l')) # cuenta los caracteres encontrados en la cadena
print("07. ", myStr.count('o'))
print("08. ", myStr.count(' '))
print("09. ", myStr.startswith('hola ')) # El texto empieza por..(busca por caracteres)
print("10. ", myStr.endswith('ld')) # El texto termina por..(busca por caracteres)
print("11. ", myStr.__add__(' hola munDo').upper()) # adiciona texto a la cadena
print("12. ", myStr.split()) # separa el texto en una lista a partir de espacio en blanco por default-defecto
print("13. ", myStr.split(',')) # separa el texto en una lista a partir de un caracter específico
print("14. ", myStr.split('o')) # separa el texto en una lista a partir de un caracter específico
print("15. ", myStr.find('o')) # buscar un caracter dentro de un texto, devuelve la posición donde encuentra el caracter 'o'
list=myStr.split('o')
print ("16. ", list) # devuelve la lista split('o')
list=myStr.split('o').__len__()
print ("17. ", list) # devuelve la longitud de la lista empieza en 1
print("18. ", len(myStr)) # longitud de un String, empieza en 0
print("19. ", myStr.index('e')) # devuelve la posición donde encuentra el caracter 'e'
print("20. ", myStr.isnumeric()) # para saber si es númerico
print("21. ", myStr.isalpha()) # para saber si es alfanumerico
print("22. ", myStr[0]) # imprimir el caracter de la posición
print("23. ", myStr[-0]) # imprime lo mismo de la posición [0]
print("24. ", myStr[1]) # imprimir el caracter de la posición 
print("25. ", myStr[-1]) # imprimir el caracter de la posición empezando inverso desde la derecha empieza en -1
print("26. ", myStr[4]) # imprimir el caracter de la posición
print("27. ", myStr[-4]) # imprimir el caracter de la posición empezando inverso desde la derecha
print("28. ", "My String is: " + myStr) # unión de strings - concatenar
print(f"29.  My String is: {myStr}") # otra forma de concatenar - v3.6 -->
print("30. ", "My String is: {0}".format(myStr)) # unión de strings - concatenar - v3.6 -->

# -O-J-O- Ejecución
# 01.  HELLO WORLD, HOLA MUNDO ESTO ES UNA CADENA
# 02.  hello world, hola mundo esto es una cadena
# 03.  hELLO wORLD, hOLA mUNDO ESTO ES UNA CADENA
# 04.  Hello world, hola mundo esto es una cadena
# 05.  BYE WORLD, HOLA MUNDO ESTO ES UNA CADENA
# 06.  4
# 07.  5
# 08.  7
# 09.  False
# 10.  False
# 11.  HELLO WORLD, HOLA MUNDO ESTO ES UNA CADENA HOLA MUNDO
# 12.  ['Hello', 'World,', 'Hola', 'Mundo', 'esto', 'es', 'una', 'cadena']
# 13.  ['Hello World', ' Hola Mundo esto es una cadena']
# 14.  ['Hell', ' W', 'rld, H', 'la Mund', ' est', ' es una cadena']
# 15.  4
# 16.  ['Hell', ' W', 'rld, H', 'la Mund', ' est', ' es una cadena']
# 17.  6
# 18.  42
# 19.  1
# 20.  False
# 21.  False
# 22.  H
# 23.  H
# 24.  e
# 25.  a
# 26.  o
# 27.  d
# 28.  My String is: Hello World, Hola Mundo esto es una cadena
# 29.  My String is: Hello World, Hola Mundo esto es una cadena
# 30.  My String is: Hello World, Hola Mundo esto es una cadena



myInteger = 10


myInteger.__eq__(10)
# -O-J-O- Ejecución
# True

# dir(myInteger)
# print(dir(myInteger))
# -O-J-O- Ejecución
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

None
# dir(None)
# print(dir(None))
# -O-J-O- Ejecución
# ['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



