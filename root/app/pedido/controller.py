from cgi import FieldStorage
from os import environ

from pedido.model import PedidoModel                                         
from pedido.view import PedidoView  

class PedidoController(object):                                                
                                                                                  
    def __init__(self):                                                          
        self.model = PedidoModel()
        self.view = PedidoView()

    def ok(self):
        self.view.ok()

        
