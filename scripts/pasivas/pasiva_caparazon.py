from habilidad_pasiva_unica import PasivaUnica
from scripts.estadisticas import Estadisticas

class PasivaCaparazon(PasivaUnica):
    # atributos
    aux_vida = None
    PORCENTAJE = 1.05
    aux_defensa = None

    # constructor
    def __init__(self, nombre, descripcion, nivel, estadisticas):
        super().__init__(nombre, descripcion, nivel, estadisticas)
        self.aux_vida = self.estadisticas.getVida()
        self.aux_defensa = self.estadisticas.getDefensaFisica()

    # metodos
    def activar(self, estadisticas):
        self.estadisticas = Estadisticas(estadisticas)

        if self.aux_vida > self.estadisticas.getVida():
            self.estadisticas.setDefensaFisica(
                self.estadisticas.getDefensaFisica*self.PORCENTAJE)
            self.aux_vida = self.estadisticas.getVida()

    def desactivar(self):
        self.estadisticas.setDefensaFisica(self.aux_defensa)
