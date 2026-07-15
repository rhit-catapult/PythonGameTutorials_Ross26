"""
CARD 08: Images Instead of Drawn Shapes
------------------------------------------
Teaches: loading a .png as an image, and using .get_rect() to know its
size/position for movement and collision.

API you'll use:
    player_img = pygame.image.load("assets/player.png").convert_alpha()
    player_rect = player_img.get_rect(center=(320, 240))
    screen.blit(player_img, player_rect)

This card has NO image file yet, so it draws a placeholder square that
you should replace with pygame.image.load once you have art (find free
game art at kenney.nl or opengameart.org, save it in an "assets" folder
next to your game file).

Run this file first — you'll see a placeholder square move with the
mouse. Then follow the TODOs to swap in a real image.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 08: Images & Sprites")
clock = pygame.time.Clock()

# Placeholder "image" — a surface we drew ourselves, standing in for a
# loaded PNG so this file runs with zero assets.
placeholder = pygame.Surface((60, 60))
placeholder.fill((100, 180, 255))
player_img = placeholder
player_rect = player_img.get_rect(center=(320, 240))

# TODO 1: Once you have a .png saved in an "assets" folder, uncomment and
# edit this line to load it instead of using the placeholder:
# player_img = pygame.image.load("assets/player.png").convert_alpha()
# player_rect = player_img.get_rect(center=(320, 240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # TODO 2: Make player_rect.center follow the mouse position (this
    # reuses card 04_mouse_input.py — get_pos(), then set .center = pos)

    # TODO 3 (bonus): Resize the image with pygame.transform.scale(img,
    # (new_width, new_height)) and see how that changes get_rect(). Try
    # pygame.transform.rotate(img, angle) too.

    screen.fill((20, 20, 20))
    screen.blit(player_img, player_rect)
    pygame.display.update()
    clock.tick(60)
