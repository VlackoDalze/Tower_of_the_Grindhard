class Statistics:
    # constructor
    def __init__(self, health, mana, physicalAttack, magicalAttack, physicalDefense, magicalDefense, precision, evasion, critProbability, critMultiplier, speed):
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
