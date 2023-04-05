import pygame
import typing

from pygame.math import Vector2, Vector3

class UI_fragment(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position: typing.Union[Vector2, typing.Tuple[int, int]]):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ui_image = ui_image
        self.position = position

    def draw(self):
        if isinstance(self.position, tuple):
            self.screen.blit(self.ui_image, self.position)
        else:
            self.screen.blit(self.ui_image, self.position.xy)

    # Pintar la superficie de la imagen con el color deseado
    def getMultiplyColorTexture(self, texture: pygame.Surface, color: typing.Union[Vector3, typing.Tuple[int, int, int]]):
        return texture.fill(color, special_flags=pygame.BLEND_MULT)