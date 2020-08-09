#################################################################
#Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
#################################################################

x = "Hello World!"
y ="H-e-l-l-o- -W-o-r-l-d"

# [star:end]
print(x, x[2:]) # O-J-O- Ejecucion: Hello World! llo World!

print(x, x[:2]) # O-J-O- Ejecucion: Hello World! He

print(x, x[:-2]) # O-J-O- Ejecucion: Hello World! Hello Worl

print(x, x[-2:]) # O-J-O- Ejecucion: Hello World! d!

print(x, x[2:-2]) # O-J-O- Ejecucion: Hello World! llo Worl

print(y, y[::2]) # O-J-O- Ejecucion: H-e-l-l-o- -W-o-r-l-d Hello World

print(y, len(y)) # O-J-O- Ejecucion: H-e-l-l-o- -W-o-r-l-d 21

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
print("single quotes are ' '") # O-J-O- Ejecucion: single quotes are ' '

print(len(astring)) # O-J-O- Ejecucion: 12 , because "Hello world!" is 12 characters long, including punctuation and spaces.

astring = "Hello world!" 
print(astring.index("o")) # O-J-O- Ejecucion:  4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.
# Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

astring = "Hello world!"
print(astring.count("l")) # O-J-O- Ejecucion: 3, This counts the number of l's in the string.

print(astring[11]) # O-J-O- Ejecucion: !, #Si sólo tiene un número entre paréntesis, extrae el carácter que ocupa esa posición. start things at 0 instead of 1

print(astring[:3]) # O-J-O- Ejecucion: Hel, # Si se omite el primer número pero se mantiene el colon, se extrae desde el principio hasta el número que dejó en. start things at 0 instead of 1

print(astring[2:]) # O-J-O- Ejecucion: llo world!, # Si omite el segundo número, se extrae desde el primer número hasta el final. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # O-J-O- Ejecucion:  lo w, starting at index 3, and ending at index 6. You can even put negative numbers inside the brackets. 
# start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # O-J-O- Ejecucion: lo w
print(astring[3:7:1]) # O-J-O- Ejecucion: lo w, the characters of string from 3 to 7 skipping one character. Extrae un caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # O-J-O- Ejecucion: lo w, 
print(astring[3:7:2]) # O-J-O- Ejecucion: l, the characters of string from 3 to 7 skipping three character. Extrae primer caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

astring = "Hello world!"
print(astring[3:7]) # O-J-O- Ejecucion: lo w, 
print(astring[3:7:3]) # O-J-O- Ejecucion: lw, the characters of string from 3 to 7 skipping three character. Extrae primero y último caracter starting at index 3 and ending at index 6. The general form is [start:stop:step]. start things at 0 instead of 1

# reverse a string like this
astring = "Hello world!"
print(astring[::-1]) # O-J-O- Ejecucion: !dlrow olleH

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
print("Length of s = %d" % len(s)) # O-J-O- Ejecucion: Length of s = 20

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a")) # O-J-O- Ejecucion: The first occurrence of the letter a = 8

# Number of a's should be 2
print("a occurs %d times" % s.count("a")) # O-J-O- Ejecucion: a occurs 2 times

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5 # O-J-O- Ejecucion: The first five characters are 'Strin'

print("The next five characters are '%s'" % s[5:10]) # 5 to 10 # O-J-O- Ejecucion: The next five characters are 'gs ar'

print("The thirteenth character is '%s'" % s[12]) # Just number 12 # O-J-O- Ejecucion: The thirteenth character is 'a'

print("The characters with odd ('IMPAR') index are '%s'" %s[1::2]) # Start 1 hasta el final extrae cada 2 (0-based indexing) # O-J-O- Ejecucion: The characters with odd ('IMPAR') index are 'tig r wsm!'

print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end # O-J-O- Ejecucion: The last five characters are 'some!'

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper()) # O-J-O- Ejecucion: String in uppercase: STRINGS ARE AWESOME!
print("String in lowercase: %s" % s.lower()) # O-J-O- Ejecucion: String in lowercase: strings are awesome!

astring = "Hello world!"
print(astring.startswith("Hello")) # O-J-O- Ejecucion: True, the string starts with something
print(astring.endswith("asdfasdfasdf")) # O-J-O- Ejecucion: False, the string ends with something,

print("-----------------")

mystring = "Hello world!"
o = (mystring.index("o"))

print("la primera 'o' en la cadena %s esta en la posicion %d " % (mystring, o))
# O-J-O- Ejecucion: la primera 'o' en la cadena Hello world! esta en la posicion 4

char = "l"
mycount = mystring.count("l")

print("la cadena contiene %d %s " %(mycount, char ))
# O-J-O- Ejecucion: la cadena contiene 3 l


print("upper", mystring.upper()) # O-J-O- Ejecucion: upper HELLO WORLD!
print("lower", mystring.lower()) # O-J-O- Ejecucion: lower hello world!

print("split", mystring.split(" ")) # O-J-O- Ejecucion: split ['Hello', 'world!'], This splits the string into a bunch of strings grouped together in a list.

# String Formatting
# Python uses C-style string formatting to create new, formatted strings. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, 
# which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

name = "John"
print("Hello, %s!" % name) # O-J-O- Ejecucion: Hello, John!

# To use two or more argument specifiers, use a tuple (parentheses):

name = "John"
age = 23
print("%s is %d years old." % (name, age)) # O-J-O- Ejecucion: John is 23 years old.

# Any object which is not a string can be formatted using the %s operator as well. 
# The string which returns from the "repr" method of that object is formatted as the string. 
# For example:

mylist = [1,2,3]
print("A list: %s" % mylist) # O-J-O- Ejecucion: A list: [1, 2, 3]

###############
#  Excercise  #
###############

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. 
# Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data) # O-J-O- Ejecucion: Hello John Doe. Your current balance is $53.44.

mensaje = "this is an string: Hello World"
print(mensaje) # O-J-O- Ejecucion: this is an string: Hello World

a = 40
print(a) # O-J-O- Ejecucion: 40
print("this is a: " + str(a)) # O-J-O- Ejecucion: this is a: 40

b = 2
print(b) # O-J-O- Ejecucion: 2
print("this is b: " + str(b)) # O-J-O- Ejecucion: this is b: 2

c = a + b
print(c) # O-J-O- Ejecucion: 42
print("this is a Result c = a + b: " + str(c)) # O-J-O- Ejecucion: this is a Result c = a + b: 42

