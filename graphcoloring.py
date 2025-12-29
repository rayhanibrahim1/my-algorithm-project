# ---------- Check if color is safe ----------
def is_safe(vertex, graph, colors, color):
    for adj in graph[vertex]:
        if colors[adj] == color:
            return False
    return True


# ---------- Backtracking Utility ----------
def graph_coloring_util(vertex, graph, colors, N, K):
    # If all vertices are colored
    if vertex == N:
        return True

    # Try all colors for current vertex
    for color in range(1, K + 1):
        if is_safe(vertex, graph, colors, color):
            colors[vertex] = color
            if graph_coloring_util(vertex + 1, graph, colors, N, K):
                return True
            colors[vertex] = 0  # Backtrack

    return False


# ---------- Graph Coloring Function ----------
def graph_coloring(N, edges, K):
    # Create adjacency list
    graph = {i: [] for i in range(N)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * N

    if graph_coloring_util(0, graph, colors, N, K):
        print(f"Coloring Possible with {K} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {K} Color")


# ---------- Read Input ----------
def read_input():
    N, M, K = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    return N, edges, K


# ---------- Main ----------
if __name__ == "__main__":
    N, edges, K = read_input()
    graph_coloring(N, edges, K)

