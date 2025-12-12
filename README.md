Maze Pathfinding Algorithms: IDDFS & A*

This repository contains two popular maze-solving algorithms implemented in Python:

Iterative Deepening Depth-First Search (IDDFS)

A* Search Algorithm

Both programs work on grid-based mazes, support four-directional movement, and demonstrate different approaches to solving pathfinding problems.

📌 1. Maze Pathfinding using Iterative Deepening Depth-First Search (IDDFS)
Project Overview

This implementation uses the IDDFS algorithm to determine whether a valid path exists between a start and a target cell in a 2D maze.
The maze contains empty cells (0) and walls (1), and movement is allowed in:

Up

Down

Left

Right

IDDFS increases the depth limit gradually, combining the completeness of BFS with the memory efficiency of DFS.

Features

Fully working IDDFS algorithm

Prevents revisiting cells using a visited matrix

Works with any grid size

Accepts user input

Returns traversal path if found

Reports failure if no path exists

Input Format
rows cols
<row1 values>
<row2 values>
...
<rowN values>
Start: x y
Target: x y

Example:
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3

Output Format
If a path is found:
Path found at depth <D> using IDDFS
Traversal Order: [(x1,y1), (x2,y2), ...]

If no path exists:
Path not found at max depth <D> using IDDFS

Algorithm Logic (IDDFS)

Start with depth = 0

Run DFS with a depth limit

If not found → increase depth

Repeat until solution is found or max depth reached

This approach prevents unnecessary memory usage while ensuring complete search coverage.

How to Run

Save the script as:

iddfs_maze.py


Run the program:

python iddfs_maze.py


Input the maze when prompted.

Sample Output
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3)]

📌 2. Maze Pathfinding using A* Search Algorithm
Project Overview

This implementation uses the A* algorithm to compute the shortest path in a maze using the Manhattan distance heuristic.
The maze is loaded from an input.txt file.

Features

Reads maze grid from input.txt

Supports Up, Down, Left, Right movement

Optimal pathfinding using A* algorithm

Uses Manhattan distance heuristic

Reconstructs and prints the shortest path

Clean, modular Python code

Input Format (input.txt)
R C
<row1 values>
<row2 values>
...
<row R values>
sr sc
tr tc

Example:
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
1 1 0 0 0
0 0 0 1 0
0 0
4 4

How to Run

Keep these two files in the same folder:

astar_maze.py
input.txt


Run the program:

python3 astar_maze.py

Algorithm Logic (A*)

A* uses the priority function:

f(n) = g(n) + h(n)


Where:

g(n) = cost from start to current node

h(n) = Manhattan distance to target

f(n) = total score used to select the next best node

Sample Output
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

📁 Project Structure
/
├── iddfs_maze.py
├── astar_maze.py
├── input.txt
└── README.md

📚 Learning Outcomes

Understanding IDDFS and DFS backtracking

Implementing A* with heuristics

Working with grid-based pathfinding

Creating modular search algorithms

Reading structured input files

📄 License

This project is open-source under the MIT License.

👤 Author

Developed by Rayhan.
