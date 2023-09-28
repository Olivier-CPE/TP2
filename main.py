# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 28/09/2023, jeudi
 * TODO :
"""

import dictionnaire

dictionnaire = dictionnaire.d

tableau_transitions = (
    (1, 8, 8, 8, 4, 8),
    (8, 1, 2, 8, 8, 8),
    (8, 2, 8, 3, 8, 8),
    (5, 8, 8, 8, 7, 9),
    (8, 8, 8, 3, 8, 8),
    (8, 5, 6, 8, 8, 0),
    (8, 6, 8, 8, 8, 9),
    (8, 8, 8, 8, 8, 9),
    (8, 8, 8, 8, 8, 8),
    (1, 8, 8, 8, 4, 8)
)

phrase = "Olivier vend un ananas bdjkabdjk."


def decoupage_liste(string):
    # decoupe la phrase en liste de mots et de ponctuation
    liste = []
    mot = ""

    ponctuations = [a for a in dictionnaire if dictionnaire[a] == 5]

    string = string.lower()

    if string[-1] == " ":
        string = string[:-1]

    for i in string:
        if i == " ":
            liste.append(mot)
            mot = ""
        elif i in ponctuations:
            liste.append(mot)
            liste.append(i)
            mot = ""
        else:
            mot += i

    if mot != "":
        liste.append(mot)

    return liste


def getType(string):
    if string in dictionnaire:
        return dictionnaire[string]
    else:
        return None


liste = decoupage_liste(phrase)

liste_types = [getType(a) for a in liste]

print(liste_types)
print(decoupage_liste(phrase))

etat = 6
type_mot = 2

# Récupérer l'état suivant
print(tableau_transitions[etat][type_mot])

    

