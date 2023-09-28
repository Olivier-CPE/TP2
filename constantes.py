# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 28/09/2023, jeudi
 * TODO :
 * Ce fichier contient les constantes utilisées dans le programme
"""

dictionnaire = {
    "le": 0,
    "la": 0,
    "les": 0,
    "un": 0,
    "une": 0,
    "des": 0,
    "beau": 1,
    "belle": 1,
    "joli": 1,
    "grand": 1,
    "petit": 1,
    "gros": 1,
    "vieux": 1,
    "bleu": 1,
    "nouveau": 1,
    "jeux": 2,
    "livre": 2,
    "stylo": 2,
    "phrase": 2,
    "ordinateur": 2,
    "ananas": 2,
    "pomme": 2,
    "poire": 2,
    "mange": 3,
    "écrit": 3,
    "vend": 3,
    "achète": 3,
    "donne": 3,
    "est": 3,
    "suis": 3,
    "sont": 3,
    "olivier": 4,
    "maxime": 4,
    "jean": 4,
    "pierre": 4,
    "paul": 4,
    "marie": 4,
    ".": 5,
    "?": 5,
    "!": 5,
    ",": 5,
    ";": 5,
    ":": 5
}

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
