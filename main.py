import pygame
from sys import exit
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix

# Inicio el programa
pygame.init()

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
MAX_FPS = 60
#FPS 60/5 = 12
MAX_MOVEMENT_FPS = MAX_FPS/5
BLANCO = (255, 255, 255)

# definiendo el tamaño de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Titulo de la pantalla
pygame.display.set_caption("Tower of the Grindhard")

# Variables
data_time = 0  # Se usa para los movimiento de físicas
scene_level = 'level00' 

#Textura de jugador
player_texture = pygame.image.load("assets/player/base/elf_male.png")

#Variable de acción del personaje
movimiento_derecha = False
movimiento_izquierda = False
movimiento_arriba = False
movimiento_abajo = False

player = Jugador("player1","none",player_texture,None,None,None,3,19,"Humano")

collide_level1 = get_collider_matrix(scene_level)

# defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

def drawMap(level):
    level_texture = pygame.image.load(f'scene/{level}/_composite.png')
    screen.blit(level_texture, (0, 0))

def drawCollider(map_collider_matriz):
    eje_x = 0  # eje x
    eje_y = 0  # eje y

    for row in map_collider_matriz:
        for column in row:

            if (column == '1'):  # Muro
                pygame.draw.rect(screen, BLANCO, (eje_x, eje_y, 32, 32))
            if (column == '2'):  # La puerta
                pygame.draw.rect(screen, (126, 126, 0), (eje_x, eje_y, 32, 32))
            if (column == '3'):  # Cofres
                pygame.draw.rect(screen, (0, 126, 0), (eje_x, eje_y, 32, 32))
            if (column == '4'):  # Muebles
                pygame.draw.rect(screen, (0, 126, 126), (eje_x, eje_y, 32, 32))

            eje_x = eje_x + CELL_SIZE  # aumenta x +32

        eje_y = eje_y + CELL_SIZE  # aumenta y+32
        eje_x = 0  # resets x

player_update_time = 0

while True:
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a :
                movimiento_izquierda = True
            if event.key == pygame.K_d :
                movimiento_derecha = True
            if event.key == pygame.K_w :
                movimiento_arriba = True
            if event.key == pygame.K_s :
                movimiento_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a :
                movimiento_izquierda = False
            if event.key == pygame.K_d :
                movimiento_derecha = False
            if event.key == pygame.K_w :
                movimiento_arriba = False
            if event.key == pygame.K_s :
                movimiento_abajo = False

    # RENDER GAME HERE

    # ACTUALIZACIÓN DEL MOVIMIENTO DEL JUGADOR A 5 FPS
    if player_update_time >= MAX_MOVEMENT_FPS:
        player.move(movimiento_izquierda, movimiento_derecha, movimiento_abajo,movimiento_arriba)
        player_update_time = 0  # reinicio el temporizador

    #dibujo el mapa
    drawMap(scene_level)

    #dibujo las colisiones en el mapa a partir de una matriz
    drawCollider(collide_level1)
    
    # Dibujo al jugador
    player.draw(screen)

    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    # incremento el temporizador
    player_update_time += 1
    pygame.display.update()
