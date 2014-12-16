#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
'''Fonctions communes.'''

import os #sys
import pygame
import constantes as constante
import fonctions as fonction
#from random import randrange    


class Joystick(pygame.sprite.Sprite): 
    '''Definie le joystick.'''
    def __init__(self):
        #Initialise le joystick
        pygame.sprite.Sprite.__init__(self)
        self.joy = pygame.joystick.get_count()
        #Charger le texte du joystick
        self.texte_joystick = fonction.Texte("", 20, constante.noir)
        
    def actualiser(self):
        #Actualiser le joystick.
		#L'actualisation n'affiche rien !!!
        self.joy = pygame.joystick.get_count()
        print self.joy    
        if self.joy > 0: 
            self.texte_joy = "Joystick ok !"
            print("Joystick branché !!!")
        else:
            self.texte_joy = "Pas de Joystick !"
            print "Joystick debranché !!!"
        
    def afficher(self, ecran):
        #Sert pour afficher le joystick. ???
        ecran.blit(self.texte_joystick.afficher(str(self.texte_joy)), self.texte_joystick.position(2, 0, 25, 90))
