import pygame


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    def add_points(self, points):
        self.score += points

    def draw(self, screen):
        text_image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_image, (10, 10))
