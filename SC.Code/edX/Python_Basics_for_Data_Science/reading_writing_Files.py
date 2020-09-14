#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Mon Sep 14 14:03:35 2020

@author: scelis - ¯\_(ツ)_/¯

!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

Reading Files and Writing Files

reading_writing_Files.py
"""

file = open("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Python_Basics_for_Data_Science/example1.txt","r")
# =============================================================================
# 
# modes of open files
# 
#     r Read mode for reading files (default)
#     w Write mode for writing files
#     a Append mode for appending files
#       
#   Use file object to obtain information about the file
#   Use the data attribute name to get the name of the file.
#   Use the data attribute mode to get the mode object is in using.
# 
#   Allways close file object - close method
# 
#   The best practice is using with statement becouse automatically closes the file even if the code encounters an exception
# 
# =============================================================================


file.name
# '/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Python_Basics_for_Data_Science/example1.txt'

file.mode # 'r'

# Read the file
FileContent = file.read()
FileContent

# Print the file
print(FileContent)

# Type of file content
type(FileContent) # str

file.close() #  close file object 


#   The best practice is using with statement becouse automatically closes the file even if the code encounters an exception

example1="/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Python_Basics_for_Data_Science/example1.txt"

with open(example1, "r") as file:
    FileContent = file.read()
    print(FileContent)

# Verify if the file is closed
print(file.closed) # True

# See the content of file
print(FileContent)

FileContent 
# 'This is line 1\nThis is line 2\nThis is line 3\n'
    

# We don’t have to read the entire(todo) file, Read first four characters, cierta cantidad de datos
with open(example1, "r") as file:
    print(file.read(4)) # This
    
# Read certain amount of characters
with open(example1, "r") as file:
    print(file.read(4)) # This
    print(file.read(4)) #  is 
    print(file.read(7)) # line 1
    print(file.read(15)) # This is line 2
    

# read one line of the file at a time using the method readline(): 
with open(example1, "r") as file:
    print('first line: ' + file.readline())
    
    
# We can use a loop to iterate through each line:
# Iterate through the lines
with open(example1,"r") as file:
        i = 0;
        for line in file:
            print("Iteration", str(i), ": ", line)
            i = i + 1;     
            
# Iteration 0 :  This is line 1

# Iteration 1 :  This is line 2

# Iteration 2 :  This is line 3

# We can use the method readlines() to save the text file to a list: 
# Read all lines and save as a list

with open(example1, "r") as file:
    FileasList = file.readlines()

FileasList
# ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']

FileasList[0] # 'This is line 1\n'

long = len(FileasList) # 3   

for i in range(long):
    print(FileasList[i])
    
# This is line 1

# This is line 2

# This is line 3

with open(example1, "r") as file:
    for line in file:
        print(line)
        
# This is line 1

# This is line 2

# This is line 3        

# Esto es una prueba con un argumento en el readlines en teoria puede leer los caracteres de una línea pero no me ha funcionado.. (review)
with open(example1, "r") as file:
    chars = file.readlines(10)

chars # ['This is line 1\n']

"""
Writing Files
save the text file to a list
"""
example2="/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Python_Basics_for_Data_Science/example2.txt"

# Write line to file
with open(example2, 'w') as wfile:
    file.write("This is line A \n")
    file.write("This is line B")
    
# Read file to see if it worked
with open(example2, 'r') as testwfile:
    print(testwfile.read())

# This is line A 
# This is line B

lines = ["This is line A \n","This is line B \n","This is line C \n"]
with open(example2, 'w') as file:
    for line in lines:
        file.write(line)
        
"""
Appending Files - add
save the text file to a list
"""
example3="/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/Python_Basics_for_Data_Science/example3.txt"
    
with open(example3, 'a') as file:
    for line in lines:
        file.write(line)
     
# Copy one file to a new file         
with open(example2, "r") as rfile:
    
    with open(example3, "w") as wfile:
        
        for line in rfile:
            wfile.write(line)


# Read file to see if it worked
with open(example3, 'r') as testwfile:
    print(testwfile.read())
    
with open(example3, 'a') as testwfile:
    testwfile.write("This is line D\n")