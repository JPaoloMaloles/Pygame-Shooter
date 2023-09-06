import pygame
class ProjectileClass():
    def __init__(self, input):
        self.projectile_color = input["projectile_color"]
        self.position = pygame.Vector2(
            input['x_position'], input['y_position'])
        self.projectile = pygame.Surface((10, 10))
        self.rectangle = input['display_surface'].get_rect(topleft=(self.position))

    def fill(self, display_surface):
        self.projectile.fill(f'{self.projectile_color}')
        display_surface.blit(self.projectile, self.position)
        print(f"projectile rendered at {self.position}")

    def chase(self, player_position):
        a = self.position.x
        b = self.position.y
        print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {player_position.x}')
        print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {self.position.x}')
        # print(
        #     f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {(player_position.x - self.position.x)/0.5}')
        if abs((player_position.x - self.position.x)/0.5) >= 0.5:
            print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@ {((a - player_position.x)/0.5):12f}')
            if player_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((player_position.x - self.position.x) /
                     ((player_position.x - self.position.x)/0.5))
            else:
                self.position.x = self.position.x - \
                    ((player_position.x - self.position.x) /
                     ((player_position.x - self.position.x)/0.5))
        if abs((player_position.y - self.position.y)/0.5) >= 0.5:
            print(
                f'!!!!!!!!!!!!!!!!!!!!!!!! {((b - player_position.y)/0.5):12f}')
            if player_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((player_position.y - self.position.y) /
                     ((player_position.y - self.position.y)/0.5))
            else:
                self.position.y = self.position.y - \
                    ((player_position.y - self.position.y) /
                     ((player_position.y - self.position.y)/0.5))
    