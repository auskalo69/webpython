from core.db import sql_execute
from settings import datos_acceso

class ProductoModel(object):

    def __init__(self):
        self.producto_id = 0
        self.denominacion = ""
        self.precio = 0.0
        self.barcode = ""

    def insert(self):
        sql = """
              INSERT INTO producto
              (denominacion, precio, barcode)
              VALUES (%s, %s, %s)
        """
        datos = list(vars(self).values())[1:]
        self.producto_id = sql_execute(datos_acceso, sql, datos)
        
    def update(self):
        sql = """
            UPDATE producto
            SET denominacion = %s, precio = %s, barcode = %s
            WHERE producto_id = %s
        """
        datos = (self.denominacion, self.precio, self.barcode, self.producto_id)
        if sql_execute(datos_acceso, sql, datos) == 0:
            self.producto_id = 0
        
    def select(self):        
        sql = """                                        
            SELECT denominacion, precio, barcode                    
            FROM producto                                           
            WHERE producto_id = %s
        """ 
        datos = (self.producto_id,)        
        if (resultados := sql_execute(datos_acceso, sql, datos)):
            self.denominacion = resultados[0][0]
            self.precio = resultados[0][1]
            self.barcode = resultados[0][2]
        else:
            self.producto_id = 0
     
    def delete(self):
        sql = "DELETE FROM producto WHERE producto_id = %s"
        datos = (self.producto_id,)    
        sql_execute(datos_acceso, sql, datos)

