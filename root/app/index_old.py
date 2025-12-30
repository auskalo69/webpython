#!/usr/bin/env python3
from os import environ
from sys import path
path.append("/home/auskalo/proyectos/webpython/root/app")

uri = environ.get("REQUEST_URI", "/")

componentes = uri.split('/')[1:]
rid = componentes[2] if len(componentes) == 3 else None
ruta_modulo = f'{componentes[0]}.controller'
nombre_controlador = f'{componentes[0].capitalize()}Controller'
modulo = __import__(ruta_modulo, fromlist=[nombre_controlador])
controlador = getattr(modulo, nombre_controlador)()
if not rid == None:
    getattr(controlador, componentes[1])(rid)
else:
    getattr(controlador, componentes[1])()
      
