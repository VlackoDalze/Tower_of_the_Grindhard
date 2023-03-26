import pygame
import scripts.setting as setting

def movimiento(colision: bool=True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movimiento_izquierda = colision
            if event.key == pygame.K_d :
                movimiento_derecha = colision
            if event.key == pygame.K_w :
                movimiento_arriba = colision
            if event.key == pygame.K_s :
                movimiento_abajo = colision
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a :
                movimiento_izquierda = colision
            if event.key == pygame.K_d :
                movimiento_derecha = colision
            if event.key == pygame.K_w :
                movimiento_arriba = colision
            if event.key == pygame.K_s :
                movimiento_abajo = colision

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :
                movimiento_izquierda = colision
            if event.key == pygame.K_RIGHT :
                movimiento_derecha = colision
            if event.key == pygame.K_UP :
                movimiento_arriba = colision
            if event.key == pygame.K_DOWN :
                movimiento_abajo = colision

def colision(muro,player):
        if player.right >= setting.SCREEN_WIDTH or player.left <=0:
            movimiento(False)
        if player.bottom >= setting.SCREEN_HEIGHT or player.top <=0:
            movimiento(False)
            
        toleranciaColision = 10
        if player.colliderect(muro):
            if(abs(muro.top - player.bottom) < toleranciaColision):
                movimiento(False)
            if(abs(muro.bottom - player.top) < toleranciaColision):
                movimiento(False)
            if(abs(muro.right - player.left) < toleranciaColision):
                movimiento(False)
            if(abs(muro.left - player.right) < toleranciaColision):
                movimiento(False)

        