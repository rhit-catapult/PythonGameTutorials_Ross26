"""
CARD 10: Sound Effects & Music
-----------------------------------
Teaches: playing a sound effect on an event, and background music. Also:
handling a MISSING sound file gracefully instead of crashing, since
you'll definitely try this before you have real sound files.

API you'll use:
    pygame.mixer.init()   # do this once, near pygame.init()
    jump_sound = pygame.mixer.Sound("assets/jump.wav")
    jump_sound.play()

    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.play(-1)   # -1 = loop forever

Free sound effects: freesound.org or opengameart.org. Save as .wav or
.ogg in an "assets" folder.

Run this file. Press SPACE — it should print instead of crash, since
there's no sound file yet.
"""
import sys
import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Card 10: Sound")
clock = pygame.time.Clock()

jump_sound = None
try:
    jump_sound = pygame.mixer.Sound("assets/jump.wav")
except (pygame.error, FileNotFoundError):
    print("No assets/jump.wav found yet — that's fine for now.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # TODO 1: if jump_sound exists, play it. Otherwise print
            # something so you know the key press registered.
            pass

    # TODO 2: Once you have a music file, load it near the top of the file
    # (outside the loop!) and call pygame.mixer.music.play(-1) once, also
    # outside the loop. Music should NOT be started every frame.

    # TODO 3 (bonus): Add a mute toggle — press M to call
    # pygame.mixer.music.set_volume(0) or set_volume(0.5) to bring it back.

    screen.fill((20, 20, 20))
    pygame.display.update()
    clock.tick(60)
