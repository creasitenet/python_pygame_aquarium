#! /usr/bin/python
# -*- coding: utf-8 -*-
# Aquarium v0.1
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 05/06/12

from directeur import Directeur
from scenes import SceneInitiale

def main():
    "Pour jouer au jeu"
    directeur = Directeur()
    directeur.executer(SceneInitiale(),10)

if __name__ == "__main__":
    main()
