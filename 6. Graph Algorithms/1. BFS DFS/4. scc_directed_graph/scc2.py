"""
Kosaraju's algorithm for finding strongly connected components
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def reverse(graph):
    new_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            new_graph[v].append(u)
    return new_graph


def first_pass(graph):
    seen = set()
    ordering = []

    def dfs(v):
        seen.add(v)
        for u in graph[v]:
            if u not in seen:
                dfs(u)
        ordering.append(v)

    for u in graph.keys():
        if u not in seen:
            dfs(u)
    return ordering


def second_pass(graph, ordering):
    seen = set()
    leader = defaultdict(list)

    def dfs(v, lead, leader):
        seen.add(v)
        for u in graph[v]:
            if u not in seen:
                dfs(u, lead, leader)
        leader[lead].append(v)

    # for u in reversed(ordering):
    # or
    while ordering:
        u = ordering.pop()
        if u not in seen:
            lead = u
            dfs(u, lead, leader)

    return leader


def kosaraju(graph):
    return second_pass(graph, first_pass(reverse(graph)))


def main():
    """
    Coursera sample graph
    """
    f = open('SCC.txt')
    graph = defaultdict(list)
    for line in f:
        u, v = line.strip().split()
        graph[u].append(v)
    sccs = kosaraju(graph).values()
    print(sccs)
    print(sorted(map(len, sccs))[::-1][:10])


def test():
    graph = {
        1: [2],
        2: [3, 5],
        3: [4],
        4: [6],
        5: [1],
        6: [3]
    }
    print(kosaraju(graph))


if __name__ == '__main__':
    main()
    graph = {
        1: [2],
        2: [3, 5],
        3: [4],
        4: [6],
        5: [1],
        6: [3]
    }
