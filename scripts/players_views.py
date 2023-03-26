import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT

viewsPositions = [(0, 0),  # player 1
                  ((SCREEN_WIDTH/2)+CELL_SIZE/2, CELL_SIZE),  # player 2
                  (CELL_SIZE, (SCREEN_HEIGHT/2)+CELL_SIZE/2),  # player 3
                  ((SCREEN_WIDTH/2)+CELL_SIZE/2,
                  (SCREEN_HEIGHT/2)+CELL_SIZE/2)  # player 4
                  ]

viewsSizes = [(SCREEN_WIDTH, SCREEN_HEIGHT),  # 1 player
              (SCREEN_WIDTH/2-CELL_SIZE*1.5, SCREEN_HEIGHT-CELL_SIZE*2),  # 2 players
              (SCREEN_WIDTH/2-CELL_SIZE*1.5, SCREEN_HEIGHT /2-CELL_SIZE *1.5)  # 3 and 4 players
              ]  # restamos 2 celdas la del inicio y la del final
POSITIONX_PREV=96
POSITIONY_PREV=608

class Views:
    
    
    
    def __init__(self, players, screen):
        self.playerList = players
        
        self.screen = screen
        self.numPlayers = len(players)
        if self.numPlayers == 1:
            self.sizePlayer = (viewsSizes[0])
        elif self.numPlayers == 2:
            self.sizePlayer = (viewsSizes[1])
        else:
            self.sizePlayer = (viewsSizes[2])

    def playerView(self):
        widthView = SCREEN_WIDTH/2-CELL_SIZE*1.5
        heightView = SCREEN_HEIGHT/2-CELL_SIZE*1.5

        limitViewWidth = SCREEN_WIDTH - widthView
        limitViewHeight = SCREEN_HEIGHT - heightView
        
        basex=0
        basey=SCREEN_HEIGHT-heightView
        positionx =0 
        positiony =0
       
        for i in range(self.numPlayers):
            view = pygame.Surface(self.sizePlayer)
            jugador = self.playerList[i]
            
           
            POSITIONX_PREV+=jugador.getPositionX()  
            POSITIONY_PREV+=jugador.getPositionY()
            print(POSITIONX_PREV,POSITIONY_PREV)
        # ubicar la vista, respetando los limites, por alguna razon tiene errores si no lo haces
            positionx = jugador.getPositionX()  
            positiony = jugador.getPositionY()
            print(positionx, positiony)
            # aqui hay que hacer lo de los hilos para que las camaras se fijen en c/u de los players
            if positionx>POSITIONX_PREV:
                basex+=CELL_SIZE
            if positionx<POSITIONX_PREV:
                basex-=CELL_SIZE 
            if positiony>POSITIONY_PREV:
                basey+=CELL_SIZE 
            if positiony<POSITIONY_PREV:
                basey-=CELL_SIZE
            # recorte de screen esot varia segun la posicion del personaje
            recorte= self.screen.subsurface((basex, basey, widthView, heightView))
            recorte= pygame.transform.scale(recorte,viewsSizes[i]) #redimiension
            # ubica dentro del view el recorte del screen
            view.blit(recorte, (0,0))#es el relleno de la vista
           # view.fill()
            
            self.screen.blit(view, viewsPositions[i])#es la vista
