import pygame
from sys import exit
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix, get_animated_decorations_matrix
from scripts.torch import Torch
from scripts.players_views import Views

# Inicio el programa
pygame.init()

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

# Variables
data_time = 0  # Se usa para los movimiento de físicas
scene_level = 'level00'

# Textura de jugador
player_texture = pygame.image.load("assets/player/base/elf_male.png")
players_list = []
player1 = Jugador("player1", "none", player_texture,
                 None, None, None, 3, 19, "Humano")
player2 = Jugador("player2", "none", player_texture,
                 None, None, None, 3, 19, "Humano")
player3 = Jugador("player1", "none", player_texture,
                 None, None, None, 3, 19, "Humano")
player4 = Jugador("player2", "none", player_texture,
                 None, None, None, 3, 19, "Humano")
players_list.append(player1)
players_list.append(player2)
players_list.append(player3)
players_list.append(player4)


collide_level1 = get_collider_matrix(scene_level)
animated_decorations_matrix = get_animated_decorations_matrix(scene_level)

def drawMap(level):
    level_texture = pygame.image.load(f'scene/{level}/_composite.png')
    screen.blit(level_texture, (0, 0))
   
def drawViews(players,screen):
    createViews=Views(players,screen) 
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


def get_animated_decoration_array(map_animated_decorations_matrix):
    eje_x = 0  # eje x
    eje_y = 0  # eje y
    list_animated_decoration = []

    for row in map_animated_decorations_matrix:
        for column in row:

            # almaceno en la lista de objetos si se encuentra el valor 1
            if (column == '1'):  # Antorcha
                torch = Torch(eje_x, eje_y)
                list_animated_decoration.append(torch)

            eje_x += 1  # aumenta x +1 (x*32)

        eje_y += 1  # aumenta y+1 (y * 32)
        eje_x = 0  # resets x
    return list_animated_decoration

# recorro la lista de objetos del mapa que tengan animación y dibujo el objeto en el mapa


def draw_list_torch(screen, list_torch, current_sprite_anim):
    for torch in list_torch:
        if isinstance(torch, Torch):
            torch.drawTorch(screen, current_sprite_anim)


# obtengo la lista de objetos del mapa que tengan animación y la guardo en la variable list_torch
list_torch = get_animated_decoration_array(animated_decorations_matrix)

# Estados de animación para la antorcha
current_sprite_anim = 0

player_update_time = 0
furniture_animation_update_time = 0

while True:
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player1.move(event)

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
    draw_list_torch(screen, list_torch, current_sprite_anim)

    # Dibujo al jugador
    player1.draw(screen)

    # Dibujar vistas
    drawViews(players_list,screen)  
    
    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    # incremento el temporizador
    player_update_time += 1
    furniture_animation_update_time += 1
    pygame.display.update()
