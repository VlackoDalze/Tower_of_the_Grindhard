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
        name: str,
        description: str,
        level: int,
        baseStats: Statistics,
        activeAbilities,
        passiveAbilities,
        positionX: int,
        positionY: int,
        scene_level,
        
    ):
        self.screen = screen
        self.name = name
        self.description = description
        self.image = Enemy.searchEnemy(name)
        self.baseStats = baseStats
        self.activeAbilities = []
        if activeAbilities!=None:
            for ability in activeAbilities:
                self.activeAbilities.append(ability)
        self.passiveAbilities = passiveAbilities
        self.activeAbilities = activeAbilities
        self.positionX = positionX
        self.positionY = positionY
        self.scene_level = scene_level
        self.level = level
       
    def getActiveAbilities(self):
        return self.activeAbilities
    
    def addActiveAbilitie(self, activeAbilitie):
        self.activeAbilities.append(activeAbilitie)

    def getStats(self):
        return self.baseStats
    
    def getPositionX(self):
        return self.positionX
       
    def getPositionY(self):
        return self.positionY
    
    def getImageDefault(self):
        return  pygame.image.load(self.image[0])
    
    def drawEnemy(self):
        enemy = pygame.Surface((CELL_SIZE, CELL_SIZE))
        fondo = pygame.image.load(font)
        image = pygame.image.load(self.image[Enemy.index_animation])
        # mix2=pygame.image.load(self.imagen[1])
        enemy.blit(fondo, (0, 0))
        enemy.blit(image, (0, 0))
        self.screen.blit(enemy, (self.positionX, self.positionY))

        if Enemy.iteration >= 100:
            Enemy.index_animation = 1
        else:
            Enemy.index_animation = 0

        if Enemy.iteration <= 200:
            Enemy.iteration += 1
        else:
            Enemy.iteration = 0

        if str(self.positionX) + "-" + str(self.positionY) not in collision_enemy:
            collision_enemy.append(str(self.positionX) + "-" + str(self.positionY))
