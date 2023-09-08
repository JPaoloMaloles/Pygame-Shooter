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
        # print(f"Projectile rendered at {self.position}")
        pygame.draw.rect(display_surface, 'Blue', self.rectangle, 1)

class BlastProjectile(ProjectileClass):
    def __init__(self, input):
        super().__init__(input)
        self.target_position = input["mouse_position"]

    def shoot(self, dt):
        # print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {self.target_position}')
        if abs((self.target_position.x - self.position.x)/0.5) >= 0.5:
            if self.target_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((self.target_position.x - self.position.x) /
                     ((self.target_position.x - self.position.x)/60)) * dt
            else:
                self.position.x = self.position.x - \
                    ((self.target_position.x - self.position.x) /
                     ((self.target_position.x - self.position.x)/60)) * dt
        if abs((self.target_position.y - self.position.y)/0.5) >= 0.5:
            if self.target_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((self.target_position.y - self.position.y) /
                     ((self.target_position.y - self.position.y)/60)) * dt
            else:
                self.position.y = self.position.y - \
                    ((self.target_position.y - self.position.y) /
                     ((self.target_position.y - self.position.y)/60)) * dt

                     


class FollowProjectile(ProjectileClass):
    def __init__(self, input):
        super().__init__(input)
        self.target_position = input["mouse_position"]

    def tracking(self, dt):
        dynamic_mouse_position = pygame.Vector2(
            pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        # print(f'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&: {dynamic_mouse_position}')
        if abs((dynamic_mouse_position.x - self.position.x)/0.5) >= 0.5:
            if dynamic_mouse_position.x > self.position.x:
                self.position.x = self.position.x + \
                    ((dynamic_mouse_position.x - self.position.x) /
                     ((dynamic_mouse_position.x - self.position.x)/60)) * dt
            else:
                self.position.x = self.position.x - \
                    ((dynamic_mouse_position.x - self.position.x) /
                     ((dynamic_mouse_position.x - self.position.x)/60)) * dt
        if abs((dynamic_mouse_position.y - self.position.y)/0.5) >= 0.5:
            if dynamic_mouse_position.y > self.position.y:
                self.position.y = self.position.y + \
                    ((dynamic_mouse_position.y - self.position.y) /
                     ((dynamic_mouse_position.y - self.position.y)/60)) * dt
            else:
                self.position.y = self.position.y - \
                    ((dynamic_mouse_position.y - self.position.y) /
                     ((dynamic_mouse_position.y - self.position.y)/60)) * dt