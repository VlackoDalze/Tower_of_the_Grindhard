import pygame
from sys import exit
import setting
import numpy as np
import csv

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

collide_level1 = []

with open('collisions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # Almaceno la matriz
    for line in csv_reader:
        collide_level1.append(line)

# defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))
#color negro
NEGRO = (0, 0, 0)

#ejes de jugador
jugador_ejex = 32*2
jugador_ejey = 32*19

#lista de colisiones
colisiones = []
eje_x = 0  # eje x
eje_y = 0  # eje y
for row in collide_level1:
    for column in row:

        if column=="1" or column=="2" or column=="3" or column=="4" :
            colisiones.append(str(eje_x)+"-"+str(eje_y))
           
        eje_x = eje_x + CELL_SIZE  # aumenta x +32
    eje_y = eje_y + CELL_SIZE  # aumenta y+32
    eje_x = 0  # resets x
    
while True:
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    ejex= jugador_ejex
    ejey=jugador_ejey
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ejex = ejex-CELL_SIZE
            if event.key ==pygame.K_RIGHT:
                ejex =ejex+CELL_SIZE
            if event.key==pygame.K_UP:
                ejey = ejey-CELL_SIZE
            if event.key== pygame.K_DOWN:
                ejey = ejey+CELL_SIZE
            print(ejex,ejey)  
     
        if str(ejex)+"-"+str(ejey) not in colisiones:  
            jugador_ejex = ejex
            jugador_ejey = ejey
            
    # Lleno la pantalla con el color para borrar cualquier cosa del último cuadro
    screen.fill(BLANCO)

    # RENDER GAME HERE
    # Dibujo el mapa
    # Itera sobre el mapa y dibuja cada textura
    # for y in range(MAP_HEIGHT):
    #     for x in range(MAP_WIDTH):
    #         # Calcula la posición en píxeles de la textura en el mapa
    #         texture_x = x * CELL_SIZE
    #         texture_y = y * CELL_SIZE

    #         # Dibuja la imagen de la textura en la posición correspondiente
    #         if map_data[y][x] == 0:
    #             screen.blit(floor_texture, (texture_x, texture_y))
    #         elif map_data[y][x] == 1:
    #             screen.blit(wall_texture, (texture_x, texture_y))

    # Dibuja la imagen en la pantalla
    # screen.blit(image, (x * CELL_SIZE, y * CELL_SIZE))
    # pygame.draw.circle(screen, BLANCO, (64,64), 8)

    screen.blit(level1_texture, (0, 0))
    pygame.draw.rect(screen, NEGRO, (jugador_ejex, jugador_ejey, 32, 32))

    # Sistema de jugador
   
       

    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    pygame.display.update()
