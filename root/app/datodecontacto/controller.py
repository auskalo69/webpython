from cgi import FieldStorage
from os import environ

from datodecontacto.model import DatoDeContactoModel                                         
from datodecontacto.view import DatoDeContactoView  

class DatoDeContactoController(object):                                                
                                                                                  
    def __init__(self):                                                          
         self.model = DatoDeContactoModel()
         self.view = DatoDeContactoView()

    def guardar(self):
        data = FieldStorage()
        denominacion = data['denominacion'].value
        valor = data['valor'].value
        """ 
        print("Content-Type: text/plain\n")
        print("")
        print(denominacion, valor)
        """
        
        errores = {}
        total_denominacion = len(denominacion)                                   
        if total_denominacion < 4 or total_denominacion > 40:
             errores['denominacion'] = """El dato de contacto tiene una cantidad          
                     de caracteres no valido."""    
        
        total_valor = len(valor)                                   
        if total_valor < 9 or total_valor > 100:
             errores['valor'] = """El valor tiene una cantidad          
                     de caracteres no válido."""    

        if errores:                                                              
            self.view.agregar(errores)                                            
            exit()
    
        self.model.denominacion = denominacion
        self.model.valor = valor
        self.model.insert()
        message = "Guardado"
        self.view.mostrar_mensaje(self.model.datodecontacto_id, message)
        

    def agregar(self):
        self.view.agregar(errores={})
    
    def ver(self, _id):                                                          
        self.model.datodecontacto_id = int(_id)                                        
        self.model.select()                                                      
        if self.model.datodecontacto_id == 0:                                          
            message = "id inexistente"                                           
            self.view.mostrar_mensaje(_id, message)                              
            exit()                                                               
        self.view.ver(self.model) 

        
