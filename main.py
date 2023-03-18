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

while True:
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:


    # flip() la pantalla para poner su trabajo en la pantalla
    pygame.display.flip()
    data_time = clock.tick(MAX_FPS)  # limito el FPS a 60
    pygame.display.update()
