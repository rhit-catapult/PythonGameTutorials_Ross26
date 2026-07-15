"""
CARD 11: Game States (Start Screen / Playing / Game Over)
--------------------------------------------------------------
Teaches: the "state machine" pattern — using a single variable to track
which "mode" the game is in, and drawing/updating differently depending
on that mode. This is how almost every real game handles menus, pausing,
and win/lose screens.

Pattern:
    state = "start"    # or "playing", or "gameover"

    if state == "start":
        ...draw a title screen, wait for a key to start...
    elif state == "playing":
        ...run the actual game...
    elif state == "gameover":
        ...draw "you lose", wait for a key to restart...

Run this file. It's stuck on the start screen forever — make it
transition.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 11: Game States")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

state = "start"
player_y = 240

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if state == "start" and event.key == pygame.K_SPACE:
                pass  # TODO 1: switch state to "playing"
            elif state == "gameover" and event.key == pygame.K_SPACE:
                pass  # TODO 3: reset player_y and switch state back to "playing"

    screen.fill((20, 20, 20))

    if state == "start":
        msg = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(msg, (150, 220))
    elif state == "playing":
        # TODO 2: put real gameplay here. For now, just move player_y down
        # each frame, and switch state to "gameover" once it passes 480 —
        # that's enough to see the whole loop work end to end.
        pygame.draw.circle(screen, (100, 200, 255), (320, int(player_y)), 20)
    elif state == "gameover":
        msg = font.render("Game Over — SPACE to retry", True, (255, 80, 80))
        screen.blit(msg, (100, 220))

    pygame.display.update()
    clock.tick(60)
