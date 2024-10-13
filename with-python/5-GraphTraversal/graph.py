from collections import deque


class Graph:
    """Represent the graph with an adjacency list"""

    def __init__(self, directed=False):
        self.graph = {}
        self._directed = directed

    def add_edge(
        self,
        u,
        v,
    ):
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
        process_vertex_early,
        process_vertex_late,
        process_edge,
    ):
        # discovered: vertex found
        discovered = {vertex: False for vertex in self.graph}

        # processed: all edges connected to vertex have been checked
        processed = {vertex: False for vertex in self.graph}

        # discovery relation (can be used for path construction)
        parent = {vertex: None for vertex in self.graph}

        queue = deque([start])
        discovered[start] = True

        while queue:
            v = queue.popleft()
            process_vertex_early(v)
            processed[v] = True

            neighbors = self.graph.get(v, [])
            for y in neighbors:
                if not processed[y] or self._directed:
                    process_edge(v, y)

                if not discovered[y]:
                    queue.append(y)
                    discovered[y] = True
                    parent[y] = v

            process_vertex_late(v)


def process_vertex_early(v):
    print(f"Processed vertex early: {v}")


def process_edge(v, y):
    print(f"Processed edge ({v} -> {y})")


def process_vertex_late(v):
    return  # do nothing


# Usage:
def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.print()

    print("...Starting BFS...")
    g.bfs(
        start=1,
        process_vertex_early=process_vertex_early,
        process_edge=process_edge,
        process_vertex_late=process_vertex_late,
    )
    print("...End BFS...")


if __name__ == "__main__":
    main()
