import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
def bfs(v):
    queue = deque()
    visited[v] = 1
    queue.append(v)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[a] + 1

bfs(1)
result = 0

for i in range(2, n+1):
    if 0 < visited[i] < 4:
        result += 1

print(result)