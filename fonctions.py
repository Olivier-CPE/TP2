# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 28/09/2023, jeudi
 * TODO :
 * Ce fichier contient les fonctions utilisées dans le programme
"""

import constantes

# import des constantes
dictionnaire = constantes.dictionnaire
tableau_transitions = constantes.tableau_transitions


def decoupage_liste(string):
    # decoupe la phrase en liste de mots et de ponctuation
    liste = []
    mot = ""

    ponctuations = [a for a in dictionnaire if dictionnaire[a] == 5]  # liste des ponctuations

    string = string.lower()  # met la phrase en minuscule pour eviter les erreurs

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


def recuperer_type(string):
    if string in dictionnaire:
        return dictionnaire[string]
    else:  # si le mot n'est pas dans le dictionnaire
        return None


def verification_lexicale(phrase):
    etat = 0  # etat initial

    liste = decoupage_liste(phrase)  # liste de mots et de ponctuation

    liste = [a for a in liste if a != ""]  # supprime les espaces

    liste_types = [recuperer_type(a) for a in liste]  # liste des types de chaque mot

    for type_mot in liste_types:
        if type_mot is None:
            print(f"Erreur: Le mot n'est pas dans le dictionnaire")
            print(f"Mot : {liste[liste_types.index(type_mot)]}")
            return False

        etat = tableau_transitions[etat][type_mot]  # calcule état suivant

        if etat == 8:  # si l'état est 8, la phrase n'est pas valide
            return False

    return etat == 9  # si l'état final est 9, la phrase est valide


def test_verification_lexicale():
    phrases = {
        "Le stylo est un stylo bleu.": True,
        "Le stylo est un stylo bleu": False,
        "Olivier mange un ananas.": True,
        "Maxime une pomme.": False,
        ".": False,
        " ": False,
        "Olivier.": False,
        "Le petit stylo bleu écrit une belle phrase.": True,
        "Le petit stylo bleu écrit une belle phrase. Olivier mange un ananas.": True,  # 2 phrases
    }

    for phrase in phrases:
        if verification_lexicale(phrase):
            print(f"La phrase '{phrase}' est valide (resultat attendu : {phrases[phrase]})")
        else:
            print(f"La phrase '{phrase}' n'est pas valide (resultat attendu : {phrases[phrase]})")
        print("--------------------------------------------------")
