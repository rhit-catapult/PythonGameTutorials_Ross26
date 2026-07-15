"""
CARD 15: Formation Movement (bounce & descend)
----------------------------------------------------
Teaches: the classic Space-Invaders-style movement — a row of enemies
that all move the same direction, bounce off the screen edge, and step
down a little each time they bounce. Every enemy runs the SAME code
independently, but because they all follow the same rule, they LOOK like
they're moving as one unit.

Two ways to write the same idea — try the first one, get it working,
then look at the second and see why it's the same thing with less state.

VERSION A (explicit direction flag):
    if self.moving_right:
        self.x += self.speed
        if self.x > self.original_x + 100:
            self.moving_right = False
            self.y += 20
    else:
        self.x -= self.speed
        if self.x < self.original_x - 100:
            self.moving_right = True
            self.y += 20

VERSION B (flip the sign of speed instead of tracking a flag):
    self.x += self.speed
    if abs(self.x - self.original_x) > 100:
        self.speed = -self.speed
        self.y += 20

Run this file. One enemy is defined below — it currently doesn't move.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 15: Formation Movement")
clock = pygame.time.Clock()


class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.original_x = x

    def move(self):
        pass
        # TODO 1: implement Version A or Version B from the docstring above.
        # Either is fine — pick whichever makes more sense to you first.

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 60, 60), (self.x, self.y, 30, 20))


# TODO 2: Make a LIST of several Enemy objects in a row (reuses card 09 +
# 13) — e.g. Enemy(80 * i, 40, 2) for i in range(6)
enemies = [Enemy(80, 40, 2)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for enemy in enemies:
        enemy.move()

    # TODO 3 (bonus): once any enemy's .y passes some value (say 400),
    # that's a "the enemies reached you" lose condition — this is exactly
    # how the Space Invaders tutorial checks for player death. Try wiring
    # it up with card 11's game-state pattern.

    screen.fill((15, 15, 25))
    for enemy in enemies:
        enemy.draw(screen)
    pygame.display.update()
    clock.tick(60)
