def get_tree_path(parent, start_root_hint, u):
    """
    Remonte de u jusqu'à la racine en suivant parent[].
    Renvoie le chemin dans l'ordre [racine, ..., u].
    """
    path = []
    current = u

    while True:
        path.append(current)

        if parent[current] == current:
            break

        current = parent[current]

    path.reverse()
    return path


def reconstruct_cycle(parent, u, v):
    """
    Reconstruit un cycle à partir d'une cross edge (u, v).
    """

    # Récupérer les chemins de la racine vers u et v
    path_u = get_tree_path(parent, None, u)
    path_v = get_tree_path(parent, None, v)

    # Trouver le dernier ancêtre commun (LCA)
    i = 0

    while i < min(len(path_u), len(path_v)) and path_u[i] == path_v[i]:
        i += 1

    # Revenir à l'indice du dernier ancêtre commun
    i -= 1

    # Construire le cycle sans dupliquer le LCA
    cycle = path_u[i:] + path_v[i+1:][::-1]

    return cycle


def cycle_length(cycle):
    """
    Retourne la longueur du cycle.
    """
    if cycle is None:
        return float('inf')

    return len(cycle)


def find_shortest_cycle(graph):
    """
    Trouve le cycle le plus court dans un graphe non orienté
    en exécutant BFS depuis chaque sommet.
    """

    from bfs import bfs

    best_cycle = None
    best_len = float('inf')

    # Parcourir tous les sommets du graphe
    for vertex in graph:

        # Effectuer BFS depuis le sommet courant
        result = bfs(graph, vertex)

        parent = result["parent"]
        cycle_edges = result["cycle_edges"]

        # Examiner toutes les arêtes non présentes dans l'arbre BFS
        for edge in cycle_edges:

            u, v = tuple(edge)

            # Reconstruire le cycle correspondant
            cycle = reconstruct_cycle(parent, u, v)

            # Vérifier si ce cycle est plus court
            if cycle_length(cycle) < best_len:
                best_len = cycle_length(cycle)
                best_cycle = cycle

    return best_cycle


def validate_cycle(graph, cycle):
    """
    Vérifie si le cycle est valide dans le graphe.
    """

    from graph import get_neighbors

    if cycle is None or len(cycle) < 3:
        return False

    # Vérifier chaque arête du cycle, y compris la dernière
    for i in range(len(cycle)):
        a = cycle[i]
        b = cycle[(i + 1) % len(cycle)]

        if b not in get_neighbors(graph, a):
            return False

    # Vérifier que les sommets ne sont pas répétés
    if len(set(cycle)) != len(cycle):
        return False

    return True