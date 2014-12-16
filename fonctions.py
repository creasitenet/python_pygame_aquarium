#! /usr/bin/python
# -*- coding: utf-8 -*-
# Ecrit par : Edouard Boissel
# Licence : LGPL
# Date : 03/06/12
'''Fonctions communes.'''

import os #sys
import pygame
import constantes as constante

if not pygame.font: print ("Attention, fonts desactives")
if not pygame.mixer: print ("Warning, sons desactives")


def continuer(evenement):
    '''Definie la fin du programme par pression de la touche [Escape].'''
    for e in evenement:
        if e.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
            return False      #retourne False (faux)
        elif e.type == pygame.KEYDOWN: #Si un de ces événements est de type touche clavier
            if e.key == pygame.K_ESCAPE or e.key == pygame.K_a: # si on appuie sur ESC ou q (pygame qwerty)
                return False # retourne False (faux)
    return True #par defaut continuer vaut True (Vrai)

def pause(touche):
    pause = 0
    if touche == 112:
        pause=1
        pygame.time.wait(100)
            
def charger_image(nom, alpha = False, repertoire = "images"):
    '''Charge une image du répertoire prédéfini.'''
    chemin = os.path.join(repertoire, nom)
    try:
        image = pygame.image.load(chemin)
    except pygame.error(message):
        print("Impossible de charger l'image : ", chemin)
        raise SystemExit(message)
        
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

'''if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()'''


def charger_son(nom, repertoire = "sons"):
    '''Charge un son du répertoire prédéfini.'''
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    chemin = os.path.join(repertoire, nom)
    try:
        son = pygame.mixer.Sound(chemin)
    except pygame.error(message):
        print ("Impossible de charger le son : ", chemin)
        raise SystemExit(message)
    return son


def charger_police(nom,  taille = 36):
    chemin = os.path.join('data', nom)
    return pygame.font.Font(chemin, taille)


class Texte():
    '''Cree un texte pour l'afficher.'''
    def __init__(self, txt= "", taille= 24, couleur= (0, 0, 0), police= None):
        #Initialise le texte.
        self.police = pygame.font.Font(police, taille)
        self.txt = txt
        self.texte = None #on vide la variable texte
        self.rect = None #idem pour le rectangle
        self.couleur = couleur
        self.afficher()
        
    def afficher(self, chaine= ""):
        #Affiche le texte.
        self.texte = self.police.render(self.txt + chaine, True, self.couleur)
        self.rect = self.texte.get_rect()
        return self.texte
        
    def changer_couleur(self, couleur):
        #Change la couleur du texte.
        self.couleur = couleur
        
    def position(self, x= 0, y= 0, offset_x= 0, offset_y= 0):
        #Définir la position a laquelle afficher le texte sur l'ecran  
    
        #"Horizontalement 0 = haut, 1 = milieu, 2= bas"
        if y == 0:
            self.rect.top = offset_y
        elif y == 1:
            self.rect.centery = constante.HAUTEUR / 2 + offset_y
        elif y == 2:
            self.rect.bottom = constante.HAUTEUR - offset_y
            
        #"Verticalement 0 = gauche, 1 = milieu, 2= droite"
        if x == 0:
            self.rect.left = offset_x
        elif x == 1:
            self.rect.centerx = constante.LARGEUR / 2 + offset_x
        elif x == 2:
            self.rect.right = constante.LARGEUR - offset_x
        return self.rect
      


class Texte_multiligne():
    '''Classe pour afficher plusieurs lignes de texte.'''
    def __init__(self, lignes = (""), taille= 24, couleur= (0, 0, 0), police = None):
        #"Initialise les multiples lignes de texte."
        self.police = pygame.font.Font(police, taille)
        self.lignes = lignes
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.texte = []
        self.rects = []
        self.taille = [0, 0]
        self.couleur = couleur
        self.generer()
        
    def generer(self):
        #"Generer un texte pour chaque chaine et le rectangle conteneur."
        for ligne in self.lignes:
            #Creer les nouveaux textos et leurs postions.
            self.texte.append(self.police.render(ligne, True, self.couleur))
            self.rects.append(self.texte[-1].get_rect())
            #Creer le conteneur de tous les textes.
            if self.rects[-1].w > self.rect.w:
                self.rect.w = self.rects[-1].w
            self.rect.h += self.rects[-1].h

    def changer_couleur(self, couleur):
        #"Change la couleur du texte."
        self.couleur = couleur
        
    def afficher(self, ecran, aligner = 0):
        #"Afficher les textes sur l'ecran."
        for i in range(0, len(self.rects)):
            self.rects[i].top = self.rect.top + self.rects[i].h * i
            self.alignement(aligner)
            ecran.blit(self.texte[i], self.rects[i])
        
    def position(self, x= 0, y= 0, offset_x= 0, offset_y= 0):
        #"Definie la position du conteneur sur l'écran."
        if y == 0:
            self.rect.top = offset_y
        elif y == 1:
            self.rect.centery = constante.HAUTEUR / 2 + offset_y
        elif y == 2:
            self.rect.bottom = constante.HAUTEUR - offset_y
        if x == 0:
            self.rect.left = offset_x
        elif x == 1:
            self.rect.centerx = constante.LARGEUR / 2 + offset_x
        elif x == 2:
            self.rect.right = constante.LARGEUR - offset_x

    def alignement(self, aligner= 0):
        #"Definie l'alignement de chaque texte dans le conteneur."
        for rect in self.rects:
            if aligner == 0:
                rect.left = self.rect.left
            elif aligner == 1:
                rect.centerx = self.rect.centerx
            elif aligner == 2:
                rect.right = self.rect.right
