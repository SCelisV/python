# Muestra por pantalla los numeros de esta lista que son mayores que 5.
numeros = [1, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7]
print(numeros)
tot=0
for i in numeros:
  if i > 5: 
    tot += 1
    print i
# Indica cuantos numeros de la lista son mayores que 5
print ("hay " + str(tot) + " numeros mayores que cinco")
# Muestra por pantalla una nueva lista que traduzca los elementos de la lista original:
# Los menores o iguales que 5 serán 0,
# Los mayores que 5 serán 1.
lst=[0 if x<=5 else 1 for x in numeros]
print lst


# listado de pruebas  ####
  
# el aerogenerador
# la mina
# el caracol
# fizzbuzz
# listas locas

###################
# Nóminas (listas)#
###################

# Las nóminas de nuestros empleados están en esta lista de números.
nominas = [1900, 2000, 1800, 2400, 1700, 1950, 2000, 1806, 2400, 1700]
print("nominas: " + str(nominas))
# Cuanto gasta la empresa en nominas mensualmente, Y de forma anual
gMes = (sum(nominas))
print("la empresa gasta en nominas al mes: %d" %gMes)
gAno = gMes * 12
print("el gasto anual del la empresa en nominas es: %d" %gAno)
# Cual es la nomina mas alta y la mas baja
print("la nomina mas baja es: " +str(min(nominas)))
print("la nomina mas alta es: " +str(max(nominas)))
# Cual es la media de las nominas en la empresa
print("la media de las nominas es: " + str(gMes/len(nominas)))
# Si las nominas estuvieran en dolares y las quisieramos en euros cual sera la nueva lista de nominas? 1 EUR = 1.09 DOL
eNominas=[int(i/1.09) for i in nominas]
print("nominas en euros: " + str(eNominas))
# Bonus: Pasa a dolares las nominas de mas de 2000 Euros solamente.
# eNominasgt2000=[e>2000 for e in eNominas]
dNominasgt2000e=[(int(e*1.09)) if e>2000 else 0 for e in eNominas]
print("nominas gt de 2000e a dolares: " + str(dNominasgt2000e))

###################
# Fechas (strings)#
###################

fecha = "10/03/2016"
print ("fecha: " + str(fecha))
# print(fecha) -->  10/03/2016
# Obten el dia, mes y ano de esta fecha

fecha = "10/03/2016"
print ("fecha: " + str(fecha))
# print(fecha) -->  10/03/2016
# Obten el dia, mes y ano de esta fecha

# split me crea una lista ['10', '03', '2016']
print(fecha.split("/"))

# dia: 10 - [0:2] [star:end]
dd = fecha[:2]
print("dia: " +str(dd))

# mes: 03 - [3:5] [star:end]
mes = fecha[3:5]
print("mes: " +str(mes))

# anio: 2016 - [6:10] [star:end]
anio = fecha[6:10]
print("anio: " +str(anio))

# Dada una fecha en formato dd/mm/yy calcula el numero de dias que tiene ese mes. Puedes ignorar si es bisiesto o no.

fecha = "10/03/2016"

diasanio = [31,28,31,30,31,30,31,31,30,31,30,31]
diasaniobis = [31,29,31,30,31,30,31,31,30,31,30,31]

# print("diasanio: " + str(diasanio));
# print("diasaniobis: " + str(diasaniobis));

# dia: 10 - [0:2] [star:end]
dd = fecha[:2]
print("dia: " +str(dd))

# mes: 03 - [3:5] [star:end]
mes = fecha[3:5]
print("mes: " +str(mes))

# anio: 2016 - [6:10] [star:end]
anio = fecha[6:10]
print("anio: " +str(anio))

print("El mes [ %s ] tiene: " %mes + str(diasanio[int(mes)-1]) + " dias")

# Calcula el numero de dias que tiene el mes de la fecha actual. Puedes ignorar si es bisiesto o no.

from datetime import date
today = date.today()
print("fecha actual =", today)
month = today.month
print("El mes [ %s ] tiene: " %month + str(diasanio[int(month)-1]) + " dias")

# Ahora pide la fecha al usuario mediante la funcion input() e imprime dia, mes y ano por consola.

errorFecha = 0
strFecha = raw_input('Digita una fecha en formato dd/mm/yyyy: \n')

if len(strFecha) <> 10:
      errorFecha = 1
else: 
    lstFecha=(strFecha.split("/"))
    print(len(lstFecha))
    if len(lstFecha) <> 3:
          errorFecha = 1
    else:
      # validadia(lstFecha[0])
      # validames(lstFecha[1])
      # validaanio(lstFecha[2])
      print("dia: " + str(lstFecha[0]) + " mes: " + str(lstFecha[1]) + " anio: " +str(lstFecha[2]))


if errorFecha == 1:
  print ('Fecha invalida: ' + strFecha)


# def convInt(lstFecha):
#   for i in lstFecha:
#   return int(lstFecha[i])

        # dd=int(lstFecha[1])
        # mm=int(lstFecha[2])
        # yy=int(lstFecha[3])
        # print("continue...")
        # tipo_dd = type(dd)
        # tipo_mm = type(mm)
        # tipo_yy = type(yy)

#Bonus: Reutiliza el codigo con una funcion que devuelva dia, mes y ano.
import datetime
fec = datetime.date(2007, 12, 5)
print fec.day
print fec.month
print fec.year
# Netflix (diccionarios)
# Como ejemplo:

item = {"name": "", "year": 0, "genre": ""}

# Ahora muchas:
padrino = {"name": "El padrino", "year": 1972, "genre": "Drama"}

lista = {"name": "La lista de Schindler", "year": 1993, "genre":"Drama"}

doce = {"name": "12 hombres sin piedad", "year": 1957, "genre": "Drama"}

vida = {"name": "La vida es bella", "year": 1997, "genre": "Comedy"}

bueno = {"name": "El bueno, el feo y el malo", "year": 1966, "genre": " Western"}

cadena = {"name": "Cadena perpetua", "year": 1994, "genre": "Drama"}

siete = {"name": "Los siete samurais", "year": 1954, "genre": "Adventure"}

netflix = [padrino, lista, doce, vida, bueno, cadena, siete]

print(padrino.items())
# print(padrino.keys())
# print(padrino.values())

# Dime el anio de estreno de "el padrino" y su genero.
print(padrino['name'], padrino['genre'])

# Cuantas peliculas hay en nuestra playlist de Netflix?
# print(netflix)
print(len(netflix))

# Cuantas peliculas de Drama hay en nuestra playlist de Netflix
totdrama=0
for peli in netflix:
    # print(peli['genre'])
    if(((peli['genre']))=="Drama"):
        totdrama +=1
print totdrama

# Cuantas peliculas de Drama anteriores a 1990 hay en nuestra playlist de Netflix?

totdrama=0
for peli in netflix:
    # print(peli['genre'] , peli['year'])
    if(((peli['genre']))=="Drama") and ((peli['year'])<1990):
      totdrama +=1
print totdrama

# Bonus: Cual es el titulo con el nombre mas largo?

lst=[len(peli['name']) for peli in netflix]
# print(len(lst))
print(max(lst))
