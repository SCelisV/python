# modules_04.py => utilizar modulos de terceros 

#  añadir colores a la consola - https://pypi.org/search/?q=colorama


# (base) hadoop@ubuntu-hokkaido-3568:~/python$ python --version
# Python 3.7.4
# (base) hadoop@ubuntu-hokkaido-3568:~/python$ pip --version
# pip 19.2.3 from /home/hadoop/anaconda3/lib/python3.7/site-packages/pip (python 3.7)

# => instalar el paquete
# (base) hadoop@ubuntu-hokkaido-3568:~/python$ pip install colorama

# => importar modulo 
# import colorama

# => desde el modulo importar metodos
from colorama import Fore, Style

# => muestra el texto "Hello World" en Rojo
print(Fore.RED + "Hello World") 

print("--------------------")


# => para que funcione en windows: - incluir init
from colorama import Fore, Style, init
init(convert=True)
# => muestra el texto "Hello World" en Rojo
print(Fore.RED + "Hello World") 

print("--------------------")
