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
        self.health: float = health
        self.mana: float = mana
        self.physicalAttack: float = physicalAttack
        self.magicalAttack: float = magicalAttack
        self.physicalDefense: float = physicalDefense
        self.magicalDefense: float = magicalDefense
        self.precision: float = precision
        self.evasion: float = evasion
        self.critProbability: float = critProbability
        self.critMultiplier: float = critMultiplier
        self.speed: float = speed

    # getters and setters
    def getStat(self, name):
        
        if name == 'health':
            return self.health 
        if name == 'mana':
            return self.mana 
        if name == 'physicalAttack':
            return self.physicalAttack 
        if name == 'magicalAttack':
            return self.magicalAttack 
        if name == 'physicalDefense':
            return self.physicalDefense 
        if name == 'magicalDefense':
            return self.magicalDefense 
        if name == 'precision':
            return self.precision 
        if name == 'evasion':
            return self.evasion 
        if name == 'critProbability':
            return self.critProbability
        if name == 'critMultiplier':
            return self.critMultiplier
        if name == 'speed':
            return self.speed 
        
        
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
        statsString = (
            "\n"
            "Health: {}\n"
            "Mana: {}\n"
            "Physical attack: {}\n"
            "Magical attack: {}\n"
            "Physical defense: {}\n"
            "Magical defense: {}\n"
            "Precision: {}\n"
            "Evasion: {}\n"
            "Crit probability: {}\n"
            "Crit multiplier: {}\n"
            "Speed: {}"
        ).format(
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
        return statsString
