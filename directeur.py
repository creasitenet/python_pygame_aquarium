#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 05/06/12
'''Module pour la gestion de la scene en Pygame.'''

import pygame
import constantes as constante
import fonctions as fonction

class Directeur():
    '''Classe pour la gestion de la scene.'''
    def __init__(self):
        
        #Initialiser Pygame.
        pygame.init()
        
        #Ouverture de la fenêtre Pygame  avec ECRAN = (largeur,  hauteur)
        self.ecran = pygame.display.set_mode(constante.ECRAN)
        
        #Icone
        self.icone = fonction.charger_image(constante.ICONE, True)
        pygame.display.set_icon(self.icone)
        
        #Titre
        pygame.display.set_caption(constante.TITRE)
        
        #Vitesse de boucles
        self.horloge = pygame.time.Clock()
        
        #Variable scene vide
        self.scene = None
        
    def executer(self, scene_initiale, fps=constante.FPS):
        '''Executer la logique du jeu.'''
        #Variable scene avec les données transmises (la scene initiale au début)
        self.scene = scene_initiale
        jouer = True
        while jouer:
            #Limitation de vitesse de la boucle
            self.horloge.tick(fps)
            
            #Joystick
            self.nb_joysticks = pygame.joystick.get_count()
            if self.nb_joysticks > 0:
                joystick1 = pygame.joystick.Joystick(0)
                joystick1.init()
            
            #Acquisition des évenements.
            evenement = pygame.event.get() #print evenement
            
            #Interaction avec la scene.
            for e in evenement:
                #Clavier
                if e.type == pygame.KEYDOWN: # or e.type == pygame.KEYUP:
                    self.scene.evenements_clavier(e)
                   
                #Souris
                if e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEMOTION: #pygame.MOUSEBUTTONUP #pygame.MOUSEMOTION
                    self.scene.evenements_souris(e)
                    
                #Joystick #axes (d'une croix ou d'un pad) #boutons #trackballs #chapeaux ou hats
                if e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN:
                    self.scene.evenements_joystick(e)
            
            #Actualisations de la scene
            self.scene.actualiser() 
            #Affichage de la scene sur l'écran
            self.scene.afficher(self.ecran) 
            #Changement de scene
            self.scene = self.scene.scene
            #Sortir de la boucle donc du jeu. #envoi des evenement quitter et clavier à la fonction quitter
            jouer = fonction.continuer(evenement) #true = continuer, false = quitter
            #Rafraichissement
            pygame.display.flip()
        
        #en dehors de la boucle jouer, on quitte 
        pygame.quit()
