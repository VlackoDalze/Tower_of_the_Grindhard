from abc import abstractmethod
from abc import ABCMeta

class PasivaUnica(metaclass=ABCMeta): #clase abstracta -a
    
    @abstractmethod
    def activar(self,estadisticas):
        pass

    @abstractmethod
    def deactivar(self):
        pass
