
def create_graph(vertices=None):
    """
    Create an empty graph represented by an adjacency list.
    """
    if vertices is None:
        vertices = []

    graph = {}

    for vertex in vertices:
        graph[vertex] = []

    return graph


def add_vertex(graph, vertex):
    """
    Add a vertex if it does not already exist.
    """
    if vertex not in graph:
        graph[vertex] = []


def add_edge(graph, u, v):
    """
    Add an undirected edge between u and v.
    """
    add_vertex(graph, u)
    add_vertex(graph, v)

    if v not in graph[u]:
        graph[u].append(v)

    if u not in graph[v]:
        graph[v].append(u)


def get_neighbors(graph, vertex):
    """
    Return the neighbors of a vertex.
    """
    return graph.get(vertex, [])
