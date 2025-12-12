def is_valid(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and not visited[x][y]


def dfs_limited(x, y, target, grid, visited, depth_limit, path):
    # If we exceed depth limit, stop exploring
    if depth_limit < 0:
        return False

    visited[x][y] = True
    path.append((x, y))

    # If we found the target
    if (x, y) == target:
        return True

    # Explore neighbors: Down, Up, Right, Left
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, grid, visited):
            if dfs_limited(nx, ny, target, grid, visited, depth_limit - 1, path):
                return True

    # Backtrack
    visited[x][y] = False
    path.pop()
    return False


def iddfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    max_depth = rows * cols  # worst case

    for depth in range(max_depth + 1):
        visited = [[False]*cols for _ in range(rows)]
        path = []

        if dfs_limited(start[0], start[1], target, grid, visited, depth, path):
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", path)
            return

    print(f"Path not found at max depth {max_depth} using IDDFS")


# -------------------------
# Reading Input from User
# -------------------------

rows, cols = map(int, input().split())

grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))

sx, sy = map(int, input().replace("Start:", "").split())
tx, ty = map(int, input().replace("Target:", "").split())

start = (sx, sy)
target = (tx, ty)

iddfs(grid, start, target)
