# i번 노드의 깊이를 di
# r의 깊이를 0, 방문되지 않은 노드의 깊이는 -1
# 방문순서를 ti라고 하자
# 시작의 순서는 1, 방문되지 않으면 0
# 모든 노드에 대한 di * ti
# 오름차순으로 방문한다

import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(v):
    result = 0

    cnt = 1
    depth = [-1] * (n+1)
    depth[v] = 0
    count = [0] * (n+1)
    count[v] = 1
    
    queue = deque([v])

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if depth[i] > -1 or count[i] > 0:
                continue
            cnt += 1
            depth[i] = depth[now] + 1
            count[i] += cnt
            queue.append(i)
    
    for a, b in zip(depth[1:], count[1:]):
        result += a * b
    
    return result

print(bfs(r))