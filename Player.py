import pygame
class PlayerClass:
    def __init__(self, input):
        self.player_color = input['player_color']
    #     self.player_position = pygame.Vector2(
    # input['display_surface'].get_width() / 2, input['display_surface'].get_height() / 2)
        self.player_surface = input['player_surface']
        self.player_rect = self.player_surface.get_rect(topleft=input['player_position'])

    def render(self, display_surface, player_position):
        self.player_rect = self.player_surface.get_rect(topleft=player_position)
        display_surface.blit(self.player_surface, self.player_rect)
        self.player_surface.fill(self.player_color)
        pygame.draw.rect(display_surface, 'Green', self.player_rect, 1)
 