# CLI-Snake
A turn based snake game that you can play in the command line.  

## Purpose
This is developed as an educational tool, to teach the basics of programming/game design.  It is turned based to help keep the design simple, but a real-time version is planned to build on this example. 

## Running program
You can start a game simply by running the script:
```bash
python3 snake.py
```
This will start a game and print out the board with a prompt for input.
```
Score: 0
 ==========
|          |
|   @oo    |
|          |
|          |
|     *    |
|          |
|          |
|          |
|          |
|          |
 ==========
> s
```
The user can enter "w","s","a", or "d" for movement, or "q" to quit the current game.  

## Customization 

If you import this code as a library, you can customize the board length, board height, and the starting length of the snake.  

```py
from snake import Game

G = Game(board_length=5, board_height=4, snake_length=4)
G.start()
```
