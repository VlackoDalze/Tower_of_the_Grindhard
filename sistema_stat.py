class Sistema_stats:

    #atributos
    vida = 0
    mana = 0
    ataqueFisico = 0
    ataqueMagico = 0
    defensaFisica = 0
    defensaMagica = 0
    precision = 0
    evasion = 0
    probCritica = 0
    multiplicadorCritico = 0
    velocidad = 0

    #constructor
    def __init__(self,vida,mana,ataqueFisico,ataqueMagico,defensaFisica,defensaMagica,precision,evasion,probCritica,multiplicadorCritico,velocidad):
        self.vida = vida
        self.mana = mana
        self.ataqueFisico = ataqueFisico
        self.ataqueMagico = ataqueMagico
        self.defensaFisica = defensaFisica
        self.defensaMagica = defensaMagica
        self.precision = precision
        self.evasion = evasion
        self.probCritica = probCritica
        self.multiplicadorCritico = multiplicadorCritico
        self.velocidad = velocidad

    #getters
    def __getVida__(self):
        return self.vida
    
    def __getMana__(self):
        return self.mana
    
    def __getAtaqFis__(self):
        return self.ataqueFisico
    
    def __getAtaqMag__(self):
        return self.ataqueMagico
    
    def __getDefFis__(self):
        return self.defensaFisica
    
    def __getDefMag__(self):
        return self.defensaMagica
    
    def __getPrec__(self):
        return self.precision

    def __getEva__(self):
        return self.evasion
    
    def __getProbCrit__(self):
        return self.probCritica
    
    def __getMultiCrit__(self):
        return self.multiplicadorCritico
    
    def __getVel__(self):
        return self.velocidad
    
    #setters
    def __setVida__(self,vida):
        self.vida = vida

    def __setMana__(self,mana):
        self.mana = mana

    def __setAtaqFis__(self,ataqueFisico):
        self.ataqueFisico = ataqueFisico

    def __setAtaqMag__(self,ataqueMagico):
        self.ataqueMagico = ataqueMagico

    def __setDefFis__(self,defensaFisica):
        self.defensaFisica = defensaFisica

    def __setDefMag__(self,defensaMagica):
        self.defensaMagica = defensaMagica

    def __setPrec__(self,precision):
        self.precision = precision

    def __setEva__(self,evasion):
        self.evasion = evasion

    def __setProbCrit__(self,probCritica):
        self.probCritica = probCritica

    def __setMultiCrit__(self,multiplicadorCritico):
        self.multiplicadorCritico = multiplicadorCritico

    def __setVel__(self,velocidad):
        self.velocidad = velocidad