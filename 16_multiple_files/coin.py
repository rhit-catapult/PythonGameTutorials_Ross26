import pygame


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), 10)

    def is_collected_by(self, player_rect):
        return player_rect.collidepoint(self.x, self.y)
