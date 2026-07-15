"""
CARD 16 STARTING POINT: one file, three classes, getting long.

Run this first. It's a complete, working little game: move the player
with arrow keys, collect coins, watch your score go up. Nothing to fix —
it works. The problem isn't that it's broken, it's that it's about to
get a lot longer as you add more to it, and everything is jammed into
one file.

Your task (see 16_multiple_files_and_imports.md) is to split this into
separate files WITHOUT changing what the game does.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Coin Collector (single file)")
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = 5

    def handle_input(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if pressed_keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


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


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

    def add_points(self, points):
        self.score += points

    def draw(self, screen):
        text_image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_image, (10, 10))


player = Player(300, 400)
coins = [Coin(80, 100), Coin(200, 300), Coin(400, 150), Coin(560, 350)]
scoreboard = Scoreboard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    player.handle_input(pressed_keys)

    for coin in coins:
        if not coin.collected and coin.is_collected_by(player.rect):
            coin.collected = True
            scoreboard.add_points(10)

    screen.fill((20, 20, 20))
    player.draw(screen)
    for coin in coins:
        coin.draw(screen)
    scoreboard.draw(screen)
    pygame.display.update()
    clock.tick(60)
