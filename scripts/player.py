from scripts.character import Character
from scripts.setting import SILVER_MEDIUM_FONT
import pygame
from scripts.collider_matrix_maker import get_collider_matrix
from scripts.triggers import Triggers
from scripts.enemigo import collision_enemy
WHITE = (255, 255, 255)


class Player(Character):
    newID = 0
    def __init__(self, screen: pygame.Surface, name, description, image, baseStats, activeAbilities, passiveAbilities, posX, posY, race, sceneLevel):
        super().__init__(screen, name, description, image, baseStats,activeAbilities, passiveAbilities, posX, posY)
        self.flip = False
        self.direction = 1
        self.id = Player.newID
        Player.newID += 1
        self.race = race
        self.sceneLevel = sceneLevel
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.inventory = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        self._pause = False
        self._interfaceActive = True
        self._inventoryActive = False
        self._mapActive = False
        self._settingActive = False

    # Methods

    def toggleBoolean(self, booleanValue:bool):
        if booleanValue == False:
            return True
        else:
            return False

    def equip(self, item):
        self.equipment.append(item)

    def addToInventory(self, item):
        self.inventory.append(item)

    def removeFromInventory(self, item):
        self.inventory.remove(item)

    def getId(self):
        return self.id

    def getScreen(self):
        return self.screen

    def getSceneLevel(self):
        return self.sceneLevel

    def getDirectionMove(self):
        if self.right:
            return 'right'
        elif self.left:
            return 'left'
        elif self.up:
            return 'up'
        else:
            return 'down'

    def move(self, event, assignedKeys):
        # *Control area
        movement_speed = super().getCellSize()
        listaKeys = [[pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q],
                    [pygame.K_g, pygame.K_j, pygame.K_y, pygame.K_h, pygame.K_t],
                    [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RSHIFT],
                    [pygame.K_KP_4, pygame.K_KP_6, pygame.K_KP_8, pygame.K_KP_5, pygame.K_KP_7]]
                    
        # *Movement area
        aux_x = self.posX
        aux_y = self.posY

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][0]:
            aux_x -= movement_speed  
            self.left = True
            self.right = False
            self.up = False
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][1]:
            aux_x += movement_speed
            self.left = False
            self.right = True
            self.up = False
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][2]:
            aux_y -= movement_speed
            self.left = False
            self.right = False
            self.up = True
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][3]:
            aux_y += movement_speed
            self.left = False
            self.right = False
            self.up = False
            self.down = True

        colisiones = drawCollider(super().getCellSize(), self.sceneLevel)

        if str(aux_x) + "-" + str(aux_y) not in colisiones and str(aux_x) + "-" + str(aux_y) not in collision_enemy:
            self.posX = aux_x
            self.posY = aux_y
            self.rect.x = aux_x
            self.rect.y = aux_y

            Triggers.searchListTriggers([self.posX, self.posY], self.sceneLevel, event, self.id)

    def draw(self):
        self.screen.blit(pygame.transform.flip(
            self.player_texture, self.flip, False), self.rect)


def drawCollider(sizeCell, sceneLevel):
    map_collider_matriz = get_collider_matrix(sceneLevel)
    eje_x = 0  # x-axis
    eje_y = 0  # y-axis
    colisiones = []
    for row in map_collider_matriz:
        for column in row:
            if (column == '1'  or column == '4'):  # wall and decoration collision
                colisiones.append(str(eje_x)+"-"+str(eje_y))
            eje_x = eje_x + sizeCell  # increase x by +32
        eje_y = eje_y + sizeCell  # increase y by +32
        eje_x = 0  # reset x
    return colisiones
