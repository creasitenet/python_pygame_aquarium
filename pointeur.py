#! /usr/bin/python
# -*- coding: utf-8 -*-
# DK labyrinthe
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
"Element pointer pour le menu."

import pygame
import constantes as constante
import fonctions as fonction
#from random import randrange     
 

class Pointeur(pygame.sprite.Sprite): 
    "Definie le comportement et les caractéristiques du pointer."
    def __init__(self, case_x, case_y):
        "Initialise le gorille"
        pygame.sprite.Sprite.__init__(self)
        #Charger l'image ou sprite du pointer
        self.image = fonction.charger_image("pointeur.png", True)
        #Initialiser le deplacement à non
        self.deplacement = 'non'
        #Definir la position de depart en case et en pixels
        self.case_x = case_x
        self.case_y = case_y
        self.x = self.case_x * constante.taille_sprite
        self.y = self.case_y * constante.taille_sprite
        self.position = (self.x, self.y)
     
    def deplacer(self, case_x, case_y):
        "Deplacer le pointer par case depuis la scene."
        if case_x != 0:
            self.case_x = self.case_x + case_x
        if case_y != 0:
            self.case_y = self.case_y + case_y
        self.deplacement = "oui"

    def positionner(self, case_x, case_y):
        "Positionner le pointer par case depuis la scene."
        self.case_x = case_x
        self.case_y = case_y
        self.deplacement = "oui"
        
    def evenements_clavier(self, touche = None):
        "Recoit les evenements clavier pour déterminer les action du pointeur."
        pass
    
    def evenements_souris(self, position = None):
        "Recoit les evenements souris pour déterminer les action du pointeur."
        pass

    def evenements_joystick(self, axe = None, sens = None):
        "Recoit les evenements joystick pour déterminer les action du pointeur."
        pass
       
    def actualiser(self):
        "Actualiser la position du pointeur." # L'actualisation n'affiche rien !!!
        if self.deplacement == "oui":
            son = pygame.mixer.Sound("./sons/bouge.ogg")
            son.set_volume(0.3) #volume
            son.fadeout(100) #Fondu ms de la fin de l'objet "son"
            son.play()

        #Agreger nouvelle position
        self.x = self.case_x * constante.taille_sprite        
        self.y = self.case_y * constante.taille_sprite
        self.position = (self.x, self.y)
        self.deplacement = "non"
        
    def afficher(self, ecran):
        "Sert pour afficher le pointeur."
        ecran.blit(self.image, self.position) 
        
        