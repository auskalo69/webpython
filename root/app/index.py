#!/usr/bin/env python3
"""
from os import environ                                              # Importando el diccionario environ (contiene variables de entorno)
from sys import path                                                # Importando la lista path para agregar una nueva ruta de importación 
path.append("/home/auskalo/proyectos/webpython/root/app")           # Añandiendo una ruta de importación a la lista path

uri = environ.get("REQUEST_URI", "/")                               # Recuperando la clave 'REQUEST_URI' del diccionario environ
                                                                    # Si la clave no existe, devuelve el segundo parámetro de get
controladores = {                                                   # Definiendo un diccionario de contralador {'uri': 'NombreControlador'}
    'producto': 'Producto',
    'datodecontacto': 'DatoDeContacto'
}

componentes = uri.split('/')[1:]                                    # Dividiendo la uri utilizando la barra diagonal como divisor
rid = componentes[2] if len(componentes) == 3 else None             # Estableciendo el valor de la ID
ruta_modulo = f'{componentes[0]}.controller'                        # Definiendo la ruta del módulo

nombre_controlador = f'{controladores[componentes[0]]}Controller'   # Definiendo el nombre del controlador
modulo = __import__(ruta_modulo, fromlist=[nombre_controlador])     # Importando el controlador desde el módulo
controlador = getattr(modulo, nombre_controlador)()                 # Instanciando el controlador (creando un objeto 'controlador')

if not rid == None:                                                 # Dicidiendo si ejecutar el recurso pasando o no la ID
    getattr(controlador, componentes[1])(rid)                       # Ejecutando recurso con la ID
else:
    getattr(controlador, componentes[1])()                          # Ejecutando recurso sin la ID
"""

from MySQLdb import connect


def sql_execute(datos_acceso, sql, parametros=()):
    conexion = connect(**datos_acceso)
    cursor = conexion.cursor()
    cursor.execute(sql, parametros)

    if not sql.upper().find('SELECT') > -1:
        conexion.commit()
        data = cursor.lastrowid
    else:
        data = cursor.fetchall()

    cursor.close()
    conexion.close()

    return data


datos_acceso = dict(
    host='localhost',
    db='webpython',
    user='alikate',
    passwd='euskaraz'
)       

sql = "SHOW TABLES"
datos = sql_execute(datos_acceso, sql)

print("Content-Type: text/html")
print("")
print(datos)

