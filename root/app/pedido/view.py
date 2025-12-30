from string import Template                                                      
                                                                                 
                                                                                 
class PedidoView(object):                                                      
                                                                                 
    def ok(self, errores={}):
        with open('static/templates/pedido_agregar.html', 'r') as f:
            html = f.read()                    
        

        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)                                   
                                                                                 

