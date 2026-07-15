import sys
import pygame

from player import Player
from coin import Coin
from scoreboard import Scoreboard

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Coin Collector (multi-file)")
clock = pygame.time.Clock()

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
