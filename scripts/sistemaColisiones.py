import pygame

def movimiento(event,colision: bool):
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

def colision(muro,col):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if muro.colliderect(col):
            movimiento(event,False)
        else:
            movimiento(event,True)

        