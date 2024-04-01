# IART - AMADO

## How to run and use the program

Having installed `python` and `pygame` (through `pip`) on your machine, just run the command below inside the directory.

```bash
$ pip install pygame
$ python3 main.py
```

This will open the game's main menu. You can navigate through it using the `up` and `down` arrow keys and `ENTER` to select.

Head to the `Tutorial` menu, where we show how the in-game menu works.

The game has three different levels. The main distinction between these levels is the generation of the starting board, for example, the level 3 board will be way different from the solution than the 1st level board. You have 70 seconds to solve the 1st board. After solving, 70 seconds will be added to the remaining time to do the 2nd board and so on. There are 5 boards in total for each level. The timer only starts counting after you do a move. You can exit the game by pressing the `ESCAPE` button at any time (except when the AI is thinking of a path to follow).

You can play the game by yourself if you wish to, or enable the AI with different algorithms (some may take way longer than others, also dependant on level) after pressing these numbers:

0. Breadth-first Search
1. Depth-first Search
2. Simple Greedy Search
3. Color Cluster Greedy Search
4. A* Simple    
5. A* Color Cluster
6. Depth Limited Search
7. Iterative Deepening

The algorithms will think about the best solution to run, without pressing any keys (which means the timer will not start), and when a solution is found it will run that sequence to complete the board.

There is also a `Settings` menu where you can change the game's resolution (by default `640x480` and always `4:3` ratio, to give that retro look) up to `1280x960`.

### HAVE FUN!