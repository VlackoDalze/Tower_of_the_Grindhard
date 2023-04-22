from scripts.character import Character
from scripts.setting import SILVER_MEDIUM_FONT
import pygame
from scripts.collider_matrix_maker import get_collider_matrix
from scripts.triggers import Triggers
from scripts.enemigo import collision_enemy
from scripts.object import *
from scripts.statistics import Statistics
import scripts.texture_pack as texture_pack

WHITE = (255, 255, 255)

# Equipments for testing
primary_weapon = PrimaryWeapon(
    texture_pack.normal_primary_weapon_warrior_texture,
    "Sword",
    "A sharp, deadly blade",
    Statistics(),
)
secondary_weapon = SecondaryWeapon(
    texture_pack.normal_secondary_weapon_warrior_texture,
    "Bow",
    "A ranged weapon for skilled marksmen",
    Statistics(),
)
armor = Armor(
    texture_pack.normal_armor_texture,
    "Chain-mail",
    "Protective armor made of interlocking metal rings",
    Statistics(200),
)
glove = Glove(
    texture_pack.normal_glove_texture,
    "Leather Belt",
    "A sturdy belt to hold your pants up",
    Statistics(),
)
pants = Pants(
    texture_pack.normal_pants_texture,
    "Leather Pants",
    "Basic leather pants for protection",
    Statistics(),
)
helmet = Helmet(
    texture_pack.normal_headgear_texture,
    "Iron Helmet",
    "A heavy helmet to protect your head",
    Statistics(),
)
shoes = Shoes(
    texture_pack.normal_boot_texture,
    "Leather Boots",
    "Sturdy boots for rough terrain",
    Statistics(),
)
cape = Cape(
    texture_pack.normal_cape_texture,
    "Cloak",
    "A dark cloak for stealthy movement",
    Statistics(),
)


class Player(Character):
    newID = 0

    def __init__(
        self,
        screen: pygame.Surface,
        name,
        description,
        image,
        baseStats,
        activeAbilities,
        passiveAbilities,
        posX,
        posY,
        race,
        sceneLevel,
    ):
        super().__init__(
            screen,
            name,
            description,
            image,
            baseStats,
            activeAbilities,
            passiveAbilities,
            posX,
            posY,
        )
        self.race = race
        self.sceneLevel = sceneLevel
        self.stats: Statistic = Statistics()
        self.flip = False
        self.direction = 1
        self.id = Player.newID
        Player.newID += 1
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.equipping = True
        self.equipments = {
            PrimaryWeapon: primary_weapon,
            SecondaryWeapon: secondary_weapon,
            Armor: armor,
            Glove: glove,
            Pants: pants,
            Helmet: helmet,
            Shoes: shoes,
            Cape: cape,
        }
        equipmentKeys = self.getEquipmentsKeys()

    # Methods

    # TODO: modificar algunos aspecto del equipado (return)
    def equip(self, equipment: Equipment):
        equipmentReturn:Equipment = self.equipments[type(equipment)]
        self.equipments[type(equipment)] = equipment

    def getEquipments(self):
        return self.equipments

    def setEquipments(self, equipment: Equipment):
        self.equipment = equipment

    def getEquipmentsKeys(self):
        return self.equipments.keys()

    def recalculateStats(self):
        health: float = 0.0
        mana: float = 0.0
        physicalAttack: float = 0.0
        magicalAttack: float = 0.0
        physicalDefense: float = 0.0
        magicalDefense: float = 0.0
        precision: float = 0.0
        evasion: float = 0.0
        critProbability: float = 0.0
        critMultiplier: float = 0.0
        speed: float = 0.0
        for equipment_key in self.getEquipmentsKeys():
            health += self.equipments[equipment_key].getStatistic().getHealth()
            mana += self.equipments[equipment_key].getStatistic().getMana()
            physicalAttack += (
                self.equipments[equipment_key].getStatistic().getPhysicalAttack()
            )
            magicalAttack += (
                self.equipments[equipment_key].getStatistic().getMagicalAttack()
            )
            physicalDefense += (
                self.equipments[equipment_key].getStatistic().getPhysicalDefense()
            )
            magicalDefense += (
                self.equipments[equipment_key].getStatistic().getMagicalDefense()
            )
            precision += self.equipments[equipment_key].getStatistic().getPrecision()
            evasion += self.equipments[equipment_key].getStatistic().getEvasion()
            critProbability += (
                self.equipments[equipment_key].getStatistic().getCritProbability()
            )
            critMultiplier += (
                self.equipments[equipment_key].getStatistic().getCritMultiplier()
            )
            speed += self.equipments[equipment_key].getStatistic().getSpeed()
        self.stats = Statistics(
            health,
            mana,
            physicalAttack,
            magicalAttack,
            physicalDefense,
            magicalDefense,
            precision,
            evasion,
            critProbability,
            critMultiplier,
            speed,
        )

    def getId(self):
        return self.id

    def getScreen(self):
        return self.screen

    def getSceneLevel(self):
        return self.sceneLevel

    def getDirectionMove(self):
        if self.right:
            return "right"
        elif self.left:
            return "left"
        elif self.up:
            return "up"
        else:
            return "down"

    def move(self, event, assignedKeys):
        # *Control area
        movement_speed = super().getCellSize()
        listaKeys = [
            [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q],
            [pygame.K_g, pygame.K_j, pygame.K_y, pygame.K_h, pygame.K_t],
            [
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_RSHIFT,
            ],
            [pygame.K_KP_4, pygame.K_KP_6, pygame.K_KP_8, pygame.K_KP_5, pygame.K_KP_7],
        ]

        # *Movement area
        aux_x = self.posX
        aux_y = self.posY

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][0]:
            aux_x -= movement_speed
            self.left = True
            self.right = False
            self.up = False
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][1]:
            aux_x += movement_speed
            self.left = False
            self.right = True
            self.up = False
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][2]:
            aux_y -= movement_speed
            self.left = False
            self.right = False
            self.up = True
            self.down = False

        if event.type == pygame.KEYDOWN and event.key == listaKeys[assignedKeys][3]:
            aux_y += movement_speed
            self.left = False
            self.right = False
            self.up = False
            self.down = True

        colisiones = drawCollider(super().getCellSize(), self.sceneLevel)

        if (
            str(aux_x) + "-" + str(aux_y) not in colisiones
            and str(aux_x) + "-" + str(aux_y) not in collision_enemy
        ):
            self.posX = aux_x
            self.posY = aux_y
            self.rect.x = aux_x
            self.rect.y = aux_y

            Triggers.searchListTriggers(
                [self.posX, self.posY], self.sceneLevel, event, self.id
            )

    def draw(self):
        self.screen.blit(
            pygame.transform.flip(self.player_texture, self.flip, False), self.rect
        )


def drawCollider(sizeCell, sceneLevel):
    map_collider_matriz = get_collider_matrix(sceneLevel)
    eje_x = 0  # x-axis
    eje_y = 0  # y-axis
    colisiones = []
    for row in map_collider_matriz:
        for column in row:
            if column == "1" or column == "4":  # wall and decoration collision
                colisiones.append(str(eje_x) + "-" + str(eje_y))
            eje_x = eje_x + sizeCell  # increase x by +32
        eje_y = eje_y + sizeCell  # increase y by +32
        eje_x = 0  # reset x
    return colisiones
