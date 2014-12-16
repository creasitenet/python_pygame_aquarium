#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
"Elements du jeu."

import pygame
import constantes as constante
import fonctions as fonction
from random import randint
#from random import randrange     
 

class Poisson(pygame.sprite.Sprite): 
    "Definie le comportement et les caractéristiques du poisson."
    def __init__(self):
        "Initialise le poisson"
        pygame.sprite.Sprite.__init__(self)
        #couleur
        couleurs = ["bleu","jaune","rouge","violet"]
        couleur_nb = randint(0,3)
        couleur = couleurs[couleur_nb]
        
        self.couleur = couleur
        #Charger les images ou sprites du personnage
        if self.couleur == "bleu":
            self.droite = fonction.charger_image("poisson_bleu_droite.png", True)
            self.gauche = fonction.charger_image("poisson_bleu_gauche.png", True)
        
        if self.couleur == "jaune":
            self.droite = fonction.charger_image("poisson_jaune_droite.png", True)
            self.gauche = fonction.charger_image("poisson_jaune_gauche.png", True)
            
        if self.couleur == "rouge":
            self.droite = fonction.charger_image("poisson_rouge_droite.png", True)
            self.gauche = fonction.charger_image("poisson_rouge_gauche.png", True)
            
        if self.couleur == "violet":
            self.droite = fonction.charger_image("poisson_violet_droite.png", True)
            self.gauche = fonction.charger_image("poisson_violet_gauche.png", True)
        #self.haut = fonction.charger_image("poisson_droite.png", True)
        #self.bas = fonction.charger_image("poisson_droite.png", True)
        #Definir l'image par defaut à droite
        self.image = self.droite
        #Initialiser le deplacement à non
        #self.deplacer = 'non'
        #Definir la position de depart en case et en pixels
        self.position = self.image.get_rect()
        self.position.x = 0 
        self.position.y = 0
        self.vitesse = [2, 2]
        #Generer
        self.generer()
        
    def generer(self):
        "Generer la position de départ du poisson."
        lmax = constante.LARGEUR - (self.position.width /2)
        self.position.x = randint(1, lmax)
        hmax = constante.HAUTEUR - (self.position.height /2)
        self.position.y = randint(1, hmax)
        
            
    def evenements(self, evenement = None):
        "Recoit les evenements pour déterminer les action du poisson."
        pass
    
    def evenements_clavier(self, touche = None):
        "Recoit les evenements clavier pour déterminer les action du poisson."
        # Définir la touche enfoncée 
        pass
    
    def evenements_souris(self, position = None):
        "Recoit les evenements souris pour déterminer les action du poisson."
        #print bouton #1 = gauche, 2 = milieu, 3 = droite, 4 = molette haut, 5 = molette bas
        #print position # position en pixel sur l'ecran
        pass
        
    def evenements_joystick(self, axe = None, sens = None):
        "Recoit les evenements joystick pour déterminer les action du gorille."
        pass
        
    
    def faim(self):
        "Detecte si le poisson a faim."
        pass
        
    def actualiser(self):
        "Actualiser la position du poisson." # L'actualisation n'affiche rien !!!
        
        #Déplacement automatique
        if self.position.x < 0 or self.position.x > constante.LARGEUR:
            self.vitesse[0] = -self.vitesse[0]
        if self.position.y < 0 or self.position.y > constante.HAUTEUR:
            self.vitesse[1] = -self.vitesse[1]
       
        #changement d'image
        if self.vitesse[0] >= 1: #va a droite
            self.image = self.droite
        elif self.vitesse[0] <= -1: #va a gauche
            self.image = self.gauche
            
        #Agreger nouvelle position
        self.position = self.position.move(self.vitesse)
        #self.position = (self.x, self.y)
        #On réinitialise la variable deplacer à non.
        #self.deplacer = 'non'
        
    def mange(self, nourriture):
        "Detecte si le poisson mange."
        if self.pos_x == nourriture.rect.x and self.pos_y == nourriture.rect.y:
            return True
        return False
        
    def collision(self):
        "Verifie si le serpent entre en collision avec les parois ou lui même."
        pass
        '''if (self.corp[0].left< 0 or self.corp[0].right> constante.LARGEUR or
               self.corp[0].top< 0 or self.corp[0].bottom> constante.HAUTEUR or
               self.corp[0] in self.corp[1:]):
               return True
        return False'''
    
    def afficher(self, ecran):
        "Sert pour afficher le gorille."
        ecran.blit(self.image, self.position) 
        
        