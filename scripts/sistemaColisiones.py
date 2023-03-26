import pygame
import scripts.setting as setting
import scripts.jugador as jugador

def movimiento(colision: bool):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def colisionTrigger(puerta: pygame.Rect,player: pygame.Rect):
        if player.right >= setting.SCREEN_WIDTH or player.left <=0:
            movimiento(False)
        if player.bottom >= setting.SCREEN_HEIGHT or player.top <=0:
            movimiento(False)

        toleranciaColision = 10
        if player.colliderect(puerta):
            if((puerta.top - player.bottom) < toleranciaColision):
                movimiento(False)
            if((puerta.bottom - player.top) < toleranciaColision):
                movimiento(False)
            if((puerta.right - player.left) < toleranciaColision):
                movimiento(False)
            if((puerta.left - player.right) < toleranciaColision):
                movimiento(False)

def colisionCollider(muro: pygame.Rect,player: pygame.Rect):
    if player.right >= setting.SCREEN_WIDTH or player.left <=0:
        movimiento(False)
    if player.bottom >= setting.SCREEN_HEIGHT or player.top <=0:
        movimiento(False)

    toleranciaColision = 40
    if player.colliderect(muro):
        if(abs(muro.top - player.bottom) < toleranciaColision):
            print(muro.top-player.bottom)
            movimiento(False)
        if(abs(muro.bottom - player.top) < toleranciaColision):
            print(muro.bottom - player.top)
            movimiento(False)
        if(abs(muro.right - player.left) < toleranciaColision):
            print(muro.right - player.left)
            movimiento(False)
        if(abs(muro.left - player.right) < toleranciaColision):
            print(muro.left - player.right)
            movimiento(False)        