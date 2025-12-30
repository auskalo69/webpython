from cgi import FieldStorage
from os import environ 

from producto.model import ProductoModel
from producto.view import ProductoView

class ProductoController(object):
        
    def __init__(self):
        self.model = ProductoModel()
        self.view = ProductoView()

    def guardar(self):      
        data = FieldStorage()
        denominacion = data['denominacion'].value       
        precio = data['precio'].value
        precio = precio.replace(",", ".")
        barcode = data['barcode'].value

        errores = {}
        total_denominacion = len(denominacion)
        if total_denominacion < 4 or total_denominacion > 50:
            errores['denominacion'] = """El producto tiene una cantidad 
                    de caracteres no valido."""

        if precio.replace('.', '').isdigit():
            precio = float(precio)
        else:
            errores['precio'] = 'El precio no es válido'
        
        total_barcode = len(barcode)
        if total_barcode != 13:
            errores['barcode'] = "Barcode no correcto"

        if errores:
           self.view.agregar(errores) 
           exit()    

        self.model.denominacion = denominacion
        self.model.precio = precio
        self.model.barcode = barcode        
        self.model.insert()
        message = "guardado"
        self.view.mostrar_mensaje(self.model.producto_id, message)

    def agregar(self):
        self.view.agregar(errores={})  

    def ver(self, _id):      
        self.model.producto_id = int(_id)
        self.model.select()
        if self.model.producto_id == 0:
            message = "id inexistente"
            self.view.mostrar_mensaje(_id, message)
            exit() 
        self.view.ver(self.model)

    def eliminar(self, _id):
        self.model.producto_id = int(_id)
        self.model.delete()                
        message = "eliminado"
        self.view.mostrar_mensaje(_id, message)

    def editar(self, _id):
        self.model.producto_id = int(_id)
        self.datodecontacto_id = 0                                               
        self.denominacion = ""                                                   
        self.valor = self.model.select()
        if self.model.producto_id == 0:
            message = "ID. inexistente"
            self.view.mostrar_mensaje(_id, message)
            exit()
        self.view.editar(self.model)

    def actualizar(self):
        data = FieldStorage()
        producto_id = data['producto_id'].value
        denominacion = data['denominacion'].value
        precio = data['precio'].value
        barcode = data['barcode'].value       

        errores = {}                                                             
        total_denominacion = len(denominacion)                                   
        if total_denominacion < 4 or total_denominacion > 50:                    
            errores['denominacion'] = """roducto tiene una cantidad          
                    de caracteres no valido."""                                  
                                                                                 
        if precio.replace('.', '').isdigit():                                    
            precio = float(precio)                                               
                                                                                 
        total_barcode = len(barcode)                                             
        if total_barcode != 13:                                                  
            errores['barcode'] = "Barcode no correcto"                           
                                                                                 
        if errores:                                                              
           self.view.agregar(errores)                                            
           exit() 

        self.model.producto_id = producto_id
        self.model.denominacion = denominacion
        self.model.precio = precio
        self.model.barcode = barcode
        self.model.update()
        if self.model.producto_id == 0:
            message = "id inexistente"
            self.view.mostrar_mensaje(producto_id, message)
            exit()
 
        message = "actualizado"
        self.view.mostrar_mensaje(self.model.producto_id, message)
