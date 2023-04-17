class Statistics:
    # constructor
    def __init__(
        self,
        health: float = 0.0,
        mana: float = 0.0,
        physicalAttack: float = 0.0,
        magicalAttack: float = 0.0,
        physicalDefense: float = 0.0,
        magicalDefense: float = 0.0,
        precision: float = 0.0,
        evasion: float = 0.0,
        critProbability: float = 0.0,
        critMultiplier: float = 0.0,
        speed: float = 0.0,
    ):
        self.health = health
        self.mana = mana
        self.physicalAttack = physicalAttack
        self.magicalAttack = magicalAttack
        self.physicalDefense = physicalDefense
        self.magicalDefense = magicalDefense
        self.precision = precision
        self.evasion = evasion
        self.critProbability = critProbability
        self.critMultiplier = critMultiplier
        self.speed = speed

    # getters and setters
    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getMana(self):
        return self.mana

    def setMana(self, mana):
        self.mana = mana

    def getPhysicalAttack(self):
        return self.physicalAttack

    def setPhysicalAttack(self, physicalAttack):
        self.physicalAttack = physicalAttack

    def getMagicalAttack(self):
        return self.magicalAttack

    def setMagicalAttack(self, magicalAttack):
        self.magicalAttack = magicalAttack

    def getPhysicalDefense(self):
        return self.physicalDefense

    def setPhysicalDefense(self, physicalDefense):
        self.physicalDefense = physicalDefense

    def getMagicalDefense(self):
        return self.magicalDefense

    def setMagicalDefense(self, magicalDefense):
        self.magicalDefense = magicalDefense

    def getPrecision(self):
        return self.precision

    def setPrecision(self, precision):
        self.precision = precision

    def getEvasion(self):
        return self.evasion

    def setEvasion(self, evasion):
        self.evasion = evasion

    def getCritProbability(self):
        return self.critProbability

    def setCritProbability(self, critProbability):
        self.critProbability = critProbability

    def getCritMultiplier(self):
        return self.critMultiplier

    def setCritMultiplier(self, critMultiplier):
        self.critMultiplier = critMultiplier

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def toString(self):
        statsString = """Health: {}
        Mana: {}
        Physical attack: {}
        Magical attack: {}
        Physical defense: {}
        Magical defense: {}
        Precision: {}
        Evasion: {}
        Crit probability: {}
        Crit multiplier: {}
        Speed: {}""".format(
            self.getHealth(),
            self.getMana(),
            self.getPhysicalAttack(),
            self.getMagicalAttack(),
            self.getPhysicalDefense(),
            self.getMagicalDefense(),
            self.getPrecision(),
            self.getEvasion(),
            self.getCritProbability(),
            self.getCritMultiplier(),
            self.getSpeed(),
        )
