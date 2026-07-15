"""
CARD 12: Randomness
-----------------------
Teaches: the random module — spawning things in random places, picking a
random enemy type, random colors, random delays.

API you'll use:
    import random
    random.randint(0, 640)          # random whole number, both ends included
    random.choice(["a", "b", "c"])  # random item from a list
    random.random()                 # random float between 0 and 1

Run this file. Press SPACE — a circle should appear at a random position
and with a random color, but the TODOs aren't filled in yet.
"""
import sys
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 12: Randomness")
clock = pygame.time.Clock()

circle_x, circle_y = 320, 240
circle_color = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass  # TODO 1: set circle_x, circle_y to random positions
            # on screen (0-640, 0-480)
            # TODO 2: set circle_color to a random (r, g, b) tuple using
            # random.randint(0, 255) three times

    # TODO 3 (bonus): use random.choice() to pick between 3 different
    # circle sizes, or 3 preset "enemy type" colors, each time SPACE is
    # pressed — this is the pattern for randomized enemy variety.

    screen.fill((20, 20, 20))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), 25)
    pygame.display.update()
    clock.tick(60)
