import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

result = []

def bfs(start):
    count = 1
    visited = [0] * (n+1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i]:
                continue
            count += 1
            visited[i] = count
            queue.append(i)
    return visited
            
print(*bfs(r)[1:], sep="\n")