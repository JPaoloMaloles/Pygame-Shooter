import pygame
class EnemyClass():
    def __init__(self, input):
        self.color = input["color"]
        self.position = pygame.Vector2(
            input['x_position'], input['y_position'])
        self.surface = pygame.Surface((10, 10))
        self.rectangle = self.surface.get_rect(topleft=(self.position))

    def fill(self, display_surface):
        self.rectangle = self.surface.get_rect(topleft=self.position)
        self.surface.fill(f'{self.color}')
        display_surface.blit(self.surface, self.position)
        print(f"surface rendered at {self.position}")
        pygame.draw.rect(display_surface, 'Green', self.rectangle, 1)

    def chase(self, player_position):
        a = self.position.x
        b = self.position.y
        print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {player_position}')
        # print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {self.position.x}')
        # print(
        #     f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {(player_position.x - self.position.x)/0.5}')
        if abs((player_position.x - self.position.x)/0.5) >= 0.5:
            # print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@ {((a - player_position.x)/0.5):12f}')
            if player_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((player_position.x - self.position.x) /
                     ((player_position.x - self.position.x)/0.5))
            else:
                self.position.x = self.position.x - \
                    ((player_position.x - self.position.x) /
                     ((player_position.x - self.position.x)/0.5))
        if abs((player_position.y - self.position.y)/0.5) >= 0.5:
            # print(
            #     f'!!!!!!!!!!!!!!!!!!!!!!!! {((b - player_position.y)/0.5):12f}')
            if player_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((player_position.y - self.position.y) /
                     ((player_position.y - self.position.y)/0.5))
            else:
                self.position.y = self.position.y - \
                    ((player_position.y - self.position.y) /
                     ((player_position.y - self.position.y)/0.5))
    