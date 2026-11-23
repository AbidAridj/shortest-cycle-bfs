
from src.graph import create_graph, add_vertex, add_edge, get_neighbors

# Create a graph
graph = create_graph(["A", "B", "C"])

# Add edges
add_edge(graph, "A", "B")
add_edge(graph, "A", "C")
add_edge(graph, "B", "C")

# Display the graph
print("Graph:", graph)

# Display neighbors of A
print("Neighbors of A:", get_neighbors(graph, "A"))

from src.bfs import bfs

result = bfs(graph, "A")

print("\nBFS starting from A:")
print("Parent:", result["parent"])
print("Distance:", result["distance"])
print("Cycle edges:", result["cycle_edges"])
