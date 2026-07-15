"""
CARD 04: Mouse Input
----------------------
Teaches: reading mouse position every frame, and reacting to click EVENTS
(clicks are events, like key presses — they fire once, not every frame).

API you'll use:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # inside the event loop:
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos, event.button)   # button: 1=left, 2=middle, 3=right

Run this file. A circle follows nothing yet — make it follow your mouse.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 04: Mouse Input")
clock = pygame.time.Clock()

circle_color = (100, 200, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # TODO 2: When the mouse is clicked (MOUSEBUTTONDOWN), change
        # circle_color to a random or different color. (Pairs well with
        # card 12_randomness.py.)

    # TODO 1: Get the current mouse position and store it in mouse_x, mouse_y
    mouse_x, mouse_y = 320, 240  # placeholder — replace with real mouse pos

    screen.fill((15, 15, 25))
    pygame.draw.circle(screen, circle_color, (mouse_x, mouse_y), 20)

    # TODO 3 (bonus): Make the circle only appear (get drawn) if the mouse
    # is within a certain region of the screen — e.g. only the right half.
    # This is the first step toward clickable buttons.

    pygame.display.update()
    clock.tick(60)
