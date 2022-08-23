# Pong game
This project represents an attempt to make the classic "Pong" game, but with **Turtle** standard module, instead of wellknown Pygame library.

Every match is "endless" (no points limit) and simply starts with the execution of the script.

There are 2 players active at the same time.

## Controls
**PLAYER A**: w (up), s (down).

**PLAYER B**: Arrow Up, Arrow Down.

![image](https://user-images.githubusercontent.com/65022671/185482732-010ed113-d4f3-4782-99fe-f8eb0bc0ca78.png)
## Know problems
- FPS: in Turtle, you can't limit or use the delta to fix FPS.
- Multiple inputs at the same time: in Turtle, you can't input multiple keys at the same time. This result in "Player A plays, Player B waits". This limitation could lead to some interesting game design choice.
