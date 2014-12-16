#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
'''Elements du jeu.'''

import pygame
import constantes as constante
import fonctions as fonction
from random import randrange, randint

class Nourriture(pygame.sprite.Sprite): 
    '''Define l'image de la nourriture bulles et les positions d'affichage.'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Chargement des images des différentes nourritures
        self.image1 = fonction.charger_image("nourriture1.png", True)
        self.image2 = fonction.charger_image("nourriture2.png", True)
        self.image3 = fonction.charger_image("nourriture3.png", True)
        
        #structure images
        self.images = [] #image
        #structure positions
        self.positions = [] #tuple (x,y)
        # structure direction (sens et vitesse)
        self.directions = [] #tuple (x,y)
        #on ne genere pas pour ne rien afficher sans action de l'utilisateur
        
    def generer(self, position_x, position_y):
        #Generer la position de départ de la nourriture.
        nombre = randint(5, 10)
        for i in range(0, nombre): #pour chaque nourriture 
            #image
            imagenb = randint(1, 3)
            if imagenb == 1:
                image = self.image1
            elif imagenb == 2:
                image = self.image2  
            elif imagenb == 3:
                image = self.image3  
            self.images.append(image)
            #position
            nbpx = randrange(-5, 5, 1)
            nbpy = randrange(-3, 3, 1)
            position = (position_x + nbpx, position_y + nbpy)
            self.positions.append(position)
            #direction
            direction_x = randrange(-3, 3, 1) # x entre -2 et 2 erratique ?
            direction_y = randrange(1, 3, 1) #y entre 1 et 3 descente obligatoire
            direction = (direction_x, direction_y)
            self.directions.append(direction)  
            #increment
            ++i

    def evenements_souris(self, bouton = None, position = None):
        #Recoit les evenements souris.
        #print (bouton) #1 = gauche, 2 = milieu, 3 = droite, 4 = molette haut, 5 = molette bas
        #print (position) # position en pixel sur 
        if bouton == 5: #molette bas de la 
            self.generer(position[0], position[1]) # nourriture à la bonne position
        
    def actualiser(self):
        # Actualiser la position de chaque nourriture. 
		# N'affiche rien
        #son = pygame.mixer.Sound("./sons/bouge.ogg")
        #son.set_volume(0.3) #volume        
        #son.fadeout(300) #Fondu à 300ms de la fin de l'objet "son"
        
        #Déplacement        
        for i in range(0, len(self.images)): #pour chaque nourriture de la struture    
            #Agreger position et direction
            self.positions[i] = (self.positions[i][0] + self.directions[i][0], self.positions[i][1] + self.directions[i][1])
            #Changement de direction
            direction_x = randrange(-3, 3, 1) # x entre -3 et 3 erratique ?
            direction_y = randrange(1, 3, 1) #y entre 1 et 3 descente obligatoire
            self.directions[i] = (direction_x, direction_y) #enregistrement  
                       
            #Arrive en bas, on efface le dernier élément
            if self.positions[i][1] > constante.HAUTEUR + 100:
                self.effacer(i)
                break
      
        #print (self.positions)          
           
                
    def afficher(self, ecran):
        #Sert pour afficher la nourriture.
        for i in range(0, len(self.images)):
            ecran.blit(self.images[i], self.positions[i])
                
    def effacer(self, numero):
        #Sert pour effacer la nourriture.
        self.images.pop(numero) 
        self.positions.pop(numero)     
        self.directions.pop(numero)

