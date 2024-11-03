import pygame

class Fond:
    def __init__(self):
        self.position = (0, 0)
        self.img = pygame.image.load('fond.png').convert_alpha()