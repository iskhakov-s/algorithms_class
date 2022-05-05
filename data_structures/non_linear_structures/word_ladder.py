from graph import Graph
from itertools import combinations


def word_ladder(lst: str):
    g = Graph()
    patterns: dict[str, list] = {}
    for word in lst:
        for i, _ in enumerate(word):
            pattern = word[:i] + '_' + word[i + 1:]
            patterns.setdefault(pattern, []).append(word)
            
    for words in patterns.values():
        for w1, w2 in combinations(words, 2):
            g.add_edge(w1, w2)
            g.add_edge(w2, w1)
            
    return g


def main():
    g1 = word_ladder(['bass', 'beat', 'bent', 'best', 'pass', 'past', 'peat', 'pest', 'teat', 'tent', 'test'])
    g1.print_edges()


if __name__ == '__main__':
    main()
    