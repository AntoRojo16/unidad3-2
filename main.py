from ClaseHelado import Helado
from ClaseSabor import Sabor
from claseManejadorHelados import ManejadorHelados
from claseManejadorSabores import ManejadorSabores
if __name__=="__main__":
    #unSabor=Sabor(123,"leche y cacao","chocolate")
    #otroSabor=Sabor(234,"leche y almendra","almendra")
    #unHelado=Helado(150,500,unSabor)
    #unHelado.addSabor(otroSabor)
    #print(unHelado)
    sabores=ManejadorSabores()
    sabores.inicializar()
    print(sabores)
    heladosVendidos=ManejadorHelados()
    heladosVendidos.venta(sabores)
    heladosVendidos.venta(sabores)
    heladosVendidos.venta(sabores)
    #heladosVendidos.venta(sabores)
    #heladosVendidos.venta(sabores)
    print("mostrar todos los helados vendidos")
    heladosVendidos.mostrarHeladosVendidos()
    heladosVendidos.contarSabor(sabores)
    heladosVendidos.ejercicio3(sabores)
    heladosVendidos.ejrcicio4()