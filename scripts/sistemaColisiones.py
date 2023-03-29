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

def colisionCollider(colision: list):
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

    if colision:
         print("colision")