import pygame
class vistas:
    def __init__(self, width=None, height=None,players=None):
        self.width = width
        self.height = height
        self.players = players

    def PlayerView(self, player):
        pygame.Surface(self.width, self.height)
        