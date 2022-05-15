from graph import Graph
from itertools import combinations


def word_ladder(lst: str):
    g = Graph()
    patterns: dict[str, list] = {}
    for word in lst:
        for i, _ in enumerate(word):
            pattern = word[:i] + "_" + word[i + 1 :]
            patterns.setdefault(pattern, []).append(word)

    for words in patterns.values():
        for w1, w2 in combinations(words, 2):
            g.add_edge(w1, w2)
            g.add_edge(w2, w1)

    return g


def word_ladder_bfs(graph: Graph, word):
    g: Graph = graph.clone()
    for node in g.nodes.values():
        node.dist = float("inf")
    node = graph.get_node(word)
    node.dist = 0
    queue = [node]

    while queue:
        node = queue.pop(0)
        for i in node.neighbors:
            if i.dist == float("inf"):
                i.dist = node.dist + 1
                queue.append(i)

    return g


def main():
    g = word_ladder(
        [
            "bass",
            "beat",
            "bent",
            "best",
            "pass",
            "past",
            "peat",
            "pest",
            "teat",
            "tent",
            "test",
        ]
    )
    # g.print_edges()

    bfs = word_ladder_bfs(g, "pass")
    for node, nbr in bfs:
        print(f"{node.key}, {node.dist} -> {nbr.key}, {nbr.dist}")


if __name__ == "__main__":
    main()

