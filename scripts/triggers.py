from scripts.collider_matrix_maker import get_collider_matrix
import pygame
import scripts.setting as setting
import scripts.ui_fragment as ui_fragment

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
letter_style = "assets/font/Silver.ttf"
image = 'assets/dungeon/chest_2_open.png'
font='assets/dungeon/floor/sandstone_floor_0.png'
icon="assets/misc/error.png"
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
                ui_fragment.Text_area_fragment(screen, newMessage, font_size, position,(200,100)).draw()

            else:
                newMessage="Esperando..."  + str( Triggers.numPlayersReady)+"/"+str( Triggers.countPlayersNextScene)
                if float(aux[0])+size_messageExit>=SCREEN_WIDTH-size_messageExit:
                    aux[0]=SCREEN_WIDTH-size_messageExit
                position = (str(float(aux[0])),str(float(aux[1])-centery_text))
                ui_fragment.Text_area_fragment(screen, newMessage, font_size, position,(200,100)).draw()

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
                    