import pygame
from scripts.statistics import Statistics


class Object(pygame.sprite.Sprite):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class Equipment(Object):
    def __init__(self, name, description, statistics: Statistics):
        super().__init__(name, description)
        self.statistics = statistics

    def getStatistic(self):
        return self.statistics

    def setStatistic(self, statistic: Statistics):
        self.statistic = statistic


class PrimaryWeapon(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class SecondaryWeapon(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Armor(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Belt(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Pants(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Helmet(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Shoes(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)


class Cape(Equipment):
    def __init__(self, name, description, statistics):
        super().__init__(name, description, statistics)
