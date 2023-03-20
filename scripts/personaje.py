import pygame
from scripts.estadisticas import Estadisticas as Estadisticas
import scripts.setting as setting
from habilidad_pasiva_unica import PasivaUnica

class Personaje(pygame.sprite.Sprite):
    #atributos
    nombre = None
    descripcion = None
    imagen = None
    estadisticasBase = None
    habilidadesActivas = None
    habilidadesPasivas = None

    #constructor
    def __init__(self, nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas, posicionX,posicionY):
        pygame.sprite.Sprite.__init__(self)
        self.CELL_SIZE = setting.CELL_SIZE
        self.player_texture = imagen
        self.rect = self.player_texture.get_rect()
        self.rect.center = ((posicionX * self.CELL_SIZE)+16, (posicionY * self.CELL_SIZE)+16)

        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen
        self.estadisticasBase = estadisticasBase
        self.habilidadesActivas = habilidadesActivas
        self.habilidadesPasivas = habilidadesPasivas
        
    #metodos
    def defender(self,recibeAtaque): #recibe ataque es un array con dos valores el daño  y el tipo de daño
        dano = recibeAtaque[0]
        tipoDeDano = recibeAtaque[1]
        if int(tipoDeDano)==0: #  0 fisico
            return Estadisticas(self.estadisticasBase).getDefensaFisica()-float(dano)
        else: # 1 magico
            return Estadisticas(self.estadisticasBase).getDefensaMagica()-float(dano)

    def atacar(self,tipoDeDano):
        if int(tipoDeDano)==0: #  0 fisico
            return (Estadisticas(self.estadisticasBase).getAtaqueFisico(),0)
        else:  # 1 magico
            return (Estadisticas(self.estadisticasBase).getAtaqueMagico(),1)

    def draw(self, screen):
        screen.blit(self.player_texture, self.rect)

    def getCellSize(self):
        return self.CELL_SIZE

      #pasiva unica y otras pasivas -a
    def activarPasivas(self):
      PasivaUnica(self.habilidadesPasivas).activar()

    def desactivarPasivas(self):
       PasivaUnica(self.habilidadesPasivas).deactivar()