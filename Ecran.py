import pygame

class Ecran:
    def __init__(self):
        self.dimensions = width, height = (252, 500)

    def afficher(self):
        pygame.display.set_mode(self.dimensions)