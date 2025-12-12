import heapq

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        R, C = map(int, f.readline().split())
        grid = [list(map(int, f.readline().split())) for _ in range(R)]
        sr, sc = map(int, f.readline().split())
        tr, tc = map(int, f.readline().split())
    return R, C, grid, (sr, sc), (tr, tc)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(R, C, grid, start, target):
    sr, sc = start
    tr, tc = target

    # Priority queue: (f_cost, g_cost, (r, c))
    pq = []
    heapq.heappush(pq, (manhattan(start, target), 0, start))

    visited = set()
    parent = {}  # to reconstruct path

    while pq:
        f, g, (r, c) = heapq.heappop(pq)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        # Goal reached
        if (r, c) == (tr, tc):
            path = []
            cur = (r, c)
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            path.append(start)
            path.reverse()
            return path

        # Directions: Up, Down, Left, Right
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan((nr, nc), target)
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (new_f, new_g, (nr, nc)))

    return None  # No path found

def main():
    R, C, grid, start, target = read_input()
    path = astar(R, C, grid, start, target)

    if path is None:
        print("No path found.")
    else:
        print("Shortest path found:")
        for cell in path:
            print(cell)


if __name__ == "__main__":
    main()
