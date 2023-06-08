import csv
from ClaseSabor import Sabor
class ManejadorSabores:
    __lista=[]
    
    
    def __init__(self):
        self.__lista=[]
        
        
    def agregarSabor(self,sabor):
        self.__lista.append(sabor)
        
        
    def inicializar(self):
        archivo=open("sabores.csv")
        reader=csv.reader(archivo,delimiter=",")
        band=True
        for fila in reader:
            if band:
                band= not band
            else:
                Id=fila[0]
                ingrediente=fila[1]
                nombre=fila[2]
                unSabor=Sabor(Id,ingrediente,nombre)
                self.agregarSabor(unSabor)
        archivo.close()
        
        
        
    def __str__(self):
        s=""
        for sabore in self.__lista:
            s+=str(sabore)+"\n"
            
        return s
                
   
    
    def getSabores(self):
        return self.__lista
        
            
            
            