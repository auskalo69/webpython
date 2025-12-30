from cgi import FieldStorage
from os import environ

from agenda.model import AgendaModel                                         
from agenda.view import AgendaView  

class AgendaController(object):                                                
                                                                                  
    def __init__(self):                                                          
        self.model = AgendaModel()
        self.view = AgendaView()

    def agregar(self):
        self.view.agregar()

        
