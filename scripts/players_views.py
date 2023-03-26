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
    def __init__(self,players=None,screen=None):
        self.players = players
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
            self.screen.blit(view,viewsPositions[i])
        