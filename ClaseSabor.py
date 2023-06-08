class Sabor:
    __idSabor=0
    __ingredientes=""
    __nombre=""
    
    
    def __init__(self,Id,ingrediente,nombre):
        self.__idSabor=Id
        self.__ingredientes=ingrediente
        self.__nombre=nombre
        
        
    def  __str__(self):
        return ("Id del sabor {}, ingredientes {}, Nombre del sabor {}".format(self.__idSabor,self.__ingredientes,self.__nombre))




    def getIdSabor(self):
        return self.__idSabor


    def getNombre (self):
        return self.__nombre