import pygame
from sys import exit
import random
import time
from Player import PlayerClass
from Enemy import EnemyClass
from Projectiles import ProjectileClass, ClassicProjectile, BlastProjectile, FollowProjectile
import math


pygame.init()
display_surface = pygame.display.set_mode((800, 400))
running = True
game_running = False
player_objects = []  # Make sure when ending games to set this to 0
enemy_objects = []
dying_enemy_ids = []
dying_projectile_ids = []
existing_projectiles = []
last_enemy_creation_timestamp = []
time_since_last_projectile_created = 0
clock = pygame.time.Clock()
dt = 0


def out_of_bounds(player_position, player_surface):
    # stops player from leaving the screen
    if player_position.x > display_surface.get_width() - player_surface.get_width():
        player_position.x = display_surface.get_width() - player_surface.get_width()
        print('right boundary')
    if player_position.x < 0:
        player_position.x = 0
        print('left boundary')
    if player_position.y > display_surface.get_height() - player_surface.get_height():
        player_position.y = display_surface.get_height() - player_surface.get_height()
        print('bottom boundary')
    if player_position.y < 0:
        player_position.y = 0
        print('top boundary')


def time_display(time_passed):
    time_passed_text = pygame.font.SysFont(
        'timesnewroman',  30).render(f'time: {time_passed}', True, "white", "black")

    fps = round(clock.get_fps())
    fps_text = pygame.font.SysFont(
        'timesnewroman',  30).render(f'fps: {fps}', True, "white", "black")
    display_surface.blit(time_passed_text, (0, 0))
    display_surface.blit(
        fps_text, (display_surface.get_width()-fps_text.get_width(), 0))


def create_enemy():
    if time_passed % 3 == 0:
        if time_passed not in last_enemy_creation_timestamp:
            print(f'exact {pygame.time.get_ticks()}')
            print(f'create projectile-------------------------{time_passed}')
            print(len(enemy_objects))
            enemy_objects.append(time_passed)
            last_enemy_creation_timestamp.append(time_passed)
            print(f'pastprojectiles 0: {last_enemy_creation_timestamp[0]}')
            enemy_objects[len(enemy_objects) - 1] = EnemyClass(
                {'color': 'red', 'x_position': player_position.x, 'y_position': random.randint(0, display_surface.get_height()), 'display_surface': display_surface})
            print(
                f'pastprojectiles AFTER: {enemy_objects[len(enemy_objects) - 1]}')
            enemy_objects[0].fill(display_surface)

        if len(last_enemy_creation_timestamp) > 1:
            last_enemy_creation_timestamp.pop(0)


def player_enemy_collision(player_rect):
    continue_game = True
    for index, enemy in enumerate(enemy_objects):
        if pygame.Rect.colliderect(player_rect, enemy.rectangle):
            continue_game = False
    return continue_game


def projectile_enemy_collision(projectile_rect, projectile_index):
    print(f'number of enemies: {len(enemy_objects)}')
    for index, enemy in enumerate(enemy_objects):
        if pygame.Rect.colliderect(projectile_rect, enemy.rectangle):
            if index not in dying_enemy_ids:
                print(f'projectile index is: {projectile_index}')
                dying_projectile_ids.append(projectile_index)
                dying_enemy_ids.append(index)

    return dying_enemy_ids, dying_projectile_ids


def player_movement(player_position):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 200 * dt
    if keys[pygame.K_s]:
        player_position.y += 200 * dt
    if keys[pygame.K_a]:
        player_position.x -= 200 * dt
    if keys[pygame.K_d]:
        player_position.x += 200 * dt


def player_click(time_since_last_projectile_created):
    mouse_click = pygame.mouse.get_pressed()
    if time_passed - time_since_last_projectile_created >= 1:
        if mouse_click[0]:
            time_since_last_projectile_created = time_passed
            go_right = False
            go_down = False
            target_position = pygame.Vector2(0, 0)
            existing_projectiles.append("f")

            target_position = pygame.Vector2(
                pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if target_position.x > player_position.x:
                go_right = True
            else:
                go_right = False

            if target_position.y > player_position.y:
                go_down = True
            else:
                go_down = False

            x_length_diff = abs(target_position.x-player_position.x)
            y_length_diff = abs(target_position.y-player_position.y)
            hypotenuse = math.hypot(x_length_diff, y_length_diff)

            angle = math.acos(x_length_diff/hypotenuse)

            existing_projectiles[len(existing_projectiles)-1] = ClassicProjectile(
                {'color': 'orange', 'x_position': player_position.x, 'y_position': player_position.y, 'mouse_position': target_position, 'go_right': go_right, 'go_down': go_down, 'angle': angle})
        if mouse_click[1]:
            time_since_last_projectile_created = time_passed
            existing_projectiles.append("f")
            existing_projectiles[len(existing_projectiles)-1] = BlastProjectile(
                {'color': 'green', 'x_position': player_position.x, 'y_position': player_position.y, 'mouse_position': pygame.Vector2(
                    pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])})
        if mouse_click[2]:
            time_since_last_projectile_created = time_passed
            existing_projectiles.append("f")
            existing_projectiles[len(existing_projectiles)-1] = FollowProjectile(
                {'color': 'Pink', 'x_position': player_position.x, 'y_position': player_position.y, 'mouse_position': pygame.Vector2(
                    pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])})
    return time_since_last_projectile_created


# ------------------------------------------------------ game cycle
while running:
    time_passed = round(pygame.time.get_ticks() * 0.001, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(player_objects) == 0:
                    player_position = pygame.Vector2(
                        display_surface.get_width() / 2, display_surface.get_height() / 2)
                    print(f'{player_position}')
                    player_objects.append('a')
                    player_objects[len(player_objects)-1] = PlayerClass(
                        {'player_position': player_position, 'player_color': 'white', 'player_surface': pygame.Surface((10, 10))})
                    print('player created')
                    game_running = True

    while game_running:
        floor_surface = pygame.Surface((display_surface.get_width(), 100))
        floor_surface.fill('Blue')
        floor_rect = floor_surface.get_rect(
            topleft=(0, display_surface.get_height() - floor_surface.get_height()))

        time_passed = round(pygame.time.get_ticks() * 0.001, 1)
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player_objects = []
                    enemy_objects = []
                    existing_projectiles = []
                    last_enemy_creation_timestamp = []
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
        player_movement(player_position)
        time_since_last_projectile_created = player_click(
            time_since_last_projectile_created)
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_position.y -= 300 * dt
        # if keys[pygame.K_s]:
        #     player_position.y += 300 * dt
        # if keys[pygame.K_a]:
        #     player_position.x -= 300 * dt
        # if keys[pygame.K_d]:
        #     player_position.x += 300 * dt

        # print(f'@@@@@@@@@@@@@ {player_position.x}')
        # print(f'~~~~~~~~~~~~~ {player_position.y}')
        create_enemy()
        # ------------------------------------------------------ rendering graphics
        display_surface.fill('Purple')
        display_surface.blit(
            floor_surface, (0, display_surface.get_height() - floor_surface.get_height()))

        time_display(time_passed)
        for enemy in enemy_objects:
            enemy.chase(player_position)
            enemy.fill(display_surface)
            # put missile collision here

        for player in player_objects:
            out_of_bounds(player_position, player.player_surface)
            player.render(display_surface, player_position)
            game_running = player_enemy_collision(player.player_rect)

        for index, projectile in enumerate(existing_projectiles):
            if getattr(projectile, 'shoot', False):
                projectile.shoot(dt)
            if getattr(projectile, 'tracking', False):
                projectile.tracking(dt)
            projectile.fill(display_surface)
            dying_enemy_ids, dying_projectile_ids = projectile_enemy_collision(
                projectile.rectangle, index)
            # print('======================================')
            # print('======================================')
            # print(f'length of enemy ids, length of projectile ids: {len(dying_enemy_ids)} and {len(dying_projectile_ids)}')
            # print('======================================')
            # print('======================================')

        for id in dying_enemy_ids:
            print(f'length of enemy objects: {len(enemy_objects)}')
            enemy_objects.pop(id)
        for id in dying_projectile_ids:
            print(f'THE PROJECTILE ID IS {id}')
            print(
                f'length of existing_projectiles: {len(existing_projectiles)}')
            existing_projectiles.pop(id)

        dying_enemy_ids = []
        dying_projectile_ids = []

        if not game_running:
            player_objects = []
            enemy_objects = []
            existing_projectiles = []
            last_enemy_creation_timestamp = []

        pygame.display.flip()
        print(f'gamerunning is : {game_running}')
    time_display(time_passed)
    display_surface.fill('Blue')
    pygame.display.flip()


pygame.quit()
