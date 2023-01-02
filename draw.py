#! /usr/bin/env python3

"""
Module permmettant l'affichage d'une image gif représentant les différentes
étapes de l'approximation de pi par la méthode de Monte Carlo
"""
import sys
import subprocess
import approximate_pi
import affichage_approx

def points_taille(abscisse, ordonnee, taille):
    """
    Récupère les coordonnées d'un point entre -1 et 1 pour les placer entre 0 et taille-1.

    Parameters
    ----------

    abscisse : float
        abscisse du point entre -1 et 1
    ordonnee : float
        ordonnee du point entre -1 et 1
    taille : int
        taille de l'image en pixels

    Returns
    -------

    abscisse : int
        abscisse du point entre 0 et taille-1
    ordonnee : int
        ordonnee du point entre 0 et taille-1

    """
    abscisse = round((1+abscisse)/2*(taille-1))
    ordonnee = round((1+ordonnee)/2*(taille-1))
    return abscisse, ordonnee

def tableau_couleurs(tableau, points, taille, compteur):
    """
    Place les points dans le tableau grâce à leurs coordonnées et leur donne
    leur couleur selon leur placement.

    Parameters
    ----------

    tableau : list
        Contient des listes contenant des tuples correspondant à la
        couleur de chaque pixel
    points : tuple
        Tuple fournit par un fonction génératrice avec en premier élément les coordonnées
        du point et en deuxième un booléen indiquant sa position ou non dans le cercle
    taille : int
        taille de l'image en pixels
    compteur : int
        permet de calculer l'approximation à chaque 'rajout' de points

    Returns
    -------

    tableau : list
        le même qu'à l'entrée sauf que celui-ci est mis à jour avec les nouveaux points
    compteur : int
        permet de calculer la nouvelle approximation de pi
    """
    for elt in points:
        abscisse, ordonnee = points_taille(elt[0][0], elt[0][1], taille)

        # Si l'élément est dans le cercle, on met la couleur en rouge
        if elt[1]:
            tableau[abscisse][ordonnee] = (255, 0, 0)
            compteur += 1
        # sinon la couleur est verte
        else:
            tableau[abscisse][ordonnee] = (0, 255, 0)
    return tableau, compteur

def generate_ppm_file(tableau, affichage_nombre, num_image, approx, nb_apres_virgule):
    """
    Génère une image au format ppm

    Parameters
    ----------

    tableau : list
        Contient des listes contenant des  tuples correspondant à la
        couleur de chaque pixel
    affichage_nombre : list
        Contient des listes contenant des booléens correspondant à la
        couleur de chaque pixel, ici blanc ou noir car ne contient que les pixels de l'affichage
    num_image : int
        numéro d'apparition de l'image dans le gif
    approx : float
        approximation du nombre pi qui a été calculé
    nb_apres_virgule : int
        spécifie la précision de l'approximation qui va être affiché en donnant le nombre de
        chiffres après la virgule à garder

    Returns
    -------

    nom_image : str
        Renvoie le nom de l'image créée
    """
    nom_image = f"img{num_image}_{approx:.{nb_apres_virgule}f}.ppm".replace(".", "-", 1)

    # on écrit en premier en ASCII le format, la taille de l'image et on précise le nombre
    # de couleurs sur lequel on code

    with open(nom_image, "w") as image:
        image.write(f"P6 {len(tableau)} {len(tableau)} 255\n")

    # puis on écrit la couleur de chaque pixel en binaire

    with open(nom_image, "ab") as image:
        for i in range(len(tableau)):
            for j in range(len(tableau)):
                if affichage_nombre[i][j]:
                    image.write(bytes((255, 255, 255)))
                else:
                    image.write(bytes(tableau[i][j]))
    return nom_image

def main():

    """
    Fonction principale qui utilise les images des différents cercles aux différentes étapes
    pour créer un gif
    """
    # On vérifie que les paramètres précisés par l'utilisateur sont valables
    try:
        taille = int(sys.argv[1])
        nb_points = int(sys.argv[2])
        nb_apres_virgule = int(sys.argv[3])
    except (IndexError, ValueError):
        print("Erreur : Pour utiliser ce programme : il faut rentrer trois entiers : \n \
            - la taille de l'image qui doit être supérieur à 100 \n \
            - le nombre de points qui doit être supérieur à 100 \n \
            - le nombre de chiffres après la virgule qui doit être compris entre 1 et 5")
        sys.exit()
    try:
        if taille < 100:
            raise ValueError
        if nb_points < 100:
            raise ValueError
        if nb_apres_virgule < 1 or nb_apres_virgule > 5:
            raise ValueError
    except ValueError:
        print("Erreur : Pour utiliser ce programme : il faut rentrer trois entiers : \n \
            - la taille de l'image qui doit être supérieur à 100 \n \
            - le nombre de points qui doit être supérieur à 100 \n \
            - le nombre de chiffres après la virgule qui doit être compris entre 1 et 5")
        sys.exit()

    # On initialise les différents éléments nécessaires

    compteur = 0
    nom_images = []
    tab = [[(0, 0, 0) for i in range(taille)] for j in range(taille)]

    # On génère 10 images en récupérant les points depuis la fonction approximate
    # On les place dans une matrice, de même on récupère l'affichage de l'approximation
    # On appelle la fonction génératrice de l'image

    for i in range(10):
        tab, compteur = tableau_couleurs(tab, approximate_pi.points_a_afficher(round(nb_points/10))\
                                        , taille, compteur)
        approx = 4*compteur/(nb_points/10*(i+1))
        nom_images.append(generate_ppm_file(tab, \
            affichage_approx.rajoute_affichage(approx, nb_apres_virgule, taille),\
            i, approx, nb_apres_virgule))

    # On exécute ensuite la commande permettant de créer l'image gif

    gif = "output.gif"
    subprocess.call(f"convert -delay 150 -loop 5 {nom_images[0]} {nom_images[1]} \
        {nom_images[2]} {nom_images[3]} {nom_images[4]} {nom_images[5]} {nom_images[6]} \
        {nom_images[7]} {nom_images[8]} {nom_images[9]} {gif}", shell=True)

if __name__ == "__main__":
    main()
