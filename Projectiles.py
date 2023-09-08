import pygame
class ProjectileClass:
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
        print(f"Projectile rendered at {self.position}")
        pygame.draw.rect(display_surface, 'Blue', self.rectangle, 1)

class BlastProjectile(ProjectileClass):
    def __init__(self, input):
        super().__init__(input)
        self.target_position = input["mouse_position"]

    def shoot(self):
        print(f' mouse x position is {self.target_position.x}')
        if abs((self.target_position.x - self.position.x)/0.5) >= 0.5:
            if self.target_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((self.target_position.x - self.position.x) /
                     ((self.target_position.x - self.position.x)/2))
            else:
                self.position.x = self.position.x - \
                    ((self.target_position.x - self.position.x) /
                     ((self.target_position.x - self.position.x)/2))
        if abs((self.target_position.y - self.position.y)/0.5) >= 0.5:
            if self.target_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((self.target_position.y - self.position.y) /
                     ((self.target_position.y - self.position.y)/2))
            else:
                self.position.y = self.position.y - \
                    ((self.target_position.y - self.position.y) /
                     ((self.target_position.y - self.position.y)/2))
                     


class FollowProjectile(ProjectileClass):
    def __init__(self, input):
        super().__init__(input)
        self.target_position = input["mouse_position"]

    def tracking(self):
        dynamic_mouse_position = pygame.Vector2(
            pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        print(f' mouse x position is {dynamic_mouse_position.x}')
        if abs((dynamic_mouse_position.x - self.position.x)/0.5) >= 0.5:
            if dynamic_mouse_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((dynamic_mouse_position.x - self.position.x) /
                     ((dynamic_mouse_position.x - self.position.x)/2))
            else:
                self.position.x = self.position.x - \
                    ((dynamic_mouse_position.x - self.position.x) /
                     ((dynamic_mouse_position.x - self.position.x)/2))
        if abs((dynamic_mouse_position.y - self.position.y)/0.5) >= 0.5:
            if dynamic_mouse_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((dynamic_mouse_position.y - self.position.y) /
                     ((dynamic_mouse_position.y - self.position.y)/2))
            else:
                self.position.y = self.position.y - \
                    ((dynamic_mouse_position.y - self.position.y) /
                     ((dynamic_mouse_position.y - self.position.y)/2))


# class CreateProjectile:
#     def __init__(self, input):
#         self.projectile_color = input["projectile_color"]
#         self.position = pygame.Vector2(
#             input['x_position'], input['y_position'])
#         self.projectile = pygame.Surface((10, 10))
#         self.rectangle = test_surface.get_rect(topleft=(self.position))

#     def fill(self):
#         self.projectile.fill(f'{self.projectile_color}')
#         display_surface.blit(self.projectile, self.position)
#         print(f"projectile rendered at {self.position}")
#         print(f'player position at {player_pos}')

#     def chase(self):
#         a = self.position.x
#         b = self.position.y
#         print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {player_pos.x}')
#         print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {self.position.x}')
#         # print(
#         #     f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {(player_pos.x - self.position.x)/0.5}')
#         if abs((player_pos.x - self.position.x)/0.5) >= 0.5:
#             print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@ {((a - player_pos.x)/0.5):12f}')
#             if player_pos.x > self.position.x:
#                 self.position.x = self.position.x + \
#                     ((player_pos.x - self.position.x) /
#                      ((player_pos.x - self.position.x)/0.5))
#             else:
#                 self.position.x = self.position.x - \
#                     ((player_pos.x - self.position.x) /
#                      ((player_pos.x - self.position.x)/0.5))
#         if abs((player_pos.y - self.position.y)/0.5) >= 0.5:
#             print(
#                 f'!!!!!!!!!!!!!!!!!!!!!!!! {((b - player_pos.y)/0.5):12f}')
#             if player_pos.y > self.position.y:
#                 self.position.y = self.position.y + \
#                     ((player_pos.y - self.position.y) /
#                      ((player_pos.y - self.position.y)/0.5))
#             else:
#                 self.position.y = self.position.y - \
#                     ((player_pos.y - self.position.y) /
#                      ((player_pos.y - self.position.y)/0.5))