import pygame
from sys import exit
import scripts.setting as setting

from scripts.collider_matrix_maker import (
    get_collider_matrix,
    get_animated_decorations_matrix,
)
from scripts.torch import Torch
from scripts.players_views import Views
from scripts.ui_fragment import *
from scripts.music import Music
from scripts.menu import Menu

# from scripts.shadows import Shadows
from scripts.triggers import Triggers
from scripts.shadowsv2 import Shadows2
from scripts.enemy import Enemy
from scripts.gui import Gui_drawer

from scripts.object import PrimaryWeapon
import scripts.texture_pack as texture_pack
from scripts.statistics import Statistics
from scripts.player import Player
from scripts.interfaceSelectRace import SelectRaces
# Inicio el programa
pygame.init()
pygame.mixer.init()

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
MAX_FPS = setting.MAX_FPS

# FPS 60/5 = 12
MAX_MOVEMENT_FPS = MAX_FPS / 5
MAX_FURNITURE_ANIMATION_FPS = MAX_FPS / 4
WHITE = (255, 255, 255)

# definiendo el tamaño de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Titulo de la pantalla
pygame.display.set_caption("Tower of the Grindhard")
pygame.display.set_icon(
    pygame.image.load("assets/gui/app_image/tower_of_the_grindhard_icon.png")
)

# * Variables
data_time = 0  # Se usa para los movimiento de físicas
scene_level = "level00"
player_texture = pygame.image.load(
    "assets/player/base/elf_male.png"
)  # Textura de jugador


# collide_level1 = get_collider_matrix(scene_level)
animated_decorations_matrix = get_animated_decorations_matrix(scene_level)


def drawMap(level):
    level_texture = pygame.image.load(f"scene/{level}/_composite.png")
    screen.blit(level_texture, (0, 0))


def drawViews(players, screen):
    createViews = Views(players, screen)
    createViews.playerView()


def drawCollider(map_collider_matriz):
    eje_x = 0  # eje x
    eje_y = 0  # eje y
    for row in map_collider_matriz:
        for column in row:
            if column == "1":  # Muro
                pygame.draw.rect(screen, WHITE, (eje_x, eje_y, 32, 32))
            if column == "2":  # La puerta
                pygame.draw.rect(screen, (126, 126, 0), (eje_x, eje_y, 32, 32))
            if column == "3":  # Cofres
                pygame.draw.rect(screen, (0, 126, 0), (eje_x, eje_y, 32, 32))
            if column == "4":  # Muebles
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
            if column == "1":  # Antorcha
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
enemy_list = []
# posicion del circulo cursor
memoryPositionCircle = 0
background_music = Music(setting.musics_url_list)

equipment_area_btn_frag_array = []

gui_drawer = Gui_drawer(screen)
gui_drawer.createGUI()

select_ok=False

legendary_sword = PrimaryWeapon(
    texture_pack.rare_primary_weapon_warrior_texture,
    "Legend Sword",
    "A sharp, deadly blade",
    Statistics(300,900,156,489,156,489,156),
)

# desde aquí empieza el programa
while True:
    background_music.play_random_background_music()
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        # salir
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #*EventListeners
        gui_drawer.setEventListener(event)
        if len(players_list) > 0:
            gui_drawer.setEventToArrayBtn(event)

        # menu previo a las vistas
        if len(players_list) == 0:
            
            memoryPositionCircle = Menu(
                players_list, player_texture, screen, event, scene_level
            ).setPlayers(memoryPositionCircle)
            
            numPlayers = len(players_list)
            
            if numPlayers > 0:
                gui_drawer.createGUI_array(numPlayers)
        #menu de seleccion de raza y roles   
        elif not select_ok:
            select_ok=SelectRaces.startSelection(players_list,screen,event)
                
        else:  # vistas
            Triggers.setCountPlayers(len(players_list))
            # Cuando no está activo este fragment, se desactiva los movimientos del jugador
            for i in range(0, len(players_list)):
                if not gui_drawer.isActiveInventory():
                    players_list[i].move(event, i)
                elif gui_drawer.isActiveInventory():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        Player.nextInventoryIndex()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        Player.prevInventoryIndex()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:  # Inventario
                gui_drawer.showInventory()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:  # Mapa
                gui_drawer.hello()
                players_list[0].equip(legendary_sword)
                Player.removeFromInventory(legendary_sword)
            if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):  # Opciones
                gui_drawer.hello()
                Player.addToInventory(legendary_sword)

    # Cuando ya hay jugadores en la lista continua con los dibujados
    if len(players_list) > 0 and select_ok:  # primero debes definir el numero de jugadores
        # RENDER GAME HERE
        if furniture_animation_update_time >= MAX_FURNITURE_ANIMATION_FPS:
            current_sprite_anim += 1
            if current_sprite_anim >= Torch.get_torch_sprites_length():
                current_sprite_anim = 0
            furniture_animation_update_time = 0

        # dibujo el mapa según el nombre de la escena(nivel de piso)
        drawMap(scene_level)

        # dibujo las colisiones en el mapa a partir de una matriz (Solo para pruebas)
        # drawCollider(collide_level1)
    
        # dibujo las antorchas en el mapa a partir de una matriz
        draw_list_torch(list_torch, current_sprite_anim)

        #Actualizar la interfaz de usuario
        if gui_drawer.isActiveInventory():
            gui_drawer.updateEquipmentPanel(players_list)
            if furniture_animation_update_time >= 9:
                gui_drawer.updateInventoryContents(Player.getInventory())
            gui_drawer.setInventorySlotEventListener(event)

        # Dibujo al jugador
        for player in players_list:
            player.draw()

        # dibujo de enemigos
        # TODO: Mejorar luego para no ocupar tanto espacio en el main
        enemy1 = Enemy(
            screen,
            "Esqueleto",
            None,
            1,
            None,
            None,
            None,
            20 * CELL_SIZE,
            18 * CELL_SIZE,
            scene_level,
        )
        enemy1.drawEnemy()
        if enemy1 not in enemy_list:
            enemy_list.append(enemy1)

        # dibujo sombras
        Shadows2.drawShadows2(players_list, list_torch)
        # draw triggers deben hacer antes de las vistas
        Triggers.drawListTriggersActive(screen)
        # triggers de enemigos
        Triggers.drawEnemyTriggersActive(screen, players_list, enemy_list)

        # Dibujar vistas
        drawViews(players_list, screen)

        # Interfaz de usuario
        gui_drawer.draw_GUI()

    pygame.display.flip()  # actualizar los cambios
    #  pygame.display.flip() la pantalla para poner su trabajo en la pantalla ->actualiza toda la pantalla, es lo mismo que update()
    clock.tick(MAX_FPS)  # limito el FPS a 60

    # incremento el temporizador
    player_update_time += 1
    furniture_animation_update_time += 1
