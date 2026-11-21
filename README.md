# Shortest Cycle in an Undirected Graph

## Objective
Find and return the shortest cycle in an undirected graph using BFS from every vertex.

## Graph Representation
Adjacency List.

## Responsibilities
- Person 1: Graph representation and BFS.
- Person 2: Cycle reconstruction and testing.

## Agreed Interfaces

### graph.py
- create_graph()
- add_vertex()
- add_edge()
- get_neighbors()

### bfs.py
- bfs(graph, start)

### cycle.py
- get_tree_path(parent, u, v)
- reconstruct_cycle(parent, u, v)
- cycle_length(cycle)
- find_shortest_cycle(graph)
- validate_cycle(graph, cycle)

## Expected Output
A list of vertices representing the shortest cycle,
or None if no cycle exists.

## Complexity
To be established and justified after implementation.
