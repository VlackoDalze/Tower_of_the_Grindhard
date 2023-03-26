import pygame,sys

pygame.init()
clock = pygame.time.Clock()
screen_width,screen_height = 800,800
screen = pygame.display.set_mode((screen_width,screen_height))

def bouncing():
    global x_speed,y_speed
    rect.x += x_speed
    rect.y += y_speed
    
    pygame.draw.rect(screen,(255,255,255),rect)
    pygame.draw.rect(screen,(255,0,0),rect2)

    if rect.right >= screen_width or rect.left <=0:
        x_speed *= -1
    if rect.bottom >= screen_height or rect.top <=0:
        y_speed *= -1

    toleranciaColision = 10
    if rect.colliderect(rect2):
            if((rect2.top - rect.bottom) < toleranciaColision):
                y_speed *= -1
            if((rect2.bottom - rect.top) < toleranciaColision):
                y_speed *= -1
            if((rect2.right - rect.left) < toleranciaColision):
                x_speed *= -1
            if((rect2.left - rect.right) < toleranciaColision):
                x_speed *= -1

rect = pygame.Rect(350,350,100,100)
x_speed,y_speed = 5,4

rect2 = pygame.Rect(300,600,200,100)
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    
    bouncing()
    pygame.display.flip()
    clock.tick(60)
