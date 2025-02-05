import pygame
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.ui_fragment import Ui_fragment

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT

# intro de juego
intro_setPlayers = ["Bienvendo a ", "Tower of the Grindhard", "desea empezar esta aventura",
                    "sólo o acompañado?", "1 jugador", "2 jugadores", "3 jugadores", "4 jugadores"]

letter_style = "assets/font/Silver.ttf"
# *Pointer texture
pointer_texture = pygame.image.load('./assets/gui/pointer.png')
# Definir el color que deseas multiplicar
pointer_color = (245, 230, 100)


class Menu(object):
    pointer_texture = Ui_fragment.getMultiplyColorTexture(
        pointer_texture, pointer_color)

    def __init__(self, players_list, player_texture, screen, event,scene_level):
        self.players_list = players_list
        self.player_texture = player_texture
        self.screen = screen
        self.event = event
        self.scene_level=scene_level
        
    def playersInGame(self, num_players):
        
        for i in range(num_players):
            player = Jugador(self.screen, "player"+str(i+1), "none",
                             self.player_texture, None, None, None, 3, 19, "Humano",self.scene_level)
            self.players_list.append(player)

    def setPlayers(self, memoryPositionCircle):
        # fondo del menu necesario para se reinicie las textura de sobras
        self.screen.fill((0, 0, 0))

        letter_size = 15  # ancho de cada letra en px
        # centrar texto linea horizontal esta relacionado al tamaño de la letra importada
        width_center = SCREEN_WIDTH/4
        # centrar texto linea vertical esta relacionado al tamaño de la letra importada
        height_center = SCREEN_HEIGHT/4
        # tamaño de linea centrada en px
        line_size = (len(intro_setPlayers[0]) +
                     len(intro_setPlayers[1]))*letter_size
        # guarda la posicion del circulo o puntero de seleccion
        circle_y = memoryPositionCircle
        # letra importada desde font
        textoFont = pygame.font.Font(letter_style, 50)
        # esto es para mover 3 celdas el menu de opciones, en otras palabras centrarlo
        center_menu = 3

        text1 = textoFont.render(intro_setPlayers[0], 1, (255, 255, 255))
        text2 = textoFont.render(intro_setPlayers[1], 1, (255, 0, 0))
        text3 = textoFont.render(intro_setPlayers[2], 1, (255, 255, 255))
        text4 = textoFont.render(intro_setPlayers[3], 1, (255, 255, 255))
        text5 = textoFont.render(intro_setPlayers[4], 1, (255, 255, 255))
        text6 = textoFont.render(intro_setPlayers[5], 1, (255, 255, 255))
        text7 = textoFont.render(intro_setPlayers[6], 1, (255, 255, 255))
        text8 = textoFont.render(intro_setPlayers[7], 1, (255, 255, 255))

        self.screen.blit(text1, (width_center, height_center))
        self.screen.blit(
            text2, (width_center+len(intro_setPlayers[0])*(letter_size), height_center))
        self.screen.blit(text3, (width_center+(line_size -
                                               len(intro_setPlayers[2])*letter_size)/2, height_center+CELL_SIZE))
        self.screen.blit(text4, (width_center+(line_size -
                                               len(intro_setPlayers[3])*letter_size)/2, height_center+CELL_SIZE*2))

        self.screen.blit(text5, (width_center+CELL_SIZE*1.5 *
                                 center_menu, height_center+CELL_SIZE*5))
        self.screen.blit(text6, (width_center+CELL_SIZE*1.5 *
                                 center_menu, height_center+CELL_SIZE*6))
        self.screen.blit(text7, (width_center+CELL_SIZE*1.5 *
                                 center_menu, height_center+CELL_SIZE*7))
        self.screen.blit(text8, (width_center+CELL_SIZE*1.5 *
                                 center_menu, height_center+CELL_SIZE*8))

        aux_circle_y = circle_y  # auxiliar para limites del eje y

        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_UP:
                aux_circle_y -= CELL_SIZE
            if self.event.key == pygame.K_DOWN:
                aux_circle_y += CELL_SIZE
            if self.event.key == pygame.K_KP_ENTER or self.event.key == pygame.K_RETURN:  # crea a los jugadores
                if circle_y == 0:
                    self.playersInGame(1)
                elif circle_y == CELL_SIZE:
                    self.playersInGame(2)
                elif circle_y == CELL_SIZE*2:
                    self.playersInGame(3)
                else:
                    self.playersInGame(4)
        # mueve el circulo
        if aux_circle_y >= 0 and aux_circle_y <= CELL_SIZE*3:
            circle_y = aux_circle_y

        self.screen.blit(pointer_texture, (width_center+CELL_SIZE *
                         center_menu, height_center+CELL_SIZE*5+center_menu+circle_y))

        return circle_y  # retornas posicion del circulo o puntero de seleccion
