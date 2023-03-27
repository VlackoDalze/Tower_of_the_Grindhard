import pygame
import scripts.setting as setting
from scripts.jugador import Jugador

# def movimiento(colision: bool):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

def colisionTrigger(puerta: pygame.Rect,player: pygame.Rect,trigger: str):
        if player.colliderect(puerta):
            if trigger=="puerta":
                print("Siguiente nivel")
            else:
                print("Cofre abierto")

def colisionCollider(muro: pygame.Rect,player: pygame.Rect, jug: Jugador):
    # if player.right >= setting.SCREEN_WIDTH or player.left <=0:
    #     if player.left <=0:
    #         jug.setPosX(32)
    #     else:
    #         jug.setPosX(setting.SCREEN_WIDTH-32*2)
    # if player.bottom >= setting.SCREEN_HEIGHT or player.top <=0:
    #     if player.top <=0:
    #         jug.setPosY(32)
    #     else:
    #         jug.setPosY(setting.SCREEN_HEIGHT-32*2)
    
    x = jug.getPosX()
    y = jug.getPosY()

    if player.colliderect(muro):
        if(abs(player.bottom - muro.top)<40):
            jug.setPosX(x)
            jug.setPosY(y)
        if(abs(player.top - muro.bottom)<40):
            jug.setPosX(x)
            jug.setPosY(y+32)
        if(abs(player.left - muro.right)<40):
            jug.setPosX(x-32)
            jug.setPosY(y-32)
        if(abs(player.right - muro.left)<40):
            jug.setPosX(x+32)
            jug.setPosY(y-32)