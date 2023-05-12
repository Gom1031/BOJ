# 깊이 di 시작깊이 0 방문안된 노드는 -1
# 방문순서 ti 방문안된 노드 0
# 모든 노드에 대한 di * ti
# 정렬은 오름차순으로 방문

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

depth = [-1] * (n+1)
visited = [0] * (n+1)
count = 1

depth[r] = 0
visited[r] += count

def dfs(v):
    global visited, count
    for i in graph[v]:
        if depth[i] < 0 or visited[i] < 1:
            count += 1
            depth[i] = depth[v] + 1
            visited[i] += count
            dfs(i)
        # count += 1
        # if depth[i] < 0:
        #     depth[i] = depth[v] + 1
        #     dfs(i)

dfs(r)

# print(visited[1:], depth[1:])
sum = 0

for a, b in zip(visited[1:], depth[1:]):
    sum += a*b

print(sum)
