import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT
viewsPositions =[(CELL_SIZE,CELL_SIZE),#player 1
                 (int(SCREEN_WIDTH/2)+CELL_SIZE/2,CELL_SIZE),#player 2
                 (CELL_SIZE,int(SCREEN_HEIGHT/2)+CELL_SIZE/2),#player 3
                 (int(SCREEN_WIDTH/2)+CELL_SIZE/2,int(SCREEN_HEIGHT/2)+CELL_SIZE/2)#player 4
                 ]
viewsSizes =[(SCREEN_WIDTH-CELL_SIZE*2, SCREEN_HEIGHT-CELL_SIZE*2),#1 player
             (SCREEN_WIDTH/2-CELL_SIZE*1.5, SCREEN_HEIGHT-CELL_SIZE*2),#2 players
             (SCREEN_WIDTH/2-CELL_SIZE*1.5, SCREEN_HEIGHT/2-CELL_SIZE*1.5)# 3 and 4 players
             ]#restamos 2 celdas la del inicio y la del final

class Views:
    def __init__(self,players,screen):
        self.playerList=players
       
        self.screen = screen
        self.numPlayers = len(players)
        if self.numPlayers == 1:
            self.sizePlayer=(viewsSizes[0])
        elif self.numPlayers==2:
            self.sizePlayer=(viewsSizes[1])
        else:
            self.sizePlayer=(viewsSizes[2])
  
        

    def playerView(self):   
        for i in range(self.numPlayers):
            view=pygame.Surface(self.sizePlayer)
            jugador = self.playerList[i]
        # hacer algo con objeto_convertido  
             
            positionx=jugador.getPositionX()-(SCREEN_WIDTH/2-CELL_SIZE*1.5)/2
            
            positiony=jugador.getPositionY()-(SCREEN_HEIGHT/2-CELL_SIZE*1.5)/2
       
            print(positionx,positiony)
            
            #aqui hay que hacer lo de los hilos para que las camaras se fijen en c/u de los players
            
            camVision=pygame.Rect((positionx,positiony,SCREEN_WIDTH/2-CELL_SIZE*1.5,SCREEN_HEIGHT/2-CELL_SIZE*1.5)) #recorte de screen esot varia segun la posicion del personaje
           
           
            
            view.blit(self.screen,(0,0),camVision)  # ubica dentro del view el recorte del screen
            
            self.screen.blit(view,viewsPositions[i])
          
