from core.db import sql_execute                                                  
from settings import datos_acceso                                                
                                                                                 
class DatoDeContactoModel(object):

    def __init__(self):                                                          
        self.datodecontacto_id = 0                                                 
        self.denominacion = ""                                                   
        self.valor = ""

    def insert(self):
        sql = """                                                                
            INSERT INTO datodecontacto                                               
            (denominacion, valor)                                    
            VALUES (%s, %s)
        """ 
        datos = list(vars(self).values())[1:]
        self.datodecontacto_id = sql_execute(datos_acceso, sql, datos)

    def update(self):
        sql = """
            UPDATE datodecontacto                                                      
            SET denominacion = %s, valor = %s                    
            WHERE datodecontacto_id = %s 
        """
        datos = (self.denominacion, self.valor, self.producto_id)
        if sql_execute(datos_acceso, sql, datos) == 0:
            self.datodecontacto_id = 0

    def select(self):
        sql = """
            SELECT denominacion, valor
            FROM datodecontacto
            WHERE datodecontacto_id = %s
        """
        datos = (self.datodecontacto_id,)
        if (resultados := sql_execute(datos_acceso, sql, datos)):
            self.denominacion = resultados[0][0]
            self.valor = resultados[0][1]
        else:
            self.datodecontacto_id = 0

    def delete(self):
        sql = "DELETE FROM datodecontacto WHERE datodecontacto_id = %s"
        datos = (self.datodecontacto_id,)
        sql_excute(datos_acceso, sql, datos)

