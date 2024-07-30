# basic-chess-clock
A simple chess clock.

**Features**

When you run the Python script, it will first ask you if you want to flip Black's clock, press <ENTER> to say 'no'.
Typing anything before pressing <ENTER> will flip Black's clock vertically and horizontally.

Then, type in the amount of milliseconds (ms) that each player, Black and White, starts with.
Press <ENTER> without typing anything for the default, 180K milliseconds, or 3 minutes.

Then, type in how much Bronstein delay (ms) you want and how much Fischer increment (ms) you want. Both units are in milliseconds!
Bronstein delay describes how long it takes after your turn starts before your clock starts ticking down.
Fischer increment describes how much more time you earn AFTER finishing your turn and starting your opponent's clock.

You may set both at once! Although, it is recommended to only do one. Fischer increment tends to be more useful and intuitive.
After typing in all of this information, exit the Terminal window, and look into the new window that is using Pygame.

Notice both clocks are currently not ticking! To start White's clock, press <SPACE>.
Now White's clock is ticking, and it is time to start playing Chess over-the-board.

This clock can also be used in *any* strategy game with two players, to prevent stalling and overly long thinking by either side.

Slightly lighter colors are used, and the White clock is on the bottom, Black clock on the top.

There is an arrow pointing to whose clock is currently active. Press <SPACE> whenever your turn is finished. Play proceeds to Black, and the cycle repeats.

Once a player is under 10 seconds, a decimal digit after the seconds place will pop up.
Once a player is under 1 second, a second decimal digit after the seconds place will pop up.
Once a player is out of time, it will say *00:00.00* in RED. This means that player has lost on time.

*In chess, sometimes running out of time results in a draw instead of a loss, if the other player has insufficient material to checkmate.*

The arrow also flips after each clock switch or <SPACE> press.

Have fun!
