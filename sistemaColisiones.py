import pygame

def movimiento(colision: bool):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            movimiento_izquierda = True
        if event.key == pygame.K_d :
            movimiento_derecha = True
        if event.key == pygame.K_w :
            movimiento_arriba = True
        if event.key == pygame.K_s :
            movimiento_abajo = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a :
            movimiento_izquierda = False
        if event.key == pygame.K_d :
            movimiento_derecha = False
        if event.key == pygame.K_w :
            movimiento_arriba = False
        if event.key == pygame.K_s :
            movimiento_abajo = False

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT :
            movimiento_izquierda = False
        if event.key == pygame.K_RIGHT :
            movimiento_derecha = False
        if event.key == pygame.K_UP :
            movimiento_arriba = False
        if event.key == pygame.K_DOWN :
            movimiento_abajo = False

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        muro = pygame.sprite.spritecollide()
        if muro:
            movimiento(False)
        else:
            movimiento(True)

        