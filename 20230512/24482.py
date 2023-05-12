# 깊이 출력
# 시작 정점의 깊이는 0 방문안한 정점의 깊이는 -1

import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순 정렬
for i in graph:
    i.sort(reverse=True)

visited = [-1] * (n+1)
count = 1
visited[r] = 0

def dfs(v):
    for i in graph[v]:
        if visited[i] < 0:
            visited[i] = visited[v] + 1
            dfs(i)
dfs(r)

print(*visited[1:], sep='\n')