import pygame
from sys import exit
import setting
import numpy as np
import csv
from jugador import Jugador

# Inicio el programa
pygame.init()

# Variables statics
CELL_SIZE = setting.CELL_SIZE
MAP_WIDTH = setting.SCREEN_WIDTH // CELL_SIZE
MAP_HEIGHT = setting.SCREEN_HEIGHT // CELL_SIZE
MAX_FPS = 60
BLANCO = (255, 255, 255)

# definiendo el tamaño de la pantalla
screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Titulo de la pantalla
pygame.display.set_caption("Tower of the Grindhard")

# Variables
data_time = 0  # Se usa para los movimiento de físicas
map_data = np.random.randint(0, 2, size=(MAP_HEIGHT, MAP_WIDTH))

# Texturas
floor_texture = pygame.image.load("assets/dungeon/floor/sandstone_floor_0.png")
wall_texture = pygame.image.load("assets/dungeon/wall/brick_brown_0.png")
level1_texture = pygame.image.load("_composite.png")

#Textura de jugador
player_texture = pygame.image.load("assets/player/base/elf_male.png")

#Variable de acción del personaje
movimiento_derecha = False;
movimiento_izquierda = False;
movimiento_arriba = False;
movimiento_abajo = False;


player = Jugador("player1","none",player_texture,None,None,None,3,19,"Humano")

collide_level1 = []

with open('collisions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # Almaceno la matriz
    for line in csv_reader:
        collide_level1.append(line)

# defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

def drawMap(level_texture):
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

    player.move(movimiento_izquierda, movimiento_derecha, movimiento_abajo,movimiento_arriba)

    # RENDER GAME HERE

    drawMap(level1_texture)
    drawCollider(collide_level1)
    
    # Dibujo al jugador
    player.draw(screen)

    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    pygame.display.update()
