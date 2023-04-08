from scripts.collider_matrix_maker import get_collider_matrix
import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
letter_style = "assets/font/Silver.ttf"
image = 'assets/dungeon/chest_2_open.png'
font='assets/dungeon/floor/sandstone_floor_0.png'
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
        Triggers.numPlayersReady = numPlayers

    def drawListTriggersActive(screen:pygame.Surface):
        
        textoFont = pygame.font.Font(letter_style, 20) 
       
        size_messageOpen=120
        size_messageExit=90
        centerx_text=size_messageOpen/3
        centerx_text2=size_messageExit/3
        centery_text=CELL_SIZE/2
        
        for triggers  in  Triggers.listTriggersScreen  : 
            aux=triggers.split('-')
            if triggers!=Triggers.ActionNextScene:
                newMessage="Desea abrir el cofre?"
                text = textoFont.render(newMessage, 1, color)
                if float(aux[0])-centerx_text<0:
                    centerx_text=CELL_SIZE
                if float(aux[0])-centerx_text>=SCREEN_WIDTH-size_messageOpen:
                    centerx_text=CELL_SIZE/2
                    
                screen.blit(text, (float(aux[0])-centerx_text,float(aux[1])-centery_text))
            else: 
                newMessage="Esperando..."  + str( Triggers.numPlayersReady)+"/"+str( Triggers.countPlayersNextScene)
                text = textoFont.render(newMessage, 1, color)
                if float(aux[0])-centerx_text2<0:
                    centerx_text2=CELL_SIZE
                if float(aux[0])-centerx_text2>=SCREEN_WIDTH-size_messageExit:
                    centerx_text2+=CELL_SIZE
                
                screen.blit(text, (float(aux[0])-centerx_text2,float(aux[1])-centery_text))
                
            centerx_text=size_messageOpen/3
            
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
    messageOpen=False
    messageExit=False
    listPositions=[]

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
        
        #action cofres
        for chestAction in Triggers.chestTriggerList: #recorre las acciones de apertura de cofre
            aux_chestAction = str(chestAction).split('-')
            trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
            chest=aux_chestAction[2]+"-"+aux_chestAction[3]
            
            if trigger==str(position[0])+"-"+str(position[1]) and chest not in  Triggers.listTriggersActivated:#si uno abre el cofre, otro ya no puede
                Triggers.messageOpen=True
                
                if event.type == pygame.KEYDOWN:

                    if event.key ==pygame.K_q and id==0:#cambiar imagen de cofre
                       Triggers.listTriggersActivated.append(chest)
                    if event.key ==pygame.K_RSHIFT and id==2:#cambiar imagen de cofre
                       Triggers.listTriggersActivated.append(chest)
                    if event.key ==pygame.K_KP_7 and id==3:#cambiar imagen de cofre
                       Triggers.listTriggersActivated.append(chest)
                    if event.key ==pygame.K_t and id==1:#cambiar imagen de cofre
                       Triggers.listTriggersActivated.append(chest)
                        
                
                if str(float(aux_chestAction[2]))+"-"+ str(float(aux_chestAction[3])) not in Triggers.listTriggersScreen: #no duplicados
                    Triggers.listTriggersScreen.append(  str(float(aux_chestAction[2]))+"-"+ str(float(aux_chestAction[3])) ) 
                    
                #ejecutar acciones para apertura de cofre
            else :
                print ("a") 
                pass
            
        #action salida
        if str(position[0])+"-"+str(position[1]) == Triggers.ActionNextScene:#salida
            
            Triggers.messageExit=True
        
            if str(position[0])+"-"+str(position[1]) not in Triggers.listTriggersScreen: #no duplicados
               #contador de jugadores en salida
                Triggers.listTriggersScreen.append( str(position[0])+"-"+str(position[1]))     
                #ejecutar acciondes para salida
                
        else:
            Triggers.numPlayersReady-=1
                   
        #salir de action
           
        if Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and Triggers.messageOpen and Triggers.ActionNextScene  not in Triggers.listTriggersScreen:
            
            Triggers.listTriggersScreen.clear()
            aux_list=Triggers.twoTriggersActivated()
            if len(aux_list)>0:
                for chestAction in Triggers.chestTriggerList:
                    aux_chestAction = str(chestAction).split('-')
                    trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
                    chest=aux_chestAction[2]+"-"+aux_chestAction[3]
                    if trigger  in aux_list:
                       Triggers.listTriggersScreen.append(chest)  
                        
        elif  Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and  Triggers.messageOpen and Triggers.ActionNextScene  in Triggers.listTriggersScreen:
            
            Triggers.listTriggersScreen.clear()
            
            aux_list=Triggers.twoTriggersActivated()
            if len(aux_list)>0:
                for chestAction in Triggers.chestTriggerList:
                    aux_chestAction = str(chestAction).split('-')
                    trigger=aux_chestAction[0]+"-"+aux_chestAction[1]
                    chest=aux_chestAction[2]+"-"+aux_chestAction[3]
                    if trigger  in aux_list:
                       Triggers.listTriggersScreen.append(chest)  

            if Triggers.ActionNextScene in Triggers.listPositions:
                Triggers.listTriggersScreen.append(Triggers.ActionNextScene)  
        
        elif  Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not  Triggers.messageOpen and Triggers.ActionNextScene  in Triggers.listTriggersScreen:
            
            Triggers.listTriggersScreen.clear()

            if Triggers.ActionNextScene in Triggers.listPositions:
                Triggers.listTriggersScreen.append(Triggers.ActionNextScene)


        elif Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not Triggers.messageOpen and Triggers.ActionNextScene  not in Triggers.listTriggersScreen:
            Triggers.listTriggersScreen.pop()
            
        elif Triggers.aux_cont==Triggers.countPlayersNextScene and len(Triggers.listTriggersScreen)>0   and not Triggers.messageExit and Triggers.ActionNextScene  in Triggers.listTriggersScreen:
            Triggers.listTriggersScreen.pop()  
        elif len(Triggers.listTriggersActivated) >0:
            
            for delete in Triggers.listTriggersActivated:
                if delete in Triggers.listTriggersScreen:
                    Triggers.listTriggersScreen.remove(delete)    
                          
        if Triggers.aux_cont== Triggers.countPlayersNextScene:
            Triggers.aux_cont=0
            Triggers.messageOpen=False
            Triggers.messageExit=False
            Triggers.listPositions.clear()
                        
       