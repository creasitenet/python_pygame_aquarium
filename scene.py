#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
"Module de base pour la création de scenes."

import constantes as constante

class Scene:
    "Squelette pour chaque scene du jeu."
    def __init__(self):
        self.scene = self
    
    def evenements_clavier(self, clavier = None):
        "Lire les evenements clavier pour intéragir avec les objets."
        pass
    
    def evenements_souris(self, souris = None):
        "Lire les evenements souris pour intéragir avec les objets."
        pass
    
    def evenements_joystick(self, joystick = None):
        "Lire les evenements joystick pour intéragir avec les objets."
        pass
    
    def actualiser(self):
        "Actualiser les objets sur l'écran."
        pass
    
    def afficher(self, ecran):
        "Dessiner les objets sur l'écran."
        pass
        
    def changer_scene(self, scene, fps=constante.FPS):
        "Changer la scene du jeu"
        self.scene = scene
        