import pygame
from scripts.statistics import Statistics
import scripts.setting as setting
from scripts.unique_passive import UniquePassive


class Character(pygame.sprite.Sprite):
    def __init__(
        self,
        screen: pygame.Surface,
        name: str,
        description: str,
        image: pygame.Surface,
        baseStats: Statistics,
        activeAbilities,
        passiveAbilities,
        posX: int,
        posY: int,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.CELL_SIZE = setting.CELL_SIZE
        self.player_texture = image
        # with get.rect we obtain the X and Y axes
        self.rect = self.player_texture.get_rect()
        # we add 16 to center the image, this does not affect the X and Y axes
        self.rect.center = ((posX * self.CELL_SIZE) + 16, (posY * self.CELL_SIZE) + 16)
        self.screen = screen
        self.name = name
        self.description = description
        self.image = image
        self.baseStats = baseStats
        self.activeAbilities = []
        if activeAbilities!=None:
            for ability in activeAbilities:
                self.activeAbilities.append(ability)
        self.passiveAbilities = passiveAbilities

        # same as rect, but decomposed, we could also use rect.x or rect.y but I preferred to use the parameters that we set for something
        self.posX = posX * self.CELL_SIZE
        self.posY = posY * self.CELL_SIZE

    # methods
    # get player position
    def getBaseStats(self):
        return self.baseStats
    
    def getPositionX(self):
        return self.posX

    def getPositionY(self):
        return self.posY

    def getScreen(self):
        return self.screen

    def setImage(self, image):
        self.image = image

    def getActiveAbilities(self):
        return self.activeAbilities
    
    def addActiveAbilitie(self, activeAbilitie):
        self.activeAbilities.append(activeAbilitie)

    # def removeActiveAbilitie(self, activeAbilitie):
    #    pass
        
    def getImage(self):
        return self.image
    
    # receive attack, it is an array with two values: the damage and the type of damage
    def defend(self, receiveAttack):
        damage = receiveAttack[0]
        damageType = receiveAttack[1]
        if int(damageType) == 0:  # 0 physical
            return Statistics(self.baseStats).getPhysicalDefense() - float(damage)
        else:  # 1 magic
            return Statistics(self.baseStats).getMagicDefense() - float(damage)

    def attack(self, damageType):
        if int(damageType) == 0:  # 0 physical
            return (Statistics(self.baseStats).getPhysicalAttack(), 0)
        else:  # 1 magic
            return (Statistics(self.baseStats).getMagicAttack(), 1)

    def getCellSize(self):
        return self.CELL_SIZE

    # unique passive and other passives -a
    def activatePassives(self):
        UniquePassive(self.passiveAbilities).activate()

    def deactivatePassives(self):
        UniquePassive(self.passiveAbilities).deactivate()

class Race:
    # constructor
    def __init__(self, name, statistics, passives):
        self.name = name
        self.statistics = statistics
        self.passives = passives