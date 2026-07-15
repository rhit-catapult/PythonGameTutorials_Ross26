# Card 16: Multiple Files & Imports

Right now your game is one file. That's fine at 80 lines. It stops being
fine around 300-400 lines, when scrolling to find your `Enemy` class
takes longer than writing it did. This card is about splitting one file
into several, without changing what the game does.

## Why bother

- Easier to find things — `player.py` only has player stuff in it.
- Easier to work with a partner — you edit `enemy.py`, they edit
  `player.py`, you're not fighting over the same file.
- It's just how real projects are organized — worth knowing before day 9.

## The core idea: import

Any `.py` file can grab code from another `.py` file **in the same
folder** using `import`.

```python
# player.py
import pygame

class Player:
    def __init__(self, x, y):
        ...
```

```python
# main.py
import pygame
from player import Player       # grabs the Player class from player.py

player = Player(300, 400)
```

`from player import Player` means: "look in a file called `player.py`
in this same folder, and pull out the thing called `Player`." The file
name and the thing you're importing are usually different words — don't
mix up `import player` (grabs the whole file as a toolbox you'd then
call `player.Player`) with `from player import Player` (grabs just that
one class directly).

## Your task: split `space_game.py`

Starting point: `before/space_game.py` — run it first, see that it
works. Then create these files IN THE SAME FOLDER as `space_game.py`:

**Step 1 — `player.py`**
1. Create a new file called `player.py`.
2. At the top, add `import pygame` (the Player class uses `pygame.Rect`
   and `pygame.draw`, so this file needs its own import — imports don't
   carry over between files).
3. Cut the entire `Player` class out of `space_game.py` and paste it
   into `player.py`.

**Step 2 — `coin.py`**
1. Same idea: new file, `import pygame` at the top, cut-and-paste the
   `Coin` class in.

**Step 3 — `scoreboard.py`**
1. Same idea again for the `Scoreboard` class. Note it also uses
   `pygame.font`, so it needs `import pygame` too.

**Step 4 — fix up the main file**
Rename `space_game.py` to `main.py` (or keep the name, doesn't matter —
just be consistent about which file you actually run). At the top, add:

```python
from player import Player
from coin import Coin
from scoreboard import Scoreboard
```

Everything else in the file — the game loop, creating `player`, the list
of `coins`, the `while True:` loop — stays exactly where it is. You're
only moving the class definitions out, not the code that USES them.

**Step 5 — run it**
Run `main.py`. If you did it right, the game behaves EXACTLY like it did
before — that's the whole point. You haven't added a feature, you've
just reorganized where the code lives.

Check your work against `solutions/after/` if you get stuck.

## Common errors and what they mean

**`ModuleNotFoundError: No module named 'player'`**
Almost always means one of two things: (1) `player.py` isn't in the same
folder as the file you're running, or (2) you typo'd the filename —
`from player import Player` needs a file literally named `player.py`.

**`ImportError: cannot import name 'Player' from 'player'`**
The file `player.py` exists and was found, but nothing called `Player`
is defined inside it. Check spelling/capitalization — `Player` and
`player` are different names in Python.

**Nothing happens / old behavior when you know you changed the code**
Make sure you're running `main.py`, not still running the old
`space_game.py` copy sitting in the same folder from before you renamed
it. Delete or rename the old one to avoid confusing yourself.

**Circular imports** (rare at this scale, but good to know): if
`player.py` tries to `from main import something` WHILE `main.py` is
also importing from `player.py`, Python gets stuck in a loop. The fix is
almost always: things classes need (like `pygame`) should be imported
directly in that class's own file, not borrowed from `main.py`.

**Don't name a file the same as a library you're using** — a file
called `random.py` in your project folder will shadow Python's real
`random` module and cause very confusing errors. Same goes for
`pygame.py`.

## Optional stretch: an `assets` folder

If you're loading images or sounds (cards 08/10), it's common to also
make an `assets/` folder next to your `.py` files and load from it:

```python
pygame.image.load("assets/player.png")
```

This isn't an import, just a normal folder for non-code files — but it's
part of the same "keep things organized" idea.
