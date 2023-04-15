import pygame
import scripts.setting as setting
from scripts.torch import Torch
from scripts.collider_matrix_maker import get_collider_matrix

# Variables statics
CELL_SIZE = setting.CELL_SIZE
SCREEN_WIDTH = setting.SCREEN_WIDTH
SCREEN_HEIGHT = setting.SCREEN_HEIGHT


class Shadows2(object):
    list_of_shadows =[]
    onShadows = False
    aux_list_of_shadows =[]#shadow + alpha
    shadows_torch=False
    screen=None
    scene=None
    shadow=pygame.Surface((CELL_SIZE,CELL_SIZE))
    aux_list_shadows_removed=[]
    list_walls=[]
    def drawAllShadows(scene_level):
        map_collider_matriz = get_collider_matrix(scene_level)
        eje_x = 0  # eje x
        eje_y = 0  # eje y

        for row in map_collider_matriz:
            for column in row:

               # if (column == '1'  or column == '4'):  # colision murosy adornos
                Shadows2.list_of_shadows.append(str(eje_x)+"-"+str(eje_y))
                if column=='1' and str(eje_x)+"-"+str(eje_y) not in Shadows2.list_walls:
                    #Shadows2.list_walls.append(str(eje_x)+"-"+str(eje_y))#muro
                    wall=str(eje_x)+"-"+str(eje_y)
                    Shadows2.list_walls.append(wall)#muro
                    # if eje_x+CELL_SIZE<=SCREEN_WIDTH:
                    #     Shadows2.list_walls.append(str(eje_x+CELL_SIZE)+"-"+str(eje_y))#muro
                    # if eje_x-CELL_SIZE>=CELL_SIZE:
                    #     Shadows2.list_walls.append(str(eje_x-CELL_SIZE)+"-"+str(eje_y))#muro
                    # if eje_y+CELL_SIZE<=SCREEN_HEIGHT:
                    #     Shadows2.list_walls.append(str(eje_x)+"-"+str(eje_y+CELL_SIZE))#muro
                    # if eje_y-CELL_SIZE>=CELL_SIZE:
                    #     Shadows2.list_walls.append(str(eje_x)+"-"+str(eje_y-CELL_SIZE))#muro
                eje_x = eje_x + CELL_SIZE  # aumenta x +32

            eje_y = eje_y + CELL_SIZE  # aumenta y+32
            eje_x = 0  # resets x
            
    def iluminationArea(position:str,isplayer:bool):
        aux=position.split('-')
        ejex=int(aux[0])
        ejey=int(aux[1])
        cell=aux[0]+"-"+aux[1]
        area=[cell]
        area2=[]
        #normales
        if ejex>=CELL_SIZE:
            left_cell=str(ejex-CELL_SIZE)+"-"+aux[1]    
            area.append(left_cell)
            
        if ejex+CELL_SIZE<=SCREEN_WIDTH:  
            rigth_cell=str(ejex+CELL_SIZE)+"-"+aux[1]
            area.append(rigth_cell)
            
        if ejey+CELL_SIZE<=SCREEN_HEIGHT:
            down_cell=aux[0]+"-"+str(ejey+CELL_SIZE)
            area.append(down_cell)
            
        if ejey>=CELL_SIZE and isplayer:
            up_cell=aux[0]+"-"+str(ejey-CELL_SIZE)
            area.append(up_cell)
        #dobles
        if ejex>=CELL_SIZE*2:
            left_left_cell=str(ejex-CELL_SIZE*2)+"-"+aux[1]    
            area2.append(left_left_cell)
            
        if ejex+CELL_SIZE*2<=SCREEN_WIDTH:  
            rigth_rigth_cell=str(ejex+CELL_SIZE*2)+"-"+aux[1]
            area2.append(rigth_rigth_cell)
            
        if ejey+CELL_SIZE*2<=SCREEN_HEIGHT:
            down_down_cell=aux[0]+"-"+str(ejey+CELL_SIZE*2)
            area2.append(down_down_cell)
            
        if ejey>=CELL_SIZE*2 and isplayer:
            up_up_cell=aux[0]+"-"+str(ejey-CELL_SIZE*2)
            area2.append(up_up_cell)
        #esquinas  
        if ejex+CELL_SIZE<=SCREEN_WIDTH and ejey+CELL_SIZE<=SCREEN_HEIGHT:
            down_rigth_cell=str(ejex+CELL_SIZE)+"-"+str(ejey+CELL_SIZE)
            area2.append(down_rigth_cell)
            
        if ejex >=CELL_SIZE and ejey+CELL_SIZE<=SCREEN_HEIGHT:    
            down_left_cell=str(ejex-CELL_SIZE)+"-"+str(ejey+CELL_SIZE)
            area2.append(down_left_cell)

        if ejex+CELL_SIZE<=SCREEN_WIDTH and ejey>=CELL_SIZE and isplayer:
            up_rigth_cell=str(ejex+CELL_SIZE)+"-"+str(ejey-CELL_SIZE)
            area2.append(up_rigth_cell)
            
        if ejex >=CELL_SIZE and ejey>=CELL_SIZE  and isplayer:    
            up_left_cell=str(ejex-CELL_SIZE)+"-"+str(ejey-CELL_SIZE)
            area2.append(up_left_cell)

        for a in area:
            if  a in Shadows2.list_of_shadows:
                Shadows2.list_of_shadows.remove(a)         
            elif a  in Shadows2.aux_list_of_shadows:
                Shadows2.aux_list_of_shadows.remove(a)
            
        for a in area2:#que no permita ver detras de los muros
            if isplayer:
                aux_walls=Shadows2.limitShadowWalls(ejex,ejey)
                        
                if a not in aux_walls:
                    if  a in Shadows2.list_of_shadows:
                        Shadows2.list_of_shadows.remove(a)
                        if a not in Shadows2.aux_list_of_shadows:
                            Shadows2.aux_list_of_shadows.append(a)
            
    def limitShadowWalls(positionx,positiony):
        aux_list=[]
        
        if str(positionx+CELL_SIZE)+"-"+str(positiony) in Shadows2.list_walls: 
            aux_list.append(  str(positionx+CELL_SIZE*2)+"-"+str(positiony))
        if str(positionx-CELL_SIZE)+"-"+str(positiony) in Shadows2.list_walls: 
            aux_list.append(  str(positionx-CELL_SIZE*2)+"-"+str(positiony) )
        if str(positionx)+"-"+str(positiony+CELL_SIZE) in Shadows2.list_walls: 
            aux_list.append(  str(positionx)+"-"+str(positiony+CELL_SIZE*2))
        if str(positionx)+"-"+str(positiony-CELL_SIZE) in Shadows2.list_walls:     
            aux_list.append(   str(positionx)+"-"+str(positiony-CELL_SIZE*2))
        return aux_list
       
    def drawShadows2( players_list,list_torch):   
        
        if len(Shadows2.list_of_shadows)==0 and not Shadows2.onShadows:
            Shadows2.screen=players_list[0].getScreen()
            Shadows2.scene=players_list[0].getSceneLevel()
            Shadows2.drawAllShadows(Shadows2.scene)
            Shadows2.onShadows=False
            
        elif not Shadows2.shadows_torch:#rev
            for torch in list_torch:
                aux=str(torch.getX())+"-"+str(torch.getY())
                Shadows2.iluminationArea(aux,False)
            Shadows2.shadows_torch=True
            
        else:#code para jugadores
            for player in players_list:
                p_ejex=player.getPositionX()
                p_ejey=player.getPositionY() 
                aux=str(p_ejex)+"-"+str(p_ejey)
                Shadows2.iluminationArea(aux,True)

        Shadows2.drawDinamicShadows()

    def drawDinamicShadows():
            
        for s in Shadows2.list_of_shadows:
            aux=s.split('-')
            Shadows2.shadow.set_alpha(250)
            Shadows2.screen.blit(Shadows2.shadow,(int(aux[0]),int(aux[1])))
            
        for a_s in Shadows2.aux_list_of_shadows:
            aux=a_s.split('-')
            Shadows2.shadow.set_alpha(200)
            Shadows2.screen.blit(Shadows2.shadow,(int(aux[0]),int(aux[1])))