import pygame
from sys import exit
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix, get_animated_decorations_matrix
from scripts.torch import Torch
from scripts.players_views import Views
from scripts.ui_fragment import UI_fragment
from scripts.music import Music


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
players_list = []  # lista jugadores
ui_frag = UI_fragment(screen, player_texture, (0, 0))

#*Pointer texture
pointer_texture = pygame.image.load('./assets/gui/pointer.png')
pointer_color = (245, 230, 100) # Definir el color que deseas multiplicar 
pointer_texture_rect = ui_frag.getMultiplyColorTexture(pointer_texture, pointer_color)

# intro de juego
intro_setPlayers = ["Bienvendo a ", "Tower of the Grindhard", "desea empezar esta aventura",
                    "sólo o acompañado?", "1 jugador", "2 jugadores", "3 jugadores", "4 jugadores"]
memoryPositionCircle = 0
letter_style = setting.SILVER_MEDIUM_FONT

def playersInGame(num_players):
    for i in range(num_players):
        player = Jugador(screen, "player"+str(i+1), "none",
                         player_texture, None, None, None, 3, 19, "Humano")
        players_list.append(player)

def setPlayers(event, screen: pygame.Surface):
    #fondo del menu necesario para se reinicie las textura de sobras
    screen.fill((0,0,0))

    letter_size = 15  # ancho de cada letra en px
    # centrar texto linea horizontal esta relacionado al tamaño de la letra importada
    width_center = SCREEN_WIDTH/4
    # centrar texto linea vertical esta relacionado al tamaño de la letra importada
    height_center = SCREEN_HEIGHT/4
    # tamaño de linea centrada en px
    line_size = (len(intro_setPlayers[0])+len(intro_setPlayers[1]))*letter_size
    # guarda la posicion del circulo o puntero de selección
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

    screen.blit(text1, (width_center, height_center))
    screen.blit(
        text2, (width_center+len(intro_setPlayers[0])*(letter_size), height_center))
    screen.blit(text3, (width_center+(line_size -
                len(intro_setPlayers[2])*letter_size)/2, height_center+CELL_SIZE))
    screen.blit(text4, (width_center+(line_size -
                len(intro_setPlayers[3])*letter_size)/2, height_center+CELL_SIZE*2))

    screen.blit(text5, (width_center+CELL_SIZE*1.5 *
                center_menu, height_center+CELL_SIZE*5))
    screen.blit(text6, (width_center+CELL_SIZE*1.5 *
                center_menu, height_center+CELL_SIZE*6))
    screen.blit(text7, (width_center+CELL_SIZE*1.5 *
                center_menu, height_center+CELL_SIZE*7))
    screen.blit(text8, (width_center+CELL_SIZE*1.5 *
                center_menu, height_center+CELL_SIZE*8))

    aux_circle_y = circle_y  # auxiliar para limites del eje y

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            aux_circle_y -= CELL_SIZE
        if event.key == pygame.K_DOWN:
            aux_circle_y += CELL_SIZE
        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:  # crea a los jugadores
            if circle_y == 0:
                playersInGame(1)
            elif circle_y == CELL_SIZE:
                playersInGame(2)
            elif circle_y == CELL_SIZE*2:
                playersInGame(3)
            else:
                playersInGame(4)
    # mueve el circulo
    if aux_circle_y >= 0 and aux_circle_y <= CELL_SIZE*3:
        circle_y = aux_circle_y

    pointer_texture_rect = pointer_texture.get_rect()
    pointer_texture_rect.x = 32
    pointer_texture_rect.y = 32
    screen.blit(pointer_texture, (width_center+pointer_texture_rect.x*center_menu,height_center+pointer_texture_rect.y*5+center_menu+circle_y))

    return circle_y  # retornas posicion del circulo o puntero de selección

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
#memoria de sombras
list_shadows = []

#dibujado de sombras
def drawShadows(screen):
    
    map_collider_matriz=get_collider_matrix('level00')
    eje_y = 0  # eje y  
    cont=0
    shadows=[]

    #trackero de muros, más de 9 muros, crea una sombra
    for row in map_collider_matriz:
        for column in row:
            if (column == '1'):  # colision
                cont+=1
                if cont>9:
                    shadows.append(eje_y)
                    break          
            else: 
                cont=0
        eje_y = eje_y + CELL_SIZE  # aumenta y+32
        cont=0  
    
    for i in range(len(shadows)-1):
        if len(players_list)==1:
            if players_list[0].getPositionY()<shadows[i+1] or shadows[i+1] in list_shadows:
                alpha=0 
            else: 
                alpha=215
        elif len(players_list)==2:
            if players_list[0].getPositionY()<shadows[i+1] or  players_list[1].getPositionY()<shadows[i+1] or shadows[i+1] in list_shadows:
                alpha=0 
            else: 
                alpha=215
        elif len(players_list)==3:
            if players_list[0].getPositionY()<shadows[i+1] or  players_list[1].getPositionY()<shadows[i+1] or  players_list[2].getPositionY()<shadows[i+1] or shadows[i+1] in list_shadows:
                alpha=0 
            else: 
                alpha=215
        else:
            if players_list[0].getPositionY()<shadows[i+1] or  players_list[1].getPositionY()<shadows[i+1] or  players_list[2].getPositionY()<shadows[i+1] or  players_list[3].getPositionY()<shadows[i+1] or shadows[i+1] in list_shadows:
                alpha=0 
            else: 
                alpha=215
        shadow=pygame.Surface((SCREEN_WIDTH,shadows[i+1]-shadows[i]))
        shadow.set_alpha(alpha)
        if alpha==0:
            list_shadows.append(shadows[i+1])
        screen.blit(shadow,(0,shadows[i]))

background_music = Music(setting.musics_url_list)

#desde aquí empieza el programa
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
            memoryPositionCircle = setPlayers(event, screen)
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

        #dibujo sombras
        drawShadows(screen)

        #dibujo sombras
        drawShadows(screen)

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
