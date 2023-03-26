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
                movimiento_izquierda = not colision
            if event.key == pygame.K_d :
                movimiento_derecha = not colision
            if event.key == pygame.K_w :
                movimiento_arriba = not colision
            if event.key == pygame.K_s :
                movimiento_abajo = not colision

def colision(muro: pygame.Rect,player: pygame.Rect,eje_x: int,eje_y: int):
        player.x += eje_x
        player.y += eje_y

        if player.right >= setting.SCREEN_WIDTH or player.left <=0:
            eje_x *= -1
            movimiento(False)
        if player.bottom >= setting.SCREEN_HEIGHT or player.top <=0:
            eje_y *= -1
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

        