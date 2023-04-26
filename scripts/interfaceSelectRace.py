import pygame
import scripts.setting as setting
from scripts.player import Player
from scripts.ui_element import *

button_texture = pygame.image.load("./assets/gui/inventory/inventory_button.png")
letter_style = "assets/font/Silver.ttf"
# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
MAX_FPS = setting.MAX_FPS

races=[['Humano','assets/player/base/human_male.png'],['Ogro','assets/player/base/ogre_male.png'],
       ['Centauro','assets/player/base/centaur_brown_male.png'],['Draco','assets/player/base/draconian_white_male.png'],
       ['Demonio','assets/player/base/demonspawn_red_male.png']]
class SelectRaces():
    cleaned=False
    index_selector=0
    players_selectedRaces=[]
    pos_select=0
    def startSelection(players_list,screen:pygame.Surface,event:pygame.event):
        size_button=110
        btn_prev_x=SCREEN_WIDTH/2-size_button*2
        btn_next_x=SCREEN_WIDTH/2+size_button
        btn_y= SCREEN_HEIGHT-CELL_SIZE*4
        btn_prev = pygame.Surface((size_button,45))
        btn_next = pygame.Surface((size_button,45))
        if len(SelectRaces.players_selectedRaces)==0:
            for i in range(0,len(players_list)) :
                SelectRaces.players_selectedRaces.append(False)

        if SelectRaces.pos_select<len(players_list):
            screen.fill((255,255,255)) #clean
            
            font = pygame.font.Font(letter_style, 50)
            
            text = font.render('prev', True, (0, 0, 0))
            btn_prev = pygame.Surface((size_button,45))
            btn_prev.blit(button_texture,(0,0))
            btn_prev.blit(text,(20,0) )
            
            text2 = font.render('next', True, (0, 0, 0))
            btn_next = pygame.Surface((size_button,45))
            btn_next.blit(button_texture,(0,0))
            btn_next.blit(text2,(20,0) )
            
            screen.blit(btn_prev,(btn_prev_x, btn_y))
            screen.blit(btn_next,(btn_next_x, btn_y))
            text3 = font.render("Player "+str(players_list[SelectRaces.pos_select].getId()+1), True, (255, 0, 0))  
            screen.blit(text3,(0,0))
            area_button =[pygame.Rect((btn_prev_x, btn_y,size_button,45)),pygame.Rect(btn_next_x, btn_y,size_button,45)]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                
                if mouse_presses[0]:
                
                    pos_mouse = pygame.mouse.get_pos()
                    
                    if area_button[1].collidepoint(pos_mouse) and SelectRaces.index_selector<len(races)-1:
                        SelectRaces.index_selector+=1
                    if area_button[0].collidepoint(pos_mouse) and SelectRaces.index_selector>0:
                        SelectRaces.index_selector-=1

            if event.type == pygame.KEYDOWN and   event.key==pygame.K_RETURN :
                players_list[SelectRaces.pos_select].setImage(pygame.image.load(races[SelectRaces.index_selector][1]))
                players_list[SelectRaces.pos_select].setRace(races[SelectRaces.index_selector][0])
                SelectRaces.players_selectedRaces[SelectRaces.pos_select]=True
                SelectRaces.index_selector=0
                SelectRaces.pos_select+=1
                if False not in SelectRaces.players_selectedRaces:
                    return True 
                
                    
            letter_size=32  
            size_surface=11*letter_size
            size_nameRace=len(races[SelectRaces.index_selector][0])
            image_race=pygame.Surface((SCREEN_WIDTH/3,SCREEN_HEIGHT/2)) 
            image=pygame.image.load(races[SelectRaces.index_selector][1])
            resize= pygame.transform.scale(image, (SCREEN_WIDTH/3,SCREEN_HEIGHT/2)) #redimiension
            font = pygame.font.Font(letter_style, 100)           
            text3 = font.render(races[SelectRaces.index_selector][0], True, (0, 0, 0))

            image_race.blit(resize,(0,0))

            screen.blit(text3,(SCREEN_WIDTH/3+(size_surface-size_nameRace*letter_size)/2,40))
            
            screen.blit(image_race,(SCREEN_WIDTH/3,110))
            #for player in players_list:
                
            return False
