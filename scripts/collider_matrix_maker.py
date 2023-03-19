import csv

def get_collider_matrix(level):
    collide_matrix = []

    with open(f'scene/{level}/collisions.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)  # Almaceno la matriz
        for line in csv_reader:
            collide_matrix.append(line)
    
    return collide_matrix