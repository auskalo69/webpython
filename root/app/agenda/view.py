from string import Template                                                      
                                                                                 
                                                                                 
class AgendaView(object):                                                      
                                                                                 
    def agregar(self, errores={}):
        with open('static/templates/agenda_agregar.html', 'r') as f:
            html = f.read()                    
        
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)                                   
                                                                                 

