from estadisticas import Estadisticas
class Personaje:
    #atributos
    nombre = None
    descripcion = None
    imagen = None
    estadisticasBase = None
    habilidadesActivas = None
    habilidadesPasivas = None

    #constructor
    def __init__(self, nombre, descripcion, imagen, estadisticasBase, habilidadesActivas, habilidadesPasivas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen
        self.estadisticasBase = estadisticasBase
        self.habilidadesActivas = habilidadesActivas
        self.habilidadesPasivas = habilidadesPasivas

    #metodos
    def defender(self,recibeAtaque): #recibe ataque es un array con dos valores el daño  y el tipo de daño
        dano = recibeAtaque[0]
        tipoDeDano = recibeAtaque[1]
        if int(tipoDeDano)==0: #  0 fisico
            return Estadisticas(self.estadisticasBase).getDefensaFisica()-float(dano)
        else: # 1 magico
            return Estadisticas(self.estadisticasBase).getDefensaMagica()-float(dano)

    def atacar(self,tipoDeDano):
        if int(tipoDeDano)==0: #  0 fisico
            return (Estadisticas(self.estadisticasBase).getAtaqueFisico(),0)
        else:  # 1 magico
            return (Estadisticas(self.estadisticasBase).getAtaqueMagico(),1)