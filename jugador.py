from personaje import Personaje
class Jugador(Personaje):
    #atributos
    inventario = []
    raza=None
    equipamento=[]

    #constructor
    def __init__(self,nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas,posicionX,posicionY,raza):
        super().__init__(nombre, descripcion, imagen, estadisticasBase, habilidadesActivas,habilidadesPasivas,posicionX,posicionY)
        self.raza =raza

    #metodos
    def equipar(self, item):
        self.equipamento.append(item)
        
    def addToInventario(self,item):
        self.inventario.append(item)
        
    def removeFromInventario(self,item):
        self.inventario.remove(item)

    def move(self,movimiento_izquierda, movimiento_derecha,movimiento_abajo,movimiento_arriba):
        direction_x = 0
        direction_y = 0

        if movimiento_izquierda:
            direction_x = -super().getCellSize()
        if movimiento_derecha:
            direction_x = super().getCellSize()
        if movimiento_abajo:
            direction_y = super().getCellSize()
        if movimiento_arriba:
            direction_y = -super().getCellSize()
        
        self.rect.x += direction_x
        self.rect.y += direction_y

    