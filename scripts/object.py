import pygame
from scripts.statistics import Statistics


class Object(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, name: str, description: str):
        self.image = image
        self.name = name
        self.description = description


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
        super().__init__(image,name, description, statistics)


class Cape(Equipment):
    def __init__(self, image, name, description, statistics):
        super().__init__(image,name, description, statistics)
