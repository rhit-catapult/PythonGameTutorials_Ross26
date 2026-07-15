"""
CARD 07: Score & Text on Screen
----------------------------------
Teaches: pygame.font — rendering ANY text (score, lives, timer, messages)
as an image and drawing it to the screen.

API you'll use:
    font = pygame.font.SysFont(None, 48)          # do this ONCE, outside the loop
    text_surface = font.render("Score: 0", True, (255, 255, 255))
    screen.blit(text_surface, (x, y))

Important gotcha: font.render() makes a NEW image every time you call it.
You must call it fresh every frame if the text (like a score) changes.

Run this file. Press SPACE to add points — the score doesn't update yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 07: Score & Text")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass  # TODO 1: increase score by 1 (or 10, your call) here

    screen.fill((20, 20, 20))

    # TODO 2: Render the current score as text and blit it to the screen.
    # Remember: render() has to happen every frame if score can change.

    # TODO 3 (bonus): Add a second line of text below the score showing
    # something else — lives, a timer using card 06's ticks, or a message
    # that only appears when score > 5.

    pygame.display.update()
    clock.tick(60)
