
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
    """

    # Initialize BFS data structures
    visited = set()
    parent = {}
    distance = {}
    cycle_edges = set()

    # Initialize the queue
    queue = deque([start])

    # Mark the starting vertex as visited
    visited.add(start)
    parent[start] = None
    distance[start] = 0

    # BFS traversal
    while queue:
        u = queue.popleft()

        for v in graph[u]:

            # Case 1: Vertex v has not been visited
            if v not in visited:
                visited.add(v)
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.append(v)

            # Case 2: Vertex v has already been visited
            elif parent[u] != v and parent[v] != u:

                # Store the undirected edge without duplication
                edge = frozenset((u, v))
                cycle_edges.add(edge)

    return {
        "parent": parent,
        "distance": distance,
        "cycle_edges": list(cycle_edges)
    }
