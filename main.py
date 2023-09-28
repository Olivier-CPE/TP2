# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 28/09/2023, jeudi
 * TODO :
 * Ce fichier est le fichier principal du programme
"""

import fonctions


def main():
    """phrase = input("Entrez une phrase : ")
    valide = fonctions.verification_lexicale(phrase)

    if valide:
        print("La phrase est valide")
    else:
        print("La phrase n'est pas valide")"""

    # Lancer les tests unitaires
    fonctions.test_verification_lexicale()


if __name__ == "__main__":
    main()
