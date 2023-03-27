from scripts.personaje import Personaje as Personaje
from scripts.setting import SILVER_MEDIUM_FONT
import pygame
WHITE = (255, 255, 255)


class Jugador(Personaje):
    def __init__(self,screen: pygame.Surface, nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas, posicionX, posicionY, raza):
        super().__init__(screen,nombre, descripcion, imagen, estadisticasBase,
                         habilidadesActivas, habilidadesPasivas, posicionX, posicionY)
        self.flip = False
        self.direction = 1

        self.raza = raza

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

    def move(self, event,assignedKeys):
        # *Area de controles
        movimiento_izquierda = False
        movimiento_derecha = False
        movimiento_arriba = False
        movimiento_abajo = False
        movement_speed = super().getCellSize()
        listaKeys=[[pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s],
                   [ pygame.K_g, pygame.K_j, pygame.K_y, pygame.K_h],
                   [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN],
                   [pygame.K_KP_4, pygame.K_KP_6, pygame.K_KP_8, pygame.K_KP_5]]
        if event.type == pygame.KEYDOWN:
            
            if event.key == listaKeys[assignedKeys][0]:
                movimiento_izquierda = True
                self.posicionX -= movement_speed
            if event.key ==  listaKeys[assignedKeys][1]:
                movimiento_derecha = True
                self.posicionX += movement_speed
            if event.key ==  listaKeys[assignedKeys][2]:
                movimiento_arriba = True
                self.posicionY -= movement_speed
            if event.key ==  listaKeys[assignedKeys][3]:
                movimiento_abajo = True
                self.posicionY += movement_speed
            if event.key == pygame.K_i:  # Inventario
                self.toggleInventory()
            if event.key == pygame.K_m:  # Mapa
                self.toggleMap()
            if event.key == pygame.K_ESCAPE:  # Opciones
                self.toggleSetting()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movimiento_izquierda = False
            if event.key == pygame.K_d:
                movimiento_derecha = False
            if event.key == pygame.K_w:
                movimiento_arriba = False
            if event.key == pygame.K_s:
                movimiento_abajo = False

        # * Area de movimientos
        direction_x = 0
        direction_y = 0
     

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
    
    # * Interfaz de usuario

    def toggleGUI(self):
        self._interface_active = self.toggleBoolean(self._interface_active)
        self._pause = self.toggleBoolean(self._pause)

    def toggleInventory(self):
        self.toggleGUI()
        self._inventory_active = self.toggleBoolean(self._inventory_active)

    def toggleMap(self):
        self.toggleGUI()
        self._map_active = self.toggleBoolean(self._map_active)

    def toggleSetting(self):
        self.toggleGUI()
        self._setting_active = self.toggleBoolean(self._setting_active)

    def draw(self, screen):
        screen.blit(pygame.transform.flip(
            self.player_texture, self.flip, False), self.rect)
        self.drawGUI(screen, self._interface_active)

    # Dibuja la interfaz de usuario
    def drawGUI(self, screen, interface_active):
        if interface_active == True:
            rectangle = pygame.Rect(50, 50, 50, 50)
            pygame.draw.rect(screen, (255, 255, 255), rectangle)
        else:
            self.drawInventory(screen)
            self.drawMap(screen)
            self.drawSetting(screen)

    # Dibuja el inventario
    def drawInventory(self, screen):
        if self._inventory_active:
            screen.blit(self.inventory_bag_texture, (288, 16))
            screen.blit(self.inventory_equipment_panel_texture, (16, 16))
            screen.blit(self.inventory_equipment_area_texture, (32, 96))
            screen.blit(self.inventory_button_texture, (24, 28))
            screen.blit(self.inventory_button_texture, (144, 28))

            # *Slots
            self.drawSlots(screen, 320, 106, 12, 14, 3, 0, 0, 3)
            # * Text
            self.drawText(screen, 'Inventario', 64, 432, 21)
            self.drawText(screen, 'Equipamiento', 24, 36, 38)
            self.drawText(screen, 'Estadísticas', 24, 156, 38)

    def drawMap(self, screen):
        if self._map_active:
            rectangle = pygame.Rect(32, 32, 50, 50)
            pygame.draw.rect(screen, (0, 0, 255), rectangle)

    def drawSetting(self, screen):
        if self._setting_active:
            rectangle = pygame.Rect(32, 32, 50, 50)
            pygame.draw.rect(screen, (255, 0, 255), rectangle)

    def drawSlots(self, screen, positionX, posicionY, amount_x, amount_y, margin_top=0, margin_right=0, margin_bottom=0, margin_left=0, apply_initial_margin_X=False, apply_initial_margin_Y=False):
        position_x = positionX  # eje x
        position_y = posicionY  # eje y
        slot_texture = pygame.image.load(
            "./assets/gui/inventory/Inventory_slot.png")

        for row in range(amount_y):
            if (row > 0 or apply_initial_margin_Y):
                position_y = position_y + margin_top
            for column in range(amount_x):
                if (column > 0 or apply_initial_margin_X):
                    position_x = position_x + margin_left
                screen.blit(slot_texture, (position_x, position_y))
                position_x = position_x + super().getCellSize() + margin_right  # aumenta x +32

            position_y = position_y + super().getCellSize() + margin_bottom  # aumenta y+32
            position_x = positionX  # resets x

    def drawText(self, screen, text, size, positionX=0, posicionY=0):
        myFont = pygame.font.Font(SILVER_MEDIUM_FONT, size)
        text_gui = myFont.render(text, 1, WHITE)
        screen.blit(text_gui, (positionX, posicionY))
