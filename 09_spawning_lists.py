"""
CARD 09: Lists of Game Objects
----------------------------------
Teaches: managing MANY of something (enemies, bullets, coins) with a
Python list, and the safe way to remove items from a list while looping
over it.

API/pattern you'll use:
    enemies = []                          # empty list to start
    enemies.append({"x": 100, "y": 50})   # add a new one

    for enemy in enemies:
        enemy["y"] += 3                   # move each one

    # removing safely — DON'T remove items while a normal for-loop is
    # iterating over the same list, it skips items. Instead build a new
    # list of survivors:
    enemies = [e for e in enemies if e["y"] < 480]

Run this file. Press SPACE repeatedly — nothing spawns yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 09: Spawning Lists")
clock = pygame.time.Clock()

dots = []  # each dot will be a dict like {"x": .., "y": ..}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass  # TODO 1: append a new dot dict at, say, x=320, y=0

    # TODO 2: Loop over dots and move each one down (increase its "y")

    # TODO 3: Remove dots once they go past y=480, using the list-comp
    # pattern shown in the docstring above. Try it WITHOUT that pattern
    # first (a normal for loop with .remove() inside it) and see what
    # breaks — that's a real, common bug worth seeing once.

    screen.fill((20, 20, 20))
    for dot in dots:
        pygame.draw.circle(screen, (255, 100, 100), (dot["x"], dot["y"]), 8)
    pygame.display.update()
    clock.tick(60)
