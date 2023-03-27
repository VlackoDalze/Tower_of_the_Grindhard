import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT

viewsPositions = [(0, 0),  # player 1
                  ((SCREEN_WIDTH/2), 0),  # player 2
                  (CELL_SIZE, (SCREEN_HEIGHT/2)+CELL_SIZE/2),  # player 3
                  ((SCREEN_WIDTH/2)+CELL_SIZE/2,
                  (SCREEN_HEIGHT/2)+CELL_SIZE/2)  # player 4
                  ]

viewsSizes = [(SCREEN_WIDTH, SCREEN_HEIGHT),  # 1 player
              (SCREEN_WIDTH/2, SCREEN_HEIGHT),  # 2 players
              (SCREEN_WIDTH/2-CELL_SIZE*1.5, SCREEN_HEIGHT /2-CELL_SIZE *1.5)  # 3 and 4 players
              ]  # restamos 2 celdas la del inicio y la del final


class Views:
    widthView =  SCREEN_WIDTH/2
    heightView = SCREEN_HEIGHT/2
    basex=0
    basey=heightView
    positionx =0 
    positiony =0
    POSITIONX_PREV=0
    POSITIONY_PREV=0
    
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
       
       
        for i in range(self.numPlayers):
            view = pygame.Surface(self.sizePlayer)
            jugador = self.playerList[i]
            
            if Views.positionx == 0 and Views.positiony == 0:
                Views.POSITIONX_PREV=jugador.getPositionX()  
                Views.POSITIONY_PREV=jugador.getPositionY()
              
                
        # ubicar la vista, respetando los limites, por alguna razon tiene errores si no lo haces
            Views.positionx = jugador.getPositionX()  
            Views.positiony = jugador.getPositionY()
            print(Views.positionx, Views.positiony)
            # aqui hay que hacer lo de los hilos para que las camaras se fijen en c/u de los players
            if Views.positiony>=256 and Views.positiony<=576:
                if Views.positiony>Views.POSITIONY_PREV:
                    Views.basey+=CELL_SIZE    
                elif Views.positiony<Views.POSITIONY_PREV:
                    Views.basey-=CELL_SIZE
        
                
               
           
            if Views.positionx>=128 and Views.positionx<=608:
                if Views.positionx>Views.POSITIONX_PREV:
                    Views.basex+=CELL_SIZE    
                elif Views.positionx<Views.POSITIONX_PREV:
                    Views.basex-=CELL_SIZE
            
          
                    
            Views.POSITIONX_PREV=Views.positionx
            Views.POSITIONY_PREV=Views.positiony
            # recorte de screen esot varia segun la posicion del personaje
            print(Views.widthView)
            recorte= self.screen.subsurface((Views.basex, Views.basey, Views.widthView+16, Views.heightView))
            recorte= pygame.transform.scale(recorte,viewsSizes[i]) #redimiension
            # ubica dentro del view el recorte del screen
            view.blit(recorte, (0,0))#es el relleno de la vista
      
            self.screen.blit(view, viewsPositions[i])#es la vista
         
           
