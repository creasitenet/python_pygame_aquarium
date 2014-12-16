#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
"Scenes du jeu."

import pygame
#import time
from scene import Scene
import constantes as constante
import fonctions as fonction
import pointeur
import poisson
import poissons
import nourriture
import bulles
import credis
#from random import randrange            


class SceneInitiale(Scene):
    "Scene menu : affiche le menu."
    def __init__(self):
        #Initialisation de la scene
        Scene.__init__(self)
        #Chargement de l'image de fond de la scene
        self.fond = fonction.charger_image("fond.jpg")
        #Chargement des objets
        self.bulles = bulles.Bulles()
        self.pointeur = pointeur.Pointeur(14,3) 
        self.poisson_1 = poisson.Poisson()
        self.poisson_2 = poisson.Poisson()
        self.poisson_3 = poisson.Poisson()
        self.poisson_4 = poisson.Poisson()
        
        #Chargement de la musique de fond 
        #self.musique = pygame.mixer.music.load("./sons/bouge.ogg")
        #self.musique.set_volume(0.5)
        #self.musique.fadeout(400) 
    
        #Chargement des textes à afficher
        self.texte_titre = fonction.Texte("Aquarium", 50, constante.noir)
        #Menu
        self.texte_menu_jouer = fonction.Texte(" > Jouer [J]",30, constante.bleufonce)
        self.texte_menu_credis = fonction.Texte(" > Credits [C]",30, constante.noir)
        self.texte_menu_quitter = fonction.Texte(" > Quitter [Q]",30, constante.noir)
        #joystick
        self.nb_joysticks = pygame.joystick.get_count()
        if self.nb_joysticks > 0:
            self.texte_joystick = fonction.Texte("Joystick ok", 20, constante.gris)
        else:
            self.texte_joystick = fonction.Texte("Pas de joystick", 20, constante.gris)
    
    def evenements_clavier(self, clavier = None):
        "Lire les evenements clavier pour déterminer les action ou la scene correspondante." 
        #print clavier
        if clavier:
            touche = clavier.key
            if touche - 272 == 1: #1 en haut
                if self.pointeur.case_y > 3:
                    self.pointeur.deplacer(0,-1)
            if touche - 272 == 2: #2 en bas
                if self.pointeur.case_y < 5:
                    self.pointeur.deplacer(0,1)
            if touche == pygame.K_j: #jouer
                self.changer_scene(SceneJeu())      
            if touche == pygame.K_c: #credits    
                self.changer_scene(SceneCredis())  
            if touche == pygame.K_RETURN:
                # verifie ou se trouve le pointeur pour enclencher la scene correspondante
                if self.pointeur.case_y == 3:
                    self.changer_scene(SceneJeu())
                elif self.pointeur.case_y == 4:
                    self.changer_scene(SceneCredis())
                elif self.pointeur.case_y == 5:
                    quit()
                
    def evenements_souris(self, souris = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante." 
        if souris: #print souris
            if souris.type == pygame.MOUSEMOTION: # si deplacement souris
                position = souris.pos
                if 420 < position[0] < 565 and 90 < position[1] < 115: #jouer 
                    if self.pointeur.case_y != 3:
                        self.pointeur.positionner(14,3)
                if 420 < position[0] < 585 and 120 < position[1] < 145: #scores 
                    if self.pointeur.case_y != 4:
                        self.pointeur.positionner(14,4)
                if 420 < position[0] < 585 and 150 < position[1] < 175: #quitter
                    if self.pointeur.case_y != 5:
                        self.pointeur.positionner(14,5)
                
            if souris.type == pygame.MOUSEBUTTONDOWN: # clic souris
                bouton = souris.button
                position = souris.pos
                if bouton == 1:
                    if 450 < position[0] < 565 and 90 < position[1] < 115: #jouer 
                        self.changer_scene(SceneJeu())
                    if 450 < position[0] < 585 and 120 < position[1] < 145: #scores 
                        self.changer_scene(SceneCredis())
                    if 420 < position[0] < 585 and 150 < position[1] < 175: #quitter
                        quit()
    
    def evenements_joystick(self, joystick = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante."
        if joystick:
            # les axes
            if joystick.type == pygame.JOYAXISMOTION:
                axe = joystick.axis
                sens = joystick.value
                if axe == 1 and sens < -0.5: #aller en haut
                    if self.pointeur.case_y > 3:
                        self.pointeur.deplacer(0,-1)
                elif axe == 1 and sens < -0.5:
                    if self.pointeur.case_y < 5:
                        self.pointeur.deplacer(0,1)
                
            # les boutons
            elif joystick.type == pygame.JOYBUTTONDOWN:
                bouton = joystick.button
                if bouton == 9: #start
                    self.changer_scene(SceneJeu())
                if bouton == 2: #x
                    # verifie ou se trouve le pointeur pour enclencher la scene correspondante
                    if self.pointeur.case_y == 3:
                        self.changer_scene(SceneJeu())
                    elif self.pointeur.case_y == 4:
                        self.changer_scene(SceneCredis())
                    elif self.pointeur.case_y == 5:
                        quit()

    def actualiser(self): 
        #actualisation
        self.bulles.actualiser()
        self.poisson_1.actualiser()
        self.poisson_2.actualiser()
        self.poisson_3.actualiser()
        self.poisson_4.actualiser()
        #actualisation de la position du pointer
        self.pointeur.actualiser()
        if self.pointeur.case_y == 3:
            self.texte_menu_jouer.changer_couleur(constante.bleufonce)
            self.texte_menu_credis.changer_couleur(constante.noir)
            self.texte_menu_quitter.changer_couleur(constante.noir)
        if self.pointeur.case_y == 4:
            self.texte_menu_jouer.changer_couleur(constante.noir)
            self.texte_menu_credis.changer_couleur(constante.bleufonce)
            self.texte_menu_quitter.changer_couleur(constante.noir)
        if self.pointeur.case_y == 5:
            self.texte_menu_jouer.changer_couleur(constante.noir)
            self.texte_menu_credis.changer_couleur(constante.noir)
            self.texte_menu_quitter.changer_couleur(constante.bleufonce)
        #Joystick ?
        self.nb_joysticks = pygame.joystick.get_count()
        if self.nb_joysticks > 0:
            self.texte_joystick = fonction.Texte("Joystick ok", 16, constante.gris)
        else:
            self.texte_joystick = fonction.Texte("Pas de joystick", 16, constante.gris)
            
    def afficher(self, ecran):
        #Remplissage en noir
        ecran.fill( (0x11, 0x11, 0x11) )  
        #Image de fond
        ecran.blit(self.fond, (0, 0))   
        #Dessiner les objets. 
        self.bulles.afficher(ecran)
        self.poisson_1.afficher(ecran)
        self.poisson_2.afficher(ecran)
        self.poisson_3.afficher(ecran)
        self.poisson_4.afficher(ecran)
        #Dessiner les textes.
        ecran.blit(self.texte_titre.afficher(), self.texte_titre.position(1, 0, 0, 15))
        ecran.blit(self.texte_joystick.afficher(), self.texte_joystick.position(1, 0, 20, 50))
        ecran.blit(self.texte_menu_jouer.afficher(), self.texte_menu_jouer.position(0, 0, 450, 95))
        ecran.blit(self.texte_menu_credis.afficher(), self.texte_menu_credis.position(0, 0, 450, 125))
        ecran.blit(self.texte_menu_quitter.afficher(), self.texte_menu_quitter.position(0, 0, 450, 155))
        #ecran.blit(self.texte_compteur.afficher(str(self.compteur)), self.texte_compteur.position(0, 1, 97, 95))  
        #Dessiner le pointeur. 
        self.pointeur.afficher(ecran)
        



class SceneJeu(Scene):
    "Scene du jeu."
    def __init__(self):
        #Initialisation de la scene
        Scene.__init__(self)
        #Chargement de l'image de fond de la scene
        self.fond = fonction.charger_image("fond.jpg")
        #Creation des objets.
        self.bulles = bulles.Bulles()
        self.nourriture = nourriture.Nourriture()
        self.poissons = poissons.Poissons()
        #Variables de controle.
                      
    def evenements(self, evenement = None):
        "Lire les evenements pour déterminer les action ou la scene correspondante."
        pass
        
    def evenements_clavier(self, clavier = None):
        "Lire les evenements clavier pour déterminer les action ou la scene correspondante." 
        #print clavier
        if clavier:
            touche = clavier.key
            if touche == pygame.K_r: #retour
                self.changer_scene(SceneInitiale())
        
    def evenements_souris(self, souris = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante."
        if souris:
            if souris.type == pygame.MOUSEBUTTONDOWN: # clic souris
                bouton = souris.button
                position = souris.pos
                if bouton == 1 or bouton == 3: #bouton gauche ou droit de la souris
                    self.poissons.evenements_souris(bouton,position)
                #if bouton == 1:
                    #self.poissons.evenements_souris(position)
                #if bouton == 3: #clic droit je ballance d ela nourriture
                    #self.nourriture.evenements_souris(position)
                
    def evenements_joystick(self, joystick = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante."
        if joystick:
            if joystick.type == pygame.JOYAXISMOTION:
                pass
                #axe = joystick.axis
                #sens = joystick.value
                #self.poisson_bleu.evenements_joystick(axe,sens)
            elif joystick.type == pygame.JOYBUTTONDOWN:
                bouton = joystick.button
                if bouton == 9: #bouton START !!! MENU PAUSE !!!
                    self.changer_scene(SceneInitiale())
                #else:
                    #self.gorille.evenements_joystick(bouton)
    
    def actualiser(self): 
        #Actualisation n'affiche rien
        self.bulles.actualiser()
        self.nourriture.actualiser()
        self.poissons.actualiser()
        #self.poisson_1.actualiser()
        #self.poisson_2.actualiser()
        #self.poisson_3.actualiser()
        #self.poisson_4.actualiser()
        # Passage au niveau 2 ou jeu fini
   
    def afficher(self, ecran):
        "Afficher les objets sur l'ecran."
        #Remplissage en noir
        ecran.fill( (0x11, 0x11, 0x11) )  
        #Image de fond
        ecran.blit(self.fond, (0, 0)) 
        self.bulles.afficher(ecran)
        self.nourriture.afficher(ecran)
        self.poissons.afficher(ecran)
        #Dessiner les poissons.
        #self.poisson_1.afficher(ecran)
        #self.poisson_2.afficher(ecran)
        #self.poisson_3.afficher(ecran)
        #self.poisson_4.afficher(ecran)
        #Dessiner les textes.
        #ecran.blit(self.texte_compteur.afficher(str(self.points)), self.texte_compteur.position(2, 2, 7, 7))
        #ecran.blit(self.texte_vies.afficher(str(self.vies)), self.texte_vies.position(0, 2, 7, 7))
        


class SceneCredis(Scene):
    "Scene menu : affiche le menu."
    def __init__(self):
        #Initialisation de la scene
        Scene.__init__(self)
        #Chargement de l'image de fond de la scene
        self.fond = fonction.charger_image("fond.jpg")
        #Chargement des objets
        self.bulles = bulles.Bulles() 
        self.pointeur = pointeur.Pointeur(15,24) 
        #self.pointeur.positionner(15,3) 
        self.poisson_1 = poisson.Poisson()
        self.poisson_2 = poisson.Poisson()
        self.poisson_3 = poisson.Poisson()
        self.poisson_4 = poisson.Poisson()
        
        #Chargement de la musique de fond 
        #self.musique = pygame.mixer.music.load("./sons/bouge.ogg")
        #self.musique.set_volume(0.5)
        #self.musique.fadeout(400) 
    
        #Chargement des textes à afficher
        self.texte_titre = fonction.Texte("Aquarium", 50, constante.noir)
        self.texte_stitre = fonction.Texte("Credits", 20, constante.gris)
        self.credis = credis.lire_credis()
        self.texte_credis = fonction.Texte_multiligne( (self.credis) )
        self.texte_credis.position(0, 0, 430, 95)
        self.texte_retour = fonction.Texte(" > Retour [R]",30, constante.bleufonce)
       
    
    def evenements_clavier(self, clavier = None):
        "Lire les evenements clavier pour déterminer les action ou la scene correspondante." 
        if clavier:
            touche = clavier.key
            if touche == pygame.K_r or touche == pygame.K_RETURN: #retour au menu
                self.changer_scene(SceneInitiale())


    def evenements_souris(self, souris = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante." 
        if souris: #print souris
            if souris.type == pygame.MOUSEBUTTONDOWN: # clic souris
                bouton = souris.button
                position = souris.pos
                if bouton == 1: # si clic droit
                    if 450 < position[0] < 600 and 725 < position[1] < 745: #retour 
                        self.changer_scene(SceneInitiale())
                if bouton == 3: #si clic gauche
                    self.changer_scene(SceneInitiale()) #retour
                
    
    def evenements_joystick(self, joystick = None):
        "Lire les evenements souris pour déterminer les action ou la scene correspondante."
        if joystick:           
            if joystick.type == pygame.JOYBUTTONDOWN: # les boutons
                bouton = joystick.button
                if bouton == 9 or bouton == 1 or bouton == 2:
                    self.changer_scene(SceneInitiale()) #retour     
                      

    def actualiser(self): 
        #actualisation
        self.bulles.actualiser()
        self.poisson_1.actualiser()
        self.poisson_2.actualiser()
        self.poisson_3.actualiser()
        self.poisson_4.actualiser()
        
            
    def afficher(self, ecran):
        #Remplissage en noir
        ecran.fill( (0x11, 0x11, 0x11) )  
        #Image de fond
        ecran.blit(self.fond, (0, 0))   
        #Dessiner les objets. 
        self.bulles.afficher(ecran)
        self.poisson_1.afficher(ecran)
        self.poisson_2.afficher(ecran)
        self.poisson_3.afficher(ecran)
        self.poisson_4.afficher(ecran)
        #Dessiner les textes.
        ecran.blit(self.texte_titre.afficher(), self.texte_titre.position(1, 0, 0, 15))
        ecran.blit(self.texte_stitre.afficher(), self.texte_stitre.position(1, 0, 20, 50))
        self.texte_credis.afficher(ecran, 0)    
        ecran.blit(self.texte_retour.afficher(), self.texte_retour.position(1, 2, 27, 23))
        #Dessiner le pointeur. 
        self.pointeur.afficher(ecran)
    
  


        
