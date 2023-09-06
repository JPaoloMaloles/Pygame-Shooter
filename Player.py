import pygame
class PlayerClass:
    def __init__(self, input):
        self.player_color = input['player_color']
    #     self.player_position = pygame.Vector2(
    # input['display_surface'].get_width() / 2, input['display_surface'].get_height() / 2)
        self.player_surface = input['player_surface']

    def render(self, display_surface, player_position):
        player_rect = display_surface.get_rect(topleft=player_position)
        display_surface.blit(self.player_surface, player_rect)
        self.player_surface.fill(self.player_color)
