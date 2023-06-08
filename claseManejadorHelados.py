from claseManejadorSabores import ManejadorSabores
from ClaseHelado import Helado
from ClaseSabor import Sabor
def jls_extract_def():
    return "cont"


class ManejadorHelados:
    __lista=[]
    
    
    
    
    def __init__(self):
        self.__lista=[]
        
        
    def agregarHelado(self,helado):
        print(helado)
        self.__lista.append(helado)
        
        
          
    def venta(self,sabores):
        gramos=input("ingrese gramos")
        precio=input("ingrese precio")
        cantidad=int(input("Ingrse la cantidad de sabores"))
        print("Mostrar sabores de helados")
        print(sabores)
        unHelado=Helado(gramos,precio)
        for i in range(cantidad):
            Id=input("ingrese id del sabor: ")
            sabor=sabores.getSabores()[int(Id)-1]
            unHelado.addSabor(sabor)
        self.agregarHelado(unHelado)
        
        
        
    def mostrarHeladosVendidos(self):
        for helado in self.__lista:
            print(helado)
        
    def contarSabor(self,sabores):
        datos={}
        contadores=[]
        for i in range(len(sabores.getSabores())):
            datos={"cont":0,"Id":i+1}
            contadores.append(datos)
        for i in range(len(contadores)):
            for j in range(len(self.__lista)):
                helado=self.__lista[j]
                contadores[i]["cont"]+=int(helado.buscarSabor(contadores[i]["Id"]))

        contadores.sort(key=lambda x: x["cont"],reverse=True)
        print("\n      los sabores mas vendidos son:      ")
        #for i in range(5):
         #   idC=contadores[i]["Id"]
          #  j=0
           # sabor=sabores.getSabores()[j]
            #idS=sabor.getIdSabor()
            #while j<len(sabores.getSabores())and (int(idC)!=int(idS)):
             #   j+=1
              #  sabor=sabores.getSabores()[j]
               # idS=sabor.getIdSabor()

            #if j<len(sabores.getSabores()):
             #   print("uno de los helados mas vendidos es: {}".format(sabor.getNombre()))
            #else:
             #   print("eror no se pudo encontrar el sabor")

        for i in range(5):
            idC=contadores[i]["Id"]
            sabor=sabores.getSabores()[int(idC-1)]
            print("uno de los helados mas vendidos es: {}".format(sabor.getNombre()))
            print("la cantidad es {}".format(contadores[i]["cont"]))

    
    def ejercicio3(self,sabores):
        total=0
        nuevoId=input("Ingrese en numero de id del sabor que se desea contar")
        for helado in self.__lista:
            total+=helado.sumarCantidad(nuevoId)
        
        sabor=sabores.getSabores()[int(nuevoId)-1]
        print("La cantita total de gramos vendidios para el helado {} es: {}".format(sabor.getNombre(),total))

    def ejrcicio4(self):
        tipo=input("Ingrese la el tipo de helado (gr)")
        for helado in self.__lista:
            gramos=helado.getGramo()
            print("para este tipo de helado los sabores que se pidieron son")
            if int(gramos)==int(tipo):
                helado.mostrarSoloSabor()

    def ejercico5(self):


        dic={}
        lista=[]
        for i in range(5):
            gr=input("ingrese los gramos")
            dic={"tipo":gr,"suma":0}
        for i in range(5):
            j=0
            unHelado=self.__lista[j]
            gramos=unHelado.getGramo()
            while(int(gramos)!=int()):


        



        




        
    
            
            
        
        
        