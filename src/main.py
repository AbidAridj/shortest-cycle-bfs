from graph import create_graph, add_edge
from bfs import bfs
from cycle import find_shortest_cycle, validate_cycle, cycle_length


def test_case(nom, graph, longueur_attendue):
    print(f"--- {nom} ---")
    cycle = find_shortest_cycle(graph)
    longueur = cycle_length(cycle)

    if cycle is None:
        valide = True  # rien à valider si pas de cycle
    else:
        valide = validate_cycle(graph, cycle)

    print("Cycle trouvé :", cycle)
    print("Longueur     :", longueur)
    print("Valide       :", valide)

    ok = (longueur == longueur_attendue) and valide
    print("Résultat     :", "OK" if ok else "ECHEC (attendu:", longueur_attendue, ")")
    print()


if __name__ == "__main__":

    # 1. Triangle simple
    g1 = create_graph()
    add_edge(g1, "A", "B")
    add_edge(g1, "B", "C")
    add_edge(g1, "C", "A")
    test_case("Triangle", g1, 3)

    # 2. Carré simple
    g2 = create_graph()
    add_edge(g2, "A", "B")
    add_edge(g2, "B", "C")
    add_edge(g2, "C", "D")
    add_edge(g2, "D", "A")
    test_case("Carré", g2, 4)

    # 3. Arbre (aucun cycle)
    g3 = create_graph()
    add_edge(g3, "A", "B")
    add_edge(g3, "B", "C")
    add_edge(g3, "B", "D")
    test_case("Arbre sans cycle", g3, float("inf"))

    # 4. Graphe déconnecté avec un seul cycle
    g4 = create_graph()
    add_edge(g4, "A", "B")
    add_edge(g4, "B", "C")
    add_edge(g4, "C", "A")
    add_edge(g4, "X", "Y")
    test_case("Déconnecté avec cycle", g4, 3)

    # 5. Sommet partagé qui n'est pas la racine du BFS (teste le LCA)
    g5 = create_graph()
    add_edge(g5, "1", "2")
    add_edge(g5, "2", "3")
    add_edge(g5, "3", "1")
    add_edge(g5, "3", "4")
    add_edge(g5, "4", "5")
    add_edge(g5, "5", "6")
    add_edge(g5, "6", "3")
    test_case("Triangle + carré partageant un sommet non-racine", g5, 3)

    # 6. Test brut du BFS seul (pour voir parent/distance/cycle_edges)
    print("--- BFS brut sur le triangle ---")
    resultat = bfs(g1, "A")
    print("Parent      :", resultat["parent"])
    print("Distance    :", resultat["distance"])
    print("Cycle edges :", resultat["cycle_edges"])