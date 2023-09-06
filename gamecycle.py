import pygame
from sys import exit
import random
import time
from Player import PlayerClass

pygame.init()
display_surface = pygame.display.set_mode((800,400))
running = True
game_running = False
player_objects = [] #Make sure when ending games to set this to 0
clock = pygame.time.Clock()
dt = 0

# ------------------------------------------------------ game cycle
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(player_objects) == 0:
                    player_position = pygame.Vector2(display_surface.get_width() / 2, display_surface.get_height() / 2)
                    print(f'{player_position}')
                    player_objects.append('a')
                    player_objects[len(player_objects)-1] = PlayerClass({'player_position': player_position, 'player_color':'white', 'player_surface':pygame.Surface((10, 10))})
                    print('player created')
                    game_running = True
    
    while game_running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player_objects = []
                    game_running = False
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     players.append('a')
    #     players[len(players)-1] = PlayerClass({'display_surface': display_surface, 'player_color':'white', 'player_surface':pygame.Surface((10, 10))})
    #     print('player created')
    #     print('-----')
    #     for player in players:
    #         print(player)
    #     print('=====')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_position.y -= 300 * dt
        if keys[pygame.K_s]:
            player_position.y += 300 * dt
        if keys[pygame.K_a]:
            player_position.x -= 300 * dt
        if keys[pygame.K_d]:
            player_position.x += 300 * dt

    # ------------------------------------------------------ rendering graphics
        display_surface.fill('Purple')
        for player in player_objects:
            print(len(player_objects))
            print(player)
            player.render(display_surface, player_position)
            # display_surface.blit(player.player_surface, player_rect)
        pygame.display.flip()
        




    


pygame.quit()