from collections import deque


class Graph:
    """
    Represent the graph with an adjacency list.
    """

    def __init__(self, directed=False):
        self.graph = {}
        self._directed = directed

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

        if not self._directed:
            if v not in self.graph:
                self.graph[v] = set()
            self.graph[v].add(u)

    def print(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def bfs(
        self,
        start,
        process_vertex_early=None,
        process_vertex_late=None,
        process_edge=None,
    ):
        # discovered: vertex found
        discovered = {vertex: False for vertex in self.graph}

        # processed: all edges connected to vertex have been checked
        processed = {vertex: False for vertex in self.graph}

        # discovery relation
        parent = {vertex: None for vertex in self.graph}

        queue = deque([start])
        discovered[start] = True

        while queue:
            v = queue.popleft()
            if process_vertex_early:
                process_vertex_early(v)
            processed[v] = True

            neighbors = self.graph.get(v, [])
            for y in neighbors:
                if not processed[y] or self._directed:
                    if process_edge:
                        process_edge(v, y)

                if not discovered[y]:
                    queue.append(y)
                    discovered[y] = True
                    parent[y] = v

            if process_vertex_late:
                process_vertex_late(v)

        return parent  # used for path construction

    def count_edges(self):
        edge_count = {"count": 0}

        def process_edge(v, y):
            edge_count["count"] += 1

        self.bfs(start=1, process_edge=process_edge)
        return edge_count["count"]

    def find_shortest_path(self, start, end):
        # vertices are discovered in order of increasing distance from the root
        # -> the unique tree path from root to node x uses the smallest number of edges
        # -> this is also the shortest path if the graph is unweighted
        parent = self.bfs(start)
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path

    def connected_components(self):
        # - there's a path between any pair of vertices in a connected component
        # - different connected components are disjoint

        discovered = {vertex: False for vertex in self.graph}
        component_number = 0
        components = []

        def process_vertex_early(v):
            components[-1].append(v)
            discovered[v] = True

        for vertex in self.graph:
            if not discovered[vertex]:
                component_number += 1
                components.append([])
                self.bfs(vertex, process_vertex_early=process_vertex_early)
                print(f"Component {component_number}: {components[-1]}")

        return components

    def two_color(self):
        # a graph is bipartite if it can be colored using only 2 colors
        # such that no edge links 2 vertices of the same color

        BLACK = "BLACK"
        WHITE = "WHITE"

        bipartite = True
        color = {vertex: None for vertex in self.graph}

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

        for vertex in self.graph:
            if color[vertex] is None:
                color[vertex] = WHITE
                self.bfs(vertex, process_edge=process_edge)

        return bipartite


# Usage:
def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.print()

    # Diagram:
    # 1 - 2 - 4 - 5
    # |       |
    # 3-------'

    print("\n...Starting BFS...")
    g.bfs(
        start=1,
        process_vertex_early=lambda v: print(f"Processed vertex early: {v}"),
        process_edge=lambda v, y: print(f"Processed edge ({v} -> {y})"),
    )
    print()

    print(f"Number of edges: {g.count_edges()}\n")

    print(f"Shortest path from 1 to 4: {g.find_shortest_path(1, 4)}\n")

    print(f"...Connected components...")
    g.connected_components()
    print()

    is_bipartite = g.two_color()
    if is_bipartite:
        print("Graph is bipartite")
    else:
        print("Graph is not bipartite")


if __name__ == "__main__":
    main()
