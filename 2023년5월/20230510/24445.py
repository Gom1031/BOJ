import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순 정렬
for i in graph:
    i.sort(reverse=True)

queue = deque([])

def bfs(v):
    count = 1
    visited = [0] * (n+1)
    queue.append(v)

    visited[v] = 1

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] > 0:
                continue
            count += 1
            visited[i] += count
            queue.append(i)

    return visited[1:]

print(*bfs(r), sep='\n')