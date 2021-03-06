class Node:
    def __init__(self, key):
        self.key = key
        # key is a mutable object, need to change
        self.neighbors: dict[Node, int] = {}

    def __str__(self):
        return f"{self.key} with {len(self.neighbors)} neighbor(s)"

    def add_neighbor(self, nbr, weight=1):
        self.neighbors[nbr] = weight


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}

    def __iter__(self):
        for node in self.nodes.values():
            for nbr in node.neighbors:
                yield node, nbr

    def add_node(self, key):
        self.nodes[key] = Node(key)
        return self.nodes[key]

    def get_node(self, key):
        if key in self.nodes:
            return self.nodes[key]
        else:
            return None

    def add_edge(self, key1, key2, weight=1):
        if key1 not in self.nodes:
            self.add_node(key1)
        if key2 not in self.nodes:
            self.add_node(key2)
        self.nodes[key1].add_neighbor(self.nodes[key2], weight)

    def print_edges(self):
        for key, node in self.nodes.items():
            for nbr in node.neighbors:
                print(f"{key} -> {nbr.key}")

    def clone(self):
        g = Graph()
        for key, node in self.nodes.items():
            for nbr, weight in node.neighbors.items():
                g.add_edge(key, nbr.key, weight)
        return g


def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 1)
    g.add_edge(1, 6)
    g.add_edge(6, 8)
    g.add_edge(8, 10)
    g.add_edge(10, 7)
    g.add_edge(7, 9)
    g.add_edge(9, 6)
    g.add_edge(7, 2)
    g.add_edge(3, 8)
    g.add_edge(9, 4)
    g.add_edge(5, 10)
    g.print_edges()


if __name__ == "__main__":
    main()

