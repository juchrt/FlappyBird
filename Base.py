import pygame

class Base:
    def __init__(self):
        self.position = self.pos_x, self.pos_y = 0, 400
        self.img = pygame.image.load('base.png').convert_alpha()

    def infinie(self, ecran):
        ecran.blit(self.img, (self.pos_x, self.pos_y))
        ecran.blit(self.img, (self.pos_x + 252, self.pos_y))
        self.pos_x -= 2
        if self.pos_x <= -252 :
            self.pos_x = 0 