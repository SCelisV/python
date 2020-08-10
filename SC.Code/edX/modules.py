# modules.py

# modules propios
# modules others (internet)  => https://pypi.org/
# modules python => https://docs.python.org/3/py-modindex.html

import datetime # modules python : https://docs.python.org/3/library/datetime.html#module-datetime

# => parametro date, método today  classmethod date.today() => Return the current local date.
print(datetime.date.today())

# -O-J-O- Ejecución
# 2020-08-07
print("--------------------")

#  class datetime.timedelta => convertir minutos a horas
print(datetime.timedelta(seconds=70))

# -O-J-O- Ejecución
# 0:01:10

print("--------------------")

print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=3000, weeks=0))
print(datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=17.85715))

# -O-J-O- Ejecución

# 125 days, 0:00:00
# 125 days, 0:00:04.320000

print("--------------------")

# -O-J-O- Comments

# flask => modulo para web

# frameWork => Django 

# tkinter => interfaces gráficas de usuario