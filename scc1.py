from collections import defaultdict

import sys,threading
sys.setrecursionlimit(3000000)
threading.stack_size(67108864)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.graph_rev = defaultdict(list)
        self.visited_first = defaultdict(bool)
        self.visited_second = defaultdict(bool)
        self.s=int
        self.header=defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph_rev[v].append(u)
        self.visited_first[v] = False
        self.visited_second[u] = False

    def DFS_first(self, v, stack):
        self.visited_first[v] = True
        for j in list(self.graph_rev[v]):
            if self.visited_first[j] is False:
                self.DFS_first(j, stack)
        stack.append(v)

    def DFS_second(self, v):
        self.visited_second[v] = True
        # print(v,)
        for j in self.graph[v]:
            if self.visited_second[j] is False:
                self.DFS_second(j)
        self.header[self.s]=self.header[self.s]+1
    def scc(self):
        stack = []
        for num in list(self.graph_rev):
            if self.visited_first[num] is False:
                self.DFS_first(num, stack)
        # print('stack is ', stack)
        while stack:
            i = stack.pop()
            if self.visited_second[i] is False:
                self.s=i
                self.DFS_second(i)
                # print('\n')
        return (sorted(self.header.items(), key=lambda x: x[1]))


g = Graph(875714)
f = open('scc_test_case5.txt', 'r')
for line in f.readlines():
    u = (int(line.split(' ')[0]))
    v = (int(line.split(' ')[1]))
    g.add_edge(u, v)
f.close()
print('reading done')

'''
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)
'''
print(g.V)
# print((g.graph[1]))
# print(dict(g.graph_rev))
# print(dict(g.visited_first))
print(g.scc())
