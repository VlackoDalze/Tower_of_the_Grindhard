import pygame
import typing

from pygame.math import Vector2


class UI_fragment(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position: typing.Union[Vector2, typing.Tuple[int, int]]):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.ui_image = ui_image
        self.position = position

    def draw(self):
        if isinstance(self.position, tuple):
            self.screen.blit(self.ui_image, self.position)
        else:
            self.screen.blit(self.ui_image, self.position.xy)
