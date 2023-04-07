from pygame.locals import *
import pygame
import typing
import re

from pygame.math import Vector2, Vector3
from scripts.setting import SILVER_MEDIUM_FONT
WHITE = (255, 255, 255)
RECT_WIDTH = 2


class Ui_fragment(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.percentage = False
        self.fragment_list = []
        self.position_x, self.position_y = 0, 0

    def drawListFragments(self):
        for fragment in self.fragment_list:
            fragment.draw()

    def addFragment(self, *fragment_list):
        for fragment in fragment_list:
            self.fragment_list.append(fragment)

    def getScreen(self):
        return self.screen

    # Pintar la superficie de la imagen con el color deseado
    @staticmethod
    def getMultiplyColorTexture(texture: pygame.Surface, color: typing.Union[Vector3, typing.Tuple[int, int, int]]):
        return texture.fill(color, special_flags=pygame.BLEND_MULT)


class Complex_fragment(Ui_fragment):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position):
        super().__init__(screen)
        self.ui_image = ui_image
        self.position = Vector2(0, 0)
        if isinstance(position[0], int) and isinstance(position[1], int):
            self.position = Vector2(position[0], position[1])
        elif isinstance(position[0], str) and isinstance(position[1], str):
            if (('%' in position[0]) and ('%' in position[1])):
                self.percentage = True
                self.position = Vector2(float(position[0].removesuffix(
                    '%')), float(position[1].removesuffix('%')))
            else:
                self.position = Vector2(float(position[0]), float(position[1]))
        if self.percentage:
            self.position_x, self.position_y = self.screen.get_height() * (self.position.x /
                                                                           100), self.screen.get_width() * (self.position.y/100)
        else:
            self.position_x, self.position_y = self.position.x, self.position.y

    def draw(self):
        if isinstance(self.position, tuple):
            self.screen.blit(self.ui_image, self.position)
        else:
            self.screen.blit(self.ui_image, self.position.xy)


class Interactable_fragment(Complex_fragment):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position: typing.Union[Vector2, typing.Tuple[int, int]]):
        super().__init__(screen, ui_image, position)

    def getPosition(self):
        return self.position


class Panel_fragment(Complex_fragment):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position: typing.Union[Vector2, typing.Tuple[str, str]], area: typing.Union[Vector2, typing.Tuple[int, int]] = (100, 100)):
        super().__init__(screen, ui_image, position)
        self.area = Vector2(area[0], area[1])

    def draw(self):
        x, y = self.position_x, self.position_y
        self.ui_image = pygame.transform.scale(self.ui_image, self.area)
        self.screen.blit(self.ui_image, (x, y))


class Button_fragment(Complex_fragment):
    def __init__(self, screen: pygame.Surface, ui_image: pygame.Surface, position: typing.Union[Vector2, typing.Tuple[str, str]]):
        super().__init__(screen, ui_image, position)

    def onClick(self):
        print("Pressed")


class Text_area_fragment(Ui_fragment):
    def __init__(self, screen: pygame.Surface, text: str, size: int, position: typing.Union[Vector2, typing.Tuple[str, str]], area: typing.Union[Vector2, typing.Tuple[int, int]] = (100, 100), margin=(0, 0, 0, 0), global_color: typing.Union[Vector3, typing.Tuple[int, int, int]] = WHITE, show_text_area: bool = False):
        super().__init__(screen)
        self.text = text
        self.size = size
        if (('%' in position[0]) and ('%' in position[1])):
            self.percentage = True
            self.position = Vector2(float(position[0].removesuffix(
                '%')), float(position[1].removesuffix('%')))
        else:
            self.position = Vector2(float(position[0]), float(position[1]))
        self.area = Vector2(area[0], area[1])
        self.font = pygame.font.Font(SILVER_MEDIUM_FONT, self.size)
        self.show_text_area = show_text_area
        self.color = global_color
        self.margin_left = margin[0]
        self.margin_top = margin[1]
        self.margin_right = margin[2]
        self.margin_bottom = margin[3]

    def draw(self):
        if self.percentage:
            x, y = self.screen.get_height() * (self.position.x /
                                               100), self.screen.get_width() * (self.position.y/100)
        else:
            x, y = self.position.x, self.position.y
        initial_x, initial_y = x, y
        color_area = False
        color = self.color
        initial_color = color
        # Crea una lista 2D donde cada fila es una lista de palabras.
        words = [word.split(' ') for word in self.text.splitlines()]
        space = self.font.size(' ')[0]  # El ancho de un espacio.
        # El ancho y la altura máxima del área de escritura del texto.
        max_width, max_height = self.area.x + initial_x, self.area.y + initial_y
        # Expresiones irregular de la etiqueta
        color_tag_match = r"^<color\(\d{1,3},\d{1,3},\d{1,3}\)>.*$"
        # Posiciones iniciales de las líneas de texto.
        for line in words:
            x += self.margin_left
            y += self.margin_top
            for word in line:
                word_color_finished = False
                color = initial_color
                # Busca una cadena que comienza con "<color(\d,\d,\d)>" y termina con cualquier carácter.
                color_match = re.match(color_tag_match, word)
                if color_match:
                    color_area = True
                    color_tag = word.split('>')[0]
                    color_tag += '>'
                    color_values = re.findall(r'\d+', color_tag)
                    red, green, blue = int(color_values[0]), int(
                        color_values[1]), int(color_values[2])
                    word = word.removeprefix(color_tag)
                if word.endswith('</color>'):
                    word_color_finished = True
                    word = word.removesuffix('</color>')
                if color_area:
                    color = Vector3(red, green, blue)
                word_surface = self.font.render(word, True, color)
                if word_color_finished:
                    color_area = False
                word_width, word_height = word_surface.get_size()
                if (x + word_width) >= max_width - self.margin_right:
                    x = initial_x + self.margin_left  # Reinicia x.
                    y += word_height  # Comienza una nueva fila.
                self.screen.blit(word_surface, (x, y))
                x += (word_width + space)
            x = initial_x  # Reinicia x.
            y += word_height  # Comienza una nueva fila.
        if (self.show_text_area):
            pygame.draw.rect(self.screen, WHITE, (initial_x,
                             initial_y, self.area.x, self.area.y), RECT_WIDTH)
