import pygame
from sys import exit
import scripts.setting as setting
#from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix, get_animated_decorations_matrix
from scripts.torch import Torch
from scripts.players_views import Views, viewsPositions
from scripts.ui_fragment import *
from scripts.music import Music
from scripts.menu import Menu
#from scripts.shadows import Shadows
from scripts.triggers import Triggers
from scripts.shadowsv2 import Shadows2
from scripts.enemigo import Enemy
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

# * GUI
panel_texture = pygame.image.load(
    "assets/gui/inventory/sheet_of_old_paper.png")  # Textura de papel
button_texture = pygame.image.load("assets/gui/inventory/inventory_button.png")

panel_area = (500, 500)
position_percentage_values = ('35%', '10%')

button_position_values = ('90%', '60%')
button_area_values = (100, 40)

Gui_fragment_group = Ui_fragment(screen)

ui_frag = Ui_fragment(Gui_fragment_group.getScreen())
button_fragment_group = Ui_fragment(Gui_fragment_group.getScreen())

panel = Panel_fragment(ui_frag.getScreen(),
                       panel_texture, position_percentage_values, panel_area)
bigText = "Exerci sanctus amet. Diam at dolor <color(220,10,120)>dolor consectetuer</color> imperdiet. Tempor ea sanctus sit eum ipsum aliquyam erat erat <color(255,255,0)>sanctus</color> tincidunt lorem elitr. Ea sadipscing no accumsan tempor invidunt takimata invidunt eos option sed. Diam blandit dolor eirmod et ea eos rebum stet erat lorem et ipsum invidunt eos clita sanctus kasd labore. Takimata et lorem consequat. Iusto sit voluptua vel ut eros at volutpat odio clita magna clita elitr dolore. Diam erat elitr diam sadipscing et accusam. Elitr sit magna duis zzril et duo justo facilisis ut velit ipsum justo sit option clita et. Dolor diam diam dolor erat stet erat sed aliquyam quis. Dolore elitr te. Consetetur no tempor lorem erat gubergren doming assum elitr ut. Tempor aliquyam sea voluptua autem erat justo elit et exerci kasd diam. Dolores blandit sea elitr ut elitr aliquyam minim rebum esse. Liber clita nonummy placerat elit at. Magna praesent sed vel lorem eirmod ipsum ea zzril erat nulla est sed labore eos sed velit."
text_area = Text_area_fragment(
    ui_frag.getScreen(), bigText, 23, position_percentage_values, panel_area, (50, 30, 40, 0), (112, 66, 20))
ui_frag.add_fragment(panel, text_area)


button_fragment = Button_fragment(ui_frag.getScreen(
), button_texture, button_position_values, button_area_values)
width, height = button_fragment.get_image_size()
text_button = Text_area_fragment(button_fragment_group.getScreen(
), 'Close', 18, button_position_values, button_area_values, (width/3, height/3, 0, 0), WHITE)


button_fragment_group.add_fragment(button_fragment, text_button)


def testMethod():
    Ui_fragment.clear_fragments(Gui_fragment_group)


button_fragment.setOnClick(testMethod)

Gui_fragment_group.add_fragment(ui_frag, button_fragment_group)

# * User interface

inventory_bag_texture = pygame.image.load(
    'assets/gui/inventory/inventory_bag_panel.png')
inventory_btn_texture = pygame.image.load(
    'assets/gui/inventory/inventory_button.png')
inventory_equipment_panel_texture = pygame.image.load(
    'assets/gui/inventory/inventory_equipment_panel.png')
inventory_equipment_area_texture = pygame.image.load(
    'assets/gui/inventory/equipment_area.png')
inventory_slot = pygame.image.load(
    "./assets/gui/inventory/inventory_slot.png")

default_fragment = Ui_fragment(ui_frag.getScreen())
inventory_fragment = Ui_fragment(ui_frag.getScreen())
inventory_bag_fragment = Panel_fragment(ui_frag.getScreen(), inventory_bag_texture, (288, 16), inventory_bag_texture.get_size())
inventory_text_fragment = Text_area_fragment(ui_frag.getScreen(), 'Inventario', 42, (CELL_SIZE*14.5,-16.0),(0,0))
inventory_slot_fragment = Interactable_fragment(ui_frag.getScreen(), inventory_slot, (0,0))

inventory_equipment_panel_fragment_group = Ui_fragment(screen)
# inventory_equipment_fragment = Panel_fragment(ui_frag.getScreen(), inventory_equipment_panel_texture, ('10%','10%'),inventory_equipment_area_texture.get_size())

slots_groups_fragment = Ui_fragment.fragments_matrix_group_maker(inventory_slot_fragment, (CELL_SIZE*9,CELL_SIZE*3), (5,5),0,10,10,0)

inventory_fragment.add_fragment(inventory_bag_fragment,inventory_text_fragment,slots_groups_fragment)

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
enemy_list = []
# posicion del circulo cursor
memoryPositionCircle = 0
background_music = Music(setting.musics_url_list)

equipment_area_btn_frag_array = []



# desde aquí empieza el programa
while True:
    background_music.play_random_background_music()
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        # salir
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        button_fragment.setEventListener(event)
        # menu previo a las vistas
        if len(players_list) == 0:
            memoryPositionCircle = Menu(
                players_list, player_texture, screen, event, scene_level).setPlayers(memoryPositionCircle)
        for i in range(0, len(players_list)):    
            if(len(equipment_area_btn_frag_array) < len(players_list)):
                equipment_area_btn_frag_array.append(Button_fragment(screen, inventory_btn_texture, (0,0), (CELL_SIZE*3,CELL_SIZE)))
            equipment_area_btn_frag_array[i].setEventListener(event)

        else:  # vistas
            Triggers.setCountPlayers(len(players_list))
            # Cuando no está activo este fragment, se desactiva los movimientos del jugador
            for i in range(0, len(players_list)):
                # if event.type == pygame.KEYDOWN:
                if not (Gui_fragment_group.isActive()):
                    players_list[i].move(event, i)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:  # Inventario
                Ui_fragment.toggle_fragment(Gui_fragment_group, inventory_fragment)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:  # Mapa
                print('Mapa')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Opciones
                Ui_fragment.clear_fragments(Gui_fragment_group)

    #Cuando ya hay jugadores en la lista continua con los dibujados
    if len(players_list) > 0:  # primero debes definir el numero de jugadores
        if len(inventory_equipment_panel_fragment_group.get_fragment_list()) == 0:
            inventory_equipment_panel_fragment_group
            for i in range(len(players_list)):
                position_x = viewsPositions[i][0]
                position_y = viewsPositions[i][1]
                if ((i+1) % 2) == 0:
                    position_x *= 1.425
                position_x += 32
                position_y += 16
                inventory_equipment_panel_fragment = Panel_fragment(ui_frag.getScreen(), inventory_equipment_panel_texture, (str(position_x),str(position_y)))
                inventory_equipment_area_fragment = Panel_fragment(ui_frag.getScreen(), inventory_equipment_area_texture, (str(position_x+16),str(position_y+CELL_SIZE*3)))
                #TODO: hacer que el area de estadísticas se muestre cuando se presiona el botón correspondiente
                equipment_buttons = Ui_fragment(ui_frag.getScreen())
                def openEquipmentArea():
                    print('Equipment')
                def openStatisticsArea():
                    print('Statistics')
                equipment_area_btn_frag_array[i].setOnClick(openEquipmentArea)
                equipment_area_btn_frag_array[i].set_position((position_x+16,position_y+16))
                print(equipment_area_btn_frag_array[i].get_position())
                text_button = Text_area_fragment(equipment_area_btn_frag_array[i].getScreen(), 'Equipamiento', 20, (equipment_area_btn_frag_array[i].get_position().x+14,equipment_area_btn_frag_array[i].get_position().y+8))
                equipment_buttons.add_fragment(equipment_area_btn_frag_array[i],text_button)
                inventory_equipment_panel_fragment_group.add_fragment(inventory_equipment_panel_fragment,inventory_equipment_area_fragment,equipment_buttons)
            inventory_fragment.add_fragment(inventory_equipment_panel_fragment_group)


        # RENDER GAME HERE
        if furniture_animation_update_time >= MAX_FURNITURE_ANIMATION_FPS:
            current_sprite_anim += 1
            if current_sprite_anim >= Torch.get_torch_sprites_length():
                current_sprite_anim = 0
            furniture_animation_update_time = 0

        # dibujo el mapa
        drawMap(scene_level)

        # dibujo las colisiones en el mapa a partir de una matriz (Solo para pruebas)
        # drawCollider(collide_level1)

        # dibujo las antorchas en el mapa a partir de una matriz
        draw_list_torch(list_torch, current_sprite_anim)

        # Dibujo al jugador
        for player in players_list:
            player.draw()
            
        #dibujo de enemigos
        #esto se puede mejorar luego para no ocupar tanto espacio en el main
        enemy1=Enemy(screen,'Esqueleto',None,1,None,None,None,20*CELL_SIZE,18*CELL_SIZE,scene_level)
        enemy1.drawEnemy()
        if enemy1 not in enemy_list:
            enemy_list.append(enemy1)
            
        # dibujo sombras
        #Shadows.drawShadows(screen, players_list,scene_level)
        Shadows2.drawShadows2(players_list,list_torch)
        #draw triggers deben hacer antes de las vistas
        Triggers.drawListTriggersActive(screen)
        #triggers de enemigos
        Triggers.drawEnemyTriggersActive(screen,players_list,enemy_list)


        # Dibujar vistas
        drawViews(players_list, screen)

        # * Interfaz de usuario
        Gui_fragment_group.drawListFragments()

    pygame.display.flip()  # actualizar los cambios
    #  pygame.display.flip() la pantalla para poner su trabajo en la pantalla ->actualiza toda la pantalla, es lo mismo que update()
    clock.tick(MAX_FPS)  # limito el FPS a 60

    # incremento el temporizador
    player_update_time += 1
    furniture_animation_update_time += 1
