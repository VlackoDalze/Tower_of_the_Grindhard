import pygame
import scripts.setting as setting


class Torch(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, pos_x: int, pos_y: int):
        super().__init__()
        self.screen = screen
        self.torch_sprites = []
        self.torch_sprites.append(pygame.image.load(
            'assets/dungeon/wall/torches/torch_1.png'))
        self.torch_sprites.append(pygame.image.load(
            'assets/dungeon/wall/torches/torch_2.png'))
        self.torch_sprites.append(pygame.image.load(
            'assets/dungeon/wall/torches/torch_3.png'))
        self.torch_sprites.append(pygame.image.load(
            'assets/dungeon/wall/torches/torch_4.png'))
        # self.current_torch = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def getX(self):
        return self.pos_x* setting.CELL_SIZE
    def getY(self):
        return self.pos_y* setting.CELL_SIZE
    
    def drawTorch(self, current_torch: int):
        self.screen.blit(self.torch_sprites[current_torch], (self.pos_x *
                                                             setting.CELL_SIZE, self.pos_y*setting.CELL_SIZE))

    @staticmethod  # método estático
    def get_torch_sprites_length():
        return len(Torch(None, None, None).torch_sprites)
