#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.variable.db.py

Vamos a definir una función que se conecta a una base de datos. 
Queremos conectarnos a una base de datos por defecto simplemente llamando a esta función sin parámetros. 
También queremos conectarnos a cualquier otra base de datos pasando a la función los argumentos apropiados.

default values son overridden de acuerdo a lo que se pase a la función.

"""
# arguments.variable.db.py

def connect(**options):
    conn_params = {                             # diccionario de parámetros de conexión utilizando por defecto
                                                # permitiendo que sean sobreescritos si se proporcionan en la llamada a la función
    'host': options.get('host', '127.0.0.1'),
    'port': options.get('port', 5432),
    'user': options.get('user', ''),
    'pwd': options.get('pwd', ''),
    }
    print(conn_params)


# nos conectamos a la db - 
# db.connect(**conn_params)     # quitar el comentario de esta línea para realizar la conexion

connect()                       #   Queremos conectarnos a una base de datos por defecto simplemente llamando a esta función sin parámetros.
                                #   {'host': '127.0.0.1', 'port': 5432, 'user': '', 'pwd': ''}

connect(host='127.0.0.42', port=5433) #  conectarnos a cualquier otra base de datos pasando a la función los argumentos adecuados.
                                #   {'host': '127.0.0.42', 'port': 5433, 'user': '', 'pwd': ''}

connect(port=5431, user='xxx', pwd='xxxxxx') #  conectarnos a cualquier otra base de datos pasando a la función los argumentos adecuados.
                                #   {'host': '127.0.0.1', 'port': 5431, 'user': 'xxx', 'pwd': 'xxxxxx'}