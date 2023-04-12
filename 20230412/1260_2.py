import sys
from collection import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)


n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort()

visited = [False] * (n+1)
dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)