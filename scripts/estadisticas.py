class Estadisticas:
    # atributos
    vida = None
    mana = None
    ataqueFisico = None
    ataqueMagico = None
    defensaFisica = None
    defensaMagica = None
    presicion = None
    evasion = None
    probCritica = None
    multiplicadorCritico = None
    velocidad = None
    
    # constructor
    def __init__(self, vida, mana, ataqueFisico, ataqueMagico, defensaFisica, defensaMagica, presicion, evasion, probCritica, multiplicadorCritico, velocidad):
        self.vida = vida
        self.mana = mana
        self.ataqueFisico = ataqueFisico
        self.ataqueMagico = ataqueMagico
        self.defensaFisica = defensaFisica
        self.defensaMagica = defensaMagica
        self.presicion = presicion
        self.evasion = evasion
        self.probCritica = probCritica
        self.multiplicadorCritico = multiplicadorCritico
        self.velocidad = velocidad
        
    # getters y setters
    def getVida(self):
        return self.vida

    def setVida(self, vida):
        self.vida = vida

    def getMana(self):
        return self.mana

    def setMana(self, mana):
        self.mana = mana

    def getAtaqueFisico(self):
        return self.ataqueFisico

    def setAtaqueFisico(self, ataqueFisico):
        self.ataqueFisico = ataqueFisico

    def getAtaqueMagico(self):
        return self.ataqueMagico

    def setAtaqueMagico(self, ataqueMagico):
        self.ataqueMagico = ataqueMagico

    def getDefensaFisica(self):
        return self.defensaFisica

    def setDefensaFisica(self, defensaFisica):
        self.defensaFisica = defensaFisica

    def getDefensaMagica(self):
        return self.defensaMagica

    def setDefensaMagica(self, defensaMagica):
        self.defensaMagica = defensaMagica

    def getPresicion(self):
        return self.presicion

    def setPresicion(self, presicion):
        self.presicion = presicion

    def getEvasion(self):
        return self.evasion

    def setEvasion(self, evasion):
        self.evasion = evasion

    def getProbCritica(self):
        return self.probCritica

    def setProbCritica(self, probCritica):
        self.probCritica = probCritica

    def getMultiplicadorCritico(self):
        return self.multiplicadorCritico

    def setMultiplicadorCritico(self, multiplicadorCritico):
        self.multiplicadorCritico = multiplicadorCritico

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
