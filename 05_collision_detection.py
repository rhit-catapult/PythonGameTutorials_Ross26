"""
CARD 05: Collision Detection
------------------------------
Teaches: pygame.Rect objects and .colliderect() — the standard way to ask
"are these two rectangular things touching?"

API you'll use:
    player_rect = pygame.Rect(x, y, width, height)
    if player_rect.colliderect(other_rect):
        ...  # they're overlapping

    Rect objects also auto-update if you do player_rect.x = new_x, and
    they can just be passed straight into pygame.draw.rect(screen, color,
    player_rect) instead of a tuple.

Run this file. Move the player square with arrow keys. Right now it
passes straight through the red square — fix that.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 05: Collision")
clock = pygame.time.Clock()

player = pygame.Rect(50, 220, 40, 40)
target = pygame.Rect(500, 220, 40, 40)
caught = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.x -= 5
    if pressed_keys[pygame.K_RIGHT]:
        player.x += 5
    if pressed_keys[pygame.K_UP]:
        player.y -= 5
    if pressed_keys[pygame.K_DOWN]:
        player.y += 5

    # TODO 1: If player.colliderect(target), set caught = True

    # TODO 2: When caught, move target to a new random-ish position instead
    # of leaving it there (pairs well with card 12_randomness.py). This
    # turns "collision" into a real catch-the-target mini-game.

    # TODO 3 (bonus): Instead of a hard yes/no collision, try distance-based
    # collision for circles: distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5,
    # then check if distance < radius1 + radius2. Rects vs. circles behave
    # differently — which fits your game shape better?

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (0, 255, 0) if caught else (200, 40, 40), target)
    pygame.display.update()
    clock.tick(60)
