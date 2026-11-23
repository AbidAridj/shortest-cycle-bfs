from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) starting from a given vertex.

    Parameters:
        graph: Graph represented by an adjacency list.
        start: Starting vertex.

    Returns:
        A dictionary containing:
            - parent: BFS parent of each visited vertex.
            - distance: Distance from the starting vertex.
            - cycle_edges: Non-tree edges detected during BFS.

    Complexité : O(V + E) — chaque sommet et chaque arête du graphe
    (ou de sa composante connexe) est visité au plus une fois.
    """

    visited = set()
    parent = {}
    distance = {}
    cycle_edges = set()

    queue = deque([start])

    visited.add(start)
    parent[start] = start   # <-- correction : la racine est son propre parent
                             #     (convention attendue par cycle.py::get_tree_path,
                             #      qui s'arrête quand parent[current] == current)
    distance[start] = 0

    while queue:
        u = queue.popleft()

        for v in graph[u]:

            if v not in visited:
                visited.add(v)
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.append(v)

            elif parent[u] != v and parent[v] != u:
                edge = frozenset((u, v))
                cycle_edges.add(edge)

    return {
        "parent": parent,
        "distance": distance,
        "cycle_edges": list(cycle_edges)
    }