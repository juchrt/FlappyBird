#FlappyBird de Lucas Lacoste et Julie Chartier en L1 SDN pour le cours de programmation avancée
import pygame
from Fond import *
from Base import *
from Tuyau import *
from Oiseau import *

#fonctions pour afficher le score 
def score1(jouer):
    if jouer == 'pdt_partie' :
        affichage = game_font.render(str(int(score)),True,(255,255,255))
        score_pos = affichage.get_rect(center = (130,50))
        ecran.blit(affichage, score_pos)
    elif jouer == 'perdu': 
        affichage = game_font.render(str(int(score)),True,(255,255,255))
        score_pos = affichage.get_rect(center = (130,50))
        ecran.blit(perdu, perdu_pos)
        ecran.blit(affichage, score_pos)
    
def score2():
    affichage = game_font.render(str(int(scoretest)),True,(255,255,255))
    score_pos = affichage.get_rect(center = (130,50))
    ecran.blit(affichage, score_pos)

#initialisation pygame
successes, failures = pygame.init()

#l'horloge
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)

#définition de l'écran
ecran_dim = largeur, hauteur = (252, 500)
ecran = pygame.display.set_mode(ecran_dim)

#création du fond
fond = Fond()

#création de la base
base = Base()

#création des tuyaux
coupleTuyaux = Tuyau()

#timer tuyaux
CREATIONTUYAUX = pygame.USEREVENT
pygame.time.set_timer(CREATIONTUYAUX, 1400)

#création de l'oiseau
oiseau = Oiseau()
vitesse = 0
acceleration = 1 * 0.001
delta_t = clock.tick(FPS)

#score
score = -2
scoretest = 0
game_font = pygame.font.Font(None,40)
perdu = pygame.image.load('perdu.png').convert_alpha()
perdu_pos = perdu.get_rect(center = (121,250))

#bienvenue 
bienvenue = pygame.image.load('bienvenue.png').convert_alpha()
bienvenue_pos = bienvenue.get_rect(center = (121,250))

running = True
chute_oiseau = True
partieEnCours = False

while running :
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREATIONTUYAUX:
            coupleTuyaux.liste_tuyaux.extend(coupleTuyaux.nouveaux())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and partieEnCours == False:
                partieEnCours = True 
                coupleTuyaux.liste_tuyaux.clear()
                oiseau.rect.center = (100,250)
                score = -2
    
    #affichage du fond
    ecran.blit(fond.img, fond.position)
    
    if not partieEnCours and score <= -2:
        ecran.blit(bienvenue, bienvenue_pos)
        ecran.blit(oiseau.img, oiseau.rect)
    elif partieEnCours:
        #affichage des tuyaux
        coupleTuyaux.liste_tuyaux = coupleTuyaux.mouvement(coupleTuyaux.liste_tuyaux)
        coupleTuyaux.afficher(coupleTuyaux.liste_tuyaux, ecran)

        #affichage de la base
        base.infinie(ecran)

        #chute uniforme
        if chute_oiseau :
            vitesse = (vitesse + acceleration * delta_t)
            oiseau.rect.center = (oiseau.rect.center[0], oiseau.rect.center[1] + vitesse)
    
        #saut
        if pygame.key.get_pressed()[pygame.K_UP] and chute_oiseau:
                chute_oiseau = False
                oiseau.rect.center = (oiseau.rect.center[0], oiseau.rect.center[1] - 40)
                vitesse = 0
        if not pygame.key.get_pressed()[pygame.K_UP] and not chute_oiseau:
                chute_oiseau = True

        #collisions
        if oiseau.rect.top <= 0 or oiseau.rect.bottom >= 400:
            partieEnCours = False
        for i in coupleTuyaux.liste_tuyaux:
            if oiseau.rect.colliderect(i):
                    partieEnCours = False

        #score
        score += 0.0125
        if score >= 0 :
            score1('pdt_partie') 
        else :
            score2()
    elif not partieEnCours :
        score1('perdu')

    #affichage de l'oiseau
    ecran.blit(oiseau.img, oiseau.rect)
    pygame.display.update()
pygame.quit()