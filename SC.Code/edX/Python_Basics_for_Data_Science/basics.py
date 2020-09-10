# -*- coding: utf-8 -*-

"""
IN-WORK-OUT
Created on Thu Sep 10 16:44:35 2020

@author: scelis - ¯\_(ツ)_/¯

cast, type, operadores, variables, Strings
https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks

https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks
basics.py

"""
type("1.1")
# Cast bool to int
int(True)
# Cast int to bool
bool(1)
# cast float to int => int(1.1):1, float 1.1 to integer will result in loss of information
int(1.1)
# cast String to int  => int('1'):1
int('1')
# cast int to String  => str(1):"1"
str(1)
# cast float to String => str(4.5):'4.5'
str(4.5)
# Convert integer 2 to a float and check its type
type(float(2))
# a string that is not a perfect match for a number
# invalid literal for int() with base 10: '1 or 2 people'
int('1 or 2 people')

# -O-J-O-
# System settings about float type
# sys.float_info

# 5.0
25/5

# 5
25//5

# 4 as the double slashes stand for integer division 
25//6

# 4.166666666666667
25/6

# jerarquía
# 87.0
43+60-10*8/5

# 87.0
43+60-(10*(8/5))

# 150
2*60+30

# 150
30+2*60

# 1920
(30+2)*60

# 10
my_va10riable = 10

# 60
x=60
x

# 1.0
y = x/60
y

# 1.0
x = x / 60
x

# int
type(x)

# float
type(y)

# 142
total_min = 43 + 42 + 57

# 2.3666666666666667
total_hr = total_min / 60

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours
type(total_hours)

# If you'd rather have total hours as an integer, 
total_hours = (43 + 42 + 57) // 60  # Total hours in a single expression
total_hours
type(total_hours)

# total_min = 160
# total_hr = total_min / 60
# 160/60
# 160//60

# Strings
"Michael Jackson"
Name = "Michael Jackson"
# Negative index can help us to count the element from the end of the string.
# The last element is given by the index -1: n
print(Name[-1])

# Print the first element in the string: M
print(Name[-15])

# Slice, Slicing, Rebanada, trozo
# When taking the slice, the first number means the index (start at 0), and the second number means the length from the index to the last element you want (start at 1)
# only index 0 to index 3: 'Mich'
Name[0:4]

# only index 8 to index 11: 'Jack'
Name[8:12]

# elementos pares
# Stride - Step (Start:Stop:Step) -  We can also  input a stride value as follows, with the '2' indicating that we are selecting every "step" variable:
# # Get every second element. The elments on index 1, 3, 5 .: 'McalJcsn'
Name[::2]

# Get every second element in the range from index 0 to index 4: Mca'
Name[0:5:2]

# print out the first three elements: Mic
print(Name[:3]) 
# or Mic
print(Name[0:3])    

# 16
len(Name)

# 'Michael Jackson is the best'
Statement = Name + "is the best"

# Tuples
# 'Michael Jackson Michael Jackson Michael Jackson '
3*"Michael Jackson "
3*Name

# -O-J-O-
# Strings inmutable - 'str' object does not support item assignment
Name[0] = "J"

Name = Name+ "is the best"

# Escape sequences

# \n - new line
# Michael Jackson 
# is the best
print(" Michael Jackson \n is the best")
 
 
# \t - tabulador
# Michael Jackson \ is the best
print(" Michael Jackson \t is the best")

# r - r will tell python that string will be display as raw string
# Michael Jackson \ is the best
print(" Michael Jackson \\ is the best")

print(r" Michael Jackson \ is the best")
# Print out a backslash \
print("\\")
# or
print(r" \ ")

# Methods
# Sequence, Strings

# upper
A="Thriller is the sixth studio album"
# 'THRILLER IS THE SIXTH STUDIO ALBUM'
B=A.upper()

Name = Name+ "is the best"

# replace
# 'Jane Jackson is the best'
C=Name.replace('Michael', 'Jane')

# finds a sub-string, return the index of the first elment of substring
Name = 'Michael Jackson is the best'
# start 0: 5, 
Name.find('el')
# start 0:  8, 
Name.find('Jack')
# If cannot find the substring in the string: -1 
Name.find('&*D')
