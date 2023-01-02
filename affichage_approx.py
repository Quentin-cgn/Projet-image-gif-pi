#!/usr/bin/env python3
"""
Permet l'affichage des nombres
"""
def nombres(tableau, abs_bas_gauche, ord_bas_gauche, nombre, traits):
    """
    Trace un nombre avec les différents traits à tracer donnés en paramètre.

    Parameters
    ----------

    tableau : list
        Contient des listes contenant des booléens correspondant à la
        couleur de chaque pixel
    abs_bas_gauche : int
        abscisse du pixel en bas à gauche du nombre à tracer
    ord_bas_gauche : int
        ordonnée du pixel en bas à gauche du nombre à tracer
    nombre : int
        largeur du nombre à tracer
    traits : tuple
        contient des booléens indiquant les traits à tracer pour le nombre

    """

    epaisseur = round(len(tableau)/100)
    hauteur_nombre = 2*nombre
    # On trace plusieurs fois les traits en fonction de l'épaisseur
    for i in range(epaisseur):
        # On trace les traits horizontaux en premier
        for j in range(3):
            ordo = ord_bas_gauche
            if traits[j]:
                if j == 1:
                    if epaisseur/2 == 0.5:
                        absi = round(abs_bas_gauche - hauteur_nombre/2)+i
                    else:
                        absi = round(abs_bas_gauche - hauteur_nombre/2 - epaisseur/2)+i

                elif j == 0:
                    absi = abs_bas_gauche - hauteur_nombre+i
                else:
                    absi = abs_bas_gauche-i
                for _ in range(nombre+1):
                    tableau[absi][ordo] = True
                    ordo += 1
        # On trace les trait verticaux.
        for j in range(3, 7):
            if traits[j]:
                if j in (3, 4):
                    absi = abs_bas_gauche - hauteur_nombre
                else:
                    absi = round(abs_bas_gauche - hauteur_nombre/2)
                if j in (4, 6):
                    ordo = ord_bas_gauche + nombre-i
                else:
                    ordo = ord_bas_gauche+i
                for _ in range(round(hauteur_nombre/2)+1):
                    tableau[absi][ordo] = True
                    absi += 1

def point(tableau, absi, ordo):
    """
    Affiche un point

    Parameters
    ----------

    tableau : list
        Contient des listes contenant des booléens correspondant à la
        couleur de chaque pixel
    absi : int
        indique l'abscisse du pixel en bas à gauche du point
    ordo : int
        indique l'ordonnee du pixel en bas à gauche du point
    """
    epaisseur = round(len(tableau)/100)
    for i in range(epaisseur):
        absci_point = absi - i
        ordo_point = ordo
        for _ in range(epaisseur):
            tableau[absci_point][ordo_point] = True
            ordo_point += 1


def rajoute_affichage(approx, nombre_apres_virgule, taille):
    """
    Cette fonction s'occupe d'écrire l'approximation de pi dans une matrice

    Parameters
    ----------

    approx : float
        L'approximation du nombre pi et donc les chiffres à afficher à l'écran
    nombre_apres_virgule : int
        nombre de chiffre après la virgule à afficher
    taille : int
        taille de l'image à afficher

    Returns
    -------

    tableau : list
        liste de listes contenant des booléens indiquant les pixels des chiffres de l'affichage

    """
    # Initialisation de notre tableau de pixels
    tableau = [[False for i in range(taille)] for j in range(taille)]

    # Calcul de la taille des chiffres à afficher en fonction de la taille de l'image
    nombre_espace = taille/(4*(nombre_apres_virgule+1))
    nombre = round(4/5*nombre_espace)

    if taille < 185:
        espace = 2
        ordo = round(1/3*taille)
    else:
        espace = round(1/5*nombre_espace)
        ordo = round(3/8*taille)
    approx = str(approx)
    absi = round(taille/2+nombre)
    compteur = -2
    for elt in approx:
        if compteur == nombre_apres_virgule:
            break
        if elt == "1":
            nombres(tableau, absi, ordo, nombre, (False, False, False, False, True, False, True))
        elif elt == "2":
            nombres(tableau, absi, ordo, nombre, (True, True, True, False, True, True, False))
        elif elt == "3":
            nombres(tableau, absi, ordo, nombre, (True, True, True, False, True, False, True))
        elif elt == "4":
            nombres(tableau, absi, ordo, nombre, (False, True, False, True, True, False, True))
        elif elt == "5":
            nombres(tableau, absi, ordo, nombre, (True, True, True, True, False, False, True))
        elif elt == "6":
            nombres(tableau, absi, ordo, nombre, (True, True, True, True, False, True, True))
        elif elt == "7":
            nombres(tableau, absi, ordo, nombre, (True, False, False, False, True, False, True))
        elif elt == "8":
            nombres(tableau, absi, ordo, nombre, (True, True, True, True, True, True, True))
        elif elt == "9":
            nombres(tableau, absi, ordo, nombre, (True, True, True, True, True, False, True))
        elif elt == "0":
            nombres(tableau, absi, ordo, nombre, (True, False, True, True, True, True, True))
        else:
            point(tableau, absi, ordo)
        if elt == ".":
            ordo = ordo + espace + espace
        else:
            ordo = ordo + espace + nombre
        compteur += 1
    # On rajoute des 0 à la fin si l'approximation ne contient pas assez de nombres
    if len(approx)-2 < nombre_apres_virgule:
        for _ in range(nombre_apres_virgule-len(approx)+2):
            nombres(tableau, absi, ordo, nombre, (True, False, True, True, True, True, True))
            ordo = ordo + espace + nombre
    return tableau
                