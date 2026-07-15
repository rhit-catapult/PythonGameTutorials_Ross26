"""
CARD 03: Keyboard Movement
---------------------------
Teaches: the difference between a KEY EVENT (fires once, the instant a key
is pressed) and a HELD KEY CHECK (true every single frame the key is
down). Games almost always want the second one for movement.

API you'll use:
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:      # also: K_DOWN, K_LEFT, K_RIGHT,
        ...                            # K_w, K_a, K_s, K_d, K_SPACE

Run this file. A white square sits in the middle and does nothing yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 03: Keyboard Movement")
clock = pygame.time.Clock()

x, y = 320, 240
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # TODO 1: Get the pressed keys and move x/y when arrow keys (or WASD,
    # your choice) are held. Four if-statements, one per direction.
    pressed_keys = pygame.key.get_pressed()

    # TODO 2: The square can currently walk off the edge of the screen.
    # Add checks that clamp x and y so it can't go past 0 or past
    # (screen_width - square_size).

    # TODO 3 (bonus): Add a "sprint" key — hold SPACE to double speed for
    # one frame. Hint: this needs an if/else that changes a local speed
    # variable before you apply movement, not a permanent change to speed.

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 40, 40))
    pygame.display.update()
    clock.tick(60)
