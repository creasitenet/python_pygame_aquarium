#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
'''Elements du jeu.'''

import pygame
import constantes as constante
import fonctions as fonction
from random import randint  #randrange,
 

class Poissons(pygame.sprite.Sprite): 
    '''Definie le comportement et les caractéristiques du poisson.'''
    def __init__(self):
        '''Initialise le poisson'''
        pygame.sprite.Sprite.__init__(self)
        
        # variables générales
        # dimension de l'image
        img = fonction.charger_image("poisson_bleu_droite.png", True)
        self.dimension = img.get_rect()
        
        #structure images gauches et doite en fonction de la couleur
        self.images_gauche_droite = [] #tuple (image gauche, image droite)    
        #structure images
        self.images = [] #image
        #structure positions
        self.positions = [] #tuple (x,y)
        # structure direction (sens et vitesse)
        self.directions = [] #tuple (x,y)
		#booleen a faim
        self.afaim = True
        
    def generer(self, position_x, position_y):
        '''Generer le poisson.'''
        
        # couleur aléatoire
        couleurs_disponibles = ["bleu","jaune","rouge","violet"]
        couleur_nb = randint(0,3)
        couleur = couleurs_disponibles[couleur_nb]     
        #Charger les images ou sprites du poisson
        if couleur == "bleu":
            droite = fonction.charger_image("poisson_bleu_droite.png", True)
            gauche = fonction.charger_image("poisson_bleu_gauche.png", True)
        elif couleur == "jaune":
            droite = fonction.charger_image("poisson_jaune_droite.png", True)
            gauche = fonction.charger_image("poisson_jaune_gauche.png", True)
        elif couleur == "rouge":
            droite = fonction.charger_image("poisson_rouge_droite.png", True)
            gauche = fonction.charger_image("poisson_rouge_gauche.png", True)
        elif couleur == "violet":
            droite = fonction.charger_image("poisson_violet_droite.png", True)
            gauche = fonction.charger_image("poisson_violet_gauche.png", True)
        image_gauche_droite = (gauche, droite)
        self.images_gauche_droite.append(image_gauche_droite) 
        
        #position 
        x = position_x - (self.dimension.width /2)
        y = position_y - (self.dimension.height /2)
        position = (x, y)
        self.positions.append(position)
        
        # direction (sens et vitesse)
        direction_horizontale=0
        while direction_horizontale==0:
            direction_horizontale = randint(-3,3)
        if direction_horizontale<0:
            image = gauche  # image à gauche
        elif direction_horizontale>0:
            image = droite # image à droite
        else:
            image = droite # image par défaut à droite
        self.images.append(image) 
        
        direction_verticale=0
        while direction_verticale==0:
            direction_verticale = randint(-3,3)
        
        direction=(direction_horizontale,direction_verticale)
        self.directions.append(direction)
        
        
    def evenements(self, evenement = None):
        '''Recoit les evenements pour déterminer les actions sur les poissons. pour l'instant aucune.'''
        pass
    
    def evenements_clavier(self, touche = None):
        '''Recoit les evenements clavier pour déterminer les actions sur les poissons. pour l'instant aucune'''
        pass
    
    def evenements_souris(self, bouton = None, position = None):
        '''Recoit les evenements souris pour déterminer les action sur les poissons.'''
        #print (bouton) #1 = gauche, 2 = milieu, 3 = droite, 4 = molette haut, 5 = molette bas
        #print (position) # position en pixel sur l'ecran
        if bouton == 1: #bouton gauche de la souris
            self.generer(position[0], position[1]) # nouveau poisson à la bonne position
        if bouton == 3: #bouton droit de la souris
            self.collision(position[0], position[1]) # clic droit sur un poisson, le supprimer
        #pass
        
    def evenements_joystick(self, axe = None, sens = None):
        '''Recoit les evenements joystick pour déterminer les actions sur les poissons. pour l'instant aucune'''
        pass   
    
    def actualiser(self):
        '''Actualiser la position de chaque poisson.''' 
		# L'actualisation n'affiche rien
        for i in range(0, len(self.images)): #pour chaque poisson de la struture
            
            # changement de direction en cas de colision avec les bord
            direction_x = self.directions[i][0]
            direction_y = self.directions[i][1]
            if self.positions[i][0] < 0 or self.positions[i][0] > constante.LARGEUR:
                direction_x=-self.directions[i][0]
            if self.positions[i][1] < 0 or self.positions[i][1] > constante.HAUTEUR:
                direction_y=-self.directions[i][1]
            direction=(direction_x,direction_y)
            self.directions[i] = direction
            
			# changement de direction si il y a de la nourriture ???			
			
            # changement d'image
            if self.directions[i][0] >= 1: #va a droite
                self.images[i] = self.images_gauche_droite[i][1]
            elif self.directions[i][0] <= -1: #va a gauche
                self.images[i] = self.images_gauche_droite[i][0]
                
            #Agreger position et direction
            self.positions[i] = (self.positions[i][0] + self.directions[i][0], self.positions[i][1] + self.directions[i][1])
            #increment
            ++i
        #pass
        
    def effacer(self, numero):
        '''Sert pour effacer le poisson.'''
        self.images_gauche_droite.pop(numero)
        self.images.pop(numero) 
        self.positions.pop(numero)     
        self.directions.pop(numero)

    def faim(self):
        '''Detecte si le poisson a faim. Pas encore implémenté. La variable afaim est a true'''
        pass
    
    def mange(self, nourriture):
        '''Detecte si le poisson mange.'''
        return False
        #pass
        
    def collision(self, position_x, position_y):
        '''Verifie si la position cliquée correspond à un poisson'''
        for i in range(0, len(self.images)): #pour chaque poisson de la structure
            gauche_poisson = int(self.positions[i][0])
            droite_poisson = int(self.positions[i][0] + (self.dimension.width))
            haut_poisson = int(self.positions[i][1])
            bas_poisson = int(self.positions[i][1] + (self.dimension.height))
            #print (position_x, self.positions[i][0], gauche_poisson, droite_poisson)
            #print (position_y, self.positions[i][1], haut_poisson, bas_poisson)
            if (position_x in range(gauche_poisson, droite_poisson)) and (position_y in range(haut_poisson, bas_poisson)):
                self.effacer(i)
                break
            #increment
            ++i
        #pass
    
    def afficher(self, ecran):
        '''Sert pour afficher les poissons.'''
        for i in range(0, len(self.images)):
            ecran.blit(self.images[i], self.positions[i])
            #increment
            ++i
        #pass

