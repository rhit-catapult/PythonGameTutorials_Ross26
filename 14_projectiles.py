"""
CARD 14: Shooting / Projectiles
------------------------------------
Teaches: the "fire a bullet" pattern — combining a KEYDOWN event, a list
(card 09), and per-frame movement + cleanup, into the single most common
request in any shooter-style game.

The pattern, in words:
  1. On a key press (not held — a single press should fire ONE bullet),
     add a new bullet to a list.
  2. Every frame, move every bullet in the list.
  3. Every frame, remove bullets that have left the screen.
  4. Every frame, draw every bullet still in the list.

Notice this is EXACTLY card 09 (lists) + a movement rule + a removal
rule. Nothing new syntax-wise — just three familiar patterns stacked.

Run this file. Move with LEFT/RIGHT, press SPACE — nothing fires yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 14: Projectiles")
clock = pygame.time.Clock()

player = pygame.Rect(300, 440, 40, 20)
bullets = []  # each bullet will be a pygame.Rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass
            # TODO 1: append a new bullet Rect, centered on the player's
            # x, starting near the player's y. Something like:
            # pygame.Rect(player.centerx - 2, player.y, 4, 10)

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.x -= 5
    if pressed_keys[pygame.K_RIGHT]:
        player.x += 5

    # TODO 2: Loop over bullets and move each one up (decrease its .y)

    # TODO 3: Remove bullets once bullet.y < 0, using the list-comprehension
    # pattern from card 09: bullets = [b for b in bullets if b.y > 0]

    # TODO 4 (bonus): Add a cooldown so holding SPACE doesn't fire every
    # single frame (60 bullets/sec!). Track a "last_fire_time" using
    # pygame.time.get_ticks() (card 06) and only allow firing again after
    # ~250ms have passed.

    # TODO 5 (bonus, pairs with card 05 + 13): if you also have a list of
    # enemies, loop over bullets AND enemies together and check
    # bullet.colliderect(enemy) — this is the exact "missile hits badguy"
    # double-loop from the Space Invaders tutorial.

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 255, 0), bullet)
    pygame.display.update()
    clock.tick(60)
