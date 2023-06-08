from ClaseSabor import Sabor
class Helado:
    __gramos=0
    __precio=0
    __sabores=[]
    
    def addSabor(self,sabor):
        self.__sabores.append(sabor)
        
    def __init__(self, gramos, precio, sabor=None):
        self.__gramos=gramos
        self.__precio=precio
        self.__sabores=[]
        if sabor!=None:
            self.addSabor(sabor)
        
        
        
    def __str__(self):
        s=("Gramos {}, precio {}\n".format(self.__gramos,self.__precio))
        for sabore in self.__sabores:
            s+=str(sabore)+"\n"
            
        return s

    def mostrarSoloSabor(self):
        for sabor in self.__sabores:
            print(sabor)


    def getGramo(self):
        return self.__gramos


    def buscarSabor(self, Id):
        cont=0
        for sabor in self.__sabores:
            if int(sabor.getIdSabor())==int(Id):
                cont+=1

        return cont


    def sumarCantidad(self,idC):
        suma=0
        #print("mostrar cuantos sabores tiene")
        #print(sabor)
        for sabor in self.__sabores:
            cant=0
            if int(sabor.getIdSabor())==int(idC):
                cant=int(self.__gramos)/int(len(self.__sabores))
                print("la cantidad de sabores es {}".format(len(self.__sabores)))
                print("la cantidad de gramos es {}".format(self.__gramos))
                print("la cantidad es {}".format(cant))
                suma+=cant
        print("la cantidad ya sumada es {}".format(suma))
        return suma


    
    
    

        
        
        
    
        