# main program: /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/DPhi/main.py
# para ejecutar el programa (Ctrl + F5)

"""
# dejando los ficheros al mismo nivel 
# Estructura de ficheros

drwxrwxr-x 4 .
drwxrwxr-x 2 __pycache__
-rw-rw-r-- 1 main.py
-rw-rw-r-- 1 functions.py
"""
# una forma
"""
import functions

area = functions.calculate_square_area(5)

print("area: ", area)                            # area:  25 
"""
# otra forma
"""
import functions as f

area = f.calculate_square_area(5)

print("area: ", area)                            # area:  25 
"""

"""
# move functions.py modules/functions.py
# Estructura de ficheros

drwxrwxr-x 4 .
drwxrwxr-x 2 __pycache__
drwxrwxr-x 2 modules
-rw-rw-r-- 1 main.py

ls modules
-rw-rw-r-- functions.py
"""

"""
import modules.functions as f

area = f.calculate_square_area(5)

print("area: ", area)                            # area:  25 

"""

"""
# move functions.py SC.Code/functions.py
# Estructura de ficheros

drwxrwxr-x 4 .
drwxrwxr-x 2 __pycache__
-rw-rw-r-- main.py

ls /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code
-rw-rw-r-- functions.py

"""
import sys
sys.path.append("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/")

import functions as f
area = f.calculate_square_area(5)
print("area: ", area)                            # area:  25 

area = f.calculate_traingle_area(5, 10)
print("area: ", area)                            # area:  25.0

"""

"""