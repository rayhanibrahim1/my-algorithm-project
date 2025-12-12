A* Search Algorithm for Maze Pathfinding

This project implements the A* search algorithm to find the shortest path in a 2D grid-based maze.
The maze is loaded from an input.txt file, and the algorithm computes the optimal path from the start cell to the target cell using the Manhattan distance heuristic.

FEATURES

Reads maze dimensions and grid from input.txt

Supports four-directional movement (Up, Down, Left, Right)

Avoids walls and invalid cells

Uses the A* algorithm for optimal pathfinding

Uses Manhattan distance as the heuristic

Reconstructs and prints the shortest path

Simple, modular Python implementation

INPUT FORMAT (input.txt)

R C
<row 1 values>
<row 2 values>
...
<row R values>
sr sc
tr tc

Example input:
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
1 1 0 0 0
0 0 0 1 0
0 0
4 4

HOW TO RUN

Install Python 3.

Place astar_maze.py and input.txt in the same directory.

Run the program using:

python3 astar_maze.py

ALGORITHM USED: A*

A* calculates:

f(n) = g(n) + h(n)

where:
g(n) = actual cost from start to current node
h(n) = Manhattan distance to target
f(n) = priority value used to expand nodes

SAMPLE OUTPUT

Shortest path found:
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(3, 2)
(4, 2)
(4, 3)
(4, 4)

PROJECT STRUCTURE

astar_maze.py
input.txt
README.md

LICENSE

Open-source and free to use.

AUTHOR

Developed by Rayhan.
