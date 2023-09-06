import pygame
class ProjectileClass():
    def __init__(self, input):
        self.projectile_color = input["projectile_color"]
        self.position = pygame.Vector2(
            input['x_position'], input['y_position'])
        self.projectile = pygame.Surface((10, 10))
        self.rectangle = test_surface.get_rect(topleft=(self.position))

    def fill(self):
        self.projectile.fill(f'{self.projectile_color}')
        display_surface.blit(self.projectile, self.position)
        print(f"projectile rendered at {self.position}")
        print(f'player position at {player_pos}')

    def chase(self):
        a = self.position.x
        b = self.position.y
        print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {player_pos.x}')
        print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {self.position.x}')
        # print(
        #     f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {(player_pos.x - self.position.x)/0.5}')
        if abs((player_pos.x - self.position.x)/0.5) >= 0.5:
            print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@ {((a - player_pos.x)/0.5):12f}')
            if player_pos.x > self.position.x:
                self.position.x = self.position.x + \
                    ((player_pos.x - self.position.x) /
                     ((player_pos.x - self.position.x)/0.5))
            else:
                self.position.x = self.position.x - \
                    ((player_pos.x - self.position.x) /
                     ((player_pos.x - self.position.x)/0.5))
        if abs((player_pos.y - self.position.y)/0.5) >= 0.5:
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!! {((b - player_pos.y)/0.5):12f}')
            if player_pos.y > self.position.y:
                self.position.y = self.position.y + \
                    ((player_pos.y - self.position.y) /
                     ((player_pos.y - self.position.y)/0.5))
            else:
                self.position.y = self.position.y - \
                    ((player_pos.y - self.position.y) /
                     ((player_pos.y - self.position.y)/0.5))
    