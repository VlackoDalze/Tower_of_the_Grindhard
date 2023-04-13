import pygame
import scripts.setting as setting

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT


viewsPositions = [(0, 0),  # player 1
                  ((SCREEN_WIDTH/2), 0),  # player 2
                  (0, (SCREEN_HEIGHT/2)),  # player 3
                  ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))]  # player 4
                  

viewsSizes = [(SCREEN_WIDTH, SCREEN_HEIGHT),  # 1 player
              (SCREEN_WIDTH/2, SCREEN_HEIGHT),  # 2 players
              (SCREEN_WIDTH/2, SCREEN_HEIGHT /2)]  # 3 and 4 players
                # restamos 2 celdas la del inicio y la del final


class Views:
    widthView =  SCREEN_WIDTH/2
    heightView = SCREEN_HEIGHT/2
    DEFAULT_X_PLAYER=0
    DEFAULT_Y_PLAYER=0
    #basex/basey/positionx/positiony/POSITIONX_PREV/POSITIONY_PREV
    #  0     1       2         3           4               5
    varListforViews=[[0,heightView,0,0,0,0],[0,heightView,0,0,0,0],[0,heightView,0,0,0,0],[0,heightView,0,0,0,0]]

   
    
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

    def movCamera(num_view):    
       
        basex=Views.varListforViews[num_view][0]
        basey=Views.varListforViews[num_view][1]
        positionx=Views.varListforViews[num_view][2]
        positiony=Views.varListforViews[num_view][3]
        POSITIONX_PREV=Views.varListforViews[num_view][4]
        POSITIONY_PREV=Views.varListforViews[num_view][5]
        centerx=CELL_SIZE*4.5
        centery=CELL_SIZE*2
        #h 704, w 1056
        # al crear al personaje se pasan dos parametros x=3 y y=19
        if(Views.DEFAULT_X_PLAYER==0 and Views.DEFAULT_Y_PLAYER==0):
            Views.DEFAULT_X_PLAYER=positionx/CELL_SIZE
            Views.DEFAULT_Y_PLAYER=positiony/CELL_SIZE
            
        miny=Views.heightView-(CELL_SIZE*(SCREEN_HEIGHT/CELL_SIZE-Views.DEFAULT_Y_PLAYER))-centery #256 ->altura/2-((total celdas - celdas por defecto)*tamaño de celda)
        maxy=CELL_SIZE*(Views.DEFAULT_Y_PLAYER-1)-centery #576  ->tamaño de celda *(celdas por defecto -1) -> se le resta el tamaño de la imagen del jugador
        
        minx=(Views.DEFAULT_X_PLAYER+1) *CELL_SIZE+centerx #128  ->(celdas por defecto +1)*tamaño de celda -> se le suma el tamaño de la imagen
        maxx=Views.widthView + ((Views.DEFAULT_X_PLAYER*CELL_SIZE) -CELL_SIZE/2) +centerx#608  ->ancho/2+((celdas por defecto * tamaño de celda)-tamaño de celda/2) -> se resta 16 porque 1056/32=33 es impar

        
        if positiony>=miny and positiony<=maxy:
            if positiony>POSITIONY_PREV:
                    basey+=CELL_SIZE    
            elif positiony<POSITIONY_PREV:
                    basey-=CELL_SIZE
        elif positiony<miny:
            basey=0
        elif positiony>maxy:
            basey=Views.heightView
        
        if positionx>=minx and positionx<=maxx:
            if positionx>POSITIONX_PREV:
                basex+=CELL_SIZE    
            elif positionx<POSITIONX_PREV:
                basex-=CELL_SIZE 
        elif positionx<minx:
            basex=0
        elif positionx>maxx:
            basex=Views.widthView

        POSITIONX_PREV=positionx
        POSITIONY_PREV=positiony
        Views.varListforViews[num_view][0]=basex
        Views.varListforViews[num_view][1]=basey
        Views.varListforViews[num_view][2]=positionx
        Views.varListforViews[num_view][3]=positiony
        Views.varListforViews[num_view][4]=POSITIONX_PREV
        Views.varListforViews[num_view][5]=POSITIONY_PREV
        
        return (basex, basey, Views.widthView, Views.heightView)
    
    def createXandYprev(jugador,num_view):
        Views.varListforViews[num_view][4]=jugador.getPositionX()  
        Views.varListforViews[num_view][5]=jugador.getPositionY()
        
    def playerView(self):
            view = pygame.Surface(self.sizePlayer)
            # aqui hay que hacer lo de los hilos para que las camaras se fijen en c/u de los players
            if self.numPlayers==1:
                
                view = pygame.Surface(self.sizePlayer)
                
                if (Views.varListforViews[0][4]== 0 and Views.varListforViews[0][5]==0 ) :
                    Views.createXandYprev( self.playerList[0],0)
                    
                Views.varListforViews[0][2] = self.playerList[0].getPositionX()  
                Views.varListforViews[0][3] = self.playerList[0].getPositionY()
           
                recorte= self.screen.subsurface(Views.movCamera(0))
                recorte= pygame.transform.scale(recorte,viewsSizes[0]) #redimiension
          
                view.blit(recorte, (0,0))#es el relleno de la vista
                
                self.screen.blit(view, viewsPositions[0])#es la vista
                
            elif self.numPlayers==2: 
                aux_transform_x=SCREEN_WIDTH/2 
                aux_transform_y=SCREEN_HEIGHT/2
                aux_center_recorte=CELL_SIZE*4.5
                view = pygame.Surface(self.sizePlayer)
                view2 = pygame.Surface(self.sizePlayer)
                
                if (Views.varListforViews[0][4]== 0 and Views.varListforViews[0][5]==0 ) :
                    Views.createXandYprev(self.playerList[0],0)
                if (Views.varListforViews[1][4]== 0 and Views.varListforViews[1][5]==0 ) :
                    Views.createXandYprev( self.playerList[1],1)
                    
                Views.varListforViews[0][2] = self.playerList[0].getPositionX()  
                Views.varListforViews[0][3] = self.playerList[0].getPositionY() 

                Views.varListforViews[1][2] = self.playerList[1].getPositionX()  
                Views.varListforViews[1][3] = self.playerList[1].getPositionY()
                
                recorte= self.screen.subsurface( Views.movCamera(0))
                recorte2= self.screen.subsurface( Views.movCamera(1))
                
                recorte= pygame.transform.scale(recorte, (aux_transform_x,aux_transform_y)) #redimiension
                recorte2= pygame.transform.scale(recorte2, (aux_transform_x,aux_transform_y)) #redimiension
                    
                view.blit(recorte, (0,aux_center_recorte))#es el relleno de la vista
                view2.blit(recorte2, (0,aux_center_recorte))#es el relleno de la vista 

                self.screen.blit(view, viewsPositions[0])#es la vista  
                self.screen.blit(view2, viewsPositions[1])#es la vista 

                Views.marginView(self.screen, 2)
                
            elif self.numPlayers==3:
                
                view = pygame.Surface(self.sizePlayer)
                view2 = pygame.Surface(self.sizePlayer)
                view3 = pygame.Surface(self.sizePlayer)

                if (Views.varListforViews[0][4]== 0 and Views.varListforViews[0][5]==0 ) :
                    Views.createXandYprev( self.playerList[0],0)
                if (Views.varListforViews[1][4]== 0 and Views.varListforViews[1][5]==0 ) :
                    Views.createXandYprev( self.playerList[1],1)
                if (Views.varListforViews[2][4]== 0 and Views.varListforViews[2][5]==0 ) :
                    Views.createXandYprev( self.playerList[2],1)  
                    
                Views.varListforViews[0][2] = self.playerList[0].getPositionX()  
                Views.varListforViews[0][3] = self.playerList[0].getPositionY()  

                Views.varListforViews[1][2] = self.playerList[1].getPositionX()  
                Views.varListforViews[1][3] = self.playerList[1].getPositionY()
                
                Views.varListforViews[2][2] = self.playerList[2].getPositionX()  
                Views.varListforViews[2][3] = self.playerList[2].getPositionY()
                
                recorte= self.screen.subsurface(Views.movCamera(0))
                recorte2= self.screen.subsurface(Views.movCamera(1))
                recorte3= self.screen.subsurface(Views.movCamera(2))
                
                recorte= pygame.transform.scale(recorte, viewsSizes[2]) #re-dimensiono
                recorte2= pygame.transform.scale(recorte2, viewsSizes[2]) #re-dimensiono
                recorte3= pygame.transform.scale(recorte3, viewsSizes[2]) #re-dimensiono

                view.blit(recorte, (0,0))
                view2.blit(recorte2, (0,0))
                view3.blit(recorte3, (0,0))
                view4 = pygame.Surface(self.sizePlayer)
                
                self.screen.blit(view, viewsPositions[0])#es la vista
                self.screen.blit(view2, viewsPositions[1])#es la vista
                self.screen.blit(view3, viewsPositions[2])#es la vista
                self.screen.blit(view4, viewsPositions[3])#ventana negra

                Views.marginView(self.screen, 3)
                
            elif self.numPlayers==4:
                
                view = pygame.Surface(self.sizePlayer)
                view2 = pygame.Surface(self.sizePlayer)
                view3 = pygame.Surface(self.sizePlayer)
                view4 = pygame.Surface(self.sizePlayer)
                
                if (Views.varListforViews[0][4]== 0 and Views.varListforViews[0][5]==0 ) :
                    Views.createXandYprev( self.playerList[0],0)
                if (Views.varListforViews[1][4]== 0 and Views.varListforViews[1][5]==0 ) :
                    Views.createXandYprev( self.playerList[1],1)
                if (Views.varListforViews[2][4]== 0 and Views.varListforViews[2][5]==0 ) :
                    Views.createXandYprev( self.playerList[2],1) 
                if (Views.varListforViews[3][4]== 0 and Views.varListforViews[3][5]==0 ) :
                    Views.createXandYprev( self.playerList[3],1) 
                    
                Views.varListforViews[0][2] = self.playerList[0].getPositionX()  
                Views.varListforViews[0][3] = self.playerList[0].getPositionY() 
                   
                Views.varListforViews[1][2] = self.playerList[1].getPositionX()  
                Views.varListforViews[1][3] = self.playerList[1].getPositionY()
                
                Views.varListforViews[2][2] = self.playerList[2].getPositionX()  
                Views.varListforViews[2][3] = self.playerList[2].getPositionY() 
                   
                Views.varListforViews[3][2] = self.playerList[3].getPositionX()  
                Views.varListforViews[3][3] = self.playerList[3].getPositionY()
             
                recorte= self.screen.subsurface(Views.movCamera(0))
                recorte2= self.screen.subsurface(Views.movCamera(1))
                recorte3= self.screen.subsurface(Views.movCamera(2))
                recorte4= self.screen.subsurface(Views.movCamera(3))
                
                recorte= pygame.transform.scale(recorte, viewsSizes[2]) #redimiension
                recorte2= pygame.transform.scale(recorte2, viewsSizes[2]) #redimiension
                recorte3= pygame.transform.scale(recorte3, viewsSizes[2]) #redimiension
                recorte4= pygame.transform.scale(recorte4, viewsSizes[2]) #redimiension
                
                view.blit(recorte, (0,0))
                view2.blit(recorte2, (0,0))
                view3.blit(recorte3, (0,0))
                view4.blit(recorte4, (0,0))
                
                self.screen.blit(view, viewsPositions[0])#es la vista
                self.screen.blit(view2, viewsPositions[1])#es la vista
                self.screen.blit(view3, viewsPositions[2])#es la vista
                self.screen.blit(view4, viewsPositions[3])#ventana negra

                Views.marginView(self.screen, 4)    
           
    def marginView(screen, numViews):
        color_white=(255,255,255)   
        if numViews==2:
            pygame.draw.line(screen,color_white,(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),3)
        if numViews>2:
            pygame.draw.line(screen,color_white,(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),3)
            pygame.draw.line(screen,color_white,(0,SCREEN_HEIGHT/2),(SCREEN_WIDTH,SCREEN_HEIGHT/2),3)    

   
 