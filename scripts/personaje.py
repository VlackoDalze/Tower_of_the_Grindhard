import pygame
from scripts.estadisticas import Estadisticas
import scripts.setting as setting
from scripts.habilidad_pasiva_unica import PasivaUnica


class Personaje(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, nombre: str, descripcion: str, imagen: pygame.Surface, estadisticasBase: Estadisticas, habilidadesActivas, habilidadesPasivas, posicionX:int, posicionY:int):
        pygame.sprite.Sprite.__init__(self)
        self.CELL_SIZE = setting.CELL_SIZE
        self.player_texture = imagen
        #con get.rect obtenermos los ejes X y Y 
        self.rect = self.player_texture.get_rect()
        #se le suma 16 para acomodar la imagen, esto no afecta a los ejes X y y
        self.rect.center = ((posicionX * self.CELL_SIZE)+16,(posicionY * self.CELL_SIZE)+16)
        self.screen = screen
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen
        self.estadisticasBase = estadisticasBase
        self.habilidadesActivas = habilidadesActivas
        self.habilidadesPasivas = habilidadesPasivas
        
        # lo mismo que rect, pero descompuesto, tambien se puedo usar rect.x o rect.y pero preferi usar los parametros que por algo los ponemos
        self.posicionX = posicionX*self.CELL_SIZE
        self.posicionY = posicionY*self.CELL_SIZE
        
    # metodos
    # get de posicion del jugador

    def getPositionX(self):
        return self.posicionX

    def getPositionY(self):
        return self.posicionY

    def getScreen(self):
        return self.screen
    
    # recibe ataque es un array con dos valores el daño  y el tipo de daño
    def defender(self, recibeAtaque):
        dano = recibeAtaque[0]
        tipoDeDano = recibeAtaque[1]
        if int(tipoDeDano) == 0:  # 0 fisico
            return Estadisticas(self.estadisticasBase).getDefensaFisica()-float(dano)
        else:  # 1 magico
            return Estadisticas(self.estadisticasBase).getDefensaMagica()-float(dano)

    def atacar(self, tipoDeDano):
        if int(tipoDeDano) == 0:  # 0 fisico
            return (Estadisticas(self.estadisticasBase).getAtaqueFisico(), 0)
        else:  # 1 magico
            return (Estadisticas(self.estadisticasBase).getAtaqueMagico(), 1)

    def getCellSize(self):
        return self.CELL_SIZE

    # pasiva unica y otras pasivas -a
    def activarPasivas(self):
        PasivaUnica(self.habilidadesPasivas).activar()

    def desactivarPasivas(self):
        PasivaUnica(self.habilidadesPasivas).desactivar()
