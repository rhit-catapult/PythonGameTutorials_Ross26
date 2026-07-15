"""
CARD 06: Timing & Spawning on a Clock
----------------------------------------
Teaches: how to make something happen every N frames/seconds instead of
every single frame — the pattern behind enemy spawners, cooldowns, and
simple animation.

Two approaches shown:
  A) Frame counter: count frames, do the thing when count % N == 0
  B) Real time: use pygame.time.get_ticks() (milliseconds since start)

Run this file. Nothing spawns yet.
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 06: Timing")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

frame_count = 0
dot_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    frame_count += 1

    # TODO 1: Every 60 frames (i.e. roughly once per second at 60 fps),
    # print "tick" to the console. Hint: if frame_count % 60 == 0:

    # TODO 2: Make dot_x increase by 1 every frame, and reset to 0 once it
    # passes 640. This is the simplest possible animation — a moving dot.

    # TODO 3 (bonus): pygame.time.get_ticks() returns milliseconds since
    # the game started, and doesn't depend on frame rate the way counting
    # frames does. Try tracking "last_spawn_time = pygame.time.get_ticks()"
    # and spawning something new whenever
    # pygame.time.get_ticks() - last_spawn_time > 1000 (one second).
    # Why might this be more reliable than frame counting?

    screen.fill((20, 20, 20))
    pygame.draw.circle(screen, (255, 200, 0), (dot_x, 240), 10)
    counter_text = font.render(f"frames: {frame_count}", True, (255, 255, 255))
    screen.blit(counter_text, (10, 10))
    pygame.display.update()
    clock.tick(60)
