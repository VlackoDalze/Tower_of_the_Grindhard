from personaje import Personaje
import pygame
class Jugador(Personaje):
    #atributos
    inventario = []
    raza=None
    equipamento=[]

    #constructor
    def __init__(self,nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas,posicionX,posicionY,raza):
        super().__init__(nombre, descripcion, imagen, estadisticasBase, habilidadesActivas,habilidadesPasivas,posicionX,posicionY)
        self.flip = False
        self.direction = 1
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
        movement_speed = super().getCellSize();

        if movimiento_izquierda:
            direction_x = -movement_speed
            self.flip = True
            self.direction = -1
        if movimiento_derecha:
            direction_x = movement_speed
            self.flip = False
            self.direction = 1
        if movimiento_abajo:
            direction_y = movement_speed
        if movimiento_arriba:
            direction_y = -movement_speed
        
        self.rect.x += direction_x
        self.rect.y += direction_y

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.player_texture, self.flip, False) , self.rect)

    