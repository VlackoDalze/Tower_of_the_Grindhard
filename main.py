import pygame
from sys import exit
import scripts.setting as setting
from scripts.jugador import Jugador
from scripts.collider_matrix_maker import get_collider_matrix, get_animated_decorations_matrix
from scripts.torch import Torch
from scripts.players_views import Views
from scripts.ui_fragment import UI_fragment


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
background_sound_1 =  pygame.mixer.Sound("./assets/sounds/adventures_of_flying_jack.mp3")# sonido de fondo
background_sound_2 =  pygame.mixer.Sound("./assets/sounds/epic_blockbuster 2.mp3")
battle_sound = pygame.mixer.Sound("./assets/sounds/battle_ready.mp3")
boss_battle_sound = pygame.mixer.Sound("./assets/sounds/epic_boss_battle.mp3")
scene_level = 'level00'
player_texture = pygame.image.load(
    "assets/player/base/elf_male.png")  # Textura de jugador
players_list = []  # lista jugadores

# intro de juego
intro_setPlayers = ["Bienvendo a ", "Tower of the Grindhard", "desea empezar esta aventura",
                    "sólo o acompañado?", "1 jugador", "2 jugadores", "3 jugadores", "4 jugadores"]
memoryPositionCircle = 0
letter_style = "assets/font/Silver.ttf"


def playersInGame(num_players):
    for i in range(num_players):
        player = Jugador(screen, "player"+str(i+1), "none",
                         player_texture, None, None, None, 3, 19, "Humano")
        players_list.append(player)


def setPlayers(event, screen: pygame.Surface):

    letter_size = 15  # ancho de cada letra en px
    # centrar texto linea horizontal esta relacionado al tamaño de la letra importada
    width_center = SCREEN_WIDTH/4
    # centrar texto linea vertical esta relacionado al tamaño de la letra importada
    height_center = SCREEN_HEIGHT/4
    # tamaño de linea centrada en px
    line_size = (len(intro_setPlayers[0])+len(intro_setPlayers[1]))*letter_size
    # guarda la posicion del circulo o puntero de seleccion
    circle_y = memoryPositionCircle
    # letra importada desde font
    textoFont = pygame.font.Font(letter_style, 50)
    # al ser un circulo su tamaño es distinto al de las letras, por lo tanto hay que centrarlo
    center_circle = 3
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

    circulo = pygame.Surface((CELL_SIZE, CELL_SIZE*4))  # surface
    pygame.draw.circle(circulo, (255, 0, 0), (CELL_SIZE/2,
                       CELL_SIZE/2+circle_y), CELL_SIZE/2)  # circulo
    screen.blit(circulo, (width_center+CELL_SIZE*center_menu,
                height_center+CELL_SIZE*5+center_circle))

    return circle_y  # retornas posicion del circulo o puntero de seleccion


# collide_level1 = get_collider_matrix(scene_level)
animated_decorations_matrix = get_animated_decorations_matrix(scene_level)

ui_frag = UI_fragment(screen, player_texture, (0, 0))


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
list_shadows_y = []
list_shadows_x = []



#dibujado de sombras
def drawShadows(screen):
    
    map_collider_matriz=get_collider_matrix('level00')
    eje_y = 0  # eje y  
    eje_x=0
    cont_y=0
    cont_x=0
    shadows_y=[]
    shadows_x=[]
    

    #trackero de muros, más de 9 muros, crea una sombra horizontal
    for row in map_collider_matriz:
        for column in row:
            if (column == '1'):  # colision
                cont_y+=1
                if cont_y>9:
                    shadows_y.append(eje_y)
                    break          
            else: 
                cont_y=0
        eje_y+=CELL_SIZE  # aumenta y+32
        cont_y=0  
 
   
     #trackero de muros, más de 9 muros, crea una sombra vertical
    shadows_x_row=[]
    for  i in range(0,len(shadows_y)-1):
        valueRow=int(shadows_y[i]/CELL_SIZE)
        limitColumn=int(SCREEN_WIDTH/CELL_SIZE)
        eje_x=0
        shadows_x_row.clear()
        for h in range(0,limitColumn):
            for j in range(0,4):
                if ( map_collider_matriz[valueRow+j][eje_x] == '1'): # colision
                    cont_x+=1 
         
                if cont_x>2:
                    shadows_x_row.append([valueRow,eje_x])
                    break
                
            if eje_x<limitColumn:  
                eje_x+=1
                cont_x=0
        
        aux_list=shadows_x_row.copy()
        shadows_x.append(aux_list)    
                 
    index_shadows_y=0
    for fila in shadows_x:
        for i in range(0,len(fila)-1):

            if i==len(fila)-2 and index_shadows_y==len(shadows_y)-2: 
                shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE+CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]+CELL_SIZE))
            elif i==len(fila)-2:
                shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE+CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]))
            elif index_shadows_y==len(shadows_y)-2:
                shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]+CELL_SIZE))
            else:
                shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]))


            if len(players_list)==1:
                if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1] or shadows_y[index_shadows_y+1] in list_shadows_y:
                    alpha=0
                else: 
                    alpha=215
            elif len(players_list)==2:
                if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] or shadows_y[index_shadows_y+1] in list_shadows_y:
                    alpha=0 
                else: 
                    alpha=215
            elif len(players_list)==3:
                if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] or shadows_y[index_shadows_y+1] in list_shadows_y:
                    alpha=0 
                else: 
                    alpha=215
            else:
                if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] or  players_list[3].getPositionY()<shadows_y[index_shadows_y+1] or shadows_y[index_shadows_y+1] in list_shadows_y:
                    alpha=0 
                else: 
                    alpha=215
            
            
           
            shadow.set_alpha(alpha)
            
            if alpha==0:
                list_shadows_y.append(shadows_y[index_shadows_y+1])
                list_shadows_x.append(fila[i+1][1])
            
            screen.blit(shadow,(fila[i][1]*CELL_SIZE,fila[i][0]*CELL_SIZE))
            
        index_shadows_y+=1

#desde aqui empieza el programa

while True:
    # El evento pygame.QUIT significa que el usuario hizo click en X para cerrar la ventana
    for event in pygame.event.get():
        # salir
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.Sound.play(background_sound_2)
                print("2")

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
