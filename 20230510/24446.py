# 트리의 모든 노드의 깊이를 출력
# 시작점 r의 깊이는 0이고 방문되지 않는 노드의 깊이는 -1

import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque()
    visited = [-1] * (n+1)
    visited[v] = 0
    queue.append(v)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] > -1:
                continue
            visited[i] = visited[now] + 1
            queue.append(i)
    return visited

print(*bfs(r)[1:], sep='\n')