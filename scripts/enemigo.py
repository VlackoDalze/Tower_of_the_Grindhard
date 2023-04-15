import pygame
from scripts.statistics import Statistics
import scripts.setting as setting
from scripts.unique_passive import UniquePassive

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
letter_style = "assets/font/Silver.ttf"

font = "assets/dungeon/floor/sandstone_floor_0.png"
color = (255, 255, 255)
texture_enemy = [
    ["Esqueleto1", "assets/monster/undead/skeletons/skeleton_humanoid_small_old.png"],
    ["Esqueleto2", "assets/monster/undead/skeletons/skeleton_humanoid_small_new.png"],
]
collision_enemy = []


class Enemy:
    index_animation = 0
    iteration = 0

    def searchEnemy(nombre: str):
        animation_enemy = []
        for enemy in texture_enemy:
            if str(enemy[0]).startswith(nombre):
                animation_enemy.append(enemy[1])
        return animation_enemy

    # constructor
    def __init__(
        self,
        screen: pygame.Surface,
        nombre: str,
        descripcion: str,
        nivel: int,
        estadisticasBase: Statistics,
        habilidadesActivas,
        habilidadesPasivas,
        posicionX: int,
        posicionY: int,
        scene_level,
    ):
        self.screen = screen
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = Enemy.searchEnemy(nombre)
        self.estadisticasBase = estadisticasBase
        self.habilidadesActivas = habilidadesActivas
        self.habilidadesPasivas = habilidadesPasivas
        self.posicionX = posicionX
        self.habilidadesActivas = habilidadesActivas
        self.posicionY = posicionY
        self.scene_level = scene_level
        self.nivel = nivel

    def getPositionX(self):
        return self.posicionX

    def getPositionY(self):
        return self.posicionY

    def drawEnemy(self):
        enemy = pygame.Surface((CELL_SIZE, CELL_SIZE))
        fondo = pygame.image.load(font)
        image = pygame.image.load(self.imagen[Enemy.index_animation])
        # mix2=pygame.image.load(self.imagen[1])
        enemy.blit(fondo, (0, 0))
        enemy.blit(image, (0, 0))
        self.screen.blit(enemy, (self.posicionX, self.posicionY))

        if Enemy.iteration >= 100:
            Enemy.index_animation = 1
        else:
            Enemy.index_animation = 0

        if Enemy.iteration <= 200:
            Enemy.iteration += 1
        else:
            Enemy.iteration = 0

        if str(self.posicionX) + "-" + str(self.posicionY) not in collision_enemy:
            collision_enemy.append(str(self.posicionX) + "-" + str(self.posicionY))
