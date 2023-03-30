"""
Estos metodos leen archivos CSV y devuelven una matriz que contiene los datos del archivo.
"""
import csv

# Toma como argumento el nivel del juego y devuelve la matriz de colisiones para ese nivel


def get_collider_matrix(level):
    collide_matrix = []
    ruta="scene/"+level+"/Collisions.csv"
    with open(ruta, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)  # Almaceno la matriz
        for line in csv_reader:
            collide_matrix.append(line)

    return collide_matrix
# Toma como argumento el nivel del juego y devuelve la matriz de decoraciones animadas para ese nivel.


def get_animated_decorations_matrix(level):
    animated_decorations_matrix = []

    with open(f'scene/{level}/Dynamic_decorations.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)  # Almaceno la matriz
        for line in csv_reader:
            animated_decorations_matrix.append(line)

    return animated_decorations_matrix
