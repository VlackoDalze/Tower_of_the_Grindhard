class PasivaUnica():
    #atributos
    nombre = None
    descripcion = None
    nivel = 1
    estadisticas = None
    
    #constructor
    def __init__(self, nombre, descripcion, nivel, estadisticas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.nivel = nivel
        self.estadisticas = estadisticas
        
    #metodos para que los hijos los personalicen
    def activar():
        pass

    def deactivar():
        pass
    
    #metodos
    def getNivel(self):
        return self.nivel

    def subirNivel(self):
        self.nivel = self.nivel+1
        self.porcentaje = self.porcentaje+0.05
