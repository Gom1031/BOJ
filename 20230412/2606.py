import sys
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)

    return visited

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i: set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

print(graph)

# infected = bfs(graph, 1)
# print(len(infected) - 1)  # 1번 컴퓨터는 제외하고 개수를 출력
