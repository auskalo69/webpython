from string import Template


class ProductoView(object):
    
    def agregar(self, errores={}):
        with open('static/templates/producto_agregar.html', 'r') as f:
            html = f.read()
        
        if not errores:
            errores["denominacion"] = ""
            errores["precio"] = ""
            errores["barcode"] = ""
            html = Template(html).safe_substitute(errores)
        else:            
            html = Template(html).safe_substitute(errores)
            html = html.replace("$denominacion", "")
            html = html.replace("$precio", "")
            html = html.replace("$barcode", "")

        print("Content-Type: text/html")
        print("")
        print(html)             


    def mostrar_mensaje(self, producto_id, message):
        with open('static/templates/mensaje.html', 'r') as f:                      
            html = f.read()           
 
        diccionario = dict(
            id_producto = producto_id,
            mensaje = message
        )                                             
        html = Template(html).safe_substitute(diccionario)

        if not message == "eliminado":
            print(f"Refresh: 3, URL=/producto/ver/{producto_id}")

        print("Content-Type: text/html")
        print("")                                                                   
        print(html)       

   
    def ver(self, modelo):
        with open('static/templates/producto_ver.html', 'r') as f:           
            html = f.read()
                                                                      
        diccionario = dict(
            title="Ver Producto",                                                      
            producto_id=modelo.producto_id,
            denominacion=modelo.denominacion,
            precio=modelo.precio,
            barcode=modelo.barcode,                                            
        )                                                                                
        html = Template(html).safe_substitute(diccionario)
        print("Content-Type: text/html") 
        print("")
        print(html)

    def editar(self, modelo, errores={}):                       
        with open("static/templates/producto_editar.html") as f:
            html = f.read()

        diccionario = dict(
            title="Editar Producto",
            producto_id=modelo.producto_id,
            denominacion=modelo.denominacion,
            precio=modelo.precio,
            barcode=modelo.barcode,
        )
        html = Template(html).safe_substitute(diccionario)        
        print("Content-Type: text/html") 
        print("")
        print(html)

