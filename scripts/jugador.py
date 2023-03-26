from scripts.personaje import Personaje as Personaje
import pygame


class Jugador(Personaje):
    def __init__(self, nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas, posicionX, posicionY, raza):
        super().__init__(nombre, descripcion, imagen, estadisticasBase,
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

    def move(self, event):
        # *Area de controles
        movimiento_izquierda = False
        movimiento_derecha = False
        movimiento_arriba = False
        movimiento_abajo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movimiento_izquierda = True
            if event.key == pygame.K_d:
                movimiento_derecha = True
            if event.key == pygame.K_w:
                movimiento_arriba = True
            if event.key == pygame.K_s:
                movimiento_abajo = True
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
        movement_speed = super().getCellSize()

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

        #self.drawGUI(screen, self._interface_active)

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
            self.drawSlots(screen, 50, 50, 5, 0, 0, 5)

    def drawMap(self, screen):
        if self._map_active:
            rectangle = pygame.Rect(32, 32, 50, 50)
            pygame.draw.rect(screen, (0, 0, 255), rectangle)

    def drawSetting(self, screen):
        if self._setting_active:
            rectangle = pygame.Rect(32, 32, 50, 50)
            pygame.draw.rect(screen, (255, 0, 255), rectangle)

    def drawSlots(self, screen, positionX, posicionY, margin_top=0, margin_right=0, margin_bottom=0, margin_left=0, apply_initial_margin_X=False, apply_initial_margin_Y=False):
        position_x = positionX  # eje x
        position_y = posicionY  # eje y
        slot_texture = pygame.image.load("./assets/gui/abilities/dig.png")

        for row in range(4):
            if (row > 0 or apply_initial_margin_Y):
                position_y = position_y + margin_top
            for column in range(2):
                if (column > 0 or apply_initial_margin_X):
                    position_x = position_x + margin_left
                screen.blit(slot_texture, (position_x, position_y))
                position_x = position_x + super().getCellSize() + margin_right  # aumenta x +32

            position_y = position_y + super().getCellSize() + margin_bottom  # aumenta y+32
            position_x = positionX  # resets x
