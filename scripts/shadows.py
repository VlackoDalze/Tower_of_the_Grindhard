import pygame
import scripts.setting as setting

from scripts.collider_matrix_maker import get_collider_matrix

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT

class Shadows(object):
    
    list_shadows=[]
    shadows_y=[]
    shadows_X=[]
    
    def shadowsY(scene_level):
        
        map_collider_matriz=get_collider_matrix(scene_level)
        eje_y = 0  # eje y  
        cont_y=0
        shadows_y=[]
        
        #trackero de muros, más de 9 muros, crea una sombra horizontal
        for row in map_collider_matriz:
            for column in row:
                
                if (column == '1'):  # colision
                    cont_y+=1
                    if cont_y>9:
                        shadows_y.append(eje_y)
                        break          
                else: 
                    cont_y=0
                    
            eje_y+=CELL_SIZE  # aumenta y+32
            cont_y=0 
            
        return shadows_y

    def shadowsX(shadows_y,scene_level):
    
        map_collider_matriz=get_collider_matrix(scene_level)
        eje_x=0
        cont_x=0
        shadows_x=[]
        shadows_x_row=[]
        
        #trackero de muros, más de 9 muros, crea una sombra vertical
        for  i in range(0,len(shadows_y)-1):
            
            valueRow=int(shadows_y[i]/CELL_SIZE)
            limitColumn=int(SCREEN_WIDTH/CELL_SIZE)
            eje_x=0
            shadows_x_row.clear()
            
            for h in range(0,limitColumn):
                for j in range(0,4):
                    
                    if ( map_collider_matriz[valueRow+j][eje_x] == '1'): # colision
                        cont_x+=1 
            
                    if cont_x>2:
                        shadows_x_row.append([valueRow,eje_x])
                        break
                    
                if eje_x<limitColumn:  
                    eje_x+=1
                    cont_x=0
            
            aux_list=shadows_x_row.copy()
            shadows_x.append(aux_list)
        if len(Shadows.list_shadows)==0: 
            aux_list_shadows=[]
            
            for i in shadows_x:
                aux_list_shadows.clear()
                for j in reversed(range(len(i)-1)):
                    aux_list_shadows.append(False)
                aux_list=aux_list_shadows.copy()
                Shadows.list_shadows.append(aux_list) 
            
        return shadows_x 
    
    def verificationListShadows():
           
        for i in Shadows.list_shadows:
            for j in reversed(range(len(i)-1)):
                if not j:
                    return False

        return True
            
    #dibujado de sombras
    def drawShadows(screen:pygame.Surface,players_list,scene_level):
        
        if len(Shadows.shadows_y)==0:
            shadows_y=Shadows.shadowsY(scene_level)
            shadows_x=Shadows.shadowsX(shadows_y,scene_level)
              
        index_shadows_y=0  
        
            
        #dibuja cuadrado por cuadrado de cada fila
    
        column_bloqued=False
        no_draw=False
     
       
        if not Shadows.verificationListShadows():
        
            for fila in shadows_x: 
                
                row_bloqued=False
                index_list_shadows=0
                limit_shadows_x=0
              
                for i in reversed(range(len(fila)-1)):
                    
                    if len(players_list)==1:
        
                        if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[0].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued :
                                
                            no_draw=True

                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1] and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:
                                alpha=250 
                                no_draw=False  
                                    
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]:
                                row_bloqued=True
                                column_bloqued=True 
                                
                        else: 
                            
                            if Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:
                                
                                no_draw=True
                            else:
                                
                                alpha=250
                                no_draw=False
                                 
                    #fin  1 player
                    
                    elif len(players_list)==2:
                    
                        if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[0].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued or players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[1].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued :
                                
                            no_draw=True
                            
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1] and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:

                                alpha=250
                                no_draw=False 
                                
                                if  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and players_list[0].getPositionY()<shadows_y[index_shadows_y+1] and players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                    or  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and players_list[1].getPositionY()<shadows_y[index_shadows_y+1] and players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE:
                                    no_draw=True
                                    # alpha=0
                                    # no_draw=False
                                 
                                if  players_list[0].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[1].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1]:
                                    no_draw=True
                                    # alpha=120
                                    # no_draw=False
                                    
                            #inicio de trackeo, 1 recuadros en blanco -ubicacion de los personajes   
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]:

                                row_bloqued=True
                                column_bloqued=True 
                                limit_shadows_x=fila[i][1]*CELL_SIZE
          
                        else: 
                            
                            if Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:

                                no_draw=True
                                # alpha=75
                                # no_draw=False
                                
                            else:
                                
                                if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE  and fila[i][1]*CELL_SIZE<limit_shadows_x \
                                    or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x:

                                        if  players_list[0].getPositionY()<shadows_y[index_shadows_y] or players_list[1].getPositionY()<shadows_y[index_shadows_y]:

                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] \
                                                and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and  players_list[1].getPositionY()>=shadows_y[index_shadows_y]\
                                                and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE :
                                                # alpha=100
                                                # no_draw=False
                                                no_draw=True
                                            else:
                                                alpha=250
                                                no_draw=False 
                                                
                                        elif players_list[0].getPositionY()>shadows_y[index_shadows_y] \
                                            or players_list[1].getPositionY()>shadows_y[index_shadows_y] \
                                            :
                                                
                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                                :
                                                  
                                                no_draw=True
                                                
                                            else:
                                                
                                                alpha=250
                                                no_draw=False      
                                        else: 
                                            
                                            Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]=True
                                            no_draw=True
                                            # alpha=50
                                            # no_draw=False
                                               
                                else:
  
                                        alpha=250
                                        no_draw=False
                                        
                    #fin  2 player
                    
                    elif len(players_list)==3:
                        
                        if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[0].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued \
                            or players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[1].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued \
                            or players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[2].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued:
                                
                            no_draw=True
                            
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:

                                alpha=250
                                no_draw=False 
                                
                                if  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                    or  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                    or  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE   :

                                    no_draw=True
                                    # alpha=0
                                    # no_draw=False
                                 
                                if  players_list[0].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[1].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[2].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1]:

                                    no_draw=True
                                    # alpha=200
                                    # no_draw=False
                                    
                            #inicio de trackeo, 1 recuadros en blanco -ubicacion de los personajes   
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[2].getPositionY()<shadows_y[index_shadows_y+1]:

                                row_bloqued=True
                                column_bloqued=True 
                                limit_shadows_x=fila[i][1]*CELL_SIZE
          
                        else: 
                            
                            if Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows] :

                                no_draw=True
                         
                                # alpha=100
                                # no_draw=False
                                
                    
                            else:
                                
                                if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE  and fila[i][1]*CELL_SIZE<limit_shadows_x \
                                    or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x\
                                    or players_list[2].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x  :

                                        if  players_list[0].getPositionY()<shadows_y[index_shadows_y] \
                                            or players_list[1].getPositionY()<shadows_y[index_shadows_y] \
                                            or players_list[2].getPositionY()<shadows_y[index_shadows_y]:

                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                                or players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] :
                                                  
                                                no_draw=True
                                                # alpha=100
                                                # no_draw=False
                                                
                                            else:
                                                
                                                alpha=250
                                                no_draw=False 
                                                
                                        elif players_list[0].getPositionY()>shadows_y[index_shadows_y] \
                                            or players_list[1].getPositionY()>shadows_y[index_shadows_y] \
                                            or players_list[2].getPositionY()>shadows_y[index_shadows_y]:
                                                
                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                                or players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] :
                                                  
                                                no_draw=True
                                                
                                            else:
                                                
                                                alpha=250
                                                no_draw=False  
                                                   
                                        else: 
                                            
                                            Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]=True
                                            #no_draw=True
                                            # alpha=50
                                            #no_draw=False
                                               
                                else:
  
                                        alpha=250
                                        no_draw=False
                                
                    #fin  3 player
                    
                    elif len(players_list)==4:
                        
                        if players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[0].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued \
                            or players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[1].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued \
                            or players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[2].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued\
                            or players_list[3].getPositionY()<shadows_y[index_shadows_y+1] \
                            and  players_list[3].getPositionX()>=fila[i][1]*CELL_SIZE \
                            and not row_bloqued:
                                
                            no_draw=True
                            
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]\
                                or  players_list[3].getPositionY()<shadows_y[index_shadows_y+1] \
                                and column_bloqued and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:

                                alpha=250
                                no_draw=False 
                                
                                if  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and players_list[0].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                    or  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                    or  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE \
                                    or  players_list[3].getPositionY()>=shadows_y[index_shadows_y] and players_list[3].getPositionY()<shadows_y[index_shadows_y+1] \
                                    and players_list[3].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[3].getPositionX()>fila[i][1]*CELL_SIZE :

                                    no_draw=True
                                    # alpha=0
                                    # no_draw=False
                                 
                                if  players_list[0].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[1].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[2].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1]\
                                    or  players_list[3].getPositionX()==fila[i][1]*CELL_SIZE and  players_list[3].getPositionY()>=shadows_y[index_shadows_y] \
                                    and  players_list[3].getPositionY()<shadows_y[index_shadows_y+1]:

                                    no_draw=True
                                    # alpha=200
                                    # no_draw=False
                                    
                            #inicio de trackeo, 1 recuadros en blanco -ubicacion de los personajes   
                            if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[2].getPositionY()<shadows_y[index_shadows_y+1]\
                                or players_list[3].getPositionY()<shadows_y[index_shadows_y+1]:

                                row_bloqued=True
                                column_bloqued=True 
                                limit_shadows_x=fila[i][1]*CELL_SIZE
          
                        else: 
                            
                            if Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows] :

                                no_draw=True
                         
                                # alpha=100
                                # no_draw=False
                                
                    
                            else:
                                
                                if  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE  and fila[i][1]*CELL_SIZE<limit_shadows_x \
                                    or players_list[1].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x\
                                    or players_list[2].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x \
                                    or players_list[3].getPositionY()<shadows_y[index_shadows_y+1]  and  players_list[3].getPositionX()<fila[i+1][1]*CELL_SIZE and fila[i][1]*CELL_SIZE<limit_shadows_x :

                                        if  players_list[0].getPositionY()<shadows_y[index_shadows_y] \
                                            or players_list[1].getPositionY()<shadows_y[index_shadows_y] \
                                            or players_list[2].getPositionY()<shadows_y[index_shadows_y]\
                                            or players_list[3].getPositionY()<shadows_y[index_shadows_y]:

                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                                or players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1]\
                                                or players_list[3].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[3].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[3].getPositionY()>=shadows_y[index_shadows_y] and  players_list[3].getPositionY()<shadows_y[index_shadows_y+1]:
                                                  
                                                no_draw=True
                                                # alpha=100
                                                # no_draw=False
                                                
                                            else:
                                                
                                                alpha=250
                                                no_draw=False 
                                                
                                        elif players_list[0].getPositionY()>shadows_y[index_shadows_y] \
                                            or players_list[1].getPositionY()>shadows_y[index_shadows_y] \
                                            or players_list[2].getPositionY()>shadows_y[index_shadows_y]\
                                            or players_list[3].getPositionY()>shadows_y[index_shadows_y]:
                                                
                                            if  players_list[0].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[0].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[0].getPositionY()>=shadows_y[index_shadows_y] and  players_list[0].getPositionY()<shadows_y[index_shadows_y+1]  \
                                                or players_list[1].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[1].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[1].getPositionY()>=shadows_y[index_shadows_y] and  players_list[1].getPositionY()<shadows_y[index_shadows_y+1] \
                                                or players_list[2].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[2].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[2].getPositionY()>=shadows_y[index_shadows_y] and  players_list[2].getPositionY()<shadows_y[index_shadows_y+1] \
                                                or players_list[3].getPositionX()<fila[i+1][1]*CELL_SIZE and players_list[3].getPositionX()>fila[i][1]*CELL_SIZE\
                                                and  players_list[3].getPositionY()>=shadows_y[index_shadows_y] and  players_list[3].getPositionY()<shadows_y[index_shadows_y+1] :
                                                  
                                                no_draw=True
                                                
                                            else:
                                                
                                                alpha=250
                                                no_draw=False  
                                                   
                                        else: 
                                            
                                            Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]=True
                                            #no_draw=True
                                            # alpha=50
                                            #no_draw=False
                                               
                                else:
  
                                        alpha=250
                                        no_draw=False
          
                    #fin 4 player  

                    if not no_draw:
                        if i==len(fila)-2 and index_shadows_y==len(shadows_y)-2: 
                            shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE+CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]+CELL_SIZE))
                        elif i==len(fila)-2:
                            shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE+CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]))
                        elif index_shadows_y==len(shadows_y)-2:
                            shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]+CELL_SIZE))
                        else:
                            shadow=pygame.Surface(((fila[i+1][1]-fila[i][1])*CELL_SIZE,shadows_y[index_shadows_y+1]-shadows_y[index_shadows_y]))  
                            
                        shadow.set_alpha(alpha)   
                        screen.blit(shadow,(fila[i][1]*CELL_SIZE,fila[i][0]*CELL_SIZE))
                    
                    if  no_draw and not Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows]:
                        Shadows.list_shadows[index_shadows_y][len(Shadows.list_shadows[index_shadows_y])-1-index_list_shadows] =True
                        no_draw=False
                        
                    index_list_shadows+=1
                    
                index_shadows_y+=1
    