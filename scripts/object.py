import pygame
from scripts.statistics import Statistics
from scripts.ui_element import *
from scripts.setting import SCREEN_WIDTH, SCREEN_HEIGHT
from scripts.texture_pack import inventory_slot


TEXT_SIZE = 23


class Object(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, name: str, description: str):
        self.image = image
        self.name = name
        self.description = description
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.panelElement = Panel_element(
            inventory_slot, (0, 0), (CELL_SIZE * 6, CELL_SIZE * 6)
        )
        # self.panelElement.addElement()

    def getImage(self) -> pygame.Surface:
        return self.image

    def setImage(self, image):
        self.image = image

    def getName(self) -> str:
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description):
        self.description = description

    def showPanelElements(self, masterElements, position):
        if masterElements.containElement(self.panelElement):
            masterElements.getElementList().remove(self.panelElement)
        else:
            self.panelElement.setPosition(position)
            masterElements.addElement(self.panelElement)


class Equipment(Object):
    def __init__(self, image, name, description, statistics: Statistics):
        super().__init__(image, name, description)
        self.statistics = statistics

    def getStatistic(self):
        return self.statistics

    def setStatistic(self, statistic: Statistics):
        self.statistic = statistic


class PrimaryWeapon(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class SecondaryWeapon(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Armor(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Glove(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Pants(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Helmet(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Shoes(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Cape(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description, statistics)


class Edible(Object):  # comestible
    def __init__(self, image, name, description, statistics):
        super().__init__(image, name, description)
        self.statistics = statistics
