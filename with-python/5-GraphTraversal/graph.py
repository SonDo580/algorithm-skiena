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

        def count_edges(v, y):
            edge_count["count"] += 1

        self.bfs(start=1, process_edge=count_edges)
        return edge_count["count"]

    def find_shortest_path(self, start, end):
        # - vertices are discovered in order of increasing distance from the root
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


# Usage:
def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.print()

    print("\n...Starting BFS...")
    g.bfs(
        start=1,
        process_vertex_early=lambda v: print(f"Processed vertex early: {v}"),
        process_edge=lambda v, y: print(f"Processed edge ({v} -> {y})"),
    )
    print("...End BFS...\n")

    print(f"Number of edges: {g.count_edges()}\n")
    print(f"Shortest path from 1 to 4: {g.find_shortest_path(1, 4)}\n")


if __name__ == "__main__":
    main()
