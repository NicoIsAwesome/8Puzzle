# 8Puzzle

## Usage
work with python2

### [1] edit the numberList in the 8puzzle.py
```
numberList = [1, 7, 8, 2, 3, 4, 5, 6, 0]

Note:
0 = space
---------    ---------
| 1 7 8 |    |   1 2 |
| 2 3 4 | => | 3 4 5 |
| 5 6   |    | 6 7 8 |
---------    ---------
```

### [2] select a seacrh algorithm ('bfs', 'dfs', 'ucs', 'greedy', 'astar') in the 8puzzle.py
```
algo = 'astar'    # algo can be one of 'bfs', 'dfs', 'ucs', 'greedy', 'astar'
```

### [3] python 8puzzle.py
```
========================================
Need 24 moves to solve this puzzle by astar: ('left', 'up', 'up', 'right', 'down', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 'up', 'right', 'down', 'left', 'left', 'down', 'right', 'right', 'up', 'left', 'up', 'left')
========================================
---------
| 1 7 8 |
| 2 3 4 |
| 5 6   |
---------
move#1: left
---------
| 1 7 8 |
| 2 3 4 |
| 5   6 |
---------
move#2: up
---------
| 1 7 8 |
| 2   4 |
| 5 3 6 |
---------
move#3: up
---------
| 1   8 |
| 2 7 4 |
| 5 3 6 |
---------
move#4: right
---------
| 1 8   |
| 2 7 4 |
| 5 3 6 |
---------
move#5: down
---------
| 1 8 4 |
| 2 7   |
| 5 3 6 |
---------
move#6: left
---------
| 1 8 4 |
| 2   7 |
| 5 3 6 |
---------
move#7: left
---------
| 1 8 4 |
|   2 7 |
| 5 3 6 |
---------
move#8: down
---------
| 1 8 4 |
| 5 2 7 |
|   3 6 |
---------
move#9: right
---------
| 1 8 4 |
| 5 2 7 |
| 3   6 |
---------
move#10: right
---------
| 1 8 4 |
| 5 2 7 |
| 3 6   |
---------
move#11: up
---------
| 1 8 4 |
| 5 2   |
| 3 6 7 |
---------
move#12: left
---------
| 1 8 4 |
| 5   2 |
| 3 6 7 |
---------
move#13: up
---------
| 1   4 |
| 5 8 2 |
| 3 6 7 |
---------
move#14: right
---------
| 1 4   |
| 5 8 2 |
| 3 6 7 |
---------
move#15: down
---------
| 1 4 2 |
| 5 8   |
| 3 6 7 |
---------
move#16: left
---------
| 1 4 2 |
| 5   8 |
| 3 6 7 |
---------
move#17: left
---------
| 1 4 2 |
|   5 8 |
| 3 6 7 |
---------
move#18: down
---------
| 1 4 2 |
| 3 5 8 |
|   6 7 |
---------
move#19: right
---------
| 1 4 2 |
| 3 5 8 |
| 6   7 |
---------
move#20: right
---------
| 1 4 2 |
| 3 5 8 |
| 6 7   |
---------
move#21: up
---------
| 1 4 2 |
| 3 5   |
| 6 7 8 |
---------
move#22: left
---------
| 1 4 2 |
| 3   5 |
| 6 7 8 |
---------
move#23: up
---------
| 1   2 |
| 3 4 5 |
| 6 7 8 |
---------
move#24: left
---------
|   1 2 |
| 3 4 5 |
| 6 7 8 |
---------
Total number of nodes visited by astar: 18287 
```

## Reference
UC Berkeley CS188 Pacman AI projects

https://github.com/jinhoko/CS188
