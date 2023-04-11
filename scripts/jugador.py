from scripts.personaje import Personaje as Personaje
from scripts.setting import SILVER_MEDIUM_FONT
import pygame
from scripts.collider_matrix_maker import get_collider_matrix
from scripts.triggers import Triggers
WHITE = (255, 255, 255)


class Jugador(Personaje):
    newID=0
    def __init__(self, screen: pygame.Surface, nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas, posicionX, posicionY, raza, scene_level):
        super().__init__(screen, nombre, descripcion, imagen, estadisticasBase,
                         habilidadesActivas, habilidadesPasivas, posicionX, posicionY)
        self.flip = False
        self.direction = 1
        self.id=Jugador.newID
        Jugador.newID+=1
        self.raza = raza

        self.scene_level=scene_level
        
        self.inventory = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]

        self._pause = False
        self._interface_active = True
        self._inventory_active = False
        self._map_active = False
        self._setting_active = False

        self.inventory_bag_texture = pygame.image.load(
            'assets/gui/inventory/inventory_bag_panel.png')
        self.inventory_button_texture = pygame.image.load(
            'assets/gui/inventory/inventory_button.png')
        self.inventory_equipment_panel_texture = pygame.image.load(
            'assets/gui/inventory/inventory_equipment_panel.png')
        self.inventory_equipment_area_texture = pygame.image.load(
            'assets/gui/inventory/equipment_area.png')
        self.Inventory_slot = pygame.image.load(
            "./assets/gui/inventory/inventory_slot.png")

        # Crea un grupo de Sprite y añade los Sprite dentro al grupo
        # self.inventory_sprites_group = pygame.sprite.Group()
        # self.inventory_sprites_group.add(self.inventory_bag_texture)
        # self.inventory_sprites_group.add(self.inventory_button_texture)
        # self.inventory_sprites_group.add(self.inventory_equipment_panel_texture)
        # self.inventory_sprites_group.add(self.inventory_equipment_area_texture)

    # metodos

    def toggleBoolean(self, booleanValue):
        if booleanValue == False:
            return True
        else:
            return False

    def equipar(self, item):
        self.equipamento.append(item)

    def addToInventario(self, item):
        self.inventario.append(item)

    def removeFromInventario(self, item):
        self.inventario.remove(item)

    def getId(self):
        return self.id

    def getScreen(self):
        return self.screen

    def move(self, event, assignedKeys):
        # *Area de controles
        movement_speed = super().getCellSize()
        listaKeys = [[pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,pygame.K_q],
                     [pygame.K_g, pygame.K_j, pygame.K_y, pygame.K_h,pygame.K_t],
                     [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,pygame.K_RSHIFT],
                     [pygame.K_KP_4, pygame.K_KP_6, pygame.K_KP_8, pygame.K_KP_5,pygame.K_KP_7]]
           # * Area de movimientos
        aux_x =self.posicionX
            
        aux_y = self.posicionY

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][0]:
            aux_x  -=movement_speed  
            # self.posicionX -= movement_speed
        if  event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][1]:
            aux_x  += movement_speed
            # self.posicionX += movement_speed
        if  event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][2]:
            aux_y-=movement_speed
            # self.posicionY -= movement_speed
        if  event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][3]:
            aux_y+=movement_speed
            # self.posicionY += movement_speed      
        # if  event.type == pygame.KEYDOWN and event.key == pygame.K_i:  # Inventario
        #     self.toggleInventory()
        # if  event.type == pygame.KEYDOWN and  event.key == pygame.K_m:  # Mapa
        #     self.toggleMap()
        # if event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:  # Opciones
        #     self.toggleSetting()

        colisiones = drawCollider(super().getCellSize(),self.scene_level)
        
        if str(aux_x)+"-"+str(aux_y) not in colisiones:
            self.posicionX = aux_x
            self.posicionY = aux_y
            self.rect.x = aux_x
            self.rect.y = aux_y
            #if event.type == pygame.KEYUP :
            #comprobar triggers

            Triggers.searchListTriggers([self.posicionX ,self.posicionY],self.scene_level,event,self.id)

    def draw(self):
        self.screen.blit(pygame.transform.flip(
            self.player_texture, self.flip, False), self.rect)


def drawCollider(sizeCell,scene_level):
    map_collider_matriz = get_collider_matrix(scene_level)
    eje_x = 0  # eje x
    eje_y = 0  # eje y
    colisiones = []
    for row in map_collider_matriz:
        for column in row:

            if (column == '1'  or column == '4'):  # colision murosy adornos
                colisiones.append(str(eje_x)+"-"+str(eje_y))

            eje_x = eje_x + sizeCell  # aumenta x +32

        eje_y = eje_y + sizeCell  # aumenta y+32
        eje_x = 0  # resets x
    return colisiones
