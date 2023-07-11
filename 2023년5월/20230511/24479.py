import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [0] * (n+1)
count = 1

def dfs(start):
    global count
    visited[start] = count
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(r)

print(*visited[1:], sep='\n')