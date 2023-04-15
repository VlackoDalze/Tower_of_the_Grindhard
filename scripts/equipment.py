import pygame
from scripts.statistics import Statistic

class Object(pygame.sprite.Sprite):
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description

class Equipment(Object):
    def __init__(self, name, description,statistics: Statistic):
        super().__init__(name, description)
        self.statistics = statistics

class Weapon(Equipment):
    def __init__(self, name, description, is_primary):
        super().__init__(name, description)
        self.is_primary = is_primary

class Armor(Equipment):
    def __init__(self, name, description, defense_type):
        super().__init__(name, description)
        self.defense_type = defense_type

class Belt(Equipment):
    def __init__(self, name, description, bonus_type):
        super().__init__(name, description)
        self.bonus_type = bonus_type

class Pants(Equipment):
    def __init__(self, name, description, bonus_type):
        super().__init__(name, description)
        self.bonus_type = bonus_type

class Helmet(Equipment):
    def __init__(self, name, description, bonus_type):
        super().__init__(name, description)
        self.bonus_type = bonus_type

class Shoes(Equipment):
    def __init__(self, name, description, bonus_type):
        super().__init__(name, description)
        self.bonus_type = bonus_type

class Cape(Equipment):
    def __init__(self, name, description, bonus_type):
        super().__init__(name, description)
        self.bonus_type = bonus_type