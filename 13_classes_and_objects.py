"""
CARD 13: Classes & Objects
------------------------------
Teaches: writing your own class — the pattern behind almost every "real"
game (a Player class, an Enemy class, a Bullet class, etc). If your game
has more than one KIND of thing (player + enemies + coins), you want
this.

Why bother? Without a class, tracking 5 coins means 5 sets of x/y/value
variables, or a messy list of tuples where you forget which number means
what. A class bundles "everything a coin is + everything a coin can do"
into one object.

API/pattern you'll use:
    class Coin:
        def __init__(self, x, y):      # runs once, when you MAKE a coin
            self.x = x                  # self.___ = stored data on THIS coin
            self.y = y

        def draw(self, screen):         # a method — something a coin can DO
            pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), 10)

    my_coin = Coin(100, 200)   # this calls __init__ and makes an object
    my_coin.draw(screen)       # this calls the draw method on that object

Run this file. One coin is defined below but nothing happens with it yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 13: Classes & Objects")
clock = pygame.time.Clock()


class Coin:
    def __init__(self, x, y):
        # TODO 1: store x and y on self, and add self.collected = False
        pass

    def draw(self, screen):
        # TODO 2: if not self.collected, draw a small yellow circle at
        # (self.x, self.y). If it IS collected, draw nothing (just return).
        pass

    def is_collected_by(self, player_rect):
        # TODO 3: return True if player_rect.collidepoint(self.x, self.y)
        # is True. This reuses card 05's collision idea, just point-based.
        pass


player = pygame.Rect(300, 400, 40, 40)

# TODO 4: Make a LIST of several Coin objects at different positions
# (this reuses card 09's list pattern — Coin(...) calls __init__ each time)
coins = []

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

    # TODO 5: Loop over coins. For each one, if it's_collected_by(player),
    # set its .collected = True. This is exactly the pattern the Space
    # Invaders tutorial uses for "is the badguy hit by the missile".

    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), player)
    for coin in coins:
        coin.draw(screen)
    pygame.display.update()
    clock.tick(60)
