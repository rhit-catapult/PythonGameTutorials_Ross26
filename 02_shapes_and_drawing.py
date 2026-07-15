"""
CARD 02: Shapes & Drawing
--------------------------
Teaches: how to draw circles, rectangles, lines, and polygons, and how
LAYERING works (things drawn later appear on top of things drawn earlier).

Run this file first. You'll see a red circle. That's it. Your job is to
build a little scene using the TODOs below.

API you'll use:
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), thickness)
    pygame.draw.polygon(screen, color, [(x1,y1), (x2,y2), (x3,y3)])

    color = (r, g, b), each 0-255, e.g. (255, 0, 0) is red.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 02: Shapes")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((30, 30, 40))  # background — try changing this color

    pygame.draw.circle(screen, (200, 40, 40), (320, 240), 50)

    # TODO 1: Draw a second shape somewhere else on screen.
    # Pick rect, line, or polygon. Pick your own color and position.

    # TODO 2: Draw a THIRD shape that overlaps your first shape.
    # Notice: does it draw on top or underneath? Why? (Hint: order matters —
    # whatever you draw() last ends up on top.)

    # TODO 3: Try drawing the same shape twice, in the same spot, but with
    # the last argument (thickness) different — e.g. pygame.draw.circle(
    # screen, color, pos, radius, 3) draws an OUTLINE instead of a filled
    # shape. Use this to make a shape with a border.

    pygame.display.update()
    clock.tick(60)
