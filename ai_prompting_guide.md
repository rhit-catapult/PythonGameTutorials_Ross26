# How to Prompt AI for Game Code

Using AI to help write your game is fine — it's a real skill, and this
guide is here to make sure it's actually building understanding instead
of replacing it. Don't forget: the **explain-back rule** in the AI track
addendum still applies to everything below.

## The core problem with bad AI prompts

"Make me a space shooter game" produces 200 lines you don't understand,
that may not even match how YOUR game already works. Good prompting for
this camp looks less like ordering a finished product and more like
asking a very literal, very fast pair-programmer to help you with ONE
piece at a time.

## Five habits that make a huge difference

**1. One concept at a time.**
Ask for movement. Get it working. Ask for collision. Get it working.
Don't ask for "movement, collision, scoring, and sound" in one prompt —
you'll get code you can't trace back to understand, and when it breaks
you won't know where.

**2. Paste your actual code, not a description of it.**
"I have a player Rect called `player` and a list called `enemies`, here's
my current file: [paste it]. Add code so pressing SPACE fires a bullet
that moves up the screen." The AI will match your variable names and
style instead of inventing its own structure that you now have to
reconcile with yours.

**3. Ask for the smallest version first.**
"Just get one bullet firing and moving, don't worry about removing it
off-screen yet" — get that working, see it, THEN ask for the cleanup
step. Small verified steps beat one big untested block.

**4. When it breaks, paste the real error.**
"It doesn't work" gets you nowhere. Paste the actual error message and
the line number. AI is very good at reading tracebacks — use that.

**5. Ask it to explain, not just generate.**
Add "explain what this code does, line by line" to your prompt, or ask
afterward: "explain this back to me like I'm new to Python." If you
can't repeat the explanation in your own words to a TA, you're not done
with that piece yet — go back and ask follow-up questions until you can.

## Example prompts, by concept card

Use these as a starting point — copy your own code in before running
them for real.

**Movement (card 03)**
> "Here's my pygame file [paste]. I have a Rect called `player`. Add
> code so LEFT/RIGHT arrow keys move it, and it can't go past the edges
> of a 640x480 screen. Explain the boundary-checking part."

**Mouse input (card 04)**
> "Here's my file [paste]. Make `player` follow the mouse position
> instead of using arrow keys."

**Collision (card 05)**
> "I have `player` and `enemy`, both pygame.Rect. Add a check so
> something happens (print 'hit') when they overlap. What method are you
> using and why does it work on Rects specifically?"

**Timing / spawning over time (card 06)**
> "I want a new enemy to appear roughly once per second, not every
> frame. Here's my current loop [paste]. Use pygame.time.get_ticks(), not
> a frame counter, and explain why get_ticks() is more reliable."

**Score/text (card 07)**
> "Add a score counter to my game that goes up by 10 every time
> [describe your hit/collect event] happens, and displays in the top
> left. Here's my current file [paste]."

**Images (card 08)**
> "I have an image at assets/player.png. Show me how to load it, and
> replace my drawn rectangle with it, keeping the same collision Rect."

**Lists of objects (card 09)**
> "I want multiple enemies instead of one. Here's my single-enemy code
> [paste]. Turn it into a list, and explain the difference between
> looping to move them vs. looping to remove them."

**Sound (card 10)**
> "Add a sound effect from assets/hit.wav that plays when [event]
> happens. Also show me how to handle it gracefully if the file is
> missing, so my game doesn't crash for someone testing it without the
> assets folder."

**Game states (card 11)**
> "My game currently just loops forever. Add a start screen (press SPACE
> to begin) and a game-over screen, using a state variable, not separate
> files. Here's my current loop [paste]. Explain how the state variable
> controls what gets drawn each frame."

**Randomness (card 12)**
> "Make enemies spawn at a random x position each time, using the random
> module. Here's my spawn code [paste]."

**Classes (card 13)**
> "I have repeated code for multiple coins (x, y, drawing, collision) —
> here it is [paste]. Turn this into a Coin class with __init__ and draw
> methods, and explain what `self` is doing in each method."

**Projectiles (card 14)**
> "Add a fire-on-spacebar bullet system to my game. Bullets should move
> up and delete themselves once off-screen. Here's my player code
> [paste]. Explain the removal step specifically — I want to understand
> why you can't just .remove() while looping."

**Formation movement (card 15)**
> "I want a row of enemies that all move right, bounce off the edge,
> step down, then move left, bounce again, etc — like classic Space
> Invaders. Here's my Enemy class [paste]. Show me the movement logic and
> explain how one rule makes them look coordinated."

## The debugging checkpoint still applies

Remember: at least once during the camp, you'll get a small broken file
and 15 minutes to fix it WITHOUT AI. That's not about slowing you down —
it's the only way to know the speed you're getting from AI is standing
on top of real understanding, not instead of it.
