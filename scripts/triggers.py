from scripts.collider_matrix_maker import get_collider_matrix
import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
letter_style = "assets/font/Silver.ttf"
image = 'assets/dungeon/chest_2_open.jpg'
color=(255, 255, 255)     
message = ["Desea abrir el cofre?","Esperando... "]

class Triggers():
    
    chestTriggerList=[]
    listTriggersActivated=[]
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
                    if map_collider_matriz[row][column+1]=='3' :
                        Triggers.chestTriggerList.append(str(eje_x+CELL_SIZE)+"-"+str(eje_y)+"-"+str(eje_x)+"-"+str(eje_y))
                    if map_collider_matriz[row-1][column]=='3' :
                        Triggers.chestTriggerList.append(str(eje_x)+"-"+str(eje_y-CELL_SIZE)+"-"+str(eje_x)+"-"+str(eje_y))
                    if map_collider_matriz[row+1][column]=='3':
                        Triggers.chestTriggerList.append(str(eje_x)+"-"+str(eje_y+CELL_SIZE)+"-"+str(eje_x)+"-"+str(eje_y))
                        
                eje_x = eje_x + CELL_SIZE  # aumenta x +32

            eje_y = eje_y + CELL_SIZE  # aumenta y+32
            eje_x = 0  # resets x

    def setCountPlayers(numPlayers):
        Triggers.countPlayersNextScene =numPlayers

    def drawListTriggersActive(screen):
        
        textoFont = pygame.font.Font(letter_style, 20) 
        
        for triggers  in  Triggers.listTriggersScreen  : 
            aux=triggers.split('-')
            text = textoFont.render(message[0], 1, color)
        
            screen.blit(text, (float(aux[0]),float(aux[1])))
            
        if  len(Triggers.listTriggersActivated)>0:
            for chest in Triggers.listTriggersActivated:
                aux=chest.split('-')
                changeChest=pygame.Surface((CELL_SIZE,CELL_SIZE))
                model=pygame.image.load(image)
                changeChest.blit(model, (0,0))
                screen.blit(changeChest,(float(aux[0]),float(aux[1])) )
            
   
    aux_cont= 0
    messageOpen=False
    
    def searchListTriggers(position,scene_level,event):
        
        if len(Triggers.chestTriggerList)==0:
            Triggers.createListTriggers(scene_level)
            
       
        Triggers.aux_cont+=1
        centerx_text=40
        centery_text=16
        
        
        for chestAction in Triggers.chestTriggerList: #recorre las acciones de apertura de cofre
            aux_chestAction = str(chestAction).split('-')
            trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
            chest=aux_chestAction[2]+"-"+aux_chestAction[3]
            
            if trigger==str(position[0])+"-"+str(position[1]) and chest not in  Triggers.listTriggersActivated:#si uno abre el cofre, otro ya no puede
                Triggers.messageOpen=True
                if event.type == pygame.KEYDOWN:

                    if event.key ==pygame.K_SPACE:#cambiar imagen de cofre
                       Triggers.listTriggersActivated.append(chest)
                        
                
                if str(float(aux_chestAction[2])-centerx_text)+"-"+ str(float(aux_chestAction[3])-centery_text) not in Triggers.listTriggersScreen: #no duplicados
                    Triggers.listTriggersScreen.append(  str(float(aux_chestAction[2])-centerx_text)+"-"+ str(float(aux_chestAction[3])-centery_text) ) 
                    
                #ejecutar acciones para apertura de cofre
        
        if Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not Triggers.messageOpen:
            Triggers.listTriggersScreen.pop()
              
        if Triggers.aux_cont== Triggers.countPlayersNextScene:
            Triggers.aux_cont=0
            Triggers.messageOpen=False
                        
        # if str(position[0])+"-"+str(position[1])==Triggers.ActionNextScene:#salida
            
        #         Triggers.countPlayersNextScene+=1
        #         text = textoFont.render(messageExit + str(Triggers.numPlayersReady)+"/"+str( Triggers.countPlayersNextScene), 1, color) #contador de jugadores en salida
               
                
                #ejecutar acciondes para salida

       
                