class UniquePassive():
    def __init__(self, name, description, level, statistics):
        self.name = name
        self.description = description
        self.level = level
        self.statistics = statistics

    # methods for child classes to customize
    def activate(self):
        pass

    def deactivate(self):
        pass

    # methods
    def getLevel(self):
        return self.level

    def levelUp(self):
        self.level = self.level + 1
