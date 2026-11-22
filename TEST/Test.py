# test_cycle.py

import pytest
from graph import create_graph, add_edge
from cycle import find_shortest_cycle, validate_cycle, cycle_length


def test_triangle_and_square_sharing_A():
    """
    Cas simple : le LCA coïncide avec un sommet qui peut être choisi
    comme racine de BFS (A). Vérifie le comportement de base.
    """
    graph = create_graph()
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "C")
    add_edge(graph, "C", "A")
    add_edge(graph, "A", "D")
    add_edge(graph, "D", "E")
    add_edge(graph, "E", "F")
    add_edge(graph, "F", "A")

    cycle = find_shortest_cycle(graph)

    assert cycle is not None
    assert cycle_length(cycle) == 3
    assert validate_cycle(graph, cycle)


def test_triangle_and_square_sharing_non_root_vertex():
    """
    Cas piège : le sommet partagé (3) N'EST PAS la racine du BFS
    dans certains appels. Ça force reconstruct_cycle à calculer un LCA
    non trivial (pas juste l'indice 0). C'est le test qui valide
    réellement ta logique de LCA, contrairement au test précédent.
    """
    graph = create_graph()
    add_edge(graph, "1", "2")
    add_edge(graph, "2", "3")
    add_edge(graph, "3", "1")
    add_edge(graph, "3", "4")
    add_edge(graph, "4", "5")
    add_edge(graph, "5", "6")
    add_edge(graph, "6", "3")

    cycle = find_shortest_cycle(graph)

    assert cycle is not None
    assert cycle_length(cycle) == 3   # le triangle 1-2-3 est le plus court
    assert validate_cycle(graph, cycle)


def test_simple_square_only():
    """
    Cas de base sans ambiguïté : un seul cycle possible, longueur 4.
    Sert de garde-fou si jamais un futur changement casse le cas simple.
    """
    graph = create_graph()
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "C")
    add_edge(graph, "C", "D")
    add_edge(graph, "D", "A")

    cycle = find_shortest_cycle(graph)

    assert cycle is not None
    assert cycle_length(cycle) == 4
    assert validate_cycle(graph, cycle)


def test_no_cycle_tree_graph():
    """
    Graphe sans aucun cycle (un arbre). find_shortest_cycle doit
    renvoyer None, pas planter ni renvoyer un résultat inventé.
    """
    graph = create_graph()
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "C")
    add_edge(graph, "B", "D")

    cycle = find_shortest_cycle(graph)

    assert cycle is None


def test_disconnected_graph_with_one_cycle():
    """
    Deux composantes connexes séparées : seule l'une des deux contient
    un cycle. Vérifie que la boucle externe (BFS depuis chaque sommet)
    couvre bien les deux composantes et ne rate pas le cycle isolé
    dans l'une d'elles.
    """
    graph = create_graph()
    # Composante 1 : un cycle
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "C")
    add_edge(graph, "C", "A")
    # Composante 2 : juste une arête, pas de cycle
    add_edge(graph, "X", "Y")

    cycle = find_shortest_cycle(graph)

    assert cycle is not None
    assert cycle_length(cycle) == 3
    assert validate_cycle(graph, cycle)


def test_validate_cycle_rejects_invalid_cycle():
    """
    validate_cycle doit rejeter un cycle inventé qui ne correspond
    à aucune arête réelle du graphe — teste validate_cycle isolément,
    pas via find_shortest_cycle.
    """
    graph = create_graph()
    add_edge(graph, "A", "B")
    add_edge(graph, "B", "C")
    add_edge(graph, "C", "A")

    fake_cycle = ["A", "C", "B"]  # C-B n'existe que dans un sens correct ; testons un vrai faux cas
    broken_cycle = ["A", "B", "X"]  # X n'existe pas dans le graphe

    assert validate_cycle(graph, broken_cycle) is False


def test_validate_cycle_rejects_too_short_list():
    """
    Un 'cycle' de moins de 3 sommets n'est pas un cycle valide.
    """
    graph = create_graph()
    add_edge(graph, "A", "B")

    assert validate_cycle(graph, ["A", "B"]) is False
    assert validate_cycle(graph, None) is False


def test_cycle_length_on_none():
    """
    cycle_length(None) doit renvoyer l'infini, pas planter —
    utilisé comme sentinel dans find_shortest_cycle.
    """
    assert cycle_length(None) == float('inf')