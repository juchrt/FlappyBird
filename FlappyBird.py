#flappybird de Julie Chartier et Lucas Lacoste en L1 SDN pour le cours de programmation avancée
import pygame

#initialisation pygame
successes, failures = pygame.init()

#définition de l'écran
screen_size = width, height = (1000, 600)
screen = pygame.display.set_mode(screen_size)

#l'horloge
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)

#caractéristiques de "l'oiseau"
bird_color = pygame.Color(255, 0, 0)
bird_pos = (300, 200)
bird_dim = bird_width, bird_width = 30, 30

#préchargment de "l'oiseau"
pygame.draw.rect(screen, bird_color, (bird_pos, bird_dim))

#données pour la chut uniforme
acceleration = 1 * 0.001
vitesse = (0,0)
delta_t = clock.tick(FPS)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    #saut de "l'oiseau"
    if pygame.key.get_pressed()[pygame.K_UP]:
        vitesse = (0, 0)
        bird_pos = (bird_pos[0], bird_pos[1] -12)
    isPressed = False
    #chute uniforme
    if not isPressed :
        vitesse = (vitesse[0] + acceleration * delta_t, vitesse[1] + acceleration * delta_t)
        bird_pos = (bird_pos[0], bird_pos[1] + vitesse[1] * delta_t)

    screen.fill(pygame.color.Color(0, 0, 0))
    pygame.draw.rect(screen, bird_color, (bird_pos, bird_dim))
    pygame.display.update()
pygame.quit()