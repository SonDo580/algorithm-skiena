from graph import Graph


def count_edges(g: Graph):
    edge_count = {"count": 0}

    def process_edge(v, y):
        edge_count["count"] += 1

    g.bfs(start=1, process_edge=process_edge)
    return edge_count["count"]


def find_shortest_path(g: Graph, start, end):
    # vertices are discovered in order of increasing distance from the root
    # -> the unique tree path from root to node x uses the smallest number of edges
    # -> this is also the shortest path if the graph is unweighted
    parent = g.bfs(start)
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def connected_components(g: Graph):
    # - there's a path between any pair of vertices in a connected component
    # - different connected components are disjoint

    discovered = {vertex: False for vertex in g.graph}
    component_number = 0
    components = []

    def process_vertex_early(v):
        components[-1].append(v)
        discovered[v] = True

    for vertex in g.graph:
        if not discovered[vertex]:
            component_number += 1
            components.append([])
            g.bfs(vertex, process_vertex_early=process_vertex_early)
            print(f"Component {component_number}: {components[-1]}")

    return components


def two_color(g: Graph):
    # a graph is bipartite if it can be colored using only 2 colors
    # such that no edge links 2 vertices of the same color

    BLACK = "BLACK"
    WHITE = "WHITE"

    bipartite = True
    color = {vertex: None for vertex in g.graph}

    def complement(c):
        if c == BLACK:
            return WHITE
        if c == WHITE:
            return BLACK

    def process_edge(v, y):
        nonlocal bipartite
        if color[v] == color[y]:
            bipartite = False
            print(f"Warning: not bipartite due to edge ({v}, {y})")
        color[y] = complement(color[v])

    for vertex in g.graph:
        if color[vertex] is None:
            color[vertex] = WHITE
            g.bfs(vertex, process_edge=process_edge)

    return bipartite


# Usage:
def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    # Diagram:
    # 1 - 2 - 4 - 5
    # |       |
    # 3-------'

    print(f"Number of edges: {count_edges(g)}\n")

    print(f"Shortest path from 1 to 4: {find_shortest_path(g, start=1, end=4)}\n")

    print(f"...Connected components...")
    components = connected_components(g)
    print(f"Total: {len(components)}\n")

    if two_color(g):
        print("Graph is bipartite")
    else:
        print("Graph is not bipartite")


if __name__ == "__main__":
    main()
