from cgi import FieldStorage
from os import environ

from albaran.model import AlbaranModel                                         
from albaran.view import AlbaranView  

class AlbaranController(object):                                                
                                                                                  
    def __init__(self):                                                          
        self.model = AlbaranModel()
        self.view = AlbaranView()

    def cambiarestado(self):
        self.view.cambiarestado()

        
