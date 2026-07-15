# Concept Card Menu

This is not a tutorial you have to do in order. Files 02-16 below is a **standalone,
runnable** mini-game that teaches ONE thing. Run it, read it, mess with the
TODOs, then decide if your project needs that skill. If it does, build it
into your game. If it doesn't, skip it.

If you are new to programming, start with Python basics with files in 01-IntroToPython.
If you have prior experience, you can probably skip these.

How to use these:
1. `02_shapes_and_drawing.py` (or whichever file), run and see it work first.
2. Read the comments. Try to understand what the code is doing.
3. Do the TODOs 
4. Once it clicks, go copy the pattern into YOUR game file. Don't keep
   working in the card file. The card is scratch paper, your game is the
   real thing.

You do not need to finish every card. You do not need to do them in
order. Pick based on what your game needs.

| Card | Teaches | You probably need this if your game has... |
|---|---|---|
| 01_IntroToPython | Walks through the basics of programming with Python | every game |
| 02_shapes_and_drawing.py | pygame.draw shapes, colors, layering | any custom-drawn character/object |
| 03_keyboard_movement.py | held-key movement vs. single-press events | a player you move with keys |
| 04_mouse_input.py | mouse position, clicks, hover | a game you click/point at |
| 05_collision_detection.py | Rect.colliderect, distance checks | anything that can hit/catch/avoid anything |
| 06_timing_and_animation.py | clock.tick, delta time, spawning on a timer | enemies that spawn over time, cooldowns, animation |
| 07_score_and_text.py | pygame.font, rendering text/numbers on screen | a score, lives, timer, or any HUD text |
| 08_images_and_sprites.py | loading .png images instead of drawn shapes, Sprite class | art assets instead of circles/rects |
| 09_spawning_lists.py | lists of game objects, adding/removing while looping | multiple enemies/bullets/coins at once |
| 10_sound.py | playing sound effects and music, handling missing files | any sound at all |
| 11_game_states.py | start screen / playing / game over as a state machine | a title screen, pause, win/lose screen |
| 12_randomness.py | the random module for variety | randomized spawn points, enemy types, drops |
| 13_classes_and_objects.py | writing your own class, `self`, `__init__`, methods | more than one KIND of game object (player + enemies + coins...) |
| 14_projectiles.py | the fire-a-bullet pattern (event + list + movement + cleanup) | shooting, throwing, or launching anything |
| 15_enemy_formation_movement.py | bounce-and-descend movement for a whole row/group | a group of enemies that move together, Space-Invaders style |
| 16_multiple_files | Walks through how to split large game projects into multiple files | your big game |

Cards 13-15 build on the earlier ones — do 05 (collision) and 09 (lists)
before 13 or 14 if you haven't already, since they reuse those patterns.

Each file is self-contained — no shared imports beyond pygame, sys, and
occasionally random. Feel free to smash two cards together (e.g. spawn a
list of random enemies with a timer = cards 06 + 09 + 12).

## When you're stuck
1. Read the error message. What line? What's it telling you?
2. Check the API hint comment in the card. Is your syntax matching it?
3. Feel free to ask a friend
4. Ask me anything!

We are not going to lecture at the front of the room. If three+ people
have the same question, we'll pause and do a 2-minute mini-demo, but
otherwise this room runs on cards + asking.

## Using AI on any of these cards
If you're on the AI-assisted track, `ai_prompting_guide.md` has an
example prompt for every card above, plus habits that keep you actually
learning instead of just pasting. Read `ai_track_addendum.md` too — it
has the two extra rules for that track.
