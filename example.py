import pygame
from sys import exit

pygame.init()
display_surface = pygame.display.set_mode((800,400))
running = True
game_running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.quit()