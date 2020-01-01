from collections import deque
def bfs(graph,s):
    # graph is the directed graph as a dict
    # s is the starting vertex
    explored=set()
    queue=deque()
    explored.add(s)
    queue.append(s)
    while queue:
        v=queue.popleft()
        for neighbour in graph[v]:
            if neighbour not in explored:
                explored.add(neighbour)
                queue.append(neighbour)
    return explored
if __name__ == '__main__':
    graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    print (bfs(graph,'A'))
