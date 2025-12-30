from string import Template                                                      
                                                                                 
                                                                                 
class DatoDeContactoView(object):                                                      
                                                                                 
    def agregar(self, errores={}):
        with open('static/templates/datodecontacto_agregar.html', 'r') as f:
            html = f.read()                    
     
        if not errores:                                                              
            errores["denominacion"] = ""                                         
            errores["valor"] = ""                                               
            html = Template(html).safe_substitute(errores)                       
        else:                                                                    
            html = Template(html).safe_substitute(errores)                       
            html = html.replace("$denominacion", "")                             
            html = html.replace("$valor", "")    
        
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)                                   
                                                                                 

    def mostrar_mensaje(self, datodecontacto_id, message):                             
        with open('static/templates/mensaje.html', 'r') as f:                    
            html = f.read()                                                      
                                                                                 
        diccionario = dict(                                                      
            id_producto = datodecontacto_id,                                           
            mensaje = message                                                    
        )                                                                        
        html = Template(html).safe_substitute(diccionario)                       
                                                                                 
        if not message == "eliminado":                                           
            print(f"Refresh: 3, URL=/datodecontacto/ver/{datodecontacto_id}")                
                                                                                 
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)                  

    def ver(self, modelo):                                                       
        with open('static/templates/datodecontacto_ver.html', 'r') as f:               
            html = f.read()                                                      
                                                                                 
        diccionario = dict(                                                      
            title="Ver Dato de Contacto",                                                
            datodecontacto_id=modelo.datodecontacto_id,                                      
            denominacion=modelo.denominacion,                                    
            valor=modelo.valor                                                
        )                                                                        
        html = Template(html).safe_substitute(diccionario)                       
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html) 

    def editar(self, modelo, errores={}):                                        
        with open("static/templates/datodecontacto_editar.html") as f:                 
            html = f.read()                                                      
                                                                                 
        diccionario = dict(                                                      
            title="Editar Dato de Contacto",                                             
            producto_id=modelo.datodecontacto_id,                                      
            denominacion=modelo.denominacion,                                    
            precio=modelo.valor                                                
        )                                                                        
        html = Template(html).safe_substitute(diccionario)                       
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)   
