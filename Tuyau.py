import pygame
import random

class Tuyau:
    def __init__(self):
        self.img = pygame.image.load('tuyau copy.png').convert_alpha()
        self.liste_tuyaux = []
        self.liste_hauteurs_possibles = [130, 160, 190, 220, 250, 280, 310, 330]
    
    def nouveaux(self):
        position_hasard = random.choice(self.liste_hauteurs_possibles)
        nouveauTuyau1 = self.img.get_rect(midtop = (500, position_hasard))
        nouveauTuyau2 = self.img.get_rect(midbottom = (500, position_hasard - 100))
        return nouveauTuyau1, nouveauTuyau2

    def afficher(self, tuyaux, ecran):
        for tuyau in tuyaux:
            if tuyau.bottom >= 400:
                ecran.blit(self.img, tuyau)
            else:
                autre = pygame.transform.flip(self.img, False, True)
                ecran.blit(autre, tuyau)

    def mouvement(self, tuyaux):
        for tuyau in tuyaux:
            tuyau.centerx -= 2
        return tuyaux


