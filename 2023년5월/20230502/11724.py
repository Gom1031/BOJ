import sys
sys.setrecursionlimit(10**9)

n, m = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
visited = [False] * (n+1)

def dfs(x, graph):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i, graph)
    return

for i in range(1,n+1):
    if visited[i] == False:
        result += 1
        dfs(i, graph)

print(result)