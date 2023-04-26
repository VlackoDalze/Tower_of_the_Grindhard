
class Skills():
    def __init__(self,name,description,damage,type):
        self.name = name
        self.description = description
        self.damage = damage
        self.type=type 
        self.lvl=1
        

    def getName(self):
        return self.name

    def getDamage(self):
        return self.damage

    def getType(self):
        return self.type
