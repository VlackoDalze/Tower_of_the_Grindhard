from pygame.locals import *
import pygame
import typing
import re
from copy import copy
from scripts.setting import SCREEN_WIDTH, SCREEN_HEIGHT

from pygame.math import Vector2, Vector3
from scripts.setting import SILVER_MEDIUM_FONT, CELL_SIZE

WHITE = (255, 255, 255)
RECT_WIDTH = 2


def defaultMethod():
    print("Empty method")


class UiElement(pygame.sprite.Sprite):
    screen = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.percentage = False
        self.element_list = []

    def drawListElements(self):
        for element in self.element_list:
            if isinstance(element, Complex_element) or isinstance(
                element, TextElement
            ):
                if element.getElementList():
                    element.draw()
                    element.drawListElements()
                else:
                    element.draw()
            else:
                element.drawListElements()

    def addElement(self, *element_list):
        for element in element_list:
            self.element_list.append(element)

    def closeElement(self, *element_list):
        for element in element_list:
            if not self.element_list:
                self.element_list.remove(element)

    def containElement(self, Elements) -> bool:
        for element in self.element_list:
            if element == Elements:
                return True
        return False

    def getElementList(self) -> []:
        return self.element_list

    # Comprueba si la lista está vacío, en caso afirmativo devolverá True en caso contrario devolverá False, es decir, no está activo
    def isActive(self) -> bool:
        return self.element_list

    @staticmethod
    def setGlobalScreen(screen):
        UiElement.screen = screen

    @staticmethod
    def ElementsMatrixGroupMaker(
        element,
        position: typing.Union[Vector2, typing.Tuple[float, float]],
        amount: typing.Union[Vector2, typing.Tuple[int, int]],
        margin: typing.Tuple[float, float, float, float] = (0, 0, 0, 0),
        apply_initial_margin_X=False,
        apply_initial_margin_Y=False,
    ):
        element_group = UiElement()
        position_x = position[0]  # eje x
        position_y = position[1]  # eje y

        for row in range(amount[1]):
            if row > 0 or apply_initial_margin_Y:
                position_y = position_y + margin[1]
            for column in range(amount[0]):
                if column > 0 or apply_initial_margin_X:
                    position_x = position_x + margin[3]
                copy_element = copy(element)
                copy_element.setPosition((position_x, position_y))
                element_group.addElement(copy_element)
                position_x = position_x + CELL_SIZE + margin[0]  # aumenta x +32
            position_y = position_y + CELL_SIZE + margin[2]  # aumenta y+32
            position_x = position[0]  # resets x
        return element_group

    @staticmethod
    def clearElements(*element_group_list):
        for Elements in element_group_list:
            Elements.getElementList().clear()

    # Pintar la superficie de la imagen con el color deseado
    @staticmethod
    def getMultiplyColorTexture(
        texture: pygame.Surface,
        color: typing.Union[Vector3, typing.Tuple[int, int, int]],
    ):
        return texture.fill(color, special_flags=pygame.BLEND_MULT)

    @staticmethod
    def toggleElement(group_element, element):
        if not (group_element.containElement(element)):
            group_element.addElement(element)
        elif group_element.containElement(element):
            UiElement.clearElements(group_element)


class Complex_element(UiElement):
    def __init__(self, ui_image: pygame.Surface, position):
        super().__init__()
        self.ui_image = ui_image
        self.position = Vector2(0, 0)
        self.setPosition(position)

    def draw(self):
        if isinstance(self.position, tuple):
            UiElement.screen.blit(self.ui_image, self.position)
        else:
            UiElement.screen.blit(self.ui_image, self.position.xy)

    def getImageSize(self):
        return self.ui_image.get_size()

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        if (isinstance(position[0], float) or isinstance(position[0], int)) and (
            isinstance(position[1], int) or isinstance(position[1], float)
        ):
            self.position = Vector2(position[0], position[1])
        elif isinstance(position[0], str) and isinstance(position[1], str):
            if ("%" in position[0]) and ("%" in position[1]):
                self.position = Vector2(
                    (float(position[0].removesuffix("%")) / 100)
                    * UiElement.screen.get_width(),
                    (float(position[1].removesuffix("%")) / 100)
                    * UiElement.screen.get_height(),
                )
            else:
                self.position = Vector2(float(position[0]), float(position[1]))

    def getImage(self):
        return self.ui_image


#!Cancelado, no veo el como hacerlo y que no tiene tanta importancia como para dedicarle tanto tiempo
# class Interactable_element(Complex_element):
#     def __init__(
#         self,
#
#         ui_image: pygame.Surface,
#         position: typing.Union[Vector2, typing.Tuple[str, str]],
#     ):
#         super().__init__(screen, ui_image, position)
#         self.index = 0

#     def draw(self):
#         x, y = self.position.x, self.position.y
#         UiElement.screen.blit(self.ui_image, (x, y))
#         width, height = self.ui_image.get_size()
#         rect = (x, y, width, height)
#         pygame.draw.rect(UiElement.screen, WHITE, rect, 2)


class Panel_element(Complex_element):
    def __init__(
        self,
        ui_image: pygame.Surface,
        position: typing.Union[Vector2, typing.Tuple[str, str]],
        area: typing.Union[Vector2, typing.Tuple[int, int]] = (0, 0),
    ):
        super().__init__(ui_image, position)
        self.area = Vector2(area[0], area[1])
        if (self.area.x != 0) and (self.area.y != 0):
            self.ui_image = pygame.transform.scale(self.ui_image, self.area)

    def getArea(self):
        return self.area

    def draw(self):
        x, y = self.position.x, self.position.y
        UiElement.screen.blit(self.ui_image, (x, y))


class Button_element(Complex_element):
    eventList = []

    def __init__(
        self,
        ui_image: pygame.Surface,
        position: typing.Union[Vector2, typing.Tuple[str, str]],
        area: typing.Union[Vector2, typing.Tuple[int, int]],
        onClick=defaultMethod,
    ):
        super().__init__(ui_image, position)
        self.area = Vector2(area[0], area[1])
        self._pressed = False
        self.onClick = onClick

    def draw(self):
        x, y = self.position.x, self.position.y
        button_width, button_height = self.area.x, self.area.y
        self.ui_image = pygame.transform.scale(self.ui_image, self.area)
        UiElement.screen.blit(self.ui_image, (x, y))
        for event in Button_element.eventList:
            if event.type == pygame.MOUSEBUTTONDOWN and (self._pressed == False):
                mouse_pos = pygame.mouse.get_pos()
                if (
                    x < mouse_pos[0] < x + button_width
                    and y < mouse_pos[1] < y + button_height
                ):
                    self._pressed = True
                    self.onClick()
            if event.type == pygame.MOUSEBUTTONUP:
                self._pressed = False

    def setOnClick(self, onClick):
        self.onClick = onClick

    def getArea(self):
        return self.area

    @staticmethod
    def appendGlobalEventListener(event):
        Button_element.eventList.append(event)

    @staticmethod
    def clearGlobalEventListener():
        Button_element.eventList.clear()


class TextElement(UiElement):
    def __init__(
        self,
        text: str,
        textSize: int,
        position: typing.Union[Vector2, typing.Tuple[str, str]],
        area: typing.Union[Vector2, typing.Tuple[int, int]] = (100, 100),
        color: typing.Union[Vector3, typing.Tuple[int, int, int]] = WHITE,
        show_text_area: bool = False,
    ):
        super().__init__()
        self.text = text
        self.textSize = textSize
        self.setPosition(position)
        self.area = Vector2(area[0], area[1])
        self.color = color
        self.show_text_area = show_text_area
        # Establecemos la fuente del texto
        self.font = pygame.font.Font(SILVER_MEDIUM_FONT, self.textSize)

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_width, text_height = text_surface.get_size()
        center_position_x = (self.position.x + (self.area.x / 2)) - (text_width / 2)
        center_position_y = (self.position.y + (self.area.y / 2)) - (text_height / 3)
        position_center = Vector2(center_position_x, center_position_y)
        UiElement.screen.blit(text_surface, position_center)
        # Show text area
        if self.show_text_area:
            self.drawTextArea()

    def setText(self, text):
        self.text = text

    def setPosition(self, position):
        if (isinstance(position[0], float) or isinstance(position[0], int)) and (
            isinstance(position[1], int) or isinstance(position[1], float)
        ):
            self.position = Vector2(position[0], position[1])
        elif isinstance(position[0], str) and isinstance(position[1], str):
            if ("%" in position[0]) and ("%" in position[1]):
                self.position = Vector2(
                    (float(position[0].removesuffix("%")) / 100)
                    * UiElement.screen.get_width(),
                    (float(position[1].removesuffix("%")) / 100)
                    * UiElement.screen.get_height(),
                )
            else:
                self.position = Vector2(float(position[0]), float(position[1]))

    def drawTextArea(self):
        pygame.draw.rect(
            UiElement.screen,
            WHITE,
            (self.position.x, self.position.y, self.area.x, self.area.y),
            RECT_WIDTH,
        )


class TextAreaElement(TextElement):
    def __init__(
        self,
        text: str,
        textSize: int,
        position: typing.Union[Vector2, typing.Tuple[str, str]],
        area: typing.Union[Vector2, typing.Tuple[int, int]] = (100, 100),
        global_color: typing.Union[Vector3, typing.Tuple[int, int, int]] = WHITE,
        show_text_area: bool = False,
        margin=(0, 0, 0, 0),
    ):
        super().__init__(text, textSize, position, area, global_color, show_text_area)
        self.margin_left = margin[0]
        self.margin_top = margin[1]
        self.margin_right = margin[2]
        self.margin_bottom = margin[3]

    def draw(self):
        x, y = self.position.x, self.position.y
        initial_x, initial_y = x, y
        color_area = False
        color = self.color
        initial_color = color
        # Crea una lista 2D donde cada fila es una lista de palabras.
        words = [word.split(" ") for word in self.text.splitlines()]
        space = self.font.textSize(" ")[0]  # El ancho de un espacio.
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
                    color_tag = word.split(">")[0]
                    color_tag += ">"
                    color_values = re.findall(r"\d+", color_tag)
                    red, green, blue = (
                        int(color_values[0]),
                        int(color_values[1]),
                        int(color_values[2]),
                    )
                    word = word.removeprefix(color_tag)
                if word.endswith("</color>"):
                    word_color_finished = True
                    word = word.removesuffix("</color>")
                if color_area:
                    color = Vector3(red, green, blue)
                word_surface = self.font.render(word, True, color)
                if word_color_finished:
                    color_area = False
                word_width, word_height = word_surface.get_size()
                if (x + word_width) >= max_width - self.margin_right:
                    x = initial_x + self.margin_left  # Reinicia x.
                    y += word_height  # Comienza una nueva fila.
                UiElement.screen.blit(word_surface, (x, y))
                x += word_width + space
            x = initial_x  # Reinicia x.
            y += word_height  # Comienza una nueva fila.
        if self.show_text_area:
            self.drawTextArea()
