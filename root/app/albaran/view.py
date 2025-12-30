from string import Template                                                      
                                                                                 
                                                                                 
class AlbaranView(object):                                                      
                                                                                 
    def cambiarestado(self, errores={}):
        with open('static/templates/albaran_cambiarestado.html', 'r') as f:
            html = f.read()                    
        
        print("Content-Type: text/html")                                         
        print("")                                                                
        print(html)                                   
                                                                                 

