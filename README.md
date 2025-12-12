Maze Pathfinding using Iterative Deepening Depth-First Search (IDDFS)

📌 Project Overview

This project implements a maze pathfinding algorithm using Iterative Deepening Depth-First Search (IDDFS).
Given a 2D grid maze containing empty cells (0) and walls (1), the program determines whether a valid path exists between a start and target cell.

Movement is allowed in four directions:

Up

Down

Left

Right

The search avoids revisiting any cell within a single path exploration and increases the depth limit iteratively until a solution is found or all depths are exhausted.

🎯 Features

Fully working IDDFS algorithm

Prevents revisiting cells using a visited matrix

Works for any grid size

Accepts user input in structured format

Returns traversal path if found

Reports failure when no path exists

📥 Input Format

The program expects input in the following structure:

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

📤 Output Format

If a path is found:

Path found at depth <D> using IDDFS
Traversal Order: [(x1,y1), (x2,y2), ..., (xn,yn)]


If no path exists:

Path not found at max depth <D> using IDDFS

🧠 Algorithm Logic (IDDFS)

IDDFS works by repeatedly applying Depth-Limited DFS with increasing depth limits:

Start with depth = 0

Perform DFS but stop when depth reaches limit

If target not found, increase depth and repeat

Stop when solution is found or maximum possible depth reached

This combines the memory efficiency of DFS with the completeness of BFS.

🧩 Code Description

is_valid()
Checks if the next move is inside the grid, not a wall, and not visited.

dfs_limited()
Performs DFS up to a given depth limit. Uses backtracking to explore alternate paths.

iddfs()
Runs DFS repeatedly with increasing depth limits until the target is found.

Input reading section
Handles structured user input for grid, start, and target.

▶️ How to Run

Save the Python file (e.g., iddfs_maze.py)

Run using:

python iddfs_maze.py


Provide input when prompted (copy and paste the input format).

🧪 Sample Test Case
Input:
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3

Output:
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3)]

📚 Learning Outcomes

Understanding and implementing IDDFS

Working with recursive DFS and backtracking

Handling grid-based pathfinding

Managing visited states correctly

Building user-interactive Python scripts

📄 License

This project is open-source and free to use under the MIT License.

🤝 Contributions

Feel free to submit issues or pull requests to improve the project, optimize searching, or add visualizations.
