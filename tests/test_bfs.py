
from src.graph import create_graph, add_edge
from src.bfs import bfs


# TEST 1: Graph without a cycle
print("TEST 1: Graph without a cycle")

graph1 = create_graph(["A", "B", "C"])
add_edge(graph1, "A", "B")
add_edge(graph1, "B", "C")

result1 = bfs(graph1, "A")

print("Parent:", result1["parent"])
print("Distance:", result1["distance"])
print("Cycle edges:", result1["cycle_edges"])


# TEST 2: Graph with a triangle
print("\nTEST 2: Graph with a triangle")

graph2 = create_graph(["A", "B", "C"])
add_edge(graph2, "A", "B")
add_edge(graph2, "B", "C")
add_edge(graph2, "C", "A")

result2 = bfs(graph2, "A")

print("Parent:", result2["parent"])
print("Distance:", result2["distance"])
print("Cycle edges:", result2["cycle_edges"])


# TEST 3: Disconnected graph
print("\nTEST 3: Disconnected graph")

graph3 = create_graph(["A", "B", "C", "D"])
add_edge(graph3, "A", "B")
add_edge(graph3, "C", "D")

result3 = bfs(graph3, "A")

print("Parent:", result3["parent"])
print("Distance:", result3["distance"])
print("Cycle edges:", result3["cycle_edges"])

print("\nTEST 4: Graph with multiple cycles")

graph4 = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

result = bfs(graph4, "A")

print("Parent:", result["parent"])
print("Distance:", result["distance"])
print("Cycle edges:", result["cycle_edges"])


print("\nTEST 5: Disconnected graph with a cycle")

graph5 = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D", "E"],
    "D": ["C", "E"],
    "E": ["C", "D"]
}

result = bfs(graph5, "A")

print("BFS from A:")
print("Parent:", result["parent"])
print("Distance:", result["distance"])
print("Cycle edges:", result["cycle_edges"])

result = bfs(graph5, "C")

print("\nBFS from C:")
print("Parent:", result["parent"])
print("Distance:", result["distance"])
print("Cycle edges:", result["cycle_edges"])

