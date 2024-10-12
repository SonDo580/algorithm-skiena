class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, directed = False):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

        if not directed:
            if v not in self.graph:
                self.graph[v] = set()
            self.graph[v].add(u)
    
    def print(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Usage:
def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.print()

if __name__ == "__main__":
    main()