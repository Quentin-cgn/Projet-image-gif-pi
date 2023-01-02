#!/usr/bin/env python3

"""
Module permettant d'obtenir une valeur approchée de pi par la méthode de Monte Carlo.
Ce module peut aussi être importé pour se servir des coordonnées des points pour afficher
une image.
"""

import random
import sys

def points_a_afficher(nb_points):
    """
    Fonction utilisable par le module draw.py. Cette fonction est une fonction génératrice et
    se charge de renvoyer des points aléatoires entre 0 et 1 et de dire si ils sont placés ou
    non dans le cercle

    Parameters
    ----------

    nb_points : int
        spécifie le nombre de points aléatoires à prendre entre -1 et 1
    """
    for _ in range(nb_points):
        abscisse, ordonnee = random.uniform(-1, 1), random.uniform(-1, 1)

        # On vérifie si le point est dans le cercle ou non et on renvoie ce point
        yield ((abscisse, ordonnee), abscisse**2+ordonnee**2 < 1)

def main():
    """
    Cette fonction s'exécute si le programme est exécuté en tant que programme principal
    Elle se charge de renvoyer une approximation de pi par la méthode de Monte Carlo
    """
    compteur = 0
    for _ in range(int(sys.argv[1])):
        abscisse, ordonnee = random.uniform(-1, 1), random.uniform(-1, 1)
        if abscisse**2+ordonnee**2 < 1:
            compteur += 1
    print(4*compteur/int(sys.argv[1]))

if __name__ == "__main__":
    main()
