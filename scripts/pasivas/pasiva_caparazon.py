from habilidad_pasiva_unica import PasivaUnica
from scripts.estadisticas import Estadisticas

class PasivaCaparazon(PasivaUnica):
    #atributos
    nombre = None
    descripcion = None
    aux_vida = None
    estadisticas = None
    porcentaje = 1.05
    nivel = 1
    aux_defensa = None

    #constructor
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    #metodos
    def activar(self, estadisticas):
        self.estadisticas = Estadisticas(estadisticas)
        if self.aux_defensa is None:
            self.aux_defensa = self.estadisticas.getDefensaFisica()

        if self.aux_vida is None:
            self.aux_vida = self.estadisticas.getVida()

        if self.aux_vida > self.estadisticas.getVida():
            self.estadisticas.setDefensaFisica(
                self.estadisticas.getDefensaFisica*self.porcentaje)

    def desactivar(self):
        self.estadisticas.setDefensaFisica(self.aux_defensa)

    def getNivel(self):
        return self.nivel

    def subirNivel(self):
        self.nivel = self.nivel+1
        self.porcentaje = self.porcentaje+0.05
