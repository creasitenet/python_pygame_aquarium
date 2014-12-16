#! /usr/bin/python
# -*- coding: utf-8 -*-
# DK labyrinthe
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
"Les credits."
    
def lire_credis():
    #scores = []
    with open("fichiers/credis.sc", "r") as fichier:
        liste_credis = [] #liste des scores
        for ligne in fichier: #parcourt des lignes du fichier
            taille_ligne=len(ligne)
            ligne_propre = ligne[0:taille_ligne-1] #ignorer les "\n" de fin de ligne
            liste_credis.append(ligne_propre) #ajout de chaque ligne propre dans la liste des scores 
        credis = liste_credis #enregistrement des scores
    return credis
