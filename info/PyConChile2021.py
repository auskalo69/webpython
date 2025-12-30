# Leer las metavariables CGI
from os import environ
variable = environ.get(’NOMBRE DE LA METAVARIABLE’, ‘valor por defecto’)

# Reconocer el método HTTP de una solicitud
from os import environ
metodo_http = environ.get(‘REQUEST_METHOD’, ‘GET’)


# Reconocer el URI
recurso = environ.get(‘REQUEST_URI’, ‘/’)

# Algunos ejemplos de cómo emplear el reconocimiento de URIs
# 1) Definir los recursos habilitados en una lista.
#    Si el recurso solicitado está en la lista, se toma una decisión.
recursos = ['/foo/bar', '/pepe/juan']
if recurso in recursos:
    # decisión

# 2) Definir los recursos habilitados en un diccionario donde las claves
# son los recursos solicitados y los valores, nuevos URIs

recursos = {’/foo/bar’: ‘/foo-bar.py’,
    ‘/pepe/juan’: ‘/inicio.py’}
script = recursos.get(recurso, ‘/inicio.py’)

print(“Content-type: text/html”)
print(“Location: {}”.format(script))
print(“”)

# Ejemplo de empleo del método HTTP
metodo = environ.get(‘REQUEST_METHOD’, ‘GET’)
metodo_requerido = ‘POST’
# Lo correcto: método es POST
# Negación (agrupación lógica): not (enunciado) 
# Hipótesis:
# Si el método no es correcto, rechazo tu solicitud
if not (metodo is metodo_permitido):
    print(“Content-type: text/html”)
    print(“Status: 405 Method Not Allowed”)
    …


# Sintaxis de escritura para cabeceras HTTP
print(“Content-type: <mime-type>“)
print(“Status: <estado HTTP>“)
print(“<Campo-de-Cabecera>: <valor del campo>“)
print(“”)
print(“<cuerpo del mensaje>")


# Recibir datos de una solicitud hecha a través del método GET
from os import environ
from urllib.parse import parse_qs

cadena_de_consulta = environ.get('QUERY_STRING', '')
parametros = parse_qs(cadena_de_consulta)

"""
El resultado se presenta en una salida de la shell de Python:
>>> qs = "nombre=Ana&apellido=perez&edad=12"
>>> from urllib.parse import parse_qs
>>> parse_qs(qs)
{’nombre’: ['Ana'], ‘apellido’: ['perez'], ‘edad’: ['12']}
>>> parse_qs(qs)['nombre']
['Ana']
>>> 
>>> parse_qs(qs)['nombre'][0]
‘Ana’
“””

# Recibir datos a partir de una solicitud hecha por POST
from cgi import FieldStorage

data = FieldStorage()
variable = data['NOMBRE DEL PARÁMETRO'].value

# NOMBRE DEL PARÁMETRO: puede ser el nombre de, por ejemplo, 
# un campo de formulario HTML como el que sigue
<form id='foobar' action='/recurso'>
    <input name='nombre' id='nombre' type="text">
    <input name='appelidos' id='apellidos' type="text">
    <input name='edad' id='edad' type="number">
    <input id='submit' type='submit' value='Enviar'>
</form>

# En Python obtendría el valor del campo ’nombre’ con estas instrucciones:
from cgi import FieldStorage
data = FieldStorage()
nombre = data['nombre'].value

# Subir archivos (es igual que recibir cualquier dato por POST)
# Si el formulario HTML es este:
<form id='foobar' action='/recurso' enctype='multipart/form-data'>
    <input name='archivo' id='archivo' type="file">
</form>

# El código Python será:
from cgi import FieldStorage
data = FieldStorage()
contenido = data['archivo'].value

with open(“/ruta/destino/archivo”, “wb”) as archivo:
    archivo.write(contenido)


# Conexiones a bases de datos
from <BIBLIOTECA> import connect

# Crear conexión
conexion = connect(**datos_acceso)
# Abrir cursor
cursor = conexion.cursor()
# Ejecutar consulta
cursor.execute(sql)
# Confirmar datos (para consultas de escritura)
conexion.commit()
# Recuperar datos (para consultas de lectura)
datos = cursor.fetchall()

# Cerrar cursor
cursor.close()
# Cerrar conexión
conexion.close()

# Independencia del código HTML
<!-- archivo foo.html -->
<p>Esto es un $modificador dentro del archivo foo.html</p>

# Archivo .py
from string import Template
with open(‘foo.html’, ‘r’) as archivo:
    html = archivo.read()

diccionario = dict(modificador=’valor variable’)
html = Template(html).safe_substitute(diccionario)

# Definición de cookies
# Mediante las cabeceras HTTP:
Set-Cookie: <nombre>=<valor>

# Mediante el módulo http.cookies:
from http.cookies import SimpleCookie
cookie = SimpleCookie()
cookie['SID'] = “123456”
print(cookie)

# Generar identificadores de alta entropía mediante funciones hash
from hashlib import <función hash>

from hashlib import sha1
resumen = sha1(b”una cadena compleja”).hexdigest()

# Los identificadores se pueden guardar en archivos ocultos
# NO usar archivos temporales
with open(‘/ruta/a/.directorio/.sid_{}’.format(sid)’…

# Leer cookies de una solicitud
from http.cookies import SimpleCookie
from os import environ

cookie = environ.get(‘HTTP_COOKIE’, ‘’)
cookies = SimpleCookie()
cookies.load(cookie)

sid = cookie['sid'].value