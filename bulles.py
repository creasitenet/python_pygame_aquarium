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

class Bulles(pygame.sprite.Sprite): 
    '''Define l'image des bulles et les positions d'affichage.
    N'utilise pas la fonction get_rect qui pourrait simplifier'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Chargement des images des différentes nourritures
        self.image1 = fonction.charger_image("bulle1.png", True)
        self.image2 = fonction.charger_image("bulle2.png", True)
        
        #structure images
        self.images = [] #image
        #structure positions
        self.positions = [] #tuple (x,y)
        # structure direction (sens et vitesse)
        self.directions = [] #tuple (x,y)
        #Generer.
        self.generer()
        
    def generer(self):       
        for i in range(0, 30): #pour chaque bulle 
            #image
            imagenum = randint(1, 2)
            if imagenum == 1:
                image = self.image1
            elif imagenum == 2:
                image = self.image2    
            self.images.append(image)
            #position
            position_x = randrange(0, constante.LARGEUR, 1) # x = aleatoire
            position_y = randrange(0, constante.HAUTEUR, 1)  # y aleatoire
            position = (position_x, position_y)
            self.positions.append(position)
            #direction
            direction_x = 0 # x = 0 , y entre 1 et 3
            direction_y = randint(1, 3) #y entre 1 et 3
            direction = (direction_x, -direction_y) #-Y car on veut que ça monte pas que ça descende
            self.directions.append(direction)  
            #print self.positions
            #increment
            ++i


    def actualiser(self):
        '''Actualiser la positionde chaque bulle. n'affiche rien'''
        #son = pygame.mixer.Sound("./sons/bouge.ogg")
        #son.set_volume(0.3) #volume        
        #son.fadeout(300) #Fondu à 300ms de la fin de l'objet "son"
        
        #Déplacement        
        for i in range(0, len(self.images)): #pour chaque bulle de la struture
            #Agreger position et direction
            self.positions[i] = (self.positions[i][0] + self.directions[i][0], self.positions[i][1] + self.directions[i][1])
            #Arrive en haut ?
            if self.positions[i][1] < -20:
                position_x = randrange(0, constante.LARGEUR, 1) # x = aleatoire
                position_y = constante.HAUTEUR + 20  # y en dessous de l'ecran
                position = (position_x, position_y)
                self.positions[i] = position
                
                
    def afficher(self, ecran):
        '''Sert pour afficher les bulles.'''
        for i in range(0, len(self.images)):
            ecran.blit(self.images[i], self.positions[i])



