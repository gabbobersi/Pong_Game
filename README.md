# Pong game with Turtle module
This project represents an attempt to make the classic "Pong" game, but with the standard **Turtle** module, instead of well-known Pygame library.

Every game is "infinite" (no points limit) and simply starts with the execution of the script.

There are 2 active players at the same time.

## Controls
**PLAYER A**: w (up), s (down).

**PLAYER B**: Arrow Up, Arrow Down.

![image](https://user-images.githubusercontent.com/65022671/185482732-010ed113-d4f3-4782-99fe-f8eb0bc0ca78.png)
## Known problems
- FPS: Turtle module has no built-in to calculates and eventually limits FPS. 
  - TODO: Manual FPS calculation/limitation.
- Multiple inputs at the same time: Turtle module doesn't consider multiple keys pressed at the same time. This result in "Player A plays, Player B waits".
  - TODO: Implements a player inputs queue.
