from personaje import Personaje
class Enemigo(Personaje):
    #atributos
    tipo=None
    
    #constructor
    def __init__(self,tipo):
        self.tipo=tipo