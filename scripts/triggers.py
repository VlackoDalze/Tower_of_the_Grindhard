from scripts.collider_matrix_maker import get_collider_matrix
import pygame
import scripts.setting as setting
import scripts.ui_element as ui_element
from scripts.enemy import Enemy
# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
letter_style = "assets/font/Silver.ttf"
image = 'assets/dungeon/chest_2_open.png'
font='assets/dungeon/floor/sandstone_floor_0.png'
icon="assets/misc/error.png"


positions_players=[[(SCREEN_WIDTH/8,SCREEN_HEIGHT/6)]
                   
                   ,[(SCREEN_WIDTH/8,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/8,SCREEN_HEIGHT/2.5/2+120)] 
                   
                   ,[(SCREEN_WIDTH/8+100,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/8,SCREEN_HEIGHT/2.5/2+50),\
                           (SCREEN_WIDTH/8+100,SCREEN_HEIGHT/2.5/2+190)]
                   
                   ,[(SCREEN_WIDTH/8+100,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/8,SCREEN_HEIGHT/2.5/2+20),\
                           (SCREEN_WIDTH/8,SCREEN_HEIGHT/2.5/2+130),\
                               (SCREEN_WIDTH/8+100,SCREEN_HEIGHT/2.5/2+240)]]    
   
position_enemies=[[(SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/6)]
                  
                   ,[(SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2.5/2+120)] 
                   
                   ,[(SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/2+SCREEN_WIDTH/6+100,SCREEN_HEIGHT/2.5/2+50),\
                           (SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2.5/2+190)]
                   
                   ,[(SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2/7),\
                       (SCREEN_WIDTH/2+SCREEN_WIDTH/6+100,SCREEN_HEIGHT/2.5/2+20),\
                           (SCREEN_WIDTH/2+SCREEN_WIDTH/6+100,SCREEN_HEIGHT/2.5/2+130),\
                               (SCREEN_WIDTH/2+SCREEN_WIDTH/6,SCREEN_HEIGHT/2.5/2+240)]] 

#---------------------- barra de vida, ancho, barra de mana, cursor de turno, letras de vida y mana
position_bars=[[(50,20,SCREEN_WIDTH/4,50,5,10,(0,25,20,0,40,25), (SCREEN_WIDTH/4-40,27.5,12.5))]
                      
                   ,[(25,20,SCREEN_WIDTH/4/2,25,5,10,(-25,25,-5,0,15,25), (SCREEN_WIDTH/6-60,27.5,12.5)),\
                       (25,20,SCREEN_WIDTH/4/2,25,5,10,(-25,25,-5,0,15,25), (SCREEN_WIDTH/6-60,27.5,12.5))]\
                   
                   ,[(0,20,SCREEN_WIDTH/4/3,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-80,27.5,12.5)),\
                       (0,20,SCREEN_WIDTH/4/3,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-80,27.5,12.5)),\
                          (0,20,SCREEN_WIDTH/4/3,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-80,27.5,12.5))]
                   
                   ,[(0,20,SCREEN_WIDTH/4/4,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-100,27.5,12.5)),\
                       (0,20,SCREEN_WIDTH/4/4,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-100,27.5,12.5)),\
                          (0,20,SCREEN_WIDTH/4/4,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-100,27.5,12.5)),\
                              (0,20,SCREEN_WIDTH/4/4,0,5,10,(-50,25,-30,0,-10,25), (SCREEN_WIDTH/6-100,27.5,12.5))]]      
  
size_playersAndEnemies=[(SCREEN_WIDTH/4,SCREEN_HEIGHT/2.5)
                        ,(SCREEN_WIDTH/4/2,SCREEN_HEIGHT/2.5/2)
                        ,(SCREEN_WIDTH/4/3,SCREEN_HEIGHT/2.5/3)
                        ,(SCREEN_WIDTH/4/4,SCREEN_HEIGHT/2.5/4)]




color=(255, 255, 255)     


class Triggers():
    
    chestTriggerList=[]
    listTriggersActivated=[]
    listTriggers=[]
    countPlayersNextScene=0
    numPlayersReady=0
    ActionNextScene=""
    listTriggersScreen=[]

    
    def createListTriggers(scene_level) :
        
        map_collider_matriz = get_collider_matrix(scene_level)
        eje_x = 0  # eje x
        eje_y = 0  # eje y
        
        for row in  range(0,len(map_collider_matriz)-1):
            for column in range(0,len(map_collider_matriz[row])-1):
                #1 muro , 4 adorno o cofre, 3 acion abrir cofre,  2 acion puerta salida
                if map_collider_matriz[row][column] == '2':  # next scene
                   Triggers.ActionNextScene=(str(eje_x)+"-"+str(eje_y))

                if map_collider_matriz[row][column] == '4':  # others
    
                    #matriz tesoro +-x y y guarda posibles 3, si algun player activa un 3, los demas se bloquean  
                    if map_collider_matriz[row][column-1]=='3' :
                        Triggers.chestTriggerList.append(str(eje_x-CELL_SIZE)+"-"+str(eje_y)+"-"+str(eje_x)+"-"+str(eje_y))#pos 3 , pos 4 ->action x cofre
                        Triggers.listTriggers.append(str(eje_x-CELL_SIZE)+"-"+str(eje_y))
                    if map_collider_matriz[row][column+1]=='3' :
                        Triggers.chestTriggerList.append(str(eje_x+CELL_SIZE)+"-"+str(eje_y)+"-"+str(eje_x)+"-"+str(eje_y))
                        Triggers.listTriggers.append(str(eje_x+CELL_SIZE)+"-"+str(eje_y))
                    if map_collider_matriz[row-1][column]=='3' :
                        Triggers.chestTriggerList.append(str(eje_x)+"-"+str(eje_y-CELL_SIZE)+"-"+str(eje_x)+"-"+str(eje_y))
                        Triggers.listTriggers.append(str(eje_x)+"-"+str(eje_y-CELL_SIZE))
                    if map_collider_matriz[row+1][column]=='3':
                        Triggers.chestTriggerList.append(str(eje_x)+"-"+str(eje_y+CELL_SIZE)+"-"+str(eje_x)+"-"+str(eje_y))
                        Triggers.listTriggers.append(str(eje_x)+"-"+str(eje_y+CELL_SIZE))
                        
                eje_x = eje_x + CELL_SIZE  # aumenta x +32

            eje_y = eje_y + CELL_SIZE  # aumenta y+32
            eje_x = 0  # resets x

    def setCountPlayers(numPlayers):
        Triggers.countPlayersNextScene =numPlayers
       
    def drawEnemyTriggersActive(screen,playerslist,enemylist):
        
        aux_lis_enemy_triggers=[]
        
        for player in playerslist:#jugador
            for enemy in enemylist:#enemigo
                if player.getPositionX()-CELL_SIZE== enemy.getPositionX() and player.getPositionY() == enemy.getPositionY()\
                    or player.getPositionX()+CELL_SIZE== enemy.getPositionX() and player.getPositionY() == enemy.getPositionY()\
                        or player.getPositionX()==  enemy.getPositionX() and player.getPositionY()-CELL_SIZE == enemy.getPositionY()\
                            or player.getPositionX()==  enemy.getPositionX() and player.getPositionY()+CELL_SIZE == enemy.getPositionY():

                                if str(enemy.getPositionX())+"-"+str(enemy.getPositionY()) not in aux_lis_enemy_triggers:
                        
                                    image=pygame.image.load(icon)   
                                    image=pygame.transform.scale(image, (CELL_SIZE/2,CELL_SIZE/2))  
                                    screen.blit(image,(enemy.getPositionX()+CELL_SIZE/4,enemy.getPositionY()-CELL_SIZE/2))  
                                    aux_lis_enemy_triggers.append(str(enemy.getPositionX())+"-"+str(enemy.getPositionY()))
                                    player.setAffectedEnemy(enemy)
                else:
                   
                    if player.getAffectedEnemy()!=None:
                        player.setAffectedEnemy(None)

    def startBattle():
        Triggers.inBattle= True       

    def endBattle(): 
        Triggers.inBattle= False 

    inBattle=False  
    copyStatsAndSaveObjects=[[],[],[],[]] #0 players , 1 enemies , 2 noduples players , 3 noduples enemy
    aux_positions_players=None
    aux_positions_enemies=None    
    aux_positions_playersBars=None
    aux_positions_enemiesBars=None
    order_attack=[]
    aux_num_enemy=[]
    order_attack_enemy=[]
    type_enemies=None
    
    def modeBattle(players_list,screen,event): 
        screen.fill((255,255,255)) #clean
        border=5
        letter_size=15
        size_button=13*letter_size
        height_button=45
        font = pygame.font.Font(letter_style, 50)
        font3 = pygame.font.Font(letter_style, 20)             
        font2 = pygame.font.Font(letter_style, 30)      
        button_texture = pygame.image.load("./assets/gui/inventory/inventory_button.png")
        area_battle = pygame.Surface((SCREEN_WIDTH-border*2,SCREEN_HEIGHT/3*2-border*2))
        area_btns_width=SCREEN_WIDTH/3-border*2
        aux_resizeWidth=(SCREEN_WIDTH/3-border*2)/4
        area_btns_height=SCREEN_HEIGHT/3-border*2
        texts=['Habilidades','Consumibles','Otros','Vida','Mana','Ataque físico','Ataque mágico','Defensa física',
               'Defensa mágica','Precisión','Evasión','Probabilidad de crítico','Multiplicador de crítico','Velocidad']
        
        if len(Triggers.copyStatsAndSaveObjects[2])==0:
            for i in range(0,len(players_list)):
                if players_list[i] not in Triggers.copyStatsAndSaveObjects[2]:
                    Triggers.copyStatsAndSaveObjects[0].append(players_list[i].getTotalAllStatsInObject()) #stats
                    Triggers.copyStatsAndSaveObjects[2].append(players_list[i]) #players
                    
                if players_list[i].getAffectedEnemy()!=None and  Triggers.type_enemies==None:
                    type_enemies=players_list[i].getAffectedEnemy().getName()

        if len(Triggers.copyStatsAndSaveObjects[3])==0:
            Triggers.copyStatsAndSaveObjects[3]= Enemy.createRandomEnemies(type_enemies,len(players_list)) #enemies
            for enemy in  Triggers.copyStatsAndSaveObjects[3]:
                Triggers.copyStatsAndSaveObjects[1].append(enemy.getStats()) #stats
          
        if Triggers.aux_positions_players==None:
            Triggers.aux_positions_players=positions_players[len(Triggers.copyStatsAndSaveObjects[2])-1]
            Triggers.aux_positions_enemies=position_enemies[len(Triggers.copyStatsAndSaveObjects[3])-1]
            Triggers.aux_positions_playersBars=position_bars[len(Triggers.copyStatsAndSaveObjects[2])-1]
            Triggers.aux_positions_enemiesBars=position_bars[len(Triggers.copyStatsAndSaveObjects[3])-1]
        #areas
        area_btns= pygame.Surface((area_btns_width-aux_resizeWidth,area_btns_height))
        area_info=  pygame.Surface((area_btns_width +aux_resizeWidth,area_btns_height))
        area_resulButton= pygame.Surface((area_btns_width,area_btns_height))
        
        text = font.render(texts[0], True, (255, 255, 255))
        text2 = font.render(texts[1], True, (255, 255, 255))
        text3 = font.render(texts[2], True, (255, 255, 255))
          
        btn_skills = pygame.Surface((size_button,height_button))
        btn_consumables = pygame.Surface((size_button,height_button))
        btn_others = pygame.Surface((size_button,height_button))
        button_texture=pygame.transform.scale(button_texture,(size_button,height_button)) #redimiension
        
        btn_skills.blit(button_texture,(0,0))
        btn_skills.blit(text,((size_button-len(texts[0])*letter_size)/2,0) )

        btn_consumables.blit(button_texture,(0,0))
        btn_consumables.blit(text2,((size_button-len(texts[1])*letter_size)/2,0) )

        btn_others.blit(button_texture,(0,0))
        btn_others.blit(text3,((size_button-len(texts[2])*letter_size)/2,0) )

        area_btns.blit(btn_skills,(area_btns.get_width()/2-size_button/2, area_btns.get_height()/2-height_button*1.5-border))
        area_btns.blit(btn_consumables,(area_btns.get_width()/2-size_button/2,  area_btns.get_height()/2-height_button*0.5))
        area_btns.blit(btn_others,(area_btns.get_width()/2-size_button/2, area_btns.get_height()/2+height_button*0.5+border))

        screen.blit(area_battle,(0+border,0+border))
        screen.blit(area_btns,(0+border,SCREEN_HEIGHT/3*2+border))
        screen.blit(area_resulButton,(SCREEN_WIDTH/3+border-aux_resizeWidth,SCREEN_HEIGHT/3*2+border))
        
        #rangos de botones
        range_buttons =[pygame.Rect(0+border+area_btns.get_width()/2-size_button/2, SCREEN_HEIGHT/3*2+border+area_btns.get_height()/2-height_button*1.5-border,size_button,height_button),
                      pygame.Rect(0+border+area_btns.get_width()/2-size_button/2, SCREEN_HEIGHT/3*2+border+area_btns.get_height()/2-height_button*0.5,size_button,height_button),
                      pygame.Rect(0+border+area_btns.get_width()/2-size_button/2, SCREEN_HEIGHT/3*2+border+area_btns.get_height()/2+height_button*0.5+border,size_button,height_button)]
 
        #pintado de imagenes de players
        for i in range(0,len(players_list)):
            image_player= pygame.transform.scale(players_list[i].getImage(), size_playersAndEnemies[len(Triggers.copyStatsAndSaveObjects[2])-1] )#redimiension

            #barras de vida
            pygame.draw.line(screen,(0,128,0),\
                
            (Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][0] ,\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][1]),\
                    
            (Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][2]-Triggers.aux_positions_playersBars[i][0],\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][1]),\

            Triggers.aux_positions_playersBars[i][5])
            
            pygame.draw.line(screen,(0,0,255),\
                
            (Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][3],\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][4]),\
                    
            (Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][2]-Triggers.aux_positions_playersBars[i][3],\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][4]),\
                    
            Triggers.aux_positions_playersBars[i][5])

            text26= font3.render(str(Triggers.copyStatsAndSaveObjects[0][i].getHealth())+"/"+str(players_list[i].getTotalStat('health')), True, (255, 255, 255))
            text27= font3.render(str(Triggers.copyStatsAndSaveObjects[0][i].getMana())+"/"+str(players_list[i].getTotalStat('mana')), True, (255, 255, 255))

            screen.blit(text26,(Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][7][0],\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][7][1]))  
            
            screen.blit(text27,(Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][7][0],\
                Triggers.aux_positions_players[i][1]-Triggers.aux_positions_playersBars[i][7][2]))   
           
            screen.blit(image_player, Triggers.aux_positions_players[i])
            
        #pintado de imagenes de enemies 
        for i in range(0,len(Triggers.copyStatsAndSaveObjects[3])): 
            image_enemy= pygame.transform.scale(Triggers.copyStatsAndSaveObjects[3][i].getImageDefault(), size_playersAndEnemies[len(Triggers.copyStatsAndSaveObjects[3])-1]) #redimiension

            pygame.draw.line(screen,(0,128,0),\
                
            (Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][0] ,\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][1]),\
                    
            (Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][2]-Triggers.aux_positions_enemiesBars[i][0],\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][1]),\

            Triggers.aux_positions_enemiesBars[i][5])
            
            pygame.draw.line(screen,(0,0,255),\
                
            (Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][3],\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][4]),\
                    
            (Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][2]-Triggers.aux_positions_enemiesBars[i][3],\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][4]),\
                    
            Triggers.aux_positions_enemiesBars[i][5])
            
            text28= font3.render(str(Triggers.copyStatsAndSaveObjects[1][i].getHealth())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getHealth()), True, (255, 255, 255))
            text29= font3.render(str(Triggers.copyStatsAndSaveObjects[1][i].getMana())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getMana()), True, (255, 255, 255))

            screen.blit(text28,(Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][7][0],\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][7][1]))  
            
            screen.blit(text29,(Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][7][0],\
                Triggers.aux_positions_enemies[i][1]-Triggers.aux_positions_enemiesBars[i][7][2]))   
            
            screen.blit(image_enemy, Triggers.aux_positions_enemies[i])
 
        aux_higher_speed=float('-inf')  #valor minimo de float
        next_turn=None
        isEnemy=None
        
        #icono de turno basado en a velocidad, usar copy por si sufren algun debuff
        for copyPlayer in Triggers.copyStatsAndSaveObjects[0]:
            if copyPlayer not in Triggers.order_attack and  copyPlayer.getSpeed() > aux_higher_speed :
                aux_higher_speed=copyPlayer.getSpeed()
                next_turn=copyPlayer
                isEnemy=False
                
        # if len(Triggers.order_attack)==len(Triggers.copyStatsAndSaveObjects[0]):
        #     aux_higher_speed=0
            
        for copyEnemy in Triggers.copyStatsAndSaveObjects[1]:
            if copyEnemy not in Triggers.order_attack_enemy and copyEnemy.getSpeed() > aux_higher_speed:
                aux_higher_speed  =copyEnemy.getSpeed()
                next_turn=copyEnemy 
                isEnemy=True

        # dibujar el triángulo en la pantalla        
        if isEnemy:   
            for i in range(0, len(Triggers.copyStatsAndSaveObjects[1])):   
                if Triggers.copyStatsAndSaveObjects[1][i]==next_turn: 
                    pygame.draw.polygon(screen,(255, 0, 0),
                                [(Triggers.aux_positions_enemies[i][0]+Triggers.aux_positions_enemiesBars[i][6][0],Triggers.aux_positions_enemies[ i][1]-Triggers.aux_positions_enemiesBars[i][6][1]),\
                                 (Triggers.aux_positions_enemies[ i][0]+Triggers.aux_positions_enemiesBars[i][6][2],Triggers.aux_positions_enemies[ i][1]-Triggers.aux_positions_enemiesBars[i][6][3]),\
                                 (Triggers.aux_positions_enemies[ i][0]+Triggers.aux_positions_enemiesBars[i][6][4],Triggers.aux_positions_enemies[ i][1]-Triggers.aux_positions_enemiesBars[i][6][5])] )
                                            
  
                    #atributos
                    text4 = font2.render(texts[3], True, (255, 255, 255))
                    text5 = font2.render(texts[4], True, (255, 255, 255))
                    text6 = font2.render(texts[5], True, (255, 255, 255))
                    text7 = font2.render(texts[6], True, (255, 255, 255))
                    text8 = font2.render(texts[7], True, (255, 255, 255))
                    text9 = font2.render(texts[8], True, (255, 255, 255))
                    text10 = font2.render(texts[9], True, (255, 255, 255))
                    text11 = font2.render(texts[10], True, (255, 255, 255))
                    text12= font2.render(texts[11], True, (255, 255, 255))
                    text13= font2.render(texts[12], True, (255, 255, 255))
                    text14= font2.render(texts[13], True, (255, 255, 255))
                        
                    text15= font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getHealth())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getHealth()), True, (255, 255, 255))
                    text16= font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getMana())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getMana()), True, (255, 255, 255))
                    text17= font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getPhysicalAttack())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getPhysicalAttack()), True, (255, 255, 255))
                    text18 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getMagicalAttack())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getMagicalAttack()), True, (255, 255, 255))
                    text19= font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getPhysicalDefense())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getPhysicalDefense()), True, (255, 255, 255))
                    text20 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getMagicalDefense())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getMagicalDefense()), True, (255, 255, 255))
                    text21 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getPrecision())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getPrecision()), True, (255, 255, 255))
                    text22= font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getEvasion())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getEvasion()), True, (255, 255, 255))
                    text23 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getCritProbability())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getCritProbability()), True, (255, 255, 255))
                    text24 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getCritMultiplier())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getCritMultiplier()), True, (255, 255, 255))
                    text25 = font2.render(str(Triggers.copyStatsAndSaveObjects[1][i].getSpeed())+"/"+str(Triggers.copyStatsAndSaveObjects[3][i].getStats().getSpeed()), True, (255, 255, 255))
                    
                    area_info.blit(text4,(10,0))     
                    area_info.blit(text5,(10,20))
                    area_info.blit(text6,(10,40))
                    area_info.blit(text7,(10,60))     
                    area_info.blit(text8,(10,80))
                    area_info.blit(text9,(10,100))
                    area_info.blit(text10,(10,120))     
                    area_info.blit(text11,(10,140))
                    area_info.blit(text12,(10,160))
                    area_info.blit(text13,(10,180))     
                    area_info.blit(text14,(10,200))
                    
                    area_info.blit(text15,(area_info.get_width()/2+30,0))
                    area_info.blit(text16,(area_info.get_width()/2+30,20))
                    area_info.blit(text17,(area_info.get_width()/2+30,40))
                    area_info.blit(text18,(area_info.get_width()/2+30,60))
                    area_info.blit(text19,(area_info.get_width()/2+30,80))
                    area_info.blit(text20,(area_info.get_width()/2+30,100)) 
                    area_info.blit(text21,(area_info.get_width()/2+30,120))
                    area_info.blit(text22,(area_info.get_width()/2+30,140))
                    area_info.blit(text23,(area_info.get_width()/2+30,160)) 
                    area_info.blit(text24,(area_info.get_width()/2+30,180)) 
                    area_info.blit(text25,(area_info.get_width()/2+30,200))
                    break
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Triggers.order_attack_enemy.append(next_turn)   
                     
        elif not isEnemy:
            for i in range(0, len(Triggers.copyStatsAndSaveObjects[0])):   
                if Triggers.copyStatsAndSaveObjects[0][i]==next_turn: 
                    pygame.draw.polygon(screen,(255, 0, 0),
                                [(Triggers.aux_positions_players[i][0]+Triggers.aux_positions_playersBars[i][6][0],Triggers.aux_positions_players[ i][1]-Triggers.aux_positions_playersBars[i][6][1]),\
                                 (Triggers.aux_positions_players[ i][0]+Triggers.aux_positions_playersBars[i][6][2],Triggers.aux_positions_players[ i][1]-Triggers.aux_positions_playersBars[i][6][3]),\
                                 (Triggers.aux_positions_players[ i][0]+Triggers.aux_positions_playersBars[i][6][4],Triggers.aux_positions_players[ i][1]-Triggers.aux_positions_playersBars[i][6][5])] )
                                            
                    
                    #atributos
                    text4 = font2.render(texts[3], True, (255, 255, 255))
                    text5 = font2.render(texts[4], True, (255, 255, 255))
                    text6 = font2.render(texts[5], True, (255, 255, 255))
                    text7 = font2.render(texts[6], True, (255, 255, 255))
                    text8 = font2.render(texts[7], True, (255, 255, 255))
                    text9 = font2.render(texts[8], True, (255, 255, 255))
                    text10 = font2.render(texts[9], True, (255, 255, 255))
                    text11 = font2.render(texts[10], True, (255, 255, 255))
                    text12= font2.render(texts[11], True, (255, 255, 255))
                    text13= font2.render(texts[12], True, (255, 255, 255))
                    text14= font2.render(texts[13], True, (255, 255, 255))
                        
                    text15= font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getHealth())+"/"+str(players_list[i].getTotalStat('health')), True, (255, 255, 255))
                    text16= font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getMana())+"/"+str(players_list[i].getTotalStat('mana')), True, (255, 255, 255))
                    text17= font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getPhysicalAttack())+"/"+str(players_list[i].getTotalStat('physicalAttack')), True, (255, 255, 255))
                    text18 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getMagicalAttack())+"/"+str(players_list[i].getTotalStat('magicalAttack')), True, (255, 255, 255))
                    text19= font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getPhysicalDefense())+"/"+str(players_list[i].getTotalStat('physicalDefense')), True, (255, 255, 255))
                    text20 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getMagicalDefense())+"/"+str(players_list[i].getTotalStat('magicalDefense')), True, (255, 255, 255))
                    text21 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getPrecision())+"/"+str(players_list[i].getTotalStat('precision')), True, (255, 255, 255))
                    text22= font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getEvasion())+"/"+str(players_list[i].getTotalStat('evasion')), True, (255, 255, 255))
                    text23 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getCritProbability())+"/"+str(players_list[i].getTotalStat('critProbability')), True, (255, 255, 255))
                    text24 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getCritMultiplier())+"/"+str(players_list[i].getTotalStat('critMultiplier')), True, (255, 255, 255))
                    text25 = font2.render(str(Triggers.copyStatsAndSaveObjects[0][i].getSpeed())+"/"+str(players_list[i].getTotalStat('speed')), True, (255, 255, 255))
                    
                    area_info.blit(text4,(10,0))     
                    area_info.blit(text5,(10,20))
                    area_info.blit(text6,(10,40))
                    area_info.blit(text7,(10,60))     
                    area_info.blit(text8,(10,80))
                    area_info.blit(text9,(10,100))
                    area_info.blit(text10,(10,120))     
                    area_info.blit(text11,(10,140))
                    area_info.blit(text12,(10,160))
                    area_info.blit(text13,(10,180))     
                    area_info.blit(text14,(10,200))
                    
                    area_info.blit(text15,(area_info.get_width()/2+30,0))
                    area_info.blit(text16,(area_info.get_width()/2+30,20))
                    area_info.blit(text17,(area_info.get_width()/2+30,40))
                    area_info.blit(text18,(area_info.get_width()/2+30,60))
                    area_info.blit(text19,(area_info.get_width()/2+30,80))
                    area_info.blit(text20,(area_info.get_width()/2+30,100)) 
                    area_info.blit(text21,(area_info.get_width()/2+30,120))
                    area_info.blit(text22,(area_info.get_width()/2+30,140))
                    area_info.blit(text23,(area_info.get_width()/2+30,160)) 
                    area_info.blit(text24,(area_info.get_width()/2+30,180)) 
                    area_info.blit(text25,(area_info.get_width()/2+30,200))   
                    break        
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    pos_mouse = pygame.mouse.get_pos()
                    if range_buttons[0].collidepoint(pos_mouse):
                        print("habilidad")
                        Triggers.order_attack.append(next_turn)
                        # area_resulButton.blit()
                    if range_buttons[1].collidepoint(pos_mouse):
                        print("consumible")
                    if range_buttons[2].collidepoint(pos_mouse):
                        print("otros")
                        
        screen.blit(area_info,(SCREEN_WIDTH/3*2+border-aux_resizeWidth,SCREEN_HEIGHT/3*2+border))
                  
        if len(Triggers.order_attack_enemy)==len(Triggers.copyStatsAndSaveObjects[3]) and len(Triggers.order_attack)==len(Triggers.copyStatsAndSaveObjects[2]):
            Triggers.order_attack=[]
            Triggers.order_attack_enemy=[]
                 
        pass
              
    def drawListTriggersActive(screen:pygame.Surface):
        font_size = 20
        textoFont = pygame.font.Font(letter_style, font_size) 
        letter_size=CELL_SIZE*2/11 #tamaño en px de una letra
        size_messageOpen=6*letter_size #numero de letras de la palabra
        size_messageExit=15*letter_size
        centery_text=CELL_SIZE/2
        
        for triggers  in  Triggers.listTriggersScreen  : 
            aux=triggers.split('-')
            
            if not (triggers == Triggers.ActionNextScene):
                newMessage="Abrir?"
                if float(aux[0])+size_messageOpen>=SCREEN_WIDTH-size_messageOpen:
                    aux[0]=SCREEN_WIDTH-size_messageOpen
                position = (str(float(aux[0])),str(float(aux[1])-centery_text))
                ui_element.TextElement(newMessage, font_size, position,(CELL_SIZE,CELL_SIZE)).draw()

            else:
                newMessage="Esperando..."  + str( Triggers.numPlayersReady)+"/"+str( Triggers.countPlayersNextScene)
                if float(aux[0])+size_messageExit>=SCREEN_WIDTH-size_messageExit:
                    aux[0]=SCREEN_WIDTH-size_messageExit
                position = (str(float(aux[0])),str(float(aux[1])-centery_text))
                ui_element.TextAreaElement(newMessage, font_size, position).draw()

        if  len(Triggers.listTriggersActivated)>0:
            for chest in Triggers.listTriggersActivated:
                aux=chest.split('-')
                changeChest=pygame.Surface((CELL_SIZE,CELL_SIZE))
                mix1=pygame.image.load(font)
                mix2=pygame.image.load(image)
                changeChest.blit(mix1, (0,0))
                changeChest.blit(mix2, (0,0))
                screen.blit(changeChest,(float(aux[0]),float(aux[1])) )          
        
    aux_cont= 0
    prev_aux_cont= aux_cont
    messageOpen=False
    messageExit=False
    listPositions=[]
    memoryListPositions=[]
    playersReaady=[]
    
    def twoTriggersActivated():
        aux_list=[]
        for position in Triggers.listPositions:
            if position in Triggers.listTriggers:
                    aux_list.append(position) 
        return aux_list    

    def searchListTriggers(position,scene_level,event,id):
        
        if len(Triggers.chestTriggerList)==0:
            Triggers.createListTriggers(scene_level)
            
        if  Triggers.aux_cont<Triggers.countPlayersNextScene:
            Triggers.listPositions.append(str(position[0])+"-"+str(position[1]))
            
            
        Triggers.aux_cont+=1
        
        # if len(Triggers.memoryListPositions)< Triggers.aux_cont:
        #     Triggers.memoryListPositions.append(str(position[0])+"-"+str(position[1]))
        #action cofres
        
        for chestAction in Triggers.chestTriggerList: #recorre las acciones de apertura de cofre
            aux_chestAction = str(chestAction).split('-')
            trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
            chest=aux_chestAction[2]+"-"+aux_chestAction[3]
            
            if trigger==str(position[0])+"-"+str(position[1]) and chest not in  Triggers.listTriggersActivated:#si uno abre el cofre, otro ya no puede
                Triggers.messageOpen=True
                
                if event.type == pygame.KEYDOWN and   event.key==pygame.K_q and id==0:#cambiar imagen de cofre
                    Triggers.listTriggersActivated.append(chest)
                if  event.type == pygame.KEYDOWN and  event.key==pygame.K_RSHIFT and id==2:#cambiar imagen de cofre
                    Triggers.listTriggersActivated.append(chest)
                if event.type == pygame.KEYDOWN and   event.key ==pygame.K_KP_7 and id==3:#cambiar imagen de cofre
                    Triggers.listTriggersActivated.append(chest)
                if  event.type == pygame.KEYDOWN and  event.key ==pygame.K_t and id==1:#cambiar imagen de cofre
                    Triggers.listTriggersActivated.append(chest)
                
                if aux_chestAction[2]+"-"+ aux_chestAction[3] not in Triggers.listTriggersScreen: #no duplicados
                    Triggers.listTriggersScreen.append(  aux_chestAction[2]+"-"+ aux_chestAction[3] ) 
                    
                #ejecutar acciones para apertura de cofre
       
        #action salida
        if str(position[0])+"-"+str(position[1]) == Triggers.ActionNextScene:#salida
            
            Triggers.messageExit=True
            
            if len(Triggers.playersReaady)==0:
                Triggers.numPlayersReady+=1
                Triggers.playersReaady.append(str(position[0])+"-"+str(position[1])+"-"+str(id))
            
            if   str(position[0])+"-"+str(position[1])+"-"+str(id) not in Triggers.playersReaady:  
                Triggers.numPlayersReady+=1
                Triggers.playersReaady.append(str(position[0])+"-"+str(position[1])+"-"+str(id))
            
            if str(position[0])+"-"+str(position[1]) not in Triggers.listTriggersScreen: #no duplicados
               #contador de jugadores en salida
                Triggers.listTriggersScreen.append( str(position[0])+"-"+str(position[1]))     
                #ejecutar acciondes para salida
                
        else:
            if len(Triggers.playersReaady)>0:
                for player in Triggers.playersReaady:
                    
                    aux=  player.split('-')   
                    saved_posx=aux[0]
                    saved_posy=aux[1]
                    saved_id=aux[2]
                    
                    if int(saved_id)==id:
                        Triggers.numPlayersReady-=1
                        Triggers.playersReaady.remove(saved_posx+"-"+saved_posy+"-"+saved_id)
                
        #salir de action
           
        if Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and Triggers.messageOpen and Triggers.ActionNextScene  not in Triggers.listTriggersScreen and event.type != pygame.KEYDOWN:
            
            Triggers.listTriggersScreen.clear()
            aux_list=Triggers.twoTriggersActivated()
            if len(aux_list)>0:
                for chestAction in Triggers.chestTriggerList:
                    aux_chestAction = str(chestAction).split('-')
                    trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
                    chest=aux_chestAction[2]+"-"+aux_chestAction[3]
                    if trigger  in aux_list  and chest not in Triggers.listTriggersActivated:
                        Triggers.listTriggersScreen.append(chest)  

        elif  Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and  Triggers.messageOpen and Triggers.ActionNextScene  in Triggers.listTriggersScreen and event.type != pygame.KEYDOWN:
            
            Triggers.listTriggersScreen.clear()
            
            aux_list=Triggers.twoTriggersActivated()
            if len(aux_list)>0:
                for chestAction in Triggers.chestTriggerList:
                    aux_chestAction = str(chestAction).split('-')
                    trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
                    chest=aux_chestAction[2]+"-"+aux_chestAction[3]
                    if trigger  in aux_list  and chest not in Triggers.listTriggersActivated:
                        Triggers.listTriggersScreen.append(chest)  

            if Triggers.ActionNextScene in Triggers.listPositions:
                Triggers.listTriggersScreen.append(Triggers.ActionNextScene)  
        
        elif  Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not  Triggers.messageOpen and Triggers.ActionNextScene  in Triggers.listTriggersScreen and event.type != pygame.KEYDOWN:
            
            Triggers.listTriggersScreen.clear()

            if Triggers.ActionNextScene in Triggers.listPositions:
                Triggers.listTriggersScreen.append(Triggers.ActionNextScene)
                
        #error cuando nadie se mueve siempre es false       
    
        elif Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not Triggers.messageOpen and Triggers.ActionNextScene  not in Triggers.listTriggersScreen\
            and event.type != pygame.KEYDOWN:
            Triggers.listTriggersScreen.pop()


        elif len(Triggers.listTriggersActivated) >0:
            
            for delete in Triggers.listTriggersActivated:
                if delete in Triggers.listTriggersScreen:
                    Triggers.listTriggersScreen.remove(delete)    
        #falta cuando empieza y ya esta uno en una posicion 

        if Triggers.aux_cont== Triggers.countPlayersNextScene:
            Triggers.aux_cont=0
            Triggers.messageOpen=False
            Triggers.messageExit=False


            # if Triggers.isMoved():
            #     Triggers.memoryListPositions.clear()
            #     Triggers.memoryListPositions=Triggers.listPositions.copy()    
            Triggers.listPositions.clear()
        # if Triggers.aux_cont==1 and len(Triggers.listTriggersScreen)==0:
        #     Triggers.inPositionTrigger()
                       
    # def isMoved():
    #     if len(Triggers.memoryListPositions)>0 and len(Triggers.listPositions)>0:
    #         for i in range(0,len(Triggers.listPositions)):
    #             if Triggers.listPositions[i] != Triggers.memoryListPositions[i]:
    #                 return True
                
    #         return False
    #     else: 
    #         return False
        
    # def inPositionTrigger():
    #     for memory in Triggers.memoryListPositions:
    #         if memory in Triggers.listTriggers:
    #             for positionChest in Triggers.chestTriggerList:
    #                 positionChest=chest.split('-')
    #                 trigger=positionChest[0]+"-"+positionChest[1]
    #                 chest=positionChest[2]+"-"+positionChest[3]
    #                 if trigger==memory:
    #                     Triggers.listTriggersScreen(chest)
    #                     break
                    