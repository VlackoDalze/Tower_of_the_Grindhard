from razas.raza import Raza
class Sistema_Rol:
    # lista de jugadores
    jugadores = []
    # lista de enemigos
    enemigos = []

    def iniciarSistemaRol(self, jugadores, enemigos):
        jugadores = list(jugadores)
        enemigos = list(enemigos)

    def verificarVelocidad(self):
        # lista completa
        miembros_totales = [self.jugadores, self.enemigos]
        #turno de ??
        turno_segun_velocidad = miembros_totales[0]
        for miembro in miembros_totales:
            if Raza(miembro).getVelocidad() > Raza(turno_segun_velocidad).getVelocidad():
                turno_segun_velocidad = miembro
        #retorna el miembro segun la velocidad
        return turno_segun_velocidad
