import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

depth = [-1] * (n+1)
visited = [0] * (n+1)

depth[r] = 0
count = 1
visited[r] += count

def dfs(v):
    global depth, visited, count
    for i in graph[v]:
        if depth[i] < 0 or visited[i] < 1:
            count += 1
            depth[i] = depth[v] + 1
            visited[i] += count
            dfs(i)

dfs(r)

sum = 0

for a, b in zip(visited[1:], depth[1:]):
    sum += a*b

print(sum)