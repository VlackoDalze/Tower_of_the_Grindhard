from personaje import Personaje
class Jugador(Personaje):
    #atributos
    inventario = []
    raza=None
    equipamento=[]

    #constructor
    def __init__(self,nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas,raza):
        super().__init__(nombre, descripcion, imagen, estadisticasBase, habilidadesActivas,habilidadesPasivas)
        self.raza =raza
      
        
    #metodos
    def equipar(self, item):
        self.equipamento.append(item)
        
    def addToInventario(self,item):
        self.inventario.append(item)
        
    def removeFromInventario(self,item):
        self.inventario.remove(item)