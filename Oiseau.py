import pygame


class Oiseau:
    def __init__(self):
        self.img = pygame.image.load('oiseau.png').convert_alpha()
        self.position = self.pos_x, self.pos_y = 100, 250
        self.rect = self.img.get_rect(center = self.position)
        self.chute_oiseau = True

    def saut(self):
        if pygame.key.get_pressed()[pygame.K_UP] and self.chute_oiseau:
            self.chute_oiseau = False
            self.position = (self.pos_x, self.pos_y - 40)
            self.vitesse = 0
        if not pygame.key.get_pressed()[pygame.K_UP] and not self.chute_oiseau:
            self.chute_oiseau = True

    def collision_ou_pas(self, liste_tuyaux):
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            running = False
        for i in liste_tuyaux:
            if self.rect.colliderect(i):
                    running = False