import pygame
from sys import exit
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix, get_animated_decorations_matrix
from scripts.torch import Torch
from scripts.players_views import Views
from scripts.ui_fragment import UI_fragment
from scripts.music import Music
from scripts.menu import Menu
from scripts.shadows import Shadows

# Inicio el programa
pygame.init()
pygame.mixer.init()

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
MAX_FPS = setting.MAX_FPS

# FPS 60/5 = 12
MAX_MOVEMENT_FPS = MAX_FPS/5
MAX_FURNITURE_ANIMATION_FPS = MAX_FPS/4
WHITE = (255, 255, 255)

# definiendo el tamaño de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Titulo de la pantalla
pygame.display.set_caption("Tower of the Grindhard")

# * Variables
data_time = 0  # Se usa para los movimiento de físicas
scene_level = 'level00'
player_texture = pygame.image.load(
    "assets/player/base/elf_male.png")  # Textura de jugador
ui_frag = UI_fragment(screen, player_texture, (0, 0))

# collide_level1 = get_collider_matrix(scene_level)
animated_decorations_matrix = get_animated_decorations_matrix(scene_level)


def drawMap(level):
    level_texture = pygame.image.load(f'scene/{level}/_composite.png')
    screen.blit(level_texture, (0, 0))


def drawViews(players, screen):
    createViews = Views(players, screen)
    createViews.playerView()


def drawCollider(map_collider_matriz):
    eje_x = 0  # eje x
    eje_y = 0  # eje y

    for row in map_collider_matriz:
        for column in row:

            if (column == '1'):  # Muro
                pygame.draw.rect(screen, WHITE, (eje_x, eje_y, 32, 32))
            if (column == '2'):  # La puerta
                pygame.draw.rect(screen, (126, 126, 0), (eje_x, eje_y, 32, 32))
            if (column == '3'):  # Cofres
                pygame.draw.rect(screen, (0, 126, 0), (eje_x, eje_y, 32, 32))
            if (column == '4'):  # Muebles
                pygame.draw.rect(screen, (0, 126, 126), (eje_x, eje_y, 32, 32))

            eje_x = eje_x + CELL_SIZE  # aumenta x +32

        eje_y = eje_y + CELL_SIZE  # aumenta y+32
        eje_x = 0  # resets x


def get_animated_decoration_array(screen, map_animated_decorations_matrix):
    eje_x = 0  # eje x
    eje_y = 0  # eje y
    list_animated_decoration = []

    for row in map_animated_decorations_matrix:
        for column in row:

            # almaceno en la lista de objetos si se encuentra el valor 1
            if (column == '1'):  # Antorcha
                torch = Torch(screen, eje_x, eje_y)
                list_animated_decoration.append(torch)

            eje_x += 1  # aumenta x +1 (x*32)

        eje_y += 1  # aumenta y+1 (y * 32)
        eje_x = 0  # resets x
    return list_animated_decoration

# recorro la lista de objetos del mapa que tengan animación y dibujo el objeto en el mapa


def draw_list_torch(list_torch, current_sprite_anim):
    for torch in list_torch:
        if isinstance(torch, Torch):
            torch.drawTorch(current_sprite_anim)


# obtengo la lista de objetos del mapa que tengan animación y la guardo en la variable list_torch
list_torch = get_animated_decoration_array(screen, animated_decorations_matrix)

# Estados de animación para la antorcha
current_sprite_anim = 0
player_update_time = 0
furniture_animation_update_time = 0

# memoria de sombras
list_shadows = []
# lista jugadores
players_list = []
# posicion del circulo cursor
memoryPositionCircle = 0

background_music = Music(setting.musics_url_list)

# desde aquí empieza el programa
while True:
    background_music.play_random_background_music()
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        # salir
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # menu previo a las vistas
        if len(players_list) == 0:
            memoryPositionCircle = Menu(
                players_list, player_texture, screen, event).setPlayers(memoryPositionCircle)
        else:  # vistas
            for i in range(len(players_list)):
                players_list[i].move(event, i)

    if len(players_list) > 0:  # primero debes definir el numero de jugadores

        # RENDER GAME HERE
        if furniture_animation_update_time >= MAX_FURNITURE_ANIMATION_FPS:
            current_sprite_anim += 1
            if current_sprite_anim >= Torch.get_torch_sprites_length():
                current_sprite_anim = 0
            furniture_animation_update_time = 0

        # dibujo el mapa
        drawMap(scene_level)

        # dibujo las colisiones en el mapa a partir de una matriz
        # drawCollider(collide_level1)

        # dibujo las antorchas en el mapa a partir de una matriz
        draw_list_torch(list_torch, current_sprite_anim)

        # Dibujo al jugador
        for player in players_list:
            player.draw()

        # dibujo sombras
        Shadows.drawShadows(screen, players_list)

        # Dibujar vistas
        drawViews(players_list, screen)

        ui_frag.draw()

        for player in players_list:
            player.drawGUI()

    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    # incremento el temporizador
    player_update_time += 1
    furniture_animation_update_time += 1

    pygame.display.update()
